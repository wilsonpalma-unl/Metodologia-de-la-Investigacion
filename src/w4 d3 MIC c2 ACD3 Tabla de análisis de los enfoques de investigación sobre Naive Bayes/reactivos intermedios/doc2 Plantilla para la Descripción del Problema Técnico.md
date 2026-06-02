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

[1] S. B. Kim, K. S. Han, H. C. Rim, and S. H. Myaeng, “Some effective techniques for naive bayes text classification,” *IEEE Transactions on Knowledge and Data Engineering*, vol. 18, no. 11, pp. 1457–1466, Nov. 2006, doi: 10.1109/TKDE.2006.180.

[2] K. Sangounpao and P. Muenchaisri, “Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset,” in *Proceedings - 20th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing, SNPD 2019*, 2019, pp. 53–58, doi: 10.1109/SNPD.2019.8935711.

[3] E. Frank and R. R. Bouckaert, “Naive Bayes for Text Classification with Unbalanced Classes,” in *Lecture Notes in Computer Science*, vol. 4213, 2006, pp. 503–510, doi: 10.1007/11871637_49.

[4] D. Zhang, J. Wang, E. Yilmaz, X. Wang, and Y. Zhou, “Bayesian performance comparison of text classifiers,” in *SIGIR 2016 - Proceedings of the 39th ACM SIGIR Conference on Research and Development in Information Retrieval*, 2016, pp. 15–24, doi: 10.1145/2911451.2911547.

[5] L. Jiang, C. Li, S. Wang, and L. Zhang, “Deep feature weighting for naive Bayes and its application to text classification,” *Engineering Applications of Artificial Intelligence*, vol. 52, pp. 26–39, 2016, doi: 10.1016/J.ENGAPPAI.2016.02.002.