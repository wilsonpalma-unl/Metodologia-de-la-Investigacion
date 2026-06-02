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

