# CAPÍTULO X
# PROGRAMAS DE REFORZAMIENTO Y ELECCIÓN

---

## INTRODUCCIÓN

En los Capítulos 8 a 11, estudiamos cómo los organismos aprenden relaciones causales entre eventos en su entorno: qué estímulos predicen refuerzos (Capítulos 8-9) y cómo se forman asociaciones estímulo-consecuencia a través del condicionamiento (Capítulos 10-11). El modelo de Rescorla-Wagner nos mostró cómo los valores asociativos V(E,O) se actualizan con la experiencia, permitiendo a los organismos anticipar eventos biológicamente relevantes.

Sin embargo, conocer que un estímulo predice un refuerzo es solo parte del problema adaptativo que enfrentan los organismos. El problema complementario—igualmente fundamental—es cómo traducir ese conocimiento en distribuciones óptimas de acción. Un organismo puede saber perfectamente que la respuesta R₁ produce r₁ refuerzos por minuto y que R₂ produce r₂ refuerzos por minuto. Pero ¿cuántas respuestas debe asignar a cada opción? ¿Cuánto tiempo dedicar a cada alternativa? ¿Debe responder exclusivamente a la opción más rica, o distribuir sus respuestas proporcionalmente?

Este capítulo aborda precisamente estas cuestiones, estudiando cómo los programas de reforzamiento—las reglas que especifican qué respuestas producen refuerzos—controlan la distribución temporal y numérica del comportamiento. Comenzaremos examinando los programas simples como funciones de retroalimentación que relacionan respuestas con refuerzos. Luego analizaremos la ecuación de Herrnstein, que proporciona una formalización cuantitativa de cómo el refuerzo controla la tasa de respuesta. Posteriormente estudiaremos situaciones de elección recurrente donde múltiples opciones están disponibles simultáneamente, revelando el fenómeno de igualación: los organismos distribuyen sus respuestas proporcionalmente a los refuerzos obtenidos. Finalmente, examinaremos diferentes interpretaciones teóricas de este fenómeno—maximización global versus igualación de tasas locales—y el papel crítico que juega la estructura temporal de los programas de reforzamiento.

La comprensión de estos mecanismos no solo completa nuestra visión de cómo el refuerzo controla el comportamiento, sino que establece los fundamentos para analizar, en capítulos posteriores, modelos más sofisticados de optimización conductual y aprendizaje por refuerzo en ambientes dinámicos.

---

## PARTE 1: PROGRAMAS DE REFORZAMIENTO COMO FUNCIONES DE RETROALIMENTACIÓN

### De Thorndike a Skinner: El Estudio Sistemático del Reforzamiento

La investigación experimental del efecto del refuerzo sobre el comportamiento tiene sus raíces en los estudios pioneros de Edward Thorndike a finales del siglo XIX. En su famosa "caja problema", Thorndike observó que los gatos aprendían gradualmente a escapar mediante respuestas que producían consecuencias favorables—una observación que formalizó como la Ley del Efecto. Sin embargo, fue Clark Hull quien, en las décadas de 1930 y 1940, intentó por primera vez una formulación matemática rigurosa de cómo el refuerzo afecta la "fuerza del hábito". Hull propuso que cada refuerzo incrementaba la asociación estímulo-respuesta de forma acumulativa, pero su formulación enfrentaba serias dificultades empíricas.

El cambio fundamental vino con B.F. Skinner, quien en su libro *The Behavior of Organisms* (1938) introdujo una perspectiva radicalmente diferente. En lugar de conceptualizar el refuerzo como algo que fortalece asociaciones internas (el enfoque de Hull), Skinner propuso estudiar las **relaciones funcionales** entre el comportamiento observable y sus consecuencias ambientales. Este cambio de perspectiva—del "dentro del organismo" al "organismo en su ambiente"—permitió un análisis cuantitativo más directo de cómo diferentes contingencias de refuerzo controlan el comportamiento.

Skinner desarrolló el protocolo experimental que dominaría las siguientes décadas de investigación: la **cámara operante** (posteriormente llamada "caja de Skinner"). En su versión más común, una rata o paloma se encuentra en un ambiente controlado con un manipulandum (palanca o disco iluminado) y un dispositivo dispensador de reforzadores (comida o agua). El experimentador programa las contingencias que determinan qué respuestas producirán refuerzo, y el equipo automático registra con precisión el número y temporalización de las respuestas. Esta tecnología experimental permitió el análisis cuantitativo sistemático de cómo diferentes **programas de reforzamiento**—las reglas que especifican qué respuestas se refuerzan—controlan patrones específicos de comportamiento.

### Los Cuatro Programas Básicos de Reforzamiento

Skinner identificó cuatro programas básicos que han sido objeto de análisis intensivo durante más de ochenta años. Estos programas difieren en dos dimensiones: (1) si el criterio para reforzamiento se basa en el **número de respuestas** (programas de razón) o en el **tiempo transcurrido** (programas de intervalo), y (2) si el requisito es **fijo** (constante de ensayo a ensayo) o **variable** (cambiante impredeciblemente):

**1. Razón Fija (RF):** Se refuerza cada n-ésima respuesta. Por ejemplo, RF 10 significa que cada décima respuesta produce refuerzo. Este programa genera tasas de respuesta muy altas con pausas características después de cada refuerzo ("pausa post-refuerzo"). Ejemplos cotidianos incluyen trabajo a destajo: un cosechador que recibe pago por cada caja de fruta recolectada responde bajo un programa de razón.

**2. Razón Variable (RV):** El número de respuestas requeridas para refuerzo varía impredeciblemente alrededor de un promedio. RV 50 significa que en promedio se requieren 50 respuestas por refuerzo, pero en una ocasión pueden ser 30, en otra 70, etc. Este programa produce las tasas de respuesta más altas y sostenidas de todos los programas básicos, sin pausas post-refuerzo. Las máquinas tragamonedas operan bajo programas de razón variable.

**3. Intervalo Fijo (IF):** Se refuerza la primera respuesta que ocurre después de que ha transcurrido un período fijo de tiempo desde el último refuerzo. IF 60-seg significa que después de cada refuerzo, debe pasar al menos 60 segundos antes de que otra respuesta pueda ser reforzada. Este programa genera un patrón característico de "festón": pausa post-refuerzo seguida de aceleración progresiva conforme se aproxima el momento de disponibilidad del refuerzo. Muchas situaciones cotidianas involucran contingencias de intervalo fijo: revisar el horno durante la cocción, verificar el correo que llega a una hora determinada.

**4. Intervalo Variable (IV):** El tiempo requerido desde el último refuerzo hasta que el siguiente está disponible varía impredeciblemente alrededor de un promedio. IV 60-seg significa que en promedio transcurren 60 segundos entre refuerzos disponibles, pero el intervalo específico varía de ensayo a ensayo. Este programa produce tasas de respuesta moderadas y muy estables, sin pausas post-refuerzo. La pesca es un ejemplo aproximado: los peces muerden a intervalos impredecibles.

### Programas de Reforzamiento como Funciones de Retroalimentación

Más allá de la descripción cualitativa de los patrones conductuales que generan, los programas de reforzamiento pueden analizarse formalmente como **funciones de retroalimentación** que especifican la relación matemática entre respuestas emitidas (R) y refuerzos obtenidos (r). Esta perspectiva, desarrollada por Baum (1973) y Staddon (1979), permite un análisis cuantitativo de cómo cada programa transforma comportamiento en consecuencias.

#### Programas de Razón Variable: Retroalimentación Lineal

Para un programa RV n, la probabilidad de refuerzo es constante e igual a p = 1/n en cada respuesta. Por lo tanto, si un organismo emite R respuestas, el número esperado de refuerzos obtenidos es:

**r = R/n**

o en términos de tasas (respuestas y refuerzos por unidad de tiempo):

**r = R/n**

Esta función de retroalimentación es **lineal**: cada respuesta adicional incrementa los refuerzos obtenidos en una cantidad constante (1/n). La pendiente de esta función, 1/n, representa la "densidad de refuerzo" del programa. Un RV 50 tiene pendiente 1/50 = 0.02 (dos refuerzos por cada 100 respuestas), mientras que un RV 100 tiene pendiente 1/100 = 0.01 (un refuerzo por cada 100 respuestas).

Esta linealidad tiene implicaciones importantes para la optimalidad conductual, como veremos en secciones posteriores. En particular, implica que no hay "rendimientos decrecientes": cada respuesta adicional produce el mismo incremento marginal en refuerzos obtenidos.

#### Programas de Intervalo Variable: Retroalimentación No-Lineal

Los programas IV presentan una estructura de retroalimentación fundamentalmente diferente. En un programa IV, los refuerzos se hacen disponibles a intervalos impredecibles independientemente del comportamiento del organismo, pero requieren al menos una respuesta para ser colectados. Una vez que un refuerzo está disponible, permanece disponible hasta que el organismo responde y lo recolecta.

Para derivar la función de retroalimentación de un IV, consideremos la dinámica temporal del programa. Si el organismo responde a una tasa R (respuestas/segundo) y el programa establece refuerzos disponibles a una tasa programada r_max (la tasa máxima posible de refuerzo), entonces la probabilidad de que un refuerzo esté disponible en cualquier momento es aproximadamente:

**P(refuerzo disponible) = r_max × IRT_medio**

donde IRT_medio = 1/R es el tiempo promedio entre respuestas. Por lo tanto, la tasa de refuerzo obtenida es:

**r ≈ r_max[1 - exp(-R/R₀)]**

donde R₀ es un parámetro relacionado con la tasa programada del IV. Esta función muestra **rendimientos decrecientes**: incrementos en la tasa de respuesta producen incrementos cada vez menores en la tasa de refuerzo obtenida. La función es aproximadamente lineal para tasas bajas de respuesta (cuando R << R₀), pero se aplana asintóticamente aproximándose a r_max conforme R aumenta.

Una forma más simple, frecuentemente usada en análisis teóricos, es la aproximación hiperbólica:

**r = r_max R/(R + c)**

donde c es un parámetro que determina la curvatura de la función. Esta ecuación captura la característica esencial: conforme R aumenta, r se aproxima asintóticamente a r_max.

#### Implicaciones de las Diferentes Funciones de Retroalimentación

La diferencia fundamental entre las funciones de retroalimentación lineales (RV) y no-lineales (IV) tiene profundas implicaciones para el comportamiento óptimo. En un programa RV, dado que cada respuesta contribuye igualmente a la obtención de refuerzos, la estrategia óptima desde una perspectiva de maximización es responder continuamente a la tasa más alta posible. No hay "costo de oportunidad" por responder más: más respuestas siempre significan proporcionalmente más refuerzos.

En contraste, en un programa IV existe un claro costo de oportunidad: respuestas excesivamente rápidas desperdician esfuerzo sin incrementar proporcionalmente los refuerzos obtenidos. La tasa óptima de respuesta en un IV depende del balance entre "asegurar la recolección de refuerzos disponibles" y "no desperdiciar esfuerzo en respuestas innecesarias". Como veremos en la Parte 4, esta diferencia estructural explica por qué los organismos responden mucho más rápido en programas RV que en programas IV comparables.

### Análisis de Equilibrio y Estabilidad

Los programas de reforzamiento pueden analizarse también desde la perspectiva de **sistemas de retroalimentación**. En esta conceptualización, las respuestas del organismo (la salida del sistema) producen refuerzos (que retroalimentan al sistema), los cuales a su vez afectan futuras respuestas. Un sistema está en **equilibrio** cuando la tasa de respuesta se estabiliza—esto es, cuando R(t+1) = R(t).

Para un programa RV con función de retroalimentación r = R/n, el equilibrio depende de la función que relaciona refuerzos obtenidos con tasa de respuesta futura. Si asumimos (siguiendo a Herrnstein, como veremos en la Parte 2) que:

**R = k·r/(r + r₀)**

entonces en equilibrio:

**R = k·(R/n)/(R/n + r₀)**

Resolviendo para R:

**R(n + R/r₀) = kR/n**

**R + R²/(nr₀) = kR/n**

Esta ecuación tiene solución no-trivial positiva, indicando que existe un equilibrio estable para cualquier valor de n. La estabilidad del equilibrio puede analizarse mediante la derivada de la función en el punto de equilibrio; para los programas RV e IV típicos, los equilibrios son estables (perturbaciones pequeñas decaen con el tiempo).

Para programas IV, el análisis es más complejo debido a la naturaleza no-lineal de la función de retroalimentación, pero los principios son similares: existe un equilibrio estable determinado por la intersección de la función de retroalimentación del programa y la función de respuesta del organismo.

### Explicaciones del Control por Programas de Reforzamiento

¿Por qué diferentes programas producen patrones tan característicos y distintivos de comportamiento? Se han propuesto varias explicaciones, que enfatizan diferentes aspectos de las contingencias:

#### 1. Modelamiento de Tiempos entre Respuestas (IRTs)

Una explicación influyente, propuesta por Morse (1966) y desarrollada por Shimp (1969), sostiene que los programas de reforzamiento funcionan seleccionando (reforzando diferencialmente) ciertos **tiempos entre respuestas** (Inter-Response Times, IRTs). En un programa RF, por ejemplo, los IRTs cortos son reforzados más frecuentemente que los largos, porque cada respuesta rápida acerca al organismo al cumplimiento del requisito. En contraste, en un programa IF, los IRTs largos inicialmente (durante la pausa post-refuerzo) son adaptativos porque responder tempranamente es inútil.

Esta hipótesis puede formalizarse: si P(refuerzo|IRT) es la probabilidad condicional de refuerzo dado un IRT de cierta duración, entonces la distribución de IRTs debería reflejar esta probabilidad diferencial. Análisis empíricos han mostrado efectivamente que las distribuciones de IRTs en diferentes programas se ajustan cualitativamente a esta predicción.

#### 2. Sensibilidad a Correlaciones Temporales

Una explicación alternativa enfatiza que los organismos son sensibles a las **correlaciones temporales** entre respuestas y refuerzos. Killeen y Fetterman (1988) demostraron que incluso cuando la tasa global de refuerzo se mantiene constante, los organismos son sensibles a la contingencia temporal local: responden más cuando las respuestas están temporalmente cercanas a los refuerzos.

En programas de razón, cada respuesta está correlacionada positivamente con la proximidad al refuerzo—cada respuesta acerca al organismo al refuerzo. En programas de intervalo, esta correlación es débil o nula: responder más rápido no acerca temporalmente al refuerzo. Esta diferencia en la estructura correlacional podría explicar las tasas de respuesta dramáticamente diferentes que producen los dos tipos de programas.

#### 3. Control por Estímulos Discriminativos

Una tercera línea explicativa sugiere que los patrones conductuales bajo diferentes programas reflejan control por **estímulos discriminativos** generados por el propio programa. En un programa IF, por ejemplo, la pausa post-refuerzo y la aceleración subsecuente podrían reflejar discriminación temporal: el organismo aprende que refuerzos son improbables inmediatamente después del último refuerzo, pero se vuelven progresivamente más probables conforme pasa el tiempo.

Evidencia para esta interpretación proviene de experimentos con "relojes externos" que señalan el tiempo transcurrido en el intervalo: cuando se agregan tales señales, el control temporal se vuelve más preciso, sugiriendo que el tiempo funciona como un estímulo discriminativo.

Es probable que las tres clases de mecanismos contribuyan al control ejercido por diferentes programas de reforzamiento. El modelamiento de IRTs, la sensibilidad a correlaciones temporales, y el control discriminativo temporal no son mutuamente excluyentes, sino aspectos complementarios de cómo las contingencias de refuerzo esculpen patrones complejos de comportamiento.

### Conexión con los Capítulos Sobre Condicionamiento

Los programas de reforzamiento pueden verse como casos especiales de las contingencias estudiadas en el condicionamiento Pavloviano (Capítulos 8-11), pero aplicados al comportamiento operante. Así como el modelo de Rescorla-Wagner especifica cómo la contingencia entre EC y EI controla la adquisición de asociaciones, los programas de reforzamiento especifican contingencias entre respuestas y refuerzos.

Sin embargo, hay una diferencia crucial: en el condicionamiento clásico, el experimentador controla tanto la presentación del EC como del EI, independientemente del comportamiento del organismo. En el condicionamiento operante, el organismo controla con sus respuestas la presentación del reforzador. Esta diferencia transforma el aprendizaje en un **sistema de retroalimentación activa**: el comportamiento genera sus propias consecuencias, que a su vez modifican el comportamiento futuro.

Los modelos cuantitativos del condicionamiento operante (que comenzaremos a examinar en la siguiente parte) pueden verse como análogos operantes del modelo de Rescorla-Wagner: ambos especifican cómo la experiencia modifica valores (asociativos en un caso, operantes en el otro) que controlan el comportamiento. La diferencia fundamental es que en el caso operante, el organismo tiene control activo sobre la generación de esa experiencia.

---

## PARTE 2: DE LA ACCIÓN A LA ELECCIÓN—LA ECUACIÓN DE HERRNSTEIN

### El Problema de Especificar la Forma Funcional

En la Parte 1 vimos que los programas de reforzamiento pueden caracterizarse como funciones de retroalimentación que relacionan respuestas con refuerzos: r = f(R). Sin embargo, para predecir el comportamiento, necesitamos la función complementaria: cómo los refuerzos obtenidos controlan la tasa de respuesta futura. Es decir, necesitamos especificar R = g(r).

Durante la primera mitad del siglo XX, varios teóricos propusieron formas funcionales para esta relación. Hull sugirió una función exponencial basada en su concepto de "fuerza del hábito". Skinner, deliberadamente descriptivo, evitó comprometerse con una forma matemática específica. El avance crucial vino con Richard Herrnstein en la década de 1960, quien propuso una forma funcional específica basada en datos empíricos de experimentos de elección.

### Evidencia Empírica: Los Experimentos de Catania y Reynolds

Para entender la propuesta de Herrnstein, debemos primero examinar los datos que la motivaron. Catania y Reynolds (1968) realizaron un experimento elegante con palomas en el que variaron sistemáticamente la tasa de refuerzo en un programa IV manteniendo constantes otras variables. Midieron la tasa de respuesta en estado estable para diferentes valores de tasa de refuerzo programada.

Los resultados revelaron una relación sistemática con dos características fundamentales:

1. **Rendimientos decrecientes:** Conforme aumentaba la tasa de refuerzo, la tasa de respuesta también aumentaba, pero con incrementos progresivamente menores. La función no era lineal.

2. **Asíntota finita:** Para tasas muy altas de refuerzo, la tasa de respuesta se aproximaba a un valor máximo finito, no crecía indefinidamente.

Estas dos características sugerían una función con forma hiperbólica. Herrnstein propuso que la forma matemática más parsimoniosa que capturaba estas propiedades era:

**R₁ = kr₁/(r₁ + r₀)**

donde:
- R₁ es la tasa de respuesta (respuestas por unidad de tiempo)
- r₁ es la tasa de refuerzo obtenida para esa respuesta
- k es un parámetro que representa la tasa máxima de respuesta que el organismo puede emitir
- r₀ es un parámetro que representa los "refuerzos de otras fuentes" (explicado más adelante)

### Interpretación de los Parámetros

#### El Parámetro k: Capacidad Conductual

El parámetro k representa la tasa de respuesta asintótica—el máximo absoluto que el organismo podría alcanzar si toda la capacidad conductual se dedicara a esa respuesta. Cuando r₁ es muy grande (r₁ >> r₀), la ecuación se aproxima a R₁ ≈ k. Este parámetro está limitado por restricciones físicas y fisiológicas: hay un límite superior a qué tan rápido un organismo puede responder dado el tiempo requerido para cada respuesta y las limitaciones motoras.

Empíricamente, k varía entre organismos y tipos de respuestas. Para palomas picando un disco iluminado, k típicamente está en el rango de 200-300 respuestas por minuto. Para ratas presionando una palanca, k suele ser menor, alrededor de 100-150 respuestas por minuto. Es importante notar que k es una constante del organismo y la respuesta, no del programa de reforzamiento específico.

#### El Parámetro r₀: Refuerzos de Fuentes Alternativas

El parámetro r₀ es conceptualmente más sutil. Herrnstein lo interpretó como la tasa de refuerzo obtenida de **todas las demás fuentes** disponibles para el organismo. Aun en una cámara operante aparentemente vacía, el organismo tiene acceso a refuerzos alternativos: puede explorar el ambiente, acicalarse, descansar, etc. Estas actividades alternativas compiten con la respuesta operante medida por el experimentador.

Matemáticamente, r₀ determina la "semisaturación" de la función: cuando r₁ = r₀, la tasa de respuesta es R₁ = k/2 (la mitad del máximo). Por lo tanto, r₀ puede interpretarse como la tasa de refuerzo necesaria para alcanzar el 50% de la tasa de respuesta máxima.

Esta interpretación implica que **todo comportamiento refleja elección**: incluso cuando solo una respuesta operante está explícitamente disponible y es medida, el organismo está constantemente eligiendo entre esa respuesta y todas las demás actividades posibles. Esta idea—que no existe "comportamiento en aislamiento"—es fundamental para entender la ecuación de Herrnstein.

### Derivación Conceptual de la Ecuación de Herrnstein

Aunque Herrnstein propuso su ecuación inicialmente de forma empírica, puede derivarse de supuestos más fundamentales. La derivación más intuitiva parte de dos principios:

**Principio 1: Restricción Temporal**

El tiempo total disponible para el organismo es fijo. Si T₁ es el tiempo dedicado a la respuesta operante medida y T₀ es el tiempo dedicado a todas las demás actividades, entonces:

**T₁ + T₀ = T_total = constante**

Normalizando a T_total = 1, tenemos T₁ + T₀ = 1.

**Principio 2: Distribución Proporcional al Refuerzo**

El organismo distribuye su tiempo entre alternativas proporcionalmente a los refuerzos obtenidos de cada una:

**T₁/T₀ = r₁/r₀**

Este supuesto implica que el organismo es sensible a la rentabilidad relativa de cada alternativa. Rearreglando:

**T₁ = T₀(r₁/r₀)**

Sustituyendo en la restricción temporal T₁ + T₀ = 1:

**T₀(r₁/r₀) + T₀ = 1**

**T₀(r₁ + r₀)/r₀ = 1**

**T₀ = r₀/(r₁ + r₀)**

Por lo tanto:

**T₁ = 1 - T₀ = r₁/(r₁ + r₀)**

Finalmente, si la tasa de respuesta es proporcional al tiempo dedicado con constante de proporcionalidad k (la tasa de respuesta cuando T₁ = 1):

**R₁ = kT₁ = kr₁/(r₁ + r₀)**

Esta derivación muestra que la ecuación de Herrnstein emerge naturalmente de dos supuestos simples: restricción temporal y distribución proporcional al refuerzo.

### Ajuste a Datos Empíricos

La ecuación de Herrnstein ha demostrado ajustarse notablemente bien a datos de múltiples experimentos. Algunos ejemplos representativos:

**Catania y Reynolds (1968):** Variando r₁ en programas IV para palomas, los datos mostraron la función hiperbólica predicha con r² > 0.95 en la mayoría de los sujetos.

**Herrnstein (1970):** En un análisis de múltiples estudios con diferentes programas y especies, la ecuación contabilizó más del 90% de la varianza en tasas de respuesta.

**De Villiers y Herrnstein (1976):** Demostraron que la ecuación se mantiene incluso cuando se manipulan variables como el tamaño del reforzador (cantidad de comida), el esfuerzo requerido para responder, y el retraso del refuerzo—ajustando apropiadamente lo que cuenta como "tasa de refuerzo efectiva".

Es importante notar que el ajuste de la ecuación no es perfecto en todos los casos. Hay desviaciones sistemáticas, especialmente para tasas muy bajas o muy altas de refuerzo. Además, la ecuación asume estado estable: predice la tasa de respuesta una vez que el comportamiento se ha estabilizado, no la dinámica de adquisición. No obstante, como descripción cuantitativa del control del refuerzo sobre la tasa de respuesta en estado estable, la ecuación de Herrnstein representa uno de los logros más exitosos de la psicología cuantitativa.

### Extensiones: Efectos de Magnitud, Demora, y Esfuerzo

La ecuación básica de Herrnstein asume que todos los refuerzos son equivalentes. Sin embargo, sabemos que factores como la magnitud del reforzador, la demora entre respuesta y refuerzo, y el esfuerzo requerido para responder afectan el comportamiento. Estos factores pueden incorporarse en una versión extendida de la ecuación.

#### Magnitud del Reforzador

Si A₁ representa la magnitud (cantidad) del reforzador, entonces la tasa de refuerzo efectiva puede definirse como:

**r₁_efectivo = A₁ × r₁**

Sustituyendo en la ecuación de Herrnstein:

**R₁ = k(A₁r₁)/(A₁r₁ + r₀)**

Esta formulación predice correctamente que incrementar la magnitud del reforzador aumenta la tasa de respuesta de manera similar a incrementar la frecuencia de refuerzo.

#### Demora del Reforzador

Si D₁ es la demora entre la respuesta y la entrega del reforzador, su efecto puede modelarse mediante un factor de descuento:

**r₁_efectivo = r₁/(1 + kD₁)**

donde k es una constante de descuento temporal. Esta formulación captura el hallazgo robusto de que reforzadores demorados son menos efectivos para mantener el comportamiento.

#### Esfuerzo de la Respuesta

Si E₁ representa el esfuerzo (o "costo") asociado con emitir la respuesta, su efecto puede modelarse como un término que reduce la tasa efectiva de respuesta:

**R₁_neto = R₁ - cE₁**

donde c es una constante de costo. Alternativamente, el esfuerzo puede conceptualizarse como reduciendo el valor efectivo del reforzador.

Estas extensiones demuestran la flexibilidad de la ecuación de Herrnstein para acomodar múltiples dimensiones relevantes de las contingencias de refuerzo.

### Aplicaciones a la Modificación Conductual

La ecuación de Herrnstein tiene implicaciones prácticas importantes para intervenciones conductuales. En contextos aplicados, frecuentemente se busca aumentar la frecuencia de comportamientos deseables (e.g., completar tareas académicas) o disminuir comportamientos problemáticos (e.g., rabietas). La ecuación sugiere varias estrategias:

**1. Incrementar r₁ (reforzamiento directo):** La estrategia más obvia es aumentar el reforzamiento del comportamiento objetivo. Sin embargo, la ecuación predice rendimientos decrecientes: duplicar r₁ no duplicará R₁.

**2. Reducir r₀ (empobrecimiento de alternativas):** Otra estrategia es reducir el reforzamiento disponible de fuentes alternativas. Por ejemplo, en un aula, minimizar distracciones (juguetes, ventanas interesantes) reduce r₀, aumentando la proporción de comportamiento dedicado a la tarea académica.

**3. Reforzamiento diferencial de comportamientos alternativos (DRA):** Para reducir un comportamiento problemático, se puede reforzar una respuesta alternativa incompatible. Si el comportamiento problemático (R₁) obtiene r₁ refuerzos y el comportamiento alternativo (R₂) obtiene r₂ refuerzos, entonces:

**R₁ = kr₁/(r₁ + r₂ + r₀)**

Aumentar r₂ reduce R₁ incluso sin cambiar directamente las consecuencias del comportamiento problemático.

Un ejemplo clínico ilustrativo es el tratamiento de autolesión en individuos con discapacidades del desarrollo. Investigaciones han demostrado que la autolesión frecuentemente es mantenida por refuerzo social (atención de cuidadores). La ecuación de Herrnstein predice que proporcionar refuerzo social no-contingente (aumentando r₀) o reforzar comportamientos alternativos de comunicación (aumentando r₂) reducirá la autolesión, predicción confirmada en múltiples estudios aplicados.

### La Transición de Acción Simple a Elección

La ecuación de Herrnstein para una sola respuesta puede parecer describir "comportamiento en aislamiento", pero conceptualmente implica elección: el organismo está eligiendo entre la respuesta medida (R₁) y todas las demás actividades (R₀). Esta conceptualización prepara el terreno para analizar situaciones de elección explícita, donde dos o más respuestas medibles están disponibles simultáneamente.

Cuando generalizamos la ecuación de Herrnstein a situaciones con múltiples respuestas explícitas, obtenemos un sistema de ecuaciones. Para dos respuestas:

**R₁ = kr₁/(r₁ + r₂ + r₀)**

**R₂ = kr₂/(r₁ + r₂ + r₀)**

Estas ecuaciones describen cómo cada respuesta es afectada por los refuerzos obtenidos de ambas alternativas. Un resultado importante emerge al considerar la **razón** de estas tasas de respuesta:

**R₁/R₂ = r₁/r₂**

Este resultado—que la razón de respuestas iguala la razón de refuerzos—es la **ley de igualación**, el fenómeno central que examinaremos en la Parte 3. La ecuación de Herrnstein, derivada del análisis de respuestas individuales, predice igualación en situaciones de elección concurrente. Esta transición de la acción simple a la elección es uno de los logros teóricos más elegantes de la psicología cuantitativa del aprendizaje.

---

## PARTE 3: ELECCIÓN RECURRENTE E IGUALACIÓN

### El Protocolo de Elección Concurrente

Para estudiar sistemáticamente cómo los organismos distribuyen su comportamiento entre múltiples alternativas, necesitamos un protocolo experimental que permita elección continua y repetida. El paradigma estándar es el **procedimiento de elección concurrente**, desarrollado por Findley (1958) y Herrnstein (1961).

En su forma básica, una paloma enfrenta dos discos iluminados, cada uno asociado con un programa de reforzamiento independiente. La paloma puede picotear cualquier disco en cualquier momento, y los programas operan simultáneamente. Típicamente, ambos programas son de intervalo variable (IV-IV concurrentes), aunque también se han estudiado otras combinaciones (RV-RV, IV-RV, etc.).

Un aspecto técnico crucial es el **changeover delay (COD)**: un breve período (típicamente 1-3 segundos) después de cambiar de una alternativa a otra durante el cual no puede obtenerse refuerzo. Este requisito previene una estrategia simple de "cambio rápido" donde el organismo alternaría rápidamente entre alternativas para "cosechar" refuerzos de ambas sin costo. El COD asegura que hay un costo temporal por cambiar, forzando al organismo a distribuir el tiempo de manera más comprometida entre alternativas.

### Distinguir "Optar" de "Asignar": Sistemas Abiertos versus Cerrados

Antes de examinar los datos de elección concurrente, es fundamental distinguir dos tipos cualitativamente diferentes de situaciones de elección:

**Optar (sistemas abiertos):** El organismo hace una elección discreta entre alternativas mutuamente excluyentes, y cada elección "cierra" esa oportunidad. Ejemplo: elegir entre dos restaurantes para cenar. Una vez que has elegido y cenado en uno, la oportunidad de cenar en el otro esa noche se perdió. En estos casos, la estrategia óptima típicamente es **maximización**: seleccionar consistentemente la mejor opción.

**Asignar (sistemas cerrados):** El organismo distribuye continuamente su comportamiento entre alternativas que permanecen disponibles indefinidamente. Ejemplo: una abeja que puede visitar repetidamente dos tipos de flores en un prado. Cada visita no agota las flores; puede regresar múltiples veces a cada tipo. En estos casos, la distribución óptima depende de cómo cada alternativa "recupera" su valor con el tiempo.

Los protocolos de elección concurrente con programas IV-IV son sistemas cerrados: las alternativas permanecen disponibles continuamente, y el organismo puede cambiar entre ellas repetidamente. Esta distinción es crucial porque las predicciones normativas difieren radicalmente entre estos dos tipos de situaciones. En sistemas abiertos, maximización (selección exclusiva de la mejor opción) es óptima. En sistemas cerrados con recuperación temporal (como los programas IV), otras estrategias pueden ser óptimas, como veremos.

### El Descubrimiento de la Ley de Igualación

Herrnstein (1961) realizó el experimento clásico que reveló la ley de igualación. Entrenó palomas en varios procedimientos de elección concurrente IV-IV, variando sistemáticamente las tasas de refuerzo programadas para cada alternativa. Por ejemplo, en una condición el disco izquierdo podía proporcionar refuerzos en promedio cada 40 segundos (IV 40-seg) mientras el disco derecho proporcionaba refuerzos cada 120 segundos (IV 120-seg). En otra condición, las tasas eran IV 60-seg versus IV 180-seg, etc.

Herrnstein midió tanto el número de respuestas a cada alternativa como el tiempo dedicado a cada una. El resultado fue sorprendente en su regularidad: **la proporción de respuestas a cada alternativa igualaba la proporción de refuerzos obtenidos de cada alternativa**. Formalmente:

**R₁/(R₁ + R₂) = r₁/(r₁ + r₂)**

o equivalentemente en forma de razones:

**R₁/R₂ = r₁/r₂**

Por ejemplo, si una alternativa proporcionaba el 75% de los refuerzos (3 de cada 4), la paloma dirigía aproximadamente el 75% de sus respuestas a esa alternativa. Esta relación se mantuvo a través de diferentes valores absolutos de las tasas de refuerzo: lo que importaba era la **razón relativa**, no los valores absolutos.

Resultados similares se obtuvieron para la distribución de **tiempo**: la proporción de tiempo dedicado a cada alternativa también igualaba la proporción de refuerzos:

**T₁/(T₁ + T₂) = r₁/(r₁ + r₂)**

Igualación del tiempo es particularmente interesante porque el tiempo es una medida "continua" del comportamiento, mientras que el número de respuestas es discreto. El hecho de que ambas medidas muestren igualación sugiere que es un fenómeno fundamental de la distribución conductual.

### Generalización de la Ley de Igualación

Investigaciones posteriores demostraron que la igualación no se limita a palomas en protocolos de elección concurrente. El fenómeno se ha replicado en:

**Múltiples especies:** Ratas, monos, humanos (tanto niños como adultos), y varias especies adicionales muestran igualación en protocolos apropiados.

**Diferentes dimensiones de refuerzo:** No solo la **frecuencia** (tasa) de refuerzo, sino también la **magnitud** (cantidad de comida por refuerzo), la **calidad** (preferencia intrínseca por diferentes tipos de reforzadores), e incluso la **probabilidad** de refuerzo muestran igualación. Por ejemplo:

**R₁/R₂ = (A₁r₁)/(A₂r₂)**

donde A₁ y A₂ son las magnitudes de los reforzadores.

**Diferentes tipos de programas:** Aunque IV-IV concurrentes son el protocolo estándar, igualación también ocurre (con algunas modificaciones) en programas concurrentes de razón variable (RV-RV) y programas mixtos.

Esta generalidad extraordinaria sugiere que igualación refleja un principio fundamental de cómo el comportamiento se distribuye en respuesta a consecuencias diferenciales.

### Igualación Generalizada: Sensibilidad y Sesgo

Aunque la ley de igualación simple describe muchos datos notablemente bien, análisis más detallados revelaron desviaciones sistemáticas. Baum (1974) propuso una **forma generalizada** de la ley de igualación que acomoda estas desviaciones:

**log(R₁/R₂) = a·log(r₁/r₂) + log(b)**

Esta ecuación, expresada en logaritmos para linearizar la relación, introduce dos nuevos parámetros:

#### Parámetro de Sensibilidad (a)

El parámetro *a* mide qué tan sensible es la distribución de respuestas a diferencias en el refuerzo. Si a = 1, obtenemos igualación estricta (la forma simple de la ley). Si a < 1, ocurre **undermatching** (subigualación): el organismo no es suficientemente sensible a las diferencias en refuerzo, distribuyendo su comportamiento más equitativamente de lo que predicha igualación estricta. Si a > 1, ocurre **overmatching** (sobreigualación): el organismo es excesivamente sensible, mostrando preferencia más extrema de lo que predice igualación estricta.

Empíricamente, undermatching (a < 1) es el patrón más común, con valores típicos de a entre 0.7 y 0.9 en palomas. Varios factores pueden producir undermatching:

1. **Changeover delay (COD):** Períodos más largos de COD tienden a reducir *a*, aparentemente porque aumentan el "costo" de cambiar entre alternativas.

2. **Discriminabilidad de las alternativas:** Cuando las alternativas son difíciles de discriminar (e.g., dos tonos de frecuencia similar), *a* disminuye.

3. **Experiencia:** Con entrenamiento extenso, *a* tiende a aproximarse a 1.0.

#### Parámetro de Sesgo (b)

El parámetro *b* mide **sesgo** o preferencia intrínseca por una alternativa independiente de las contingencias de refuerzo programadas. Si b = 1, no hay sesgo. Si b > 1, hay sesgo hacia la alternativa 1; si b < 1, hay sesgo hacia la alternativa 2.

Las fuentes de sesgo incluyen:

1. **Posición:** Muchos organismos muestran preferencia por responder en cierta ubicación espacial (e.g., palomas frecuentemente prefieren el disco derecho).

2. **Características del estímulo:** Diferencias en color, brillo, o modalidad sensorial de las alternativas pueden crear preferencias intrínsecas.

3. **Tipo de respuesta:** Si las dos alternativas requieren respuestas topográficamente diferentes (e.g., picar versus presionar), puede haber sesgo basado en la facilidad o "naturalidad" de cada respuesta.

El sesgo es importante desde una perspectiva aplicada porque indica preferencias que deben controlarse experimentalmente o tenerse en cuenta en interpretaciones teóricas. Desde una perspectiva teórica, el sesgo es menos interesante que la sensibilidad porque no refleja sensibilidad a las contingencias.

### El Fenómeno de Undermatching y el Papel del COD

El undermatching (a < 1) es el patrón modal en experimentos de elección concurrente, y merece atención especial porque tiene implicaciones teóricas importantes. Una variable que afecta dramáticamente el grado de undermatching es la duración del **changeover delay (COD)**.

Catania (1966) demostró que sin COD, las palomas frecuentemente muestran un patrón de "alternación rápida": cambian frecuentemente entre alternativas, recolectando refuerzos de ambas sin distribuir preferencia de manera diferencial. Esto produce undermatching extremo (a cercano a 0).

A medida que la duración del COD aumenta, *a* se incrementa, aproximándose a 1.0 con CODs de 2-5 segundos. Sin embargo, CODs muy largos (>10 segundos) pueden reducir *a* nuevamente, aparentemente porque "desacoplan" las respuestas de los refuerzos inmediatos.

La interpretación teórica dominante es que el COD funciona como un **costo de cambio**: hace que cambiar entre alternativas sea menos ventajoso, obligando al organismo a "comprometerse" más con cada alternativa por períodos más largos. Sin este costo, la estrategia óptima a corto plazo es "muestrear" ambas alternativas frecuentemente, lo cual produce distribuciones menos diferenciadas.

### Igualación en Programas de Razón Variable Concurrentes

Hasta aquí nos hemos enfocado en programas IV-IV concurrentes. ¿Qué ocurre con programas de razón variable concurrentes (RV-RV)? Recordemos que en programas RV, la función de retroalimentación es lineal: cada respuesta adicional produce el mismo incremento marginal en refuerzos obtenidos. Esto crea una dinámica fundamentalmente diferente.

Herrnstein y Loveland (1975) estudiaron elección concurrente RV-RV, variando sistemáticamente la razón relativa de los requisitos. Los resultados fueron dramáticamente diferentes de los hallazgos con IV-IV: en lugar de igualación, los animales mostraron **preferencia exclusiva** por la alternativa con el menor requisito de respuesta.

Cuando una alternativa requería RV 30 (en promedio 30 respuestas por refuerzo) y la otra RV 90, las palomas respondían casi exclusivamente al RV 30. Esta preferencia exclusiva es consistente con **maximización**: dado que la función de retroalimentación es lineal, maximizar refuerzos requiere responder exclusivamente a la alternativa más rica.

Curiosamente, cuando los dos programas RV eran idénticos (e.g., RV 50 en ambas alternativas), Staddon y Hinson (1983) encontraron que el comportamiento dependía del valor absoluto del programa:

- **Programas "ricos" (RV pequeños, e.g., RV 20):** Preferencia exclusiva por una alternativa (seleccionada arbitrariamente).
- **Programas "pobres" (RV grandes, e.g., RV 100):** Distribución aproximadamente igual (indiferencia).

Este patrón es desconcertante desde perspectivas de maximización o igualación estrictas. Una interpretación es que con programas "pobres", los organismos exploran más debido a la incertidumbre: con refuerzos infrecuentes, mantener el muestreo de ambas alternativas es adaptativo. En contraste, con programas "ricos" donde los refuerzos son frecuentes, el organismo rápidamente "detecta" cuál alternativa está produciendo más y se compromete exclusivamente con ella.

### Derivación de Igualación desde la Ecuación de Herrnstein

Vimos al final de la Parte 2 que las ecuaciones de Herrnstein para dos respuestas concurrentes:

**R₁ = kr₁/(r₁ + r₂ + r₀)**

**R₂ = kr₂/(r₁ + r₂ + r₀)**

implican:

**R₁/R₂ = r₁/r₂**

Esta derivación es directa, pero tiene un supuesto crítico que debe hacerse explícito: **r₀ es constante** a través de diferentes condiciones experimentales. Es decir, asumimos que los "refuerzos de fuentes alternativas" no cambian cuando manipulamos r₁ y r₂.

¿Es plausible este supuesto? En una cámara operante bien controlada, donde las únicas fuentes de refuerzo explícitas son los dos programas concurrentes, parece razonable. Sin embargo, si hay fuentes adicionales de refuerzo (e.g., comida disponible en el piso de la cámara, actividades no medidas que son reforzantes), y si estas fuentes varían entre condiciones, entonces r₀ no sería constante y la derivación fallaría.

Esta sensibilidad de la predicción de igualación al supuesto de r₀ constante es una debilidad potencial de la derivación. Modelos alternativos (que examinaremos en la Parte 4) han propuesto mecanismos que producen igualación sin requerir este supuesto.

### Igualación de Tasas Locales: Una Interpretación Alternativa

La formulación estándar de igualación compara **tasas globales** acumuladas sobre sesiones completas: la razón de respuestas totales iguala la razón de refuerzos totales. Sin embargo, Heyman y Luce (1979) propusieron una interpretación más local: los organismos igualan las **tasas locales de refuerzo** experimentadas en cada alternativa.

La tasa local de refuerzo en una alternativa se define como:

**ρ₁ = r₁/T₁**

donde r₁ es el número de refuerzos obtenidos de la alternativa 1 y T₁ es el tiempo dedicado a esa alternativa. Es decir, ρ₁ es los "refuerzos por unidad de tiempo invertido" en esa alternativa.

La hipótesis de igualación de tasas locales propone:

**ρ₁ = ρ₂**

o:

**r₁/T₁ = r₂/T₂**

Esta formulación es matemáticamente equivalente a:

**T₁/T₂ = r₁/r₂**

Es decir, la razón de tiempos dedicados iguala la razón de refuerzos obtenidos. Dado que típicamente R₁/R₂ ≈ T₁/T₂ (las razones de respuestas y tiempos son similares), esta formulación también implica igualación de respuestas.

La ventaja conceptual de esta interpretación es que sugiere un mecanismo psicológico: los organismos podrían ser sensibles a la **rentabilidad** (refuerzos/tiempo) experimentada localmente en cada alternativa, y ajustar su distribución de tiempo para igualar estas rentabilidades. Desde una perspectiva ecológica, igualar tasas locales tiene sentido: garantiza que el organismo no está "desperdiciando tiempo" en una alternativa que es localmente menos productiva.

Esta interpretación conecta igualación con modelos de forrajeo óptimo en ecología conductual, donde un supuesto central es que los organismos son sensibles a las "tasas de ganancia" de diferentes parches de recursos en su ambiente.

---

## PARTE 4: INTERPRETACIONES TEÓRICAS DE IGUALACIÓN

### El Problema de la Explicación

La ley de igualación es un hallazgo empírico robusto: describe con notable precisión cómo los organismos distribuyen su comportamiento en procedimientos de elección concurrente. Sin embargo, describir un fenómeno no es lo mismo que explicarlo. ¿Por qué los organismos igualan? ¿Qué procesos—psicológicos, fisiológicos, o evolutivos—producen este patrón?

Esta pregunta ha generado un debate teórico de décadas, con dos familias principales de explicaciones:

1. **Maximización global:** Igualación emerge como consecuencia de maximizar alguna medida global de beneficio (refuerzos totales, tasa promedio de refuerzo, etc.).

2. **Igualación de tasas locales (melioration):** Los organismos igualan tasas locales de refuerzo, sin necesidad de computar o representar una medida global.

Examinaremos ambas perspectivas y la evidencia que las favorece o contradice.

### Maximización Global como Explicación de Igualación

#### La Argumentación de Rachlin

Rachlin y colaboradores (Rachlin, 1973; Rachlin, Green, Kagel, & Battalio, 1976) argumentaron que igualación puede ser una consecuencia de maximización si consideramos las restricciones apropiadas. Su razonamiento es el siguiente:

En un procedimiento de elección concurrente IV-IV, el objetivo "racional" de un organismo debería ser **maximizar la tasa total de refuerzo obtenida**:

**Maximizar: r₁ + r₂**

Sin embargo, hay restricciones. El tiempo total disponible es fijo:

**T₁ + T₂ = T_total**

Además, recordemos que en programas IV, la tasa de refuerzo obtenida de cada alternativa depende de cuánto tiempo se dedica a ella. Específicamente, para un programa IV con tasa programada r_max, la tasa obtenida aproximadamente sigue:

**r = r_max[1 - exp(-T/τ)]**

donde τ es una constante temporal. Para tiempos T suficientemente grandes (cuando T >> τ), esto se aproxima a r ≈ r_max. Pero para distribuciones de tiempo, la relación exacta importa.

Rachlin demostró que bajo estas restricciones, la distribución de tiempo que maximiza r₁ + r₂ es precisamente aquella que satisface:

**T₁/T₂ = r₁_max/r₂_max**

donde r₁_max y r₂_max son las tasas programadas de los dos programas IV. Y dado que r₁ ≈ r₁_max y r₂ ≈ r₂_max (cuando los organismos pasan suficiente tiempo en cada alternativa), esto implica:

**T₁/T₂ = r₁/r₂**

Es decir, **igualación de tiempos**, que a su vez implica igualación de respuestas.

Esta derivación sugiere que igualación no es un principio fundamental, sino una **consecuencia emergente** de maximización sujeta a las restricciones específicas de los programas IV concurrentes.

#### Limitaciones de la Explicación por Maximización

Aunque elegante, la explicación por maximización enfrenta varias dificultades:

1. **Depende críticamente de los programas IV:** La derivación asume funciones de retroalimentación no-lineales características de programas IV. Para programas RV concurrentes (con funciones lineales), maximización predice preferencia exclusiva, no igualación. De hecho, como vimos, los organismos sí muestran preferencia exclusiva en RV-RV, consistente con maximización. Pero esto significa que igualación no es un principio general—es específico a situaciones con funciones de retroalimentación particulares.

2. **Requiere "sabiduría" global:** Para maximizar la tasa total de refuerzo, el organismo necesitaría representar o computar esta cantidad global y ajustar su comportamiento en consecuencia. No está claro qué mecanismos psicológicos permitirían esto.

3. **No explica undermatching:** La derivación predice igualación perfecta (a = 1), pero como vimos, undermatching (a < 1) es común. Explicar undermatching requiere supuestos adicionales ad hoc.

4. **Evidencia contradictoria (discutida abajo):** Hay experimentos diseñados específicamente para distinguir maximización de igualación local, y algunos favorecen igualación local.

### Experimento Crítico: Programas Concurrentes RV-IV

Herrnstein y Heyman (1979) realizaron un experimento crucial diseñado para distinguir entre maximización global e igualación de tasas locales. Usaron programas **concurrentes RV-IV**: una alternativa operaba bajo un programa de razón variable, la otra bajo un programa de intervalo variable.

La lógica es la siguiente: en un programa RV, la tasa local de refuerzo (r/T) es constante sin importar cuánto tiempo se dedique—cada minuto adicional produce el mismo número de refuerzos. En contraste, en un programa IV, la tasa local de refuerzo disminuye con el tiempo dedicado (rendimientos decrecientes). 

**Predicción de maximización global:** Para maximizar refuerzos totales, el organismo debería responder casi exclusivamente al RV, porque no hay rendimientos decrecientes—más tiempo siempre produce proporcionalmente más refuerzos.

**Predicción de igualación de tasas locales:** El organismo debería distribuir tiempo hasta que las tasas locales sean iguales:

**r_RV/T_RV = r_IV/T_IV**

Dado que en el RV la tasa local es aproximadamente constante (r_RV/T_RV ≈ r_max_RV), mientras en el IV la tasa local disminuye con T_IV, existiría una distribución de tiempo que iguala estas tasas locales—y esta distribución **no** es exclusividad del RV.

**Resultados:** Herrnstein y Heyman encontraron que los organismos **no** respondieron exclusivamente al RV. En cambio, distribuyeron tiempo entre ambas alternativas de manera consistente con igualación de tasas locales. Esto favorece la interpretación de igualación local sobre maximización global.

Sin embargo, este resultado no es completamente concluyente. Houston y McNamara (1981) argumentaron que bajo ciertos supuestos sobre los "costos" de responder (esfuerzo, tiempo por respuesta), maximización podría predecir distribuciones no-exclusivas incluso en RV-IV. El debate continúa.

### Melioration: Igualación como Maximización Local

Herrnstein y Vaughan (1980) propusieron una teoría alternativa llamada **melioration** (del latín "melior" = mejor). La idea central es que los organismos no intentan maximizar una medida global, sino que siguen una regla local simple:

**Regla de Melioration:** "Si la tasa local de refuerzo en la alternativa 1 es mayor que en la alternativa 2, transfiere tiempo de la alternativa 2 a la alternativa 1."

Formalmente, si:

**r₁/T₁ > r₂/T₂**

entonces incrementar T₁ (y correspondientemente reducir T₂, dado que T₁ + T₂ = constante).

Este proceso dinámico continúa hasta alcanzar un equilibrio donde:

**r₁/T₁ = r₂/T₂**

Es decir, **igualación de tasas locales**.

La teoría de melioration tiene varias características atractivas:

1. **Mecanismo psicológicamente plausible:** Comparar tasas locales ("¿cuál alternativa me está dando más refuerzos por mi tiempo?") es conceptualmente más simple que representar y maximizar una tasa global.

2. **Proceso dinámico:** Melioration especifica cómo el comportamiento cambia con el tiempo, no solo el estado de equilibrio. Predice que el organismo "oscilará" alrededor del punto de igualación, ajustando continuamente conforme experimenta las tasas locales.

3. **Explica desviaciones de la optimalidad:** En algunas situaciones (discutidas abajo), melioration predice que los organismos alcanzarán un equilibrio que **no** es óptimo globalmente. Estas predicciones se han confirmado empíricamente.

#### El Problema de la Ventana Temporal

Una limitación de la teoría de melioration es que no especifica claramente sobre qué **ventana temporal** el organismo calcula las tasas locales. ¿Es el promedio de los últimos 10 segundos? ¿Los últimos 5 refuerzos? ¿La sesión completa hasta ese momento?

Diferentes ventanas temporales producen predicciones diferentes sobre la dinámica del comportamiento. Ventanas cortas producirían cambios rápidos y potencialmente erráticos; ventanas largas producirían ajustes más lentos y estables.

Varios investigadores han intentado estimar la ventana temporal efectiva ajustando modelos a datos de series temporales, con resultados variables. No hay consenso sobre el valor específico, y es probable que varíe entre especies, individuos, y condiciones experimentales.

### Evidencia Favorable a Melioration: Situaciones Subóptimas

Herrnstein y Vaughan (1980) diseñaron situaciones donde **melioration y maximización predicen resultados diferentes**. Un ejemplo es el siguiente procedimiento:

Dos alternativas están disponibles. La Alternativa 1 ofrece un programa RV rico (e.g., RV 30), pero cada vez que el organismo responde a la Alternativa 1, la Alternativa 2 se "enriquece": su programa RV disminuye (requiere menos respuestas por refuerzo). Converamente, responder a la Alternativa 2 "empobrece" la Alternativa 1 (aumenta su RV).

**Predicción de maximización:** El organismo debería responder casi exclusivamente a la Alternativa 2, porque esto mantiene la Alternativa 1 rica. Luego, ocasionalmente cambiar a la Alternativa 1 para cosechar refuerzos del programa rico.

**Predicción de melioration:** El organismo calculará las tasas locales. Inicialmente, la Alternativa 1 es más rica, así que incrementa T₁. Pero esto enriquece la Alternativa 2. Eventualmente, las tasas locales se igualan, produciendo una distribución de equilibrio que **no es globalmente óptima** (obtiene menos refuerzos totales que si hubiera seguido la estrategia de maximización).

**Resultados:** Consistente con melioration, los organismos alcanzaron un equilibrio subóptimo, obteniendo menos refuerzos totales de los que podrían haber obtenido con la estrategia de maximización.

Este hallazgo es significativo porque demuestra que bajo ciertas condiciones, igualación local (melioration) lleva a resultados subóptimos globalmente, y los organismos siguen melioration en lugar de maximización.

### Modelo de Valor Q: Una Alternativa Computacional

En años recientes, algunos investigadores han propuesto que los modelos de **aprendizaje por refuerzo** de la ciencia computacional podrían proporcionar un marco unificado para entender tanto igualación como melioration. Estos modelos, desarrollados originalmente en inteligencia artificial, postulan que los organismos aprenden **valores** asociados con acciones (valores Q) y actualizan estos valores basándose en la experiencia.

Para una situación de elección simple entre dos alternativas, el organismo mantiene valores Q₁ y Q₂ que representan la "utilidad esperada" de cada alternativa. Estos valores se actualizan después de cada refuerzo según:

**Q_i(t+1) = Q_i(t) + α[r_i - Q_i(t)]**

donde α es una tasa de aprendizaje y r_i es el refuerzo obtenido (1 si se obtuvo refuerzo, 0 si no). Este es el **modelo de Bush-Mosteller**, uno de los primeros modelos cuantitativos de aprendizaje, equivalente al modelo de Rescorla-Wagner para el caso de un solo estado.

Luego, la probabilidad de elegir cada alternativa se determina mediante una **función de respuesta** (discutida extensamente en la Parte 5 sobre reglas de respuesta). Una función común es la **regla softmax**:

**P(Alternativa 1) = exp(βQ₁)/[exp(βQ₁) + exp(βQ₂)]**

donde β es un parámetro de "sensibilidad" o "temperatura".

Simulaciones computacionales han demostrado que este modelo puede producir tanto igualación como diversos grados de undermatching, dependiendo de los valores de α y β. Sin embargo, hay una limitación importante: este modelo es **independiente del contexto**. Los valores Q dependen solo de la historia de refuerzos de cada alternativa, no de la relación entre alternativas. Por lo tanto, el modelo predice que la preferencia entre dos alternativas no debería cambiar si ambas se hacen igualmente más ricas o más pobres—predicción que no siempre se cumple.

### El Experimento de Belke: Efectos de Contexto

Belke (1992) realizó un experimento crítico para evaluar si los organismos son sensibles al **contexto global** más allá de los valores individuales de cada alternativa. Entrenó ratas en dos condiciones:

**Condición 1 (Contexto Rico):** Elección concurrente entre IV 30-seg e IV 60-seg.

**Condición 2 (Contexto Pobre):** Elección concurrente entre IV 60-seg e IV 120-seg.

Noten que en ambas condiciones, la **razón** de las tasas de refuerzo es la misma (2:1). Por lo tanto, tanto la ley de igualación simple como el modelo de valor Q independiente del contexto predicen la misma preferencia en ambas condiciones.

Sin embargo, desde perspectivas que enfatizan tasas absolutas o el contexto de refuerzo total, las predicciones podrían diferir. Por ejemplo, si los organismos son sensibles a la tasa **total** de refuerzo disponible (que es mayor en la Condición 1), podrían mostrar preferencias diferentes.

**Resultados:** Belke encontró **efectos de contexto**: las ratas mostraron preferencias más extremas (más alejadas de indiferencia) en el Contexto Rico que en el Contexto Pobre. Esto contradice el modelo de valor Q simple y sugiere que los organismos son sensibles al contexto global de riqueza de refuerzo, no solo a las razones relativas.

Este hallazgo favorece teorías que postulan que los organismos representan o son sensibles a medidas globales de la disponibilidad de refuerzo, consistente con algunos aspectos de la teoría de maximización.

### Síntesis: Múltiples Mecanismos, Múltiples Niveles

La evidencia revisada sugiere que no hay una única explicación de igualación que capture todos los fenómenos. Más bien, diferentes procesos operan en diferentes niveles:

1. **A nivel evolutivo:** La selección natural favorece organismos que distribuyen su comportamiento de manera aproximadamente óptima. En ambientes con funciones de retroalimentación similares a programas IV (recursos que se recuperan con el tiempo), igualación de tasas locales es una estrategia eficaz.

2. **A nivel conductual:** Los organismos parecen seguir reglas de melioration—trasladar comportamiento hacia alternativas con mayor tasa local de refuerzo—pero también son sensibles a medidas globales como la tasa total de refuerzo.

3. **A nivel neurofisiológico:** Los circuitos cerebrales podrían implementar mecanismos similares a los modelos de valor Q, actualizando representaciones de valor asociadas con diferentes acciones, aunque probablemente con extensiones que capturan contexto global.

Una dirección prometedora para la investigación futura es integrar estas perspectivas, desarrollando modelos que especifiquen cómo mecanismos neurofisiológicos implementan reglas conductuales que fueron moldeadas por presiones selectivas evolutivas.

---

## PARTE 5: SÍNTESIS Y CONEXIONES

### Síntesis de Conceptos Principales

Este capítulo ha cubierto un arco conceptual desde el análisis de programas simples de reforzamiento hasta teorías complejas de cómo los organismos distribuyen óptimamente su comportamiento. Sinteticemos los conceptos principales:

**1. Programas como Funciones de Retroalimentación:** Los programas de reforzamiento especifican relaciones matemáticas entre comportamiento (R) y consecuencias (r). Programas de razón variable tienen funciones lineales (r = R/n), mientras programas de intervalo variable tienen funciones no-lineales con rendimientos decrecientes. Estas diferencias estructurales tienen profundas implicaciones para el comportamiento óptimo.

**2. La Ecuación de Herrnstein:** Para una respuesta individual, la tasa de respuesta R se relaciona con la tasa de refuerzo r mediante R = kr/(r + r₀), una función hiperbólica que captura rendimientos decrecientes. Los parámetros k (capacidad máxima) y r₀ (refuerzos alternativos) tienen interpretaciones psicológicas claras. Esta ecuación unifica el análisis de respuestas individuales y sienta las bases para analizar elección.

**3. La Ley de Igualación:** En situaciones de elección concurrente, los organismos distribuyen respuestas (y tiempo) proporcionalmente a los refuerzos obtenidos: R₁/R₂ = r₁/r₂. Este fenómeno, notable por su generalidad a través de especies, respuestas, y dimensiones de refuerzo, es uno de los hallazgos cuantitativos más robustos en la psicología del aprendizaje.

**4. Igualación Generalizada:** Desviaciones sistemáticas de igualación simple se capturan mediante parámetros de sensibilidad (a) y sesgo (b). Undermatching (a < 1) es el patrón más común, influido por factores como el changeover delay y la discriminabilidad de alternativas.

**5. Interpretaciones Teóricas:** Igualación puede emerger de maximización global (bajo restricciones específicas) o de igualación de tasas locales (melioration). Evidencia experimental favorece melioration en muchos casos, especialmente en situaciones donde las dos teorías hacen predicciones divergentes. Sin embargo, efectos de contexto sugieren sensibilidad a medidas globales.

**6. Especificidad de los Programas:** Las predicciones sobre comportamiento óptimo dependen críticamente de la estructura de los programas. En RV-RV concurrentes, maximización (preferencia exclusiva) es tanto normativa como empíricamente observada. En IV-IV concurrentes, igualación es observada y es aproximadamente óptima. Esta especificidad subraya la importancia de considerar las propiedades formales de las contingencias de refuerzo.

### Limitaciones y Fenómenos No Cubiertos

Aunque este capítulo ha cubierto ampliamente los modelos de igualación y maximización, varios fenómenos importantes quedan fuera de nuestro análisis:

**1. Dinámica de Adquisición:** Los modelos discutidos describen comportamiento en **estado estable** (equilibrio). No especifican cómo el comportamiento cambia con el tiempo desde el inicio del entrenamiento hasta alcanzar el equilibrio. Modelos dinámicos de aprendizaje por refuerzo, que veremos en capítulos posteriores, abordan esta cuestión.

**2. Auto-Control y Descuento Temporal:** Cuando los refuerzos están temporalmente demorados, los organismos muestran preferencias que reflejan **descuento temporal**: prefieren refuerzos inmediatos pequeños sobre refuerzos demorados grandes. Este fenómeno requiere extender los modelos de elección para incorporar la dimensión temporal explícitamente.

**3. Elección Bajo Riesgo:** Las situaciones que hemos analizado involucran reforzamiento probabilístico, pero no hemos examinado sistemáticamente cómo el **riesgo** (variabilidad en las consecuencias) afecta las preferencias. Organismos frecuentemente muestran aversión al riesgo o preferencia por el riesgo dependiendo del contexto.

**4. Programas Concurrentes Encadenados:** En muchas situaciones reales, las elecciones tienen consecuencias que se desarrollan en múltiples etapas. Programas concurrentes encadenados modelan estas situaciones, pero su análisis es considerablemente más complejo.

Estos temas serán abordados en capítulos posteriores conforme desarrollemos modelos más sofisticados de aprendizaje y decisión.

### Conexiones con Capítulos Previos y Futuros

#### Conexión con Condicionamiento Clásico (Capítulos 8-11)

Los modelos de condicionamiento operante discutidos aquí son análogos estructurales de los modelos de condicionamiento clásico. Así como el modelo de Rescorla-Wagner especifica cómo la contingencia EC-EI controla valores asociativos V, la ecuación de Herrnstein especifica cómo la contingencia respuesta-refuerzo controla tasas de respuesta R.

Una diferencia fundamental es que en el caso operante, el organismo **controla activamente** la generación de experiencia. Esto transforma el aprendizaje en un sistema de retroalimentación dinámica: el comportamiento presente afecta las consecuencias, que a su vez modifican el comportamiento futuro. Esta dinámica será central en los modelos de aprendizaje por refuerzo que examinaremos posteriormente.

#### Anticipación de Modelos de Optimización (Capítulo X+1)

Este capítulo ha introducido la tensión entre maximización global y melioration (maximización local). En el próximo capítulo, desarrollaremos formalmente **modelos de optimización**, donde especificaremos funciones de utilidad, restricciones, y métodos para encontrar distribuciones óptimas de comportamiento.

Veremos que bajo ciertas funciones de utilidad (utilidad cóncava con rendimientos decrecientes), el equilibrio óptimo implica diversificación entre alternativas—análogo a igualación. Esto proporcionará una fundamentación normativa para igualación desde la perspectiva de teoría de optimización.

También examinaremos modelos de **maximización momentánea** y **melioration formalizada**, conectando las intuiciones conceptuales desarrolladas aquí con modelos matemáticos precisos.

#### Anticipación de Aprendizaje por Refuerzo Computacional

En capítulos posteriores de la segunda parte del libro, desarrollaremos formalmente los modelos de **aprendizaje por refuerzo** (Reinforcement Learning, RL) de la ciencia computacional. Estos modelos especifican cómo los organismos aprenden valores asociados con estados y acciones (valores Q), cómo actualizan estos valores con experiencia, y cómo traducen valores en decisiones.

Los conceptos introducidos aquí—funciones de retroalimentación, maximización versus melioration, igualación—reaparecerán en el contexto de algoritmos como Q-learning, Actor-Critic, y diferencias temporales (TD). La notación y conceptos desarrollados en este capítulo proporcionan los fundamentos para esos modelos más avanzados.

Por ejemplo, la actualización de valores en el modelo de Bush-Mosteller mencionado brevemente en la Parte 4 es matemáticamente idéntica a la regla de Q-learning para el caso especial de un solo estado. La conexión formal entre estos marcos será desarrollada explícitamente en capítulos posteriores.

### Relevancia para Neurociencia del Aprendizaje

Los principios de igualación y melioration no son solo abstracciones conductuales—tienen correlatos neurofisiológicos identificables. Investigaciones en neurociencia del aprendizaje han demostrado que las neuronas dopaminérgicas del mesencéfalo señalan **errores de predicción de recompensa**, exactamente análogo al término de error en el modelo de Bush-Mosteller y Q-learning.

Cuando un refuerzo es mejor de lo esperado (r > Q), las neuronas dopaminérgicas aumentan su tasa de disparo. Cuando es peor de lo esperado (r < Q), reducen su tasa. Esta señal de error se propaga a través del cerebro, actualizando valores asociados con estados y acciones—implementando neuralmente el proceso de aprendizaje por refuerzo.

Además, diferentes regiones cerebrales parecen representar diferentes componentes de los modelos de elección. El núcleo accumbens representa valores de recompensa esperada (análogo a Q). La corteza prefrontal orbitofrontal representa valores de resultado (magnitud, calidad). La corteza cingulada anterior está involucrada en la monitorización de conflicto y el ajuste conductual—funciones consistentes con melioration.

Estas conexiones entre modelos conductuales formales y sistemas neurofisiológicos subrayan que los principios descubiertos mediante análisis experimental del comportamiento no son meramente descriptivos—reflejan mecanismos computacionales implementados en circuitos cerebrales.

### Aplicaciones más allá del Laboratorio

Aunque los principios de igualación se descubrieron en contextos experimentales altamente controlados (cámaras operantes con palomas y ratas), su relevancia se extiende ampliamente:

**Economía Conductual:** Los humanos frecuentemente distribuyen esfuerzo económico (trabajo, tiempo) entre diferentes actividades de manera consistente con igualación. Por ejemplo, estudios han mostrado que la distribución de tiempo entre diferentes trabajos iguala aproximadamente sus salarios relativos (ajustando por otros factores como preferencias intrínsecas, distancia, etc.).

**Forrajeo Animal:** Organismos en ambientes naturales distribuyen tiempo entre diferentes parches de recursos de manera predicha por igualación de tasas de ganancia locales. Abejas visitando flores, aves buscando semillas, y predadores cazando presas muestran patrones consistentes con melioration.

**Adicción y Psicopatología:** La ecuación de Herrnstein ha sido usada para modelar elección entre drogas y reforzadores alternativos en estudios de adicción. El parámetro r₀ (refuerzos alternativos) juega un papel crucial: ambientes enriquecidos con fuentes alternativas de refuerzo reducen el comportamiento de auto-administración de drogas.

**Educación:** Estudiantes distribuyen tiempo de estudio entre diferentes materias de manera aproximadamente proporcional a las "recompensas" (calificaciones, interés intrínseco) asociadas con cada una. Comprender este principio puede informar diseños instruccionales que optimicen la distribución de esfuerzo estudiantil.

Estos ejemplos ilustran que los principios formales descubiertos mediante investigación básica tienen aplicabilidad genuina para entender y predecir comportamiento en contextos complejos del mundo real.

### Preguntas Abiertas y Direcciones Futuras

A pesar del progreso considerable, múltiples preguntas permanecen abiertas:

**1. Mecanismos de Integración Temporal:** ¿Cómo calculan los organismos las "tasas locales de refuerzo"? ¿Qué ventanas temporales usan? ¿Cómo se implementan estas computaciones neuralmente?

**2. Variabilidad Individual:** Hay variabilidad sustancial entre individuos en parámetros como sensibilidad (a) y sesgo (b). ¿Qué factores—genéticos, de desarrollo, experienciales—explican esta variabilidad?

**3. Generalización a Ambientes Complejos:** Los experimentos de laboratorio usan contingencias simples. ¿Cómo se aplican los principios de igualación y melioration en ambientes naturales con múltiples alternativas, consecuencias demoradas, y estructuras de dependencia complejas?

**4. Desarrollo Ontogenético:** ¿Cómo emerge la capacidad de igualar durante el desarrollo? ¿Los organismos juveniles muestran igualación, o requiere experiencia extensa?

**5. Evolución de Estrategias de Elección:** Desde una perspectiva evolutiva, ¿bajo qué condiciones ecológicas sería adaptativo igualar versus maximizar versus seguir otras estrategias? ¿La igualación es una adaptación específica, o un subproducto de mecanismos de aprendizaje más generales?

Estas preguntas guían la investigación actual en psicología del aprendizaje, economía conductual, neurociencia, y ecología evolutiva.

---

## TABLA RESUMEN: CONCEPTOS CLAVE

| **Concepto** | **Descripción** | **Ecuación/Forma Funcional** | **Contexto** |
|---|---|---|---|
| **Programa de Razón Variable (RV)** | Refuerzo después de un número variable de respuestas (promedio n) | r = R/n (lineal) | Produce tasas altas sostenidas |
| **Programa de Intervalo Variable (IV)** | Refuerzo disponible después de intervalos variables de tiempo | r ≈ r_max[1 - exp(-R/R₀)] (no-lineal) | Produce tasas moderadas estables |
| **Ecuación de Herrnstein** | Relación hiperbólica entre tasa de refuerzo y tasa de respuesta | R₁ = kr₁/(r₁ + r₀) | Respuesta individual; k = máximo, r₀ = alternativas |
| **Ley de Igualación (Simple)** | Razón de respuestas iguala razón de refuerzos | R₁/R₂ = r₁/r₂ | Elección concurrente IV-IV |
| **Igualación Generalizada** | Forma extendida con sensibilidad y sesgo | log(R₁/R₂) = a·log(r₁/r₂) + log(b) | a = sensibilidad; b = sesgo |
| **Igualación de Tasas Locales** | Igualar refuerzos por tiempo dedicado | r₁/T₁ = r₂/T₂ | Interpretación alternativa de igualación |
| **Maximización Global** | Maximizar tasa total de refuerzo | Max(r₁ + r₂) sujeto a restricciones | Predice igualación en IV-IV bajo ciertas condiciones |
| **Melioration** | Transferir tiempo a alternativa con mayor tasa local | Si r₁/T₁ > r₂/T₂ → aumentar T₁ | Maximización local; puede ser subóptimo globalmente |
| **Undermatching** | Menor sensibilidad de lo predicho por igualación | a < 1 en ecuación generalizada | Común; influido por COD, discriminabilidad |
| **Changeover Delay (COD)** | Período después de cambiar durante el cual no hay refuerzo | Típicamente 1-3 seg | Reduce undermatching; simula costo de cambio |

---

## SÍNTESIS CONCEPTUAL

Los programas de reforzamiento, conceptualizados como funciones de retroalimentación, especifican cómo el comportamiento genera consecuencias. La estructura matemática de estas funciones—lineal para programas RV, no-lineal para IV—determina las estrategias óptimas de distribución conductual. La ecuación de Herrnstein proporciona una formalización cuantitativa elegante de cómo el refuerzo controla la tasa de respuesta, unificando el análisis de respuestas individuales y situaciones de elección.

El fenómeno de igualación revela que los organismos distribuyen comportamiento proporcionalmente a las consecuencias obtenidas, un principio cuantitativo notable por su generalidad. Las desviaciones sistemáticas (undermatching) se capturan mediante extensiones que incorporan sensibilidad y sesgo. La interpretación teórica de igualación permanece debatida: puede emerger de maximización global bajo restricciones específicas, o de reglas locales simples (melioration) que no requieren representación de medidas globales. Evidencia experimental favorece melioration en muchos contextos, aunque efectos de contexto sugieren sensibilidad a variables globales.

La comprensión de estos mecanismos no solo proporciona una base cuantitativa para analizar cómo el refuerzo controla el comportamiento, sino que establece fundamentos conceptuales y matemáticos para modelos más avanzados de optimización conductual y aprendizaje por refuerzo que examinaremos en capítulos subsecuentes.

---

## LECTURAS RECOMENDADAS

### Lecturas Fundamentales (Comprensión Básica)

**Herrnstein, R. J. (1970).** On the law of effect. *Journal of the Experimental Analysis of Behavior*, 13, 243-266.
- Artículo seminal que introduce la ecuación de Herrnstein y la ley de igualación. Altamente accesible y conceptualmente claro.

**Williams, B. A. (1988).** Reinforcement, choice, and response strength. En R. C. Atkinson et al. (Eds.), *Stevens' Handbook of Experimental Psychology* (2nd ed., Vol. 2, pp. 167-244). New York: Wiley.
- Revisión comprehensiva y excelente de modelos cuantitativos de elección. Ligeramente técnica pero muy completa.

**Davison, M., & McCarthy, D. (1988).** *The Matching Law: A Research Review.* Hillsdale, NJ: Erlbaum.
- Libro completo dedicado exclusivamente a igualación. Más técnico que los anteriores, pero la fuente definitiva sobre el tema.

### Lecturas Avanzadas (Profundización Teórica)

**Rachlin, H., Battalio, R., Kagel, J., & Green, L. (1981).** Maximization theory in behavioral psychology. *Behavioral and Brain Sciences*, 4, 371-388.
- Artículo teórico influyente argumentando que igualación emerge de maximización. Incluye comentarios de múltiples investigadores.

**Herrnstein, R. J., & Vaughan, W. (1980).** Melioration and behavioral allocation. En J. E. R. Staddon (Ed.), *Limits to Action: The Allocation of Individual Behavior* (pp. 143-176). New York: Academic Press.
- Presentación original de la teoría de melioration con evidencia empírica de conducta subóptima.

**Baum, W. M. (1974).** On two types of deviation from the matching law: Bias and undermatching. *Journal of the Experimental Analysis of Behavior*, 22, 231-242.
- Artículo técnico que introduce la forma generalizada de la ley de igualación con parámetros de sensibilidad y sesgo.

### Aplicaciones y Extensiones

**Madden, G. J., & Bickel, W. K. (Eds.) (2010).** *Impulsivity: The Behavioral and Neurological Science of Discounting.* Washington, DC: APA.
- Compilación de capítulos sobre descuento temporal y auto-control, extendiendo modelos de elección a consecuencias demoradas.

**Green, L., & Freed, D. E. (1993).** The substitutability of reinforcers. *Journal of the Experimental Analysis of Behavior*, 60, 141-158.
- Extensión de modelos de elección incorporando economía conductual: sustitutibilidad y complementariedad de reforzadores.

**Belke, T. W. (1992).** Stimulus preference and the transitivity of preference. *Animal Learning & Behavior*, 20, 401-406.
- Experimento crucial demostrando efectos de contexto que contradicen modelos simples de valor independiente.

### Conexiones con Neurociencia

**Schultz, W., Dayan, P., & Montague, P. R. (1997).** A neural substrate of prediction and reward. *Science*, 275, 1593-1599.
- Artículo fundamental conectando señales dopaminérgicas con errores de predicción en modelos de aprendizaje por refuerzo.

**Daw, N. D., & Doya, K. (2006).** The computational neurobiology of learning and reward. *Current Opinion in Neurobiology*, 16, 199-204.
- Revisión de cómo sistemas cerebrales implementan algoritmos de aprendizaje por refuerzo.

### Lecturas Históricas

**Skinner, B. F. (1938).** *The Behavior of Organisms: An Experimental Analysis.* New York: Appleton-Century-Crofts.
- Libro fundacional que introduce el análisis experimental del comportamiento y los programas básicos de reforzamiento.

**Herrnstein, R. J. (1961).** Relative and absolute strength of response as a function of frequency of reinforcement. *Journal of the Experimental Analysis of Behavior*, 4, 267-272.
- El experimento original que descubrió la ley de igualación. Breve, claro, históricamente importante.

---

**FIN DEL CAPÍTULO X**
