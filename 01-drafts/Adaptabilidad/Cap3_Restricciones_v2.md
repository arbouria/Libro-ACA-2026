# Capítulo 3: El Papel de las Restricciones en la Evolución del  Comportamiento Adaptable

### Borrador Final

Suponga que es ingeniero y su empresa le pide diseñar un robot de servicio autónomo para hogares. En su primera versión, el dueño conecta el robot a una toma de corriente antes de acostarse, como lo hace con su celular. Durante la noche el robot trabaja con esa energía, y por la mañana, cuando la batería se agota, se detiene. Usted puede mejorar la autonomía con baterías de mayor duración, pero el problema no desaparece: más tarde o más temprano, sin recarga, el robot se inmoviliza.

Un robot verdaderamente autónomo tendría que recargarse por sí mismo. Pero qué solución de diseño es la correcta depende de dónde va a operar. Si todas las casas fueran idénticas y la toma de corriente siempre estuviera en el mismo lugar, bastaría programar la ruta: a tal hora, dirigirse al punto X. Pero si las casas varían —que es el caso real— el robot necesita un algoritmo que le permita *aprender* la ubicación de las tomas en cada nuevo hogar. Y si el robot fuera a explorar un planeta desconocido, necesitaría algo más: algoritmos capaces de aprender en condiciones de incertidumbre profunda sobre cómo funciona ese entorno.

La selección natural ha operado exactamente como ese ingeniero. Los agentes biológicos enfrentan el mismo problema fundamental: obtener los recursos necesarios para sobrevivir y reproducirse, lo que en este libro llamamos **sucesos biológicamente importantes** (SBI). Como vimos en el capítulo anterior, la variabilidad heredable en el acceso a los SBI genera diferencias en éxito reproductivo, y esas diferencias acumuladas producen adaptación. La pregunta de este capítulo es cuáles tipos de soluciones ha seleccionado la evolución y qué determina cuál es la apropiada en cada caso.

La respuesta depende de dos conjuntos de restricciones: las que impone el propio organismo y las que impone el entorno.

---

## Las Restricciones del Organismo

El comportamiento tiene costos. El primero y más fundamental es que cualquier comportamiento consume tiempo, y el tiempo disponible es finito. No existe tal cosa como un momento de inactividad en sentido estricto: incluso "permanecer quieto" o "dormir" es un comportamiento que ocupa tiempo y cumple funciones. Si sumamos la duración de todos los comportamientos posibles a lo largo de un período, obtenemos una identidad:

$$T = t_1 + t_2 + t_3 \dots + t_n$$

Esta ecuación expresa una *restricción lineal*: los diferentes comportamientos compiten entre sí por el tiempo disponible. Cada segundo dedicado a buscar alimento es un segundo menos disponible para vigilar depredadores, para aparearse, para descansar. A esto le llamamos **costo de oportunidad**: el valor de la mejor alternativa a la que se renuncia cuando se elige una opción. Un agente que dedica demasiado tiempo a esconderse tendrá poco tiempo para obtener alimento o encontrar pareja, y dependiendo del entorno, eso puede resultar en menor éxito reproductivo que un animal con una distribución más equilibrada.

Estos **trade-offs** son ubicuos en biología porque las restricciones fundamentales —tiempo finito, energía limitada— hacen imposible maximizar todo simultáneamente. Como vimos al hablar de paisajes adaptativos, el óptimo es siempre un balance entre presiones en tensión. Esta restricción reaparecerá con fuerza en el Bloque III, cuando estudiemos cómo los organismos distribuyen su comportamiento entre opciones que compiten.

Un segundo grupo de restricciones del organismo incluye su estructura biológica, metabólica, neuronal y física. Estas características delimitan el rango de comportamientos posibles —el **espacio de posibilidades**— y determinan el costo energético de cada uno. A estas restricciones se suman los **costos cognitivos** de los algoritmos mismos: algunos mecanismos de aprendizaje requieren mayor capacidad de memoria o procesamiento, lo que tampoco es gratuito.

---

## Las Restricciones del Entorno

Además de las limitaciones del organismo, el entorno impone sus propias condiciones. La más fundamental es si las condiciones que determinan la disponibilidad de los SBI son **constantes o variables** a lo largo del tiempo.

Cuando las condiciones son relativamente constantes a lo largo de la historia evolutiva de una especie, la selección natural puede codificar directamente en el genoma las respuestas apropiadas. El resultado es el **comportamiento adaptado**: patrones conductuales que no requieren aprendizaje individual porque la solución ya está incorporada filogenéticamente. El reflejo de retirada ante un estímulo doloroso es un ejemplo: la relación entre calor intenso y daño tisular ha sido suficientemente constante durante millones de años. Otro ejemplo es la impronta en aves: los patitos siguen al primer objeto en movimiento que perciben después de la eclosión porque, en la historia de esa especie, ese objeto era invariablemente la madre. El ingeniero que escribe directamente en el código del robot la respuesta correcta está haciendo, en miniatura, lo que la selección natural hace con el comportamiento adaptado.

Sin embargo, los entornos de la mayoría de los organismos son variables, volátiles e inciertos. En esas condiciones, una respuesta conductual genéticamente fija sería evolutivamente subóptima: el entorno cambia, pero la respuesta no puede hacerlo. Ante un entorno variable, la selección natural favorece algo radicalmente diferente: no codificar respuestas específicas, sino codificar **algoritmos adaptativos** que permitan al organismo ajustar su conducta a las condiciones particulares de su entorno, en tiempo real. A esto le llamamos **comportamiento adaptable**.

---

## Dos Tipos de Algoritmos Adaptativos

Dentro del comportamiento adaptable pueden distinguirse dos grandes familias de algoritmos, según la estructura estadística del entorno al que responden.

Considere la vida de una bacteria en el intestino. La glucosa está dispersa de manera impredecible y la bacteria carece de receptores que le permitan detectar la fuente a distancia. Una solución posible es el movimiento aleatorio; la que evolucionó es más efectiva: un algoritmo de ascenso de colina basado en comparaciones sucesivas de la concentración del nutriente. Si en este momento la concentración es mayor que hace un instante, continuar en la misma dirección; si es menor, cambiar. Este algoritmo no requiere memoria: utiliza solo información local del momento presente. En el Bloque I estudiaremos este tipo de mecanismos —todos reactivos, sin integración de experiencia previa.

Cuando el entorno tiene una estructura causal —cuando los SBI no ocurren al azar sino correlacionados con ciertos tiempos, lugares, señales o acciones— surge la posibilidad de aprovechar esa estructura. Un organismo que recuerda dónde encontró alimento ayer puede regresar mañana; uno que aprendió que cierto sonido precede a un depredador puede anticiparse. Estos algoritmos, que llamamos **aprendizaje**, integran la experiencia previa para reducir la incertidumbre sobre el entorno. La diferencia respecto a los algoritmos reactivos no es de complejidad superficial sino de lógica: el aprendizaje solo tiene sentido si el entorno tiene estructura que pueda detectarse y aprovecharse.

Esto nos lleva a una pregunta que es, en el sentido del capítulo sobre explicación, una pregunta de nivel computacional: ¿qué tipos de estructura estadística puede tener un entorno? Especificar esas propiedades es especificar los problemas que los mecanismos de aprendizaje deben resolver —y, por tanto, organizar qué mecanismos vale la pena estudiar.

---

## Las Propiedades Estadísticas del Entorno

Un entorno puede tener estructura —información aprovechable— a lo largo de varias dimensiones. Cuáles de esas dimensiones son relevantes para un organismo determina qué clase de mecanismo debe evolucionar. Las siguientes seis propiedades han dominado el estudio del comportamiento adaptable y, no por casualidad, organizan los bloques de este libro.

**1. Tiempo de Ocurrencia**

Los SBI pueden distribuirse de manera uniforme a lo largo del tiempo o concentrarse en ciertos períodos. Las flores abren al amanecer; los búhos cazan de noche; los restaurantes tienen horarios. Un organismo que detecta esas regularidades puede dedicar su tiempo de búsqueda a los momentos rentables y usarlo en otras actividades el resto del día. Esta adaptación requiere mecanismos que midan intervalos y detecten periodicidades.

**2. Lugar de Ocurrencia**

Los SBI también pueden distribuirse de manera uniforme en el espacio o concentrarse en ciertos parches. El alimento se concentra en ciertas zonas; los depredadores frecuentan ciertos territorios. Los organismos que detectan esa estructura espacial pueden dirigir su búsqueda eficientemente: regresar a lugares previamente productivos, evitar lugares peligrosos, explorar zonas con alta probabilidad de contener recursos no descubiertos.

**3. Covarianza con el Entorno y con el Comportamiento**

Muchos SBI no son predecibles por tiempo o lugar per se, sino que están correlacionados con otras características del mundo. Las nubes oscuras predicen lluvia; ciertos olores indican la proximidad de un depredador; el patrón de coloración de algunas orugas señala su toxicidad. Un organismo que aprende estas relaciones puede anticipar los SBI antes de encontrarlos directamente.

Una segunda forma de covarianza involucra las acciones del propio organismo: muchos SBI solo ocurren si se ejecutan ciertas respuestas. Las mascotas obtienen comida solo cuando realizan conductas específicas; el acceso a un servicio de taxis requiere abrir una aplicación. Aprender qué respuestas producen qué consecuencias permite al organismo no solo predecir, sino controlar activamente la ocurrencia de SBI.

Estas dos formas de covarianza —con señales del entorno y con el comportamiento propio— comparten la misma lógica: detectar qué predice qué. Sin embargo, plantean problemas de asignación de crédito suficientemente distintos como para requerir dos capítulos separados en el Bloque II.

**4. Detección de Cambios en el Estado del Entorno**

Un problema distinto surge cuando las propiedades estadísticas del entorno cambian sin señales externas evidentes. Una reducción en la disponibilidad de presas puede reflejar variación aleatoria normal o un cambio real en el estado del entorno. Quien deja de recibir mensajes de una persona cercana debe decidir si se trata de algo fortuito o de un cambio genuino en la relación. En la literatura clásica, este problema se ha estudiado principalmente como extinción —la desaparición de un reforzador previamente presente—, pero es más general: se trata de inferir si el estado del mundo ha cambiado o si lo observado es simplemente ruido.

**5. Tasa de Ocurrencia**

Los organismos no solo detectan si un SBI ocurre o no, sino también con qué frecuencia. Para una abeja, no es suficiente saber que una zona del jardín tiene flores con néctar; importa la tasa —cuántas flores por minuto— porque esa tasa determina la rentabilidad de explotar esa zona frente a explorar otra. La noción de tasa de ocurrencia desempeña un papel central en las explicaciones contemporáneas del comportamiento de elección, como veremos en el Bloque III.

**6. Incertidumbre Esperada e Inesperada**

Cualquiera de las propiedades anteriores puede ser más o menos incierta. Cuando la variabilidad es estable —cuando existe una distribución de probabilidad constante que la describe— hablamos de **incertidumbre esperada**. El camión de transporte público no pasa siempre exactamente a la misma hora, pero la variación es predecible: tiene una distribución con media y dispersión conocidas. Cuando los parámetros de esa distribución cambian ellos mismos de acuerdo a otra distribución, el entorno se vuelve **volátil** y la incertidumbre es inesperada. En el metro de la Ciudad de México, la probabilidad de que el tren llegue en los próximos dos minutos es alta en hora pico y baja en horas de poca demanda: hay una distribución que cambia según otra distribución. El Bloque V está dedicado a los mecanismos que permiten aprender en entornos volátiles.

---

Estas seis propiedades no son una taxonomía arbitraria. Son las dimensiones sobre las que un entorno puede tener estructura estadística que un agente puede, en principio, detectar y aprovechar. Si el entorno tiene regularidad en alguna de estas dimensiones y el organismo carece del mecanismo para detectarla, hay una oportunidad adaptativa sin explotar. Si la tiene, ese mecanismo tendrá ventaja selectiva. Los capítulos siguientes estudian, uno a uno, los mecanismos que evolucionaron para responder a cada tipo de estructura.

---

## Conclusión

Este capítulo ha descrito las condiciones bajo las cuales la selección natural produce distintos tipos de soluciones conductuales. En entornos constantes, produce comportamiento adaptado: respuestas codificadas genéticamente que no requieren aprendizaje individual. En entornos variables, produce comportamiento adaptable: algoritmos que ajustan la conducta a la estructura estadística particular de cada entorno.

Dentro del comportamiento adaptable, la distinción entre algoritmos reactivos —efectivos cuando el control debe ser local e inmediato— y algoritmos de aprendizaje —necesarios cuando el entorno tiene estructura causal aprovechable— organiza los dos primeros bloques del libro. Los Bloques III y IV extienden el análisis a la elección entre opciones y al aprendizaje de secuencias. El Bloque V aborda entornos volátiles. El Bloque VI examina la estructura de las preferencias que determinan el valor de los SBI.

Lo que conecta todos esos bloques es la lógica descrita en este capítulo: cada mecanismo que estudiaremos es una solución a un problema estadístico específico que el entorno plantea. Entender el problema es la condición para entender por qué el mecanismo tiene la forma que tiene.
