# prompt1
convierte el siguiente PDF a formato markdown

# what?
En cuanto a los objetivos, no hagas eso, solo necesito las 3 preguntas

# prompt1
A continuación quiero que me ayudes con la realización de una actividad académica, pero para poder desarrollarla, es necesario que yo te proporcione contexto, es decir las versiones o archivos previos. Entonces yo te iré pasando poco a poco y tú debes analizar la información y recordar en tu contexto para que al final puedas realizar la actividad que te pido.

# prompt2
bibliografías o referencias BibTex:
```bib
@article{Kim2006,
   abstract = {While naive Bayes is quite effective in various data mining tasks, it shows a disappointing result in the automatic text classification problem. Based on the observation of naive Bayes for the natural language text, we found a serious problem in the parameter estimation process, which causes poor results in text classification domain. In this paper, we propose two empirical heuristics: per-document text normalization and feature weighting method. While these are somewhat ad hoc methods, our proposed naive Bayes text classifier performs very well in the standard benchmark collections, competing with state-of-the-art text classifiers based on a highly complex learning method such as SVM. © 2006, IEEE. All rights reserved.},
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
   abstract = {Content less than two hundred words like comments or review statements is known as a short text. Short text classification is useful for automatically categorizing sentence into predefined group. There are several traditional short text classification methods by using bag-of-words with k nearest neighbors (k-NN), Naïve Bayes, Maximum entropy, support vector machines (SVMs), and an algorithm based on statistics and rules. The deep learning method is outperformed other methods on classification of short text with normal size of dataset. Some researches classify requirements into functional and nonfunctional requirements. There is no research on multi-classification of functional requirements with a small dataset particularly for an accounting field. This paper presents an approach to classify short text for a small dataset into multiple categories of functional requirements on the accounting domain. The proposed approach uses an ontology to construct bag-of-words and uses Naive Bayes to classify for small dataset. The experiment is conducted using four hundred of datasets with 5folds and 10-folds cross-validation. The result shows that the method can correctly classify more than 80%. Additionally, comparisons between the ontology-based Naive Bayes method and other methods are investigated.},
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
   abstract = {Multinomial naive Bayes (MNB) is a popular method for document classification due to its computational efficiency and relatively good predictive performance. It has recently been established that predictive performance can be improved further by appropriate data...},
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
@article{Zhang2016,
   abstract = {How can we know whether one classifier is really better than the other? In the area of text classification, since the publication of Yang and Liu's seminal SIGIR-1999 paper, it has become a standard practice for researchers to apply nullhypothesis significance testing (NHST) on their experimental results in order to establish the superiority of a classifier. However, such a frequentist approach has a number of inherent deficiencies and limitations, e.g., the inability to accept the null hypothesis (that the two classifiers perform equally well), the difficulty to compare commonly-used multivariate performance measures like F1 scores instead of accuracy, and so on. In this paper, we propose a novel Bayesian approach to the performance comparison of text classifiers, and argue its advantages over the traditional frequentist approach based on t-test etc. In contrast to the existing probabilistic model for F1 scores which is unpaired, our proposed model takes the correlation between classifiers into account and thus achieves greater statistical power. Using several typical text classification algorithms and a benchmark dataset, we demonstrate that the our approach provides rich information about the difference between two classifiers' performances.},
   author = {Dell Zhang and Jun Wang and Emine Yilmaz and Xiaoling Wang and Yuxin Zhou},
   doi = {10.1145/2911451.2911547;SUBPAGE:STRING:BASIC},
   isbn = {9781450342902},
   journal = {SIGIR 2016 - Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval},
   keywords = {Bayesian inference,Hypothesis testing,Performance evaluation,Text classification},
   month = {7},
   pages = {15-24},
   publisher = {Association for Computing Machinery, Inc},
   title = {Bayesian performance comparison of text classifiers},
   url = {/doi/pdf/10.1145/2911451.2911547?download=true},
   year = {2016}
}
@article{Jiang2016,
   abstract = {Naive Bayes (NB) continues to be one of the top 10 data mining algorithms due to its simplicity, efficiency and efficacy. Of numerous proposals to improve the accuracy of naive Bayes by weakening its feature independence assumption, the feature weighting approach has received less attention from researchers. Moreover, to our knowledge, all of the existing feature weighting approaches only incorporate the learned feature weights into the classification of formula of naive Bayes and do not incorporate the learned feature weights into its conditional probability estimates at all. In this paper, we propose a simple, efficient, and effective feature weighting approach, called deep feature weighting (DFW), which estimates the conditional probabilities of naive Bayes by deeply computing feature weighted frequencies from training data. Empirical studies on a collection of 36 benchmark datasets from the UCI repository show that naive Bayes with deep feature weighting rarely degrades the quality of the model compared to standard naive Bayes and, in many cases, improves it dramatically. Besides, we apply the proposed deep feature weighting to some state-of-the-art naive Bayes text classifiers and have achieved remarkable improvements.},
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
```

referencias IEEE:
```markdown
\[1\] S. B. Kim, K. S. Han, and H. C. Rim, “Some effective techniques for naive bayes text classification,” IEEE Transactions on Knowledge and Data Engineering, vol. 18, no. 11, pp. 1457–1466, Nov. 2006, doi: 10.1109/TKDE.2006.180.

\[2\] K. Sangounpao and P. Muenchaisri, “Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset,” in Proc. 20th IEEE/ACIS Int. Conf. on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD), Toyama, Japan, 2019, pp. 53–58, doi: 10.1109/SNPD.2019.8935711.

\[3\] E. Frank and R. R. Bouckaert, “Naïve Bayes for text classification with unbalanced classes,” in Proc. 10th Eur. Conf. on Principles and Practice of Knowledge Discovery in Databases (PKDD), Berlin, Germany, 2006, pp. 503–510, doi: 10.1007/11871637\_49. 

\[4\] D. Zhang, J. Wang, E. Yilmaz, X. Wang, and Y. Zhou, “Bayesian performance comparison of text classifiers,” in Proc. 39th Int. ACM SIGIR Conf. on Research and Development in Information Retrieval (SIGIR), Pisa, Italy, 2016, pp. 15–24, doi: 10.1145/2911451.2911547. 

\[5\] L. Jiang, C. Li, S. Wang, and L. Zhang, “Deep feature weighting for naive Bayes and its application to text classification,” Engineering Applications of Artificial Intelligence, vol. 52, pp. 26–39, Jun. 2016, doi: 10.1016/j.engappai.2016.02.002.
```

# prompt3
archivo1:
```markdown
**Reporte Técnico de Actividades**  
**Práctico-Experimentales Nro. 001**

1. # Datos de Identificación del Estudiante y la Práctica

| Nombre del estudiante(s) | Wilson Patricio Palma Samaniego |
| :---- | :---- |
| **Asignatura** | Metodología de la Investigación en Computación |
| **Ciclo** | 4 A |
| **Unidad** | 1 |
| **Resultado de aprendizaje de la unidad** | R1. Contrasta la investigación y sus tipos con los métodos en el área de Computación y afines. |
| **Práctica Nro.** | 002 |
| **Título de la Práctica** | Clasificación de artículos según tipo de investigación y área de aplicación |
| **Nombre del Docente** | Luis Antonio Chamba Eras |
| **Fecha** | Martes 21 de abril de 2026 |
| **Horario** | 10h30 – 11h30 |
| **Lugar** | EVA-Moodle / Aula |
| **Tiempo planificado en el Sílabo** | 1 hora |

2. # Objetivo(s) de la Práctica

Clasificar artículos científicos y proyectos de investigación según su tipo (básica, aplicada,

tecnológica) y área de aplicación, vinculándolos con las sublíneas de la Carrera.

3. # Materiales, Reactivos, Equipos y Herramientas

**Materiales y reactivos:**

* Computador con acceso a Internet

* 5 artículos científicos preseleccionados por el docente

* Tabla de clasificación proporcionada en EVA-Moodle

* Mendeley o Zotero

**Equipos y herramientas:**

EVA-Moodle; guía institucional de práctica.

4. # Procedimiento / Metodología Ejecutada

Desarrollo (ABI – Aprendizaje Basado en Investigación):

1\. Recibir los 5 artículos científicos asignados por el docente.

2\. Leer el resumen, introducción y metodología de cada artículo.

3\. Identificar el tipo de investigación de cada artículo.

4\. Clasificar cada artículo según su área de aplicación y sublínea de la Carrera.

5\. Completar la tabla de clasificación con justificación breve.

6\. Subir el reporte técnico en PDF a EVA-Moodle.

5. # Resultados

   1. ## Matriz de Extracción de Artículos Científicos

      1. ### Información general del estudiante

* **Nombre del estudiante:** Wilson Palma  
* **Técnica de IA:** Aprendizaje automático supervisado (Machine Learning)  
* **Pregunta de investigación:** ¿Qué tan efectivo es Naive Bayes en clasificación de texto?

  2. ### Matriz de extracción (5 artículos)

| \# | Referencia (IEEE) | Año | Base de datos | Técnica IA | Problema abordado | Objetivo del artículo | Metodología | Dataset / Contexto | Resultados principales | Limitaciones | Aporte para la PI |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | S. B. Kim, K. S. Han y H. C. Rim, “Some Effective Techniques for Naive Bayes Text Classification,” IEEE Transactions on Knowledge and Data Engineering, vol. 18, no. 11, pp. 1457–1466, 2006\. doi: 10.1109/TKDE.2006.180 | 2006 | IEEE | Naive Bayes con normalización por documento y feature weighting | El Naive Bayes estándar obtiene resultados pobres en clasificación de texto por problemas en la estimación de parámetros | Mejorar el desempeño de Naive Bayes en clasificación de texto | Propuesta de dos heurísticas empíricas: normalización por documento y ponderación de características | Colecciones de referencia / benchmark estándar para clasificación de texto | El clasificador propuesto compite muy bien y puede llegar a rendir de forma cercana a clasificadores más complejos como SVM | Las heurísticas son ad hoc y dependen del ajuste experimental | Demuestra que Naive Bayes sí puede ser muy efectivo en texto cuando se lo mejora con normalización y ponderación |
| 2 | K. Sangounpao y P. Muenchaisri, “Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset,” Proceedings of the 20th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD), pp. 53–58, 2019\. doi: 10.1109/SNPD.2019.8935711 | 2019 | IEEE | Naive Bayes basado en ontología | Clasificación de texto corto con un conjunto de datos pequeño | Proponer una metodología de clasificación basada en ontología para mejorar Naive Bayes en texto corto | Construcción de ontología y uso de esa ontología dentro del proceso de clasificación | Dataset pequeño de texto corto / contexto de clasificación breve | El artículo propone y evalúa un enfoque viable para texto corto, mostrando que la ontología ayuda a estructurar mejor la clasificación | El tamaño reducido del dataset limita la generalización | Aporta una variante útil de Naive Bayes para escenarios de texto corto y datos escasos |
| 3 | E. Frank y R. R. Bouckaert, “Naive Bayes for Text Classification with Unbalanced Classes,” in Knowledge Discovery in Databases: PKDD 2006, Lecture Notes in Computer Science, vol. 4213, pp. 503–510, 2006\. doi: 10.1007/11871637\_49 | 2006 | Springer (LNCS) | Multinomial Naive Bayes con ajuste de priors | Desequilibrio de clases en clasificación de texto | Mejorar el rendimiento de MNB en datasets desbalanceados | Corrección por ajuste de priors de atributos / normalización adicional | Datasets desbalanceados para clasificación de documentos | La corrección propuesta mejora significativamente el área bajo la curva ROC | Se enfoca en MNB y en el problema de desbalance, no en todos los escenarios posibles | Muestra que Naive Bayes puede ser más efectivo cuando se corrige el sesgo por clases desbalanceadas |
| 4 | D. Zhang, J. Wang, E. Yilmaz, X. Wang y Y. Zhou, “Bayesian Performance Comparison of Text Classifiers,” in Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’16), pp. 15–24, 2016\. doi: 10.1145/2911451.2911547 | 2016 | ACM | Evaluación bayesiana de clasificadores de texto | Comparar de forma confiable si un clasificador es realmente mejor que otro | Proponer un enfoque bayesiano para comparar rendimiento de clasificadores de texto | Inferencia bayesiana para comparar diferencias de desempeño y medir incertidumbre | Algoritmos representativos de clasificación de texto y un dataset de benchmark | El método ofrece información más rica que NHST; además, el artículo muestra que NBMult, cuando se mejora con TF-IDF y normalización, puede ser prácticamente equivalente a SVM bajo ciertos márgenes | No es un nuevo clasificador, sino un marco de evaluación | Ayuda a interpretar con más rigor cuán efectivo es Naive Bayes frente a otros clasificadores |
| 5 | L. Jiang, C. Li, S. Wang y L. Zhang, “Deep feature weighting for naive Bayes and its application to text classification,” Engineering Applications of Artificial Intelligence, vol. 52, pp. 26–39, 2016\. doi: 10.1016/j.engappai.2016.02.002 | 2016 | Scopus | Naive Bayes con deep feature weighting | La suposición de independencia y la forma clásica de estimar probabilidades limitan la precisión de Naive Bayes | Mejorar Naive Bayes incorporando ponderación profunda de características | Cálculo profundo de frecuencias ponderadas dentro de las probabilidades condicionales | 36 datasets benchmark de UCI y aplicaciones a clasificadores Naive Bayes para texto | Rara vez empeora el modelo estándar y en muchos casos lo mejora de forma marcada; además, logra mejoras notables en clasificadores de texto basados en NB | La validación se apoya en benchmarks; requiere más procesamiento que NB básico | Refuerza la idea de que Naive Bayes puede ser muy competitivo en clasificación de texto si se mejora su representación de características |

     3. ### Síntesis de los artículos

En conjunto, la evidencia muestra que Naive Bayes sí es efectivo en clasificación de texto, pero su rendimiento mejora mucho cuando se corrigen sus debilidades clásicas. El artículo de Kim et al. muestra que la normalización por documento y la ponderación de características pueden llevar a un rendimiento comparable al de clasificadores más complejos. Frank y Bouckaert demuestran que el ajuste de priors mejora el comportamiento de Naive Bayes en clases desbalanceadas. Jiang et al. refuerzan esta idea con deep feature weighting, mostrando mejoras claras sobre la versión estándar. Sangounpao y Muenchaisri amplían el uso de Naive Bayes a texto corto con ontologías, mientras que Zhang et al. aportan una forma más rigurosa de comparar si un clasificador realmente supera a otro.

4. ### Respuesta a la pregunta de investigación

Naive Bayes es una técnica efectiva para clasificación de texto, especialmente cuando se adapta al problema concreto. En su versión básica puede quedar por debajo de métodos más complejos, pero con mejoras como normalización, ponderación de características, ajuste de priors, uso de ontologías o feature weighting profundo, su desempeño puede ser muy competitivo e incluso aproximarse al de clasificadores como SVM en algunos escenarios. Por eso, más que preguntar si Naive Bayes “sirve” o no, la evidencia indica que su efectividad depende mucho de cómo se implemente y del tipo de texto que se clasifique.

6. # Preguntas de Control

* **¿Qué criterios permiten distinguir una investigación aplicada de una investigación tecnológica en computación?**

Una investigación aplicada se distingue porque busca resolver un problema concreto o responder a una necesidad específica mediante la utilización de conocimientos ya existentes. Su énfasis está en la utilidad inmediata y en la validación de una solución en un contexto real o cercano a la realidad. En cambio, una investigación tecnológica en computación se orienta al diseño, mejora o implementación de artefactos, métodos, sistemas o herramientas tecnológicas, con el fin de optimizar procesos o generar una solución funcional. En este tipo de investigación, el producto final suele ser un sistema, prototipo, algoritmo o método que puede ser probado y evaluado técnicamente.

* **¿Cómo se vincula el tipo de investigación con la sublínea de investigación de la Carrera?**

El tipo de investigación se vincula con la sublínea de investigación porque esta define el enfoque específico dentro del área general de la carrera. En una sublínea orientada al desarrollo de software, inteligencia artificial o análisis de datos, una investigación aplicada permite resolver problemas prácticos mediante modelos o técnicas existentes, mientras que una investigación tecnológica impulsa la creación o mejora de herramientas computacionales. De esta manera, el tipo de investigación guía la forma en que se aborda el problema, la metodología utilizada y el tipo de resultados esperados dentro de la sublínea académica.

7. # Conclusiones

La práctica permitió comprender que la investigación en computación puede orientarse tanto a la solución de problemas concretos como al desarrollo de propuestas tecnológicas. Asimismo, se identificó que la relación entre investigación aplicada y sublínea de investigación es fundamental para definir el alcance, la metodología y los resultados del trabajo académico. En función del objetivo planteado, se concluye que la correcta clasificación del tipo de investigación facilita la organización del estudio y permite al estudiante justificar con mayor claridad el enfoque metodológico de su trabajo.

8. # Recomendaciones

Se recomienda analizar primero el problema de investigación para determinar si corresponde a un enfoque aplicado o tecnológico antes de redactar el documento académico. También es conveniente revisar la sublínea de investigación de la carrera para asegurar coherencia entre el tema, los objetivos y la metodología. En casos reales, se sugiere apoyar la investigación con ejemplos prácticos, fuentes científicas actualizadas y una delimitación clara del problema, de modo que la propuesta sea viable y tenga mayor pertinencia dentro del área de computación.

9. # Bibliografía / Referencias

   1. ## Referencias del docente:

* T. Diaz Bravo, I. Paredes Sanchez, y L. De la Luz Paredes, "Metodología de la Investigación Científica en Ingeniería en Ciencias Informáticas y carreras afines," SERIE, vol. 15, n.o 4, pp. 57-70, 2022\.

* P. Ralph et al., "Empirical Standards for Software Engineering Research," arXiv:2010.03525, 2020\.

  2. ## Referencias del estudiante:

\[1\] S. B. Kim, K. S. Han, and H. C. Rim, “Some effective techniques for naive bayes text classification,” IEEE Transactions on Knowledge and Data Engineering, vol. 18, no. 11, pp. 1457–1466, Nov. 2006, doi: 10.1109/TKDE.2006.180.

\[2\] K. Sangounpao and P. Muenchaisri, “Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset,” in Proc. 20th IEEE/ACIS Int. Conf. on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD), Toyama, Japan, 2019, pp. 53–58, doi: 10.1109/SNPD.2019.8935711.

\[3\] E. Frank and R. R. Bouckaert, “Naïve Bayes for text classification with unbalanced classes,” in Proc. 10th Eur. Conf. on Principles and Practice of Knowledge Discovery in Databases (PKDD), Berlin, Germany, 2006, pp. 503–510, doi: 10.1007/11871637\_49. 

\[4\] D. Zhang, J. Wang, E. Yilmaz, X. Wang, and Y. Zhou, “Bayesian performance comparison of text classifiers,” in Proc. 39th Int. ACM SIGIR Conf. on Research and Development in Information Retrieval (SIGIR), Pisa, Italy, 2016, pp. 15–24, doi: 10.1145/2911451.2911547. 

\[5\] L. Jiang, C. Li, S. Wang, and L. Zhang, “Deep feature weighting for naive Bayes and its application to text classification,” Engineering Applications of Artificial Intelligence, vol. 52, pp. 26–39, Jun. 2016, doi: 10.1016/j.engappai.2016.02.002.

10. # Anexos

No se generaron anexos en el desarrollo de esta actividad.
```

# prompt4
archivo2:
```markdown
**Plantilla para la Descripción del Problema Técnico**

**1. Contexto general del problema**

En el área de **Sistemas Inteligentes y Minería de Texto**, las organizaciones y unidades académicas enfrentan desafíos para clasificar automáticamente grandes volúmenes de información textual, especialmente cuando los documentos son breves, presentan vocabulario limitado o pertenecen a dominios específicos. Este problema aparece con frecuencia en entornos **educativos, administrativos e industriales**, donde se requiere organizar textos como requisitos, comentarios, correos, tickets o registros operativos de manera eficiente y consistente [1], [2].

**2. Situación actual basada en evidencia**

La literatura científica muestra que el clasificador Naive Bayes sigue siendo una alternativa relevante por su simplicidad y eficiencia; sin embargo, su desempeño en clasificación de texto puede verse afectado por problemas en la estimación de parámetros y por la independencia condicional asumida por el modelo [1]. Para mejorar sus resultados, se han propuesto técnicas como la normalización por documento y la ponderación de características, con mejoras observables sobre colecciones de referencia [1].  

En textos cortos y conjuntos de datos pequeños, se ha evidenciado que la incorporación de conocimiento de dominio mediante ontologías puede fortalecer la representación tipo bag-of-words y mejorar la clasificación multiclase, alcanzando resultados superiores al 80% en experimentos con validación cruzada [2]. Asimismo, en escenarios con clases desbalanceadas, Naive Bayes presenta limitaciones adicionales que requieren ajustes específicos para conservar su utilidad práctica [3].  

Por otro lado, la investigación reciente también ha demostrado que la ponderación profunda de características mejora de forma significativa el rendimiento de Naive Bayes en múltiples conjuntos de datos y en aplicaciones de clasificación textual [5]. Finalmente, la comparación de clasificadores de texto se ha abordado desde enfoques bayesianos más rigurosos, lo que confirma que el análisis experimental y estadístico sigue siendo central en este campo [4].

**3. Brecha o vacío identificado**

A pesar de los avances reportados, persiste una brecha significativa en el diseño de métodos que integren de forma simultánea **robustez frente a textos cortos, adaptación a dominios específicos, tratamiento de clases desbalanceadas y buen desempeño con conjuntos de datos pequeños**. La evidencia disponible muestra mejoras parciales, pero aún no resuelve por completo la necesidad de un enfoque estable y transferible para contextos con escasez de datos y alta variabilidad semántica [1], [2], [3], [5].

**4. Problema central**

El problema radica en que los métodos tradicionales de clasificación automática de texto, particularmente Naive Bayes en su forma estándar, presentan limitaciones de precisión y estabilidad al trabajar con textos cortos, datos escasos, clases desbalanceadas y dominios especializados, lo cual afecta la confiabilidad de la categorización automática de información textual [1], [3], [5].

**5. Consecuencias o impacto**

Esta situación genera consecuencias como **errores de clasificación**, **baja calidad en la organización de la información** y **dificultades para automatizar procesos de toma de decisiones**. Además, limita la construcción de sistemas de recuperación y análisis textual confiables, incrementa la carga manual de revisión y reduce la eficiencia en entornos donde la clasificación automática resulta crítica, como la gestión de requisitos, la administración documental y el análisis de comentarios o solicitudes [2], [4], [5].

**6. Actores involucrados**

Los principales actores involucrados incluyen:

* Usuarios finales que generan o consultan textos.
* Analistas o especialistas que validan categorías.
* Desarrolladores que implementan los modelos de clasificación.
* Instituciones u organizaciones que gestionan grandes volúmenes de información textual.
* Responsables de procesos que dependen de una clasificación automática precisa [2], [4].

**7. Variables o elementos clave**

Las variables clave asociadas al problema incluyen:

* **Precisión de clasificación**: grado de acierto del modelo al asignar categorías.
* **Longitud del texto**: especialmente relevante en textos cortos.
* **Tamaño del conjunto de datos**: influencia directa en la estabilidad del aprendizaje.
* **Desbalance de clases**: distribución desigual de ejemplos por categoría.
* **Representación de características**: bag-of-words, ponderación de términos y uso de conocimiento de dominio.
* **Capacidad de generalización**: habilidad del método para funcionar en distintos contextos y conjuntos de datos [1], [2], [3], [5].

**8. Delimitación del problema**

El presente problema se delimita al **análisis y mejora de la clasificación automática de texto en escenarios de datos textuales breves o con pocos ejemplos, usando principalmente enfoques basados en Naive Bayes y variantes de representación de características**. Se excluyen, por tanto, problemas de generación de texto, traducción automática, extracción de información profunda o clasificación basada exclusivamente en redes neuronales de gran escala, salvo como referencia comparativa [1], [2], [5].

**9. Vinculación con la sublínea de investigación**

Este problema se enmarca dentro de la sublínea de investigación de **Minería de Texto y Sistemas Inteligentes**, debido a que estudia métodos computacionales para organizar, clasificar y mejorar el tratamiento automático de información textual. La relación con esta sublínea se justifica porque el foco está en la optimización de algoritmos de clasificación, la representación de características lingüísticas y la evaluación experimental de su rendimiento en distintos contextos de datos [1], [4], [5].

**Referencias**

\[1\] S. B. Kim, K. S. Han, and H. C. Rim, “Some effective techniques for naive bayes text classification,” IEEE Transactions on Knowledge and Data Engineering, vol. 18, no. 11, pp. 1457–1466, Nov. 2006, doi: 10.1109/TKDE.2006.180.

\[2\] K. Sangounpao and P. Muenchaisri, “Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset,” in Proc. 20th IEEE/ACIS Int. Conf. on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD), Toyama, Japan, 2019, pp. 53–58, doi: 10.1109/SNPD.2019.8935711.

\[3\] E. Frank and R. R. Bouckaert, “Naïve Bayes for text classification with unbalanced classes,” in Proc. 10th Eur. Conf. on Principles and Practice of Knowledge Discovery in Databases (PKDD), Berlin, Germany, 2006, pp. 503–510, doi: 10.1007/11871637\_49. 

\[4\] D. Zhang, J. Wang, E. Yilmaz, X. Wang, and Y. Zhou, “Bayesian performance comparison of text classifiers,” in Proc. 39th Int. ACM SIGIR Conf. on Research and Development in Information Retrieval (SIGIR), Pisa, Italy, 2016, pp. 15–24, doi: 10.1145/2911451.2911547. 

\[5\] L. Jiang, C. Li, S. Wang, and L. Zhang, “Deep feature weighting for naive Bayes and its application to text classification,” Engineering Applications of Artificial Intelligence, vol. 52, pp. 26–39, Jun. 2016, doi: 10.1016/j.engappai.2016.02.002.
```

# prompt5
archivo3:
```markdown
# Tabla de análisis de los enfoques de investigación

| Artículos | Enfoque Cuantitativo | Enfoque Cualitativo | Enfoque mixto | Observación |
|---|---|---|---|---|
| [1] | Sí | No | No | El estudio propone y evalúa técnicas para clasificar texto con Naive Bayes mediante experimentación sobre colecciones estándar de prueba. Presenta medición de desempeño y comparación de resultados, por lo que corresponde a un enfoque cuantitativo [1]. |
| [2] | Sí | No | No | La investigación aplica un método basado en ontología y Naive Bayes sobre un conjunto de datos pequeño, usando validación cruzada y métricas de clasificación. La lógica del trabajo es experimental y medible, no interpretativa, así que se clasifica como cuantitativa [2]. |
| [3] | Sí | No | No | El artículo estudia el comportamiento de Naive Bayes para clasificación de texto en clases desbalanceadas y verifica su rendimiento mediante evaluación empírica. Al centrarse en resultados numéricos y comparación de desempeño, corresponde al enfoque cuantitativo [3]. |
| [4] | Sí | No | No | El trabajo propone un enfoque bayesiano para comparar el rendimiento de clasificadores de texto usando datos de experimentación y análisis estadístico. La investigación se apoya en evidencia cuantificable, por lo que es claramente cuantitativa [4]. |
| [5] | Sí | No | No | El estudio introduce ponderación profunda de características para Naive Bayes y la valida en 36 conjuntos de datos de referencia. Debido a que usa experimentación, métricas de desempeño y comparación de modelos, el enfoque es cuantitativo [5]. |

# Referencias

\[1\] S. B. Kim, K. S. Han, and H. C. Rim, “Some effective techniques for naive bayes text classification,” IEEE Transactions on Knowledge and Data Engineering, vol. 18, no. 11, pp. 1457–1466, Nov. 2006, doi: 10.1109/TKDE.2006.180.

\[2\] K. Sangounpao and P. Muenchaisri, “Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset,” in Proc. 20th IEEE/ACIS Int. Conf. on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD), Toyama, Japan, 2019, pp. 53–58, doi: 10.1109/SNPD.2019.8935711.

\[3\] E. Frank and R. R. Bouckaert, “Naïve Bayes for text classification with unbalanced classes,” in Proc. 10th Eur. Conf. on Principles and Practice of Knowledge Discovery in Databases (PKDD), Berlin, Germany, 2006, pp. 503–510, doi: 10.1007/11871637\_49. 

\[4\] D. Zhang, J. Wang, E. Yilmaz, X. Wang, and Y. Zhou, “Bayesian performance comparison of text classifiers,” in Proc. 39th Int. ACM SIGIR Conf. on Research and Development in Information Retrieval (SIGIR), Pisa, Italy, 2016, pp. 15–24, doi: 10.1145/2911451.2911547. 

\[5\] L. Jiang, C. Li, S. Wang, and L. Zhang, “Deep feature weighting for naive Bayes and its application to text classification,” Engineering Applications of Artificial Intelligence, vol. 52, pp. 26–39, Jun. 2016, doi: 10.1016/j.engappai.2016.02.002.
```

# prompt6
archivo4:
```markdown
---
title: "Mapa conceptual: problema, contexto, actores y posibles objetivos"
subtitle: "Clasificación automática de texto con Naive Bayes"
abstract: |
  El presente trabajo desarrolla un mapa conceptual sobre el problema de investigación centrado en la clasificación automática de texto con Naive Bayes, considerando su contexto académico e institucional, los actores involucrados, las variables o elementos centrales y los posibles objetivos de mejora. La propuesta se enmarca en la línea de investigación institucional “Tecnologías de la Computación para la Innovación Tecnológica, Desarrollo Sostenible y la Transformación Digital”, específicamente en el itinerario de Sistemas Inteligentes y la sublínea de Inteligencia Artificial y Aprendizaje Automático [1]. A partir de la evidencia bibliográfica, se identifican limitaciones del modelo Naive Bayes en textos cortos, conjuntos de datos pequeños y clases desbalanceadas, así como estrategias de mejora basadas en normalización, ponderación de características y conocimiento de dominio [2]-[6]. El resultado es una representación conceptual coherente que permite comprender el problema, su alcance y su pertinencia investigativa.
abstract-title: "Resumen"
keywords: "mapa conceptual, Naive Bayes, clasificación de texto, inteligencia artificial, aprendizaje automático, minería de texto"
subject: "Metodología de la investigación en computación"
description: "Mapa conceptual sobre el problema de clasificación automática de texto con Naive Bayes, su contexto, actores, variables y objetivos."
category: "Trabajo académico"
lang: es
author: "Wilson Palma"
date: "2026-05-05"
---

# Introducción

La clasificación automática de texto es una tarea fundamental dentro de la minería de texto y los sistemas inteligentes, ya que permite organizar grandes volúmenes de información textual de manera eficiente, consistente y escalable. En este contexto, el modelo Naive Bayes continúa siendo una alternativa importante por su simplicidad y eficiencia, aunque presenta limitaciones en escenarios complejos como textos cortos, datos escasos y clases desbalanceadas [2]-[6].

Este trabajo se enmarca en la línea de investigación institucional **“Tecnologías de la Computación para la Innovación Tecnológica, Desarrollo Sostenible y la Transformación Digital”**, definida para la Carrera de Computación de la Universidad Nacional de Loja, dentro del itinerario de **Sistemas Inteligentes** y con relación directa a la sublínea **1.1 Inteligencia Artificial y Aprendizaje Automático** [1]. También se vincula de manera complementaria con las sublíneas de **Ciencia de Datos y Big Data Analytics** y **Visión por Computador y Procesamiento de Lenguaje Natural**, por el tipo de problema abordado y la naturaleza textual del dominio [1].

# Mapa conceptual

![Mapa conceptual del problema de investigación, su contexto, actores, variables centrales y posibles objetivos.](mapa conceptual.png)

# Desarrollo conceptual

El **problema central** se ubica en la **clasificación automática de texto con Naive Bayes**, especialmente cuando se trabaja con textos cortos, conjuntos de datos pequeños, clases desbalanceadas y dominios específicos. La literatura muestra que el rendimiento del clasificador puede verse afectado por la estimación de parámetros y por la independencia condicional asumida por el modelo, lo que reduce su precisión en ciertas condiciones [2], [4], [5].

El **contexto** de la investigación corresponde al área de **Sistemas Inteligentes y Minería de Texto**, dentro de la línea institucional de la Carrera de Computación [1]. Esta línea promueve el estudio y aplicación de tecnologías computacionales emergentes para la innovación tecnológica, la transformación digital y la solución de problemas reales, incluyendo inteligencia artificial, ciencia de datos, ingeniería de software y computación aplicada [1]. En ese marco, la investigación sobre Naive Bayes resulta pertinente porque aporta conocimiento sobre métodos de clasificación aplicables a entornos con información textual limitada y variabilidad semántica [2]-[6].

Los **actores involucrados** en el problema incluyen a los usuarios finales que generan o consultan textos, los analistas o especialistas que validan categorías, los desarrolladores que implementan los modelos de clasificación, las instituciones que gestionan grandes volúmenes de información y los responsables de procesos que dependen de una clasificación precisa [2], [4]. Cada uno de estos actores se relaciona con la utilidad práctica del clasificador, ya que el resultado del sistema impacta en la organización, recuperación y uso de la información.

Las **variables o elementos centrales** del problema son la precisión de clasificación, la longitud del texto, el tamaño del conjunto de datos, el desbalance de clases, la representación de características y la capacidad de generalización. Estas variables condicionan el desempeño del modelo y determinan su utilidad en escenarios reales [2], [3], [5]. Por ejemplo, la normalización por documento y la ponderación de características mejoran el rendimiento del clasificador en colecciones de texto estándar, mientras que el uso de ontologías y la ponderación profunda de características permiten mejorar la clasificación en contextos con pocos datos o con texto breve [2], [3], [5].

A partir de este análisis, los **posibles objetivos** de investigación se orientan a mejorar la precisión del clasificador Naive Bayes, aumentar su robustez frente a textos cortos y clases desbalanceadas, integrar representaciones de características más eficaces y evaluar variantes del modelo mediante experimentación cuantitativa [2]-[6]. Además, la evidencia también sugiere que una comparación rigurosa entre clasificadores requiere enfoques estadísticos apropiados, como los propuestos en la comparación bayesiana de desempeño [4].

En síntesis, el mapa conceptual muestra que el problema de investigación no debe entenderse de forma aislada, sino como parte de un sistema de relaciones entre contexto, actores, variables y objetivos. Esta articulación permite justificar la pertinencia del estudio dentro de la línea institucional de investigación y dentro de la sublínea de inteligencia artificial y aprendizaje automático [1].

# Conclusión

El mapa conceptual elaborado organiza de forma clara el problema de investigación y lo relaciona con su entorno académico e institucional. Se evidencia que Naive Bayes es una técnica efectiva para clasificación de texto, pero su desempeño depende de la calidad de la representación textual, del tamaño del conjunto de datos y del tratamiento de condiciones como el desbalance de clases [2]-[6]. Asimismo, la investigación se alinea con la línea institucional de la Carrera de Computación, especialmente con la sublínea de inteligencia artificial y aprendizaje automático [1]. Por ello, el mapa conceptual no solo cumple una función descriptiva, sino también orientadora para delimitar el problema y proyectar sus objetivos de mejora.

# Referencias

[1] Universidad Nacional de Loja, *Propuesta de Línea de Investigación: "Tecnologías de la Computación para la Innovación Tecnológica, Desarrollo Sostenible y la Transformación Digital"*, Carrera de Computación, Facultad de la Energía, las Industrias y los Recursos Naturales No Renovables, Loja, Ecuador, Aug. 2025.

[2] S. B. Kim, K. S. Han, H. C. Rim, and S. H. Myaeng, “Some effective techniques for naive bayes text classification,” *IEEE Transactions on Knowledge and Data Engineering*, vol. 18, no. 11, pp. 1457–1466, Nov. 2006, doi: 10.1109/TKDE.2006.180.

[3] K. Sangounpao and P. Muenchaisri, “Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset,” in *Proc. 20th IEEE/ACIS Int. Conf. on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD)*, Toyama, Japan, 2019, pp. 53–58, doi: 10.1109/SNPD.2019.8935711.

[4] E. Frank and R. R. Bouckaert, “Naive Bayes for Text Classification with Unbalanced Classes,” in *Proc. 10th Eur. Conf. on Principles and Practice of Knowledge Discovery in Databases (PKDD)*, Berlin, Germany, 2006, pp. 503–510, doi: 10.1007/11871637_49.

[5] D. Zhang, J. Wang, E. Yilmaz, X. Wang, and Y. Zhou, “Bayesian performance comparison of text classifiers,” in *Proc. 39th Int. ACM SIGIR Conf. on Research and Development in Information Retrieval (SIGIR)*, Pisa, Italy, 2016, pp. 15–24, doi: 10.1145/2911451.2911547.

[6] L. Jiang, C. Li, S. Wang, and L. Zhang, “Deep feature weighting for naive Bayes and its application to text classification,” *Engineering Applications of Artificial Intelligence*, vol. 52, pp. 26–39, Jun. 2016, doi: 10.1016/j.engappai.2016.02.002.
```

archivo5:
```markdown
Perfecto. Tomo como **válida y prioritaria** la línea institucional del PDF: **“Tecnologías de la Computación para la Innovación Tecnológica, Desarrollo Sostenible y la Transformación Digital”**, organizada en los itinerarios de **Sistemas Inteligentes, Ingeniería de Software y Computación Aplicada**. Dentro de ese marco, tu tema encaja de forma natural en **Sistemas Inteligentes**, especialmente en la sublínea **1.1 Inteligencia Artificial y Aprendizaje Automático**, con apoyo conceptual de **1.2 Ciencia de Datos y Big Data Analytics** y **1.4 Visión por Computador y Procesamiento de Lenguaje Natural** por tratarse de clasificación textual. 

### Estructura del mapa conceptual

**Nodo central:**
**Problema de investigación:** *Clasificación automática de texto con Naive Bayes en escenarios de textos cortos, pocos datos y clases desbalanceadas.*

**1. Contexto**

* Área: **Sistemas Inteligentes y Minería de Texto**.
* Línea institucional: **Tecnologías de la Computación para la Innovación Tecnológica, Desarrollo Sostenible y la Transformación Digital**.
* Sublínea más afín: **1.1 IA y Aprendizaje Automático**.
* Soporte complementario: **1.2 Ciencia de Datos y Big Data Analytics** y **1.4 PLN**. 

**2. Problema central**

* Naive Bayes estándar puede perder precisión por suposiciones simplificadoras.
* El desempeño disminuye en **textos cortos**, **datasets pequeños** y **clases desbalanceadas**.
* Esto afecta la confiabilidad de la categorización automática.

**3. Actores**

* **Usuarios finales:** generan o consultan textos.
* **Analistas / especialistas:** validan categorías.
* **Desarrolladores:** implementan el clasificador.
* **Instituciones:** gestionan documentos o información textual.
* **Responsables de proceso:** toman decisiones basadas en la clasificación.

**4. Variables o elementos centrales**

* **Precisión de clasificación**
* **Longitud del texto**
* **Tamaño del conjunto de datos**
* **Desbalance de clases**
* **Representación de características**
* **Capacidad de generalización**

**5. Posibles objetivos**

* Mejorar la **precisión** del clasificador.
* Aumentar la **robustez** frente a textos cortos y pocos datos.
* Reducir el impacto del **desbalance de clases**.
* Evaluar variantes de Naive Bayes para contextos específicos.
* Lograr una herramienta útil para apoyo a la toma de decisiones.

### Relaciones que conviene dibujar con flechas

**Contexto institucional y científico** → condiciona → **Problema de investigación**
**Problema de investigación** → involucra → **Actores**
**Variables centrales** → afectan → **Precisión y generalización**
**Problema de investigación** → motiva → **Posibles objetivos**
**Sublínea 1.1 IA y Aprendizaje Automático** → alberga → **la investigación**
**Sublíneas 1.2 y 1.4** → complementan → **análisis y representación del texto**. 

### Versión breve para poner en el mapa

**Naive Bayes en clasificación de texto**
→ presenta limitaciones en **textos cortos**, **datos pequeños** y **clases desbalanceadas**
→ afecta la **precisión** y la **confiabilidad**
→ involucra a **usuarios, analistas, desarrolladores e instituciones**
→ depende de variables como **longitud del texto, tamaño del dataset y representación de características**
→ plantea como objetivo **mejorar la clasificación automática**
→ se ubica en la línea **Tecnologías de la Computación para la Innovación Tecnológica, Desarrollo Sostenible y la Transformación Digital**, sublínea **IA y Aprendizaje Automático**. 


```



# prompt6
Quiero que hagas la siguiente actividad, pero primero quiero planificación, así que dime, que es lo que piensas hacer para darte luz verde.
En cuanto a los objetivos, no hagas eso, solo necesito las 3 preguntas.
vas a tener que al final presentarme todo el latex pero ya te paso la plantilla despues de esto.
A continuación lo que tienes que elaborar:
```markdown
# FEIRNNR - Carrera de Computación

## Guía de Actividades Práctico-Experimentales
**Nro. 004**

## 1. Datos Generales

- **Asignatura:** Metodología de la Investigación en Computación
- **Ciclo:** 4 A
- **Unidad:** 1
- **Resultado de aprendizaje de la unidad:** R1. Contrasta la investigación y sus tipos con los métodos en el área de Computación y afines.
- **Práctica Nro.:** 004
- **Título de la práctica:** Formulación de objetivos y pregunta de investigación
- **Nombre del docente:** Luis Antonio Chamba Eras
- **Fecha:** Martes 5 de mayo de 2026
- **Horario:** 10h30 – 11h30
- **Lugar:** EVA-Moodle / Aula
- **Tiempo planificado en el Sílabo:** 1 hora

## 2. Objetivo(s) de la Práctica

Redactar el objetivo general, los objetivos específicos y la pregunta de investigación del proyecto integrador, aplicando criterios SMART.

## 3. Materiales y reactivos

- Computador
- Plantilla de formulación de objetivos (EVA-Moodle)
- Taxonomía de Bloom revisada
- Problema de investigación versión 1 (APE 3)

## 4. Equipos y herramientas

EVA-Moodle; guía institucional de práctica.

## 5. Procedimiento / Metodología

**Desarrollo (ABI – Aprendizaje Basado en Investigación):**

1. Revisar el problema de investigación versión 1.
2. Formular la pregunta de investigación derivada del problema.
3. Redactar el objetivo general usando verbos de la taxonomía de Bloom.
4. Derivar 3 objetivos específicos coherentes con el objetivo general.
5. Verificar la coherencia problema-pregunta-objetivos usando criterios SMART.
6. Subir el reporte técnico en PDF a EVA-Moodle.

## 6. Resultados esperados

Documento con pregunta de investigación, objetivo general y 3 objetivos específicos versión 1.

## 7. Preguntas de Control

- ¿Cuál es la relación entre la pregunta de investigación y los objetivos?
- ¿Qué verbos de la taxonomía de Bloom son más adecuados para objetivos de investigación tecnológica?

## 8. Evaluación

Instrumento: Rúbrica de evaluación configurada en EVA-Moodle, alineada al modelo de evaluación integral del desempeño y al PID de la Carrera.

## 9. Bibliografía

Yuni, J. A., y Urbano, C. A. *Metodología y técnicas para investigar*. Buenos Aires, Argentina: Editorial Brujas, 2020.

## 10. Elaboración y Aprobación

**Elaborado por**  
Luis Antonio Chamba Eras  
Docente

**Revisado por** *(Solo si aplica)*  
Técnico Docente

**Aprobado por**  
Edison L. Coronel Romero  
Director de Carrera
```

# prompt7
Adjuntar: [propuesta_linea_investigacion_computacion_unl](./recursos/propuesta_linea_investigacion_computacion_unl.pdf)

Bien, puedes proceder con lo acordado.
Eso sí, te menciono que todo lo que tenga que ver sobre la linea de investigacion y las sublíneas, sacalo de este documento PDF que te acabo de adjuntar (no importa lo que yo haya escrito anteriormente sobre lineas y sublineas de investigación ya que tenía que haberlo sacado de este PDF adjunto pero no lo hice)

# prompt8
Pero haz tú el Mapa conceptual digital, y trata de que se parezca a los generados con alguna de las herramientas (CmapTools, Draw.io, Canva). Esto último te lo digo por lo que la ultima vez, lo que me hiciste parecía más una infografía que un mapa conceptual.

# prompt9
Quiero que realices la siguiente actividad, pero primero quiero planificación, así que dime, que es lo que piensas hacer para darte luz verde.

Quiero que realices la actividad completa en markdown (y la presentas en un bloqe de codigo markdown para poder copiar su contenido), al final incluyes las referencias en IEEE y dentro del contenido referencias esas fuentes como citas en formato IEEE (ejemplo "parrafo1 [1].\nparrafo2 [2]. ...").

La imagen ya la tengo descargada en local, por lo que el el pdf solo la incluyes con el nombre "mapa conceptual.png" y le pones el respectivo caption.

Rellena (en base a lo solicitado como actividad y a lo elaborado) e Incluye los siguientes metadatos en el encabezado yaml al inicio del markdown:
---
title:
subtitle:
abstract:
abstract-title:
keywords:
subject:
description:
category:
lang: es
author: Wilson Palma
date:
---

# prompt10
No incluyas conclusiones y recomendaciones en el latex que generes ya que el docente dijo que por el momento que eso no.
Ahora sí, procede con la siguiente plantilla en latex:
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
Práctico-Experimentales Nro. 001\par}
\end{center}

\section{Datos de Identificación del Estudiante y la Práctica}

\noindent
\begin{tabularx}{\textwidth}{|L{0.43\textwidth}|Y|}
\hline
\textbf{Nombre del estudiante(s)} & Edison Leonardo Coronel Romero \\ \hline
\textbf{Asignatura} & Desarrollo Basado en Plataformas \\ \hline
\textbf{Ciclo} & 5 A \\ \hline
\textbf{Unidad} & 1 \\ \hline
\textbf{Resultado de aprendizaje de la unidad} &  \\ \hline
\textbf{Práctica Nro.} & 001 \\ \hline
\textbf{Título de la Práctica} & Implementar un servicio REST con Node.js \\ \hline
\textbf{Nombre del Docente} & Edison Leonardo Coronel Romero \\ \hline
\textbf{Fecha} & Viernes 3 de octubre \\ \hline
\textbf{Horario} & 07h30 -- 10h30 \\ \hline
\textbf{Lugar} & \makecell[tl]{Laboratorio Computación aplicada\\Laboratorio Desarrollo de Software\\Laboratorio de redes y Sistemas Operativos\\Laboratorio Virtual\\EVA\\Aula} \\ \hline
\textbf{Tiempo planificado en el Sílabo} & 3 horas \\ \hline
\end{tabularx}

\section{Objetivo(s) de la Práctica}
Escriba el objetivo de la práctica (copiado de la guía proporcionada por el docente).

\section{Materiales, Reactivos, Equipos y Herramientas}
Liste los materiales, reactivos, equipos y herramientas utilizados en la práctica, confirmando los de la guía o agregando los adicionales.

\section{Procedimiento / Metodología Ejecutada}
Describa brevemente los pasos que siguió durante la ejecución de la práctica.

\section{Resultados}
Incluya evidencias del trabajo realizado (tablas, gráficos, capturas de pantalla, registros de ejecución, modelos, programas, informes, etc.).

\newpage

\section{Preguntas de Control}
Responda a las preguntas del docente.

\section{Conclusiones}
Redacte las principales conclusiones de la práctica, vinculándolas con el objetivo planteado.

\section{Recomendaciones}
Incluya sugerencias para mejorar la práctica o su aplicación en casos reales.

\section{Bibliografía / Referencias}
Liste las fuentes adicionales consultadas siguiendo el formato IEEE.

\section{Anexos}
Recursos de apoyo para cada una de las secciones anteriores.

\end{document}
```

# prompt11
cuando te dije que no hagas los objetivos me refería a que en las indicaciones pedía algo sobre redactar unos objetivos, ahí me refería, pero la seccion de objetivos en la plantilla latex, la tienes que reemplazar con la sección de objetivos que estaban en las indicaciones hací como hiciste con las demás cosas. objetivos redactados, con los objetivos de la practica son 2 cosas muy diferentes. Y en la sección de resultados van las 3 preguntas.
Procede con esa correciones en el latex que generaste.

# prompt12
en la misma pregunta incluye cual es la variable independiente y dependiente