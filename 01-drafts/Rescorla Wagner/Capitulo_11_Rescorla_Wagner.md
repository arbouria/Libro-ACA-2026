# Capítulo 11: El Modelo de Rescorla-Wagner {#sec-rescorla-wagner}

## Objetivos del Capítulo

Al finalizar este capítulo, deberías ser capaz de explicar por qué el modelo de Bush-Mosteller no puede dar cuenta de fenómenos de competencia entre estímulos como el bloqueo y el ensombrecimiento, y cómo la innovación de Rescorla-Wagner—el cálculo del error de predicción basado en la suma de valores de todos los elementos presentes—resuelve elegantemente este problema computacional. Comprenderás los supuestos formales del modelo: separabilidad de estímulos compuestos, valores predictivos positivos y negativos, y la regla de suma para integrar valores. Serás capaz de derivar las predicciones del modelo para fenómenos clave (bloqueo, ensombrecimiento, inhibición condicionada, sobreexpectación) y entenderás que estos no son fenómenos independientes sino consecuencias matemáticas necesarias de un único principio: competencia por error de predicción limitado. Reconocerás las limitaciones del modelo (extinción, inhibición latente, pre-condicionamiento sensorial) y cómo estas motivaron extensiones posteriores. Finalmente, apreciarás que Rescorla-Wagner representa un cambio conceptual profundo: de concebir el aprendizaje como registro de contigüidades a entenderlo como inferencia activa sobre estructura causal en ambientes complejos.

---

## Introducción: Más Allá de Estímulos Aislados

En el capítulo anterior, vimos que el modelo de aprendizaje por refuerzo de Bush-Mosteller, conocido también como modelo de aprendizaje de error de predicción, captura razonablemente bien la adquisición de valor predictivo cuando un estímulo o respuesta aislados van seguidos de un refuerzo. El modelo formaliza la intuición de que el aprendizaje es impulsado por la discrepancia entre lo que se esperaba (el valor V) y lo que se obtuvo (el reforzador R). Cuando esta discrepancia es grande, el aprendizaje es rápido; cuando es pequeña, el aprendizaje se desacelera hasta detenerse cuando la predicción es perfecta.

Sin embargo, este modelo no puede dar cuenta de los resultados presentados en el Capítulo 8 sobre asignación de crédito a estímulos, los cuales ilustran la importancia de una serie de correlaciones más complejas: aquellas que sostiene el estímulo condicionado con la aparición del refuerzo, aquellas que sostiene el EC con otros estímulos presentes (elementos del contexto), y aquellas que existen previamente entre otros estímulos distintos y el refuerzo actual. Los fenómenos de bloqueo, ensombrecimiento, e inhibición condicionada demuestran que los organismos no tratan cada estímulo de forma independiente, sino que los estímulos compiten entre sí por la capacidad limitada de predecir el reforzador.

### El Problema Computacional

Considere una situación cotidiana. Regresa a casa después de cenar en un restaurante nuevo y experimenta un malestar estomacal. El ambiente del restaurante era un compuesto de múltiples elementos: el sabor del platillo, el aroma, la música ambiental, el color de las paredes, su acompañante de mesa, el plato en que se sirvió la comida. ¿Cómo determina su sistema de aprendizaje cuál de estos elementos causó su malestar? Si ya sabe por experiencia previa que su acompañante es agradable y nunca le ha causado malestar, ese elemento ya tiene un valor predictivo establecido. ¿Cómo afecta esto a la asignación de crédito a los otros elementos del compuesto?

El modelo de Bush-Mosteller no puede responder esta pregunta porque actualiza cada elemento de forma independiente. Si el sabor, el aroma y la música estaban todos presentes antes del malestar, cada uno se actualizaría como si fuera el único predictor, sin considerar la presencia de los demás. Esto viola el principio fundamental que emerge de la evidencia empírica: los organismos tienen una capacidad limitada de asociación que debe distribuirse entre múltiples predictores competidores.

### La Respuesta de Rescorla y Wagner

Originalmente, los resultados de competencia entre estímulos indujeron interpretaciones que enfatizaban que la asignación de crédito dependía de que el reforzador fuera sorpresivo, inesperado, informativo, o que atrajera la atención. En 1972, Robert Rescorla y Allan Wagner presentaron un modelo matemático elegante que capturaba formalmente la intuición acerca del papel de la sorpresa sin hacer referencia a procesos atencionales que se suponían difíciles de evaluar con sujetos no humanos. La innovación fue conceptualmente simple pero profundamente poderosa: el error de predicción que impulsa el aprendizaje no se calcula comparando el reforzador con el valor del estímulo individual, sino con la suma de los valores de todos los estímulos presentes.

Este modelo sigue siendo hasta la fecha uno de los motores principales de la investigación en aprendizaje, tanto en psicología como en neurociencia y aprendizaje automático. Su influencia se extiende desde la comprensión de neuronas dopaminérgicas que codifican errores de predicción hasta algoritmos de aprendizaje por refuerzo en inteligencia artificial.

---

## Parte I: Recordatorio del Modelo de Bush-Mosteller

Antes de adentrarnos en la innovación de Rescorla-Wagner, es crucial recordar precisamente qué aspectos del modelo de Bush-Mosteller se conservan y cuáles se modifican. El modelo de Bush-Mosteller captura el principio básico de la reducción de error de predicción:

$$V_{x,t+1} = V_{x,t} + \alpha(R_t - V_{x,t})$$

Donde:
- $V_{x,t}$ es el valor predictivo del estímulo $x$ en el ensayo $t$
- $R_t$ es el reforzador recibido (típicamente 1 si está presente, 0 si está ausente)
- $\alpha$ es la tasa de aprendizaje ($0 < \alpha < 1$)
- $(R_t - V_{x,t})$ es el error de predicción

### Características Clave que se Conservarán

**1. Motor del aprendizaje:** El error de predicción impulsa el cambio en el valor. Sin error, no hay aprendizaje.

**2. Ganancias decrecientes:** A medida que $V$ se aproxima a $R$, el error disminuye y el aprendizaje se desacelera automáticamente.

**3. Asíntota natural:** El valor converge hacia $R$ cuando no hay más error de predicción—el sistema encuentra su punto de equilibrio sin necesidad de mecanismos adicionales.

### La Limitación Crítica

Bush-Mosteller solo considera un elemento a la vez. Si múltiples estímulos están presentes, cada uno se actualiza independientemente usando su propio valor individual:

$$\Delta V_A = \alpha(R_t - V_{A,t})$$
$$\Delta V_B = \alpha(R_t - V_{B,t})$$

Esto significa que si $A$ y $B$ están presentes juntos y son seguidos por un reforzador, ambos aprenderán en paralelo sin "saber" de la existencia del otro. No hay competencia, no hay interferencia. El modelo puede explicar cómo un tono aislado adquiere valor predictivo cuando se presenta antes de comida, pero no puede explicar qué ocurre cuando un tono y una luz predicen conjuntamente el mismo reforzador, ni qué sucede cuando la luz ya predice perfectamente la comida antes de que se introduzca el tono.

Esta limitación no es un defecto menor que pueda ignorarse. Los fenómenos de bloqueo y ensombrecimiento demuestran que es fundamental para entender cómo funcionan realmente los sistemas de aprendizaje biológicos. La modificación de Rescorla-Wagner para resolver esta limitación es el tema central de este capítulo.

---

## Parte II: Los Dos Componentes del Modelo de Rescorla-Wagner

El modelo de Rescorla-Wagner incluye dos grandes componentes que lo distinguen de su predecesor. Es importante entender que el primero se conserva intacto—la innovación reside enteramente en el segundo componente.

### Componente 1: El Motor de Bush-Mosteller

Rescorla-Wagner mantiene el principio de reducción de error de predicción como motor fundamental del aprendizaje. El aprendizaje sigue siendo impulsado por la discrepancia entre lo esperado y lo obtenido. La estructura básica de la ecuación de actualización se preserva. Lo único que cambia es qué se compara con el reforzador para calcular el error—este cambio aparentemente menor tiene consecuencias profundas.

### Componente 2: Modelo de Percepción de Estímulos Compuestos

Este es el aporte revolucionario y representa un supuesto explícito sobre cómo los organismos perciben y procesan estímulos complejos. El modelo propone que los organismos perciben estímulos complejos como conjuntos de elementos separables que compiten entre sí por asignarse el crédito del reforzador.

Un rostro, por ejemplo, no se procesa como una unidad integrada indivisible, sino como un conjunto de elementos distinguibles: ojos, nariz, boca, orejas, contorno facial, textura de piel. Cada elemento puede adquirir independientemente valor predictivo, pero crucialmente, todos compiten por un "presupuesto" limitado de valor total determinado por la magnitud del reforzador.

### La Intuición Central

Imaginen que prueban un platillo nuevo en un restaurante y les encanta intensamente. El platillo es un compuesto de múltiples elementos: los ingredientes principales, las especias, la presentación visual, el plato en que se sirve, el ambiente del restaurante, la compañía con quien comen. ¿Cómo determina su sistema de aprendizaje qué elemento o elementos "causaron" su placer intenso?

El modelo de Rescorla-Wagner propone que cada elemento compite por explicar el resultado. El placer total que experimentaron representa un "presupuesto" fijo de valor predictivo que debe distribuirse entre los elementos. Si ya saben por experiencia previa que disfrutan intensamente la compañía de su acompañante (ese elemento ya tiene valor alto), quedará menos "crédito" disponible para asignárselo a los ingredientes del platillo. El sistema asume implícitamente que los elementos en conjunto deben predecir el nivel total de placer experimentado—ni más ni menos.

Esta intuición de presupuesto limitado y competencia entre elementos es la clave conceptual del modelo. Formalizar matemáticamente esta intuición resulta sorprendentemente simple, como veremos en la siguiente sección.

---

## Parte III: Supuestos Formales del Modelo

El modelo de Rescorla-Wagner se basa en cinco supuestos fundamentales que deben especificarse con precisión para derivar predicciones cuantitativas.

### Supuesto 1: Separabilidad de los Estímulos

Los estímulos compuestos están conformados por elementos (estímulos) separables que pueden procesarse de forma independiente.

Una cara no es un estímulo integrado único e indivisible. Es un conjunto de elementos: ojos, boca, orejas, nariz, contorno, textura, color. Cada elemento puede procesarse, representarse y evaluarse independientemente en el sistema nervioso. Esta separabilidad permite que diferentes elementos adquieran diferentes valores predictivos, y es lo que hace posible la competencia entre elementos.

Este supuesto no es trivial. Implica que el sistema perceptual descompone experiencias en componentes antes de asignarles valor predictivo. Estudios posteriores han demostrado que esta descomposición puede ocurrir a múltiples niveles: características visuales elementales (orientación, color, movimiento), objetos completos, categorías abstractas. El nivel apropiado de descomposición depende de la historia de aprendizaje del organismo y de la estructura del ambiente.

### Supuesto 2: Valor Predictivo de los Elementos

Cada elemento tiene un número (valor) asociado que representa su capacidad predictiva. A diferencia de Bush-Mosteller donde los valores eran necesariamente no-negativos, Rescorla-Wagner permite valores en todo el rango real:

- $V$ puede ser positivo: predice la presencia de un reforzador
- $V$ puede ser cero: no predice nada (estímulo neutral)
- $V$ puede ser negativo: predice la ausencia de un reforzador

Esta extensión a valores negativos es crucial. Permite formalizar el concepto de inhibición condicionada: estímulos que no simplemente no predicen un reforzador, sino que activamente predicen su ausencia. Como veremos, esta capacidad de representar predictores de ausencia emerge naturalmente del mecanismo de competencia.

**Relación con la conducta:** Es importante enfatizar que el valor es solo ordinalmente relacionado con la respuesta observable. Un elemento con $V = 1$ no produce necesariamente el doble de respuestas que uno con $V = 0.5$. Los valores numéricos indican el orden de predicción (mayor valor = mayor predicción) y probablemente mayor respuesta, pero la relación cuantitativa exacta entre $V$ y la tasa de respuesta no está especificada por el modelo. Esta es una limitación deliberada que mantiene al modelo general y testable—especifica relaciones ordinales sin comprometerse con funciones de mapeo específicas que podrían variar entre especies, contextos y medidas de respuesta.

### Supuesto 3: Regla de Integración—La Suma de Valores

Cuando múltiples elementos están presentes simultáneamente, el valor predictivo total del compuesto es la suma aritmética simple de los valores de todos sus elementos:

$$V_{total} = V_A + V_B + V_C + \ldots + V_n$$

Si un compuesto incluye un tono, una luz y el contexto experimental:

$$V_{total} = V_{tono} + V_{luz} + V_{contexto}$$

Esta suma representa la predicción total del organismo sobre la magnitud del reforzador que aparecerá. La regla de suma es el supuesto más simple posible para combinar predicciones de múltiples fuentes—hay reglas alternativas más complejas (promedios ponderados, productos, máximos) pero la suma resulta ser una excelente primera aproximación y hace al modelo matemáticamente tratable.

Un aspecto sutil pero importante: todos los elementos presentes contribuyen a $V_{total}$, no solo los que el experimentador designó como "estímulos condicionados". El contexto experimental (la caja, los sonidos de fondo, la iluminación) también son elementos con sus propios valores que contribuyen a la suma. Esto tiene implicaciones profundas para fenómenos contextuales que discutiremos más adelante.

### Supuesto 4: Actualización Basada en $V_{total}$

Este es el corazón de la innovación. El cambio en el valor de cada elemento depende de la discrepancia entre el reforzador obtenido y la suma de todos los valores presentes:

$$\Delta V_x = \alpha_x \beta (R - V_{total})$$

No es $(R - V_x)$ como en Bush-Mosteller, sino $(R - V_{total})$. Esta modificación aparentemente pequeña—reemplazar $V_x$ por $V_{total}$ en el cálculo del error—tiene consecuencias profundas:

**1. El error de predicción es compartido:** Todos los elementos presentes experimentan el mismo error de predicción. Si el reforzador fue mayor de lo esperado basándose en $V_{total}$, el error es positivo para todos. Si fue menor, el error es negativo para todos.

**2. Todos los elementos se actualizan con base en el mismo error:** Cada elemento ajusta su valor proporcionalmente al mismo error global, aunque la magnitud del ajuste puede diferir si tienen diferentes parámetros $\alpha$.

**3. Si el error es cero para el compuesto, ningún elemento cambia:** Cuando $V_{total} = R$, no importa cuánto contribuya cada elemento individual a esa suma—todos dejan de aprender. El sistema alcanzó un equilibrio colectivo.

### Supuesto 5: Competencia entre Elementos

La consecuencia directa de usar $V_{total}$ en lugar de $V_x$: los elementos compiten por un valor predictivo limitado.

El valor predictivo total está limitado por $R$. Cuando $V_{total}$ alcanza $R$, no queda error de predicción y el aprendizaje se detiene para todos los elementos. Si un elemento ya "capturó" la mayor parte del valor predictivo disponible, queda poco o nada disponible para otros elementos presentes. Este es el mecanismo matemático que formaliza la competencia.

**Analogía económica:** Imaginen un presupuesto fijo ($R = 100$ pesos) que debe distribuirse entre varios departamentos (elementos). Si el departamento A ya tiene asignados 90 pesos ($V_A = 0.9$ si $R = 1$), y el departamento B tiene 5 pesos ($V_B = 0.05$), solo quedan 5 pesos disponibles ($1 - 0.95 = 0.05$). Si se introduce un nuevo departamento C, debe competir por esos 5 pesos restantes. El presupuesto total no puede exceder 100 pesos—es una cantidad conservada que se redistribuye pero no se crea.

Esta competencia no requiere que los elementos "sepan" de la existencia mutua o que haya un mecanismo de comunicación explícito entre ellos. Emerge automáticamente del cálculo centralizado de $V_{total}$ y su uso para determinar el error de predicción compartido.

---

## Parte IV: La Ecuación Completa de Rescorla-Wagner

### Forma Básica para un Solo Elemento

Para un elemento individual $x$ presente en un ensayo donde también están presentes otros elementos:

$$\Delta V_x = \alpha_x \beta (R - V_{total})$$

O en forma recursiva que muestra el valor en el siguiente ensayo:

$$V_{x,t+1} = V_{x,t} + \alpha_x \beta (R_t - V_{total,t})$$

Donde $V_{total,t} = \sum_{i \in \text{presentes}} V_{i,t}$ es la suma de los valores de todos los elementos presentes en el ensayo $t$.

### Los Parámetros $\alpha$ y $\beta$

El modelo introduce dos parámetros de aprendizaje en lugar de uno. Esta distinción captura una intuición importante sobre las fuentes de variación en la velocidad de aprendizaje.

**$\alpha_x$: Asociabilidad del Estímulo**

Representa qué tan fácilmente el estímulo $x$ forma asociaciones. Diferentes estímulos tienen diferentes asociabilidades que reflejan sus propiedades perceptuales:

- Estímulos más salientes (intensos, novedosos, biológicamente relevantes) tienen $\alpha$ más alto
- Estímulos débiles o difíciles de percibir tienen $\alpha$ más bajo
- $\alpha$ puede variar entre elementos: $\alpha_{luz\_intensa} > \alpha_{luz\_tenue}$

En la formulación original, $\alpha$ es una propiedad fija del estímulo. Extensiones posteriores (Pearce-Hall, Mackintosh) permiten que $\alpha$ cambie con la experiencia—un tema que exploraremos en la sección de limitaciones.

**$\beta$: Efectividad del Reforzador**

Representa qué tan efectivo es el reforzador para producir aprendizaje. Diferentes reforzadores tienen diferentes efectividades:

- Reforzadores intensos o biológicamente importantes tienen $\beta$ más alto
- Reforzadores débiles tienen $\beta$ más bajo
- $\beta$ puede diferir entre adquisición ($\beta_1$) y extinción ($\beta_2$)

**¿Por qué dos parámetros?**

La distinción permite al modelo capturar que tanto las propiedades del EC como las del reforzador influyen en la velocidad de aprendizaje. Un estímulo muy saliente ($\alpha$ alto) con un reforzador débil ($\beta$ bajo) podría aprender a la misma velocidad que un estímulo poco saliente ($\alpha$ bajo) con un reforzador intenso ($\beta$ alto). La separación hace al modelo más flexible sin añadir complejidad matemática sustancial.

En muchas aplicaciones simplificadas, se combina $\alpha_x \beta$ en un solo parámetro efectivo de tasa de aprendizaje. Para nuestros propósitos, a menudo usaremos esta simplificación, escribiendo simplemente $\alpha$ para el producto $\alpha_x \beta$.

### Forma General para Múltiples Elementos

Para un compuesto que incluye elementos $A, B, C, \ldots$, cada elemento se actualiza:

$$\Delta V_A = \alpha_A \beta (R - V_{total})$$
$$\Delta V_B = \alpha_B \beta (R - V_{total})$$
$$\Delta V_C = \alpha_C \beta (R - V_{total})$$

Donde:

$$V_{total} = V_A + V_B + V_C + \ldots$$

Noten que el error $(R - V_{total})$ es el mismo para todos los elementos—solo difieren en sus parámetros $\alpha$ que determinan cuánto aprenden del error compartido.

### Sistema Dinámico Acoplado

Una perspectiva importante: el modelo de Rescorla-Wagner para múltiples elementos no es una colección de ecuaciones independientes, sino un sistema dinámico acoplado. El cambio en $V_A$ depende de $V_B, V_C, \ldots$ a través de $V_{total}$, y viceversa. Las ecuaciones están interconectadas—esto es lo que genera competencia.

Para un compuesto de dos elementos, tenemos:

$$V_{A,t+1} = V_{A,t} + \alpha_A \beta (R - V_{A,t} - V_{B,t})$$
$$V_{B,t+1} = V_{B,t} + \alpha_B \beta (R - V_{A,t} - V_{B,t})$$

Este es un sistema de dos ecuaciones en diferencias acopladas. Las trayectorias de $(V_A, V_B)$ en el espacio de estados bidimensional convergen a un subespacio donde $V_A + V_B = R$—una recta en el plano 2D. La distribución específica del valor entre $A$ y $B$ a lo largo de esta recta depende de sus parámetros $\alpha$ y de sus valores iniciales.

Esta perspectiva de sistemas dinámicos no es típica en textos de psicología, pero es invaluable para entender profundamente las propiedades del modelo y conectarlo con herramientas de análisis de otras disciplinas.

---

## Parte V: Derivando Fenómenos Clave

La potencia del modelo de Rescorla-Wagner reside en que los principales fenómenos de competencia entre estímulos no se postulan ad hoc—emergen como consecuencias matemáticas necesarias de los supuestos del modelo. En esta sección derivaremos formalmente cómo el modelo explica bloqueo, ensombrecimiento, inhibición condicionada y sobreexpectación.

### Bloqueo: Derivación Matemática

El bloqueo fue descubierto por Leon Kamin en 1968 trabajando con ratas en un paradigma de miedo condicionado. Kamin observó algo profundamente sorprendente: si las ratas primero aprendían a temer un tono porque iba seguido de shock eléctrico, y luego se introducía una luz que siempre aparecía junto con el tono (formando un compuesto tono-luz que también iba seguido de shock), las ratas no aprendían a temer la luz. Era como si el tono, al ya predecir perfectamente el shock, "bloqueaba" el aprendizaje sobre la luz nueva.

Este fenómeno desafió profundamente la noción de que la contigüidad era suficiente para el aprendizaje. La luz iba seguida del shock consistentemente en todos los ensayos de la Fase 2, pero no adquiría valor predictivo. El modelo de Bush-Mosteller predecía aprendizaje normal porque la luz tenía contigüidad perfecta con el shock. El modelo de Rescorla-Wagner explica este resultado como una consecuencia matemática directa de la competencia por error de predicción limitado. El bloqueo no requiere explicación adicional—emerge automáticamente de la ecuación.

**Protocolo de Kamin (1968):**

**Fase 1:** Estímulo $A$ → Reforzador (múltiples ensayos hasta que $V_A \approx R$)

**Fase 2:** Compuesto $AB$ → Reforzador

**Predicción de Bush-Mosteller:** En Fase 2, el estímulo $B$ debería aprender normalmente porque va seguido de reforzador. $\Delta V_B = \alpha_B(R - V_B) > 0$ siempre que $V_B < R$.

**Derivación según Rescorla-Wagner:**

Al final de la Fase 1:
- $V_A \approx R$ (supongamos exactamente $R$ para simplicidad)
- $V_B = 0$ (no ha sido presentado)

En el primer ensayo de Fase 2:
- $V_{total} = V_A + V_B = R + 0 = R$
- Error de predicción: $\delta = R - V_{total} = R - R = 0$
- Actualización: $\Delta V_A = \alpha_A \beta \cdot 0 = 0$
- Actualización: $\Delta V_B = \alpha_B \beta \cdot 0 = 0$

El elemento $B$ no aprende porque el error de predicción es cero. El reforzador ya está completamente predicho por $A$, así que no hay "sorpresa" que pueda asignarse a $B$. Este bloqueo es completo y permanente—en todos los ensayos subsecuentes de Fase 2, $V_{total} = R$ y el error permanece en cero.

**Generalización:** El bloqueo ocurre siempre que $V_{total}$ alcanza $R$ antes de introducir un nuevo elemento. No importa qué elementos contribuyan a $V_{total}$—si la suma ya iguala a $R$, elementos nuevos no pueden adquirir valor.

### Ensombrecimiento: Competencia por Error Limitado

El ensombrecimiento fue descrito originalmente por Pavlov y estudiado sistemáticamente por investigadores como Mackintosh en las décadas de 1960 y 1970. El fenómeno demuestra que cuando dos estímulos se presentan simultáneamente desde el inicio del entrenamiento, el estímulo más saliente o intenso adquiere mayor valor predictivo que el estímulo menos saliente, a pesar de que ambos tienen exactamente la misma relación temporal con el reforzador. Por ejemplo, si se entrena a ratas con un compuesto de luz brillante más tono suave, y luego se prueban los elementos por separado, la respuesta a la luz es mayor que la respuesta al tono.

Este resultado es incompatible con teorías basadas puramente en contigüidad—ambos elementos deberían aprender igual porque ambos van seguidos del reforzador con la misma frecuencia. Tampoco puede explicarse con el modelo de Bush-Mosteller, que predice aprendizaje idéntico para ambos elementos (asumiendo parámetros iguales). El modelo de Rescorla-Wagner captura el ensombrecimiento a través de la interacción entre diferencias en asociabilidad (α) y competencia por error compartido. Los elementos con mayor α aprenden más rápido del mismo error, capturando mayor proporción del valor total disponible.

**Protocolo:**
- Grupo 1: Compuesto $AB$ → Reforzador (donde $\alpha_A > \alpha_B$)
- Grupo 2: Estímulo $A$ solo → Reforzador  
- Grupo 3: Estímulo $B$ solo → Reforzador

**Pregunta:** ¿Cómo se compara el valor final de $A$ en Grupo 1 versus Grupo 2? ¿Y el valor de $B$ en Grupo 1 versus Grupo 3?

**Derivación para valores asintóticos:**

En equilibrio, el cambio debe ser cero para ambos elementos:

$$\Delta V_A = \alpha_A \beta (R - V_A - V_B) = 0$$
$$\Delta V_B = \alpha_B \beta (R - V_A - V_B) = 0$$

Ambas ecuaciones implican: $R - V_A - V_B = 0$, es decir, $V_A + V_B = R$.

Pero ¿cómo se distribuye este valor total entre $A$ y $B$? Siguiendo las dinámicas del sistema, la razón de cambio entre los elementos es:

$$\frac{\Delta V_A}{\Delta V_B} = \frac{\alpha_A}{\alpha_B}$$

Esto implica que en equilibrio:

$$\frac{V_A}{V_B} = \frac{\alpha_A}{\alpha_B}$$

Combinando con $V_A + V_B = R$:

$$V_A = \frac{\alpha_A}{\alpha_A + \alpha_B} R$$
$$V_B = \frac{\alpha_B}{\alpha_A + \alpha_B} R$$

Si $\alpha_A = 2\alpha_B$, entonces $V_A = \frac{2}{3}R$ y $V_B = \frac{1}{3}R$.

**Comparación con entrenamiento solo:**
- Grupo 2 (solo $A$): $V_A = R$
- Grupo 3 (solo $B$): $V_B = R$

El elemento $A$ en compuesto adquiere menos valor que solo ($\frac{2}{3}R < R$), y $B$ adquiere aún menos ($\frac{1}{3}R < R$). El elemento más saliente "ensombrece" al menos saliente—ambos sufren del compuesto, pero el débil sufre más.

### Inhibición Condicionada: Valores Negativos

La inhibición condicionada fue reconocida por Pavlov, quien notó que algunos estímulos no simplemente carecían de capacidad excitatoria sino que activamente suprimían respuestas condicionadas. Sin embargo, fue difícil de estudiar rigurosamente porque requiere distinguir entre un estímulo neutral (que no predice nada) y un estímulo inhibitorio (que predice ausencia). Rescorla, en trabajos pioneros de finales de los 1960s, desarrolló pruebas operacionales rigurosas para detectar inhibición condicionada y demostró que ciertos protocolos de entrenamiento generan estímulos con propiedades inhibitorias genuinas.

A diferencia del modelo de Bush-Mosteller que solo permite valores no-negativos, Rescorla-Wagner permite valores negativos que representan inhibición condicionada—la predicción activa de ausencia de reforzador. Esta capacidad de generar valores negativos no fue postulada ad hoc para explicar inhibición, sino que emerge naturalmente cuando el error de predicción basado en $V_{total}$ se vuelve negativo. Un estímulo adquiere valor negativo cuando se presenta en compuesto con un excitador en ausencia del reforzador, generando un error negativo que impulsa su valor por debajo de cero.

**Protocolo para generar inhibición:**
- Ensayos $A+$: Estímulo $A$ → Reforzador (hasta que $V_A \approx R$)
- Ensayos $AB-$: Compuesto $AB$ → Sin reforzador

**Derivación:**

Después del entrenamiento $A+$:
- $V_A \approx R$
- $V_B = 0$

En el primer ensayo $AB-$:
- $V_{total} = V_A + V_B = R + 0 = R$
- Reforzador presente: $R = 0$ (ausencia)
- Error: $\delta = 0 - R = -R < 0$

Actualizaciones:
- $\Delta V_A = \alpha_A \beta (-R) < 0$ (el valor de $A$ disminuye)
- $\Delta V_B = \alpha_B \beta (-R) < 0$ (el valor de $B$ disminuye hacia negativo)

En ensayos subsecuentes $AB-$, $V_{total}$ disminuye gradualmente. Eventualmente alcanza equilibrio cuando $V_{total} = 0$ (predice correctamente la ausencia de reforzador).

En equilibrio: $V_A + V_B = 0$, lo que implica $V_B = -V_A$.

Si durante los ensayos $AB-$ no se presentan más ensayos $A+$ para mantener $V_A$ alto, ambos valores decaen. Pero si se intercalan ensayos $A+$ (para mantener $V_A \approx R$) con ensayos $AB-$, entonces en equilibrio de los ensayos $AB-$:

$$V_B \approx -R$$

El estímulo $B$ adquiere valor negativo que "cancela" el valor positivo de $A$, prediciendo correctamente que el compuesto no produce reforzador.

**Pruebas de inhibición propuestas por Rescorla:**

**1. Prueba de sumación:** Presentar $B$ con un nuevo excitador $C$ (donde $V_C > 0$). El modelo predice que la respuesta a $BC$ debería ser menor que a $C$ solo, porque $V_{BC} = V_B + V_C < V_C$ cuando $V_B < 0$.

**2. Prueba de retardo:** Entrenar $B$ como excitador ($B+$). El modelo predice aprendizaje más lento porque $B$ comienza con valor negativo y primero debe alcanzar cero antes de volverse positivo.

Ambas predicciones se confirman empíricamente. Crucialmente, Rescorla argumentó que solo pasando ambas pruebas podemos concluir que un estímulo es verdaderamente inhibitorio, descartando explicaciones alternativas basadas en atención.

### Sobreexpectación: Reducción Cuando la Suma Excede el Reforzador

La sobreexpectación representa una de las predicciones más elegantes y contraintuitivas del modelo de Rescorla-Wagner. A diferencia del bloqueo, ensombrecimiento e inhibición—fenómenos que ya se conocían empíricamente cuando se formuló el modelo—la sobreexpectación fue predicha por el modelo antes de ser descubierta experimentalmente. Kremer (1978) diseñó experimentos específicamente para probar esta predicción derivada del modelo, y los resultados confirmaron la predicción de forma notable.

El fenómeno desafía la intuición porque involucra reforzamiento continuo llevando a reducción de valores. Si dos estímulos se entrenan por separado hasta que cada uno predice perfectamente un reforzador, y luego se presentan juntos seguidos del mismo reforzador, uno esperaría intuitivamente que sus valores se mantuvieran estables o incluso incrementaran—después de todo, ambos están siendo reforzados. Sin embargo, el modelo predice exactamente lo opuesto: ambos valores deben decrecer. La razón es que la suma de sus predicciones excede el reforzador disponible, generando un error de predicción negativo a pesar de la presencia del reforzador.

**Protocolo:**
- Fase 1: Entrenar $A+$ y $B+$ por separado hasta que ambos alcancen $V_A \approx V_B \approx R$
- Fase 2: Presentar compuesto $AB+$

**Predicción intuitiva:** Los valores de $A$ y $B$ deberían mantenerse o incrementar—ambos están siendo reforzados.

**Derivación según Rescorla-Wagner:**

Al inicio de Fase 2:
- $V_A \approx R$
- $V_B \approx R$  
- $V_{total} = V_A + V_B \approx 2R$

En ensayos $AB+$:
- Error: $\delta = R - V_{total} = R - 2R = -R < 0$

Actualizaciones:
- $\Delta V_A = \alpha_A \beta (-R) < 0$ (valor de $A$ disminuye)
- $\Delta V_B = \alpha_B \beta (-R) < 0$ (valor de $B$ disminuye)

Ambos valores decrecen hasta que $V_A + V_B = R$. La suma de las predicciones excedía el reforzador disponible—el sistema estaba "sobreexpectando" y debe corregir hacia abajo.

Esta predicción sorprendente fue confirmada experimentalmente por Rescorla y otros. Es una demostración elegante del poder predictivo del modelo: genera expectativas contraintuitivas que resultan correctas.

---

## Parte VI: Simulaciones y Visualización

[Esta sección incluiría las simulaciones que mencionas tener. Describo qué figuras serían ideales:]

**Figura 11.1: Bloqueo**
Panel A: Fase 1 (solo A) - Curva de adquisición de $V_A$ hacia $R$
Panel B: Fase 2 (AB compuesto) - $V_A$ permanece estable, $V_B$ permanece en cero
Panel C: Prueba - Respuesta a $B$ solo es mínima

**Figura 11.2: Ensombrecimiento**  
Comparación de valores finales: $V_A$ en compuesto vs. solo, $V_B$ en compuesto vs. solo
Mostrar cómo la razón de asociabilidades determina la distribución del valor

**Figura 11.3: Inhibición Condicionada**
Panel A: Entrenamiento $A+$ y $AB-$ intercalados
Panel B: Evolución de $V_A$ y $V_B$ a través de ensayos, mostrando $V_B$ volviéndose negativo
Panel C: Prueba de sumación con nuevo excitador $C$

**Figura 11.4: Sobreexpectación**
Panel A: Fase 1 - Ambos elementos alcanzan $V \approx R$
Panel B: Fase 2 - Ambos valores decrecen en compuesto
Panel C: Comparación con grupo control que no recibe Fase 2

**Figura 11.5: Espacio de Estados 2D**
Trayectorias de $(V_A, V_B)$ para diferentes protocolos
Mostrar convergencia a la recta $V_A + V_B = R$
Ilustrar cómo diferentes parámetros $\alpha$ producen diferentes puntos de equilibrio sobre esta recta

---

## Parte VII: Limitaciones del Modelo y Extensiones

Dentro de la psicología, pocos modelos han sido tan exitosos como el de Rescorla-Wagner en dar cuenta de una amplia gama de resultados, abrir nuevas rutas de investigación y capturar formalmente intuiciones sobre competencia entre estímulos. Sin embargo, como ocurre con cualquier modelo científico, hay un número de fenómenos empíricos para los cuales el modelo genera predicciones incorrectas. Estas "fallas" no representan fracasos sino oportunidades: han dado lugar a extensiones del modelo y a modelos alternativos que profundizan nuestra comprensión. A continuación presentamos tres limitaciones importantes seleccionadas por su claridad conceptual y porque motivaron desarrollos teóricos importantes.

### Limitación 1: Extinción y Recuperación Espontánea

**Predicción del modelo:** En extinción, el reforzador que previamente seguía a un estímulo deja de presentarse. $R$ cambia de 1 a 0. El modelo predice que el valor del estímulo decrece gradualmente hacia cero:

$$\Delta V = \alpha \beta (0 - V) = -\alpha \beta V$$

Cuando $V$ alcanza cero, el error es cero y no hay más cambio. El modelo asume que un estímulo extinguido ($V = 0$) debe ser funcionalmente idéntico a un estímulo neutral que nunca fue condicionado ($V = 0$).

**Evidencia problemática:** Hay una multitud de reportes que contradicen esta predicción:

**1. Recuperación espontánea:** El mero paso del tiempo produce una reaparición de la respuesta condicionada después de extinción completa. Si se entrena $A+$, se extingue $A$ hasta que no produce respuesta, y luego se deja pasar tiempo sin presentar $A$, la respuesta a $A$ reaparece parcialmente.

**2. Readquisición más rápida:** Estímulos previamente extinguidos adquieren valor predictivo más rápido que estímulos neutrales en readquisición, a pesar de que se supone que ambos inician con $V = 0$.

**3. Renovación contextual:** La extinción es específica al contexto. Si se entrena en contexto 1, se extingue en contexto 2, y se prueba nuevamente en contexto 1, la respuesta reaparece.

**Implicación teórica:** Estos hallazgos sugieren que la extinción no simplemente "borra" el aprendizaje original, reduciendo $V$ a cero. Más bien, la extinción parece ser un proceso de aprendizaje nuevo que coexiste con el aprendizaje original. El organismo retiene información sobre ambas contingencias (reforzamiento y no-reforzamiento) y el contexto determina cuál se expresa.

**Modelos alternativos:** Esta literatura ha generado modelos que distinguen entre aprendizaje de una asociación y su expresión en conducta (Wagner, Bouton), y modelos que representan múltiples memorias contextualizadas en lugar de un solo valor (modelos de contexto, teorías de memoria múltiple).

### Limitación 2: Inhibición Latente

**Protocolo:**
- Grupo Experimental: Fase 1: Presentación de $X$ solo (sin reforzador, 60 ensayos). Fase 2: $X+$ (con reforzador)
- Grupo Control: Solo Fase 2: $X+$

**Predicción del modelo:** En Fase 1, $X$ se presenta sin reforzador. Con $R = 0$ y asumiendo $V_X$ inicia en cero:

$$\Delta V_X = \alpha \beta (0 - 0) = 0$$

No hay cambio en $V_X$—permanece en cero. Al inicio de Fase 2, ambos grupos tienen $V_X = 0$. Por tanto, el modelo predice adquisición idéntica en Fase 2 para ambos grupos.

**Evidencia empírica:** Consistentemente se encuentra que el Grupo Experimental muestra adquisición significativamente más lenta en Fase 2. La preexposición al estímulo sin reforzador retarda el aprendizaje subsecuente—un efecto conocido como inhibición latente.

**Interpretaciones teóricas:** El fenómeno sugiere que algo cambia durante la Fase 1 a pesar de que $V$ permanece en cero. Las interpretaciones principales apelan a:

**1. Atención:** La preexposición reduce la atención asignada al estímulo. Si el parámetro $\alpha$ (que representa asociabilidad) decrece con la exposición no reforzada, el aprendizaje subsecuente será más lento. Esta idea motivó modelos donde $\alpha$ no es constante sino que cambia con la experiencia (Pearce-Hall, Mackintosh).

**2. Comparación de contextos:** El estímulo en Fase 1 se asocia con el contexto de no-reforzamiento. En Fase 2, debe aprender una nueva asociación que compite con la anterior (Bouton).

**Implicación más amplia:** La inhibición latente demuestra que los organismos rastrean más información sobre estímulos que solo su valor predictivo actual. Rastrean historias de reforzamiento, predictabilidad, y confiabilidad. Los modelos puros de "valor único" como Rescorla-Wagner no pueden capturar esta riqueza.

### Limitación 3: Precondicionamiento Sensorial

**Protocolo:**
- Fase 1: Aparear $A$ con $B$ (sin reforzador): $A \rightarrow B$
- Fase 2: Entrenar $B$ con reforzador: $B+$
- Prueba: ¿Produce $A$ respuesta?

**Resultado empírico:** Sí, $A$ produce respuesta a pesar de nunca haber sido apareado directamente con reforzador. El organismo parece haber formado una asociación $A \rightarrow B$ en Fase 1, y cuando $B$ adquiere valor en Fase 2, este valor se "transfiere" a $A$.

**Predicción del modelo:** En Fase 1, sin reforzador:

$$\Delta V_A = \alpha \beta (0 - V_{total}) = -\alpha \beta (V_A + V_B)$$

Si ambos inician en cero, no hay cambio. El modelo no predice formación de asociación $A \rightarrow B$ en ausencia de reforzador. En Fase 2, solo $V_B$ incrementa. En la prueba, $V_A$ permanece en cero y no debería producir respuesta.

**Implicación teórica:** El precondicionamiento sensorial sugiere que los organismos forman asociaciones entre estímulos (relaciones $E \rightarrow E$) independientemente de reforzadores. El modelo de Rescorla-Wagner solo representa relaciones $E \rightarrow R$ (estímulo predice reforzador). Modelos más complejos (SOP de Wagner, redes asociativas) permiten representar relaciones $E \rightarrow E$ además de $E \rightarrow R$.

### Perspectiva sobre las Limitaciones

Es crucial entender estas limitaciones no como fracasos que invalidan el modelo, sino como fronteras que delimitan su dominio de aplicabilidad. El modelo de Rescorla-Wagner captura un aspecto fundamental del aprendizaje: cómo los organismos compiten explicaciones alternativas por resultados observados cuando múltiples predictores están presentes. Esto lo hace excepcionalmente bien.

Sin embargo, los organismos hacen más que esto. Rastrean historias de aprendizaje, ajustan atención dinámicamente, representan estructuras relacionales complejas, y contextualizan memoria. Ningún modelo único puede capturar toda esta complejidad. El progreso científico proviene de entender claramente qué captura cada modelo y qué queda fuera, y de desarrollar iterativamente modelos más comprensivos que conservan las virtudes de sus predecesores mientras expanden su alcance.

---

## Tabla Resumen: El Modelo de Rescorla-Wagner

| Aspecto | Descripción | Fórmula/Valor |
|---------|-------------|---------------|
| **Ecuación Básica** | Actualización de valor de elemento individual | $\Delta V_x = \alpha_x \beta (R - V_{total})$ |
| **Forma Recursiva** | Valor en siguiente ensayo | $V_{x,t+1} = V_{x,t} + \alpha_x \beta (R_t - V_{total,t})$ |
| **Cálculo de V_total** | Suma de valores de todos elementos presentes | $V_{total} = \sum_{i \in presentes} V_i$ |
| **Parámetro α** | Asociabilidad del EC (0 < α < 1) | Fijo por estímulo en modelo original |
| **Parámetro β** | Efectividad del reforzador (0 < β < 1) | Puede diferir entre adquisición/extinción |
| **Error de Predicción** | Motor del aprendizaje, compartido por todos elementos | $\delta = R - V_{total}$ |
| **Rango de Valores** | Permite valores negativos (inhibición) | $-\infty < V < +\infty$ |
| **Punto de Equilibrio** | Cuando no hay más aprendizaje | $V_{total} = R$ |
| **Competencia** | Valor total limitado por R | $\sum V_i \rightarrow R$ |
| **Bloqueo** | Condición para bloqueo completo | $V_{total} = R$ antes de introducir nuevo elemento |
| **Ensombrecimiento** | Razón de valores en equilibrio | $V_A / V_B = \alpha_A / \alpha_B$ |
| **Inhibición** | Valores negativos cuando | Entrenamiento $A+$ seguido de $AB-$ |
| **Sobreexpectación** | Reducción cuando | $V_{total} > R$ |

**Nota:** La diferencia clave con Bush-Mosteller: el error se calcula como $(R - V_{total})$ en lugar de $(R - V_x)$, introduciendo competencia entre elementos.

---

## Conceptos Clave y Síntesis

Este capítulo ha presentado el modelo de Rescorla-Wagner, una extensión conceptualmente simple pero profundamente poderosa del modelo de Bush-Mosteller que resuelve el problema computacional de asignar crédito entre múltiples predictores competidores de un mismo reforzador.

La innovación central del modelo consiste en calcular el error de predicción que impulsa el aprendizaje no comparando el reforzador con el valor del estímulo individual, sino con la suma de los valores de todos los estímulos presentes. Esta modificación aparentemente menor—reemplazar $V_x$ por $V_{total}$ en la ecuación de actualización—tiene consecuencias profundas: introduce competencia automática entre elementos por un presupuesto limitado de valor predictivo determinado por la magnitud del reforzador.

El modelo se basa en cinco supuestos formales: separabilidad de estímulos compuestos en elementos, valores predictivos que pueden ser positivos (excitatorios) o negativos (inhibitorios), suma aritmética simple para integrar valores de múltiples elementos, actualización basada en el error calculado contra $V_{total}$, y competencia emergente entre elementos. Estos supuestos, combinados con la ecuación de actualización, generan predicciones cuantitativas para fenómenos empíricos clave.

Vimos cómo el bloqueo, ensombrecimiento, inhibición condicionada y sobreexpectación no son fenómenos independientes que requieren explicaciones separadas, sino consecuencias matemáticas necesarias del mecanismo de competencia. El bloqueo ocurre cuando $V_{total}$ ya alcanza $R$ antes de introducir un nuevo elemento, eliminando el error de predicción disponible para asignarse al elemento nuevo. El ensombrecimiento resulta de que elementos con diferentes asociabilidades ($\alpha$) aprenden a diferentes velocidades del mismo error compartido, con elementos más salientes capturando mayor proporción del valor total. La inhibición condicionada emerge cuando un elemento se presenta en compuesto con un excitador en ausencia de reforzador, generando errores de predicción negativos que impulsan el valor del elemento hacia valores negativos que predicen ausencia de reforzador. La sobreexpectación demuestra que cuando la suma de valores excede el reforzador disponible, todos los valores deben reducirse para corregir la sobreestimación.

Las limitaciones del modelo—su incapacidad para explicar recuperación espontánea después de extinción, inhibición latente por preexposición, y precondicionamiento sensorial—no representan fracasos sino fronteras que delimitan su dominio de aplicabilidad. Estas limitaciones han motivado extensiones importantes: modelos donde la asociabilidad ($\alpha$) cambia dinámicamente con la experiencia (Pearce-Hall, Mackintosh), teorías que distinguen entre aprendizaje de asociaciones y su expresión contextualizada (Bouton, Wagner), y modelos que representan relaciones entre estímulos además de relaciones estímulo-reforzador (redes asociativas, SOP).

La influencia del modelo de Rescorla-Wagner se extiende mucho más allá de la psicología del aprendizaje animal. En neurociencia, el descubrimiento de que neuronas dopaminérgicas codifican errores de predicción al estilo Rescorla-Wagner vincula el modelo con mecanismos neurales específicos. En aprendizaje automático, los algoritmos de temporal-difference learning que subyacen al aprendizaje por refuerzo moderno son extensiones directas del principio de error de predicción. En psicología clínica, la comprensión de extinción como aprendizaje nuevo en lugar de olvido ha transformado el tratamiento de trastornos de ansiedad mediante terapias de exposición basadas en aprendizaje inhibitorio.

Quizás la contribución conceptual más profunda del modelo es su reconceptualización del aprendizaje. En lugar de ver el aprendizaje como registro pasivo de contigüidades, el modelo lo concibe como proceso activo de construcción de modelos predictivos del mundo. Los organismos no simplemente asocian estímulos con resultados—extraen estructura causal de experiencias complejas, compitiendo explicaciones alternativas unas contra otras, actualizando creencias basándose en discrepancias entre predicciones y resultados. Esta visión del aprendizaje como inferencia sobre estructura causal ha demostrado ser extraordinariamente fructífera y continúa guiando la investigación contemporánea en múltiples disciplinas.

---

## Lecturas Recomendadas

### Artículo Original

- Rescorla, R. A., & Wagner, A. R. (1972). "A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement." En A. H. Black & W. F. Prokasy (Eds.), *Classical Conditioning II: Current Research and Theory* (pp. 64-99). Appleton-Century-Crofts. [El artículo original—lectura esencial para estudiantes serios]

### Revisiones y Síntesis

- Miller, R. R., Barnet, R. C., & Grahame, N. J. (1995). "Assessment of the Rescorla-Wagner model." *Psychological Bulletin*, 117(3), 363-386. [Evaluación comprehensiva de éxitos y limitaciones del modelo]

- Siegel, S., & Allan, L. G. (1996). "The widespread influence of the Rescorla-Wagner model." *Psychonomic Bulletin & Review*, 3(3), 314-321. [Impacto del modelo en múltiples áreas]

- Rescorla, R. A. (1988). "Pavlovian conditioning: It's not what you think it is." *American Psychologist*, 43(3), 151-160. [Revisión accesible por el propio Rescorla]

### Evidencia Empírica Clave

**Bloqueo:**
- Kamin, L. J. (1968). "'Attention-like' processes in classical conditioning." En M. R. Jones (Ed.), *Miami Symposium on the Prediction of Behavior: Aversive Stimulation* (pp. 9-31). University of Miami Press. [El descubrimiento original del bloqueo]

**Sobreexpectación:**
- Kremer, E. F. (1978). "The Rescorla-Wagner model: Losses in associative strength in compound conditioned stimuli." *Journal of Experimental Psychology: Animal Behavior Processes*, 4(1), 22-36. [Demostración de sobreexpectación]

- Rescorla, R. A. (2006). "Deepened extinction from compound stimulus presentation." *Journal of Experimental Psychology: Animal Learning and Cognition*, 32(2), 135-144. [Evidencia moderna]

**Inhibición Latente:**
- Lubow, R. E., & Moore, A. U. (1959). "Latent inhibition: The effect of nonreinforced pre-exposure to the conditional stimulus." *Journal of Comparative and Physiological Psychology*, 52(4), 415-419. [Descubrimiento original del fenómeno]

**Contingencia:**
- Rescorla, R. A. (1968). "Probability of shock in the presence and absence of CS in fear conditioning." *Journal of Comparative and Physiological Psychology*, 66(1), 1-5. [Demostración clásica de que la contigüidad no es suficiente]

### Modelos Alternativos y Extensiones

- Pearce, J. M., & Hall, G. (1980). "A model for Pavlovian learning: Variations in the effectiveness of conditioned but not of unconditioned stimuli." *Psychological Review*, 87(6), 532-552. [Modelo donde α (atencionalidad) cambia con experiencia]

- Mackintosh, N. J. (1975). "A theory of attention: Variations in the associability of stimuli with reinforcement." *Psychological Review*, 82(4), 276-298. [α depende de qué tan buen predictor es el estímulo relativo a otros]

- Wagner, A. R. (1981). "SOP: A model of automatic memory processing in animal behavior." En N. E. Spear & R. R. Miller (Eds.), *Information Processing in Animals: Memory Mechanisms* (pp. 5-47). Erlbaum. [Modelo con dinámica temporal dentro de ensayos]

- Le Pelley, M. E. (2004). "The role of associative history in models of associative learning: A selective review and a hybrid model." *Quarterly Journal of Experimental Psychology*, 57B(3), 193-243. [Integración de modelos de atención]

### Neurociencia e Implementación

- Schultz, W., Dayan, P., & Montague, P. R. (1997). "A neural substrate of prediction and reward." *Science*, 275(5306), 1593-1599. [Neuronas dopaminérgicas codifican errores de predicción al estilo R-W]

- Niv, Y., & Schoenbaum, G. (2008). "Dialogues on prediction errors." *Trends in Cognitive Sciences*, 12(7), 265-272. [Puente entre modelos computacionales y neurobiología]

- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. [Capítulos 6-7: TD-learning como extensión de R-W; disponible gratis en línea]

### Aplicaciones Clínicas

- Craske, M. G., Treanor, M., Conway, C. C., Zbozinek, T., & Vervliet, B. (2014). "Maximizing exposure therapy: An inhibitory learning approach." *Behaviour Research and Therapy*, 58, 10-23. [Aplicación de principios de aprendizaje asociativo a tratamiento de ansiedad]

- Bouton, M. E. (2002). "Context, ambiguity, and unlearning: Sources of relapse after behavioral extinction." *Biological Psychiatry*, 52(10), 976-986. [Relevancia de contexto para extinción clínica]

- Bouton, M. E. (2016). *Learning and Behavior: A Contemporary Synthesis* (2nd ed.). Sinauer Associates. [Capítulos 4-5: Contexto moderno del modelo]

### Textos de Referencia

- Pearce, J. M. (2008). *Animal Learning and Cognition: An Introduction* (3rd ed.). Psychology Press. [Capítulos 3-5: Tratamiento comprehensivo de R-W y alternativas]

- Domjan, M. (2014). *The Principles of Learning and Behavior* (7th ed.). Cengage Learning. [Capítulo 4: Introducción pedagógica a modelos de condicionamiento]

- Mackintosh, N. J. (1974). *The Psychology of Animal Learning*. Academic Press. [Tratamiento clásico comprehensivo de teorías asociativas]

### Recursos Computacionales

- McLaren, I. P. L., & Mackintosh, N. J. (2000). "An elemental model of associative learning: I. Latent inhibition and perceptual learning." *Animal Learning & Behavior*, 28(3), 211-246. [Implementación computacional detallada]

- *Sniffy, the Virtual Rat* (software educativo para simular R-W)
- Código Python disponible en: https://github.com/SussilloDavid/rw-model

---

## Ejercicios

### Ejercicios Conceptuales

**1. De Bush-Mosteller a Rescorla-Wagner: Análisis de la Modificación Crítica**

La diferencia entre Bush-Mosteller y Rescorla-Wagner es el cambio de $(R - V_x)$ a $(R - V_{total})$ en el cálculo del error de predicción.

a) Explique conceptualmente por qué este cambio introduce competencia entre elementos. Use un ejemplo concreto de dos estímulos $A$ y $B$ presentes simultáneamente, donde $V_A = 0.6$, $V_B = 0.3$, y $R = 1$. Calcule el error de predicción bajo ambos modelos y explique cómo las actualizaciones difieren.

b) Demuestre algebraicamente que si solo un elemento está presente, Rescorla-Wagner reduce exactamente a Bush-Mosteller. ¿Qué implica esto sobre la relación entre los modelos? ¿Es R-W una "extensión" o un "reemplazo" de B-M?

c) El cambio de $V_x$ a $V_{total}$ puede interpretarse como que el sistema calcula un "error global" en lugar de "errores locales" para cada elemento. Discuta las ventajas y desventajas computacionales de cada enfoque. ¿Bajo qué condiciones ambientales sería ventajoso usar errores locales versus un error global?

**2. Separabilidad de Estímulos: Implicaciones y Límites**

El supuesto de separabilidad establece que estímulos compuestos se procesan como conjuntos de elementos independientes.

a) Considere tres niveles posibles de descomposición para un rostro: (i) características visuales elementales (bordes verticales, horizontales, colores), (ii) partes faciales (ojos, nariz, boca), (iii) configuraciones holísticas ("rostro amenazante", "rostro familiar"). ¿A qué nivel predice el modelo que ocurre la separabilidad? ¿Cómo podría diseñar un experimento para determinar empíricamente el nivel apropiado de descomposición?

b) El fenómeno de "configuración" sugiere que a veces estímulos compuestos se tratan como unidades únicas que no se reducen a sus elementos. Por ejemplo, un compuesto $AB$ podría tratarse como un tercer elemento $C$ en lugar de la suma de $A$ y $B$. ¿Cómo modificaría el modelo para permitir tanto procesamiento elemental como configuracional? Proponga una regla específica que determine cuándo usar cada modo.

c) En música, una melodía no es solo la suma de notas individuales—la relación temporal y armónica entre notas importa. ¿El supuesto de separabilidad y suma lineal de Rescorla-Wagner puede capturar aprendizaje musical? Si no, ¿qué estructura matemática alternativa se requeriría?

**3. Inhibición Condicionada: Mecanismos y Pruebas**

Rescorla propuso dos pruebas para determinar si un estímulo es inhibitorio: sumación y retardo.

a) Explique por qué ni la prueba de sumación ni la de retardo son suficientes por sí solas para concluir que un estímulo es inhibitorio. Para cada prueba, proponga una explicación alternativa basada en atención (novedad/habituación) que podría producir el mismo patrón de resultados. ¿Por qué pasar ambas pruebas descarta estas explicaciones alternativas?

b) Diseñe un protocolo experimental completo para crear un inhibidor condicionado $X$ y verificar que pasa ambas pruebas. Especifique: (i) fases de entrenamiento con número de ensayos, (ii) grupos control apropiados, (iii) procedimientos de prueba, (iv) predicciones cuantitativas del modelo para cada grupo.

c) El modelo permite valores arbitrariamente negativos ($V \rightarrow -\infty$ en principio). ¿Existe un límite funcional para qué tan negativo puede ser un inhibidor? Considere: ¿Qué significaría biológicamente un valor de $V = -1000$? ¿Hay restricciones prácticas que limitarían valores extremos?

**4. Análisis Crítico de Limitaciones del Modelo**

El modelo no puede explicar recuperación espontánea, inhibición latente, y precondicionamiento sensorial.

a) Para cada limitación, identifique qué supuesto específico del modelo es violado por la evidencia empírica. Por ejemplo, ¿es el supuesto de que $V$ es un solo número en lugar de múltiples memorias? ¿El supuesto de que $\alpha$ es constante? Sea específico.

b) Compare las tres limitaciones en términos de qué tan "fatal" son para el modelo. ¿Alguna podría resolverse con modificaciones menores? ¿Alguna requiere reconceptualización fundamental? Ordénelas de menos a más problemática y justifique su ranking.

c) Rescorla & Wagner sabían del fenómeno de inhibición latente cuando formularon su modelo. ¿Por qué cree que eligieron publicar un modelo que no lo explicaba? Discuta el trade-off entre simplicidad/elegancia matemática versus cobertura empírica comprehensiva en la construcción de modelos científicos.

**5. Competencia vs. Cooperación entre Elementos**

El modelo asume competencia (suma de valores limitada por $R$), pero podría imaginarse un modelo cooperativo.

a) Proponga un "modelo cooperativo" alternativo donde elementos en compuesto se facilitan mutuamente en lugar de competir. Especifique matemáticamente cómo cambiaría la ecuación de actualización. ¿Qué predicciones generaría este modelo para bloqueo y ensombrecimiento?

b) En el mundo real, ¿hay situaciones donde esperaríamos cooperación en lugar de competencia? Considere: (i) elementos que son componentes funcionales de una acción compleja (ej. músculos que deben coordinarse), (ii) señales multimodales redundantes en ambientes ruidosos. ¿Sería adaptativo un mecanismo cooperativo en estos casos?

c) Diseñe un experimento crítico que podría distinguir entre competencia verdadera (predicción de R-W) versus independencia simple (predicción de B-M) versus cooperación (su modelo del inciso a). Especifique medidas y patrón de resultados para cada hipótesis.

### Ejercicios Cuantitativos

**6. Simulación Manual de Bloqueo** [★★☆ Intermedio]

Simule el protocolo de bloqueo de Kamin paso a paso.

**Fase 1:** Elemento $A$ solo → Reforzador ($R = 1$)  
**Fase 2:** Compuesto $AB$ → Reforzador ($R = 1$)

Use parámetros: $\alpha_A = 0.3$, $\alpha_B = 0.3$, $\beta = 1$, $V_A(0) = V_B(0) = 0$.

a) Calcule manualmente $V_A$ para los primeros 5 ensayos de Fase 1. Muestre todos los cálculos usando $\Delta V_A = \alpha_A \beta (R - V_A)$. ¿Cuántos ensayos se requieren para que $V_A > 0.95$?

b) Usando el valor final de $V_A$ de la Fase 1, calcule $V_A$ y $V_B$ para los primeros 5 ensayos de Fase 2. Use $V_{total} = V_A + V_B$ para calcular el error. ¿Qué observa sobre $\Delta V_B$?

c) Derive la solución analítica para $V_A(t)$ durante la Fase 1 (ver Capítulo 10 para método). Use esta solución para determinar exactamente en qué ensayo $V_A$ alcanza 0.99. Compare con una simulación numérica iterativa.

d) Si el bloqueo no fuera perfecto y $V_A$ al final de Fase 1 fuera solo 0.8 (en lugar de $\approx 1$), ¿qué valor final alcanzaría $V_B$ en Fase 2? Derive esta respuesta usando la condición de equilibrio $V_A + V_B = R = 1$.

**7. Análisis Cuantitativo de Ensombrecimiento** [★★★ Avanzado]

Dos elementos $A$ y $B$ se entrenan en compuesto desde el inicio.

$\alpha_A = 0.4$, $\alpha_B = 0.2$, $\beta = 1$, $R = 1$, $V_A(0) = V_B(0) = 0$.

a) Derive las ecuaciones diferenciales acopladas que gobiernan la evolución de $V_A$ y $V_B$:

$$V_{A,t+1} = V_{A,t} + \alpha_A \beta (R - V_{A,t} - V_{B,t})$$
$$V_{B,t+1} = V_{B,t} + \alpha_B \beta (R - V_{A,t} - V_{B,t})$$

Calcule manualmente los primeros 3 ensayos mostrando todos los pasos.

b) En equilibrio, ambos elementos dejan de cambiar. Use esto para derivar:
   - La condición $V_A + V_B = R$
   - La razón $V_A / V_B = \alpha_A / \alpha_B$
   
   Resuelva el sistema para obtener $V_A^*$ y $V_B^*$ en función de $\alpha_A$, $\alpha_B$, y $R$. Verifique numéricamente con los valores dados.

c) Grafique en el espacio 2D $(V_A, V_B)$ las siguientes curvas:
   - Isoclina nula de $A$: puntos donde $\Delta V_A = 0$
   - Isoclina nula de $B$: puntos donde $\Delta V_B = 0$
   - Trayectorias desde $(0,0)$ hacia el equilibrio
   - La recta $V_A + V_B = 1$

¿Dónde se intersectan las isoclinas? ¿Todas las trayectorias convergen al mismo punto?

d) Si $\alpha_A = \alpha_B$ (elementos igualmente salientes), ¿qué predice el modelo sobre $V_A$ vs $V_B$ en equilibrio? ¿Sigue habiendo ensombrecimiento? Explique la dependencia en condiciones iniciales cuando las saliencias son iguales.

**8. Inhibición Condicionada: Cálculos Numéricos** [★★☆ Intermedio]

Protocolo: Entrenamiento discriminativo
- Ensayos $A+$: $A$ solo → Reforzador ($R = 1$)
- Ensayos $AB-$: Compuesto $AB$ → Sin reforzador ($R = 0$)
- Proporción: 50% ensayos $A+$, 50% ensayos $AB-$ (intercalados aleatoriamente)

Parámetros: $\alpha_A = \alpha_B = 0.2$, $\beta_+ = 1.0$ (adquisición), $\beta_- = 0.5$ (extinción).

a) Simule 20 ensayos (10 de cada tipo, alternando). Calcule $V_A$ y $V_B$ después de cada ensayo. Grafique ambos valores versus número de ensayo. ¿Convergen a un equilibrio estable?

b) Derive los valores de equilibrio teóricos. En equilibrio, el cambio promedio debe ser cero:

$$E[\Delta V_A] = 0.5 \cdot \alpha_A \beta_+ (1 - V_A) + 0.5 \cdot \alpha_A \beta_- (0 - V_A - V_B) = 0$$
$$E[\Delta V_B] = 0.5 \cdot \alpha_B \beta_- (0 - V_A - V_B) = 0$$

Resuelva para $V_A^*$ y $V_B^*$. Compare con los valores asintóticos de su simulación.

c) ¿Qué sucede si $\beta_+ = \beta_-$ (misma tasa de aprendizaje para reforzamiento y no-reforzamiento)? Recalcule equilibrios. ¿Cómo afecta la asimetría en betas al grado de inhibición de $B$?

d) Realice las dos pruebas de inhibición:
   - **Sumación:** Calcule respuesta esperada a un nuevo excitador $C$ con $V_C = 0.8$ solo, versus compuesto $BC$
   - **Retardo:** Simule ensayos $B+$ empezando desde el valor inhibitorio que alcanzó. ¿Cuántos ensayos para alcanzar $V_B = 0.5$? Compare con entrenar un estímulo neutral nuevo.

**9. Sobreexpectación: Análisis Formal** [★★★ Avanzado]

Fase 1: Entrenar $A+$ y $B+$ por separado hasta convergencia ($V_A \approx V_B \approx 1$)  
Fase 2: Presentar compuesto $AB+$

a) Derive matemáticamente que en la Fase 2, el error de predicción es negativo:

$$\delta = R - V_{total} = 1 - (V_A + V_B) < 0 \text{ cuando } V_A + V_B > 1$$

¿Cuál es el error en el primer ensayo de Fase 2 si ambos valores inician exactamente en 1?

b) Simule la Fase 2 con parámetros $\alpha_A = \alpha_B = 0.3$, $\beta = 1$, iniciando con $V_A = V_B = 1$. Calcule 10 ensayos. ¿A qué valores convergen $V_A$ y $V_B$? ¿Suma a $R = 1$ como predice la teoría?

c) Incluya un grupo control que en Fase 2 continúa recibiendo $A+$ y $B+$ por separado (no compuesto). Compare los valores finales de $V_A$ en ambos grupos. Este es el efecto crítico de sobreexpectación: el compuesto reduce valores por debajo de lo que se mantiene con entrenamiento separado.

d) Algunos investigadores argumentan que sobreexpectación es una predicción "antiintuitiva" del modelo. ¿Por qué? Desde una perspectiva de optimización Bayesiana, ¿es realmente sorprendente que valores se reduzcan cuando hay evidencia de que la suma sobrepredice? Discuta desde perspectiva normativa.

**10. Contingencia versus Contigüidad: Experimento de Rescorla (1968)** [★★★ Avanzado]

Rescorla manipuló $P(shock|tone)$ y $P(shock|no-tone)$ independientemente en miedo condicionado con ratas.

Condición 1: $P(shock|tone) = 0.4$, $P(shock|no-tone) = 0.1$ (Contingencia positiva)  
Condición 2: $P(shock|tone) = 0.4$, $P(shock|no-tone) = 0.4$ (Sin contingencia, solo contigüidad)

a) Para la Condición 1, en 100 ensayos esperamos: 40% con tono (40 ensayos), 60% sin tono (60 ensayos). De los 40 con tono, 40% (16) tienen shock. De los 60 sin tono, 10% (6) tienen shock. El tono está presente en 16 de 22 shocks totales (73%). ¿Esperaría aprendizaje según Bush-Mosteller? ¿Según Rescorla-Wagner?

b) Modele la Condición 2 usando Rescorla-Wagner incluyendo el contexto como elemento. Ensayos son: (i) TONO+CONTEXTO → shock ($R=1$), (ii) TONO+CONTEXTO → nada ($R=0$), (iii) CONTEXTO solo → shock ($R=1$), (iv) CONTEXTO solo → nada ($R=0$), cada uno con probabilidades apropiadas.

Ejecute simulación con $\alpha_{tono} = 0.3$, $\alpha_{context} = 0.1$, $\beta = 1$. Después de 100 ensayos, ¿qué valor tiene el tono? ¿El contexto?

c) Compare $V_{tono}$ final entre Condición 1 y Condición 2. El modelo debe predecir valores similares (porque contigüidades similares) o diferentes (porque contingencias diferentes)? Verifique con sus simulaciones.

d) Rescorla encontró que solo la Condición 1 produce miedo al tono; Condición 2 no. ¿Sus simulaciones capturan este resultado? Si el contexto en Condición 2 alcanza valor alto, ¿cómo "bloquea" el aprendizaje al tono?

### Ejercicios Aplicados

**11. Aplicación Clínica: Terapia de Exposición para Fobia** [★★☆ Intermedio]

Un paciente tiene fobia a perros desarrollada después de ser mordido. Tiene miedo tanto a perros grandes como a parques (contexto donde ocurrió el incidente).

Usando Rescorla-Wagner, modele:
- $V_{perros} = 0.9$ (alto miedo)
- $V_{parque} = 0.6$ (miedo moderado al contexto)

a) Protocolo tradicional de exposición: presentar perros en la clínica (contexto diferente) sin consecuencia aversiva. Modele 20 ensayos de PERRO+CLÍNICA → $R=0$. Asuma $\alpha_{perro} = 0.3$, $\alpha_{clínica} = 0.1$, $\beta = 0.4$ (extinción).

Calcule $V_{perro}$ y $V_{clínica}$ finales. ¿El miedo a perros se extingue?

b) Problema de renovación contextual: después de extinción en clínica, el paciente ve un perro en un parque. ¿Qué predice el modelo? Use $V_{perro}$ de (a) y $V_{parque} = 0.6$ (no cambió). Calcule $V_{total}$ en contexto parque.

c) Protocolo mejorado: exposición en múltiples contextos. Modele extinción alternando PERRO+CLÍNICA y PERRO+PARQUE. ¿Cómo afecta esto a $V_{parque}$? ¿Reduce renovación contextual?

d) El modelo predice que la extinción no "borra" el aprendizaje original (limitación de recuperación espontánea). Proponga una intervención adicional basada en aprendizaje inhibitorio: crear un inhibidor condicionado que el paciente pueda usar. ¿Qué elemento usaría como inhibidor y cómo lo entrenaría?

**12. Publicidad y Asociaciones de Marca** [★★★ Avanzado]

Una compañía quiere asociar su marca (M) con sentimientos positivos usando celebridades (C) en anuncios.

**Situación inicial:**
- Celebridad ya es muy popular: $V_C = 0.9$
- Marca es neutral: $V_M = 0$
- Reacción positiva esperada del consumidor: $R = 1$

a) Estrategia 1: Anuncios mostrando MARCA+CELEBRIDAD juntos. Modele 10 exposiciones con $\alpha_M = 0.2$, $\alpha_C = 0.3$, $\beta = 0.8$. ¿Qué valor alcanza la marca?

¿Por qué este valor es menor que $R = 1$? Explique en términos de bloqueo.

b) Estrategia 2: Introducir progresivamente. Primero, 5 exposiciones de CELEBRIDAD sola (para mantener $V_C$ alto). Luego, 10 exposiciones de MARCA+CELEBRIDAD. Luego, 5 exposiciones de MARCA sola (para probar valor adquirido).

Modele la secuencia completa. ¿La marca alcanza valor más alto que en Estrategia 1?

c) Problema de sobre-exposición: si la celebridad aparece en demasiados productos, su valor predictivo se "diluye". Modele: CELEBRIDAD aparece con MARCA-A (su producto), MARCA-B (competidor 1), MARCA-C (competidor 2), cada uno con $R = 1$ y misma frecuencia.

¿Qué valores finales alcanzan cada marca? Compare con caso donde celebridad es exclusiva de MARCA-A.

d) Escándalo de celebridad: después de que $V_C = 0.9$, la celebridad tiene escándalo y $R$ cambia a 0 (o negativo). ¿Cómo afecta esto a $V_M$? Si los valores estaban correlacionados (compuesto), ¿la marca sufre "contagio" negativo? Modele 10 exposiciones post-escándalo.

**13. Diseño de Sistema de Recomendación con Competencia** [★★★ Avanzado]

Un sistema de recomendación de películas debe aprender preferencias de usuario basándose en características de películas (géneros, actores, directores).

Película = compuesto de características: {Ciencia-Ficción, Tom-Cruise, Acción}

**Usuario califica películas:**
- "Edge of Tomorrow" (Sci-Fi, Tom-Cruise, Acción) → Calificación 5/5 ($R = 1$)
- "Minority Report" (Sci-Fi, Tom-Cruise, Thriller) → Calificación 5/5 ($R = 1$)
- "Top Gun" (Acción, Tom-Cruise, Drama) → Calificación 3/5 ($R = 0.6$)
- "Inception" (Sci-Fi, Acción, Christopher-Nolan) → Calificación 5/5 ($R = 1$)

a) Use Rescorla-Wagner para actualizar valores de cada característica después de cada calificación. Asuma todas las $\alpha = 0.2$, $\beta = 1$, valores iniciales en 0.

Calcule $V_{Sci-Fi}$, $V_{Tom-Cruise}$, $V_{Acción}$, $V_{Thriller}$, $V_{Drama}$, $V_{Nolan}$ después de las 4 películas.

b) Prediga la calificación esperada para una nueva película:
- "Oblivion" (Sci-Fi, Tom-Cruise) → $V_{total} = ?$
- "The Avengers" (Acción, Sci-Fi, [nuevo-director]) → $V_{total} = ?$

Compare con enfoque de Bush-Mosteller donde cada característica se actualiza independientemente. ¿Qué diferencia hace la competencia?

c) El sistema nota que el usuario calificó 10 películas de Sci-Fi altamente. ¿Habrá "bloqueo" donde el género Sci-Fi captura todo el valor y no aprende sobre actores/directores específicos? ¿Cómo podría ajustar parámetros $\alpha$ para balancear aprendizaje entre niveles de características (género vs actor)?

d) Fenómeno de "filter bubble": si el sistema solo recomienda películas con $V_{total}$ alto, el usuario solo ve Sci-Fi. Esto refuerza $V_{Sci-Fi}$ aún más, creando ciclo de retroalimentación. Proponga una modificación al algoritmo que introduzca exploración ocasional de características con valores bajos. Use concepto de ε-greedy o softmax del Capítulo 10.

**14. Análisis de Caso: Supersticiones en Deportes** [★★☆ Intermedio]

Un bateador de béisbol desarrolla ritual de tocar su casco tres veces antes de cada turno al bate. Comenzó este ritual después de un juego excepcional.

a) Modele el desarrollo de esta "superstición" usando Rescorla-Wagner. El compuesto es {HABILIDAD, RITUAL} y el resultado es éxito al batear ($R = 1$ para hit, $R = 0$ para out).

Asuma que HABILIDAD ya tiene $V_{hab} = 0.7$ (es buen bateador). En el juego donde comenzó el ritual, tuvo éxito: HABILIDAD+RITUAL → Hit ($R = 1$).

¿Qué predice el modelo sobre $V_{ritual}$ después de 1 ensayo? ¿Y después de 50 ensayos con 70% de hits (consistente con su habilidad real)?

b) ¿Por qué el ritual no es "bloqueado" completamente por la habilidad preexistente? (Pista: $V_{hab} < R$, así que hay error de predicción residual disponible).

Compare con caso donde $V_{hab} = 1.0$ (bateador perfecto). ¿Se desarrollaría la superstición?

c) Ahora el jugador tiene racha mala (50% hits en lugar de 70%). El ritual está presente en todos los intentos. ¿Cómo cambia $V_{ritual}$ y $V_{hab}$? Modele 20 turnos con $R = 1$ en 50% aleatorio.

¿El modelo predice que el jugador abandonará el ritual (cuando $V_{ritual}$ se vuelve negativo) o lo mantendrá?

d) Fenómeno real: muchos atletas mantienen rituales a pesar de que racionalmente saben que no son causales. Discuta por qué Rescorla-Wagner (modelo normativo de inferencia causal) no captura este comportamiento. ¿Qué factores psicológicos adicionales (aversión al riesgo, costo de omisión, sesgos confirmatorios) explicarían persistencia de supersticiones?

---

**Fin del Capítulo 11**
