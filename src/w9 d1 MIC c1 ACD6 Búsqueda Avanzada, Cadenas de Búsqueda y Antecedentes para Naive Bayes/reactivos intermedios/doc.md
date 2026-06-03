---
title: "ACD 6: Búsqueda Avanzada, Cadenas de Búsqueda y Antecedentes"
subtitle: "Efectividad de Naive Bayes en la clasificación de texto"
abstract: "Este documento presenta antecedentes y un estado del arte inicial sobre la efectividad de Naive Bayes en la clasificación de texto. A partir de una búsqueda avanzada en bases académicas, se revisan trabajos relacionados con mejoras del algoritmo, selección y ponderación de características, manejo de clases desbalanceadas, variantes bayesianas y aplicaciones en distintos dominios, con el fin de identificar tendencias, aportes relevantes y la brecha de investigación que sustenta el estudio."
abstract-title: "Resumen"
keywords: ["Naive Bayes", "clasificación de texto", "antecedentes", "estado del arte", "búsqueda avanzada", "minería de texto", "procesamiento de lenguaje natural"]
subject: "Búsqueda bibliográfica y redacción de antecedentes de investigación"
description: "Documento académico con antecedentes y estado del arte inicial sobre la efectividad de Naive Bayes en clasificación de texto, elaborado a partir de búsqueda avanzada y selección de fuentes relevantes."
category: "Investigación académica"
lang: es
author: Wilson Palma
date: 2026-06-01
---

# Tema de investigación

**Pregunta de investigación:** ¿Qué tan efectivo es Naive Bayes en clasificación de texto?

**Palabras clave principales:** Naive Bayes, text classification, document classification, text mining, text categorization, natural language processing, feature selection, feature weighting, smoothing, unbalanced classes.

# Estrategia de búsqueda

Para construir el corpus documental del proyecto se empleó una búsqueda avanzada basada en sinónimos, variantes conceptuales y términos relacionados con el problema de investigación. La cadena de búsqueda se formuló con operadores booleanos para ampliar la cobertura y, al mismo tiempo, mantener la pertinencia temática:

```text
("naive bayes" OR "naive bayes classifier" OR "naive bayes classification" OR
"bayes classifier" OR "multinomial naive bayes" OR "bernoulli naive bayes")
AND
("text classification" OR "document classification" OR "text categor*" OR
"text mining" OR "text analytics" OR "natural language processing" OR "NLP" OR
"sentiment analysis" OR "topic classification" OR "document categor*")
```

La búsqueda se orientó a bases de datos académicas como Scopus, IEEE Xplore, ACM Digital Library y Google Scholar, complementando con literatura gris cuando fue pertinente. Como criterios de selección se priorizaron artículos centrados en: a) mejoras metodológicas de Naive Bayes, b) análisis de desempeño en clasificación textual, c) selección y ponderación de características, y d) aplicaciones del algoritmo en distintos dominios.

# Antecedentes

Naive Bayes ha sido ampliamente utilizado en clasificación de texto debido a su simplicidad, eficiencia computacional y capacidad para ofrecer resultados competitivos como modelo base. Uno de los trabajos más influyentes fue la revisión de la formulación multinomial para categorización textual, en la que se demostró que el modelo podía mantener un desempeño sólido en tareas de clasificación cuando se adaptaba adecuadamente al dominio documental [1]. A partir de este punto, la literatura comenzó a estudiar no solo su aplicación directa, sino también las condiciones bajo las cuales Naive Bayes conserva una efectividad aceptable en escenarios con vocabularios extensos, clases desbalanceadas y textos ruidosos [2], [3].

Una primera línea de investigación se centró en mejorar el comportamiento del clasificador mediante ajustes probabilísticos y técnicas de suavizado. Se ha mostrado que la forma de estimar las probabilidades tiene un impacto importante en la estabilidad del modelo, especialmente cuando aparecen observaciones poco frecuentes o inexistentes en el corpus de entrenamiento [2], [4]. En contextos con clases desbalanceadas, también se ha evidenciado que el rendimiento puede deteriorarse si no se considera la distribución desigual de las categorías, lo que refuerza la necesidad de adaptar Naive Bayes a la estructura real del conjunto de datos [3]. Estos trabajos muestran que la efectividad del algoritmo no depende únicamente del modelo base, sino también de la forma en que se estiman y corrigen sus parámetros [2], [3], [4].

Posteriormente, varios estudios se enfocaron en la selección de características, ya que la representación textual suele producir espacios de gran dimensionalidad y con abundante redundancia. En esta línea, se propuso que eliminar términos poco informativos puede mejorar el rendimiento de Naive Bayes al conservar aquellos atributos que aportan mayor poder discriminativo [5]. De manera complementaria, otros trabajos investigaron el escalamiento o ponderación de características dependiente de clase, buscando que las palabras más representativas para cada categoría tengan mayor influencia en la decisión final [6]. Estos aportes son especialmente relevantes porque muestran que el modelo puede ser fortalecido cuando se combina con técnicas de preprocesamiento y reducción de dimensionalidad [5], [6].

Otra línea de antecedentes importante corresponde a las extensiones del supuesto de independencia condicional, que constituye la base del Naive Bayes clásico. Dado que dicho supuesto no siempre se ajusta a la estructura real del lenguaje, algunos autores propusieron variantes de orden superior para capturar relaciones entre términos que el modelo tradicional no representa [7]. En la misma dirección, se exploraron enfoques más sofisticados de selección y ponderación de características para aproximarse mejor a la complejidad del texto sin abandonar la lógica bayesiana [8], [9]. Estas investigaciones sugieren que una de las vías más prometedoras no es reemplazar Naive Bayes, sino ampliar sus capacidades para reducir los efectos de sus simplificaciones estructurales [7], [8], [9].

También ha sido recurrente la comparación de Naive Bayes frente a otros clasificadores textuales. Un enfoque bayesiano para comparar el desempeño de distintos clasificadores mostró que las diferencias entre modelos dependen del corpus, del criterio de evaluación y de la naturaleza de la tarea, por lo que no es correcto asumir superioridad universal de un algoritmo sobre otro [10]. Además, otro estudio propuso una clasificación bayesiana basada en características específicas de clase, destacando que el rendimiento puede mejorar cuando la representación del texto se ajusta a la información más discriminativa de cada categoría [11]. En consecuencia, la literatura sugiere que Naive Bayes sigue siendo relevante, pero su efectividad es contextual y debe analizarse según el tipo de texto, el idioma, la longitud del documento y el balance entre clases [10], [11].

# Estado del arte inicial

A partir de la revisión preliminar de la literatura, el estado del arte inicial muestra que la investigación sobre Naive Bayes en clasificación de texto se ha organizado alrededor de cuatro ejes principales: mejoras algorítmicas, selección de características, manejo de la dependencia entre términos y aplicación en dominios específicos.

En el primer eje, los trabajos más tempranos demostraron que el rendimiento del clasificador puede mejorar mediante técnicas de ajuste probabilístico, suavizado y tratamiento de clases desbalanceadas [2], [3], [4]. Este conjunto de aportes estableció una base metodológica sólida para entender que la versión estándar del algoritmo no siempre es suficiente por sí sola. Más adelante, estudios como los de Tang et al. reforzaron la idea de que la optimización del espacio de atributos es decisiva para lograr resultados competitivos en clasificación textual [8], [11].

En el segundo eje, la selección y ponderación de características aparece como una de las estrategias más consistentes para incrementar la efectividad de Naive Bayes [5], [6], [8], [9]. La evidencia revisada indica que, al reducir ruido, eliminar redundancia y resaltar los términos más relevantes por clase, el clasificador mejora su capacidad de discriminación. Este hallazgo se mantiene en trabajos más recientes que continúan refinando la importancia de los atributos, lo que confirma que la calidad de la representación textual es tan importante como el algoritmo mismo [9], [12].

En el tercer eje, la literatura propone que la independencia entre palabras, asumida por el modelo clásico, limita parcialmente su potencial. Como respuesta, se han diseñado variantes de orden superior, adaptaciones del hidden Naive Bayes y esquemas de ponderación profunda por clase, con resultados que apuntan a una mayor robustez en ciertos escenarios [7], [12], [13], [14]. Esto indica que la evolución del modelo no ha consistido en abandonar la idea bayesiana, sino en enriquecerla para reflejar mejor la dependencia semántica y estructural del lenguaje.

En el cuarto eje, las aplicaciones prácticas confirman la vigencia del algoritmo en tareas reales. Se han reportado usos de Naive Bayes en clasificación de textos cortos, análisis de sentimiento, reseñas y problemas documentales de distintos dominios [15], [16]. Aunque algunos de estos estudios se enfocan en aplicaciones más que en la comparación teórica del algoritmo, aportan evidencia de que Naive Bayes sigue siendo una opción útil por su rapidez, interpretabilidad y facilidad de implementación [15], [16], [17]. En particular, los estudios aplicados muestran que el algoritmo conserva valor cuando se trabaja con corpus pequeños, textos breves o escenarios en los que se necesita una solución eficiente y trazable [15], [16].

Con base en esta revisión inicial, puede afirmarse que Naive Bayes sigue siendo un clasificador competitivo para texto, pero su efectividad depende de la calidad de los atributos, del tratamiento del desbalance, de la representación semántica y del tipo de corpus analizado [1]-[17]. La brecha que justifica este proyecto es que la evidencia existente se encuentra dispersa entre mejoras metodológicas y aplicaciones específicas, por lo que todavía hace falta una síntesis que permita determinar en qué condiciones el algoritmo funciona mejor y en cuáles pierde capacidad predictiva. Por ello, esta investigación se orienta a organizar, comparar y valorar la literatura disponible para establecer una conclusión más sólida sobre su efectividad en clasificación de texto.

# Conclusión

La revisión preliminar confirma que Naive Bayes es un enfoque ampliamente estudiado en clasificación de texto y que su rendimiento puede mejorar significativamente mediante técnicas complementarias como suavizado, selección de características, ponderación por clase y adaptaciones estructurales [2]-[9], [12], [13], [14]. Asimismo, la evidencia muestra que su desempeño es contextual y que no debe evaluarse de forma aislada, sino en función del corpus, del tipo de texto y de la tarea específica [10], [11], [15], [16], [17]. En consecuencia, el estado del arte inicial proporciona una base suficiente para continuar con un análisis más profundo de la efectividad del algoritmo en escenarios textuales diversos.

# Referencias

[1] A. M. Kibriya, E. Frank, B. Pfahringer y G. Holmes, “Multinomial naive Bayes for text categorization revisited,” en *AI 2004: Advances in Artificial Intelligence*, Berlin, Heidelberg: Springer, 2005, pp. 488–499.


[2] S. B. Kim, K. S. Han, H. C. Rim y S. H. Myaeng, “Some effective techniques for naive bayes text classification,” *IEEE Transactions on Knowledge and Data Engineering*, vol. 18, no. 11, pp. 1457–1466, 2006.


[3] E. Frank y R. R. Bouckaert, “Naive Bayes for text classification with unbalanced classes,” *Lecture Notes in Computer Science*, vol. 4213, pp. 503–510, 2006.


[4] F. He y X. Ding, “Improving Naive Bayes Text Classifier Using Smoothing Methods,” en *Advances in Information Retrieval*, Berlin, Heidelberg: Springer, 2007, pp. 703–707.


[5] J. Chen, H. Huang, S. Tian y Y. Qu, “Feature selection for text classification with Naïve Bayes,” *Expert Systems with Applications*, vol. 36, no. 3, pp. 5432–5435, 2009.


[6] E. S. Youn y M. K. Jeong, “Class dependent feature scaling method using naive Bayes classifier for text datamining,” *Pattern Recognition Letters*, vol. 30, no. 5, pp. 477–485, 2009.


[7] M. C. Ganiz, C. George y W. M. Pottenger, “Higher order Naïve bayes: A novel non-IID approach to text classification,” *IEEE Transactions on Knowledge and Data Engineering*, vol. 23, no. 7, pp. 1022–1034, 2011.


[8] B. Tang, S. Kay y H. He, “Toward Optimal Feature Selection in Naive Bayes for Text Categorization,” *IEEE Transactions on Knowledge and Data Engineering*, vol. 28, no. 9, pp. 2508–2521, 2016.


[9] L. Zhang, L. Jiang, C. Li y G. Kong, “Two feature weighting approaches for naive Bayes text classifiers,” *Knowledge-Based Systems*, vol. 100, pp. 137–144, 2016.


[10] D. Zhang, J. Wang, E. Yilmaz, X. Wang y Y. Zhou, “Bayesian Performance Comparison of Text Classifiers,” en *Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval*, New York, NY, USA: ACM, 2016, pp. 15–24.


[11] B. Tang, H. He, P. M. Baggenstoss y S. Kay, “A Bayesian Classification Approach Using Class-Specific Features for Text Categorization,” *IEEE Transactions on Knowledge and Data Engineering*, vol. 28, no. 6, pp. 1602–1606, 2016.


[12] S. Ruan, H. Li, C. Li y K. Song, “Class-specific deep feature weighting for naïve bayes text classifiers,” *IEEE Access*, vol. 8, pp. 20151–20159, 2020.


[13] H. Kim, J. Kim, J. Kim y P. Lim, “Towards perfect text classification with Wikipedia-based semantic Naïve Bayes learning,” *Neurocomputing*, vol. 315, pp. 128–134, 2018.


[14] S. Gan, S. Shao, L. Chen, L. Yu y L. Jiang, “Adapting hidden naive bayes for text classification,” *Mathematics*, vol. 9, no. 19, 2021.


[15] K. Sangounpao y P. Muenchaisri, “Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset,” en *Proceedings of the 20th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing*, 2019, pp. 53–58.


[16] J. B. Awotunde, S. Misra, V. Katta y O. C. Adebayo, “An Ensemble-Based Hotel Reviews System Using Naive Bayes Classifier,” *CMES - Computer Modeling in Engineering and Sciences*, vol. 137, no. 1, pp. 131–154, 2023.


[17] M. Romano, G. Contu, F. Mola y C. Conversano, “Threshold-based Naïve Bayes classifier,” *Advances in Data Analysis and Classification*, vol. 18, no. 2, pp. 325–361, 2024.