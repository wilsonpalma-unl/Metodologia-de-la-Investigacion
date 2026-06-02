```yaml
Actividad:
    type:
        class: APE
        number: 3
    description:
        para hoy la matriz en word, la idea en esta practica es identificar una oportunidad para investigación. usar el tema signado por el inge en el excel. vamos a trabajar con los notebooks que nos sirven para las actividades autónomas. necesitamos el uso etico de la tecnología ya que la IA va a ayudarnos con la lectura.
        [10:40:31]
        quiere hacer un ejercicio real. por lo que le pidió a alguien que comparta su matriz por telegram y Alejandro se ofreció.
        \> recordar que cada uno tiene asignada una tecnica en el excel. y con esa tecnica continuamos.
    indicaciones:
        Desarrollo (ABI – Aprendizaje Basado en Investigación):
        1. Revisar las fuentes bibliográficas recopiladas en la APE 1.
        2. Identificar brechas, necesidades o problemas detectados en la literatura.
        3. Redactar la descripción del problema preliminar usando la plantilla.
        4. Identificar actores involucrados, contexto y variables/elementos centrales.
        5. Vincular el problema con la sublínea de investigación seleccionada.
        6. Subir el reporte técnico en PDF a EVA-Moodle.
    [10:44.31]
    Procedimiento:
        1. Entonces procedemos a crear un nuevo Notebook y cargamos nuestros 5 articulos encontrados sobre e tema asignado en el excel al notebook creado.
            - https://doi.org/10.1109/TKDE.2006.180
            - https://doi.org/10.1109/SNPD.2019.8935711
            - https://doi.org/10.1007/11871637_49
            - https://doi.org/10.1145/2911451.2911547
            - https://doi.org/10.1016/j.engappai.2016.02.002
        2. ahora basados en el paso 2 de indicaciones: Necesitamos generar un buen prompt.
            Prompt de Alejandro Padilla:
                Actuá como un asistente de investigación académica especializado en el tema. Tu única fuente de información son los 5 artículos cargados en este notebook.

                Pregunta de investigación que estoy explorando:
                ¿Qué tan efectivo es Naive Bayes en clasificación de texto?

                Tu tarea: identificar y sistematizar las brechas, necesidades y problemas que los autores de estos artículos detectan sobre el tema.

                Para cada hallazgo entregá:

                Tipo: clasificalo como Brecha de conocimiento, Limitación técnica, Necesidad metodológica, Problema práctico/aplicado o Contradicción entre estudios.
                Descripción: explicá el problema en 2 a 4 oraciones, con lenguaje técnico preciso.
                Evidencia textual: Quiero que realices la actividad completa en markdown (y la presentas en un bloqe de codigo markdown para poder copiar su contenido), al final incluyes las referencias en IEEE y dentro del contenido referencias esas fuentes como citas en formato IEEE (ejemplo "parrafo1 [1].\nparrafo2 [2].\n...").
                Fuente: indicá de qué artículo proviene citando en IEEE como te acabé de decir usando las referencias de las fuentes en formato ".bib".
                Implicancia para la investigación: una oración sobre por qué esa brecha importa para responder mi pregunta de investigación.
                Reglas obligatorias:
                    No inventes nada que no esté en los artículos. Si un punto no está respaldado por el texto, no lo incluyas.
                    Si dos artículos coinciden en señalar el mismo problema, agrupalos en un solo hallazgo y citá ambos.
                    Si dos artículos se contradicen, marcalo explícitamente como Contradicción entre estudios.
                    Diferenciá claramente entre lo que los autores afirman y lo que vos inferís. Si inferís algo, marcalo como [Inferencia].
                Formato de salida: tabla en markdown con las columnas: \#, Tipo, Descripción, Evidencia textual, Fuente, Implicancia.

                Al final de la tabla, agregá una sección llamada "Síntesis de brechas dominantes" (máximo 150 palabras) donde identifiques los 2 o 3 problemas más recurrentes o críticos detectados en el conjunto de los 5 artículos.
            
            \> Segun el inge, dice que le falta poner a Alejandro en el prompt, que la IA vaya poniendo citas y referencias mientras va redactando. Entonces hay que agregarle eso del IEEE.
            \> Si uno no referencia o cita fuentes, se considera plagio.
            \> Notebook de Alejandro Padilla:
                "https://notebooklm.google.com/notebook/2d558801-3cd2-4c7b-8042-7ed8447a8c5d"
            [11:08:30]
            > Es mejor pasarle a Notebook, la bibliografía en formato bib los 5 artículos con ayuda de Mendeley
            > Listo, se exportaron las bibliografías en formato .bib con ayuda de mendeley

            Paso x: instalar plugin de mendeley para word

            > No subir nada por ahora en la actividad APE3 de MIC en el eva, mañana ya continuamos y subimos.
            [11:31]
            > El inge nos compartirá la plantilla al telegram para mañana continuar.

        3. aquí tambien basado en el punto 3 de las indicaciones: El inge nos proporcionará una plantilla
```