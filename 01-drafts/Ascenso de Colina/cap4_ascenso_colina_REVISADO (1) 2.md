# Capítulo 4: Ascenso de Colina
## Un Mecanismo de Adaptación Sin Historia

---

## Introducción

En el capítulo anterior vimos cómo la selección natural opera a escala filogenética para producir comportamiento adaptado: soluciones codificadas genéticamente que funcionan bien en entornos relativamente predecibles. Pero la mayoría de los organismos enfrentan entornos variables en escalas de tiempo mucho más cortas que las generaciones, y deben ajustar su comportamiento durante su propia vida, a veces en segundos. ¿Qué ocurre cuando esa variación es tan rápida que la selección natural no puede anticiparla, pero tampoco hay tiempo para aprender en el sentido pleno de la palabra?

Este capítulo introduce el primer mecanismo en nuestro cajón de herramientas: el **ascenso de colina** (*hill climbing*). Es un algoritmo elegantemente simple que permite a organismos muy básicos —incluso sin sistema nervioso— navegar eficientemente hacia recursos en entornos variables. Lo que hace pedagógicamente valioso a este mecanismo no es solo su utilidad práctica, sino que sus componentes esenciales reaparecerán, en formas más sofisticadas, cuando lleguemos al aprendizaje propiamente dicho. Seguiremos aquí la misma progresión que usaremos a lo largo del curso: primero el problema adaptativo, luego el comportamiento observado, después el algoritmo abstracto, y finalmente su expresión matemática.

---

## El Problema Adaptativo

Incluso los organismos más simples —bacterias, plantas, amebas— enfrentan un problema biológico fundamental: localizar y acceder a fuentes de energía que están distribuidas de manera variable e impredecible en el espacio. Una bacteria nadando en un medio acuoso, una plántula germinando en el suelo del bosque, una ameba moviéndose hacia nutrientes químicos: todos comparten el mismo desafío básico. ¿Cómo moverse hacia una concentración mayor de aquello que se necesita, sin saber de antemano dónde está?

El problema se complica por una restricción fundamental: muchos de estos organismos carecen de **receptores de distancia**, los órganos sensoriales que permiten detectar recursos remotamente, como la visión o el olfato en mamíferos. Sin estos receptores, el organismo no puede simplemente "ver" dónde está la comida y dirigirse hacia ella. Solo puede detectar si la concentración de nutrientes en su ubicación *actual* es mayor o menor que hace un momento. La información disponible es estrictamente local y temporal.

A esto se añaden otras restricciones. El organismo solo tiene acceso a información sobre su posición actual y, mediante una memoria muy breve, su posición inmediatamente anterior: no dispone de un mapa del entorno ni puede comparar simultáneamente múltiples ubicaciones distantes. La detección de cambios en concentración tampoco es perfecta; fluctuaciones aleatorias pueden hacer que una zona parezca momentáneamente mejor o peor de lo que realmente es. Cada movimiento consume energía y tiempo, por lo que el organismo no puede explorar indefinidamente. Y en entornos con múltiples fuentes de nutrientes, existe el riesgo de quedarse "atascado" en una fuente pequeña y cercana, sin alcanzar una fuente mayor más alejada —el problema clásico de los **máximos locales**.

Vale la pena notar que este problema no es exclusivo de bacterias o plantas. Es el mismo desafío que enfrenta un robot explorando un terreno desconocido, un algoritmo buscando la mejor solución en un espacio de posibilidades, o tú cuando buscas señal de wifi caminando por un edificio que no conoces: sin mapa, sin vista del router, guiándote solo por la barra de señal que sube o baja con cada paso.

---

## El Comportamiento Observado

### Plantas y el Fototropismo

Las plantas verdes enfrentan una competencia intensa por la luz solar. Una plántula germinando en el suelo del bosque debe crecer hacia la luz esquivando obstáculos —otras plantas, ramas, rocas— que bloquean su camino. Lo hace mediante tres comportamientos coordinados: el tallo rota, "barriendo" diferentes direcciones; una vez que detecta mayor intensidad lumínica en alguna dirección, crece preferentemente hacia ese lado (fototropismo); y simultáneamente crece hacia arriba, alejándose del suelo. La combinación de estos tres comportamientos simples produce trayectorias sorprendentemente eficientes hacia la luz, incluso cuando ésta proviene de direcciones cambiantes o hay obstáculos en el camino.

### La Bacteria Navegando Gradientes Químicos

La bacteria *Salmonella* es notablemente exitosa localizando alimento. En un experimento clásico, se introduce una pipeta capilar con nutrientes en agua donde bacterias nadan libremente. Después de algunos minutos, hay significativamente más bacterias dentro de la pipeta que afuera: las bacterias "encontraron" la fuente de alimento sin cerebro, sin ojos, sin mapa.

La observación detallada del comportamiento de salmonelas individuales revela un patrón que puede parecer sorprendente en su simplicidad. Las bacterias alternan entre dos comportamientos básicos. El primero, que podemos llamar **maromas** (*tumbling*), consiste en girar sobre sí mismas en direcciones aleatorias sin desplazamiento neto: es una forma de exploración, de muestrear diferentes direcciones posibles. El segundo, el **nado en línea recta** (*running*), produce desplazamiento neto en la dirección actual: es explotación, aprovechar una dirección prometedora.

Lo crucial no son los comportamientos en sí, sino la regla que determina cuándo cambiar de uno a otro. Esa regla es sencilla: si la concentración química está mejorando —si la bacteria se mueve hacia mayor concentración—, continúa nadando recto; si la concentración deja de mejorar o empeora, pasa a maromas, reorientándose aleatoriamente hasta que por casualidad apunta en una dirección donde la concentración vuelve a mejorar. Lo que controla la transición no son los valores absolutos de concentración, sino los *cambios* en concentración. La bacteria es sensible a si las cosas están mejorando o empeorando, no a cuán buenas son en un momento dado.

### La Adaptación Sensorial: El Problema de "Nunca Es Suficiente"

Hay una complicación adicional. Si la bacteria cambiara a nado recto ante el *primer* incremento detectado en concentración y se quedara ahí, probablemente terminaría en la primera mejora que encontró, no en la mejor ubicación posible. Las bacterias resuelven esto mediante **adaptación sensorial**: después de un tiempo breve, el sistema de detección "se acostumbra" al nivel actual de concentración. Lo que antes parecía "alta concentración" se convierte gradualmente en el nuevo punto de referencia "normal". Esto obliga a la bacteria a seguir buscando mejoras: lo que momentos antes era suficientemente bueno para mantener el nado recto ya no lo es. La bacteria vuelve a dar maromas hasta encontrar una concentración aún mayor.

La adaptación sensorial implementa una forma de insatisfacción adaptativa: el organismo nunca se contenta completamente con lo actual, sino que sigue buscando mientras haya tiempo y energía. Como veremos más adelante, esta misma lógica reaparece en mecanismos de aprendizaje mucho más complejos.

---

## El Algoritmo

Ahora que vimos el comportamiento empírico, podemos abstraer el mecanismo subyacente. En su versión más básica, el ascenso de colina funciona así: el organismo almacena el valor actual de la variable que le importa (concentración química, intensidad lumínica, señal de wifi); ejecuta una acción exploratoria aleatoria; compara el nuevo valor con el almacenado; si mejoró, pasa a explotación (nado recto, crecimiento direccional, caminar en esa dirección); si no mejoró, continúa explorando. Después de un tiempo, la adaptación sensorial actualiza el punto de referencia, lo que fuerza al sistema a volver a explorar en busca de mejoras adicionales.

Existe una variante ligeramente más sofisticada que podemos llamar **ascenso de mayor pendiente**, análoga a cómo actuarías escalando el Ajusco con los ojos vendados. En lugar de tomar la primera dirección que mejore, el organismo muestrea múltiples direcciones, registra el valor en cada una, y luego se mueve hacia la que mostró la mayor mejora. Esta variante requiere más capacidad de memoria, pero puede ser más eficiente en entornos ruidosos donde un solo muestreo puede dar una impresión equivocada.

El ejemplo de la búsqueda de señal wifi ilustra bien la diferencia entre ambas variantes. En el ascenso simple, caminas en una dirección aleatoria y verificas la señal; si mejoró, sigues en esa dirección; si empeoró, te detienes, giras aleatoriamente, y pruebas otra dirección. En el ascenso de mayor pendiente, te detienes donde estás, das algunos pasos exploratorios en diferentes direcciones —norte, sur, este, oeste— verificas la señal en cada una, y luego caminas decididamente hacia donde la señal fue mayor. En ambos casos estás haciendo *comparaciones sucesivas*: no puedes ver dónde está el router, solo puedes comparar si tienes más o menos señal que hace un momento.

### Los Componentes del Mecanismo

Independientemente de la variante, cualquier implementación del ascenso de colina requiere los mismos ingredientes. El organismo debe ser sensible a alguna propiedad del entorno que correlacione con recursos o peligros —esta variable funciona como señal de retroalimentación que guía el comportamiento sin necesidad de representar explícitamente la ubicación del recurso. Debe retener, aunque sea brevemente, el valor de esa variable en el momento inmediatamente anterior; sin esta memoria mínima no hay base para comparación. El mecanismo central opera sobre esa comparación: si el valor actual es mayor que el anterior, las cosas están mejorando; si no, no lo están. Esta comparación sucesiva —el mismo lugar en dos tiempos diferentes— es lo que distingue al ascenso de colina del mecanismo que veremos en el capítulo siguiente, donde dos lugares se comparan simultáneamente.

El algoritmo requiere además dos modos conductuales contrastantes —exploración y explotación— y una regla clara para cambiar de uno a otro: si el cambio supera cierto umbral, explotar; si no, explorar. El umbral puede ser cero (cualquier mejora es suficiente) o mayor (se requiere una mejora sustancial), lo que ayuda a filtrar fluctuaciones aleatorias en entornos ruidosos. Finalmente, la adaptación sensorial evita el estancamiento en máximos locales al gradualmente ajustar el punto de referencia hacia el valor actual.

---

## 🎮 Simulador: Ascenso de Colina en un Gradiente

**[SIMULADOR AQUÍ: Agente navegando gradiente de concentración con parámetros a y b ajustables]**

**Objetivo:** Descubrir qué combinación de adaptación sensorial y sensibilidad al cambio produce navegación eficiente hacia la fuente de nutrientes, y entender por qué ninguno de los dos extremos (muy lenta/muy rápida) funciona bien.

**Parámetros manipulables:**

El parámetro *a* controla la velocidad de adaptación sensorial (0 < a < 1). Un valor cercano a 1 significa adaptación lenta: el sistema recuerda el pasado por mucho tiempo y tiende a explotar una dirección durante periodos largos. Un valor cercano a 0 significa adaptación rápida: el sistema "olvida" rápidamente y vuelve a explorar pronto.

El parámetro *b* controla la sensibilidad al cambio (b > 0). Un valor alto hace al sistema muy sensible a cambios pequeños; un valor bajo requiere cambios grandes para afectar el comportamiento.

**Ejercicios:**

*Básico:* Comienza con a = 0.9 y b = 0.5. Observa la trayectoria del agente hacia la fuente. ¿Cuánto tiempo tarda? Ahora reduce a a 0.3 manteniendo b constante. ¿Qué cambia en la trayectoria? ¿Llega más rápido o más lento? Antes de cambiar el parámetro, predice qué esperas ver.

*Intermedio:* Coloca dos fuentes de nutrientes: una pequeña cerca del punto de inicio y una grande más alejada. Con a = 0.95 (adaptación muy lenta), ¿el agente queda atrapado en la fuente pequeña o encuentra la grande? Ahora prueba a = 0.5. ¿Cambia el resultado? ¿Puedes explicar por qué la adaptación sensorial ayuda a escapar de los máximos locales?

*Avanzado:* Activa el ruido ambiental en la detección de concentración. Encuentra la combinación de a y b que produce la navegación más eficiente (menor tiempo para llegar, trayectoria más directa) en presencia de ruido. ¿Por qué el ruido hace que algunos valores de b que funcionaban bien sin ruido ya no funcionen?

**Conexión con la teoría:** Lo que observas en el simulador ilustra el corazón de la ecuación que veremos a continuación. El parámetro a determina cuánto "pesa" el pasado en la decisión presente; el término b·[X(t+1) − X(t)] captura exactamente el cambio que la bacteria detecta. Cuando ese cambio es positivo y suficientemente grande, Y supera el umbral y el agente explota; cuando es cero o negativo, Y decae y el agente vuelve a explorar.

---

## Formalización Matemática

Ahora que los componentes del algoritmo son claros, podemos expresarlos con precisión matemática. Esto no añade misterio —simplemente captura en notación compacta lo que ya describimos en palabras.

### La Ecuación Central

El ascenso de colina puede representarse con una sola ecuación que combina los dos ingredientes clave: la adaptación sensorial y la detección de cambio:

$$Y(t+1) = a \cdot Y(t) + b \cdot [X(t+1) - X(t)]$$

donde Y(t) es la variable de decisión en el tiempo t (piensa en ella como el "estado interno" que determina qué modo conductual se ejecuta), X(t) es el valor de la variable ambiental en el tiempo t (concentración química, intensidad lumínica, señal de wifi), *a* es el parámetro de adaptación sensorial (0 < a < 1), y *b* es el parámetro de sensibilidad al cambio (b > 0).

El primer término, a·Y(t), captura la adaptación sensorial. Si a = 1, el valor previo de Y persiste indefinidamente —no hay adaptación. Si a < 1, Y "decae" gradualmente hacia cero aun cuando no haya nuevas señales del ambiente. Cuanto menor es a, más rápido el sistema se ajusta al nivel actual y vuelve a explorar.

El segundo término, b·[X(t+1) − X(t)], captura la detección de cambio. El término entre corchetes es simplemente la diferencia entre el valor ahora y el valor hace un momento: ¿mejoró o empeoró? El parámetro b amplifica o atenúa la importancia de ese cambio en el comportamiento.

La regla que conecta Y con el comportamiento observable es sencilla: si Y supera cierto umbral (típicamente cero), el organismo explota —nada recto, crece hacia la luz, camina en esa dirección; si Y está por debajo del umbral, el organismo explora —da maromas, rota, prueba otra dirección.

### Un Ejemplo Numérico

Sigamos la dinámica con valores concretos: a = 0.9, b = 0.5, umbral = 0.

Partimos de Y(0) = 0 y X(0) = 5 (concentración inicial). El agente está en modo exploración.

**Tiempo 1:** La concentración mejora a X(1) = 7.
Y(1) = 0.9 × 0 + 0.5 × (7 − 5) = 0 + 1.0 = **1.0** → Explotar (nado recto).

**Tiempo 2:** La concentración sigue mejorando: X(2) = 9.
Y(2) = 0.9 × 1.0 + 0.5 × (9 − 7) = 0.9 + 1.0 = **1.9** → Explotar.

**Tiempo 3:** La concentración se estabiliza: X(3) = 9.
Y(3) = 0.9 × 1.9 + 0.5 × (9 − 9) = 1.71 + 0 = **1.71** → Explotar (pero Y empieza a decaer).

**Tiempo 4:** La concentración baja ligeramente: X(4) = 8.
Y(4) = 0.9 × 1.71 + 0.5 × (8 − 9) = 1.54 − 0.5 = **1.04** → Explotar.

**Tiempo 5:** Sigue bajando: X(5) = 7.
Y(5) = 0.9 × 1.04 + 0.5 × (7 − 8) = 0.94 − 0.5 = **0.44** → Explotar (pero Y casi en umbral).

**Tiempo 6:** La concentración sigue empeorando: X(6) = 6.
Y(6) = 0.9 × 0.44 + 0.5 × (6 − 7) = 0.40 − 0.5 = **−0.10** → **Explorar** (dar maromas).

La secuencia ilustra algo importante: el sistema no cambia a exploración en el instante en que la concentración deja de mejorar. La inercia del término a·Y mantiene la explotación durante un tiempo, actuando como un filtro que evita responder a fluctuaciones momentáneas. Pero eventualmente, si la concentración no mejora o empeora, Y cae por debajo del umbral y el organismo vuelve a buscar.

### Propiedades del Sistema

Varios aspectos de esta dinámica merecen atención. El balance entre exploración y explotación queda controlado por los dos parámetros: a bajo produce adaptación rápida y más exploración; a alto produce adaptación lenta y más explotación; b alto hace al sistema sensible a cambios pequeños; b bajo requiere cambios grandes para modificar el comportamiento. El término a·Y actúa además como un filtro de inercia: las fluctuaciones momentáneas no alteran inmediatamente el comportamiento, sino que se requiere evidencia sostenida de cambio. Y la adaptación garantiza que el sistema no se estanque: incluso en una buena ubicación, Y decae eventualmente y el organismo vuelve a explorar, lo que le permite encontrar fuentes aún mejores más adelante.

---

## Lo que el Ascenso de Colina Hace y No Hace

Es crucial entender los límites de este mecanismo, porque precisamente esos límites motivarán los mecanismos que estudiaremos en capítulos posteriores.

El ascenso de colina permite adaptación en tiempo real —el organismo ajusta su comportamiento momento a momento— y navegación eficiente hacia gradientes sin necesidad de mapa ni receptores de distancia. El balance exploración-explotación emerge automáticamente de la dinámica del sistema, y la robustez ante ruido está garantizada por la inercia del término a·Y.

Lo que el mecanismo *no* hace es igualmente revelador. El organismo no acumula información de experiencias pasadas: solo compara "ahora" con "hace un momento". Si repetimos la misma situación mañana, el organismo responde igual que hoy —no hay memoria de largo plazo ni integración de historia. El mecanismo es puramente reactivo: responde a cambios que ya ocurrieron, no anticipa cambios futuros. No hay modelo interno del entorno; el organismo no "sabe" dónde están las fuentes, solo sigue gradientes locales. Y no hay aprendizaje en el sentido estricto: una bacteria que navegó exitosamente ayer no navega mejor hoy por haber tenido esa experiencia.

Esta distinción es central para el libro. El **comportamiento adaptativo sin aprendizaje** —como el ascenso de colina— produce flexibilidad conductual en respuesta al entorno actual, pero sin retener información de experiencias previas. El **comportamiento adaptable** —que estudiaremos en los bloques siguientes— supone exactamente eso: un cambio duradero en el sistema como resultado de la experiencia, una integración de historia. El ascenso de colina es un mecanismo de comparación sucesiva sin integración de historia. Su importancia pedagógica radica en que los mismos principios —comparación, reducción de error, balance exploración-explotación, adaptación— reaparecerán en mecanismos de aprendizaje mucho más complejos.

---

## Conexiones

### Hacia Atrás: Selección Natural

El ascenso de colina es una instancia de ensayo y error análoga, en su lógica, a la selección natural. La exploración aleatoria genera variación conductual; la comparación determina qué variantes "sobreviven" (se explotan); la explotación continúa mientras el gradiente es favorable. La diferencia crucial es temporal: la selección natural opera a escala filogenética (generaciones), mientras que el ascenso de colina opera a escala ontogenética (segundos o minutos en la vida del individuo). Son el mismo principio en escalas de tiempo radicalmente distintas.

### Hacia Adelante: Aprendizaje por Refuerzo

El ascenso de colina anticipa conceptos que serán centrales en el Bloque II. La diferencia [X(t+1) − X(t)] es una primera versión del **error de predicción**: la discrepancia entre lo que se esperaba y lo que ocurrió. La actualización incremental de Y es análoga a cómo el valor asociativo se ajusta ensayo a ensayo en los modelos que estudiaremos. Y el dilema exploración-explotación, que aquí aparece en su forma más simple, se convertirá en uno de los problemas centrales del aprendizaje por refuerzo en el Bloque IV.

### Lateral: Sistemas de Retroalimentación (Próximo Capítulo)

El ascenso de colina utiliza **comparación sucesiva**: el mismo lugar en dos tiempos diferentes. El próximo capítulo introduce los sistemas de retroalimentación, que utilizan **comparación simultánea**: dos sensores detectan el gradiente al mismo tiempo en dos puntos del espacio. Ambos son mecanismos de adaptación sin aprendizaje, pero la diferencia en el tipo de comparación tiene consecuencias importantes para qué problemas puede resolver cada uno.

---

## Ejercicios de Comprensión

**1.** Una ameba se mueve hacia una fuente de glucosa en un gradiente de concentración. Describe, en términos del algoritmo de ascenso de colina, lo que ocurre cuando la concentración de glucosa deja de aumentar durante varios segundos. ¿Qué papel juega la adaptación sensorial en ese momento? ¿Qué pasaría si el parámetro *a* fuera exactamente 1?

**2.** Imagina que estás buscando señal de wifi en un edificio desconocido usando ascenso de mayor pendiente. Explica con tus palabras qué tendrías que hacer físicamente en cada paso del algoritmo. Ahora compara: ¿en qué situaciones preferiría el ascenso simple sobre el de mayor pendiente?

**3.** Usando la ecuación Y(t+1) = a·Y(t) + b·[X(t+1) − X(t)], con a = 0.8 y b = 1.0, calcula los valores de Y para los siguientes 4 tiempos. El umbral es 0.

| Tiempo | X(t) | Y(t) | ¿Explorar o explotar? |
|--------|------|------|-----------------------|
| 0 | 10 | 0 | — |
| 1 | 12 | ? | ? |
| 2 | 14 | ? | ? |
| 3 | 14 | ? | ? |
| 4 | 13 | ? | ? |

¿En qué momento el sistema cambia de modo? ¿Qué dice eso sobre la relación entre estabilización de concentración y exploración?

**4.** El capítulo afirma que el ascenso de colina *no* es aprendizaje. ¿Qué le falta para serlo? Formula una modificación hipotética al mecanismo que lo convertiría en algo más parecido al aprendizaje. ¿Qué nueva capacidad adaptativa tendría el organismo con esa modificación?

**5.** *(Reflexión)* El texto menciona que la adaptación sensorial implementa una forma de "insatisfacción adaptativa". ¿Por qué sería desadaptativo un organismo que *no* tuviera esta propiedad, es decir, que se contentara para siempre con el primer gradiente positivo que encontrara? ¿Puedes pensar en algún contexto donde esa estrategia podría ser ventajosa?

---

## Resumen

El problema adaptativo de este capítulo es localizar recursos en entornos variables sin receptores de distancia ni mapa previo. La solución que estudiamos es el ascenso de colina, un algoritmo de comparación sucesiva que alterna entre exploración aleatoria y explotación direccional, guiado por cambios en una variable ambiental de interés. Sus ingredientes esenciales son: detección de una variable relevante, memoria mínima del valor previo, comparación presente-pasado, dos modos conductuales contrastantes, una regla de transición entre ellos, y adaptación sensorial que previene el estancamiento en máximos locales.

Lo que el mecanismo no hace es tan importante como lo que hace: no hay integración de historia, ni predicción, ni representación del entorno, ni cambio duradero. El ascenso de colina es comportamiento adaptativo sin aprendizaje. Su relevancia pedagógica está en que los mismos principios —comparación, reducción de error, balance exploración-explotación— reaparecerán, transformados y enriquecidos, en los mecanismos de aprendizaje que estudiaremos en los bloques siguientes.

En el próximo capítulo veremos sistemas de retroalimentación, donde el comportamiento no solo responde al entorno sino que lo modifica, creando lazos cerrados de interdependencia entre el organismo y su entorno.

---

## Para Profundizar

Berg, H.C. & Brown, D.A. (1972). Chemotaxis in Escherichia coli analysed by three-dimensional tracking. *Nature, 239*, 500–504. El paper clásico que caracterizó el comportamiento de run and tumble en bacterias.

Schnitzer, M.J. (1993). Theory of continuum random walks and application to chemotaxis. *Physical Review E, 48*(4), 2553–2568. Formalización matemática del mecanismo en bacterias.

Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4a ed.), Capítulo 4. Tratamiento del ascenso de colina en el contexto de algoritmos de búsqueda en inteligencia artificial.
