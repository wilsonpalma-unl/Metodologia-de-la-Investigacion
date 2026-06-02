# -*- coding: utf-8 -*-
"""
Genera un único archivo .bib a partir de una lista de DOI.

Estrategia de recuperación de metadatos:
1) Crossref REST API
2) OpenAlex
3) Landing page del DOI (meta tags, JSON-LD y heurísticas HTML)

Dependencias:
    pip install requests beautifulsoup4 lxml
"""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

# =========================
# CONFIGURACIÓN
# =========================

DOIS = [
    "10.1007/3-540-45683-x_45",
    "10.1007/978-3-540-30586-6_76",
    "10.1007/978-3-540-71496-5_73",
    "10.1007/11871637_49",
    "10.1007/11735106_17",
    "10.1016/j.eswa.2008.06.054",
    "10.1016/j.proeng.2011.08.404",
    "10.1016/j.patrec.2015.07.028",
    "10.1016/j.patrec.2008.11.013",
    "10.1016/j.knosys.2016.02.017",
    "10.1016/j.engappai.2016.02.002",
    "10.1016/j.asoc.2020.106652",
    "10.1016/j.knosys.2010.04.004",
    "10.1016/j.neucom.2018.07.002",
    "10.5555/1619645.1619732",
]

OUTPUT_BIB = "articulos.bib"

# Opcional: si quieres ser más “polite” con OpenAlex, coloca tu correo.
# OPENALEX_MAILTO = "tu_correo@dominio.com"
OPENALEX_MAILTO = None

USER_AGENT = "BibGenerator/2.0 (mailto:example@example.com)"

SESSION = requests.Session()
SESSION.headers.update(
    {
        "User-Agent": USER_AGENT,
        "Accept": "application/json, text/html;q=0.9, */*;q=0.8",
    }
)

# =========================
# UTILIDADES GENERALES
# =========================

def normalize_doi(doi: str) -> str:
    return doi.strip().lower()

def doi_path(doi: str) -> str:
    return quote(normalize_doi(doi), safe="")

def clean_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()

def clean_abstract_text(text: str) -> str:
    """
    Limpia abstracts que pueden venir con JATS/XML/HTML.
    """
    if not text:
        return ""

    text = html.unescape(text)
    # Quita tags XML/HTML
    text = re.sub(r"<[^>]+>", " ", text)
    text = clean_whitespace(text)
    return text

def bibtex_escape(value: str) -> str:
    """
    Escapa caracteres problemáticos para BibTeX.
    No altera Unicode; lo importante es escapar símbolos especiales.
    """
    if value is None:
        return ""

    replacements = {
        "\\": r"\\",
        "{": r"\{",
        "}": r"\}",
        "%": r"\%",
        "&": r"\&",
        "#": r"\#",
        "_": r"\_",
        "$": r"\$",
    }
    for k, v in replacements.items():
        value = value.replace(k, v)
    return value

def first_nonempty(*values: Optional[str]) -> str:
    for v in values:
        if v and str(v).strip():
            return str(v).strip()
    return ""

def safe_get(dct: Any, *keys, default=None):
    cur = dct
    for k in keys:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return default
    return cur

# =========================
# OPENALEX
# =========================

def openalex_abstract_from_index(index: Optional[dict]) -> str:
    """
    Convierte abstract_inverted_index a texto plano.
    OpenAlex guarda el abstract como índice invertido, no como texto plano.
    """
    if not index or not isinstance(index, dict):
        return ""

    positions = {}
    for word, idxs in index.items():
        if not isinstance(idxs, list):
            continue
        for idx in idxs:
            positions[idx] = word

    if not positions:
        return ""

    return clean_whitespace(" ".join(positions[i] for i in sorted(positions)))

def fetch_openalex(doi: str) -> dict:
    """
    Intenta recuperar el work desde OpenAlex por DOI.
    Primero usa el endpoint de un solo work; si falla, usa filter exacto.
    """
    doi_n = normalize_doi(doi)

    # Intento 1: endpoint single work
    full_id = f"https://doi.org/{doi_n}"
    encoded_full_id = quote(full_id, safe="")
    url_1 = f"https://api.openalex.org/works/{encoded_full_id}"
    params = {}
    if OPENALEX_MAILTO:
        params["mailto"] = OPENALEX_MAILTO

    try:
        r = SESSION.get(url_1, params=params, timeout=30)
        if r.ok:
            return r.json()
    except Exception:
        pass

    # Intento 2: filter exacto
    url_2 = "https://api.openalex.org/works"
    params = {"filter": f"doi:{doi_n}"}
    if OPENALEX_MAILTO:
        params["mailto"] = OPENALEX_MAILTO

    try:
        r = SESSION.get(url_2, params=params, timeout=30)
        if r.ok:
            data = r.json()
            results = data.get("results", [])
            if results:
                return results[0]
    except Exception:
        pass

    return {}

# =========================
# CROSSREF
# =========================

def fetch_crossref(doi: str) -> dict:
    """
    Recupera metadatos desde Crossref.
    """
    url = f"https://api.crossref.org/works/{doi_path(doi)}"
    try:
        r = SESSION.get(url, timeout=30)
        if r.ok:
            payload = r.json()
            return payload.get("message", {}) or {}
    except Exception:
        pass
    return {}

def crossref_abstract_to_text(abstract: Optional[str]) -> str:
    """
    Crossref puede devolver abstract en JATS/XML.
    """
    if not abstract:
        return ""
    # Intento parsear como XML; si no cuadra, cae al limpiado simple.
    try:
        soup = BeautifulSoup(abstract, "lxml-xml")
        extracted = clean_whitespace(" ".join(soup.stripped_strings))
        if extracted:
            return extracted
    except Exception:
        pass
    return clean_abstract_text(abstract)

# =========================
# LNDING PAGE DEL DOI
# =========================

def fetch_doi_landing_html(doi: str) -> tuple[str, str]:
    """
    Resuelve el DOI a su landing page y devuelve (url_final, html).
    """
    url = f"https://doi.org/{doi_path(doi)}"
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    try:
        r = SESSION.get(url, headers=headers, timeout=30, allow_redirects=True)
        ctype = (r.headers.get("Content-Type") or "").lower()
        if r.ok and ("text/html" in ctype or "application/xhtml+xml" in ctype or "<html" in r.text.lower()):
            return r.url, r.text
    except Exception:
        pass
    return "", ""

def extract_meta_content(soup: BeautifulSoup, names: list[str]) -> str:
    """
    Busca contenido en <meta name="..."> o <meta property="...">.
    """
    for name in names:
        tag = soup.find("meta", attrs={"name": name})
        if tag and tag.get("content"):
            val = clean_whitespace(tag.get("content", ""))
            if val:
                return val

        tag = soup.find("meta", attrs={"property": name})
        if tag and tag.get("content"):
            val = clean_whitespace(tag.get("content", ""))
            if val:
                return val

    return ""

def extract_jsonld_abstract(soup: BeautifulSoup) -> str:
    """
    Busca abstract/description dentro de JSON-LD.
    """
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = script.string or script.get_text(strip=True)
        if not raw:
            continue
        try:
            data = json.loads(raw)
        except Exception:
            continue

        def walk(obj):
            if isinstance(obj, dict):
                # Prioridad al campo abstract explícito
                for key in ("abstract", "description"):
                    val = obj.get(key)
                    if isinstance(val, str) and len(clean_whitespace(val)) > 60:
                        return clean_whitespace(val)
                for v in obj.values():
                    found = walk(v)
                    if found:
                        return found
            elif isinstance(obj, list):
                for item in obj:
                    found = walk(item)
                    if found:
                        return found
            return ""

        found = walk(data)
        if found:
            return found

    return ""

def extract_heading_based_abstract(soup: BeautifulSoup) -> str:
    """
    Heurística común: buscar un heading 'Abstract' y capturar el bloque siguiente.
    """
    heading_names = {"abstract", "resumen", "summary", "abstracto"}

    # 1) Buscar nodos con id/class que contengan abstract
    for tag in soup.find_all(True):
        tid = " ".join(tag.get("class", [])) + " " + str(tag.get("id", ""))
        if re.search(r"abstract|resumen|summary", tid, flags=re.I):
            txt = clean_whitespace(tag.get_text(" ", strip=True))
            if len(txt) > 80:
                return txt

    # 2) Buscar headings y tomar contenido cercano
    for h in soup.find_all(re.compile(r"^h[1-6]$")):
        title = clean_whitespace(h.get_text(" ", strip=True)).lower()
        if title in heading_names:
            chunks = []
            for sib in h.find_next_siblings():
                if sib.name and re.match(r"^h[1-6]$", sib.name):
                    break
                text = clean_whitespace(sib.get_text(" ", strip=True))
                if text:
                    chunks.append(text)
            candidate = clean_whitespace(" ".join(chunks))
            if len(candidate) > 80:
                return candidate

    return ""

def extract_landing_abstract(html_text: str) -> str:
    """
    Intenta extraer abstract desde landing page del editor.
    Orden:
    - meta abstract explícito
    - JSON-LD
    - heurística por headings/secciones
    - description/og:description como último recurso
    """
    if not html_text:
        return ""

    soup = BeautifulSoup(html_text, "lxml")

    # Meta tags explícitos de abstract/resumen
    explicit = extract_meta_content(
        soup,
        [
            "citation_abstract",
            "prism.abstract",
            "dc.Description",
            "dc.description",
            "description",
        ],
    )
    if len(explicit) > 80:
        return explicit

    # JSON-LD
    jld = extract_jsonld_abstract(soup)
    if len(jld) > 80:
        return jld

    # Secciones / headings
    sec = extract_heading_based_abstract(soup)
    if len(sec) > 80:
        return sec

    # Último recurso: description social/meta
    fallback = extract_meta_content(
        soup,
        [
            "og:description",
            "twitter:description",
        ],
    )
    if len(fallback) > 120:
        return fallback

    return ""

# =========================
# MERGE DE METADATOS
# =========================

def authors_from_crossref(meta: dict) -> str:
    authors = meta.get("author") or []
    out = []
    for a in authors:
        family = clean_whitespace(a.get("family", ""))
        given = clean_whitespace(a.get("given", ""))
        if family and given:
            out.append(f"{family}, {given}")
        elif family:
            out.append(family)
        elif given:
            out.append(given)
    return " and ".join(out)

def authors_from_openalex(meta: dict) -> str:
    auths = meta.get("authorships") or []
    out = []
    for a in auths:
        author = a.get("author") or {}
        name = clean_whitespace(author.get("display_name", ""))
        if name:
            parts = [p.strip() for p in name.split(",")]
            if len(parts) >= 2:
                out.append(f"{parts[0]}, {parts[1]}")
            else:
                out.append(name)
    return " and ".join(out)

def year_from_crossref(meta: dict) -> str:
    for path in (
        ("published-print", "date-parts"),
        ("published-online", "date-parts"),
        ("created", "date-parts"),
        ("issued", "date-parts"),
    ):
        dp = safe_get(meta, *path)
        if isinstance(dp, list) and dp and dp[0]:
            return str(dp[0][0])
    return ""

def year_from_openalex(meta: dict) -> str:
    y = meta.get("publication_year")
    return str(y) if y else ""

def venue_from_crossref(meta: dict, entry_type: str) -> str:
    ct = meta.get("container-title") or []
    if ct and isinstance(ct, list) and ct[0]:
        return clean_whitespace(ct[0])
    return ""

def venue_from_openalex(meta: dict) -> str:
    return clean_whitespace(
        safe_get(meta, "primary_location", "source", "display_name", default="")
        or safe_get(meta, "host_venue", "display_name", default="")
        or ""
    )

def pages_from_crossref(meta: dict) -> str:
    return clean_whitespace(meta.get("page", ""))

def pages_from_openalex(meta: dict) -> str:
    biblio = meta.get("biblio") or {}
    first_page = clean_whitespace(biblio.get("first_page", ""))
    last_page = clean_whitespace(biblio.get("last_page", ""))
    if first_page and last_page:
        return f"{first_page}--{last_page}"
    return first_page or last_page or ""

def map_entry_type(crossref_type: str, openalex_type: str = "") -> str:
    t = (crossref_type or openalex_type or "").lower()

    mapping = {
        "journal-article": "article",
        "proceedings-article": "inproceedings",
        "book-chapter": "incollection",
        "book": "book",
        "reference-entry": "incollection",
        "posted-content": "misc",
        "report": "techreport",
        "dissertation": "phdthesis",
        "dataset": "misc",
        "peer-review": "misc",
    }
    return mapping.get(t, "article")

def make_bib_key(doi: str, title: str, year: str, authors: str) -> str:
    """
    Clave estable y razonablemente humana.
    """
    doi_tail = re.sub(r"[^A-Za-z0-9]+", "", doi.split("/")[-1])[:8]
    title_words = re.findall(r"[A-Za-z0-9]+", title or "")
    short_title = title_words[0] if title_words else "ref"
    surname = "ref"
    if authors:
        first_author = authors.split(" and ")[0]
        surname = first_author.split(",")[0].strip() if "," in first_author else first_author.split()[0].strip()
        surname = re.sub(r"[^A-Za-z0-9]+", "", surname) or "ref"
    year = year or "nd"
    return f"{surname}{year}_{short_title}_{doi_tail}"

@dataclass
class Record:
    doi: str
    entry_type: str
    key: str
    fields: dict[str, str]

def collect_record(doi: str) -> Record:
    doi_n = normalize_doi(doi)

    crossref = fetch_crossref(doi_n)
    openalex = fetch_openalex(doi_n)

    # Landing page sólo si hace falta
    landing_url = ""
    landing_html = ""

    # Campos base desde Crossref
    title = first_nonempty(
        (crossref.get("title") or [""])[0] if crossref.get("title") else "",
        openalex.get("display_name", ""),
    )

    year = first_nonempty(
        year_from_crossref(crossref),
        year_from_openalex(openalex),
    )

    authors = first_nonempty(
        authors_from_crossref(crossref),
        authors_from_openalex(openalex),
    )

    entry_type = map_entry_type(crossref.get("type", ""), openalex.get("type", ""))

    venue = first_nonempty(
        venue_from_crossref(crossref, entry_type),
        venue_from_openalex(openalex),
    )

    volume = first_nonempty(crossref.get("volume", ""), safe_get(openalex, "biblio", "volume", default=""))
    number = first_nonempty(crossref.get("issue", ""), safe_get(openalex, "biblio", "issue", default=""))
    pages = first_nonempty(pages_from_crossref(crossref), pages_from_openalex(openalex))
    publisher = first_nonempty(crossref.get("publisher", ""), safe_get(openalex, "primary_location", "source", "publisher", default=""))
    doi_field = first_nonempty(crossref.get("DOI", ""), openalex.get("doi", ""), doi_n)
    url = first_nonempty(crossref.get("URL", ""), openalex.get("id", ""), f"https://doi.org/{doi_n}")

    # Abstract: Crossref -> OpenAlex -> landing page
    abstract = clean_abstract_text(crossref_abstract_to_text(crossref.get("abstract", "")))

    if not abstract:
        oa_abstract = openalex_abstract_from_index(openalex.get("abstract_inverted_index"))
        if oa_abstract:
            abstract = oa_abstract

    if not abstract:
        landing_url, landing_html = fetch_doi_landing_html(doi_n)
        if landing_html:
            abstract = extract_landing_abstract(landing_html)

    # Keywords / subjects
    keywords = ""
    subject = crossref.get("subject") or []
    if isinstance(subject, list) and subject:
        keywords = ", ".join([clean_whitespace(str(s)) for s in subject if clean_whitespace(str(s))])

    # Campos para BibTeX
    fields: dict[str, str] = {}

    if title:
        fields["title"] = title
    if authors:
        fields["author"] = authors
    if year:
        fields["year"] = year
    if venue:
        fields["journal" if entry_type == "article" else "booktitle"] = venue
    if volume:
        fields["volume"] = volume
    if number:
        fields["number"] = number
    if pages:
        fields["pages"] = pages
    if publisher:
        fields["publisher"] = publisher
    if doi_field:
        fields["doi"] = doi_field
    if url:
        fields["url"] = url
    if abstract:
        fields["abstract"] = abstract
    if keywords:
        fields["keywords"] = keywords

    key = make_bib_key(doi_n, title, year, authors)

    return Record(
        doi=doi_n,
        entry_type=entry_type,
        key=key,
        fields=fields,
    )

# =========================
# BIBTEX
# =========================

def render_bibtex(record: Record) -> str:
    lines = [f"@{record.entry_type}{{{record.key},"]

    # Orden deseado de campos
    preferred_order = [
        "author",
        "title",
        "journal",
        "booktitle",
        "year",
        "volume",
        "number",
        "pages",
        "publisher",
        "doi",
        "url",
        "abstract",
        "keywords",
    ]

    used = set()

    for field in preferred_order:
        if field in record.fields and record.fields[field]:
            value = bibtex_escape(record.fields[field])
            lines.append(f"  {field} = {{{value}}},")
            used.add(field)

    # Cualquier campo extra
    for field, value in record.fields.items():
        if field in used or not value:
            continue
        lines.append(f"  {field} = {{{bibtex_escape(value)}}},")

    if len(lines) > 1:
        lines[-1] = lines[-1].rstrip(",")

    lines.append("}")
    return "\n".join(lines)

def generate_bib(dois: list[str], output_path: str = OUTPUT_BIB) -> None:
    seen = set()
    entries = []

    for doi in dois:
        doi_n = normalize_doi(doi)
        if doi_n in seen:
            continue
        seen.add(doi_n)

        print(f"Procesando: {doi_n}")
        try:
            record = collect_record(doi_n)
            entry = render_bibtex(record)
            entries.append(entry)
        except Exception as exc:
            print(f"[WARN] No se pudo procesar {doi_n}: {exc}")

    content = "\n\n".join(entries) + "\n"
    Path(output_path).write_text(content, encoding="utf-8")
    print(f"\nArchivo generado: {output_path}")

if __name__ == "__main__":
    generate_bib(DOIS, OUTPUT_BIB)