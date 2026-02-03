# CAPÍTULO X - SUBCAPÍTULO 10.3
# LA ECUACIÓN DE HERRNSTEIN: EXPLICANDO IGUALACIÓN

---

## INTRODUCCIÓN

En el Subcapítulo 10.2 documentamos uno de los hallazgos empíricos más robustos en el análisis experimental del comportamiento: la Ley de Igualación. Cuando palomas, ratas, humanos y otras especies enfrentan dos alternativas concurrentes—cada una reforzada en su propio programa de intervalo variable—distribuyen sus respuestas proporcionalmente a los refuerzos obtenidos: B₁/B₂ = r₁/r₂. Este patrón demostró ser notablemente general, replicándose en múltiples especies, tipos de respuestas, reforzadores, y procedimientos experimentales.

Sin embargo, documentar un fenómeno empírico no es explicarlo. La pregunta teórica fundamental permanece: ¿Por qué los organismos igualan? ¿Qué principio subyacente produce este patrón observable? ¿Es igualación el resultado de alguna "ley del efecto" más fundamental que opera en situaciones de elección?

Richard Herrnstein abordó esta pregunta en 1970, desarrollando lo que llamó la "Ley del Efecto Relativa". Su objetivo era ambicioso: crear una teoría cuantitativa general del control conductual por el refuerzo que, cuando se aplicara a situaciones de elección concurrente, derivara matemáticamente la igualación como una consecuencia lógica. Este subcapítulo examina esta teoría: la ecuación de Herrnstein. Veremos cómo surge de datos empíricos, cómo puede derivarse conceptualmente de principios simples, y—crucialmente—cómo predice igualación cuando se aplica a situaciones de elección concurrente.

---

## DE THORNDIKE A HERRNSTEIN: FORMALIZANDO LA LEY DEL EFECTO

### La Búsqueda de una Forma Funcional

La investigación experimental del efecto del refuerzo sobre el comportamiento tiene sus raíces en los estudios pioneros de Edward Thorndike a finales del siglo XIX. En su famosa "caja problema", Thorndike observó que los gatos aprendían gradualmente a escapar mediante respuestas que producían consecuencias favorables—una observación que formalizó como la **Ley del Efecto**: "las respuestas seguidas por satisfacción tienden a repetirse".

Sin embargo, la formulación de Thorndike era fundamentalmente cualitativa. No especificaba la forma matemática de la relación entre refuerzo y comportamiento. ¿Cómo exactamente los refuerzos "fortalecen" las respuestas? ¿Es esta relación lineal, exponencial, logarítmica?

Clark Hull fue quien, en las décadas de 1930 y 1940, intentó por primera vez una formulación matemática rigurosa. Hull propuso que cada refuerzo incrementaba la "fuerza del hábito" de forma acumulativa, siguiendo una función exponencial. Sin embargo, su formulación enfrentaba serias dificultades empíricas: no predecía correctamente cómo variaba la tasa de respuesta con diferentes tasas de refuerzo.

B.F. Skinner adoptó un enfoque radicalmente diferente. En lugar de postular construcciones hipotéticas internas como "fuerza del hábito", Skinner propuso estudiar directamente las **relaciones funcionales** entre el comportamiento observable y sus consecuencias ambientales. Este cambio de perspectiva—del "dentro del organismo" al "organismo en su ambiente"—permitió un análisis cuantitativo más directo. Sin embargo, Skinner deliberadamente evitó comprometerse con formas matemáticas específicas, manteniendo un enfoque descriptivo.

El avance crucial vino con Richard Herrnstein en la década de 1960. Herrnstein combinó la búsqueda de Hull de una formulación matemática con el análisis funcional de Skinner. Su innovación fundamental fue proponer que la fuerza del efecto es **relativa**, no absoluta: lo que importa no es cuánto refuerzo obtiene una respuesta en términos absolutos, sino cuánto obtiene en relación con todas las demás fuentes de refuerzo disponibles para el organismo.

---

## EVIDENCIA EMPÍRICA: LOS EXPERIMENTOS DE CATANIA Y REYNOLDS

Para entender la propuesta de Herrnstein, debemos primero examinar los datos que la motivaron. Catania y Reynolds (1968) realizaron un experimento elegante con palomas en el que variaron sistemáticamente la tasa de refuerzo en un programa de intervalo variable (IV) manteniendo constantes otras variables. En cada condición experimental, una paloma tenía acceso a un solo disco iluminado que operaba bajo un programa IV específico. Los experimentadores variaron la tasa programada del IV a través de diferentes condiciones—IV 30-seg, IV 60-seg, IV 120-seg, etc.—y midieron la tasa de respuesta en estado estable para cada valor.

Los resultados revelaron una relación sistemática con dos características fundamentales:

**1. Rendimientos decrecientes:** Conforme aumentaba la tasa de refuerzo programada, la tasa de respuesta también aumentaba, pero con incrementos progresivamente menores. La función no era lineal. Por ejemplo, pasar de IV 120-seg a IV 60-seg (duplicando la tasa de refuerzo) no duplicaba la tasa de respuesta—el incremento era menor que el doble.

**2. Asíntota finita:** Para tasas muy altas de refuerzo, la tasa de respuesta se aproximaba a un valor máximo finito; no crecía indefinidamente. Existía un límite superior a qué tan rápido las palomas podían responder, determinado por restricciones físicas y fisiológicas.

Estas dos características—rendimientos decrecientes y asíntota finita—son las propiedades distintivas de una función hiperbólica. Herrnstein propuso que la forma matemática más parsimoniosa que capturaba estos datos era:

**R = kr/(r + R_e)**

donde:
- **R** es la tasa de respuesta (respuestas por minuto)
- **r** es la tasa de refuerzo obtenida (refuerzos por minuto)
- **k** es un parámetro que representa la tasa máxima de respuesta posible
- **R_e** es un parámetro que representa los "refuerzos de otras fuentes"

Esta ecuación capturaba elegantemente ambas características observadas: cuando r es pequeño comparado con R_e, la función es aproximadamente lineal (R ≈ kr/R_e); cuando r es muy grande, R se aproxima asintóticamente a k.

---

## LA ECUACIÓN DE HERRNSTEIN: INTERPRETACIÓN DE LOS PARÁMETROS

### El Parámetro k: Capacidad Conductual

El parámetro **k** representa la tasa de respuesta asintótica—el máximo absoluto que el organismo podría alcanzar si toda su capacidad conductual se dedicara a esa respuesta. Matemáticamente, cuando la tasa de refuerzo r es muy grande (r >> R_e), la ecuación se aproxima a:

R ≈ kr/(r) = k

Este parámetro está limitado por restricciones físicas y fisiológicas. Hay un límite superior a qué tan rápido un organismo puede responder, determinado por:

- El tiempo requerido para ejecutar cada respuesta (la topografía motora)
- Limitaciones biomecánicas (velocidad de contracción muscular, tiempo de recuperación)
- Restricciones de procesamiento perceptual-motor

Empíricamente, k varía entre organismos y tipos de respuestas:

- **Palomas picando un disco:** k típicamente está en el rango de 200-300 respuestas por minuto
- **Ratas presionando una palanca:** k suele ser menor, alrededor de 100-150 respuestas por minuto
- **Humanos en tareas motoras simples:** k puede ser considerablemente más alto, dependiendo de la respuesta específica

Es crucial notar que **k es una constante del organismo y la respuesta**, no del programa de reforzamiento específico. Dos programas diferentes (digamos, IV 30-seg vs. IV 120-seg) aplicados al mismo organismo deberían producir el mismo valor de k cuando se ajusta la ecuación a los datos.

### El Parámetro R_e: Refuerzos de Fuentes Alternativas

El parámetro **R_e** es conceptualmente más sutil y representa una de las innovaciones teóricas más profundas de Herrnstein. R_e se interpreta como la tasa de refuerzo obtenida de **todas las demás fuentes** disponibles para el organismo—es decir, refuerzos que no provienen de la respuesta operante que el experimentador está midiendo.

Esta interpretación puede parecer extraña al principio. En una cámara operante aparentemente vacía—una paloma en una caja con un solo disco iluminado—¿de dónde vienen estos "otros refuerzos"? Herrnstein argumentó que aun en este ambiente simplificado, el organismo tiene acceso a múltiples actividades alternativas:

- **Exploración del ambiente:** Inspeccionar paredes, esquinas, el dispensador de comida
- **Acicalamiento:** Limpiarse las plumas, rascarse
- **Descanso:** Simplemente estar quieto, no hacer nada
- **Actividades estereotipadas:** Dar vueltas, movimientos repetitivos

Cada una de estas actividades puede tener algún valor reforzante intrínseco—reducen estados aversivos (aburrimiento, incomodidad), producen estimulación sensorial novedosa, o satisfacen motivaciones endógenas. Aunque no son refuerzos tan poderosos como la comida, contribuyen al "presupuesto" total de refuerzo del organismo.

Matemáticamente, R_e determina la **semisaturación** de la función: cuando r = R_e, la tasa de respuesta es:

R = k(R_e)/(R_e + R_e) = k/2

Es decir, R_e es la tasa de refuerzo necesaria para alcanzar el 50% de la tasa de respuesta máxima. Por lo tanto, R_e puede interpretarse como una medida de cuán "competitivas" son las fuentes alternativas de refuerzo: un R_e alto significa que hay muchas alternativas atractivas, requiriendo tasas altas de refuerzo de la respuesta operante para capturar una fracción sustancial del comportamiento.

### La Implicación Profunda: Todo Comportamiento Refleja Elección

La interpretación de R_e lleva a una conclusión conceptual fundamental: **no existe "comportamiento en aislamiento"**. Incluso cuando solo una respuesta operante está explícitamente disponible y es medida por el experimentador, el organismo está constantemente eligiendo entre esa respuesta y todas las demás actividades posibles.

Esta perspectiva unifica el estudio de respuestas individuales y situaciones de elección explícita. No son fenómenos cualitativamente diferentes; más bien, representan puntos en un continuo donde el número de alternativas explícitamente programadas y medidas varía. Esta unificación conceptual es uno de los logros teóricos más importantes de la ecuación de Herrnstein.

---

## DERIVACIÓN CONCEPTUAL DE LA ECUACIÓN DE HERRNSTEIN

Aunque Herrnstein propuso su ecuación inicialmente de forma empírica—ajustando funciones matemáticas a datos experimentales—también puede derivarse conceptualmente a partir de principios más fundamentales. Esta derivación no solo proporciona una justificación teórica de la forma funcional, sino que también aclara los supuestos subyacentes.

### Principio 1: Restricción Temporal

El tiempo total disponible para el organismo es fijo. Si **T₁** es el tiempo dedicado a la respuesta operante medida (picar el disco) y **T₀** es el tiempo dedicado a todas las demás actividades (exploración, acicalamiento, descanso), entonces:

**T₁ + T₀ = T_total = constante**

Para simplificar la derivación, normalizamos el tiempo total a T_total = 1 (equivalente a expresar tiempos como proporciones). Por lo tanto:

**T₁ + T₀ = 1**

Esta es simplemente la restricción de que el organismo debe estar haciendo algo en cada momento—no puede estar simultáneamente realizando múltiples actividades incompatibles.

### Principio 2: Distribución Proporcional al Refuerzo

El organismo distribuye su tiempo entre alternativas proporcionalmente a los refuerzos obtenidos de cada una. Este es el supuesto crucial que conecta la restricción temporal con las tasas de refuerzo:

**T₁/T₀ = r/R_e**

donde:
- **r** es la tasa de refuerzo obtenida de la respuesta operante medida
- **R_e** es la tasa de refuerzo obtenida de todas las demás actividades

Este supuesto implica que el organismo es sensible a la **rentabilidad relativa** de cada alternativa. Si la respuesta operante produce el doble de refuerzos que las actividades alternativas, el organismo dedica el doble de tiempo a la respuesta operante.

### Derivación Algebraica

Ahora podemos derivar la ecuación de Herrnstein combinando estos dos principios. Rearreglando el Principio 2:

**T₁ = T₀(r/R_e)**

Sustituyendo en la restricción temporal T₁ + T₀ = 1:

**T₀(r/R_e) + T₀ = 1**

Factorizando T₀:

**T₀(r/R_e + 1) = 1**

**T₀[(r + R_e)/R_e] = 1**

Resolviendo para T₀:

**T₀ = R_e/(r + R_e)**

Por lo tanto, sustituyendo en T₁ = 1 - T₀:

**T₁ = 1 - R_e/(r + R_e)**

**T₁ = [(r + R_e) - R_e]/(r + R_e)**

**T₁ = r/(r + R_e)**

Finalmente, si asumimos que la tasa de respuesta es proporcional al tiempo dedicado, con constante de proporcionalidad **k** (la tasa de respuesta cuando T₁ = 1, es decir, cuando toda la capacidad conductual se dedica a la respuesta operante):

**R = kT₁ = kr/(r + R_e)**

Esta es precisamente la ecuación de Herrnstein. La derivación muestra que emerge naturalmente de dos supuestos simples y plausibles: restricción temporal y distribución proporcional al refuerzo.

---

## PREDICCIONES CUANTITATIVAS Y AJUSTE A DATOS EMPÍRICOS

### Forma Hiperbólica: Rendimientos Decrecientes

La ecuación de Herrnstein R = kr/(r + R_e) tiene una forma hiperbólica característica que produce **rendimientos decrecientes**: incrementos sucesivos en la tasa de refuerzo r producen incrementos cada vez menores en la tasa de respuesta R.

Para ver esto matemáticamente, calculemos la derivada de R con respecto a r:

dR/dr = k(r + R_e) - kr / (r + R_e)²
      = kR_e / (r + R_e)²

Esta derivada es siempre positiva (R aumenta con r), pero disminuye conforme r aumenta (el denominador crece). Es decir, la "ganancia marginal" de incrementar r es mayor cuando r es pequeño y menor cuando r es grande.

### Casos Límite

La ecuación también tiene comportamientos límite intuitivos:

**1. Cuando r → 0 (sin refuerzo de la respuesta operante):**

R → k(0)/(0 + R_e) = 0

Sin refuerzo, la respuesta se extingue (tasa de respuesta cero).

**2. Cuando r → ∞ (refuerzo muy abundante):**

R → kr/(r) = k

La respuesta alcanza su máximo físico posible.

**3. Cuando r = R_e (refuerzo operante igual a refuerzo de fondo):**

R = k(R_e)/(R_e + R_e) = k/2

La respuesta ocurre a la mitad de su tasa máxima—tiempo igualmente distribuido entre la respuesta operante y las alternativas.

### Evidencia Empírica del Ajuste

La ecuación de Herrnstein ha demostrado ajustarse notablemente bien a datos de múltiples experimentos:

**Catania y Reynolds (1968):** Variando r en programas IV para palomas, los datos mostraron la función hiperbólica predicha con r² > 0.95 en la mayoría de los sujetos. Los valores estimados de k estaban en el rango de 200-250 respuestas/minuto, consistentes con las capacidades motoras de las palomas. Los valores de R_e típicamente estaban en el rango de 5-15 refuerzos/hora.

**Herrnstein (1970):** En un análisis exhaustivo de múltiples estudios con diferentes programas, especies, y procedimientos, la ecuación contabilizó más del 90% de la varianza en tasas de respuesta. Este nivel de precisión predictiva es excepcional en psicología cuantitativa.

**De Villiers y Herrnstein (1976):** Demostraron que la ecuación se mantiene incluso cuando se manipulan variables como la magnitud del reforzador (cantidad de comida), el esfuerzo requerido para responder, y la demora del refuerzo—siempre que estas variables se incorporen apropiadamente en la definición de "tasa de refuerzo efectiva".

Por ejemplo, si A es la magnitud del reforzador, la tasa de refuerzo efectiva puede definirse como:

**r_efectivo = A × r**

Y la ecuación se convierte en:

**R = k(Ar)/(Ar + R_e)**

Esta formulación predice correctamente que incrementar la magnitud del reforzador aumenta la tasa de respuesta de manera similar a incrementar la frecuencia de refuerzo.

### Limitaciones del Ajuste

Es importante notar que el ajuste de la ecuación no es perfecto en todos los casos. Hay desviaciones sistemáticas, especialmente:

- Para tasas muy bajas de refuerzo (r cercano a cero), donde puede haber efectos de extinción más complejos
- Para tasas muy altas de refuerzo, donde pueden aparecer fenómenos de saciación
- Durante transiciones entre condiciones (la ecuación predice estado estable, no dinámica de adquisición)

Además, la ecuación asume que R_e permanece constante a través de condiciones experimentales—un supuesto que puede violarse si las manipulaciones experimentales afectan inadvertidamente las fuentes alternativas de refuerzo.

No obstante, como descripción cuantitativa del control del refuerzo sobre la tasa de respuesta en estado estable, la ecuación de Herrnstein representa uno de los logros más exitosos de la psicología cuantitativa.

---

## DERIVACIÓN CRUCIAL: DE HERRNSTEIN A IGUALACIÓN

### Aplicación a Situaciones de Elección Concurrente

La ecuación de Herrnstein para una sola respuesta puede parecer describir "comportamiento en aislamiento", pero conceptualmente implica elección: el organismo está eligiendo entre la respuesta medida (R₁) y todas las demás actividades (R₀). Esta conceptualización prepara el terreno para analizar situaciones de **elección explícita**, donde dos o más respuestas medibles están disponibles simultáneamente.

Cuando generalizamos la ecuación de Herrnstein a situaciones con dos respuestas concurrentes, obtenemos un sistema de dos ecuaciones. Para una paloma que puede picar cualquiera de dos discos, cada uno reforzado en su propio programa IV:

**R₁ = kr₁/(r₁ + r₂ + R_e)**

**R₂ = kr₂/(r₁ + r₂ + R_e)**

Estas ecuaciones describen cómo cada respuesta es afectada por los refuerzos obtenidos de **ambas alternativas**, más los refuerzos de otras fuentes (R_e). La estructura matemática captura el hecho de que las dos respuestas operantes y las actividades de fondo compiten por la capacidad conductual limitada del organismo.

### La Derivación Algebraica

Un resultado extraordinario emerge al considerar la **razón** de estas tasas de respuesta. Dividamos la primera ecuación por la segunda:

**R₁/R₂ = [kr₁/(r₁ + r₂ + R_e)] / [kr₂/(r₁ + r₂ + R_e)]**

Observemos que el denominador (r₁ + r₂ + R_e) aparece en ambos términos. Cuando dividimos, estos términos se cancelan:

**R₁/R₂ = [kr₁] / [kr₂]**

El parámetro k también se cancela:

**R₁/R₂ = r₁/r₂**

Este es precisamente el resultado de **igualación**: la razón de respuestas iguala la razón de refuerzos.

### La Importancia de las Cancelaciones

La derivación algebraica es simple, pero su significado teórico es profundo. La igualación emerge **automáticamente** de la ecuación de Herrnstein cuando se aplica a situaciones de elección concurrente. No necesitamos postular igualación como un principio separado; es una **consecuencia matemática** de cómo el refuerzo controla respuestas individuales.

Crucialmente, observemos qué se cancela en la derivación:

- El parámetro **k** (capacidad máxima de respuesta)
- El denominador completo **(r₁ + r₂ + R_e)**

Estas cancelaciones implican que **los valores absolutos de k y R_e no afectan la razón R₁/R₂**—solo afectan las tasas absolutas de respuesta R₁ y R₂. Dos palomas con diferentes capacidades motoras (diferentes valores de k) o diferentes niveles de refuerzo de fondo (diferentes valores de R_e) deberían ambas mostrar igualación: R₁/R₂ = r₁/r₂.

Esta independencia de igualación respecto a parámetros individuales es consistente con la robustez empírica del fenómeno: igualación se observa a través de variaciones en especies (que tienen diferentes k), procedimientos experimentales (que pueden variar R_e), y otros factores.

---

## EJEMPLO NUMÉRICO CONCRETO

Para ilustrar concretamente cómo funciona esta derivación, consideremos un experimento específico con valores numéricos realistas.

### Especificación del Experimento

Una paloma enfrenta dos discos iluminados con los siguientes programas concurrentes:

- **Alternativa 1:** IV 60-seg → tasa programada r₁ = 60 refuerzos/hora = 1.0 refuerzo/minuto
- **Alternativa 2:** IV 120-seg → tasa programada r₂ = 30 refuerzos/hora = 0.5 refuerzos/minuto

Basándonos en experimentos previos con esta paloma, sabemos que sus parámetros son:
- **k** = 120 respuestas/minuto (capacidad máxima de respuesta)
- **R_e** = 10 refuerzos/hora = 0.167 refuerzos/minuto (refuerzo de fondo)

### Aplicación de la Ecuación de Herrnstein

Aplicamos la ecuación a cada alternativa:

**Para Alternativa 1:**

R₁ = (120)(1.0) / (1.0 + 0.5 + 0.167)
   = 120 / 1.667
   = 72 respuestas/minuto

**Para Alternativa 2:**

R₂ = (120)(0.5) / (1.0 + 0.5 + 0.167)
   = 60 / 1.667
   = 36 respuestas/minuto

### Verificación de Igualación

Ahora verificamos si estas tasas de respuesta satisfacen igualación:

**Razón de respuestas:**
R₁/R₂ = 72/36 = 2.0

**Razón de refuerzos:**
r₁/r₂ = 1.0/0.5 = 2.0

**¡Igualación perfecta!** R₁/R₂ = r₁/r₂ = 2.0

### Observación Clave: El Papel de R_e y k

Observemos que:
- El valor específico de **R_e** (0.167) afectó los valores absolutos de R₁ y R₂
- El valor específico de **k** (120) afectó los valores absolutos de R₁ y R₂
- Pero **ninguno de estos parámetros afectó la razón** R₁/R₂

Para verificar esto, repitamos el cálculo con diferentes valores de parámetros:

**Caso alternativo:**
- k = 150 (paloma más rápida)
- R_e = 0.25 (más refuerzo de fondo)

R₁ = (150)(1.0) / (1.0 + 0.5 + 0.25) = 150/1.75 = 85.7 resp/min
R₂ = (150)(0.5) / (1.0 + 0.5 + 0.25) = 75/1.75 = 42.9 resp/min

R₁/R₂ = 85.7/42.9 = 2.0 (¡exactamente igual!)

Esta cancelación matemática es **la clave de por qué emerge igualación**: los parámetros específicos del organismo y del contexto afectan cuánto responde en términos absolutos, pero no cómo distribuye sus respuestas entre alternativas. La distribución relativa depende únicamente de las tasas relativas de refuerzo.

---

## LIMITACIONES DE LA ECUACIÓN DE HERRNSTEIN

A pesar de su éxito empírico y elegancia teórica, la ecuación de Herrnstein tiene limitaciones importantes que deben reconocerse:

### 1. Asume Estado Estable

La ecuación predice tasas de respuesta en **equilibrio**—después de que el comportamiento se ha estabilizado con exposición prolongada a las contingencias. No modela la **dinámica de adquisición**: cómo cambian las respuestas sesión por sesión conforme el organismo aprende las nuevas contingencias.

Para analizar la dinámica temporal, se necesitan modelos más complejos que incorporen mecanismos de aprendizaje—por ejemplo, modelos de aprendizaje por refuerzo que especifican cómo se actualizan valores Q con la experiencia (tema de capítulos posteriores).

### 2. No Predice Dinámica Temporal Dentro de Sesiones

Incluso en estado estable, la ecuación predice promedios sobre sesiones completas. No captura **patrones temporales** dentro de sesiones: cómo fluctúan las respuestas momento a momento, cómo se distribuyen en el tiempo relativo al último refuerzo, etc.

Por ejemplo, en programas de intervalo fijo (IF), los organismos muestran un patrón característico de "festón": pausa post-refuerzo seguida de aceleración. La ecuación de Herrnstein no predice este patrón temporal—solo predice la tasa promedio.

### 3. Aplicación Problemática a Programas RV

La ecuación fue derivada y probada principalmente con programas IV. Su aplicación a programas de razón variable (RV) es más problemática. En RV, la tasa de refuerzo es directamente proporcional a la tasa de respuesta (r = R/n), creando un sistema de retroalimentación positiva que puede no estabilizarse de la manera que la ecuación asume.

De hecho, en programas RV concurrentes, los organismos frecuentemente muestran preferencia casi exclusiva por la alternativa más rica—un patrón muy diferente de igualación observado en IV-IV concurrentes.

### 4. No Explica Undermatching Directamente

Empíricamente, igualación perfecta (R₁/R₂ = r₁/r₂) es relativamente rara. Más común es **undermatching**: la distribución de respuestas es menos extrema que la distribución de refuerzos. Por ejemplo, si r₁/r₂ = 4, frecuentemente se observa R₁/R₂ ≈ 2.5.

La ecuación de Herrnstein en su forma básica predice igualación perfecta. Explicar undermatching requiere supuestos adicionales—por ejemplo, que R_e no es constante sino que varía con las manipulaciones experimentales, o que hay discriminabilidad imperfecta entre alternativas.

### 5. Sensibilidad al Supuesto de R_e Constante

La derivación de igualación de Herrnstein tiene un supuesto crítico: **R_e es constante** a través de diferentes condiciones experimentales. Es decir, asumimos que los "refuerzos de fuentes alternativas" no cambian cuando manipulamos r₁ y r₂.

¿Es plausible este supuesto? En una cámara operante bien controlada, donde las únicas fuentes de refuerzo explícitas son los dos programas concurrentes, parece razonable. Sin embargo, si hay fuentes adicionales de refuerzo que varían entre condiciones, entonces R_e no sería constante y la derivación fallaría.

Esta sensibilidad de la predicción de igualación al supuesto de R_e constante es una debilidad potencial. Modelos alternativos (que examinaremos en el Subcapítulo 10.5) han propuesto mecanismos que producen igualación sin requerir este supuesto.

---

## TRANSICIÓN AL SUBCAPÍTULO 10.4

La ecuación de Herrnstein proporciona una explicación elegante de la igualación: cuando se aplica a dos respuestas concurrentes, la cancelación algebraica de los términos k y (r₁ + r₂ + R_e) produce automáticamente la Ley de Igualación (R₁/R₂ = r₁/r₂). Este logro teórico—derivar un fenómeno empírico robusto desde principios generales—representa un hito en la formalización cuantitativa del comportamiento.

Sin embargo, como mencionamos, la igualación perfecta (donde la razón de respuestas iguala exactamente la razón de refuerzos) es más la excepción que la regla en datos experimentales. En la mayoría de los experimentos, se observa **undermatching**: los organismos distribuyen su comportamiento de forma menos extrema que lo predicho por igualación estricta. Además, frecuentemente aparecen **preferencias inherentes** (bias) independientes de las razones de refuerzo programadas.

Recordemos la forma generalizada de igualación que documentamos en el Subcapítulo 10.2:

**B₁/B₂ = b(r₁/r₂)^a**

donde:
- **a** (sensibilidad) típicamente es menor que 1.0 (undermatching)
- **b** (bias) frecuentemente difiere de 1.0 (preferencia inherente)

¿Qué factores causan estas desviaciones sistemáticas de la igualación perfecta? ¿Cómo pueden los experimentadores manipularlas? ¿Qué nos dicen estas desviaciones sobre los mecanismos que controlan la elección?

El siguiente subcapítulo examina precisamente estas preguntas, analizando los determinantes del undermatching y el bias, y cómo procedimientos experimentales específicos—especialmente el changeover delay (COD)—modulan la sensibilidad de la elección a las razones de refuerzo.

---

## CONCEPTOS CLAVE

- **Ley del Efecto Relativa:** El efecto del refuerzo sobre el comportamiento es relativo, no absoluto—depende del refuerzo de todas las fuentes disponibles
- **Ecuación de Herrnstein:** R = kr/(r + R_e) describe cómo la tasa de refuerzo controla la tasa de respuesta en estado estable
- **Parámetro k:** Tasa máxima de respuesta posible, determinada por restricciones físicas y fisiológicas del organismo
- **Parámetro R_e:** Tasa de refuerzo de fuentes alternativas (actividades de fondo), representa competencia por capacidad conductual
- **Forma hiperbólica:** La ecuación produce rendimientos decrecientes—incrementos sucesivos en r tienen efectos progresivamente menores en R
- **Derivación conceptual:** La ecuación emerge de dos principios: restricción temporal (T₁ + T₀ = 1) y distribución proporcional al refuerzo (T₁/T₀ = r/R_e)
- **Generalización a elección concurrente:** Para dos respuestas: R₁ = kr₁/(r₁ + r₂ + R_e) y R₂ = kr₂/(r₁ + r₂ + R_e)
- **Derivación de igualación:** Al dividir las ecuaciones, k y el denominador se cancelan, produciendo R₁/R₂ = r₁/r₂
- **Independencia de parámetros:** La razón R₁/R₂ no depende de k ni R_e—solo depende de r₁/r₂
- **Limitaciones:** Asume estado estable, no predice dinámica temporal, sensible al supuesto de R_e constante, no explica undermatching directamente

---

## OBJETIVOS DE APRENDIZAJE

Al completar este subcapítulo, el estudiante debe ser capaz de:

1. Explicar la transición histórica de formulaciones cualitativas (Thorndike) a formulaciones cuantitativas (Herrnstein) de la Ley del Efecto
2. Describir los hallazgos empíricos de Catania y Reynolds (1968) que motivaron la forma hiperbólica de la ecuación de Herrnstein
3. Interpretar el significado de los parámetros k y R_e en términos de procesos conductuales y fisiológicos
4. Derivar la ecuación de Herrnstein a partir de los principios de restricción temporal y distribución proporcional al refuerzo
5. Aplicar la ecuación de Herrnstein a situaciones específicas calculando tasas de respuesta predichas dados valores de r, k, y R_e
6. Demostrar algebraicamente cómo igualación (R₁/R₂ = r₁/r₂) emerge de la aplicación de la ecuación de Herrnstein a elección concurrente
7. Explicar por qué la razón R₁/R₂ es independiente de k y R_e pero depende de r₁/r₂
8. Trabajar con ejemplos numéricos concretos para verificar predicciones de igualación
9. Identificar las limitaciones principales de la ecuación de Herrnstein (estado estable, dinámica temporal, R_e constante, undermatching)
10. Articular la conexión conceptual entre comportamiento individual y elección: todo comportamiento refleja elección entre alternativas explícitas e implícitas

---

**FIN DEL SUBCAPÍTULO 10.3**
