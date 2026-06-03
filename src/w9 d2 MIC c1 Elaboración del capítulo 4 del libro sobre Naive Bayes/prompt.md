# prompt1
Quiero que hagas la siguiente actividad, pero primero quiero planificación, así que dime, que es lo que piensas hacer para darte luz verde.

Actividad a elaborar:
```markdown
# Indicaciones para la elaboracion del capítulo 4
- (Miercoles) Cada uno va a hacer un capitulo del libro (en mi caso me tocó el capítulo 4) y para poder hacer ese capitulo del libro se debe resolver la pregunta que nos tocó como tema de investigación.
    - enfoque netamente tecnico para nuestro capitulos dentro del libro.
    - Cada capítulo tiene 4 secciones [Introduccion, Fundamentos Teóricos, Metodologia y Análisis de la Literatura, Conclusiones]
    - extension de 10 páginas como mínimo
```

Información Relevante:
```yaml
Estudiante:
    numero en la lista: 22
    nombre: Wilson Patricio Palma Samaniego
    correo: (wilson.palma@unl.edu.ec)
Tecnica de IA asignada: Naive Bayes
Pregunta de investigación asignada: ¿Qué tan efectivo es Naive Bayes en clasificación de texto?
Capítulo asignado:
    numero: 4
    nombre: Evaluación de la Efectividad del Algoritmo Naive Bayes en la Clasificación de Textos.
    seccion en la que vá ubicado el capítulo: Aprendizaje Estadístico y Modelos de Clasificación/Regresión
Enlace a mi documento elaborado en Overleaf: https://www.overleaf.com/project/6a171507259b739914a8d1bd
```

# prompt2
Bien, puedes proceder con lo acordado.

Me gustaría que (en los lugares que consideres oportuno) incluyas figuras, quiero que incluyas el caption de la imagen. El caption debe estar bien redactado y en español.

Si te parece conveniente también puedes incluir tablas en los lugares que consideres necesarios del documento.

Respecto a las referencias, tengo un archivo llamado "referencias.bib" y dentro del contenido citas esas referencias, en formato IEEE.

Un poco de contexto y recursos que te podrían ser útiles.

No se si te sirva pero el inge nos proporcionó este texto como metodología en general, ya que todos tenemos temas diferentes.

Metodología en general:
```text
Metodología del proceso: Los estudiantes de la asignatura de metodología de la investigación en computación, al inicio de la asignatura se les asignó una pregunta de investigación relacionada con las técnicas de la Inteligencia Artificial. Son un total de 43 preguntas/estudiantes.

Inicialmente ellos definieron las cadenas de búsqueda a partir de la descomposición en palabras claves de la pregunta de investigación en conjunto con operadores lógicos.

Posterior, se realizó la ejecución de dichas cadenas en las bases de datos IEEE Xplore, ACM Digital Lybrary. Un primer entregable fue una matriz con 5 artículos científicos localizados en cualquiera de esas bases de datos. Aquí se empezó a usar un gestor bibliográfico como Mendeley y Zotero, además, del uso de Oveleaf para la escritura en LaTeX y NotebookLM para extraer información no sesgada de los artículos en una matriz de extracción de datos. 

Luego, se expandieron las bases de datos a ScienceDirect, Springer y Lens, para localizar 15 artículos científicos en el mismo contexto de la pregunta de investigación. Teniendo en total 20 artículos en su base de datos en el gestor bibliográfico. Aquí los estudiantes aprendieron el método de jerarquización usando NotebookLM, para identificar esos artículos útiles para su pregunta de investigación.

Finalmente, se realizó la búsqueda en la base de datos Scopus, utilizando la cadena de búsqueda original y/o una mejorada para extraer los metadatos de los artículos relacionados con la pregunta, luego se exportó esos metadatos en archivo de texto y en formato BibTex para que sean usados tanto en la jerarquización con NotebookLM como para la gestión con Mendeley y Overlef de los artículos que apoyen a responder la pregunta de investigación. Aquí se usó Scopus AI para generar un reporte sobre cada pregunta de investigación que finalmente fue exportado en PDF.


Objetivo: rescatar las técnicas de IA que existen antes de la llegada de la IA Generativa, y que son la base teórica para los sistemas inteligentes, y muchas de ellas incluidas en la IA Generativa, pero que no son conocidas , y que son abordadas por los ingenierons que construyen herramientas de IA.
```

Y tambien la Plantilla latex para el capítulo 4. Cabe recalcar que el contenido que ahora tiene la plantilla no se acerca para nada a las 10 páginas por lo que tranquilamente puedes ignorar el contenido y reemplazarlo por lo que tú prefieras, lo que sí me importa es que respetes la estructura y tú generas todo el contenido suficiente para tener más de 10 páginas.

Plantilla latex para el capítulo 4:
```tex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CAPÍTULO 04: NAIVE BAYES
% AUTOR: Wilson Patricio Palma Samaniego
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\chapter{Evaluación de la Efectividad del Algoritmo Naive Bayes en la Clasificación de Textos}
\label{cap:capitulo_04}

\textbf{Autor:} Wilson Patricio Palma Samaniego (wilson.palma@unl.edu.ec) \\
\textbf{Técnica asignada:} Naive Bayes \\

\section{Introducción}
Este capítulo aborda formalmente la efectividad del algoritmo Naive Bayes en la clasificación de textos, con el objetivo de responder a la pregunta de investigación: \textit{¿Qué tan efectivo es Naive Bayes en clasificación de texto?}. La revisión se fundamenta en 44 artículos identificados mediante una cadena de búsqueda especializada, en los que se analiza tanto la mejora del algoritmo como su aplicación en distintos dominios textuales \cite{Kim2006,Frank2006,CHEN20095432,Tang20162508,Romano2024325}.

\section{Fundamentos Teóricos}
Naive Bayes es un clasificador probabilístico basado en el teorema de Bayes, que estima la clase más probable para un documento a partir de la evidencia observada en sus términos. Su formulación general para la clasificación de un documento $d$ en una clase $c$ se expresa en la Ecuación \ref{eq:nb}:

\begin{equation}
P(c \mid d) = \frac{P(c)\,P(d \mid c)}{P(d)}
\label{eq:nb}
\end{equation}

En clasificación de texto, bajo el supuesto de independencia condicional entre palabras, el modelo suele implementarse como:

\begin{equation}
\hat{c} = \arg\max_{c \in C} P(c)\prod_{i=1}^{n} P(w_i \mid c)
\label{eq:nb_texto}
\end{equation}

donde $w_i$ representa cada término del documento. Aunque esta suposición simplifica el modelado, múltiples estudios han mostrado que el método sigue siendo competitivo en tareas de clasificación textual, especialmente cuando se combina con selección de características, ponderación de atributos, suavizado o variantes mejoradas \cite{Kibriya2005,He2007,CHEN20095432,FENG2015109,ZHANG2016137,Gan2021}.

\section{Metodología y Análisis de la Literatura}
Para evaluar la efectividad de Naive Bayes en clasificación de textos, se realizó una jerarquización de los artículos recuperados en dos niveles de relevancia: \textbf{alto} y \textbf{medio}. Los artículos de alto nivel se centran en mejorar el algoritmo, compararlo de forma exhaustiva o proponer variantes relevantes; mientras que los de nivel medio aplican NB a dominios específicos, idiomas particulares o tareas concretas, aportando evidencia práctica sobre su desempeño.

En total, la evidencia recopilada permite observar que Naive Bayes mantiene una buena capacidad de clasificación en escenarios con textos cortos, datos desbalanceados, dominios especializados y tareas de análisis de sentimiento. Sin embargo, su rendimiento mejora notablemente cuando se incorporan técnicas complementarias como selección de atributos, ponderación de características y ajuste fino del modelo \cite{Kim2006,Frank2006,He2007,CHEN20095432,YOUN2009477,Tang20162508,Ruan202020151}.

La Tabla \ref{tab:rendimiento_nb} resume las principales dimensiones de análisis identificadas en la literatura revisada.

\begin{table}[h]
\centering
\caption{Dimensiones de análisis de la efectividad de Naive Bayes en clasificación de textos.}
\label{tab:rendimiento_nb}
\begin{tabular}{lll}
\toprule
\textbf{Parámetro} & \textbf{Hallazgo en la literatura} & \textbf{Implicación} \\
\midrule
Precisión & Mejora con selección y ponderación de características & Mayor capacidad discriminativa \\
Robustez & Funciona bien en textos cortos y dominios específicos & Utilidad práctica en escenarios reales \\
Simplicidad & Modelo probabilístico directo y eficiente & Bajo costo computacional \\
Adaptabilidad & Variantes como hidden NB, higher-order NB y semantic NB mejoran su desempeño & El modelo puede adaptarse a contextos complejos \\
Interpretabilidad & Fácil de explicar y de implementar & Adecuado para aplicaciones académicas y aplicadas \\
\bottomrule
\end{tabular}
\end{table}

En este análisis, también se consideró que varios estudios reportan mejoras importantes al combinar Naive Bayes con técnicas como smoothing, feature weighting, feature selection o modelos híbridos. Esto demuestra que, aunque el clasificador base es simple, su efectividad aumenta cuando se ajusta a la estructura del problema textual \cite{10.1007/978-3-540-71496-5_73,CHEN20095432,ZHANG2016137,ELHINDI2020106652,Romano2024325}.

\section{Conclusiones}
La evidencia revisada permite concluir que Naive Bayes sigue siendo una técnica efectiva para la clasificación de textos, especialmente por su eficiencia computacional, su facilidad de implementación y su buen rendimiento en tareas de categorización textual. No obstante, su desempeño no depende únicamente del algoritmo base, sino también del tratamiento previo de los datos, del balance de clases, de la representación textual y de las mejoras metodológicas incorporadas.

En consecuencia, Naive Bayes no solo es un clasificador vigente, sino también una base metodológica sólida para construir soluciones más avanzadas en clasificación de texto, particularmente cuando se combina con estrategias de selección de características, ponderación, suavizado o variantes especializadas \cite{Kim2006,Frank2006,Tang20161602,Tang20162508,Gan2021,Romano2024325}.
```

Tómate tu tiempo.

# prompt3
Bien, entonces procede.

Por si lo necesites te paso mis referencias en formato bibtex:
```bibtex
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

# prompt4
Bien, pero las figuras tienen que estar en latex y no en markdown. Las tablas tienen que seguir un formato específico ya que estoy limitado a ciertos paquetes.

formato de tablas, ademas de los paquetes a los que estoy limitado para tablas:
```latex
\documentclass[11pt,oneside]{book} 

% --- Paquetes Básicos e Idioma ---
\usepackage[spanish,es-tabla]{babel} 
\usepackage[utf8]{inputenc}        
\usepackage[T1]{fontenc}           
\usepackage{geometry}              
\geometry{a4paper, margin=1in}

% --- Paquetes Científicos Estándar ---
\usepackage{amsmath,amsfonts,amssymb} 
\usepackage{graphicx}              
\usepackage{booktabs}              
\usepackage{cite}                  
\usepackage{hyperref}      


\begin{table}[h]
\centering
\caption{Dimensiones de análisis en redes probabilísticas clínicas.}
\label{tab:rendimiento}
\begin{tabular}{lll}
\toprule
\textbf{Parámetro} & \textbf{Ventaja Tecnológica} & \textbf{Restricción} \\
\midrule
Cómputo & Consumo mínimo de memoria RAM & Complejidad algorítmica NP-Hard \\
Explicabilidad & Trazabilidad analítica exacta & Dependencia de expertos de dominio \\
\bottomrule
\end{tabular}
\end{table}
```

# prompt5
Esta super Bien, pero trata de extender lo más que puedas el contenido (Ya que sí llegamos a las 10, casi 11, pero por si al caso prefiero que me salgan unas 14 o 15 páginas) y tembien quiero que uses más referencias por que hasta ahora solo has usado 20, claro que tengo 44 referencias, pero supongo que el inge a de querer que las use, por lo que te pide que uses más citas. Realiza esto que te acabo de mancionar en el siguiente latex, ya que lo he modificado.

```latex

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% CAPÍTULO 04: NAIVE BAYES

% AUTOR: Wilson Patricio Palma Samaniego

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



\chapter{Evaluación de la Efectividad del Algoritmo Naive Bayes en la Clasificación de Textos}

\label{cap:capitulo_04}



\textbf{Autor:} Wilson Patricio Palma Samaniego (wilson.palma@unl.edu.ec) \\

\textbf{Técnica asignada:} Naive Bayes \\



\section{Introducción}



En el contexto del libro, este capítulo se ubica dentro del eje temático \textit{Aprendizaje Estadístico y Modelos de Clasificación/Regresión}, con un enfoque técnico orientado a la evaluación de un clasificador probabilístico clásico. La pregunta que guía el desarrollo es concreta y delimitada: \textit{¿Qué tan efectivo es Naive Bayes en clasificación de texto?}. Esta cuestión resulta especialmente pertinente porque la clasificación textual constituye uno de los problemas más representativos de la minería de texto y del procesamiento de lenguaje natural, dos áreas donde la eficiencia computacional, la interpretabilidad y la robustez del modelo son tan importantes como su precisión predictiva.



Naive Bayes se ha mantenido como un algoritmo de referencia en tareas de clasificación supervisada por su simplicidad, su bajo costo computacional y su facilidad de implementación. Aun así, la literatura muestra que su desempeño no depende únicamente del algoritmo base, sino también de la representación de los datos, del balance de clases, del tamaño del corpus, del ruido léxico y de las técnicas de mejora que se incorporen al flujo de trabajo \cite{Kim2006,Frank2006,Kibriya2005}. Por ello, más que preguntar si Naive Bayes \textit{sirve} o \textit{no sirve}, la pregunta técnicamente más útil es en qué condiciones su desempeño es competitivo y qué mecanismos permiten fortalecerlo \cite{Jiang2016,10.1145/2911451.2911547}.



Este capítulo analiza esa cuestión desde tres ángulos complementarios. Primero, desarrolla los fundamentos teóricos necesarios para comprender el funcionamiento del clasificador. Segundo, presenta la metodología de revisión y jerarquización de la evidencia bibliográfica utilizada para el proyecto. Tercero, sintetiza el análisis de la literatura y responde la pregunta de investigación a partir de los patrones observados en los estudios seleccionados. El objetivo no es solo describir el algoritmo, sino valorar su efectividad como solución técnica para clasificación textual en escenarios reales y académicos.



\begin{figure}[htbp]

\centering

\includegraphics[width=0.9\textwidth]{figuras/esquema_evaluacion_naive_bayes.png}

\caption{Esquema conceptual de la evaluación de Naive Bayes en clasificación de textos.}

\label{fig:esquema_evaluacion}

\end{figure}



\section{Fundamentos teóricos}



\subsection{Clasificación de textos y representación documental}



La clasificación de textos es una tarea de aprendizaje supervisado en la que un documento $d$ debe asignarse a una clase $c$ perteneciente a un conjunto finito $C$. En escenarios prácticos, el documento suele representarse mediante un vector de características derivado de su contenido léxico. La forma más común de representación es el modelo \textit{bag of words}, en el que el orden de las palabras se ignora y cada término aporta evidencia sobre la pertenencia del documento a una clase concreta.



Esta representación, aunque simplificada, es muy útil en clasificación textual porque convierte un problema de lenguaje natural en un problema numérico apto para modelos estadísticos. Sin embargo, también genera alta dimensionalidad, esparsidad y redundancia léxica. Por ello, la literatura sobre Naive Bayes en texto se ha concentrado en técnicas de selección y ponderación de características, así como en mecanismos para mejorar la estimación de probabilidades condicionales \cite{CHEN20095432,YOUN2009477,ZHANG2016137,Tang20162508}.



Desde el punto de vista técnico, la clasificación textual suele enfrentar cuatro condiciones que afectan la precisión del modelo: vocabularios extensos, documentos muy breves, clases desbalanceadas y variabilidad semántica. Naive Bayes ofrece una respuesta atractiva a ese problema porque calcula probabilidades de pertenencia sin requerir procedimientos de optimización complejos. No obstante, su supuesto de independencia condicional entre atributos es una simplificación fuerte que puede limitar su rendimiento cuando los términos del documento presentan correlaciones semánticas o sintácticas significativas \cite{Ganiz20111022,Gan2021}.



\subsection{Teorema de Bayes y regla de decisión}



Naive Bayes se basa en el teorema de Bayes, una regla fundamental de la inferencia probabilística. Para una clase $c$ y un documento $d$, la probabilidad posterior se expresa como:



\begin{equation}

P(c \mid d) = \frac{P(c)\,P(d \mid c)}{P(d)}

\label{eq:bayes}

\end{equation}



En clasificación, el denominador $P(d)$ es constante para todas las clases, por lo que la decisión se toma maximizando el numerador. La regla de decisión se escribe como:



\begin{equation}

\hat{c} = \arg\max_{c \in C} P(c)\,P(d \mid c)

\label{eq:decision}

\end{equation}



Cuando el documento se representa como un conjunto de palabras $\{w_1, w_2, \dots, w_n\}$ y se asume independencia condicional entre ellas, el producto de probabilidades condicionales toma la forma:



\begin{equation}

\hat{c} = \arg\max_{c \in C} P(c)\prod_{i=1}^{n}P(w_i \mid c)

\label{eq:naive}

\end{equation}



La independencia condicional es la suposición que da nombre al algoritmo. En rigor, la suposición rara vez se cumple en lenguaje natural, pero el modelo sigue siendo útil porque la simplificación reduce drásticamente el número de parámetros a estimar y hace viable su aplicación en corpora grandes o medianos \cite{Kibriya2005,Frank2006}. En otras palabras, Naive Bayes no busca modelar la estructura lingüística completa de un texto, sino capturar suficiente evidencia estadística para tomar decisiones útiles.



Para evitar problemas de subflujo numérico y facilitar el cálculo, la expresión anterior suele transformarse a escala logarítmica:



\begin{equation}

\hat{c} = \arg\max_{c \in C} \left[\log P(c) + \sum_{i=1}^{n}\log P(w_i \mid c)\right]

\label{eq:logdecision}

\end{equation}



Esta forma permite trabajar con sumas en lugar de productos y resulta más estable desde el punto de vista computacional. En clasificación de textos, la decisión final depende de la clase con mayor puntuación posterior, lo que convierte al algoritmo en un clasificador generativo de implementación directa.



\subsection{Modelo multinomial, suavizado y estimación de parámetros}



La variante más utilizada en clasificación textual es el modelo multinomial, en el que las frecuencias de las palabras dentro de cada clase se emplean para estimar probabilidades. Si $N_{w,c}$ representa el número de veces que la palabra $w$ aparece en documentos de la clase $c$, y $N_c$ el total de palabras observadas en esa clase, la estimación básica es:



\begin{equation}

P(w \mid c) = \frac{N_{w,c}}{N_c}

\label{eq:mnb_basic}

\end{equation}



El problema aparece cuando una palabra no se observa en el conjunto de entrenamiento para una clase específica, lo cual haría que la probabilidad condicional sea cero y anule completamente el producto de la ecuación \eqref{eq:naive}. Para resolverlo, se aplica suavizado, normalmente Laplace o alguna variante afín, de modo que:



\begin{equation}

P(w \mid c) = \frac{N_{w,c} + \alpha}{N_c + \alpha |V|}

\label{eq:smoothing}

\end{equation}



donde $|V|$ representa el tamaño del vocabulario y $\alpha$ es el parámetro de suavizado. Este mecanismo mejora la estabilidad de la estimación, especialmente cuando el corpus es pequeño o el vocabulario es muy amplio \cite{10.1007/978-3-540-71496-5_73}. En los estudios revisados, el suavizado aparece como una de las correcciones más sencillas y efectivas para hacer más robusto al clasificador.



La estimación de la probabilidad a priori $P(c)$ también es relevante, porque refleja la frecuencia relativa de cada clase en el conjunto de entrenamiento. Cuando existe desbalance, esta probabilidad puede sesgar fuertemente la predicción hacia las clases mayoritarias. Frank y Bouckaert muestran que ajustar los priors y corregir el tratamiento del desbalance mejora de manera importante el comportamiento de Naive Bayes en clasificación documental \cite{Frank2006}. En consecuencia, el rendimiento del algoritmo depende tanto del modelo de evidencia como de la calidad de las probabilidades previas.



\subsection{Métricas para evaluar efectividad}



Hablar de efectividad en clasificación textual implica considerar varias dimensiones al mismo tiempo. Una sola métrica no basta para describir el comportamiento del modelo. En esta investigación, la efectividad se interpreta de forma integrada a partir de precisión, recall, F1 y costo computacional. En términos de clasificación binaria, las métricas básicas son:



\begin{equation}

\text{Precisión} = \frac{TP}{TP+FP}

\label{eq:precision}

\end{equation}



\begin{equation}

\text{Recall} = \frac{TP}{TP+FN}

\label{eq:recall}

\end{equation}



\begin{equation}

F1 = \frac{2 \cdot \text{Precisión} \cdot \text{Recall}}{\text{Precisión} + \text{Recall}}

\label{eq:f1}

\end{equation}



La precisión indica cuántas de las predicciones positivas fueron correctas; el recall mide cuántos positivos reales fueron recuperados; y el F1 resume ambos aspectos en una sola medida. Aunque en clasificación multiclase se utilizan variantes macro y micro, la lógica es la misma: una técnica es más efectiva si consigue equilibrio entre acierto, cobertura y estabilidad.



En la literatura sobre Naive Bayes, la comparación con otros clasificadores ha demostrado que el análisis debe ser más amplio que la simple exactitud global. Zhang et al. proponen una comparación bayesiana de clasificadores de texto para evitar las limitaciones de las pruebas frecuentistas tradicionales y capturar de forma más realista la incertidumbre de los resultados \cite{10.1145/2911451.2911547}. Esto es importante porque la \textit{efectividad} de un clasificador no se reduce a un número aislado; también incluye robustez, interpretabilidad, costo de entrenamiento y sensibilidad al contexto.



\subsection{Variantes y mejoras del algoritmo}



El análisis de la literatura muestra que el Naive Bayes clásico suele mejorarse mediante cuatro líneas técnicas principales: selección de características, ponderación de atributos, relajación del supuesto de independencia y adaptación al dominio semántico o al cambio de distribución.



La primera línea de mejora es la selección de características. En textos, el vocabulario suele ser muy amplio y gran parte de los términos aporta poca discriminación. Chen et al. proponen métricas específicas de evaluación de rasgos para Naive Bayes, mientras que Youn y Jeong introducen un esquema de \textit{class dependent feature scaling} que incrementa la capacidad de discriminación del modelo \cite{CHEN20095432,YOUN2009477}. De modo semejante, Tang, Kay y He muestran que la selección óptima de características puede mejorar significativamente la clasificación con Naive Bayes sin sacrificar su simplicidad \cite{Tang20162508}.



La segunda línea es la ponderación de características. Kim et al. muestran que la normalización por documento y el \textit{feature weighting} permiten que Naive Bayes compita con métodos más complejos en clasificación textual \cite{Kim2006}. Jiang et al. van más allá al proponer una ponderación profunda de características que mejora el modelo base en múltiples conjuntos de datos \cite{Jiang2016}. En una dirección similar, Zhang et al. presentan dos enfoques de ponderación que mantienen el bajo costo computacional y elevan la precisión \cite{ZHANG2016137}. Estas propuestas son especialmente relevantes porque resuelven una debilidad conocida del modelo: su tratamiento uniforme de las palabras dentro de una clase.



La tercera línea es la relajación del supuesto de independencia condicional. Ganiz et al. proponen un Naive Bayes de orden superior, no IID, capaz de capturar dependencias que el modelo clásico ignora \cite{Ganiz20111022}. Ding et al. desarrollan un clasificador bayesiano novedoso que busca relajaciones funcionales de ese supuesto \cite{4554061}. Más recientemente, Gan et al. adaptan \textit{hidden naive Bayes} para texto, y El Hindi et al. proponen algoritmos de \textit{lazy fine-tuning} para mejorar el desempeño en clasificación textual \cite{Gan2021,ELHINDI2020106652}. Estos trabajos muestran que el modelo sigue evolucionando sin perder su esencia probabilística.



La cuarta línea es la adaptación al dominio semántico o al cambio de distribución. Kim et al. integran información basada en Wikipedia para construir un Naive Bayes semántico con alta efectividad en corpora de referencia \cite{KIM2018128}. En otro contexto, Dai et al. desarrollan un enfoque de transferencia de conocimiento entre dominios con Naive Bayes para cuando los datos de entrenamiento y prueba no siguen la misma distribución \cite{10.5555/1619645.1619732}. Ambas propuestas confirman que Naive Bayes no es un algoritmo estático; puede ampliarse para responder mejor a condiciones complejas y heterogéneas.



La tabla siguiente resume, desde una perspectiva técnica, las principales dimensiones que aparecen reiteradamente en la literatura revisada.



\begin{table}[htbp]

\centering

\caption{Dimensiones técnicas de la efectividad de Naive Bayes en clasificación de textos}

\label{tab:dimensiones}

\begin{tabular}{|p{3.2cm}|p{6.0cm}|p{5.3cm}|}

\hline

\textbf{Dimensión} & \textbf{Hallazgo recurrente en la literatura} & \textbf{Implicación técnica} \\

\hline

Precisión & Mejora cuando se combinan selección y ponderación de características \cite{Kim2006,Jiang2016,ZHANG2016137}. & Aumenta la capacidad discriminativa del modelo. \\

\hline

Robustez & Funciona bien en textos cortos, corpus pequeños y dominios específicos \cite{Sangounpao2019,Awotunde2023131,Pratmanto2020}. & Es útil en escenarios reales con datos limitados. \\

\hline

Adaptabilidad & Variantes como higher-order NB, hidden NB y semantic NB extienden el modelo base \cite{Ganiz20111022,Gan2021,KIM2018128}. & El algoritmo puede adaptarse a contextos más complejos. \\

\hline

Estabilidad & El suavizado y el ajuste de priors reducen errores de estimación \cite{Frank2006,10.1007/978-3-540-71496-5_73}. & Evita probabilidades nulas y sesgo por clases. \\

\hline

Interpretabilidad & Su formulación probabilística es clara y directa \cite{Kim2006,Frank2006}. & Facilita su explicación y uso académico. \\

\hline

Costo computacional & Mantiene baja complejidad de entrenamiento y predicción \cite{Jiang2016,CHEN20095432}. & Es viable para sistemas con recursos limitados. \\

\hline

\end{tabular}

\end{table}



\begin{figure}[htbp]

\centering

\includegraphics[width=0.92\textwidth]{figuras/estructura_conceptual_naive_bayes.png}

\caption{Estructura conceptual del clasificador Naive Bayes aplicado a documentos de texto.}

\label{fig:estructura_nb}

\end{figure}



\section{Metodología y análisis de la literatura}



\subsection{Estrategia metodológica general}



La metodología seguida para este capítulo se apoyó en la lógica general de trabajo usada durante toda la asignatura. Primero, la pregunta de investigación se descompuso en palabras clave principales y términos asociados. Después, se construyeron cadenas de búsqueda con operadores lógicos para recuperar estudios en bases como IEEE Xplore y ACM Digital Library. El primer corte produjo una matriz inicial de cinco artículos científicos, lo que permitió empezar la extracción y la lectura analítica de manera controlada.



Posteriormente, la búsqueda se amplió a fuentes como ScienceDirect, Springer y Lens para reunir un corpus de veinte referencias sólidas y luego, en una fase de mayor refinamiento, se utilizó Scopus para obtener metadatos y consolidar una base de cuarenta y cuatro artículos relacionados con la pregunta de investigación. En ese proceso se usaron Mendeley o Zotero para la gestión bibliográfica, Overleaf para la escritura en LaTeX y NotebookLM para jerarquizar y organizar la información extraída. Esta secuencia metodológica no solo permitió localizar literatura, sino también clasificarla, compararla y convertirla en evidencia argumentativa para responder la pregunta planteada.



\begin{figure}[htbp]

\centering

\includegraphics[width=0.9\textwidth]{figuras/flujo_metodologico_general.png}

\caption{Flujo metodológico general seguido para la búsqueda, selección y análisis de la literatura.}

\label{fig:flujo_metodologico}

\end{figure}



La lógica de selección de la literatura se basó en dos criterios centrales: relevancia temática y aporte técnico. La relevancia temática se definió por la relación directa del artículo con Naive Bayes y clasificación textual; el aporte técnico, por su capacidad para explicar, mejorar o comparar el comportamiento del algoritmo. Bajo esa lógica, los trabajos que estudian técnicas de selección de rasgos, ponderación, suavizado, adaptación semántica o relajación del supuesto de independencia fueron considerados más útiles que aquellos centrados únicamente en aplicaciones muy específicas sin discusión metodológica profunda.



\begin{table}[htbp]

\centering

\caption{Criterios de inclusión y exclusión empleados en el análisis bibliográfico}

\label{tab:criterios}

\begin{tabular}{|p{3.2cm}|p{5.8cm}|p{5.5cm}|}

\hline

\textbf{Criterio} & \textbf{Inclusión} & \textbf{Exclusión} \\

\hline

Relación con el tema & Estudios centrados en Naive Bayes, clasificación de texto o variantes del modelo. & Trabajos sin vínculo directo con clasificación textual o sin referencia al algoritmo. \\

\hline

Aporte técnico & Artículos que mejoran, comparan o adaptan el clasificador. & Estudios meramente descriptivos sin aporte metodológico claro. \\

\hline

Tipo de evidencia & Experimentos, métricas de clasificación, análisis comparativo, validación cruzada. & Opiniones no justificadas o textos sin metodología explícita. \\

\hline

Utilidad para la pregunta & Fuentes que ayudan a responder qué tan efectivo es Naive Bayes en texto. & Fuentes que no permiten extraer conclusiones sobre desempeño. \\

\hline

\end{tabular}

\end{table}



\subsection{Estructura de la evidencia recuperada}



La revisión bibliográfica mostró una evolución ordenada en varias etapas: búsqueda inicial de cinco artículos, análisis de brechas, clasificación de enfoques, mapa conceptual, formulación de objetivos, ampliación a veinte fuentes y, finalmente, recuperación de cuarenta y cuatro artículos con metadatos completos. Esta secuencia es importante porque demuestra trazabilidad y madurez progresiva del proyecto. No se trató de acumular referencias de manera indiscriminada, sino de construir un corpus cada vez más preciso y útil.



\begin{table}[htbp]

\centering

\caption{Síntesis de las etapas de construcción del corpus bibliográfico}

\label{tab:etapas}

\begin{tabular}{|p{2.4cm}|p{2.8cm}|p{8.0cm}|}

\hline

\textbf{Etapa} & \textbf{Producto} & \textbf{Propósito} \\

\hline

APE2 & Matriz de cinco artículos & Obtener evidencia preliminar sobre la efectividad del algoritmo. \\

\hline

APE3 & Análisis de brechas & Identificar limitaciones, vacíos y problemas recurrentes. \\

\hline

ACD3 & Tabla de enfoques & Verificar el tipo de investigación predominante en la literatura. \\

\hline

AA3 & Mapa conceptual & Delimitar problema, contexto, actores y objetivos. \\

\hline

APE4 & Pregunta y objetivos & Traducir la brecha en una ruta de investigación clara. \\

\hline

APE5 & Veinte fuentes & Consolidar antecedentes y ampliar el estado del arte. \\

\hline

APE6 & Cuarenta y cuatro artículos y BibTeX & Organizar la base documental final para el análisis técnico. \\

\hline

AA6 & Antecedentes iniciales & Sintetizar la evidencia en una narrativa académica coherente. \\

\hline

\end{tabular}

\end{table}



\subsection{Análisis temático de la literatura}



Al analizar las cuarenta y cuatro fuentes reunidas, la evidencia se agrupa en cinco grandes ejes: mejoras al modelo base, selección y ponderación de características, variantes no IID o de orden superior, adaptación semántica o por transferencia, y aplicaciones en dominios específicos. Esa organización permite ver que la efectividad de Naive Bayes no es uniforme, sino dependiente del tipo de problema textual.



\paragraph{1. Mejoras al modelo base}



Los estudios más tempranos muestran que el Naive Bayes multinomial puede mejorar notablemente si se corrigen sus problemas de estimación. Kim et al. proponen normalización por documento y ponderación de características, obteniendo resultados comparables a clasificadores más complejos \cite{Kim2006}. De forma similar, Kibriya et al. revisan el desempeño del modelo multinomial y señalan que TF-IDF y la normalización son componentes importantes para elevar su rendimiento \cite{Kibriya2005}. En esta misma línea, Schneider enfatiza que el bajo desempeño de Naive Bayes no se debe a una falla total del método, sino a una modelación incompleta del texto y a una selección inadecuada de atributos \cite{10.1007/978-3-540-30586-6_76}.



\paragraph{2. Selección y ponderación de características}



La literatura es consistente al señalar que la selección de rasgos es uno de los factores más importantes para la efectividad del algoritmo. Chen et al. proponen medidas específicas para seleccionar características relevantes en textos multiclase \cite{CHEN20095432}. Youn y Jeong presentan una técnica de escalado dependiente de la clase que mejora la capacidad del clasificador para distinguir entre categorías \cite{YOUN2009477}. Tang, Kay y He muestran, además, que acercarse a una selección óptima puede traducirse en mejoras sustanciales de desempeño sin comprometer la simplicidad del modelo \cite{Tang20162508}. A esto se suman Jiang et al., quienes incorporan \textit{deep feature weighting}, y Zhang et al., que diseñan dos estrategias de ponderación con beneficios concretos en precisión \cite{Jiang2016,ZHANG2016137}.



\paragraph{3. Variantes no IID y modelos extendidos}



Una de las limitaciones más conocidas del modelo clásico es su supuesto de independencia condicional. Cuando las palabras están correlacionadas, la hipótesis naive se vuelve demasiado restrictiva. Ganiz et al. responden a este problema proponiendo un Naive Bayes de orden superior que modela dependencias entre atributos \cite{Ganiz20111022}. Ding et al. también presentan un clasificador bayesiano novedoso que busca relajaciones funcionales de ese supuesto \cite{4554061}. Más recientemente, Gan et al. adaptan \textit{hidden naive Bayes} para texto y El Hindi et al. proponen un mecanismo de \textit{lazy fine-tuning} para mejorar el desempeño local del modelo \cite{Gan2021,ELHINDI2020106652}. Estos trabajos demuestran que Naive Bayes sigue siendo una plataforma fértil para el desarrollo de variantes técnicas.



\paragraph{4. Adaptación semántica y transferencia entre dominios}



Otra línea de evolución importante consiste en incorporar información semántica o de dominio. Kim et al. utilizan conceptos asociados a Wikipedia para enriquecer la representación documental y mejorar el clasificador \cite{KIM2018128}. Dai et al. muestran que el modelo puede adaptarse mediante transferencia entre dominios cuando el conjunto de prueba y entrenamiento difieren sustancialmente \cite{10.5555/1619645.1619732}. Este tipo de trabajos amplía la aplicabilidad del método y demuestra que la simplicidad del modelo no impide introducir conocimiento adicional.



\paragraph{5. Aplicaciones en dominios específicos}



La efectividad de Naive Bayes también se verifica en tareas concretas. Sangounpao y Muenchaisri lo aplican a texto corto en un conjunto de datos pequeño, con apoyo ontológico \cite{Sangounpao2019}. Awotunde et al. lo integran en un sistema de análisis de reseñas de hoteles \cite{Awotunde2023131}. Pratmanto et al. lo usan en análisis de opiniones sobre aplicaciones móviles y Musleh et al. lo aplican al análisis de comentarios en YouTube \cite{Pratmanto2020,Musleh2023}. También se reportan usos en textos cortos en polaco, clasificación académica y categorización documental \cite{Wawer20191321,Humaidi2023,Wang2007,Mendoza2011251}. Estos estudios no siempre buscan perfeccionar el algoritmo, pero sí demuestran que su desempeño práctico sigue siendo útil en contextos variados.



\begin{table}[htbp]

\centering

\caption{Estrategias de mejora de Naive Bayes y su efecto observado en la literatura}

\label{tab:mejoras}

\begin{tabular}{|p{4.1cm}|p{3.4cm}|p{4.0cm}|p{4.0cm}|}

\hline

\textbf{Estrategia} & \textbf{Referencias representativas} & \textbf{Efecto principal} & \textbf{Observación técnica} \\

\hline

Normalización y ponderación por documento & \cite{Kim2006,10.1007/978-3-540-30549-1_43} & Mejora la calidad de la estimación de probabilidades. & Permite competir con clasificadores más complejos. \\

\hline

Selección de características & \cite{CHEN20095432,YOUN2009477,Tang20162508} & Reduce ruido y esparsidad del vocabulario. & Incrementa discriminación y estabilidad. \\

\hline

Ponderación de características & \cite{Jiang2016,ZHANG2016137,Ruan202020151} & Ajusta el peso de términos relevantes por clase. & Eleva la precisión sin perder simplicidad. \\

\hline

Suavizado y ajuste de priors & \cite{Frank2006,10.1007/978-3-540-71496-5_73} & Evita probabilidades nulas y sesgo por clases desbalanceadas. & Mejora robustez y estabilidad numérica. \\

\hline

Modelos no IID o de orden superior & \cite{Ganiz20111022,4554061,Gan2021} & Captura dependencias entre términos. & Reduce la rigidez del supuesto naive. \\

\hline

Adaptación semántica o por transferencia & \cite{KIM2018128,10.5555/1619645.1619732} & Mejora rendimiento en dominios cambiantes o enriquecidos semánticamente. & Amplía la aplicabilidad del modelo. \\

\hline

Ajuste local y fine-tuning & \cite{ELHINDI2020106652} & Recalibra probabilidades según vecinos cercanos o contexto local. & Es útil cuando el conjunto de entrenamiento es limitado. \\

\hline

\end{tabular}

\end{table}



\subsection{Síntesis del análisis de la literatura}



El análisis integrado de la evidencia permite formular una conclusión intermedia muy clara: Naive Bayes es técnicamente efectivo para clasificación textual, pero su rendimiento depende del tratamiento previo del texto y del tipo de mejora aplicada al modelo. En su forma básica puede quedar por debajo de métodos más sofisticados en algunos conjuntos de datos, pero con selección de características, ponderación, suavizado y ajustes estructurales, su comportamiento mejora de manera consistente \cite{Kim2006,Frank2006,Jiang2016,ZHANG2016137,Tang20162508}.



La literatura también sugiere que la comparación entre clasificadores no debe hacerse únicamente con la idea de \textit{ganador absoluto}. Zhang et al. muestran que la comparación bayesiana ofrece una visión más completa que las pruebas tradicionales \cite{10.1145/2911451.2911547}. Ese enfoque es importante porque, en clasificación textual, el mejor clasificador no siempre es el más complejo, sino el que mejor se adapta al corpus, a la métrica y a las restricciones de uso. En ese sentido, Naive Bayes conserva ventaja en escenarios donde se valora rapidez, interpretabilidad y capacidad suficiente con recursos limitados.



\begin{figure}[htbp]

\centering

\includegraphics[width=0.9\textwidth]{figuras/relacion_mejoras_naive_bayes.png}

\caption{Relación entre las principales técnicas de mejora y el incremento observado en la efectividad de Naive Bayes.}

\label{fig:relacion_mejoras}

\end{figure}



\section{Conclusiones}



La pregunta de investigación planteada en este capítulo puede responderse con base en la evidencia revisada: Naive Bayes es una técnica efectiva para clasificación de texto, pero su efectividad es condicional y no absoluta. Su desempeño es especialmente sólido cuando el problema presenta alta dimensionalidad, textos breves, necesidad de interpretación rápida y restricciones de costo computacional. En esos escenarios, el clasificador mantiene una relación favorable entre simplicidad y rendimiento \cite{Kim2006,Frank2006,Sangounpao2019,Awotunde2023131}.



Sin embargo, la efectividad del modelo mejora de forma notoria cuando se aplican técnicas complementarias. La selección de características reduce ruido y esparsidad; la ponderación de atributos incrementa la discriminación entre clases; el suavizado corrige probabilidades nulas; y las variantes no IID, semánticas o de ajuste local compensan las limitaciones del supuesto de independencia condicional \cite{CHEN20095432,YOUN2009477,Jiang2016,ZHANG2016137,Ganiz20111022,Gan2021,ELHINDI2020106652}. Por tanto, el Naive Bayes clásico debe entenderse como una base metodológica robusta, pero no necesariamente como su forma final más potente.



También se concluye que la comparación justa de Naive Bayes con otros clasificadores exige una evaluación rigurosa. En algunos corpora, variantes mejoradas del modelo pueden acercarse a la precisión de clasificadores más complejos e incluso competir de forma equilibrada con ellos \cite{Kim2006,10.1145/2911451.2911547,KIM2018128}. Esto confirma que la simplicidad no implica necesariamente bajo rendimiento; más bien, obliga a analizar cuidadosamente el tipo de problema, la calidad de las características y la estrategia de modelado empleada.



En síntesis, Naive Bayes sigue siendo una técnica vigente, útil y teóricamente sólida para la clasificación de textos. No es el clasificador universalmente mejor, pero sí uno de los más versátiles y didácticos para construir soluciones de minería textual cuando se combina con técnicas de mejora apropiadas. Desde el punto de vista técnico, su efectividad no radica únicamente en la fórmula bayesiana, sino en la manera en que se adapta a la estructura real del lenguaje y a las condiciones del corpus.



\section{Referencias}



\nocite{*}

\bibliographystyle{IEEEtran}

\bibliography{referencias}

```



