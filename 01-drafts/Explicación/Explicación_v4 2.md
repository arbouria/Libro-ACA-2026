# # Capitulo 3: Modelos y Explicación

## Borrador

Cuando los científicos son tomados desprevenidos y se les pregunta cuál es el propósito de su actividad, la mayoría dirá que es "explicar" un fenómeno. Pero cuando se les pregunta qué entienden por explicar, las respuestas divergen —a veces radicalmente. En psicología esto es especialmente visible: hay investigadores que consideran que describir con precisión una relación funcional entre variables ya constituye una explicación completa, y otros que solo aceptan como explicación la identificación del mecanismo neuronal que produce el comportamiento. Con frecuencia, ambos grupos hablan de los mismos datos experimentales.

Este capítulo propone que buena parte de esa divergencia no refleja desacuerdos sobre los hechos, sino preguntas diferentes que se responden con herramientas diferentes. Entender qué tipos de preguntas existen —y qué tipo de estructura necesita una respuesta para cada una— es uno de los recursos intelectuales más útiles que puedes llevar a la lectura de la literatura científica. Para desarrollarlo necesitamos entender primero qué son los modelos y después qué significa explicar.

---

## La Visión Ortodoxa y Sus Límites

Los psicólogos del segundo tercio del siglo XX compartían con los filósofos de su época una imagen de la teoría científica como un conjunto de leyes generales, de las cuales se podían derivar —por deducción— fenómenos individuales o patrones entre ellos. Las leyes relacionaban términos teóricos no directamente observables (como "pulsión" o "hábito") con variables medibles, mediante reglas de correspondencia que anclaban lo abstracto a lo empírico. El objetivo declarado era construir sistemas hipotético-deductivos tan completos como los que la física había desarrollado para el movimiento de los planetas o para los gases.

En este esquema, *explicar* un fenómeno significaba derivarlo lógicamente de las leyes. Si observamos que un animal corre más rápido en cierta condición, la explicación consiste en mostrar que esa velocidad se sigue de los valores de las variables teóricas postuladas por la teoría. Esta visión de la explicación —derivación lógica de un fenómeno a partir de leyes generales— es lo que Carl Hempel llamó el modelo nomológico-deductivo (ND).

El modelo ND tenía una virtud: era explícito y formalizable. Pero enfrentó un problema que resultó fatal.

### El Problema de la Asimetría

Supongamos que llegamos tarde al trabajo una mañana porque el tráfico estaba congestionado. La explicación parece perfectamente razonable: el tráfico causó el retraso. Ahora nota que con la misma estructura lógica podríamos "derivar" el estado del tráfico a partir del retraso: si sabemos cuánto tarde normalmente y cuánto tardé esta mañana, puedo calcular el estado probable del tráfico. Sin embargo, intuitivamente algo está mal. El retraso no explica el tráfico; la relación va en una sola dirección.

Este problema, conocido como el problema de la asimetría, fue identificado por el propio Hempel. La explicación tiene una *dirección* que la relación lógica por sí sola no captura. Esa dirección tiene que ver con la causalidad: el tráfico causó el retraso, y no al revés. El modelo ND no distingue las dos direcciones porque es indiferente a la causalidad: desde su perspectiva, la deducción funciona en ambos sentidos.

Esta falla obligó a los filósofos a reconocer que la causalidad debe desempeñar un papel central en la explicación. Pero incorporarla adecuadamente requirió, primero, repensar qué es una teoría científica, lo que condujo al surgimiento de la noción de modelo como unidad básica de la práctica científica.

---

## De Teorías a Modelos

En la práctica real, los científicos de la segunda mitad del siglo XX dejaron paulatinamente de buscar leyes universales y comenzaron a construir modelos: el modelo de la doble hélice del ADN, los modelos de dinámica poblacional, los modelos epidemiológicos de una infección, los modelos de oferta y demanda en economía. En los capítulos que siguen encontraremos modelos del aprendizaje asociativo, de la asignación del comportamiento a distintas alternativas, y del aprendizaje por refuerzo. Todos comparten una característica: son representaciones simplificadas de alguna parte del mundo que permiten entender, predecir o intervenir sobre ella.

¿Qué es exactamente un modelo? Una manera útil de pensarlo: un modelo es una estructura —matemática, computacional, o diagramática— que representa un fenómeno mediante una relación de semejanza estructural con él. Un mapa del metro es un modelo: no reproduce cada detalle de los vagones ni la arquitectura de las estaciones, pero preserva las relaciones relevantes —qué líneas conectan qué estaciones— de forma que permite al viajero navegar el sistema. Un modelo de clima no es el clima; es una estructura que captura las interacciones dinámicas entre variables atmosféricas de forma que permite hacer predicciones útiles.

Podemos tener distintos modelos del mismo fenómeno para distintos propósitos. Un mapa que muestra solo las líneas y los puntos de transferencia es útil para llegar de un punto a otro; un mapa con información turística sobrepuesta es útil para quien visita por primera vez una ciudad. Ninguno es "el correcto" en abstracto; cada uno es correcto para su propósito. Lo mismo ocurre con los modelos en psicología: no hay un único modelo del aprendizaje que sea definitivo, sino modelos que responden preguntas distintas con distintos niveles de resolución.

### Los Modelos como Vehículos de Inferencia

Hay una discusión importante sobre cuál es exactamente la relación entre un modelo y el fenómeno que representa. Una respuesta influyente (Suppes, van Fraassen) es que esa relación es de *isomorfismo estructural*: el modelo representa exitosamente un fenómeno cuando existe una correspondencia que preserva las relaciones relevantes entre la estructura del modelo y la estructura del fenómeno empírico. Consideremos la medición de la estatura: queremos asignar números a personas de forma que se preserve la relación "más alto que". Si A es más alta que B, el número asignado a A debe ser mayor. La medición es exitosa cuando existe ese isomorfismo entre la estructura empírica ⟨Personas, más-alta-que⟩ y la estructura numérica ⟨Números, >⟩.

Esta cuenta del isomorfismo tiene méritos: hace preciso qué se requiere del modelo y guía la investigación hacia la pregunta de si la estructura empírica satisface los axiomas del modelo. En capítulos posteriores veremos que medir preferencias es problemático precisamente porque las preferencias humanas a veces violan la transitividad —una condición que el isomorfismo con los números requeriría.

Pero para este libro, una concepción más amplia resulta más útil: la visión *inferencialista* de Mauricio Suárez. Para Suárez, lo que hace que una estructura sea un modelo de un fenómeno no es que sean isomórficas, sino que el modelo *permite al usuario hacer inferencias sobre el fenómeno* en el contexto adecuado. No se requiere semejanza estructural precisa; se requiere que el modelo funcione como vehículo inferencial. Un modelo de optimización del forrajeo no es isomórfico al comportamiento de un animal buscando alimento, pero permite inferir qué patrones de búsqueda deberíamos observar si el animal está bien adaptado. Un algoritmo de aprendizaje por refuerzo no replica la fisiología neuronal, pero permite inferir cómo cambiará la conducta ante diferentes distribuciones de recompensa.

Esta concepción es más cercana a cómo los científicos usan sus modelos en la práctica, y más apropiada para un libro que incorpora modelos de optimización, algoritmos computacionales y simuladores interactivos. La pregunta que debemos hacerle a un modelo no es "¿es isomórfico al fenómeno?" sino "¿qué inferencias permite hacer, y son esas inferencias empíricamente productivas?"

---

## La Pluralidad de Formas de Explicar

Con la noción de modelo en mano, podemos volver al problema de la explicación. Veremos que no hay un único tipo de explicación científica válida; hay varios tipos, cada uno apropiado para un tipo de pregunta.

### Explicación Causal

La respuesta más directa al problema de la asimetría incorpora la causalidad explícitamente. Una manera contemporánea de entenderla es en términos *contrafactuales*: A causa B si, de no haber ocurrido A, B tampoco hubiera ocurrido, manteniendo todo lo demás constante. ¿Por qué el perro de Pavlov salivaba ante el sonido de la campana? Porque la campana precedía a la comida. ¿Cómo lo sabemos? Porque disponemos de un grupo control en el que campana y comida no estaban relacionadas, y en ese grupo el perro no saliva. Hemos construido artificialmente la situación contrafactual y verificado que el resultado también desaparece.

Una variante complementaria, desarrollada por James Woodward, es la interpretación *intervencionista*: A causa B si una intervención sobre A produce un cambio en B. Esta formulación captura por qué nos interesan las relaciones causales: porque queremos intervenir. En las ciencias del comportamiento, esta lógica está ejemplificada en el trabajo de Skinner: al manipular sistemáticamente los programas de reforzamiento y registrar los cambios en los patrones de respuesta, Skinner construyó un catálogo de relaciones causales funcionales de notable robustez. En el capítulo sobre programas de reforzamiento veremos concretamente cómo el tipo de relación entre respuesta y refuerzo determina patrones de conducta muy distintos. Identificar esas relaciones funcionales es ya una explicación completa en su nivel.

Un refinamiento importante viene de Michael Strevens. Para cualquier evento de interés, hay una multitud de factores causalmente relevantes pero no igualmente *explicativos*. Considera ¿por qué una paloma pica más una tecla después de que esa respuesta fue seguida de acceso a comida? La historia causal completa incluye: las dimensiones de la cámara, el color de la tecla, la composición exacta del alimento, la temperatura del día. Omitiendo sistemáticamente lo que no hace diferencia —cambiando la respuesta, el organismo, el reforzador, manteniendo la relación consecuente— encontramos el *hacedor de diferencia* máximamente informativo: que una consecuencia apetitiva siguió a la respuesta. Este patrón abstracto es la ley del efecto. Es una idealización —no especifica organismos, respuestas ni reforzadores particulares— pero es una buena explicación precisamente porque incluye lo que importa y omite lo que no.

### Explicación por Unificación

Philip Kitcher propuso un tipo de explicación que no requiere identificar causas específicas: las teorías explican al mostrar que fenómenos heterogéneos comparten una estructura subyacente común. La ciencia no solo busca causas; busca demostrar que lo que parece diverso es en realidad el resultado de unos pocos principios fundamentales.

El ejemplo paradigmático de este libro es la teoría de la selección natural, que examinaremos en el capítulo siguiente. La selección natural explica una diversidad asombrosa —diferencias en morfología, comportamiento, fisiología, demografía— mostrando que todos son el resultado del mismo proceso. Un corolario elegante ilustra bien la lógica: ¿por qué la mayoría de las especies de reproducción sexual tienen aproximadamente la misma proporción de machos y hembras? Ronald Fisher mostró que cualquier desviación de esa proporción produce una ventaja selectiva para los individuos que generan el sexo menos frecuente, empujando sistemáticamente la población hacia el equilibrio 1:1. El argumento no especifica los mecanismos de determinación de sexo de ninguna especie —los ignora deliberadamente. Su poder explicativo proviene de mostrar por qué ese patrón emerge en sistemas con mecanismos causales muy distintos: porque todos están sujetos a la misma dinámica.

A lo largo de este libro veremos que el principio del reforzamiento unifica de manera similar una gran diversidad de comportamientos en múltiples especies e incluso en agentes no biológicos. No necesitamos una teoría diferente para el desarrollo del lenguaje, la adicción y el forrajeo; un conjunto de principios los abarca a todos.

### Explicación Mecanicista

A comienzos del siglo XXI, un grupo de filósofos que incluye a Carl Craver y William Bechtel articuló lo que se conoce como el *nuevo mecanicismo*. La idea central: un mecanismo para un fenómeno consiste de entidades cuyas actividades e interacciones están organizadas de forma que producen ese fenómeno. Las entidades son los componentes; las actividades son lo que hacen; la organización es la estructura espacial y temporal de sus interacciones; y el fenómeno es el resultado de nivel superior que queremos explicar.

Skinner criticó lo que llamó el "sistema nervioso conceptual": la tendencia de postular procesos internos sin evidencia independiente de su existencia. Su objeción era válida como crítica a una forma de "explicar" que solo renombra el comportamiento con jerga mecanicista. El nuevo mecanicismo la toma en serio: un mecanismo genuino requiere componentes reales, identificables de manera independiente al fenómeno que explican. La distinción entre mecanismo genuino y redescripción circular es empírica, no filosófica. Cuando en los capítulos de Semestre II veamos que las neuronas dopaminérgicas del mesencéfalo codifican señales de error de predicción de recompensa —el mismo tipo de señal que aparece en los modelos de diferencias temporales— estaremos viendo una explicación mecanicista genuina: un componente identificable independientemente que implementa un proceso descrito a nivel algorítmico.

---

## Niveles de Análisis

Hemos visto que existen múltiples tipos de explicación legítima, cada uno apropiado para un tipo de pregunta. ¿Cómo organizar esa pluralidad? La respuesta que ha emergido desde varias disciplinas es pensar en términos de *niveles de análisis*: fenómenos complejos pueden analizarse en distintos niveles, cada uno con sus propios conceptos, métodos y tipos de explicación apropiados. Tres marcos organizan esos niveles de maneras complementarias (ver Figura 1.1).

### Las Cuatro Preguntas de Tinbergen

El etólogo Nikolaas Tinbergen argumentó que el estudio del comportamiento debe abordar cuatro tipos de preguntas genuinamente distintas. La distinción central es entre *causas próximas* —cómo funciona el comportamiento aquí y ahora— y *causas últimas* —por qué evolucionó. Dentro de cada categoría, distinguió dos tipos:

En las causas próximas: la pregunta del *mecanismo* (¿qué procesos fisiológicos y psicológicos producen el comportamiento?) y la pregunta del *desarrollo* (¿cómo se forma ese comportamiento a lo largo de la vida del individuo?). En las causas últimas: la pregunta de la *función* (¿cuál es el valor adaptativo del comportamiento?) y la pregunta de la *evolución* (¿cómo llegó ese comportamiento a existir en la historia de la especie?).

Consideremos un ejemplo que aparecerá en los próximos capítulos: las bacterias se mueven hacia concentraciones más altas de nutrientes. La pregunta del mecanismo se responde describiendo los receptores de quimiotaxis y los flagelos que cambian su sentido de rotación. La pregunta del desarrollo, en este caso, se responde describiendo la expresión genética durante el ciclo de vida de la bacteria. La pregunta funcional se responde mostrando que este comportamiento incrementa la probabilidad de sobrevivencia en entornos con distribución heterogénea de recursos. La pregunta evolutiva se responde trazando cómo la selección natural favorecería organismos con esta capacidad en ancestros primitivos. Estas cuatro respuestas no compiten; cada una es completa en su nivel.

El error que Tinbergen quería prevenir es tratar estas cuatro preguntas como si fueran la misma. Decir que las bacterias se mueven hacia los nutrientes "para sobrevivir" (función) no dice nada sobre el mecanismo molecular que produce el movimiento. Describir los receptores de quimiotaxis (mecanismo) no explica por qué ese mecanismo evolucionó. Confundir los niveles genera debates estériles: los investigadores no están en desacuerdo sobre los hechos, sino hablando sobre preguntas diferentes.

### El Marco de Killeen

Peter Killeen propone un vocabulario derivado de la distinción aristotélica entre tipos de causas, adaptado para las ciencias del comportamiento: *subyace* (¿qué sustrato físico lo soporta?), *induce* (¿qué variables lo producen?), *logra* (¿qué función adaptativa cumple?), y *representa* (¿qué estructura formal lo describe?). Este vocabulario es el que encontrarás en el programa oficial del curso y en parte de la literatura. Su equivalencia aproximada con los marcos de Tinbergen y Marr está indicada en la Figura 1.1: *subyace* corresponde al nivel de implementación, *induce* al nivel algorítmico y mecanismo próximo, *logra* a la función adaptativa, y *representa* al nivel computacional.

### Los Tres Niveles de Marr

Imagina que una expedición de científicos extraterrestres aterriza en la Tierra y encuentra un automóvil abandonado. Fascinados, deciden investigar cómo funciona.

El primer científico, un químico-físico, desarma el vehículo pieza por pieza. Estudia la aleación de los metales, la composición del caucho de las llantas y la química de la combustión de la gasolina. Al terminar, afirma haber "explicado" el automóvil. El segundo científico, un ingeniero, lo interrumpe: "Conocer el metal no basta. Lo importante es cómo interactúan las piezas". Él dibuja un diagrama de flujo que muestra cómo la bujía enciende la gasolina, empuja el pistón y hace girar el eje.

El tercer científico los observa y dice: "Ambos tienen razón en su nivel, pero se están perdiendo lo fundamental. No han entendido que esta máquina es una solución a un problema de desplazamiento espacial. Si no entienden que el objetivo de todo esto es llevar carga de un punto A a un punto B de la manera más eficiente posible, nunca entenderán por qué tiene ruedas en lugar de patas".

David Marr propuso un marco para entender los sistemas cognitivos que refleja exactamente esta división del trabajo. Argumentó que para entender completamente un sistema que procesa información (sea un cerebro, una bacteria o un algoritmo), debemos analizarlo en tres niveles distintos y complementarios:

El nivel *computacional* pregunta qué computa el sistema y por qué —define el problema en términos abstractos sin comprometerse con cómo se resuelve. El nivel *algorítmico* pregunta cómo lo computa —especifica los procedimientos y representaciones mediante los cuales el sistema realiza esa computación. El nivel de *implementación* pregunta en qué sustrato físico ocurre esa computación.

Marr enfatizó que cada nivel es parcialmente autónomo—puede ser estudiado independientemente de los otros niveles. Pero también están interrelacionados—restricciones en un nivel afectan los otros niveles. Podemos entender el problema computacional sin saber el algoritmo o la implementación.  Del mismo modo, podemos estudiar algoritmos abstractamente sin saber su implementación neural específica. Sin embargo, el análisis computacional restringe los algoritmos apropiados. No cualquier algoritmo resolverá el problema; debe ser uno que compute la función correcta dados las entradas y restricciones especificadas a nivel computacional. Adicionalmente, los algoritmos deben ser implementables con el hardware disponible. 

Reconociendo la interdependena de niveles, Marr argumentó que el análisis a nivel computacional debería guiar el análisis a otros niveles. Sin entender qué problema está resolviendo un sistema, es difícil entender por el papel de los algoritmos que usa. El análisis computacional proporciona el "por qué" que hace inteligible el "cómo".  

En los capítulos siguientes, en cada uno de ellos empezaremos dandole respuesta a la pregunta "por qué" antes de presentar el "como".

## Van Fraassen: La Explicación como Respuesta a Preguntas

Bas van Fraassen integra los puntos anteriores con una observación aparentemente simple pero de gran alcance: la explicación no es una relación lógica abstracta sino una actividad pragmática. Explicar es responder una pregunta de "¿por qué?" en un contexto dado. Y esas preguntas tienen una estructura que habitualmente se ignora.

Cuando preguntamos "¿por qué P?", no preguntamos "¿por qué P y no cualquier otra cosa concebible?". Preguntamos "¿por qué P en lugar de Q?", donde Q es un *contraste implícito* que depende del contexto. Considera: "¿por qué el niño tomó una manzana?". Si el contraste es {tomó / no tomó}, la respuesta es que tenía hambre. Si el contraste es {manzana / naranja / plátano}, la respuesta es que prefiere las manzanas. Si el contraste es {tomó / compró / pidió}, la respuesta es que no tenía dinero. La misma información puede ser explicativa en un contexto e irrelevante en otro.

Esta perspectiva disuelve muchos debates aparentes en la literatura. Cuando dos investigadores parecen en desacuerdo sobre qué "explica" un fenómeno, con frecuencia están haciendo contrastes implícitos distintos. El que busca mecanismos neurales contrasta el comportamiento observado con lo que ocurriría si ese mecanismo no existiera. El que busca la función evolutiva contrasta el comportamiento con lo que haría un organismo sin esa capacidad adaptativa. No están en desacuerdo sobre el mundo; están haciendo preguntas distintas. La pregunta productiva no es "¿quién tiene razón?", sino "¿qué contraste está haciendo cada uno, y es ese contraste legítimo dado el propósito de la investigación?".

---

## Una Nota sobre los Modelos de Datos

El proceso científico no termina con la observación de un fenómeno ni comienza con la construcción de un modelo teórico. Entre ambos está el trabajo de organizar los datos empíricos de forma que sean interpretables. Patrick Suppes llamó a este paso la construcción de un *modelo de datos*: la transformación de registros crudos en una representación canónica del fenómeno.

Los modelos de datos no son neutros. Cuando Skinner decidió representar el comportamiento de sus ratas como *tasa de respuesta* —número de presiones de palanca por unidad de tiempo— estaba tomando una decisión teórica disfrazada de decisión técnica. Esa representación hacía visibles ciertos patrones (pausas después del refuerzo, aceleración de la tasa bajo programas de razón) y oscurecía otros (microestructura temporal, variación en la topografía de la respuesta). Toda una tradición teórica se organizó alrededor de explicar variaciones en la tasa de respuesta, en parte porque la tasa era el modelo de datos dominante.

En los capítulos que siguen, cada vez que se introduzca una nueva medida —tiempo entre respuestas, magnitud del error de predicción, frecuencia relativa de elección— vale la pena preguntarse qué aspectos del fenómeno hace visibles esa medida y cuáles oculta.

---

## Síntesis

Tres ideas organizan este capítulo y reaparecerán a lo largo del libro.

Los modelos no son copias de la realidad sino vehículos de inferencia: su valor se mide por la calidad de las inferencias que permiten hacer, no por su fidelidad absoluta al fenómeno. Dos modelos del mismo comportamiento pueden coexistir si sirven propósitos distintos.

La explicación no es un único tipo de actividad. Hay explicaciones causales (que identifican los factores que hacen diferencia), explicaciones unificadoras (que muestran que fenómenos heterogéneos comparten estructura), y explicaciones mecanicistas (que especifican los componentes cuyas interacciones producen el fenómeno). Estas formas se complementan.

Los fenómenos complejos pueden analizarse a múltiples niveles. Tinbergen, Marr y Killeen articulan ese espacio de niveles con vocabularios distintos pero convergentes. Cuando en los capítulos que siguen encuentres modelos que parecen incompatibles, la primera pregunta que debes hacerte es si están operando al mismo nivel o respondiendo la misma pregunta. Con frecuencia, la respuesta es que no.

---

## Ejercicios de Comprensión

**Ejercicio 1 (básico).** Considera el siguiente enunciado: "Los estudiantes que duermen más horas antes de un examen obtienen mejores calificaciones." Escribe (a) una explicación contrafactual, (b) una posible explicación intervencionista, y (c) una formulación del hacedor de diferencia más abstracto. ¿Cuál de las tres te parece más informativa para el propósito de diseñar una intervención educativa? ¿Cambia tu respuesta si el propósito es comprender el funcionamiento de la memoria?

**Ejercicio 2 (intermedio).** Un experimento muestra que las ratas presionan más rápido una palanca cuando cada décima presión entrega comida que cuando cada presión la entrega. Usando el marco de Tinbergen, formula las cuatro preguntas que podrías hacer sobre este fenómeno e indica, para cada una, qué tipo de estudio o datos necesitarías para responderla.

**Ejercicio 3 (intermedio).** Alguien argumenta: "Los modelos matemáticos del aprendizaje no son realmente explicaciones porque omiten los mecanismos neuronales reales." Usando los marcos de Marr y Killeen, evalúa este argumento. ¿En qué sentido tiene razón? ¿Qué confunde?

**Ejercicio 4 (avanzado).** En los capítulos siguientes, el comportamiento de orientación de las bacterias se describirá a nivel conductual (kinesis), a nivel algorítmico (ascenso de colina) y brevemente a nivel mecanicista molecular. Elige dos de esos niveles y describe: (a) qué pregunta responde cada uno según el marco de Tinbergen y el de Marr; (b) si son "explicaciones" en los sentidos discutidos en este capítulo, y de qué tipo; (c) qué fenómeno adicional podría investigarse si combináramos información de ambos niveles.
