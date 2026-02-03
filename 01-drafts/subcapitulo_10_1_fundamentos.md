# CAPÍTULO X - SUBCAPÍTULO 10.1
# FUNDAMENTOS DE LOS PROGRAMAS DE REFORZAMIENTO

---

## INTRODUCCIÓN AL CAPÍTULO X

En los Capítulos 8 a 11, estudiamos cómo los organismos aprenden relaciones causales entre eventos en su entorno: qué estímulos predicen refuerzos (Capítulos 8-9) y cómo se forman asociaciones estímulo-consecuencia a través del condicionamiento (Capítulos 10-11). El modelo de Rescorla-Wagner nos mostró cómo los valores asociativos V(E,O) se actualizan con la experiencia, permitiendo a los organismos anticipar eventos biológicamente relevantes.

Sin embargo, conocer que un estímulo predice un refuerzo es solo parte del problema adaptativo que enfrentan los organismos. El problema complementario—igualmente fundamental—es cómo traducir ese conocimiento en distribuciones óptimas de acción. Un organismo puede saber perfectamente que la respuesta R₁ produce r₁ refuerzos por minuto y que R₂ produce r₂ refuerzos por minuto. Pero ¿cuántas respuestas debe asignar a cada opción? ¿Cuánto tiempo dedicar a cada alternativa? ¿Debe responder exclusivamente a la opción más rica, o distribuir sus respuestas proporcionalmente?

Este capítulo aborda precisamente estas cuestiones, estudiando cómo los **programas de reforzamiento**—las reglas que especifican qué respuestas producen refuerzos—controlan la distribución temporal y numérica del comportamiento. El capítulo se divide en cinco subcapítulos que construyen progresivamente nuestra comprensión:

**Subcapítulo 10.1 (este subcapítulo)** establece los fundamentos, examinando los programas básicos de reforzamiento como funciones de retroalimentación que relacionan respuestas con refuerzos.

**Subcapítulo 10.2** documenta el descubrimiento empírico de la Ley de Igualación: cuando múltiples opciones están disponibles simultáneamente, los organismos distribuyen sus respuestas proporcionalmente a los refuerzos obtenidos.

**Subcapítulo 10.3** presenta la ecuación de Herrnstein, una formalización cuantitativa de la "ley del efecto relativa" que explica por qué ocurre la igualación.

**Subcapítulo 10.4** examina las desviaciones sistemáticas de la igualación perfecta (undermatching, bias) y los factores experimentales que las modulan.

**Subcapítulo 10.5** introduce diferentes interpretaciones teóricas del fenómeno de igualación—maximización global versus reglas locales—y examina efectos de estructura temporal y contexto.

La comprensión de estos mecanismos no solo completa nuestra visión de cómo el refuerzo controla el comportamiento, sino que establece los fundamentos para analizar, en capítulos posteriores (X+1: Modelos de Optimización Molar; X+2: Modelos de Optimización Local), modelos más sofisticados de optimización conductual y aprendizaje por refuerzo en ambientes dinámicos.

---

## DE THORNDIKE A SKINNER: EL ESTUDIO SISTEMÁTICO DEL REFORZAMIENTO

La investigación experimental del efecto del refuerzo sobre el comportamiento tiene sus raíces en los estudios pioneros de Edward Thorndike a finales del siglo XIX. En su famosa "caja problema", Thorndike observó que los gatos aprendían gradualmente a escapar mediante respuestas que producían consecuencias favorables—una observación que formalizó como la **Ley del Efecto**: "De varias respuestas hechas a la misma situación, aquellas que van acompañadas o seguidas de cerca por satisfacción para el animal quedarán, en igualdad de condiciones, más firmemente conectadas con la situación; de modo que, cuando ocurre nuevamente, será más probable que ocurran." Esta ley estableció el principio fundamental que consecuencias favorables fortalecen las respuestas que las preceden.

Sin embargo, fue Clark Hull quien, en las décadas de 1930 y 1940, intentó por primera vez una formulación matemática rigurosa de cómo el refuerzo afecta la "fuerza del hábito" (s_HR en su notación). Hull propuso que cada refuerzo incrementaba la asociación estímulo-respuesta de forma acumulativa:

**s_HR = M(1 - e^(-KN))**

donde N es el número de refuerzos, M es la asíntota de aprendizaje, y K es una constante de tasa. Aunque matemáticamente elegante, esta formulación enfrentaba serias dificultades empíricas. En particular, predecía que la fuerza del hábito dependería solo del número acumulado de refuerzos, independientemente del contexto o de la disponibilidad de respuestas alternativas—una predicción que las investigaciones posteriores refutaron consistentemente.

### El Cambio Paradigmático de Skinner

El cambio fundamental vino con B.F. Skinner, quien en su libro seminal *The Behavior of Organisms* (1938) introdujo una perspectiva radicalmente diferente. En lugar de conceptualizar el refuerzo como algo que fortalece asociaciones internas hipotéticas (el enfoque de Hull), Skinner propuso estudiar las **relaciones funcionales** entre el comportamiento observable y sus consecuencias ambientales directamente medibles. Este cambio de perspectiva—del "dentro del organismo" al "organismo en su ambiente"—permitió un análisis cuantitativo más directo y empíricamente verificable de cómo diferentes contingencias de refuerzo controlan el comportamiento.

Skinner argumentó que el objetivo de la psicología conductual no debería ser inferir procesos internos no observables, sino establecer las leyes cuantitativas que gobiernan las relaciones entre variables ambientales (estímulos, contingencias de refuerzo) y conductuales (frecuencia, temporalización, distribución de respuestas). Esta perspectiva funcional se resume en su concepto de **contingencia de tres términos**: estímulo discriminativo (S^D) → respuesta (R) → consecuencia (C). El refuerzo controla el comportamiento no fortaleciendo una conexión interna, sino alterando la probabilidad futura de la respuesta en presencia del estímulo discriminativo.

### La Cámara Operante y el Análisis Experimental del Comportamiento

Para implementar su programa de investigación, Skinner desarrolló el protocolo experimental que dominaría las siguientes décadas de investigación: la **cámara operante** (posteriormente llamada "caja de Skinner" por otros investigadores, aunque Skinner prefería el término "cámara operante" para enfatizar que estudiaba comportamiento operante—comportamiento que opera sobre el ambiente para producir consecuencias).

En su versión más común para palomas, la cámara contiene:
- Un disco iluminado (tecla) que puede ser picoteado
- Un dispensador automático de grano
- Equipamiento electrónico para registrar respuestas con precisión milimétrica
- Control programático de las contingencias de refuerzo

Para ratas, el manipulandum es típicamente una palanca que puede ser presionada, con agua o pellets de comida como reforzadores.

Esta tecnología experimental permitió el análisis cuantitativo sistemático de cómo diferentes **programas de reforzamiento**—las reglas que especifican qué respuestas se refuerzan y cuándo—controlan patrones específicos de comportamiento. A diferencia de los estudios previos que usaban reforzamiento continuo (cada respuesta produce refuerzo), Skinner exploró sistemáticamente programas de **reforzamiento intermitente**, donde solo algunas respuestas producen refuerzo según reglas definidas.

---

## LOS CUATRO PROGRAMAS BÁSICOS DE REFORZAMIENTO

Skinner identificó cuatro programas básicos que han sido objeto de análisis intensivo durante más de ochenta años. Estos programas difieren en dos dimensiones ortogonales:

1. **Criterio para reforzamiento:** ¿Se basa en el **número de respuestas** (programas de razón) o en el **tiempo transcurrido** (programas de intervalo)?

2. **Variabilidad del requisito:** ¿Es el requisito **fijo** (constante de ensayo a ensayo) o **variable** (cambiante impredeciblemente)?

Esta clasificación bidimensional genera una taxonomía de 2×2 = 4 programas básicos:

### 1. Razón Fija (RF)

**Contingencia:** Se refuerza cada n-ésima respuesta. Por ejemplo, RF 10 significa que cada décima respuesta produce refuerzo (respuestas 10, 20, 30, 40, etc.).

**Patrón conductual característico:**
- Tasas de respuesta muy altas durante el trabajo hacia el refuerzo
- **Pausa post-refuerzo** característica: después de obtener refuerzo, el organismo típicamente pausa antes de reanudar respuestas
- La duración de la pausa post-refuerzo aumenta con el tamaño de la razón (RF 100 produce pausas más largas que RF 10)
- Una vez que la respuesta se reanuda, la tasa es alta y estable hasta el siguiente refuerzo

**Ejemplos cotidianos:** 
- Trabajo a destajo: un cosechador que recibe pago fijo por cada caja de fruta recolectada responde bajo un programa de razón fija
- Comisiones de ventas: un vendedor que recibe bonificación por cada 5 ventas completadas
- Tarjetas de fidelidad: "compra 10 cafés, obtén 1 gratis"

### 2. Razón Variable (RV)

**Contingencia:** El número de respuestas requeridas para refuerzo varía impredeciblemente alrededor de un promedio. RV 50 significa que en promedio se requieren 50 respuestas por refuerzo, pero en una ocasión pueden ser 30, en otra 70, en otra 45, etc. La secuencia específica es determinada por el experimentador (típicamente mediante distribución pseudo-aleatoria).

**Patrón conductual característico:**
- Este programa produce las **tasas de respuesta más altas y sostenidas** de todos los programas básicos
- **Sin pausas post-refuerzo:** el organismo continúa respondiendo inmediatamente después de recibir refuerzo
- Tasa de respuesta muy estable y resistente a extinción
- La variabilidad del programa previene que el organismo "anticipe" cuándo vendrá el siguiente refuerzo

**Ejemplos cotidianos:**
- Máquinas tragamonedas (slot machines): operan bajo programas de razón variable, produciendo respuesta persistente
- Llamadas de ventas telefónicas: se requiere número variable e impredecible de llamadas antes de lograr una venta
- Pesca en río con caña: se requiere número variable de lanzamientos antes de capturar un pez

### 3. Intervalo Fijo (IF)

**Contingencia:** Se refuerza la **primera respuesta** que ocurre después de que ha transcurrido un período fijo de tiempo desde el último refuerzo. IF 60-seg significa que después de cada refuerzo, debe pasar al menos 60 segundos antes de que otra respuesta pueda ser reforzada. Crucialmente, el tiempo corre independientemente del comportamiento del organismo—no se "reinicia" con cada respuesta.

**Patrón conductual característico:**
- **Patrón de "festón" (scallop):** pausa post-refuerzo seguida de aceleración progresiva conforme se aproxima el momento de disponibilidad del refuerzo
- En intervalos largos, la pausa puede ocupar gran proporción del intervalo
- Aceleración terminal: conforme se aproxima el final del intervalo, la tasa de respuesta aumenta rápidamente
- Este patrón sugiere que el organismo "rastrea temporalmente" la disponibilidad del refuerzo

**Ejemplos cotidianos:**
- Revisar el horno durante la cocción: el alimento no estará listo hasta que pase el tiempo programado, pero verificar antes no acelera el proceso
- Verificar el correo que llega a una hora determinada cada día
- Esperar el autobús que viene cada 15 minutos: la frecuencia de "mirar hacia la calle" aumenta conforme se aproxima la hora programada

### 4. Intervalo Variable (IV)

**Contingencia:** El tiempo requerido desde el último refuerzo hasta que el siguiente está disponible varía impredeciblemente alrededor de un promedio. IV 60-seg significa que en promedio transcurren 60 segundos entre refuerzos disponibles, pero el intervalo específico varía (e.g., 30 seg, 90 seg, 45 seg, 75 seg, etc.). Una vez que un refuerzo está disponible, permanece disponible hasta que el organismo emite una respuesta.

**Patrón conductual característico:**
- Tasas de respuesta moderadas (más bajas que RV, más altas que IF comparable)
- **Muy estables:** minimal variabilidad intra-sesión
- **Sin pausas post-refuerzo:** respuesta continua después de reforzamiento
- La impredecibilidad del tiempo hasta refuerzo disponible previene pausas estratégicas
- Alta resistencia a extinción

**Ejemplos cotidianos:**
- Pesca: los peces muerden a intervalos impredecibles; más tiempo pescando aumenta probabilidad de captura, pero no garantiza nada
- Revisar email/redes sociales: mensajes interesantes llegan a intervalos variables impredecibles
- Caza: la presa aparece a intervalos variables

### Tabla Comparativa de Programas Básicos

| Programa | Criterio | Requisito | Tasa de Respuesta | Pausa Post-Refuerzo | Patrón Temporal |
|----------|----------|-----------|-------------------|---------------------|-----------------|
| **RF** | Número respuestas | Fijo (cada n respuestas) | Muy alta | Sí, aumenta con n | Lineal durante trabajo |
| **RV** | Número respuestas | Variable (promedio n) | Máxima | No | Constante y sostenida |
| **IF** | Tiempo | Fijo (cada t segundos) | Moderada | Sí | Festón (scallop) |
| **IV** | Tiempo | Variable (promedio t) | Moderada | No | Constante y estable |

---

## PROGRAMAS DE REFORZAMIENTO COMO FUNCIONES DE RETROALIMENTACIÓN

Más allá de la descripción cualitativa de los patrones conductuales que generan, los programas de reforzamiento pueden analizarse formalmente como **funciones de retroalimentación** que especifican la relación matemática entre respuestas emitidas (R) y refuerzos obtenidos (r). Esta perspectiva, desarrollada principalmente por William Baum (1973) y John Staddon (1979), permite un análisis cuantitativo de cómo cada programa transforma comportamiento en consecuencias.

Conceptualmente, podemos representar cualquier programa de reforzamiento como una función:

**r = f(R)**

donde:
- R = número de respuestas (o tasa de respuesta, respuestas/minuto)
- r = número de refuerzos obtenidos (o tasa de refuerzo, refuerzos/minuto)
- f(·) = función de retroalimentación específica del programa

Esta formalización es poderosa porque diferentes programas corresponden a diferentes funciones matemáticas con propiedades distintas. Examinaremos las dos formas funcionales más importantes: lineal (característica de programas RV) y no-lineal hiperbólica (característica de programas IV).

### Programas de Razón Variable: Retroalimentación Lineal

Para un programa RV n, la contingencia establece que, en promedio, cada n respuestas producen un refuerzo. Esto significa que la probabilidad de refuerzo por cada respuesta individual es constante e igual a:

**p = 1/n**

Por ejemplo, en RV 50, cada respuesta tiene probabilidad p = 1/50 = 0.02 de ser reforzada.

Por lo tanto, si un organismo emite R respuestas, el **número esperado** de refuerzos obtenidos es:

**r = R × p = R × (1/n) = R/n**

Esta función de retroalimentación es **perfectamente lineal**: cada respuesta adicional incrementa los refuerzos obtenidos en una cantidad constante (1/n). La pendiente de esta función, 1/n, representa la "densidad de refuerzo" del programa:
- RV 50 tiene pendiente 1/50 = 0.02 (dos refuerzos por cada 100 respuestas)
- RV 100 tiene pendiente 1/100 = 0.01 (un refuerzo por cada 100 respuestas)
- RV 25 tiene pendiente 1/25 = 0.04 (cuatro refuerzos por cada 100 respuestas)

**Implicaciones de la linealidad:**

Esta linealidad tiene implicaciones profundas para la optimalidad conductual:

1. **No hay rendimientos decrecientes:** Cada respuesta adicional produce el mismo incremento marginal en refuerzos obtenidos. La respuesta número 1,000 es tan "productiva" como la respuesta número 1.

2. **Maximización simple:** Desde una perspectiva de maximización de refuerzos, la estrategia óptima es responder a la tasa más alta posible—más respuestas siempre significan proporcionalmente más refuerzos.

3. **Sin punto de saturación:** A diferencia de programas IV (como veremos), no hay tasa de respuesta donde incrementos adicionales dejan de producir beneficios.

### Programas de Intervalo Variable: Retroalimentación No-Lineal

Los programas IV presentan una estructura de retroalimentación fundamentalmente diferente. En un programa IV, los refuerzos se hacen **disponibles** a intervalos impredecibles independientemente del comportamiento del organismo, pero requieren al menos una respuesta para ser **colectados**. Una vez que un refuerzo está disponible, permanece disponible hasta que el organismo responde y lo recolecta ("collected holding" en la terminología técnica).

Esta estructura crea una dinámica no-lineal: responder más rápido aumenta la probabilidad de "detectar" cuando un refuerzo está disponible, pero con rendimientos decrecientes. Un organismo que responde muy lentamente se perderá muchos refuerzos disponibles; pero un organismo que responde muy rápido desperdicia esfuerzo en respuestas que no pueden ser reforzadas porque no hay refuerzo disponible en ese momento.

#### Derivación de la Función de Retroalimentación IV (MEJORA INCORPORADA)

Para derivar la función de retroalimentación de un IV, consideremos la dinámica temporal del programa. Supongamos que el programa establece refuerzos disponibles a una tasa r_max (por ejemplo, IV 60-seg tiene r_max = 1 refuerzo/minuto = 60 refuerzos/hora). El organismo responde a una tasa R (respuestas/minuto).

**Lógica probabilística:**

Los refuerzos se hacen disponibles según un **proceso de Poisson** con tasa r_max. Entre dos respuestas consecutivas del organismo, transcurre en promedio un tiempo IRT (inter-response time) dado por:

**IRT_promedio = 1/R**

Por ejemplo, si R = 30 respuestas/minuto, entonces IRT_promedio = 1/30 minuto = 2 segundos.

Durante este intervalo entre respuestas, la probabilidad de que al menos un refuerzo se haya hecho disponible es aproximadamente:

**P(refuerzo disponible) ≈ r_max × IRT_promedio = r_max × (1/R)**

Para tasas bajas de respuesta (IRT grandes), esta probabilidad se aproxima a 1—casi siempre hay un refuerzo disponible cuando el organismo finalmente responde. Para tasas altas (IRT pequeños), la probabilidad es menor—el organismo "verifica" tan frecuentemente que usualmente no ha pasado suficiente tiempo para que un refuerzo se haga disponible.

La tasa de refuerzo obtenida es el producto de la tasa de respuesta por la probabilidad de refuerzo:

**r ≈ R × P(refuerzo disponible) = R × r_max/R = r_max**

Pero esta aproximación es demasiado simple. Un análisis más riguroso usando teoría de procesos estocásticos (que va más allá del nivel de este texto) muestra que la función exacta tiene forma exponencial:

**r ≈ r_max[1 - exp(-R/R₀)]**

donde R₀ es un parámetro relacionado con la tasa programada del IV (típicamente R₀ ≈ r_max para IVs estándar).

**Intuición de la forma exponencial:**

- Para tasas **muy bajas** de respuesta (R << R₀): exp(-R/R₀) ≈ 1 - R/R₀, por lo tanto r ≈ r_max × (R/R₀) ≈ R. La función es aproximadamente lineal—respuestas adicionales incrementan refuerzos proporcionalmente.

- Para tasas **muy altas** de respuesta (R >> R₀): exp(-R/R₀) ≈ 0, por lo tanto r ≈ r_max. La función se aplana asintóticamente—incrementos adicionales en R producen incrementos cada vez menores en r, aproximándose a la tasa máxima r_max sin alcanzarla nunca.

#### Aproximación Hiperbólica Simplificada

Una forma más simple, frecuentemente usada en análisis teóricos y que captura las mismas propiedades esenciales, es la **aproximación hiperbólica**:

**r = r_max × R/(R + c)**

donde c es un parámetro que determina la curvatura de la función (típicamente c ≈ r_max).

Esta ecuación tiene las siguientes propiedades:

1. **Cuando R → 0:** r → 0 (sin respuestas, sin refuerzos colectados)
2. **Cuando R → ∞:** r → r_max (tasa asintótica máxima)
3. **Cuando R = c:** r = r_max/2 (punto medio de la curva)

La derivada de esta función es:

**dr/dR = r_max × c/(R + c)²**

que **disminuye** conforme R aumenta. Esto formaliza el concepto de **rendimientos decrecientes**: cada respuesta adicional incrementa r menos que la respuesta anterior.

### Implicaciones de las Diferentes Funciones de Retroalimentación

La diferencia fundamental entre las funciones de retroalimentación lineales (RV) y no-lineales (IV) tiene profundas implicaciones para el comportamiento óptimo:

#### Programas RV (Lineales):

Dado que cada respuesta contribuye igualmente a la obtención de refuerzos, la estrategia óptima desde una perspectiva de maximización es **responder continuamente a la tasa más alta posible**. No hay "costo de oportunidad" por responder más: más respuestas siempre significan proporcionalmente más refuerzos.

Esta predicción es consistente con los datos empíricos: los organismos responden a tasas muy altas en programas RV, limitados solo por restricciones fisiológicas (fatiga, velocidad de ejecución motora).

#### Programas IV (No-lineales):

En contraste, en un programa IV existe un claro **costo de oportunidad**: respuestas excesivamente rápidas desperdician esfuerzo sin incrementar proporcionalmente los refuerzos obtenidos. La tasa óptima de respuesta en un IV depende del balance entre:
- **Asegurar la recolección de refuerzos disponibles** (responder suficientemente rápido)
- **No desperdiciar esfuerzo en respuestas innecesarias** (no responder excesivamente rápido)

Como veremos en secciones posteriores, esta diferencia estructural explica por qué los organismos responden mucho más rápido en programas RV que en programas IV comparables (misma tasa promedio de refuerzo). En un IV 60-seg y un RV 60, ambos producen aproximadamente 1 refuerzo/minuto, pero las tasas de respuesta observadas son típicamente 3-5 veces mayores en RV que en IV.

---

## TRANSICIÓN AL SUBCAPÍTULO 10.2

Hemos establecido que los programas de reforzamiento pueden conceptualizarse como funciones matemáticas que transforman respuestas en refuerzos. Los programas RV producen retroalimentación lineal (r = R/n), mientras que los IV producen retroalimentación no-lineal con rendimientos decrecientes (r = r_max × R/(R + c)). Esta estructura matemática es fundamental para entender cómo el comportamiento genera consecuencias y, eventualmente, para analizar la optimalidad conductual.

Sin embargo, los ambientes naturales—y muchos experimentos de laboratorio—presentan no una sola opción aislada, sino **múltiples alternativas disponibles simultáneamente**. Un ave puede forrajear en dos parcelas diferentes; un humano puede alternar entre dos tareas laborales; una paloma en una cámara operante tiene acceso a dos teclas iluminadas, cada una asociada con su propio programa de reforzamiento.

¿Cómo distribuyen los organismos su comportamiento cuando enfrentan múltiples alternativas concurrentes? ¿Dedican todo su tiempo a la opción más rica (maximización exclusiva)? ¿Alternan al azar? ¿Distribuyen su comportamiento de alguna forma sistemática relacionada con las tasas de refuerzo?

Esta pregunta llevó a Richard Herrnstein, en 1961, a realizar un experimento que revelaría uno de los principios cuantitativos más robustos y sorprendentes en el análisis experimental del comportamiento. El siguiente subcapítulo examina este descubrimiento: la **Ley de Igualación**.

---

## CONCEPTOS CLAVE

- **Programas de reforzamiento:** Reglas que especifican qué respuestas producen refuerzos y cuándo
- **Cuatro programas básicos:** RF, RV (basados en número); IF, IV (basados en tiempo)
- **Razón Fija (RF):** Cada n-ésima respuesta reforzada; produce pausas post-refuerzo
- **Razón Variable (RV):** Promedio de n respuestas por refuerzo; tasa más alta y sostenida
- **Intervalo Fijo (IF):** Primera respuesta después de tiempo fijo; patrón de festón
- **Intervalo Variable (IV):** Primera respuesta después de tiempo variable; tasa estable sin pausas
- **Función de retroalimentación:** Relación matemática r = f(R) entre respuestas y refuerzos
- **Retroalimentación lineal (RV):** r = R/n, cada respuesta contribuye igualmente
- **Retroalimentación no-lineal (IV):** r = r_max × R/(R + c), rendimientos decrecientes
- **Rendimientos decrecientes:** Incrementos en respuesta producen incrementos cada vez menores en refuerzo

---

## OBJETIVOS DE APRENDIZAJE

Al completar este subcapítulo, deberías ser capaz de:

1. **Distinguir** entre programas de razón e intervalo, y entre programas fijos y variables
2. **Describir** los patrones conductuales característicos de cada uno de los cuatro programas básicos
3. **Explicar** la diferencia conceptual entre el enfoque de Hull (fuerza del hábito interna) y el enfoque de Skinner (relaciones funcionales ambientales)
4. **Representar** programas de reforzamiento como funciones de retroalimentación matemáticas
5. **Contrastar** retroalimentación lineal (RV) versus no-lineal (IV) y sus implicaciones para comportamiento óptimo
6. **Predecir** cualitativamente cómo cambios en parámetros de programas (n para RV, t para IV) afectarán tasas de refuerzo obtenidas
7. **Explicar** por qué programas IV tienen rendimientos decrecientes mientras que RV no

---

**FIN DEL SUBCAPÍTULO 10.1**
