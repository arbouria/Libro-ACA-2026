# Revisión: Capítulo — Evolución del Comportamiento Adaptable
**Revisado por:** Claude  
**Fecha:** Febrero 2026  
**Estado:** Retroalimentación estructurada + versión corregida

---

# PARTE I: RETROALIMENTACIÓN ESTRUCTURADA

## 1. Diagnóstico general

El capítulo tiene materia prima sólida: la distinción entre comportamiento adaptado y adaptable está bien planteada, la restricción lineal de tiempo es un hallazgo elegante, y la taxonomía de propiedades estadísticas del entorno es genuinamente útil para organizar el resto del libro. El problema central no es conceptual sino de ejecución: el texto tiene muchos errores tipográficos que interrumpen la lectura, el ejemplo de apertura está incompleto y hay inconsistencias entre las partes del capítulo (la conclusión menciona "cuatro propiedades estadísticas" cuando el capítulo presenta seis categorías).

La buena noticia es que con correcciones de edición y algunos ajustes de estructura, este capítulo puede funcionar bien.

---

## 2. Errores tipográficos y gramaticales (muestra representativa)

Hay errores distribuidos en todo el texto que deben corregirse antes de cualquier revisión pedagógica:

| Ubicación | Error | Corrección |
|-----------|-------|------------|
| Párrafo 1 | "loneta a una toma" | "conecta a una toma" |
| Párrafo 1 | "ángeles solares" | "paneles solares" |
| Párrafo 1 | "d una toma eléctrica" | "de una toma eléctrica" |
| Párrafo 1 | "u considera", "Ud considera" | uniformar a "usted considera" |
| Párrafo 2 | "na compañía" | "una compañía" |
| Párrafo 2 | "caas" (dos veces) | "casas" |
| Párrafo 2 | "tendría el programa del robot, tendría..." | frase duplicada |
| Párrafo de restricciones | "enel" | "en el" |
| Párrafo de restricciones | "cognitivo¿s" | "cognitivos" |
| Sección 3 | "contra de estímulos" | "control de estímulos" |
| Conclusión | "cuatro propiedades estadísticas" | inconsistente: el capítulo presenta seis categorías |

---

## 3. Problemas estructurales

### 3.1 El ejemplo de apertura está incompleto y compite con Wall-E

El capítulo abre con un robot de servicio autónomo como ejemplo motivador, lo que es una buena idea porque es diferente al Wall-E ya usado en la Introducción. Sin embargo, el ejemplo tiene tres problemas: (a) está lleno de errores tipográficos que interrumpen la lectura, (b) la lógica de los tres robots (robot simple, robot multiambiente, robot explorador) está poco desarrollada —cada caso merece un párrafo completo—, y (c) la transición hacia "selección natural ha operado como el ingeniero" llega demasiado rápido.

**Sugerencia:** Conservar el ejemplo del robot de servicio, pero desarrollar los tres casos con más claridad y corregir todos los errores. La metáfora es pedagógicamente buena: el "ingeniero" que codifica vs. el que diseña un algoritmo de aprendizaje.

### 3.2 Falta el ejemplo del "marciano" para ilustrar el nivel computacional

Usted mismo señala que en clase usa el ejemplo de un marciano que llega a la Tierra y tiene que entender un vehículo. Este ejemplo es relevante justo antes de la sección de propiedades estadísticas del entorno, donde se argumenta que para entender *qué* debe aprender un organismo, primero hay que entender *el problema* que ese aprendizaje resuelve. El marciano que intenta entender el motor sin saber para qué sirve el coche ilustra perfectamente por qué el nivel computacional debe preceder al algorítmico.

### 3.3 La conclusión no corresponde al contenido del capítulo

La conclusión menciona "cuatro propiedades estadísticas" pero el capítulo presenta seis categorías: (1) tiempo de ocurrencia, (2) lugar de ocurrencia, (3) covarianza con señales del entorno, (4) covarianza con el comportamiento (cambio de estado), (5) tasa de ocurrencia, (6) incertidumbre esperada e inesperada. La conclusión también dice "cuatro propiedades" cuando el cuerpo del capítulo claramente tiene seis secciones numeradas.

Además, la conclusión menciona "covarianzas conductuales" como si fuera una de las cuatro propiedades, pero en el cuerpo del capítulo las covarianzas conductuales están integradas en la sección 3 sobre señales del entorno, sin sección propia. Esto crea confusión: ¿son cuatro o seis? ¿Las covarianzas con señales y con comportamiento son una o dos categorías?

**Sugerencia:** Decidir si son cuatro o seis categorías y hacer que el cuerpo y la conclusión sean consistentes. Mi recomendación: mantener seis, que corresponden más fielmente a lo que el libro desarrollará capítulo por capítulo.

### 3.4 La sección de "algoritmos adaptativos" necesita un párrafo de puente

Hay un salto entre "en estos entornos variables, la evolución favorece algoritmos adaptativos" y el ejemplo de la bacteria. El lector necesita entender brevemente la distinción entre algoritmos sin memoria (Bloque I) y algoritmos con integración de experiencia (Bloque II) antes de que aparezcan los ejemplos. El mapa del libro que está en la Introducción debería resonar aquí.

---

## 4. Fortalezas del capítulo (conservar sin cambios sustanciales)

- La ecuación $T = t_1 + t_2 + \ldots + t_n$ con la discusión de costo de oportunidad es excelente y está bien situada.
- Los ejemplos cotidianos en las secciones de propiedades estadísticas son muy buenos: camiones de transporte público, mensajes de WhatsApp, restaurantes, vacaciones en Cancún vs. Guanajuato. Mantenlos todos.
- La reinterpretación de la extinción como "detección de cambio" es pedagógicamente muy valiosa: cambia el marco de referencia de los estudiantes antes de que lleguen al capítulo correspondiente.
- La distinción entre incertidumbre esperada e inesperada (volatilidad) es sofisticada y está bien explicada para un capítulo de Bloque 0.

---

## 5. Sobre los "isms" y el tono

El capítulo actual no tiene demasiados "ismos" en sentido confrontacional —ese problema es más marcado en el capítulo de explicación. Aquí el tono es relativamente neutro. Lo que sí ocurre es que en algunos momentos el texto es un poco más declarativo de lo necesario ("El mensaje central es que..."). Sugiero simplemente terminar con lo que hay que decir sin anunciarlo.

---

## 6. Sobre la longitud y el uso de listas numeradas

Las seis propiedades estadísticas del entorno están bien organizadas como lista numerada con subtítulos en negrita. Es uno de los casos donde el formato de lista está pedagógicamente justificado: hay seis categorías paralelas y los estudiantes necesitan poder regresar a cada una como referencia. Mantener el formato de lista aquí.

---

## 7. Decisiones documentadas en esta revisión

| Decisión | Rationale |
|----------|-----------|
| Conservar ejemplo del robot (apertura) pero reescribir | Es distinto del Wall-E de la Introducción; la metáfora "ingeniero que codifica vs. ingeniero que diseña algoritmos" es valiosa |
| Agregar ejemplo del "marciano" como caja de texto o párrafo | El autor lo usa en clase; ilustra por qué el nivel computacional precede al algorítmico |
| Cambiar "cuatro propiedades" a "seis" en conclusión | Consistencia con el cuerpo del capítulo |
| Corregir "ángeles solares" → "paneles solares" | Error tipográfico sustantivo (cambia el sentido) |
| Separar covarianzas ambientales de covarianzas conductuales | En el cuerpo del capítulo ambas están en la sección 3; la conclusión las trata como categorías separadas; sugiero darle a las covarianzas conductuales su propia sección (4) para consistencia con el resto del libro |
| Suavizar el final de la conclusión | Eliminar frases que anuncian lo que ya se dijo ("El mensaje central es que...") |

---

---

# PARTE II: VERSIÓN CORREGIDA

---

# Capítulo 3: Restricciones, Entorno y Comportamiento Adaptable

Suponga que es ingeniero y su empresa le pide diseñar un robot de servicio autónomo para hogares. En su primera versión, el dueño conecta el robot a una toma de corriente antes de acostarse, como lo hace con su celular. Durante la noche el robot trabaja con esa energía y por la mañana, cuando la batería se agota, se detiene. Usted puede mejorar la autonomía con baterías de mayor duración, pero el problema no desaparece: más tarde o más temprano, sin una fuente de recarga, el robot se inmoviliza. Un robot verdaderamente autónomo tendría que recargarse por sí mismo.

Para que el robot pueda reabastecerse de energía sin intervención humana, su diseño depende del entorno donde operará. Si todas las casas fueran idénticas y la toma de corriente siempre estuviera en el mismo lugar, bastaría programar la ruta: a tal hora, dirigirse al punto X. Pero si las casas varían en diseño y distribución —que es el caso real—, el robot necesita un algoritmo que le permita aprender dónde están las tomas en cada nuevo hogar. Un robot aún más sofisticado, destinado a rentar sus servicios en distintas casas, debería además generalizar ese aprendizaje: usar lo que aprendió en la primera casa para reducir el tiempo de exploración en las siguientes. Y si el robot fuera a explorar un planeta desconocido, necesitaría algo más: algoritmos que le permitan aprender en condiciones de incertidumbre profunda sobre cómo funciona ese entorno.

La selección natural ha operado exactamente como ese ingeniero. Los agentes biológicos —bacterias, invertebrados, vertebrados, humanos— enfrentan el mismo problema fundamental que los robots: obtener los recursos necesarios para sobrevivir y reproducirse, lo que en este libro llamamos **sucesos biológicamente importantes** (SBI). Como vimos en el capítulo anterior, la variabilidad heredable en el éxito para acceder a los SBI genera diferencias en éxito reproductivo, y esas diferencias, acumuladas a lo largo de generaciones, producen adaptación. La pregunta de este capítulo es: ¿qué tipos de soluciones ha seleccionado la evolución, y qué determina cuál es la más apropiada en cada caso?

La respuesta depende de dos conjuntos de restricciones: las que impone el propio organismo, y las que impone su entorno.

---

## Las Restricciones del Organismo

El comportamiento tiene costos. El primero, y el más fundamental, es que cualquier comportamiento consume tiempo, y el tiempo disponible es finito. Si sumamos la duración de todos los comportamientos posibles de un organismo a lo largo de un período, obtenemos el total del tiempo disponible. No existe tal cosa como un momento de inactividad en sentido estricto: incluso "permanecer quieto" o "dormir" es un comportamiento que ocupa tiempo y tiene funciones específicas.

$$T = t_1 + t_2 + t_3 \dots + t_n$$

Esta es una *restricción lineal*: los diferentes comportamientos compiten entre sí por el tiempo disponible. Cada segundo dedicado a buscar alimento es un segundo menos disponible para vigilar la presencia de depredadores, para aparearse, para descansar. A esto le llamamos **costo de oportunidad**: el valor de la mejor alternativa a la que se renuncia cuando se elige una opción. Un agente que dedica demasiado tiempo a esconderse de depredadores tendrá poco tiempo para obtener alimento o encontrar pareja, y dependiendo del entorno, esto puede resultar en menor éxito reproductivo que un animal con una distribución de tiempo más equilibrada. Un estudiante que dedica todo su tiempo al esparcimiento tendrá pocas horas para estudiar, y viceversa. Estos **trade-offs** son ubicuos en biología y en la vida cotidiana porque las restricciones fundamentales —tiempo finito, energía limitada— hacen imposible maximizar todo simultáneamente. Como vimos al hablar de paisajes adaptativos en el capítulo anterior, el óptimo es siempre un balance entre presiones en tensión. Esta restricción reaparece con fuerza en el Bloque III, cuando estudiemos cómo los organismos distribuyen su comportamiento entre opciones que compiten.

Un segundo grupo de restricciones del organismo incluye su estructura biológica, metabólica, neuronal y física. Estas características delimitan el rango de comportamientos posibles —lo que llamamos el **espacio de posibilidades**— y determinan el costo energético de cada uno. Un animal pequeño no puede perseguir presas grandes; un animal con visión nocturna limitada no puede forrajear eficientemente en la oscuridad. A estas restricciones se suman, más recientemente estudiados, los **costos cognitivos** asociados con diferentes algoritmos: algunos mecanismos de aprendizaje requieren mayor capacidad de memoria o procesamiento, lo que no es gratuito en términos energéticos.

---

## Las Restricciones del Entorno

Además de las limitaciones del propio organismo, el entorno impone sus propias condiciones sobre el acceso a los SBI. La más fundamental es si las condiciones que determinan la disponibilidad de esos sucesos son **constantes o variables** a lo largo del tiempo.

Cuando las condiciones son relativamente constantes —cuando el entorno que enfrenta una especie no ha cambiado sustancialmente a lo largo de su historia evolutiva— la selección natural puede codificar directamente en el genoma las respuestas apropiadas. El resultado es lo que llamaremos **comportamiento adaptado**: patrones conductuales que no requieren aprendizaje individual porque la solución ya está incorporada filogenéticamente. El reflejo de retirada ante un estímulo doloroso es un ejemplo: la relación entre calor intenso y daño tisular ha sido suficientemente constante durante millones de años como para que la selección codificara la respuesta sin necesidad de que cada individuo la aprenda desde cero. Otro caso es la impronta en aves: los patitos siguen al primer objeto en movimiento que perciben después de la eclosión porque, en la historia de esa especie, ese primer objeto era invariablemente la madre.

El ingeniero que escribe directamente en el código del robot la respuesta correcta está haciendo, en miniatura, lo mismo que la selección natural hace con el comportamiento adaptado.

Sin embargo, los entornos de la mayoría de los organismos —y de cualquier robot de servicio o exploración espacial realista— son variables, volátiles e inciertos. Los SBI aparecen y desaparecen en el tiempo y en el espacio, pueden estar correlacionados con otras características del entorno, y esa estructura cambia. En condiciones así, una respuesta conductual genéticamente fija sería evolutivamente subóptima. Ante un entorno variable, la selección natural favorece algo radicalmente diferente: no codificar respuestas específicas, sino codificar **algoritmos adaptativos** que permitan al organismo ajustar su conducta a las condiciones de su entorno particular, en tiempo real. A esto le llamamos **comportamiento adaptable**.

---

## Dos Tipos de Algoritmos Adaptativos

Dentro del comportamiento adaptable pueden distinguirse dos grandes familias de algoritmos, según la estructura estadística del entorno al que responden.

Considere la vida de una bacteria en el intestino. La glucosa está dispersa de manera impredecible y la bacteria carece de receptores que le permitan detectar la fuente a distancia. Una solución posible es el movimiento aleatorio, pero hay otra más efectiva: un algoritmo de ascenso de colina basado en comparaciones sucesivas de la concentración del nutriente. Si en este momento la concentración es mayor que hace un instante, continúa en la misma dirección; si es menor, cambia. Este algoritmo no requiere memoria: utiliza solo información local del presente inmediato. En el Bloque I estudiaremos este tipo de mecanismos y sus variantes, todos con la característica común de que el control del comportamiento es enteramente reactivo, sin integración de experiencia previa.

Cuando, en cambio, el entorno tiene una estructura causal —cuando los SBI no ocurren al azar sino correlacionados con ciertos tiempos, lugares, señales o acciones— surge la posibilidad, y la ventaja evolutiva, de algoritmos que **integren experiencia previa**. A estos algoritmos los llamamos **aprendizaje**. La diferencia respecto a los algoritmos puramente reactivos es que el aprendizaje permite al organismo reducir la incertidumbre sobre el entorno acumulando información a lo largo del tiempo. Un organismo que aprende puede predecir cuándo y dónde aparecerán los SBI y ajustar su distribución de comportamiento en consecuencia: si la comida solo está disponible en ciertos horarios, no tiene sentido dedicar tiempo de búsqueda en otros momentos.

> **El nivel computacional y el nivel algorítmico**
>
> Imagine que un extraterrestre llega a la Tierra y encuentra un automóvil. Podría intentar entenderlo examinando cada componente: cómo giran los pistones, cómo fluye el combustible, cómo funciona la transmisión. Obtendría información precisa sobre el mecanismo, pero sin saber para qué sirve el automóvil —que es un vehículo diseñado para transportar personas de un lugar a otro—, esa información sería difícil de organizar. La comprensión del *qué problema resuelve* precede y orienta la comprensión del *cómo lo resuelve*.
>
> En psicología del aprendizaje ocurre algo similar. Podemos describir con precisión qué neuronas se activan o qué ecuación describe el cambio de una asociación, pero si no sabemos qué problema adaptativo resuelve el mecanismo, esos detalles son difíciles de integrar. Por eso, antes de describir los algoritmos del aprendizaje, conviene especificar el tipo de problemas estadísticos que esos algoritmos deben resolver.

---

## Propiedades Estadísticas del Entorno: Los Problemas que el Aprendizaje Debe Resolver

Para entender qué tipo de mecanismos de aprendizaje han evolucionado, es útil primero caracterizar las propiedades del entorno que esos mecanismos deben detectar. A continuación describimos seis categorías de problemas estadísticos que aparecerán, en distintas formas, a lo largo del libro.

**1. Tiempo de Ocurrencia**

Muchos SBI exhiben regularidades temporales. Las flores abren al amanecer; los búhos cazan de noche; los restaurantes tienen horarios. Un organismo que detecta esas regularidades puede distribuir mejor su tiempo: forrajear cuando hay alimento, esconderse cuando el riesgo de depredación es mayor, prepararse para la reproducción antes de que llegue la ventana crítica. Esta adaptación requiere mecanismos que midan intervalos y detecten periodicidades.

**2. Lugar de Ocurrencia**

Los SBI también tienen estructura espacial. El alimento se concentra en ciertos parches; los depredadores frecuentan ciertos territorios; las librerías tienen libros y los hospitales tienen médicos. Los organismos que detectan esa estructura espacial pueden dirigir su búsqueda eficientemente: regresar a lugares donde previamente encontraron recursos, evitar lugares donde encontraron peligro, explorar zonas con alta probabilidad de contener recursos no descubiertos. Esta capacidad requiere mecanismos de memoria espacial y navegación.

**3. Covarianza con Señales del Entorno**

Muchos SBI no son predecibles por tiempo o lugar per se, sino que están anunciados por características del entorno. Las nubes oscuras predicen lluvia. Ciertos olores indican la proximidad de un depredador. El patrón de coloración de algunas orugas señala su toxicidad. Una alarma sísmica anticipa un terremoto. Los organismos que aprenden estas relaciones predictivas pueden anticipar los SBI antes de encontrarlos directamente, lo que permite prepararse o evitarlos. Los bloques II y V del libro están dedicados principalmente a este tipo de aprendizaje.

**4. Covarianza con el Comportamiento Propio**

Una segunda forma de covarianza involucra las acciones del propio organismo. Muchos SBI no ocurren independientemente del comportamiento: solo aparecen si se ejecutan ciertas respuestas. Las mascotas obtienen comida solo cuando realizan conductas específicas. El acceso a un servicio de transporte requiere abrir una aplicación. Ajustar la probabilidad de diferentes respuestas en función de sus resultados históricos permite al organismo no solo predecir, sino controlar activamente la ocurrencia de SBI. El Bloque III está dedicado a este problema.

**5. Detección de Cambios en el Estado del Entorno**

Un problema particularmente difícil surge cuando las propiedades estadísticas del entorno cambian sin señales externas evidentes. Una reducción en la disponibilidad de presas puede reflejar variación aleatoria normal o un cambio real en el estado del entorno. Un joven que deja de recibir mensajes de una persona cercana debe decidir si se trata de algo fortuito o de un cambio en la relación. En la literatura clásica, este problema se ha estudiado principalmente como extinción —la desaparición de un reforzador previamente presente—, pero es más general: se trata de inferir si el estado del mundo ha cambiado o si lo observado es ruido. Este problema aparece en varios bloques del libro.

**6. Tasa de Ocurrencia de los SBI**

Finalmente, los organismos no solo detectan si un SBI ocurre o no, sino también con qué frecuencia. Para una abeja, no es suficiente saber que una zona del jardín tiene flores con néctar; importa la *tasa* —cuántas flores por minuto— porque esa tasa determina la rentabilidad de explotar esa zona versus explorar otra. La decisión de dónde pasar vacaciones se basa no en un evento aislado sino en la tasa de momentos agradables que cada destino ha ofrecido. La noción de tasa de ocurrencia desempeña un papel central en las explicaciones contemporáneas del comportamiento de elección, como veremos en el Bloque III.

Una propiedad transversal a todas las categorías anteriores es que cualquiera de estas regularidades puede variar según el contexto: la disponibilidad de alimento cambia entre el día y la noche; el riesgo de depredación varía entre el campo abierto y el bosque; las reglas que gobiernan el trato social son distintas en la escuela que en casa. El capítulo sobre control de estímulos mostrará cómo los organismos ajustan finamente su comportamiento al contexto, y cuáles son los algoritmos que hacen posible ese ajuste.

Finalmente, cualquiera de las seis propiedades anteriores puede ser más o menos incierta. Cuando la incertidumbre es estable —cuando existe una distribución de probabilidad constante que describe la variabilidad—, hablamos de **incertidumbre esperada**. El camión de transporte público no pasa siempre exactamente a la misma hora, pero la variación es predecible: tiene una distribución con media y dispersión conocidas. Cuando los parámetros de esa distribución cambian ellos mismos de acuerdo a otra distribución, el entorno se vuelve **volátil** y la incertidumbre es inesperada. En el metro de la Ciudad de México, la probabilidad de que el tren llegue en los próximos dos minutos es alta en hora pico y baja en horas de poca demanda: no hay una sola distribución que la describa, sino una distribución que cambia según otra distribución. El Bloque V está dedicado a los mecanismos que permiten aprender en entornos volátiles.

---

## Conclusión: El Mapa del Libro

Este capítulo ha delineado las restricciones fundamentales sobre el acceso a los SBI —la finitud del tiempo, las limitaciones biológicas del organismo, y las propiedades estadísticas del entorno— y ha esbozado dos tipos de soluciones que la evolución ha seleccionado: comportamiento adaptado, para entornos constantes, y comportamiento adaptable, para entornos variables.

Dentro del comportamiento adaptable, la distinción entre algoritmos sin integración de historia —efectivos cuando el control debe ser puramente reactivo— y algoritmos de aprendizaje —necesarios cuando el entorno tiene una estructura causal que puede aprovecharse— organiza los bloques del libro. Los Bloques I y II corresponden a estas dos categorías de mecanismos. Los Bloques III y IV extienden el análisis a la elección entre opciones y al aprendizaje de secuencias. El Bloque V enfrenta el problema de la volatilidad. El Bloque VI examina la estructura de las preferencias que determinan el valor de los SBI.

Las seis propiedades estadísticas del entorno descritas en este capítulo —tiempo, lugar, covarianza con señales, covarianza con comportamiento, detección de cambio de estado, tasa de ocurrencia— aparecerán en distintas formas a lo largo de ese recorrido. Tenerlas presentes desde ahora permite ver los fenómenos de aprendizaje no como una colección de curiosidades experimentales, sino como soluciones a problemas estadísticos bien definidos.

---
#libronotasACA/notas/adaptabilidad

---

# PARTE III: NOTAS PARA EL AUTOR

## Preguntas abiertas que requieren su decisión

1. **¿Cuántas categorías de propiedades estadísticas?** El capítulo actualmente tiene seis. Podría simplificarse a cuatro combinando "covarianza con señales" y "covarianza con comportamiento" en una sola categoría, y "detección de cambio" con "incertidumbre". Yo prefiero las seis porque cada una corresponde a un bloque o sección específica del libro. Pero si pedagógicamente seis se siente excesivo para una primera presentación, cuatro pueden funcionar.

2. **¿Sección propia para covarianzas conductuales?** En la versión original, las covarianzas conductuales estaban mezcladas en la sección de señales del entorno. En la versión corregida les di sección propia (sección 4). Esto hace el capítulo más largo pero más consistente con la estructura del libro, donde condicionamiento clásico (covarianza con señales) y operante (covarianza con comportamiento) son bloques separados.

3. **¿Dónde está el asta de bandera?** La instrucción original menciona que los estudiantes tienen dificultad con ese ejemplo. No lo encontré en el texto del capítulo, así que asumo que fue eliminado en alguna versión anterior. Si desea reintroducir algún ejemplo de ese tipo, avíseme y lo integro.

4. **El ejemplo del "marciano"** lo incluí como caja de texto (recuadro) al introducir el nivel computacional. Puede convertirse en párrafo corrido si el formato de cajas no está disponible en la plataforma de publicación.

## Conexiones con capítulos previos/posteriores

- **Del capítulo de selección natural:** Los trade-offs y óptimos locales mencionados allí aparecen aquí como "costo de oportunidad" y "restricción lineal". Vale una referencia explícita al momento de introducir la ecuación T = t₁ + t₂ + ... + tₙ.
- **Hacia el Bloque I:** El ejemplo de la bacteria como algoritmo de ascenso de colina sin memoria anuncia directamente el capítulo de ascenso de colina. Está bien situado.
- **Hacia el Bloque II:** La sección de "covarianza con señales del entorno" prepara el terreno para asignación de crédito. El ejemplo del tono y la comida podría anticiparse brevemente aquí si desea hacerlo, o puede dejarse implícito.
