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