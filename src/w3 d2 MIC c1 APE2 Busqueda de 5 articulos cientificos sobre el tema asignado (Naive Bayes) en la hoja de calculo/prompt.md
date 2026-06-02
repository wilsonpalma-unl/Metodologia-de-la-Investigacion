# prompt1
Necesito que encuentres articulos que me sirvan para responder esta pregunta "¿Qué tan efectivo es Naive Bayes en clasificación de texto?". Orden para buscar en bases indexadas: [IEEE, ACM, SCOPUS, google academico]. Por cada articulo necesito que me digas tambien "De cual de esas bases indexadas lo sacaste" y "cual fue el script de busqueda que utilizaste para encontrar ese artículo específico en su base indexada". Tienen que ser 5 artículos. Al final me presentas los articulos mencionando de donde lo sacaste y su respectivo script de busqueda en un bloque de codigo markdown para que pueda copiar su contenido. Tomate tu tiempo.

# prompt2
Bien, a lo que tu hiciste incluso le incluí el DOI solo para que la informacion sea mas solida:
```markdown
| # | Artículo | Base indexada | Script de búsqueda utilizado | DOI |
|---|---|---|---|---|
| 1 | Some Effective Techniques for Naive Bayes Text Classification | IEEE | `("Naive Bayes" AND ("text classification" OR "text categorization" OR "document classification") AND (effectiveness OR performance OR accuracy OR improvement OR technique OR smoothing OR feature weighting))` | https://doi.org/10.1109/TKDE.2006.180 |
| 2 | Ontology-Based Naive Bayes Short Text Classification Method for a Small Dataset | IEEE | `("Naive Bayes" AND ("short text" OR "short text classification" OR "text classification") AND (ontology OR semantic OR "small dataset") AND (accuracy OR performance OR evaluation))` | https://doi.org/10.1109/SNPD.2019.8935711 |
| 3 | Naive Bayes for text classification with unbalanced classes | ACM | `("Naive Bayes" AND ("text classification" OR "document classification" OR "text categorization") AND (unbalanced) AND (performance OR accuracy OR evaluation))` | https://doi.org/10.1007/11871637_49 |
| 4 | Bayesian Performance Comparison of Text Classifiers | ACM | `("Bayesian" AND ("performance comparison" OR comparison OR evaluation) AND ("text classifiers" OR "text classification") AND ("Naive Bayes" OR bayes))` | https://doi.org/10.1145/2911451.2911547 |
| 5 | Deep feature weighting for naive Bayes and its application to text classification | SCOPUS | `TITLE-ABS-KEY(("naive bayes" OR "naïve bayes") AND ("text classification" OR "text categorization" OR "document classification") AND ("feature weighting" OR weighting OR improvement) AND (accuracy OR performance OR evaluation))` | https://doi.org/10.1016/j.engappai.2016.02.002 |
```
Y en base a todo esto quiero que rellenes el siguiente markdown con los articulos encontrados, el markdown ya tiene contenido pero desde la matriz de extraccion en adelante es informacion falsa, tu tienes que remplazar con lo que hemos encontrado y con nuestra propia informacion en base a los 5 articulos encontrados. Al final lo presentas al siguiente markdown habiendo remplazado la informacion falsa con lo nuestro y lo presentas en un bloque de codigo markdown para poder copiar su contenido. Tómate tu tiempo.

Markdown con el contenido a remplazar:
```markdown
**Matriz de Extracción de Artículos Científicos**

**Información general del estudiante**

* **Nombre del estudiante:** Wilson Palma  
* **Técnica de IA:** Aprendizaje automático supervisado (Machine Learning)  
* **Pregunta de investigación:** ¿Qué tan efectivo es Naive Bayes en clasificación de texto?

**Matriz de extracción (ejemplo con 5 artículos)**

| \# | Referencia (IEEE) | Año | Base de datos | Técnica IA | Problema abordado | Objetivo del artículo | Metodología | Dataset / Contexto | Resultados principales | Limitaciones | Aporte para la PI |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | J. Redmon et al., “You Only Look Once: Unified, Real-Time Object Detection,” IEEE CVPR | 2016 | IEEE | CNN (YOLO) | Detección de objetos en tiempo real | Proponer un modelo rápido de detección | CNN unificada para detección directa | PASCAL VOC | Alta velocidad (45 FPS) con buena precisión | Menor precisión en objetos pequeños | Introduce enfoque en tiempo real |
| 2 | R. Girshick, “Fast R-CNN,” IEEE ICCV | 2015 | IEEE | CNN | Detección de objetos | Mejorar precisión y velocidad de R-CNN | Uso de ROI pooling | VOC, ImageNet | Mejora significativa en precisión | Requiere procesamiento por regiones | Mejora precisión en detección |
| 3 | S. Ren et al., “Faster R-CNN,” IEEE TPAMI | 2017 | IEEE | CNN | Detección de objetos | Integrar generación de regiones | Redes de propuesta de regiones (RPN) | COCO | Alta precisión y velocidad | Complejidad computacional | Avance clave en detección |
| 4 | T.-Y. Lin et al., “Feature Pyramid Networks,” IEEE CVPR | 2017 | IEEE | CNN | Detección multiescala | Mejorar detección de objetos pequeños | Pirámides de características | COCO | Mejora en objetos pequeños | Mayor consumo computacional | Mejora robustez |
| 5 | J. Dai et al., “R-FCN: Object Detection via Region-based Fully Convolutional Networks,” IEEE NIPS | 2016 | IEEE | CNN | Detección eficiente | Reducir costo computacional | Fully convolutional networks | VOC | Mejor eficiencia | Menor flexibilidad | Optimiza eficiencia |

**Síntesis del ejemplo (modelo que el estudiante debe replicar)**

Las CNN han demostrado ser altamente efectivas en la detección de objetos dentro del campo de visión por computador. Los estudios analizados evidencian una evolución progresiva desde modelos como R-CNN hacia enfoques más eficientes como YOLO y Faster R-CNN. Mientras que modelos como Fast R-CNN priorizan la precisión mediante el análisis por regiones, YOLO introduce un enfoque unificado que permite detección en tiempo real. Por otro lado, técnicas como Feature Pyramid Networks mejoran el rendimiento en la detección de objetos de diferentes escalas. En general, existe un trade-off entre precisión y eficiencia computacional.

**Respuesta a la pregunta de investigación (ejemplo)**

Las CNN se aplican en la detección de objetos mediante arquitecturas especializadas que permiten identificar y localizar múltiples objetos dentro de una imagen. Estas técnicas han evolucionado hacia modelos más rápidos y precisos, como YOLO y Faster R-CNN, los cuales logran un equilibrio entre rendimiento y eficiencia, siendo ampliamente utilizados en aplicaciones como vehículos autónomos, vigilancia inteligente y análisis de imágenes médicas.
```

# prompt3
Bien, ahora tengo un markdown con todo hecho, el problema es que tenía que haberlo hecho en un plantilla de overleaft con latex pero no se nada de latex, así que te voy a pasar el markdown y el codigo latex para que lo rellenes con lo que está en el markdown. Te voy a pasar primero el texto markdown para que puedas analizar con calma y luego que ya lo hayas analizado te voy a pasar el latex.
