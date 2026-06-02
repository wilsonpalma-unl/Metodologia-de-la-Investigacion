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