# prompt1
En los entregables de la siguiente actividad, ¿A qué se refiere con Estado del arte inicial?

```markdown
# ACD 6: Búsqueda Avanzada, Cadenas de Búsqueda y Antecedentes

## Objetivo

Dominar la búsqueda avanzada en bases de datos, construir cadenas de búsqueda y redactar antecedentes.

## Contenidos

- Palabras clave y tesauros.
- Cadenas booleanas.
- Filtros y criterios.
- Scopus.
- IEEE Xplore.
- ACM Digital Library.
- Google Scholar.
- Literatura gris.
- Estado del arte.

## Procedimiento

1. Demostración en vivo: búsqueda avanzada en Scopus e IEEE Xplore (25 min).
2. Taller: construcción de cadena de búsqueda personal (25 min).
3. Exportación a Mendeley/Zotero (15 min).
4. Redacción guiada de un párrafo de antecedentes (20 min).
5. Asignación APE 6 / AA 6 (15 min).

## Recursos Didácticos

- Scopus
- IEEE Xplore
- ACM Digital Library
- Google Scholar
- Mendeley/Zotero

## Entregable / Producto

Antecedentes y estado del arte inicial.

## Evaluación

Calidad de la cadena de búsqueda y pertinencia de las fuentes (rúbrica).
```


# prompt2
A continuacion te comparto el APE6 y el AA6, no se si te sirvan para algo, pero como se mencionan en la actividad de ahora te los paso como recurso. Tambien te voy a pasar las bibliografías en formato bib, para que sepas que es lo que tengo. Y con eso quiero que desarrolles la actividad del ACD6.

Eso sí te digo, como no cabe todo de una sola vez, te voy a pasar las 3 cosas poco a poco, tu te esperas hasta que te haya entregado todo y ahí sí procedes.

APE6 en formato latex:
```latex
\documentclass[11pt,a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{array}
\usepackage{tabularx}
\usepackage{makecell}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{helvet}
\usepackage{ragged2e}
\usepackage{enumitem}
\usepackage{setspace}
\usepackage{longtable}
\usepackage{float}
\usepackage{url}

\renewcommand{\familydefault}{\sfdefault}
\geometry{
  a4paper,
  left=3.0cm,
  right=3.0cm,
  top=2.35cm,
  bottom=2.35cm,
  headheight=1.9cm,
  headsep=0.45cm
}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.22em}
\setlength{\tabcolsep}{6pt}
\renewcommand{\arraystretch}{1.08}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\includegraphics[height=1.35cm]{reporte_tecnico_overleaf_logo.png}}
\fancyhead[R]{\vspace{0.1cm}\small FEIRNNR - Carrera de Computación}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0pt}
\makeatletter
\renewcommand{\headrule}{%
  {\color{gray!65}\hrule width\headwidth height\headrulewidth \vskip-\headrulewidth}%
}
\makeatother

\titleformat{\section}
  {\bfseries\fontsize{15}{17}\selectfont}
  {\thesection.}{0.8em}{}
\titlespacing*{\section}{0pt}{0.7ex}{0.2ex}

\newcolumntype{L}[1]{>{\RaggedRight\arraybackslash}p{#1}}
\newcolumntype{Y}{>{\RaggedRight\arraybackslash}X}

\begin{document}
\thispagestyle{fancy}

\vspace*{0.15cm}

\begin{center}
{\bfseries\fontsize{23}{26}\selectfont
Reporte Técnico de Actividades\\
Práctico-Experimentales Nro. 006\par}
\end{center}

\section{Datos de Identificación del Estudiante y la Práctica}

\noindent
\begin{tabularx}{\textwidth}{|L{0.43\textwidth}|Y|}
\hline
\textbf{Nombre del estudiante(s)} & Wilson Patricio Palma Samaniego \\ \hline
\textbf{Asignatura} & Metodología de la Investigación en Computación \\ \hline
\textbf{Ciclo} & 4 A \\ \hline
\textbf{Unidad} & 1 \\ \hline
\textbf{Resultado de aprendizaje de la unidad} & R1. Contrasta la investigación y sus tipos con los métodos en el área de Computación y afines. \\ \hline
\textbf{Práctica Nro.} & 006 \\ \hline
\textbf{Título de la Práctica} & Búsqueda avanzada y exportación de referencias \\ \hline
\textbf{Nombre del Docente} & Luis Antonio Chamba Eras \\ \hline
\textbf{Fecha} & Martes 19 de mayo de 2026 \\ \hline
\textbf{Horario} & 10h30 -- 11h30 \\ \hline
\textbf{Lugar} & EVA-Moodle / Aula \\ \hline
\textbf{Tiempo planificado en el Sílabo} & 1 hora \\ \hline
\end{tabularx}

\section{Objetivo(s) de la Práctica}
Diseñar y ejecutar cadenas de búsqueda avanzada en Scopus e IEEE Xplore, exportando las referencias al gestor bibliográfico.

\section{Materiales, Reactivos, Equipos y Herramientas}
\begin{itemize}[leftmargin=1.2cm]
    \item Computador.
    \item Acceso a Scopus.
    \item Acceso a IEEE Xplore.
    \item Mendeley o Zotero.
    \item Guía de operadores booleanos.
    \item EVA-Moodle.
    \item Guía institucional de práctica.
\end{itemize}

\section{Procedimiento / Metodología Ejecutada}
La práctica se desarrolló siguiendo el enfoque de Aprendizaje Basado en Investigación (ABI), con los siguientes pasos:

\begin{enumerate}[leftmargin=1.2cm]
    \item Se definieron las palabras clave del proyecto en inglés y español, con el fin de ampliar la cobertura de búsqueda.
    \item Se construyeron cadenas de búsqueda utilizando operadores booleanos como AND, OR y NOT.
    \item Se ejecutaron búsquedas avanzadas en Scopus e IEEE Xplore aplicando filtros de año, tipo de documento y área temática.
    \item Se evaluaron los resultados obtenidos y se seleccionaron artículos adicionales relevantes para el proyecto.
    \item Se exportaron las referencias seleccionadas directamente a Mendeley o Zotero.
    \item Se documentó la cadena de búsqueda empleada y los resultados obtenidos durante la exploración bibliográfica.
    \item Finalmente, se subió el reporte técnico en formato PDF a EVA-Moodle.
\end{enumerate}

\section{Resultados}\label{resultados}

\subsection{Pregunta de investigación}\label{pregunta-de-investigaciuxf3n}

¿Qué tan efectivo es Naive Bayes en clasificación de texto?

\subsection{Cadena de búsqueda}\label{cadena-de-buxfasqueda}

\begin{verbatim}
("naive bayes" OR "naive bayes classifier" OR "naive bayes classification" OR
"bayes classifier" OR "multinomial naive bayes" OR "bernoulli naive bayes")
AND
("text classification" OR "document classification" OR "text categor*" OR
"text mining" OR "text analytics" OR "natural language processing" OR "NLP" OR
"sentiment analysis" OR "topic classification" OR "document categor*")
\end{verbatim}

\subsection{Clasificación de los 44 artículos}\label{clasificaciuxf3n-de-los-44-artuxedculos}

A continuación se presenta la clasificación de los 44 artículos identificados en las fuentes, evaluados según su relevancia para investigar la efectividad de \textbf{Naive Bayes (NB)} en la clasificación de textos.

Los criterios utilizados son:
\begin{itemize}
    \item \textbf{Alto:} El artículo se centra específicamente en mejorar el algoritmo, comparar su rendimiento de forma exhaustiva o proponer variantes fundamentales.
    \item \textbf{Medio:} El artículo aplica NB a un dominio, idioma o tarea específica (por ejemplo, medicina, árabe, detección de clickbait), priorizando la aplicación sobre el estudio teórico de la efectividad general del algoritmo.
\end{itemize}

\begin{longtable}{|c|c|p{9cm}|}
\caption{Clasificación de artículos según su relevancia para el estudio de Naive Bayes en clasificación de textos}
\label{tab:clasificacion-articulos} \\
\hline
\textbf{\#} & \textbf{Nivel de Relevancia} & \textbf{DOI o URL del Artículo} \\
\hline
\endfirsthead

\hline
\textbf{\#} & \textbf{Nivel de Relevancia} & \textbf{DOI o URL del Artículo} \\
\hline
\endhead

[1]  & \textbf{Alto}  & \url{10.1109/TKDE.2006.180} \\
\hline
[2]  & \textbf{Medio} & \url{10.1109/SNPD.2019.8935711} \\
\hline
[3]  & \textbf{Alto}  & \url{10.1007/11871637_49} \\
\hline
[4]  & \textbf{Alto}  & \url{10.1145/2911451.2911547} \\
\hline
[5]  & \textbf{Alto}  & \url{10.1016/J.ENGAPPAI.2016.02.002} \\
\hline
[6]  & \textbf{Alto}  & \url{https://doi.org/10.1007/3-540-45683-X_45} \\
\hline
[7]  & \textbf{Alto}  & \url{https://doi.org/10.1007/978-3-540-30586-6_76} \\
\hline
[8]  & \textbf{Alto}  & \url{https://doi.org/10.1007/978-3-540-71496-5_73} \\
\hline
[9]  & \textbf{Alto}  & \url{https://doi.org/10.1007/978-3-540-30549-1_43} \\
\hline
[10] & \textbf{Medio} & \url{https://doi.org/10.1007/11735106_17} \\
\hline
[11] & \textbf{Alto}  & \url{10.1016/j.eswa.2008.06.054} \\
\hline
[12] & \textbf{Alto}  & \url{10.1016/j.proeng.2011.08.404} \\
\hline
[13] & \textbf{Alto}  & \url{10.1016/j.patrec.2015.07.028} \\
\hline
[14] & \textbf{Alto}  & \url{10.1016/j.patrec.2008.11.013} \\
\hline
[15] & \textbf{Alto}  & \url{10.1016/j.knosys.2016.02.017} \\
\hline
[16] & \textbf{Alto}  & \url{10.1109/ISIP.2008.54} \\
\hline
[17] & \textbf{Alto}  & \url{10.1016/j.asoc.2020.106652} \\
\hline
[18] & \textbf{Medio} & \url{10.1016/j.knosys.2010.04.004} \\
\hline
[19] & \textbf{Alto}  & \url{10.1016/j.neucom.2018.07.002} \\
\hline
[20] & \textbf{Alto}  & \url{https://dl.acm.org/doi/10.5555/1619645.1619732} \\
\hline
[21] & \textbf{Medio} & \url{10.32604/cmes.2023.026812} \\
\hline
[22] & \textbf{Medio} & \url{10.55151/ijeedu.v5i1.99} \\
\hline
[23] & \textbf{Medio} & \url{10.62441/nano-ntp.v20iS1.77} \\
\hline
[24] & \textbf{Medio} & \url{10.38094/jastt61237} \\
\hline
[25] & \textbf{Medio} & \url{10.3390/bdcc7030127} \\
\hline
[26] & \textbf{Medio} & \url{10.1063/5.0110821} \\
\hline
[27] & \textbf{Medio} & \url{10.1016/j.fraope.2025.100373} \\
\hline
[28] & \textbf{Alto}  & \url{10.1007/s11634-023-00536-8} \\
\hline
[29] & \textbf{Medio} & \url{10.1051/e3sconf/202346502048} \\
\hline
[30] & \textbf{Medio} & \url{10.1109/ACCESS.2024.3487311} \\
\hline
[31] & \textbf{Alto}  & \url{10.26615/978-954-452-056-4_151} \\
\hline
[32] & \textbf{Medio} & \url{10.1088/1742-6596/1641/1/012043} \\
\hline
[33] & \textbf{Alto}  & \url{10.5220/0010890400003122} \\
\hline
[34] & \textbf{Alto}  & \url{10.1109/TKDE.2016.2522427} \\
\hline
[35] & \textbf{Alto}  & \url{10.3390/math9192378} \\
\hline
[36] & \textbf{Alto}  & \url{10.1109/TKDE.2010.160} \\
\hline
[37] & \textbf{Alto}  & \url{10.1007/978-3-642-41278-3_24} \\
\hline
[38] & \textbf{Alto}  & \url{10.1109/ACCESS.2020.2968984} \\
\hline
[39] & \textbf{Alto}  & \url{10.1109/TKDE.2016.2563436} \\
\hline
[40] & \textbf{Medio} & \url{10.1093/bioinformatics/btl350} \\
\hline
[41] & \textbf{Medio} & \url{10.4108/eai.12-10-2019.2296530} \\
\hline
[42] & \textbf{Medio} & \url{10.35940/ijeat.A1610.109119} \\
\hline
[43] & \textbf{Medio} & \url{10.1186/1471-2105-8-269} \\
\hline
[44] & \textbf{Alto}  & \url{10.4067/S0718-09342011000300004} \\
\hline
\end{longtable}

\subsection{Jerarquización (Alto, Medio, Bajo) de los 44 artículos en Notebook}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{\detokenize{(trozos) (6.2) Capturas de pantalla (NotebookLM).png/trozo_0.png}}
    \caption{Notebook 1}
    \label{fig:notebook1}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{\detokenize{(trozos) (6.2) Capturas de pantalla (NotebookLM).png/trozo_1.png}}
    \caption{Notebook 2}
    \label{fig:notebook2}
\end{figure}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{\detokenize{(trozos) (6.2) Capturas de pantalla (NotebookLM).png/trozo_2.png}}
    \caption{Notebook 3}
    \label{fig:notebook3}
\end{figure}

\subsection{Los 44 artículos importados en Mendeley}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{\detokenize{(6.3) Captura en Mendeley.png}}
    \caption{Los 44 artículos importados en Mendeley}
    \label{fig:mendeley44}
\end{figure}

\section{Preguntas de Control}

\textbf{1. ¿Qué ventajas ofrecen los operadores booleanos en la búsqueda bibliográfica?}

Los operadores booleanos permiten construir búsquedas más precisas y controladas. \texttt{AND} reduce el universo de resultados al exigir simultaneidad de conceptos; \texttt{OR} amplía la cobertura al incluir sinónimos, variantes ortográficas o términos relacionados; y \texttt{NOT} excluye elementos irrelevantes. Su uso mejora la pertinencia, reduce el ruido documental y facilita la recuperación sistemática de literatura académica.

\textbf{2. ¿Cómo se aplican filtros de inclusión y exclusión en una búsqueda avanzada?}

Los filtros de inclusión y exclusión se definen a partir de los criterios de la investigación. Primero se establece qué documentos deben formar parte del corpus, por ejemplo, artículos sobre Naive Bayes y clasificación de texto, publicados en revistas o conferencias, en ciertos idiomas o rangos temporales. Luego se excluyen trabajos fuera del tema, duplicados, documentos sin acceso al texto completo o estudios que no aportan evidencia útil para la pregunta de investigación. En bases como Scopus e IEEE Xplore, estos criterios se implementan mediante filtros por año, tipo de documento, área temática, idioma y palabras clave específicas.

\section{Conclusiones}

La práctica permitió aplicar de manera ordenada el proceso de búsqueda avanzada en bases de datos académicas, lo cual es fundamental para construir un marco de revisión bibliográfica sólido. El uso de operadores booleanos y filtros de recuperación facilitó la identificación de artículos relevantes sobre Naive Bayes y clasificación de texto, diferenciando con claridad aquellos estudios de alta relevancia de los de aplicación contextual. Asimismo, la exportación de referencias a Mendeley contribuyó a organizar la información de forma eficiente y a mantener trazabilidad en el proceso de investigación.

\section{Recomendaciones}

Se recomienda elaborar previamente una lista de sinónimos y términos equivalentes en inglés y español antes de ejecutar cualquier búsqueda en bases académicas. También conviene documentar cada cadena utilizada, junto con los filtros aplicados, para facilitar la replicabilidad del proceso. Además, es importante revisar manualmente las referencias exportadas al gestor bibliográfico para eliminar duplicados y corregir metadatos incompletos. Finalmente, se sugiere clasificar los artículos por nivel de relevancia desde el inicio para optimizar el análisis posterior del estado del arte.

\section{Bibliografía / Referencias}

\nocite{*}
\bibliographystyle{IEEEtran}
\bibliography{referencias}

\section{Anexos}
Recursos de apoyo para cada una de las secciones anteriores: capturas de pantalla de Scopus e IEEE Xplore, exportación de referencias a Mendeley o Zotero, y evidencia de la clasificación de los 44 artículos.

\end{document}
```

AA6 en formato markdown:
```markdown
---
title: "AA 6: Redacción de antecedentes iniciales del proyecto"
subtitle: "Efectividad de Naive Bayes en la clasificación de texto"
abstract-title: "Resumen"
abstract: "Este documento presenta los antecedentes iniciales de una investigación sobre la efectividad de Naive Bayes en la clasificación de texto. Se revisan trabajos previos enfocados en mejoras del algoritmo, selección y ponderación de características, variantes bayesianas y aplicaciones en distintos dominios, con el fin de identificar hallazgos clave y la brecha de investigación que justifica el estudio."
keywords: ["Naive Bayes", "clasificación de texto", "antecedentes", "minería de texto", "procesamiento de lenguaje natural", "machine learning"]
subject: "Redacción de antecedentes de investigación"
description: "Antecedentes iniciales sobre la efectividad de Naive Bayes en clasificación de texto, con revisión de literatura y brecha de investigación."
category: "Investigación académica"
lang: es
author: Wilson Palma
date: 2026-05-26
---

# Antecedentes iniciales del proyecto

La clasificación de texto ha sido uno de los escenarios donde Naive Bayes ha mostrado mayor utilidad debido a su simplicidad, bajo costo computacional y buen desempeño como línea base. En particular, la formulación multinomial fue revisitada tempranamente para adaptarla mejor a tareas de categorización textual, mostrando que el modelo podía competir con enfoques más complejos cuando se ajustaba adecuadamente al dominio [1]. A partir de allí, la literatura comenzó a estudiar no solo su aplicación directa, sino también las condiciones bajo las cuales Naive Bayes mantiene una efectividad aceptable en problemas con vocabularios extensos, clases desbalanceadas y datos ruidosos [2], [3].

Un primer grupo de trabajos se enfocó en mejorar el comportamiento del clasificador mediante técnicas de suavizado, balance de clases y refinamiento probabilístico. Por ejemplo, se ha mostrado que tratar el desbalance entre categorías es importante para evitar sesgos en la predicción, especialmente cuando una clase domina al resto [3]. De forma complementaria, otros autores propusieron métodos de suavizado para reducir el impacto de probabilidades nulas o escasas, mejorando la estabilidad del modelo en textos cortos o conjuntos de datos pequeños [4]. Estos estudios son relevantes porque evidencian que la efectividad de Naive Bayes no depende únicamente del algoritmo base, sino también de los ajustes previos y posteriores al proceso de clasificación [2], [4].

Otra línea importante de antecedentes se centra en la selección y ponderación de características, ya que la representación textual suele ser de alta dimensionalidad y con mucha redundancia. Chen et al. demostraron que aplicar selección de características puede mejorar Naive Bayes al eliminar términos poco informativos y conservar aquellos que aportan más discriminación entre clases [5]. Posteriormente, otros trabajos profundizaron esta idea con enfoques más finos, como la selección óptima de subconjuntos de atributos y el uso de ponderación de características para captar mejor su relevancia en cada clase [6], [7]. Estas propuestas son especialmente importantes porque sugieren que Naive Bayes, aunque simple, puede volverse más competitivo cuando se combina con estrategias de reducción y recalibración del espacio textual [5], [6], [7].

Además de la selección de variables, varios estudios han intentado romper con la independencia condicional fuerte del modelo clásico. Ganiz et al. propusieron una variante de orden superior para capturar dependencias entre términos que Naive Bayes tradicional ignora, logrando mejorar la clasificación en determinados contextos [8]. En la misma línea, trabajos más recientes incorporaron ponderación profunda por clase y adaptaciones del hidden naive bayes, buscando representar mejor la estructura interna del texto sin abandonar del todo la lógica probabilística del modelo [9], [10]. Esto confirma que buena parte de la investigación reciente no intenta reemplazar a Naive Bayes, sino extenderlo para compensar sus supuestos simplificadores [8], [9], [10].

La comparación con otros clasificadores también ha sido un tema recurrente. Un estudio basado en inferencia bayesiana para comparar clasificadores de texto mostró que el desempeño debe evaluarse con cuidado, ya que las diferencias entre modelos dependen del corpus, la métrica y la naturaleza de la tarea [11]. En consecuencia, Naive Bayes no puede considerarse universalmente superior o inferior; su efectividad es contextual y puede variar según el tipo de documento, la longitud del texto, el idioma y el balance de las clases [11]. Esto explica por qué sigue usándose como referencia en experimentos académicos y como base de comparación frente a métodos más complejos.

La literatura aplicada también refuerza esta idea de contextualidad. Se han reportado usos exitosos de Naive Bayes en clasificación de textos cortos, opiniones de usuarios, reseñas y dominios especializados, como clasificación de textos breves con apoyo ontológico [12] o análisis de reseñas de hoteles [13]. Más recientemente, han aparecido variantes como el clasificador Naive Bayes con umbrales, orientadas a mejorar su capacidad de decisión en escenarios concretos [14]. En conjunto, estos antecedentes muestran que el algoritmo sigue vigente, pero su rendimiento depende fuertemente del dominio de aplicación, de la representación textual y de las técnicas de ajuste empleadas.

Con base en lo anterior, la brecha que justifica esta investigación es que, aunque existe amplia evidencia de mejoras puntuales sobre Naive Bayes y múltiples aplicaciones en dominios distintos, los resultados están dispersos y no siempre permiten extraer una conclusión general sobre su efectividad en clasificación de texto. La mayoría de los trabajos se concentran en un solo corpus, idioma o tipo de problema, por lo que todavía resulta necesario sintetizar qué tan efectivo es realmente Naive Bayes cuando se analiza como solución general para clasificación textual. Por ello, esta investigación se orienta a reunir, comparar y evaluar la evidencia existente para determinar en qué condiciones el modelo funciona bien y en cuáles pierde efectividad [5], [6], [9], [11], [14].

# Referencias

[1] A. M. Kibriya, E. Frank, B. Pfahringer y G. Holmes, “Multinomial naive Bayes for text categorization revisited,” en *AI 2004: Advances in Artificial Intelligence*, Berlin, Heidelberg: Springer, 2005, pp. 488–499.

[2] S. B. Kim, K. S. Han, H. C. Rim y S. H. Myaeng, “Some effective techniques for naive bayes text classification,” *IEEE Transactions on Knowledge and Data Engineering*, vol. 18, no. 11, pp. 1457–1466, 2006.

[3] E. Frank y R. R. Bouckaert, “Naive Bayes for text classification with unbalanced classes,” *Lecture Notes in Computer Science*, vol. 4213, pp. 503–510, 2006.

[4] F. He y X. Ding, “Improving Naive Bayes Text Classifier Using Smoothing Methods,” en *Advances in Information Retrieval*, Berlin, Heidelberg: Springer, 2007, pp. 703–707.

[5] J. Chen, H. Huang, S. Tian y Y. Qu, “Feature selection for text classification with Naïve Bayes,” *Expert Systems with Applications*, vol. 36, no. 3, pp. 5432–5435, 2009.

[6] B. Tang, S. Kay y H. He, “Toward Optimal Feature Selection in Naive Bayes for Text Categorization,” *IEEE Transactions on Knowledge and Data Engineering*, vol. 28, no. 9, pp. 2508–2521, 2016.

[7] L. Zhang, L. Jiang, C. Li y G. Kong, “Two feature weighting approaches for naive Bayes text classifiers,” *Knowledge-Based Systems*, vol. 100, pp. 137–144, 2016.

[8] M. C. Ganiz, C. George y W. M. Pottenger, “Higher order Naïve Bayes: A novel non-IID approach to text classification,” *IEEE Transactions on Knowledge and Data Engineering*, vol. 23, no. 7, pp. 1022–1034, 2011.

[9] S. Ruan, H. Li, C. Li y K. Song, “Class-specific deep feature weighting for naïve bayes text classifiers,” *IEEE Access*, vol. 8, pp. 20151–20159, 2020.

[10] S. Gan, S. Shao, L. Chen, L. Yu y L. Jiang, “Adapting hidden naive bayes for text classification,” *Mathematics*, vol. 9, no. 19, 2021.

[11] D. Zhang, J. Wang, E. Yilmaz, X. Wang y Y. Zhou, “Bayesian Performance Comparison of Text Classifiers,” en *Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval*, New York, NY, USA: ACM, 2016, pp. 15–24.

[12] K. Sangounpao y P. Muenchaisri, “Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset,” en *Proceedings of the 20th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing*, 2019, pp. 53–58.

[13] J. B. Awotunde, S. Misra, V. Katta y O. C. Adebayo, “An Ensemble-Based Hotel Reviews System Using Naive Bayes Classifier,” *CMES - Computer Modeling in Engineering and Sciences*, vol. 137, no. 1, pp. 131–154, 2023.

[14] M. Romano, G. Contu, F. Mola y C. Conversano, “Threshold-based Naïve Bayes classifier,” *Advances in Data Analysis and Classification*, vol. 18, no. 2, pp. 325–361, 2024.
```

Bibliografía del APE6 (Tal vez no tenga mucho que ver, pero te lo paso por si al caso):
```bib
@article{Kim2006,
   author = {Sang Bum Kim and Kyoung Soo Han and Hae Chang Rim and Sung Hyon Myaeng},
   doi = {10.1109/TKDE.2006.180},
   issn = {10414347},
   issue = {11},
   journal = {IEEE Transactions on Knowledge and Data Engineering},
   keywords = {Poisson model,Text classification,feature weighting,naive Bayes classifier},
   month = {11},
   pages = {1457-1466},
   title = {Some effective techniques for naive bayes text classification},
   volume = {18},
   url = {https://ieeexplore.ieee.org/document/1704799},
   year = {2006}
}

@article{Sangounpao2019,
   author = {Ketkaew Sangounpao and Pornsiri Muenchaisri},
   doi = {10.1109/SNPD.2019.8935711},
   isbn = {9781728116518},
   journal = {Proceedings - 20th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2019},
   keywords = {accounting domain knowledge,multi-classification,ontology,requirements engineering,short text classification,small dataset,traditional classification},
   month = {7},
   pages = {53-58},
   publisher = {Institute of Electrical and Electronics Engineers Inc.},
   title = {Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset},
   url = {https://ieeexplore.ieee.org/document/8935711},
   year = {2019}
}

@article{Frank2006,
   author = {Eibe Frank and Remco R. Bouckaert},
   doi = {10.1007/11871637_49},
   isbn = {978-3-540-46048-0},
   issn = {1611-3349},
   journal = {Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)},
   pages = {503-510},
   publisher = {Springer, Berlin, Heidelberg},
   title = {Naive Bayes for Text Classification with Unbalanced Classes},
   volume = {4213 LNAI},
   url = {https://link.springer.com/chapter/10.1007/11871637_49},
   year = {2006}
}

@inproceedings{10.1145/2911451.2911547,
author = {Zhang, Dell and Wang, Jun and Yilmaz, Emine and Wang, Xiaoling and Zhou, Yuxin},
title = {Bayesian Performance Comparison of Text Classifiers},
year = {2016},
isbn = {9781450340694},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/2911451.2911547},
doi = {10.1145/2911451.2911547},
booktitle = {Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval},
pages = {15–24},
numpages = {10},
keywords = {bayesian inference, hypothesis testing, performance evaluation, text classification},
location = {Pisa, Italy},
series = {SIGIR '16}
}

@article{Jiang2016,
   author = {Liangxiao Jiang and Chaoqun Li and Shasha Wang and Lungan Zhang},
   doi = {10.1016/J.ENGAPPAI.2016.02.002},
   issn = {0952-1976},
   journal = {Engineering Applications of Artificial Intelligence},
   keywords = {Correlation-based feature selection,Feature weighting,Naive Bayes,Text classification},
   month = {6},
   pages = {26-39},
   publisher = {Pergamon},
   title = {Deep feature weighting for naive Bayes and its application to text classification},
   volume = {52},
   url = {https://www.sciencedirect.com/science/article/abs/pii/S0952197616300112?via%3Dihub},
   year = {2016}
}





@InProceedings{10.1007/3-540-45683-X_45,
author="Kim, Sang-Bum
and Rim, Hae-Chang
and Yook, DongSuk
and Lim, Heui-Seok",
editor="Ishizuka, Mitsuru
and Sattar, Abdul",
title="Effective Methods for Improving Naive Bayes Text Classifiers",
booktitle="PRICAI 2002: Trends in Artificial Intelligence",
year="2002",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="414--423",
isbn="978-3-540-45683-4",
doi = {https://doi.org/10.1007/3-540-45683-X_45}
}

@InProceedings{10.1007/978-3-540-30586-6_76,
author="Schneider, Karl-Michael",
editor="Gelbukh, Alexander",
title="Techniques for Improving the Performance of Naive Bayes for Text Classification",
booktitle="Computational Linguistics and Intelligent Text Processing",
year="2005",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="682--693",
isbn="978-3-540-30586-6",
doi = {https://doi.org/10.1007/978-3-540-30586-6_76}
}

@InProceedings{10.1007/978-3-540-71496-5_73,
author="He, Feng
and Ding, Xiaoqing",
editor="Amati, Giambattista
and Carpineto, Claudio
and Romano, Giovanni",
title="Improving Naive Bayes Text Classifier Using Smoothing Methods",
booktitle="Advances in Information Retrieval",
year="2007",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="703--707",
isbn="978-3-540-71496-5",
doi = {https://doi.org/10.1007/978-3-540-71496-5_73}
}

@InProceedings{10.1007/978-3-540-30549-1_43,
author="Kibriya, Ashraf M.
and Frank, Eibe
and Pfahringer, Bernhard
and Holmes, Geoffrey",
editor="Webb, Geoffrey I.
and Yu, Xinghuo",
title="Multinomial Naive Bayes for Text Categorization Revisited",
booktitle="AI 2004: Advances in Artificial Intelligence",
year="2005",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="488--499",
isbn="978-3-540-30549-1",
doi = {https://doi.org/10.1007/978-3-540-30549-1_43}
}

@InProceedings{10.1007/11735106_17,
author="Yin, Ling
and Power, Richard",
editor="Lalmas, Mounia
and MacFarlane, Andy
and R{\"u}ger, Stefan
and Tombros, Anastasios
and Tsikrika, Theodora
and Yavlinsky, Alexei",
title="Adapting the Naive Bayes Classifier to Rank Procedural Texts",
booktitle="Advances in Information Retrieval",
year="2006",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="179--190",
isbn="978-3-540-33348-7",
doi = {https://doi.org/10.1007/11735106_17}
}

@article{CHEN20095432,
title = {Feature selection for text classification with Naïve Bayes},
journal = {Expert Systems with Applications},
volume = {36},
number = {3, Part 1},
pages = {5432-5435},
year = {2009},
issn = {0957-4174},
doi = {https://doi.org/10.1016/j.eswa.2008.06.054},
url = {https://www.sciencedirect.com/science/article/pii/S0957417408003564},
author = {Jingnian Chen and Houkuan Huang and Shengfeng Tian and Youli Qu},
keywords = {Text classification, Feature selection, Text preprocessing, Naïve Bayes},
}

@article{ZHANG20112160,
title = {An Improvement to Naive Bayes for Text Classification},
journal = {Procedia Engineering},
volume = {15},
pages = {2160-2164},
year = {2011},
note = {CEIS 2011},
issn = {1877-7058},
doi = {https://doi.org/10.1016/j.proeng.2011.08.404},
url = {https://www.sciencedirect.com/science/article/pii/S1877705811019059},
author = {Wei Zhang and Feng Gao},
keywords = {Text classification, Feature selection, Machine learning, Naïve Bayes},
}

@article{FENG2015109,
title = {Feature subset selection using naive Bayes for text classification},
journal = {Pattern Recognition Letters},
volume = {65},
pages = {109-115},
year = {2015},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2015.07.028},
url = {https://www.sciencedirect.com/science/article/pii/S0167865515002378},
author = {Guozhong Feng and Jianhua Guo and Bing-Yi Jing and Tieli Sun},
keywords = {Bayesian model averaging, Global selection index, Latent selection augmented naive Bayes, Local selection index, Text classification},
}

@article{YOUN2009477,
title = {Class dependent feature scaling method using naive Bayes classifier for text datamining},
journal = {Pattern Recognition Letters},
volume = {30},
number = {5},
pages = {477-485},
year = {2009},
issn = {0167-8655},
doi = {https://doi.org/10.1016/j.patrec.2008.11.013},
url = {https://www.sciencedirect.com/science/article/pii/S0167865508003553},
author = {Eunseog Youn and Myong K. Jeong},
keywords = {Classification, Feature selection, Naive Bayes classifier, Recursive feature elimination},
}

@article{ZHANG2016137,
title = {Two feature weighting approaches for naive Bayes text classifiers},
journal = {Knowledge-Based Systems},
volume = {100},
pages = {137-144},
year = {2016},
issn = {0950-7051},
doi = {https://doi.org/10.1016/j.knosys.2016.02.017},
url = {https://www.sciencedirect.com/science/article/pii/S0950705116001039},
author = {Lungan Zhang and Liangxiao Jiang and Chaoqun Li and Ganggang Kong},
keywords = {Naive Bayes text classifiers, Feature weighting, Gain ratio, Decision tree},
}

@INPROCEEDINGS{4554061,
  author={Ding, Wang and Yu, Songnian and Wang, Qianfeng and Yu, Jiaqi and Guo, Qiang},
  booktitle={2008 International Symposiums on Information Processing}, 
  title={A Novel Naive Bayesian Text Classifier}, 
  year={2008},
  volume={},
  number={},
  pages={78-82},
  keywords={Bayesian methods;Text categorization;Niobium;Packaging;Artificial intelligence;Text mining;Information processing;Performance analysis;Support vector machines;Support vector machine classification;Text classification;Naive bayesian;Data mining},
  doi={10.1109/ISIP.2008.54},
  ISSN={},
  month={May},}

@article{ELHINDI2020106652,
title = {Lazy fine-tuning algorithms for naïve Bayesian text classification},
journal = {Applied Soft Computing},
volume = {96},
pages = {106652},
year = {2020},
issn = {1568-4946},
doi = {https://doi.org/10.1016/j.asoc.2020.106652},
url = {https://www.sciencedirect.com/science/article/pii/S1568494620305901},
author = {Khalil M. {El Hindi} and Reem R. Aljulaidan and Hussien AlSalman},
keywords = {Fine-tuning Naïve Bayes, Document categorization, Local learning, Multinomial text classification, Complement NB, One-versus-all NB},
}

@article{LU2010598,
title = {Chinese text classification by the Naïve Bayes Classifier and the associative classifier with multiple confidence threshold values},
journal = {Knowledge-Based Systems},
volume = {23},
number = {6},
pages = {598-604},
year = {2010},
issn = {0950-7051},
doi = {https://doi.org/10.1016/j.knosys.2010.04.004},
url = {https://www.sciencedirect.com/science/article/pii/S0950705110000638},
author = {Shing-Hwa Lu and Ding-An Chiang and Huan-Chao Keh and Hui-Hua Huang},
keywords = {Association classification, Text classification, Text mining, Text categorization},
}

@article{KIM2018128,
title = {Towards perfect text classification with Wikipedia-based semantic Naïve Bayes learning},
journal = {Neurocomputing},
volume = {315},
pages = {128-134},
year = {2018},
issn = {0925-2312},
doi = {https://doi.org/10.1016/j.neucom.2018.07.002},
url = {https://www.sciencedirect.com/science/article/pii/S0925231218308282},
author = {Han-joon Kim and Jiyun Kim and Jinseog Kim and Pureum Lim},
keywords = {Text classification, Naïve Bayes learning, Tensor space, Wikipedia, Semantic features},
}

@inproceedings{10.5555/1619645.1619732,
author = {Dai, Wenyuan and Xue, Gui-Rong and Yang, Qiang and Yu, Yong},
title = {Transferring naive bayes classifiers for text classification},
year = {2007},
isbn = {9781577353232},
publisher = {AAAI Press},
booktitle = {Proceedings of the 22nd National Conference on Artificial Intelligence - Volume 1},
pages = {540–545},
numpages = {6},
location = {Vancouver, British Columbia, Canada},
series = {AAAI'07},
url = {https://dl.acm.org/doi/10.5555/1619645.1619732}
}




@ARTICLE{Awotunde2023131,
	author = {Awotunde, Joseph Bamidele and Misra, Sanjay and Katta, Vikash and Adebayo, Oluwafemi Charles},
	title = {An Ensemble-Based Hotel Reviews System Using Naive Bayes Classifier},
	year = {2023},
	journal = {CMES - Computer Modeling in Engineering and Sciences},
	volume = {137},
	number = {1},
	pages = {131 - 154},
	doi = {10.32604/cmes.2023.026812},
	url = {https://www.scopus.com/pages/publications/85159167415?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 9; All Open Access; Gold Open Access; Green Open Access}
}

@ARTICLE{Risal202335,
	author = {Risal, Andi Akram Nur and Fathahillah and Sulaiman, Dwi Rezky Anandari},
	title = {Classification of Sentiment Analysis and Community Opinion Modeling Topics for Application of ICT in Government Operations},
	year = {2023},
	journal = {International Journal of Environment, Engineering and Education},
	volume = {5},
	number = {1},
	pages = {35 - 44},
	doi = {10.55151/ijeedu.v5i1.99},
	url = {https://www.scopus.com/pages/publications/105008537656?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 1; All Open Access; Gold Open Access}
}

@ARTICLE{Sawlani2024952,
	author = {Sawlani, Chandni and Sharma, Pooja},
	title = {A Nano Scale Machine Learning Assisted Natural Language Processing Framework for Sentiment Classification in Smart System Platform},
	year = {2024},
	journal = {Nanotechnology Perceptions},
	volume = {20},
	number = {S1},
	pages = {952 - 966},
	doi = {10.62441/nano-ntp.v20iS1.77},
	url = {https://www.scopus.com/pages/publications/85200108878?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 0; All Open Access; Gold Open Access}
}

@ARTICLE{Lwin202543,
	author = {Lwin, Nay Oo and Jain, Rituraj and Dal, Rabnaz and Yan, Htet Oo and Thaw, Kaung Khant and Naung, Saw Yan},
	title = {Text Classification for Clickbait Detection: A Model-Driven Approach Using CountVectorizer and ML Classifiers},
	year = {2025},
	journal = {Journal of Applied Science and Technology Trends},
	volume = {6},
	number = {1},
	pages = {43 - 49},
	doi = {10.38094/jastt61237},
	url = {https://www.scopus.com/pages/publications/105009105858?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 4; All Open Access; Gold Open Access}
}

@ARTICLE{Musleh2023,
	author = {Musleh, Dhiaa A. and Alkhwaja, Ibrahim and Alkhwaja, Ali and Alghamdi, Mohammed and Abahussain, Hussam and Alfawaz, Faisal and Min-Allah, Nasro and Abdulqader, Mamoun Masoud},
	title = {Arabic Sentiment Analysis of YouTube Comments: NLP-Based Machine Learning Approaches for Content Evaluation},
	year = {2023},
	journal = {Big Data and Cognitive Computing},
	volume = {7},
	number = {3},
	pages = {},
	doi = {10.3390/bdcc7030127},
	url = {https://www.scopus.com/pages/publications/85172102206?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 44; All Open Access; Gold Open Access; Green Open Access}
}

@CONFERENCE{Mazidnianto2022,
	author = {Mazidnianto, Muhammad Faisal and Damanik, Anella Prisdayanti and Budi, Indra and Santoso, Aris Budi and Putra, Prabu Kresna},
	title = {Abortion drug products classification using text mining: A case study of PT XYZ},
	year = {2022},
	journal = {AIP Conference Proceedings},
	volume = {2658},
	pages = {},
	doi = {10.1063/5.0110821},
	url = {https://www.scopus.com/pages/publications/85144139461?origin=resultslist},
	type = {Conference paper},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 0; All Open Access; Bronze Open Access}
}

@ARTICLE{Shannaq2025,
	author = {Shannaq, Boumedyen},
	title = {Enhancing Arabic text classification through mobile virtual keypad-based encoding algorithm},
	year = {2025},
	journal = {Franklin Open},
	volume = {12},
	pages = {},
	doi = {10.1016/j.fraope.2025.100373},
	url = {https://www.scopus.com/pages/publications/105017785466?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 5; All Open Access; Gold Open Access; Green Open Access}
}

@ARTICLE{Romano2024325,
	author = {Romano, Maurizio and Contu, Giulia and Mola, Francesco and Conversano, Claudio},
	title = {Threshold-based Naïve Bayes classifier},
	year = {2024},
	journal = {Advances in Data Analysis and Classification},
	volume = {18},
	number = {2},
	pages = {325 - 361},
	doi = {10.1007/s11634-023-00536-8},
	url = {https://www.scopus.com/pages/publications/85149965773?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 15; All Open Access; Green Open Access; Hybrid Gold Open Access}
}

@CONFERENCE{Humaidi2023,
	author = {Humaidi, Muhammad Haris and Sutrisno and Laksono, Pringgo Widyo},
	title = {Implementation of Machine Learning for Text Classification Using the Naive Bayes Algorithm in Academic Information Systems at Sebelas Maret University Indonesia},
	year = {2023},
	journal = {E3S Web of Conferences},
	volume = {465},
	pages = {},
	doi = {10.1051/e3sconf/202346502048},
	url = {https://www.scopus.com/pages/publications/85182782781?origin=resultslist},
	type = {Conference paper},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 0; All Open Access; Gold Open Access; Green Open Access}
}

@ARTICLE{Yu Li2024159086,
	author = {Yu Li, Xiao and Han, Ling Bo and Feng Jiang, Zheng},
	title = {Deep Learning-Based Algorithm for Classification of News Text},
	year = {2024},
	journal = {IEEE Access},
	volume = {12},
	pages = {159086 - 159098},
	doi = {10.1109/ACCESS.2024.3487311},
	url = {https://www.scopus.com/pages/publications/85209064979?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 2; All Open Access; Gold Open Access; Green Open Access}
}

@CONFERENCE{Wawer20191321,
	author = {Wawer, Aleksander and Sobiczewska, Julita},
	title = {Predicting sentiment of Polish language short texts},
	year = {2019},
	journal = {International Conference Recent Advances in Natural Language Processing, RANLP},
	volume = {2019-September},
	pages = {1321 - 1327},
	doi = {10.26615/978-954-452-056-4_151},
	url = {https://www.scopus.com/pages/publications/85076455857?origin=resultslist},
	type = {Conference paper},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 5; All Open Access; Gold Open Access}
}

@CONFERENCE{Pratmanto2020,
	author = {Pratmanto, Dany and Rousyati, Rousyati and Wati, Fanny Fatma and Widodo, Andrian Eko and Suleman, Suleman and Wijianto, Ragil},
	title = {App Review Sentiment Analysis Shopee Application in Google Play Store Using Naive Bayes Algorithm},
	year = {2020},
	journal = {Journal of Physics: Conference Series},
	volume = {1641},
	number = {1},
	pages = {},
	doi = {10.1088/1742-6596/1641/1/012043},
	url = {https://www.scopus.com/pages/publications/85097187731?origin=resultslist},
	type = {Conference paper},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 27; All Open Access; Gold Open Access}
}

@CONFERENCE{Azeraf2022315,
	author = {Azeraf, Elie and Monfrini, Emmanuel and Pieczynski, Wojciech},
	title = {Improving Usual Naive Bayes Classifier Performances with Neural Naïve Bayes based Models},
	year = {2022},
	journal = {International Conference on Pattern Recognition Applications and Methods},
	volume = {1},
	pages = {315 - 322},
	doi = {10.5220/0010890400003122},
	url = {https://www.scopus.com/pages/publications/85174564063?origin=resultslist},
	type = {Conference paper},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 6; All Open Access; Gold Open Access}
}

@ARTICLE{Tang20161602,
	author = {Tang, Bo and He, Haibo and Baggenstoss, Paul M. and Kay, Steven},
	title = {A Bayesian Classification Approach Using Class-Specific Features for Text Categorization},
	year = {2016},
	journal = {IEEE Transactions on Knowledge and Data Engineering},
	volume = {28},
	number = {6},
	pages = {1602 - 1606},
	doi = {10.1109/TKDE.2016.2522427},
	url = {https://www.scopus.com/pages/publications/84968876693?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 153; All Open Access; Green Open Access}
}

@ARTICLE{Gan2021,
	author = {Gan, Shengfeng and Shao, Shiqi and Chen, Long and Yu, Liangjun and Jiang, Liangxiao},
	title = {Adapting hidden naive bayes for text classification},
	year = {2021},
	journal = {Mathematics},
	volume = {9},
	number = {19},
	pages = {},
	doi = {10.3390/math9192378},
	url = {https://www.scopus.com/pages/publications/85115956966?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 19; All Open Access; Gold Open Access; Green Open Access}
}

@ARTICLE{Ganiz20111022,
	author = {Ganiz, Murat Can and George, Cibin and Pottenger, William M.},
	title = {Higher order Naïve bayes: A novel non-IID approach to text classification},
	year = {2011},
	journal = {IEEE Transactions on Knowledge and Data Engineering},
	volume = {23},
	number = {7},
	pages = {1022 - 1034},
	doi = {10.1109/TKDE.2010.160},
	url = {https://www.scopus.com/pages/publications/80054909897?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 47; All Open Access; Green Open Access}
}

@ARTICLE{Narayanan2013194,
	author = {Narayanan, Vivek and Arora, Ishan and Bhatia, Arjun},
	title = {Fast and accurate sentiment classification using an enhanced Naive Bayes model},
	year = {2013},
	journal = {Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)},
	volume = {8206 LNCS},
	pages = {194 - 201},
	doi = {10.1007/978-3-642-41278-3_24},
	url = {https://www.scopus.com/pages/publications/84890866356?origin=resultslist},
	type = {Conference paper},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 202; All Open Access; Green Open Access}
}

@ARTICLE{Ruan202020151,
	author = {Ruan, Shufen and Li, Hongwei and Li, Chaoqun and Song, Kunfang},
	title = {Class-specific deep feature weighting for naïve bayes text classifiers},
	year = {2020},
	journal = {IEEE Access},
	volume = {8},
	pages = {20151 - 20159},
	doi = {10.1109/ACCESS.2020.2968984},
	url = {https://www.scopus.com/pages/publications/85079740208?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 38; All Open Access; Gold Open Access; Green Open Access}
}

@ARTICLE{Tang20162508,
	author = {Tang, Bo and Kay, Steven and He, Haibo},
	title = {Toward Optimal Feature Selection in Naive Bayes for Text Categorization},
	year = {2016},
	journal = {IEEE Transactions on Knowledge and Data Engineering},
	volume = {28},
	number = {9},
	pages = {2508 - 2521},
	doi = {10.1109/TKDE.2016.2563436},
	url = {https://www.scopus.com/pages/publications/84982078862?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 216; All Open Access; Green Open Access}
}

@ARTICLE{Han20062136,
	author = {Han, Bo and Obradovic, Zoran and Hu, Zhang-Zhi and Wu, Cathy H. and Vucetic, Slobodan},
	title = {Substring selection for biomedical document classification},
	year = {2006},
	journal = {Bioinformatics},
	volume = {22},
	number = {17},
	pages = {2136 - 2142},
	doi = {10.1093/bioinformatics/btl350},
	url = {https://www.scopus.com/pages/publications/33748635165?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 17; All Open Access; Hybrid Gold Open Access}
}

@CONFERENCE{Jaman2020,
	author = {Jaman, Jajam Haerul and Hannie and Simatupang, Martina Sari},
	title = {Sentiment Analysis of the Body-Shaming Beauty Vlog Comments},
	year = {2020},
	journal = {Proceedings of the 7th Mathematics, Science, and Computer Science Education International Seminar, MSCEIS 2019},
	pages = {},
	doi = {10.4108/eai.12-10-2019.2296530},
	url = {https://www.scopus.com/pages/publications/85127560697?origin=resultslist},
	type = {Conference paper},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 4; All Open Access; Bronze Open Access}
}

@ARTICLE{Prabu20195976,
	author = {Prabu, M. and Aithani, Mayank Singh and Deb, Niroj and Joshi, Pratyush},
	title = {Communication sentiment analyzer using machine learning with naive bayes bernoullinb},
	year = {2019},
	journal = {International Journal of Engineering and Advanced Technology},
	volume = {9},
	number = {1},
	pages = {5976 - 5979},
	doi = {10.35940/ijeat.A1610.109119},
	url = {https://www.scopus.com/pages/publications/85074554442?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 0; All Open Access; Gold Open Access}
}

@ARTICLE{Wang2007,
	author = {Wang, Peng and Morgan, Alexander A. and Zhang, Qing and Sette, Alessandro and Peters, Bjoern},
	title = {Automating document classification for the Immune Epitope Database},
	year = {2007},
	journal = {BMC Bioinformatics},
	volume = {8},
	pages = {},
	doi = {10.1186/1471-2105-8-269},
	url = {https://www.scopus.com/pages/publications/34548493473?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 40; All Open Access; Gold Open Access; Green Open Access}
}

@ARTICLE{Mendoza2011251,
	author = {Mendoza, Marcelo and Ortiz, Ivette and Rojas, Víctor},
	title = {Text categorization in documentary databases using light computational models; [Categorización de texto en bases documentales a partir de modelos computacionales livianos]},
	year = {2011},
	journal = {Revista Signos},
	volume = {44},
	number = {77},
	pages = {251 - 274},
	doi = {10.4067/S0718-09342011000300004},
	url = {https://www.scopus.com/pages/publications/83055180050?origin=resultslist},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 0; All Open Access; Bronze Open Access; Green Open Access}
}


```

# prompt3
Eso es todo.

Quiero que desarrolles la siguiente actividad, pero primero quiero planificación, así que dime, que es lo que piensas hacer para darte luz verde.

Actividad a elaborar:
```markdown
# ACD 6: Búsqueda Avanzada, Cadenas de Búsqueda y Antecedentes

## Objetivo

Dominar la búsqueda avanzada en bases de datos, construir cadenas de búsqueda y redactar antecedentes.

## Contenidos

- Palabras clave y tesauros.
- Cadenas booleanas.
- Filtros y criterios.
- Scopus.
- IEEE Xplore.
- ACM Digital Library.
- Google Scholar.
- Literatura gris.
- Estado del arte.

## Procedimiento

1. Demostración en vivo: búsqueda avanzada en Scopus e IEEE Xplore (25 min).
2. Taller: construcción de cadena de búsqueda personal (25 min).
3. Exportación a Mendeley/Zotero (15 min).
4. Redacción guiada de un párrafo de antecedentes (20 min).
5. Asignación APE 6 / AA 6 (15 min).

## Recursos Didácticos

- Scopus
- IEEE Xplore
- ACM Digital Library
- Google Scholar
- Mendeley/Zotero

## Entregable / Producto

Antecedentes y estado del arte inicial.

## Evaluación

Calidad de la cadena de búsqueda y pertinencia de las fuentes (rúbrica).
```

# prompt4
Bien, puedes proceder con lo acordado.

Quiero que realices la actividad completa en markdown (y la presentas en un bloque de codigo markdown para poder copiar su contenido), al final incluyes las referencias en IEEE respetando el orden de aparición y dentro del contenido citas esas fuentes, en formato IEEE (ejemplo "parrafo1 [1].\nparrafo2 [2]. ...").

Tómate tu tiempo.




