# Capítulo 8: El Problema de la Asignación de Crédito {#sec-asignacion-credito}

## Objetivos del Capítulo

Al finalizar este capítulo, deberías ser capaz de explicar por qué el problema de la asignación de crédito es computacionalmente intratable sin mecanismos de filtrado, y cómo la evolución resolvió este problema mediante sesgos inductivos específicos. En particular, comprenderás que la contigüidad temporal, aunque útil, no es ni necesaria ni suficiente para el aprendizaje, y que el sistema nervioso opera como un detector de información que asigna crédito basándose en reducción de incertidumbre más que en simple co-ocurrencia. Identificarás los principales sesgos inductivos—sistemas de comportamiento, relevancia biológica, novedad, saliencia—y reconocerás evidencia empírica de competencia entre elementos por asignación de crédito en fenómenos como el ensombrecimiento y el bloqueo. Finalmente, comprenderás cómo estos hallazgos preparan el terreno para modelos formales basados en error de predicción que estudiaremos en el próximo capítulo.

---

## Introducción: El Detective Causal

Al interactuar con su entorno, un agente se encuentra con un constante flujo de estímulos y respuestas que se despliegan en el tiempo. Algunos de los sucesos que encuentra son biológicamente significativos, importantes para su éxito reproductivo o su supervivencia inmediata. El encuentro inesperado con un suceso biológicamente importante (SBI) echa a andar dos mecanismos: uno que controla la respuesta inmediata al SBI—consumir la comida, huir del depredador—y un segundo mecanismo que permite predecir su futura ocurrencia y, cuando sea posible, controlarlo. Es este segundo mecanismo el que nos interesa en este capítulo.

Considere un organismo que encuentra un inesperado pedazo de comida o un depredador. El primer mecanismo le permite al organismo manipular y consumir la comida, o huir y escapar del depredador. El segundo mecanismo, el que posibilita predecir y controlar un SBI, implica la existencia de una estructura causal en el entorno del organismo: esto es, que existen sucesos que predicen, o respuestas que producen, la comida o que permiten evitar al depredador. La tarea para el agente es seleccionar, dentro de un número gigantesco de posibilidades, a cuál suceso o respuesta atribuirle la ocurrencia de un SBI. A este problema de adaptación se le conoce como el de la *asignación de crédito*.

### La Magnitud del Problema

El vasto espacio de posibles candidatos para la asignación de crédito de un SBI incluye la hora a la que ocurre, dónde ocurre, el enorme grupo de sucesos que lo acompañan o los comportamientos que un organismo genera; pero también podemos incluir momentos, espacios, sucesos y comportamientos que ocurrieron en cualquier momento previo. La comida que un perro callejero se encuentra en una banqueta puede deberse a un transeúnte que el perro percibe en ese momento alejándose de la comida, o a miles de posibles transeúntes que la tiraron en un tiempo cada vez más alejado de su encuentro con el alimento. Pudo deberse a alguien que la tiró desde un transporte público un segundo antes, o diez minutos antes, o un día antes.

O considere su propia experiencia: regresa a casa después de comer en un restaurante nuevo y experimenta un fuerte malestar estomacal. ¿Qué causó su enfermedad? Las posibilidades son abrumadoras. Podría ser el sabor del platillo que ordenó, el olor del restaurante, la música que sonaba, el color de las paredes, la hora del día, su compañero de mesa, algo que comió ayer, algo que tocó en el transporte público, el estrés acumulado de su día. Esta lista podría extenderse indefinidamente hacia el pasado. Cada segundo de su vida antes del malestar contiene miles de eventos que, en principio, podrían ser la causa. ¿Cómo determina cuál fue realmente responsable?

Este problema no es una curiosidad teórica. En el Capítulo 2 establecimos que la tarea fundamental de un organismo es reducir la incertidumbre acerca de la ocurrencia de sucesos biológicamente importantes. Para lograrlo, debe identificar las señales predictivas en su entorno. Pero el entorno es un flujo constante de estimulación: en cualquier momento, cientos de estímulos están presentes simultáneamente, y miles de eventos han ocurrido en el pasado reciente. Sin algún mecanismo para filtrar este vasto espacio de posibilidades, el aprendizaje sería computacionalmente intratable.

### Sesgos Inductivos como Solución Evolutiva

Para hacer más manejable la asignación de crédito ante las limitaciones de nuestras observaciones y la riqueza de candidatos, la selección natural filtró mecanismos que llamamos *sesgos inductivos*, los cuales logran dos cometidos: primero, reducen drásticamente el espacio de candidatos a asignación de crédito y, segundo, establecen un orden de evaluación para poner a prueba a los candidatos del espacio más reducido en un momento posterior. Los sesgos pueden ser el resultado de la codificación genética de propiedades del entorno bajo el cual evolucionó la especie del organismo, o el resultado de su experiencia y aprendizaje individuales.

Estos sesgos no son "limitaciones" o "irracionalidades" del sistema de aprendizaje. Son soluciones evolutivas a un problema computacional genuino. En ciencia de la computación y aprendizaje automático, este concepto se conoce como *sesgo inductivo* (inductive bias): restricciones que guían el aprendizaje hacia ciertas hipótesis sobre otras. Sin sesgos inductivos, el aprendizaje de cualquier estructura en datos es imposible—este es un teorema formal conocido como el "No Free Lunch Theorem". Los organismos enfrentan el mismo dilema, y la evolución resolvió el problema construyendo arquitecturas cognitivas con sesgos específicos.

En este capítulo exploraremos cuáles son estos sesgos, qué tan efectivos son, y crucialmente, cuáles son sus límites. Nos concentraremos en el aprendizaje asociativo: cómo los organismos aprenden que ciertos estímulos (eventos en el mundo) predicen ciertos resultados (SBI). Dividiremos nuestra discusión en dos partes. La Parte I examina el problema de la asignación de crédito a estímulos: ¿qué eventos en el ambiente predicen el SBI? La Parte II, que será cubierta en el Capítulo 9, abordará el problema paralelo pero distinto de la asignación de crédito a respuestas: ¿qué acciones del organismo producen o previenen el SBI?

---

## Parte I: Asignación de Crédito a Estímulos

### El Paradigma de Pavlov y el Sesgo de Contigüidad

Históricamente, la contigüidad entre sucesos fue el primer sesgo en recibir atención. El sesgo consiste en suponer que la "contigüidad" entre un estímulo o una respuesta y un SBI es una regla evolutiva muy útil para reducir el espacio de opciones de asignación de crédito. El espacio de asignación de crédito se reduce a solo aquellos eventos contiguos con el SBI. Si al momento en que el perro callejero encontró la comida prestaba atención a una ambulancia que pasaba con la sirena encendida y a un transeúnte vestido como estudiante universitario, su espacio de asignación de crédito se reduciría a esos dos sucesos. Para seleccionar entre ellos, operaría un segundo sesgo que veremos en una sección subsecuente.

A principios del siglo XX, Ivan Pavlov le dio sentido experimental y conceptual al estudio de este sesgo. El propósito de los experimentos de Pavlov fue establecer la importancia de la contigüidad en la formación de nuevas asociaciones entre estímulos previamente neutrales y respuestas reflejas. El protocolo, representado en la Figura 8.1, consistió en presentarle a un perro un estímulo auditivo seguido por acceso a comida. Pavlov midió la salivación ante la comida y ante el estímulo auditivo, antes y después de haber sido presentado junto con la comida. Encontró que aparear el sonido con la comida resultó en que el perro salivara ahora no tan solo a la comida, sino también al sonido. Al sonido se le conoce como *estímulo condicionado* (EC) y a la comida como *estímulo incondicionado* (EI). En la terminología que hemos adoptado en este curso, el EI es un caso particular de un suceso biológicamente importante (SBI).

La lógica del procedimiento de Pavlov es elegante en su simplicidad: si la contigüidad temporal es el mecanismo fundamental de la asignación de crédito, entonces un estímulo neutral (el tono) que aparece consistentemente contiguo a un SBI (la comida) debería adquirir la capacidad de provocar respuestas similares a las que provoca el SBI mismo. El resultado de salivación al tono, denominado *respuesta condicionada* (RC), es evidencia de que el organismo ha asignado crédito al tono como predictor de la comida.

### El Gradiente de la Demora

En los primeros protocolos experimentales se consideraba solo un candidato al cual asignar crédito (como un tono) y la manipulación experimental era una imprecisa medida de contigüidad que implicaba diferentes relaciones temporales entre el EC y el EI. Pavlov y sus sucesores exploraron sistemáticamente estas variaciones temporales. En el *condicionamiento simultáneo*, el EC y el EI se presentan exactamente al mismo tiempo, iniciando y terminando juntos; se encontró que este procedimiento produce aprendizaje pobre. En el *condicionamiento de demora corta*, el EC inicia primero y el EI se presenta mientras el EC aún está presente, con una demora típica de medio segundo a dos segundos; este procedimiento produce aprendizaje excelente. En el *condicionamiento de demora larga*, el EC inicia y después de una demora extensa (varios segundos a minutos) aparece el EI; el aprendizaje disminuye conforme aumenta la demora. En el *condicionamiento de huella*, el EC termina completamente antes de que inicie el EI, dejando un "intervalo vacío" entre ambos; nuevamente, el aprendizaje disminuye con la duración de este intervalo. Finalmente, en el *condicionamiento hacia atrás*, el EI se presenta primero y el EC aparece después; este procedimiento produce aprendizaje mínimo o nulo.

El patrón que emerge de estos estudios se conoce como el *gradiente de la demora*: la fuerza del condicionamiento disminuye sistemáticamente conforme incrementa el tiempo entre la terminación del EC y el inicio del EI. Dependiendo de la preparación y la modalidad sensorial, después de menos de un minuto de intervalo entre EC y EI, frecuentemente no se observa aprendizaje alguno. Este gradiente sugiere que la contigüidad no es binaria—presente o ausente—sino gradual. Mientras más cercanos en el tiempo, mayor es el crédito asignado al estímulo como predictor del SBI.

### ¿Es la Contigüidad una Condición Necesaria?

El gradiente de la demora parecía establecer la contigüidad como un principio fundamental: sin proximidad temporal, no hay aprendizaje. Pero nos podemos preguntar si esta generalización es realmente universal. ¿Es la contigüidad una condición necesaria para el aprendizaje en todos los contextos? Un descubrimiento accidental de John García cambió radicalmente esta perspectiva.

García estaba estudiando los efectos de la radiación en ratas. Accidentalmente notó que las ratas desarrollaban aversión a su comida habitual después de ser irradiadas, a pesar de que el malestar gástrico causado por la radiación ocurría horas después de comer. Este hallazgo violaba directamente el gradiente de la demora establecido por Pavlov. Intrigado, García diseñó una serie de experimentos sistemáticos para explorar este fenómeno.

El experimento más influyente, realizado por García y Koelling en 1966, es un modelo de elegancia experimental. A todas las ratas se les daba acceso a un bebedero con agua azucarada en el cual cada contacto detonaba la presentación de un tono y una luz brillante. De esa forma había un compuesto conformado por dos tipos de estímulos: uno gustativo (el agua dulce) y uno audiovisual (el tono y la luz, que García llamó "brillante-ruidoso"). A la mitad de los animales se les daba una descarga eléctrica inmediata con cada lengüetazo que daban al bebedero, mientras que a la otra mitad se les inyectaba una sustancia que producía un malestar estomacal que se manifestaba horas después de la ingesta.

Los resultados fueron sorprendentes. García encontró que las ratas que recibieron las descargas eléctricas no dejaron de beber el agua azucarada, pero sí evitaban tocar el bebedero cuando este producía el tono y la luz. Mientras tanto, las ratas con malestar estomacal dejaban de beber el agua dulce, pero no presentaban aversión al tono ni a la luz. Este patrón cruzado demuestra dos cosas simultáneamente: primero, que la contigüidad no es una condición necesaria para el aprendizaje—las ratas aprendieron una aversión al sabor con demoras de horas entre el consumo y el malestar. Segundo, que la naturaleza del SBI determina cuáles elementos entran en el espacio de asignación de crédito.

### El Sesgo de Relevancia Biológica

Para las ratas, igual que para otras especies omnívoras como la nuestra, cuando el SBI es un malestar estomacal, el espacio de elección está conformado por elementos con sabor, pero no por elementos visuales o auditivos. Al sentirnos mal del estómago, lo primero que hacemos es buscar qué comimos, aunque nuestra última comida haya sido muchas horas antes. Rara vez nos preguntamos qué música estábamos escuchando o qué ropa llevábamos puesta. A este sesgo se le conoce como el sesgo de *relevancia biológica* o *preparación evolutiva* (preparedness).

Este sesgo no es arbitrario. Es el producto de la historia evolutiva de la especie. Para especies omnívoras que viven principalmente en la oscuridad, como las ratas, es fundamental detectar qué alimento es tóxico por su sabor. La visión no les proporciona información confiable sobre toxicidad en entornos oscuros, pero el sabor sí. Otras especies que habitan nichos ecológicos diferentes despliegan sesgos distintos. Las palomas, que forrajean visualmente en ambientes iluminados, no generan aversiones a sabores con la misma facilidad que las ratas. Para estas aves, la dimensión relevante es la estimulación visual, no el sabor del alimento.

La coevolución entre aves y polillas ejemplifica la importancia de la relevancia biológica. Las polillas son un alimento para ciertas aves; por otro lado, la selección natural resultó en algunas especies de polillas que son tóxicas para las aves. Esta toxicidad es identificable a través de señales visualmente perceptibles—patrones de colores llamativos y contrastantes. Gracias a esto, las aves pueden desplegar su sesgo de relevancia biológica hacia los estímulos visuales y aprender a evitar este tipo de polilla después de una sola experiencia aversiva. Este fenómeno se conoce como *aposematismo*. Simultáneamente, otro grupo de polillas no tóxicas evolucionaron para tomar ventaja de ese mismo sesgo de las aves y desarrollaron patrones visuales similares a los de las especies tóxicas para evitar ser depredadas. Este fenómeno se conoce como *mimetismo batesiano*. El sistema completo—toxicidad, aposematismo, sesgo de aprendizaje de las aves, y mimetismo—es un ejemplo magistral de cómo la selección natural moldea tanto las señales en el ambiente como los sesgos de aprendizaje que las detectan.

### El Sesgo de Novedad

Los estudios de aversión a sabores revelaron otro sesgo fundamental: la novedad. En una serie de experimentos, García presentó a las ratas dos sabores antes de inducir malestar gástrico: uno familiar (que las ratas habían probado repetidamente en días previos) y uno novedoso (que probaban por primera vez). Ambos sabores estaban igualmente contiguos con la enfermedad en el momento crítico. García encontró que las ratas desarrollaban aversión al sabor novedoso, pero no al familiar. El sistema de aprendizaje prioriza estímulos novedosos sobre familiares al asignar crédito.

Este sesgo también tiene sentido adaptativo. Si un organismo ha consumido un alimento familiar múltiples veces sin consecuencias aversivas, es improbable que ese alimento sea la causa de un episodio aislado de enfermedad. En cambio, un alimento nuevo es un candidato más plausible. Este sesgo hacia la novedad reduce la probabilidad de desarrollar aversiones incorrectas a alimentos seguros y dirige el aprendizaje hacia los verdaderos culpables.

### Resumen: Los Límites de la Contigüidad como Condición Necesaria

Los estudios de aversión a sabores demuestran que:

1. La contigüidad no es una condición necesaria para el aprendizaje. Se puede aprender con demoras de muchas horas entre el EC y el EI.

2. Sin embargo, existe un gradiente temporal: hay mayor aversión al sabor más cercano al malestar estomacal, incluso cuando múltiples sabores precedieron la enfermedad.

3. Existen sesgos biológicos que generan una predisposición a considerar solo ciertos estímulos para asignación de crédito. Estos sesgos dependen tanto de la naturaleza del SBI como de la historia evolutiva de la especie.

4. Un sesgo adicional importante es priorizar sucesos novedosos o sorprendentes dentro del proceso de asignación de crédito.

5. La contigüidad es uno de los sesgos útiles, pero no constituye una condición necesaria universal para el aprendizaje.

---

## ¿Es la Contigüidad una Condición Suficiente?

A finales de los años 60 del siglo pasado, un grupo de investigadores, entre los que destacan Leon Kamin, Robert Rescorla y Allan Wagner, condujeron una serie de experimentos dirigidos a darle respuesta a una pregunta complementaria: ¿es la contigüidad una condición suficiente para el aprendizaje? Es decir, ¿basta con que un estímulo sea contiguo a un SBI para que adquiera propiedades predictivas? En estos experimentos se presentó un compuesto de dos o más estímulos condicionados, igualmente contiguos con el suceso biológicamente importante. Un ejemplo de un compuesto de estímulos es la presentación simultánea de una luz y un tono, o la combinación de una figura visual y un color.

### Ensombrecimiento: Competencia por Saliencia

Los sucesos que anteceden a un suceso biológicamente importante regularmente están compuestos de estímulos que varían en diferentes dimensiones. Un perro que los amenaza no solo ladra y gruñe, tiene también cierto color, ciertos ojos y cierta expresión facial. Si les llegara a morder, todas estas características del perro estarían igualmente contiguas con el suceso aversivo de la mordida. Si la contigüidad fuese suficiente para el aprendizaje, todas y cada una de las características del perro se convertirían en predictores de un ataque. Pero ¿es esto lo que ocurre?

Reynolds puso a prueba esta conjetura con un experimento sencillo pero revelador. A dos palomas se les entrenó a discriminar entre dos teclas a las que podían picar. Una de las teclas, cuando era picada, generaba acceso a un comedero; la otra no. Las teclas estaban iluminadas por un compuesto de dos estímulos que variaban en forma y color. La tecla positiva (la que producía comida) mostraba un triángulo blanco sobre un fondo rojo. La tecla negativa mostraba un círculo blanco en un fondo verde. Después de que los animales habían aprendido a responder solo a la tecla positiva, Reynolds presentó los cuatro estímulos por separado: el triángulo solo, el círculo solo, el fondo rojo solo, y el fondo verde solo.

Se encontró que cada paloma respondía solo a uno de los dos estímulos del compuesto positivo. Una paloma respondía preferentemente a la figura (triángulo vs. círculo), ignorando casi completamente el color del fondo. La otra paloma respondía preferentemente al color (rojo vs. verde), ignorando la forma. A pesar de que ambos elementos—forma y color—estaban perfectamente contiguos con la recompensa durante el entrenamiento, solo uno de ellos adquirió control sobre la conducta de cada animal.

La importancia del experimento de Reynolds radica no solo en la demostración de que la contigüidad no es una condición suficiente, sino en la ilustración de un principio que será clave a lo largo de este curso: la *competencia* entre elementos, sean estímulos o respuestas. Los estímulos presentados en forma simultánea dentro de un compuesto compiten entre ellos por la asignación de crédito del organismo. En ese sentido, la asignación del crédito a uno de los estímulos por parte del organismo implica la no asignación de crédito—o la asignación de menos crédito—al otro estímulo presente. A este fenómeno se le denomina *ensombrecimiento* (overshadowing): un elemento saliente del compuesto "ensombrece" el aprendizaje sobre elementos menos salientes.

Retomando nuestro ejemplo del perro amenazante, si el perro los ataca, para algunos de ustedes el predictor del ataque será el gruñido, para otros será el color del pelaje, y para otros será la raza. Los factores que determinan cuál elemento gana la competencia incluyen la saliencia perceptual de los estímulos (intensidad, novedad, contraste) y las predisposiciones evolutivas de relevancia que discutimos anteriormente. Pero la pregunta crucial es: ¿puede la historia previa del organismo con uno de los elementos del compuesto afectar la asignación de crédito? A continuación, veremos un experimento que demuestra que una vez que se ha asignado crédito a un elemento, los organismos dejan de considerar a otros elementos como candidatos, incluso si estos son perfectamente contiguos con el SBI.

### Bloqueo: La Historia Importa

Imaginen que, después de un par de experiencias visitando restaurantes, ustedes aprenden que un mantel de tela es un buen predictor de la calidad de la comida de un lugar. En su siguiente visita a un restaurante nuevo, las mesas tienen manteles de tela, pero adicionalmente el restaurante tiene música clásica de fondo. La calidad de la comida es igualmente buena a la del último restaurante con manteles de tela que visitaron, pero en este caso la comida fue contigua tanto con el mantel de tela como con la música clásica. ¿Habrán aprendido que la música clásica es un predictor de buena comida? Para darle respuesta a esta pregunta, tendrían que observar si, al verse forzados a escoger entre dos restaurantes nuevos sin manteles de tela, seleccionarían aquel que tiene música clásica sobre el que no la tiene. La intuición sugiere que probablemente no. Una vez que el mantel de tela ya predice perfectamente la buena comida, la música clásica es redundante—no añade información nueva.

En 1969, Leon Kamin puso a prueba precisamente esta intuición en lo que se convertiría en uno de los experimentos más influyentes en la historia del estudio del aprendizaje. El diseño experimental, representado en la Figura 8.6, es el siguiente: Kamin trabajó con dos grupos de ratas. Ambos grupos pasaron por una fase de prueba idéntica, pero diferían en su experiencia previa. En la fase crítica (Fase 2), ambos grupos recibieron presentaciones de un compuesto de luz más tono, seguido de una descarga eléctrica. Para el grupo experimental, había una fase anterior (Fase 1) en la cual se presentaba la luz sola seguida de la descarga eléctrica. El grupo control no recibía esta fase preliminar—su primera experiencia con la descarga era en presencia del compuesto luz-tono.

Después del entrenamiento con el compuesto, en la Fase 3 de prueba, se presentaba el tono solo (sin la luz) para evaluar qué tanto habían aprendido las ratas acerca de él. Noten que para ambos grupos, el tono apareció exactamente la misma cantidad de veces contiguo con la descarga eléctrica durante la Fase 2. La única diferencia entre los dos grupos fue la experiencia previa del grupo experimental con la luz y la descarga en la Fase 1.

Los resultados fueron claros y sorprendentes. El grupo control, que no tenía experiencia previa con la luz, mostró un fuerte condicionamiento al tono: cuando se presentaba el tono en la prueba, las ratas mostraban signos evidentes de miedo. En contraste, las ratas del grupo experimental, que habían aprendido previamente que la luz predecía la descarga, no mostraron prácticamente ninguna evidencia de que el tono hubiera adquirido propiedades aversivas. A pesar de que el tono fue igualmente contiguo con la descarga eléctrica en la Fase 2 para ambos grupos, solo el grupo sin experiencia previa aprendió sobre él. Se dice que la experiencia previa con la luz *bloquea* el aprendizaje acerca del tono.

De la misma forma, en nuestro ejemplo de los restaurantes, el mantel de tela bloquea el aprendizaje acerca de la música clásica. Estos experimentos muestran que el grado de aprendizaje acerca de un elemento de un compuesto seguido de un SBI depende crucialmente del grado de aprendizaje adquirido previamente por otros elementos del compuesto. Una forma de interpretar estos resultados es que los elementos compiten por la asignación de crédito no solo en función de su saliencia perceptual, sino también en función de si uno de ellos ya es un predictor establecido del suceso biológicamente importante.

### La Lógica del Bloqueo: Reducción de Incertidumbre

El fenómeno de bloqueo es evidencia contundente de que la contigüidad entre un estímulo y un SBI no es una condición suficiente para el aprendizaje. Pero más allá de esta conclusión negativa, el bloqueo nos revela algo profundo sobre la lógica del sistema de aprendizaje. El sistema no está simplemente registrando co-ocurrencias. Está evaluando si un estímulo proporciona *información nueva* sobre la ocurrencia del SBI. En el experimento de Kamin, una vez que la luz predice perfectamente la descarga, el tono es informacionalmente redundante—su presencia o ausencia no cambia la predictibilidad del SBI. El sistema, por lo tanto, no "desperdicia" recursos aprendiendo sobre él.

Esta interpretación sugiere que el aprendizaje no es sobre contigüidad, sino sobre *predictibilidad* o, equivalentemente, sobre *reducción de incertidumbre*. Un estímulo recibe crédito en la medida en que su presencia reduce la incertidumbre sobre la ocurrencia del SBI. Si el SBI ya es perfectamente predecible (incertidumbre cero), nuevos estímulos contiguos no reciben crédito porque no hay incertidumbre adicional que reducir.

Esta idea—que el aprendizaje se trata de reducir la sorpresa o el error de predicción—se convertirá en el principio central de los modelos formales que estudiaremos en el próximo capítulo. El modelo de Rescorla-Wagner, que formalizó las intuiciones derivadas del experimento de bloqueo, propone precisamente que el aprendizaje es proporcional a la discrepancia entre lo que ocurre y lo que se espera. Si la luz ya predice perfectamente la descarga, no hay discrepancia cuando la descarga ocurre—incluso si un tono está presente—y por lo tanto no hay aprendizaje sobre el tono.

---

## Sistemas de Comportamiento y la Estructura del Espacio de Asignación

Hasta ahora hemos discutido los sesgos de contigüidad, relevancia biológica, y novedad como mecanismos que reducen el espacio de candidatos a asignación de crédito. Pero existe un nivel de organización aún más fundamental que estructura este espacio: los *sistemas de comportamiento*.

Jerry Hogan y John Timberlake desarrollaron una perspectiva influyente que enfatiza que el comportamiento de los organismos no es una colección arbitraria de respuestas inconexas, sino que está organizado en sistemas funcionales pre-estructurados por la evolución. Un *sistema de comportamiento* es un conjunto coordinado de mecanismos perceptuales, motivacionales y motores que evolucionaron para resolver un problema adaptativo específico. Ejemplos incluyen el sistema de alimentación (forrajeo, manipulación, consumo), el sistema de defensa ante depredadores (detección de amenazas, huida, congelamiento), y el sistema reproductivo (cortejo, cópula, cuidado parental).

Crucialmente, la ocurrencia de un SBI no solo activa al organismo de manera general—un estado que Peter Killeen denominó *arousal* o activación. El SBI específico induce el sistema de comportamiento apropiado. La presentación de comida no genera una activación inespecífica; activa específicamente el sistema de alimentación, con todas sus estructuras perceptuales y motoras asociadas. Un depredador activa el sistema de defensa. Esta activación de un sistema de comportamiento tiene una consecuencia profunda para la asignación de crédito: reduce drásticamente el espacio de estímulos que serán considerados como candidatos.

Cuando el sistema de alimentación está activo, los estímulos que son relevantes para la alimentación—sabores, olores de alimento, señales visuales de presa o comida—son procesados preferentemente. Estos estímulos "resuenan" con el sistema activo. Los estímulos irrelevantes para la alimentación—como sonidos ambientales o estímulos táctiles de superficies—son atendidos mucho menos. De esta forma, el sistema de comportamiento funciona como un filtro atencional y asociativo de primer orden, aún más fundamental que los sesgos específicos de relevancia biológica que discutimos anteriormente.

Esta perspectiva da un sustrato biológico y conceptual al sesgo de relevancia. El efecto García—donde el malestar gástrico se asocia a sabores pero no a estímulos audiovisuales—no es simplemente un sesgo arbitrario. Refleja el hecho de que el malestar gástrico activa el sistema de alimentación, y dentro de ese sistema, los sabores son las señales causalmente relevantes. Para especies omnívoras que evolucionaron en entornos donde la toxicidad de alimentos se señaliza por sabor, este sesgo de relevancia está "cableado" en la arquitectura del sistema de alimentación.

En la terminología del aprendizaje automático contemporáneo, podemos pensar en los sistemas de comportamiento como *priors* o conocimiento previo estructurado que sesga el aprendizaje. No empezamos desde cero, asignando probabilidades iguales a todos los estímulos del universo. Empezamos con un espacio de hipótesis pre-estructurado, donde ciertas dimensiones de estimulación son *a priori* más probables de ser relevantes, dado el tipo de SBI que ocurrió.

---

## Conclusiones: Navegando el Espacio de Posibilidades

Hemos visto que el problema de la asignación de crédito a estímulos es computacionalmente intratable sin mecanismos de filtrado. La selección natural no resolvió este problema con un único principio universal, sino con una cascada de sesgos que operan en diferentes niveles:

1. **Activación y Sistemas de Comportamiento:** El primer filtro. El tipo de SBI activa un sistema de comportamiento específico, que determina qué dimensiones de estimulación son relevantes. Esto reduce el espacio de trillones de estímulos posibles a un subconjunto manejable relacionado con la función adaptativa del sistema.

2. **Relevancia Biológica:** Dentro del sistema activo, ciertos estímulos tienen mayor probabilidad de ser causalmente relevantes, basándose en la historia evolutiva de la especie y su nicho ecológico.

3. **Contigüidad Temporal:** Los estímulos cercanos en el tiempo al SBI son candidatos más probables que los distantes. Este sesgo es gradual, no absoluto.

4. **Novedad:** Los estímulos nuevos son priorizados sobre los familiares, porque es más probable que un estímulo nuevo sea la causa de un evento nuevo.

5. **Saliencia Perceptual:** Los estímulos intensos y contrastantes capturan más atención y, por lo tanto, compiten mejor en situaciones de ensombrecimiento.

6. **Competencia e Informatividad:** Cuando múltiples estímulos son igualmente contiguos, compiten entre sí. El aprendizaje no es sobre contigüidad per se, sino sobre reducción de incertidumbre. Los estímulos que ya predicen perfectamente el SBI bloquean el aprendizaje sobre estímulos redundantes.

Estos sesgos no son "limitaciones" del aprendizaje, sino soluciones evolutivas a un problema computacional real. En ciencia de la computación, esto se reconoce formalmente: sin restricciones (sesgos inductivos), el aprendizaje de cualquier estructura es imposible. Los organismos enfrentan el mismo dilema, y la evolución lo resolvió construyendo arquitecturas cognitivas con sesgos específicos.

La evidencia empírica que hemos revisado—los estudios de García sobre aversiones a sabores, el ensombrecimiento de Reynolds, y especialmente el bloqueo de Kamin—demuestra que estos sesgos existen y que su lógica no es la de la simple contigüidad. El sistema de aprendizaje es un detector de información, un mecanismo para identificar señales que reducen incertidumbre. Esta conclusión nos prepara para el próximo capítulo, donde estudiaremos modelos formales que capturan matemáticamente esta lógica de reducción de error de predicción. El modelo de Rescorla-Wagner, que discutiremos en detalle en el Capítulo 9, formaliza precisamente la idea de que el aprendizaje es proporcional a la sorpresa—a la discrepancia entre lo que ocurre y lo que se espera. Este principio de reducción de error de predicción se convertirá en el motor conceptual de prácticamente todos los modelos modernos de aprendizaje, desde la neurociencia computacional hasta el aprendizaje por refuerzo en inteligencia artificial.

---

## Conceptos Clave y Síntesis

Este capítulo ha desarrollado una argumentación progresiva sobre la naturaleza del aprendizaje asociativo. Comenzamos con el reconocimiento de que el problema de la asignación de crédito es fundamentalmente intratable: dado un suceso biológicamente importante, el espacio de posibles causas se extiende infinitamente hacia el pasado. Sin mecanismos de filtrado, un organismo no podría distinguir señales predictivas genuinas de correlaciones espurias.

La solución evolutiva a este problema no fue un principio único y universal, sino una cascada de sesgos inductivos que operan en diferentes niveles de especificidad. El sesgo más fundamental es la activación de sistemas de comportamiento específicos. Cuando ocurre un SBI particular—comida, dolor, amenaza—no genera una activación inespecífica, sino que induce un sistema funcional pre-estructurado con sus propios mecanismos perceptuales y motores. Esto reduce drásticamente el espacio inicial de candidatos a solo aquellos estímulos relevantes para el sistema activo. Este es el insight de Hogan, Timberlake y Killeen.

Dentro del sistema activo operan sesgos más específicos. La relevancia biológica, demostrada dramáticamente por García, establece que ciertas dimensiones de estimulación son *a priori* más probables de ser causales dependiendo del tipo de SBI. El malestar gástrico dirige la atención hacia sabores, no hacia estímulos audiovisuales; el dolor externo hace lo opuesto. Este no es un sesgo arbitrario sino el reflejo de regularidades causales en el ambiente ancestral de cada especie. La contigüidad temporal funciona como un sesgo adicional: los eventos cercanos en el tiempo son candidatos más probables. Sin embargo, García demostró que este sesgo no es una condición necesaria—se puede aprender con demoras de horas cuando la relevancia biológica es alta. La novedad prioriza estímulos nuevos sobre familiares, reduciendo falsas alarmas sobre causas improbables.

Pero el hallazgo más profundo vino de los experimentos de Kamin sobre el bloqueo. Estos demostraron que la contigüidad tampoco es una condición suficiente. Dos estímulos pueden ser igualmente contiguos con un SBI, pero solo aquel que reduce incertidumbre adicional recibirá crédito. Si un estímulo ya predice perfectamente el resultado, estímulos adicionales contiguos son informacionalmente redundantes y no se aprende sobre ellos. Este resultado revela que el aprendizaje no es sobre contigüidad per se, sino sobre predictibilidad—sobre reducción de error de predicción.

El fenómeno de bloqueo nos obliga a reconocer que los estímulos no se procesan independientemente. Compiten entre sí por asignación de crédito. Esta competencia se observa también en el ensombrecimiento, donde elementos más salientes de un compuesto capturan más crédito que elementos menos salientes. La implicación es que el aprendizaje es un proceso activo de inferencia causal, no un registro pasivo de co-ocurrencias.

Estas conclusiones empíricas demandaron una nueva clase de teoría. El modelo de Rescorla-Wagner, que estudiaremos en el próximo capítulo, formalizó matemáticamente la idea de que el aprendizaje es proporcional a la sorpresa—a la discrepancia entre lo que ocurre y lo que se espera. Este principio de reducción de error de predicción se ha convertido en el motor conceptual no solo de teorías del aprendizaje asociativo, sino de modelos de aprendizaje por refuerzo en inteligencia artificial, teorías de codificación neural de dopamina, y modelos bayesianos de cognición. La idea de que el cerebro es fundamentalmente una máquina predictiva, constantemente minimizando error de predicción, tiene sus raíces en los experimentos que hemos revisado en este capítulo.

Los conceptos centrales que debemos retener son: primero, que los sesgos inductivos no son limitaciones irracionales sino soluciones evolutivas a un problema computacional real. Segundo, que estos sesgos operan jerárquicamente—desde la activación de sistemas de comportamiento hasta la competencia entre elementos específicos. Tercero, que la lógica del aprendizaje no es sobre asociación por contigüidad, sino sobre inferencia de estructura causal a través de la detección de qué reduce incertidumbre. Y finalmente, que entender estos principios en términos computacionales—como problemas de búsqueda en espacios de hipótesis, filtrado de información, y reducción de error—nos permite conectar el estudio clásico del aprendizaje animal con desarrollos contemporáneos en neurociencia computacional, inteligencia artificial, y teoría de la decisión.

---

## Lecturas Recomendadas

**Textos Clásicos:**

- Pavlov, I. P. (1927). *Conditioned Reflexes: An Investigation of the Physiological Activity of the Cerebral Cortex*. Oxford University Press. [Traducción del ruso al inglés del trabajo fundamental que estableció el paradigma del condicionamiento clásico]

- García, J., & Koelling, R. A. (1966). "Relation of cue to consequence in avoidance learning." *Psychonomic Science*, 4(3), 123-124. [El experimento que demostró la existencia de sesgos de relevancia biológica]

- Kamin, L. J. (1969). "Predictability, surprise, attention, and conditioning." In B. A. Campbell & R. M. Church (Eds.), *Punishment and Aversive Behavior* (pp. 279-296). Appleton-Century-Crofts. [El artículo que introdujo el fenómeno de bloqueo y cambió nuestra comprensión del aprendizaje asociativo]

**Revisiones Modernas:**

- Pearce, J. M., & Bouton, M. E. (2001). "Theories of associative learning in animals." *Annual Review of Psychology*, 52(1), 111-139. [Revisión comprehensiva de teorías contemporáneas del aprendizaje asociativo]

- Miller, R. R., & Matzel, L. D. (1988). "The comparator hypothesis: A response rule for the expression of associations." In G. H. Bower (Ed.), *The Psychology of Learning and Motivation* (Vol. 22, pp. 51-92). Academic Press. [Perspectiva alternativa al modelo de Rescorla-Wagner]

- Gallistel, C. R., & Gibbon, J. (2000). "Time, rate, and conditioning." *Psychological Review*, 107(2), 289-344. [Análisis del papel del tiempo en el aprendizaje asociativo]

**Perspectiva Evolutiva y de Sistemas de Comportamiento:**

- Domjan, M. (2005). "Pavlovian conditioning: A functional perspective." *Annual Review of Psychology*, 56, 179-206. [Excelente revisión de cómo los principios de aprendizaje reflejan soluciones evolutivas]

- Shettleworth, S. J. (2010). *Cognition, Evolution, and Behavior* (2nd ed.). Oxford University Press. [Texto comprehensivo que integra aprendizaje, cognición y evolución]

- Timberlake, W., & Lucas, G. A. (1989). "Behavior systems and learning: From misbehavior to general principles." In S. B. Klein & R. R. Mowrer (Eds.), *Contemporary Learning Theories: Instrumental Conditioning Theory and the Impact of Biological Constraints on Learning* (pp. 237-275). Erlbaum. [Presentación detallada de la teoría de sistemas de comportamiento]

- Hogan, J. A. (2001). "Development of behavior systems." In E. M. Blass (Ed.), *Handbook of Behavioral Neurobiology: Volume 13, Developmental Psychobiology, Developmental Neurobiology, and Behavioral Ecology* (pp. 229-279). Kluwer Academic/Plenum Publishers.

**Conexiones con Neurociencia y Aprendizaje Automático:**

- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. [Capítulos iniciales discuten el papel de sesgos inductivos y error de predicción en sistemas artificiales]

- Dayan, P., & Daw, N. D. (2008). "Decision theory, reinforcement learning, and the brain." *Cognitive, Affective, & Behavioral Neuroscience*, 8(4), 429-453. [Conexión entre aprendizaje asociativo y aprendizaje por refuerzo en neurociencia]

---

## Ejercicios y Problemas

### Ejercicios Conceptuales

**1. Análisis del Problema Computacional**

Considere el siguiente escenario: un ratón de laboratorio explora un nuevo ambiente durante 10 minutos antes de encontrar comida en un rincón específico. Durante esos 10 minutos, el ratón experimentó aproximadamente 600 segundos × 1000 estímulos por segundo (visuales, olfativos, táctiles, auditivos, propioceptivos) = 600,000 eventos discretos.

a) Si el ratón tuviera que considerar cada uno de estos eventos como un posible predictor de la comida, ¿cuántas hipótesis causales tendría que evaluar? (Considere que cada evento podría ser causa, o no ser causa—una decisión binaria para cada uno).

b) Explique cómo cada uno de los siguientes sesgos reduce este espacio de búsqueda:
   - Sistema de comportamiento de alimentación activo
   - Contigüidad temporal (ventana de 30 segundos antes de encontrar comida)
   - Relevancia biológica (solo estímulos olfativos y visuales)
   - Novedad (solo elementos nuevos del ambiente, no el fondo familiar)

c) Después de aplicar todos estos filtros, ¿cuántos candidatos realistas quedarían? Justifique su estimación.

**2. Relevancia Biológica y Nicho Ecológico**

Las serpientes que cazan utilizando órganos termorreceptores (detectan calor infrarrojo) pueden localizar presas endotérmicas en completa oscuridad. Si una serpiente de este tipo ingiere una presa tóxica y desarrolla malestar gástrico horas después:

a) ¿Qué dimensión sensorial predice que será más probable que la serpiente asocie con la toxicidad: temperatura de la presa, estímulos visuales, o estímulos químicos (olfato/gusto)? Justifique su respuesta considerando el nicho ecológico de la serpiente.

b) Compare su predicción con el efecto García en ratas. ¿Por qué especies diferentes desarrollan sesgos de relevancia diferentes?

c) Diseñe un experimento para probar su hipótesis sobre los sesgos de relevancia de la serpiente.

**3. Bloqueo en Contexto Humano**

María visita frecuentemente un café donde siempre tocan música jazz y sirven café en tazas azules. Ella consistentemente disfruta su experiencia (el café es excelente). Luego visita un café nuevo que también toca jazz, pero usa tazas rojas. El café es igualmente excelente.

a) Según el fenómeno de bloqueo, ¿es probable que María haya aprendido que las tazas rojas predicen buen café? ¿Por qué sí o por qué no?

b) Si quisiéramos probar si María aprendió algo sobre las tazas rojas, ¿qué situación de prueba tendríamos que crear?

c) ¿Qué factor (jazz o tazas azules) es más probable que María asocie inicialmente con el buen café en el primer café? ¿Por qué? (Considere sesgos de saliencia y relevancia).

**4. Sistemas de Comportamiento y Asignación de Crédito**

Un gato doméstico tiene hambre y su dueño abre una lata de comida. La apertura de la lata produce: (a) un sonido metálico característico, (b) un olor a pescado, (c) movimiento del dueño hacia el área de alimentación, y (d) la presentación de la comida en un plato azul.

a) ¿Cuál de estos estímulos es más probable que el gato asocie con la alimentación inminente? Justifique su respuesta considerando: (i) relevancia biológica para carnívoros, (ii) saliencia perceptual, y (iii) contigüidad temporal.

b) Con entrenamiento repetido, ¿en qué orden temporal predice que el gato comenzará a mostrar comportamiento anticipatorio (salivar, acercarse) en respuesta a cada uno de estos estímulos?

c) Después de muchas experiencias, el dueño cambia a comida en bolsa (mismo olor, sin sonido de lata metálica). ¿Qué estímulo predice que ahora controlará el comportamiento anticipatorio del gato? Explique usando los conceptos de bloqueo y competencia entre elementos.

### Ejercicios Cuantitativos

**5. Gradiente de Demora**

Suponga que la fuerza del condicionamiento (V) decrece exponencialmente con la demora (d) entre el EC y el EI según la función:

$$V = V_{max} \cdot e^{-\lambda d}$$

donde $V_{max}$ es la fuerza máxima de condicionamiento con demora cero, $\lambda$ es la tasa de decaimiento, y d es la demora en segundos.

Para un sistema de condicionamiento del miedo con $V_{max} = 1.0$ y $\lambda = 0.2$:

a) Calcule V para demoras de: 0 seg, 1 seg, 5 seg, 10 seg, 20 seg.

b) ¿A qué demora V cae al 50% de su valor máximo? (Resuelva para d cuando V = 0.5).

c) Grafique V vs. d para el rango 0-30 segundos.

d) Ahora considere el sistema de aversión a sabores estudiado por García, donde se observa aprendizaje con demoras de hasta 12 horas (43,200 segundos). Si $V_{max}$ es igual, ¿qué valor de $\lambda$ sería necesario para que V = 0.3 con d = 43,200 seg? ¿Cómo se compara este $\lambda$ con el del sistema de miedo?

**6. Competencia en Ensombrecimiento**

En un compuesto AB seguido de refuerzo, suponga que el crédito total disponible es 1.0 y se distribuye proporcionalmente a la saliencia perceptual de cada elemento.

Elemento A tiene saliencia $s_A = 0.7$
Elemento B tiene saliencia $s_B = 0.3$

a) Calcule cuánto crédito recibe cada elemento: $Crédito_A = \frac{s_A}{s_A + s_B}$

b) Si incrementamos la intensidad de A de tal forma que $s_A = 0.9$ (manteniendo $s_B = 0.3$), recalcule la distribución de crédito.

c) ¿En cuánto disminuyó el crédito recibido por B al aumentar la saliencia de A? Esto es una cuantificación del ensombrecimiento.

d) ¿Qué pasaría si ambos elementos tuvieran saliencia idéntica ($s_A = s_B = 0.5$)?

### Ejercicios Aplicados

**7. Aversiones Condicionadas en Quimioterapia**

Muchos pacientes de quimioterapia desarrollan aversiones a alimentos consumidos antes del tratamiento, incluso sabiendo conscientemente que la comida no causó la náusea.

a) Use los conceptos de este capítulo (relevancia biológica, contigüidad, sistema de comportamiento) para explicar por qué se desarrollan estas aversiones a pesar del conocimiento consciente.

b) La náusea inducida por quimioterapia ocurre típicamente 2-6 horas después de la infusión. Dado el gradiente de demora para aversiones a sabores, ¿qué alimento es más probable que adquiera la aversión: uno consumido 12 horas antes de la quimio, uno consumido 2 horas antes, o uno consumido inmediatamente antes? Justifique.

c) Proponga una intervención conductual basada en los principios de bloqueo para minimizar el desarrollo de aversiones a alimentos nutritivos importantes. (Pista: considere presentar un "sabor señuelo" justo antes del tratamiento).

**8. Diseño Experimental: Evaluando Sistemas de Comportamiento**

Diseñe un experimento para demostrar que la activación de diferentes sistemas de comportamiento determina qué estímulos entran en el espacio de asignación de crédito.

**Sujetos:** Ratas de laboratorio

**SBIs disponibles:** (a) Comida, (b) Descarga eléctrica leve en las patas

**ECs disponibles:** (i) Sabor de sacarina en agua, (ii) Luz estroboscópica, (iii) Textura del piso (suave vs. rugoso)

Especifique:
- Diseño de grupos experimentales y control
- Procedimiento de entrenamiento para cada grupo (qué ECs se aparean con qué SBIs)
- Procedimiento de prueba (qué medirá y cómo)
- Predicciones basadas en la teoría de sistemas de comportamiento
- ¿Qué patrón de resultados confirmaría que diferentes SBIs activan sistemas de comportamiento diferentes que filtran estímulos distintos?

**9. Evolución de Sesgos de Relevancia**

Considere una población de roedores omnívoros que vive en un ambiente donde:
- 30% de plantas comestibles son tóxicas (producen malestar gástrico)
- Las plantas tóxicas tienen sabores distintivos pero apariencia visual similar a las no tóxicas
- Los depredadores atacan basándose en movimiento y sonido, no en rasgos visuales de la presa

a) ¿Qué sesgos de relevancia biológica esperaría que evolucionen en esta población? Justifique por qué estos sesgos son adaptativos.

b) Ahora considere una mutación que produce roedores con un sesgo "invertido": asocian estímulos visuales con malestar gástrico y sabores con ataques de depredadores. ¿Qué problemas de supervivencia enfrentarían estos mutantes?

c) Calcule la frecuencia de encuentros con alimentos tóxicos vs. encuentros con depredadores necesaria para que el sesgo "invertido" fuera adaptativo. ¿Es este escenario ecológicamente plausible?

**10. Análisis Crítico: Límites del Bloqueo**

El bloqueo demuestra que la contigüidad no es suficiente. Sin embargo, existen condiciones donde el bloqueo no ocurre o es incompleto.

a) Investigue el fenómeno de "desbloqueo" (unblocking): si en la Fase 2 del experimento de Kamin la descarga es más intensa que en la Fase 1, el tono bloqueado sí adquiere algo de condicionamiento. ¿Por qué cree que ocurre esto? (Pista: piense en términos de error de predicción).

b) El bloqueo es más débil cuando hay una demora larga entre la Fase 1 y la Fase 2. Proponga una explicación basada en procesos de memoria.

c) Diseñe un experimento para determinar si el bloqueo refleja un fracaso en aprender sobre el estímulo bloqueado, o si el aprendizaje ocurre pero el estímulo bloqueado no controla la conducta debido a competencia en la expresión de lo aprendido. (Esto requiere distinguir entre adquisición y ejecución).

---

**Fin del Capítulo 8**
