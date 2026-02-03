# CAPÍTULO X+1
# MODELOS DE OPTIMIZACIÓN MOLAR

---

## INTRODUCCIÓN

En el capítulo anterior exploramos el fenómeno de la igualación: cuando un organismo se enfrenta a dos opciones de respuesta concurrentes, cada una reforzada en su propio programa, la distribución de respuestas (o tiempos) iguala la distribución de reforzadores. Describimos este patrón empírico con la ecuación de Herrnstein y la ecuación generalizada de igualación de Baum, y examinamos sus propiedades formales en diferentes situaciones—programas de intervalo variable (IV), razón variable (RV), y combinaciones de ambos. Documentamos también desviaciones sistemáticas del patrón ideal: undermatching, bias, y efectos de magnitud de refuerzo.

Pero describir un fenómeno no es explicarlo. ¿Por qué los organismos igualan? ¿Qué principios subyacentes producen este patrón? ¿Es la igualación una estrategia óptima adaptada por selección natural, o simplemente un subproducto de algún mecanismo más fundamental?

### De la Descripción a la Explicación

El reto al que ahora nos enfrentamos es característico de toda ciencia madura: pasar de leyes fenomenológicas—que describen regularidades empíricas—a teorías explicativas que revelan los principios subyacentes. La transición de la ley de Boyle (PV = constante) a la teoría cinética de los gases, o de las leyes de Kepler sobre movimiento planetario a la teoría gravitacional de Newton, ejemplifica esta progresión fundamental en ciencia.

En el caso de la conducta de elección, ya tenemos nuestras leyes fenomenológicas: la ecuación de Herrnstein y la ley de igualación. Ahora necesitamos teorías que expliquen por qué estas leyes se cumplen. Como vimos en el Capítulo 1 sobre explicación en ciencias del comportamiento, podemos distinguir entre análisis en diferentes niveles: computacional (¿qué problema se resuelve y por qué?), algorítmico (¿qué procedimientos generan la solución?), e implementacional (¿cómo se realiza físicamente?).

Este capítulo aborda el nivel computacional: ¿qué distribución de conducta sería óptima si el organismo pudiera computar perfectamente y tuviera conocimiento completo del entorno? Asumimos que los organismos, moldeados por millones de generaciones de selección natural, aproximan soluciones óptimas. Desarrollaremos dos modelos influyentes de optimización—el modelo de distancia mínima de Staddon y el modelo de maximización de utilidad de Rachlin—que derivan la igualación como consecuencia matemática de principios de optimización.

### Tres Capítulos, Tres Niveles de Análisis

Los próximos tres capítulos exploran la igualación en niveles complementarios:

**Este capítulo (X+1) aborda el nivel computacional.** Preguntamos: ¿qué distribución de conducta sería óptima? Desarrollaremos modelos de optimización molar que caracterizan el equilibrio al que debería converger un organismo perfectamente adaptado. Estos modelos no especifican cómo el organismo computa la solución; solo especifican cuál debería ser la solución. Proporcionan el estándar normativo contra el cual evaluar el desempeño real.

**El Capítulo X+2 se moverá al nivel algorítmico.** Preguntaremos: ¿qué reglas simples, operando localmente momento a momento sin conocimiento global, pueden generar patrones que se asemejen a la igualación? Exploraremos melioration (Herrnstein & Vaughan), maximización momentánea (Shimp), y aprendizaje de valores Q basado en error de predicción. Estos modelos especifican procedimientos implementables que podrían ejecutarse en tiempo real. Conectarán directamente con el modelo de Rescorla-Wagner de los Capítulos 8-11.

**El Capítulo X+3 abordará la traducción de valores internos a acciones observables—el problema de la regla de respuesta.** Aun si el organismo ha aprendido valores correctos, ¿cómo decide qué hacer en cada momento? Exploraremos el dilema exploración-explotación, las bases psicofísicas de las funciones de elección (teoría de Thurstone), y la regla softmax, mostrando cómo diferentes parámetros producen igualación, undermatching, o sobreigualación.

### Organización de Este Capítulo

Comenzaremos estableciendo los fundamentos de teoría de optimización conductual—los cinco principios de Staddon que justifican este enfoque y sus conexiones con ecología del comportamiento. Luego desarrollaremos dos modelos de optimización molar:

**Modelo de Distancia Mínima de Staddon (1979, 1983):** El organismo tiene un "punto de felicidad" (bliss point)—una distribución ideal de actividades. Los programas de reforzamiento imponen restricciones que impiden alcanzar el bliss point. El organismo minimiza una función de costo cuadrática que mide desviaciones de su punto de felicidad. Mediante análisis gráfico, derivaremos cómo esto predice preferencia exclusiva en programas RV concurrentes e igualación en programas IV concurrentes.

**Modelo de Maximización de Utilidad de Rachlin (Rachlin, Battalio, Kagel, & Green, 1981):** Aplica teoría microeconómica estándar. El organismo maximiza una función de utilidad con rendimientos decrecientes, sujeto a restricciones de tiempo y retroalimentación. Mediante curvas de indiferencia y análisis de tangencia, derivaremos predicciones similares.

Aunque ambos modelos parten de supuestos ligeramente diferentes, convergen en predicciones centrales. Al final compararemos ambos modelos, evaluaremos su adecuación empírica, y discutiremos transiciones hacia algoritmos de aprendizaje.

---

## PARTE 1: FUNDAMENTOS DE TEORÍA DE OPTIMIZACIÓN CONDUCTUAL

### La Premisa Evolutiva: Selección Natural como Proceso de Optimización

La aplicación de teoría de optimización al comportamiento animal tiene profundas raíces en biología evolutiva y ecología del comportamiento. La lógica es elegante: si el comportamiento ha sido moldeado por selección natural durante millones de generaciones, entonces debemos esperar que los organismos se comporten de manera que maximicen fitness—supervivencia y éxito reproductivo diferencial.

Esta expectativa no asume que los organismos calculen conscientemente estrategias óptimas. Más bien, asume que variantes conductuales que incrementaron fitness en ancestros fueron seleccionadas preferencialmente, acumulándose gradualmente. Después de suficientes generaciones, el comportamiento observado aproxima lo que un diseñador omnisciente habría programado como óptimo. La selección natural funciona como un "algoritmo de optimización lento": prueba variantes, retiene las mejores, descarta las peores, repite durante eones.

Dado que la obtención de recursos (alimento, agua, refugio, pareja) contribuye directamente al fitness, podríamos predecir que los organismos distribuirán su comportamiento de forma que maximice la tasa de obtención de recursos sujeto a restricciones físicas, temporales, fisiológicas y cognitivas.

Esta perspectiva, desarrollada extensamente en ecología conductual y teoría de forrajeo óptimo (Stephens & Krebs, 1986; Pyke et al., 1977), fue introducida al análisis experimental del comportamiento principalmente por John Staddon (1979, 1983) y Howard Rachlin y colaboradores (Rachlin et al., 1981). Staddon argumentó que el análisis de optimización proporciona un marco unificador para entender el control del comportamiento por sus consecuencias.

### Los Cinco Principios de Staddon para Análisis de Optimización

Staddon (1979) articuló cinco principios fundamentales que guían el análisis de optimización conductual:

#### Principio 1: Competencia Temporal

**El tiempo es un recurso limitado y escaso que debe distribuirse entre actividades mutuamente excluyentes.** Un organismo no puede simultáneamente forrajear en dos ubicaciones distintas ni estar dormido y despierto al mismo tiempo. Esta restricción fundamental significa que incrementar tiempo dedicado a una actividad necesariamente reduce tiempo disponible para otras.

Formalmente, si hay n actividades posibles y T_i es el tiempo dedicado a la actividad i:

**T₁ + T₂ + T₃ + ... + Tₙ = T_total**

Esta ecuación de "presupuesto temporal" es análoga a la restricción presupuestaria en economía. Cada minuto gastado en actividad A tiene un "costo de oportunidad"—es un minuto no disponible para actividades alternativas.

#### Principio 2: La Distribución como Unidad de Análisis

**El comportamiento debe analizarse en términos de distribuciones temporales o numéricas a lo largo de períodos extendidos, no respuestas individuales aisladas.** La pregunta relevante no es "¿debería emitir esta respuesta específica ahora?" sino "¿qué proporción de mi tiempo total debo dedicar a esta actividad versus otras?"

Esta perspectiva molar es esencial porque: (1) las consecuencias se acumulan temporalmente—una sola comida no determina fitness, pero la tasa promedio sobre semanas sí; (2) los programas de reforzamiento especifican contingencias sobre distribuciones (tasas, proporciones) no respuestas individuales; (3) el análisis de distribuciones permite aplicar herramientas matemáticas poderosas de optimización.

Matemáticamente, pasamos de R_i(t) = "respuesta i en momento t" (binaria, estocástica) a R_i = tasa promedio (continua, analizable). La distribución conductual es el vector (R₁, R₂, ..., Rₙ) o (T₁, T₂, ..., Tₙ) especificando cómo se reparte el comportamiento entre alternativas.

#### Principio 3: Restricciones Múltiples

**Los organismos operan bajo múltiples restricciones simultáneas que limitan el espacio de distribuciones conductuales posibles:**

- **Restricciones físicas/biológicas:** Incompatibilidades conductuales básicas (no puedes volar y nadar simultáneamente)
- **Restricciones temporales:** La suma de tiempos debe igualar el total disponible
- **Restricciones fisiológicas:** Saciedad, fatiga, límites de memoria y atención
- **Restricciones ambientales/programadas:** Las más interesantes son las impuestas por programas de reforzamiento, que especifican funciones de retroalimentación relacionando comportamiento con consecuencias

Estas restricciones definen el conjunto de distribuciones alcanzables—la "frontera de posibilidades" en términos económicos. Cualquier análisis de optimización debe especificar explícitamente todas las restricciones relevantes.

#### Principio 4: Ordenamiento por Valor

**El organismo puede ordenar diferentes estados o distribuciones por su valor biológico.** Este supuesto—que existe alguna métrica común de valor—es necesario para que tenga sentido hablar de "maximización". Sin un ordenamiento de preferencias, no hay base para seleccionar entre alternativas.

Formalmente, asumimos una función de valor V(·) o utilidad U(·) tal que V(D₁) > V(D₂) significa "D₁ es preferido a D₂", y esta relación es transitiva. ¿Qué determina este valor? En última instancia, fitness. En laboratorio, asumimos que refuerzos experimentales actúan como "proxies" de fitness: organismos evolucionaron para valorar estos recursos porque ancestralmente contribuyeron al fitness.

Este principio no asume que los organismos representen explícitamente V(·) ni que calculen conscientemente. Solo requiere que el comportamiento sea consistente con la existencia de tal función—que actúen "como si" estuvieran maximizando V(·).

#### Principio 5: Equilibrio Maximiza Valor

Finalmente, **el comportamiento en equilibrio corresponde a la distribución que maximiza valor sujeto a las restricciones.** Después de suficiente experiencia, el sistema converge hacia la distribución D* tal que V(D*) ≥ V(D) para toda distribución factible D.

Tres calificaciones importantes:

1. **"En equilibrio":** La predicción aplica a estados estacionarios, no transitorios. Durante aprendizaje inicial, el organismo puede exhibir distribuciones subóptimas mientras explora.

2. **"Maximiza valor":** Esto debe entenderse como alcanzar un máximo local, posiblemente global. No necesariamente predecimos el máximo global absoluto.

3. **"Sujeto a restricciones":** No predecimos maximización absoluta, sino condicional sobre distribuciones factibles. La optimalidad es siempre relativa a las restricciones.

### Conexión con Ecología del Comportamiento: El Teorema del Valor Marginal

Estos principios no son únicos al laboratorio operante. Son instancias de un marco más general en ecología conductual, particularmente en teoría de forrajeo óptimo.

**Ejemplo paradigmático:** Considere un predador forrajeando en un ambiente con parches de recursos distribuidos espacialmente. Cada parche inicialmente contiene muchas presas, pero conforme el predador captura presas, la tasa de obtención declina (depleción). ¿Cuándo debe abandonar el parche actual y viajar hacia uno nuevo?

El **Teorema del Valor Marginal** (Charnov, 1976) predice que el predador debe abandonar un parche cuando la tasa instantánea de captura cae por debajo de la tasa promedio en todo el ambiente (incluyendo tiempo de viaje). Matemáticamente, si g(T) es presas capturadas después de tiempo T en un parche, τ es tiempo de viaje, y T* es tiempo óptimo de permanencia:

**g'(T*) = g(T*)/(T* + τ)**

La tasa marginal (derivada) al abandonar debe igualar la tasa promedio global. Este resultado surge de maximizar tasa global de obtención de energía—análogo a nuestro problema de maximizar tasa de refuerzo en programas concurrentes.

Los programas IV concurrentes pueden conceptualizarse como "parches": cada alternativa es un parche cuya "riqueza" está fija pero cuya disponibilidad depende del tiempo desde la última visita. Cambiar entre alternativas es análogo a cambiar entre parches. El análisis de optimización predice cuánto tiempo dedicar a cada alternativa—estructuralmente similar al forrajeo en parches.

### Análisis Normativo versus Descriptivo

Es crucial entender que los modelos de optimización son **normativos**, no **descriptivos**. No afirman que los organismos de hecho se comporten óptimamente siempre; afirman lo que *deberían* hacer si estuvieran perfectamente adaptados. La pregunta empírica es cuán bien las predicciones normativas coinciden con el comportamiento observado.

Tres tipos de resultados son informativos:

**1. Coincidencia cercana:** Si el comportamiento observado coincide con predicciones de optimalidad, esto sugiere que selección natural ha moldeado eficientemente el comportamiento. También valida nuestros supuestos sobre qué está siendo optimizado y qué restricciones son relevantes.

**2. Desviaciones sistemáticas:** Si el comportamiento se desvía sistemáticamente del óptimo de manera predecible, esto revela restricciones o limitaciones omitidas. Por ejemplo, si los organismos consistentemente undermatching (s < 1), esto sugiere restricciones adicionales no capturadas: quizá exploración continua es adaptativa en ambientes inciertos, o limitaciones cognitivas impiden representación perfecta de tasas.

**3. Desviaciones idiosincráticas:** Si diferentes organismos muestran desviaciones en direcciones aleatorias sin patrón, esto podría reflejar ruido irreducible o variabilidad individual sin implicaciones teóricas profundas.

El valor del análisis normativo no depende de predicciones perfectas. Incluso con desviaciones sistemáticas, el modelo proporciona el estándar contra el cual medirlas, señalando qué factores adicionales deben incorporarse.

---

## PARTE 2: MODELO DE DISTANCIA MÍNIMA DE STADDON

### Conceptos Básicos: Punto de Felicidad y Función de Costo

El modelo de Staddon (1979, 1983) adopta un enfoque geométrico intuitivo basado en la noción de **punto de felicidad** (bliss point). La idea es elegante: cada organismo tiene una distribución preferida de actividades que exhibiría en ausencia de restricciones externas. Esta distribución representa el balance "ideal" entre diferentes comportamientos basado en utilidad intrínseca.

Por ejemplo, una rata sin restricciones podría elegir dedicar 40% de su tiempo a explorar, 30% a acicalarse, 20% a comer (cuando la comida es gratis), y 10% a actividades sociales. Este es su bliss point—la distribución que maximiza "satisfacción" interna.

Sin embargo, las contingencias ambientales imponen restricciones que típicamente impiden alcanzar el bliss point. Un programa RV que requiere 50 respuestas de palanca por cada comida fuerza al organismo a dedicar más tiempo a presionar de lo que sería su preferencia no restringida. La rata debe "trabajar" más de lo que preferiría intrínsecamente.

El modelo postula que desviaciones del bliss point generan **costo psicológico**. Alejarse del bliss point reduce "satisfacción" experimentada. El organismo debe entonces seleccionar, entre todas las distribuciones factibles, aquella más cercana a su bliss point—que minimice el costo total.

### Formalización: Tres Actividades y Función de Costo Cuadrática

Consideremos la situación más simple: un organismo con acceso a dos opciones de respuesta (R₁ y R₂), cada una reforzada en su propio programa. Sea T₁ la proporción de tiempo dedicada a responder en opción 1, T₂ a opción 2, y L a todas las demás actividades ("leisure" u ocio).

**Restricción temporal:**
**T₁ + T₂ + L = 1**

(Todos los tiempos como proporciones del total.)

En ausencia de restricciones adicionales, el organismo exhibiría su distribución preferida: **(T₁⁰, T₂⁰, L⁰)**

Este es el bliss point. Los superíndices ⁰ indican valores preferidos "basales". Por ejemplo: T₁⁰ = 0.10, T₂⁰ = 0.15, L⁰ = 0.75, indicando que sin restricciones el organismo preferiría dedicar solo 25% de su tiempo a respuestas operantes y 75% a otras actividades.

Staddon postula que el costo de desviarse del bliss point puede representarse mediante **función cuadrática**:

**C(T₁, T₂, L) = a(T₁⁰ - T₁)² + b(T₂⁰ - T₂)² + c(L⁰ - L)²**

donde a, b, c son parámetros de peso positivos determinando importancia relativa de cada actividad.

**Propiedades deseables:**

1. **Mínimo en el bliss point:** C = 0 cuando (T₁, T₂, L) = (T₁⁰, T₂⁰, L⁰). Cualquier desviación incrementa costo.

2. **Simetría:** Desviaciones en cualquier dirección (más o menos tiempo) son igualmente costosas.

3. **Convexidad:** d²C/dT² > 0. Costos marginalmente crecientes: una desviación grande es desproporcionadamente más costosa que una pequeña. Garantiza un único mínimo global.

4. **Separabilidad:** Contribuciones de cada actividad son aditivas. El costo de desviarse en T₁ es independiente del nivel de T₂ (simplificación que hace el modelo tratable).

Los parámetros a, b, c reflejan "utilidad marginal" de cada actividad. Una actividad altamente valiosa tendrá parámetro grande: desviarse es muy costoso. Una menos valiosa tendrá parámetro pequeño: el organismo tolera mayores desviaciones.
### Restricciones de Retroalimentación: Programas RV vs IV

Hasta ahora hemos especificado la función que el organismo desea minimizar (función de costo) y una restricción (temporal). Pero falta la restricción crucial: ¿cómo los programas de reforzamiento limitan las distribuciones alcanzables?

Los programas pueden conceptualizarse como **funciones de retroalimentación** especificando la relación entre tiempo dedicado a una respuesta (T₁ o T₂) y tasa de refuerzo obtenida (r₁ o r₂). Como vimos en el Capítulo X, estas funciones difieren cualitativamente:

#### Programas de Razón Variable (RV)

Para un programa RV n, la función es lineal:
**r = R/n**

En términos de proporciones de tiempo, asumiendo tasa de respuesta constante k cuando el organismo responde activamente:
**r₁ = kT₁/n₁**

El número de refuerzos obtenidos es proporcional al tiempo dedicado. La pendiente k/n representa "densidad" de refuerzo: cuántos refuerzos por unidad de tiempo.

Esta linealidad tiene implicación crucial: **no hay rendimientos decrecientes**. Cada unidad adicional de tiempo produce el mismo incremento marginal en refuerzos, sin importar cuánto tiempo ya se haya dedicado. Duplicar T₁ duplica r₁.

#### Programas de Intervalo Variable (IV)

Para programas IV, la situación es cualitativamente diferente. Los refuerzos se hacen disponibles a intervalos impredecibles independientemente del comportamiento. Una vez disponible, un refuerzo permanece disponible hasta ser recolectado. Esto crea función con **rendimientos decrecientes**: incrementos iniciales en tasa de respuesta producen grandes incrementos en refuerzo obtenido, pero incrementos subsecuentes producen beneficios progresivamente menores, asintotizando hacia un máximo.

Una aproximación útil, asumiendo respuestas distribuidas uniformemente mientras el organismo "visita" la alternativa:

**r₁ ≈ (T₁ · k)/(T₁ · k + I₁)**

donde I₁ es el intervalo promedio programado. Cuando T₁ es pequeño, T₁·k << I₁ y r₁ ≈ T₁·k/I₁ (aproximadamente lineal). Cuando T₁ es grande, T₁·k >> I₁ y r₁ ≈ 1/I₁ (asíntota al máximo).

Esta no-linealidad captura la intuición: "visitar más frecuentemente una alternativa IV incrementa refuerzos, pero con retornos decrecientes". Responder dos veces más no duplica refuerzos; solo los incrementa por factor menor que 2.

### Solución Gráfica para Programas RV Concurrentes

Ahora podemos resolver el problema visualmente. Consideremos dos programas RV concurrentes: opción 1 con RV n₁, opción 2 con RV n₂.

**Representación en espacio (T₁, T₂):**

[Figura X+1.1: Diagrama con ejes T₁ (horizontal) y T₂ (vertical). La restricción temporal T₁ + T₂ + L = 1 se puede reescribir como T₁ + T₂ ≤ 1 si ignoramos momentáneamente L. Esta restricción es la línea recta diagonal desde (0,1) hasta (1,0). El bliss point B₀ = (T₁⁰, T₂⁰) está en el interior, digamos en (0.15, 0.10). Las curvas de iso-costo son elipses concéntricas centradas en B₀.]

Las **curvas de iso-costo** son conjuntos de puntos (T₁, T₂) que producen el mismo costo C. Dado que C es cuadrática, estas curvas son elipses. Elipses más cercanas al bliss point tienen menor costo (son más preferidas). Elipses más alejadas tienen mayor costo.

Para programas RV, las **restricciones de retroalimentación** son:
- r₁ = kT₁/n₁
- r₂ = kT₂/n₂

Si el organismo desea obtener tasas específicas (r̄₁, r̄₂), esto impone:
- T₁ = n₁r̄₁/k
- T₂ = n₂r̄₂/k

La **línea de restricción de retroalimentación** para obtener refuerzo total fijo (r̄₁ + r̄₂ = constante) es una línea recta con pendiente -n₁/n₂. Diferentes líneas paralelas representan diferentes totales de refuerzo.

**Pregunta clave:** ¿Qué distribución (T₁, T₂) minimiza costo C entre todas las que producen cierta tasa total de refuerzo?

**Respuesta geométrica:** El punto donde la línea de restricción es tangente a una elipse de iso-costo. Pero debido a que las restricciones RV son **líneas rectas** y las elipses son **convexas**, la tangencia típicamente ocurre en una **esquina**: o T₁ máximo (T₂ mínimo) o T₂ máximo (T₁ mínimo).

Más precisamente, supongamos que n₁ < n₂ (opción 1 es más rica—requiere menos respuestas por refuerzo). Entonces k/n₁ > k/n₂. Para cualquier presupuesto de tiempo dado, dedicarlo todo a opción 1 produce más refuerzos que dividirlo entre ambas opciones.

Si el organismo valora obtener refuerzos (lo cual presumiblemente sí), y dado que cada unidad de tiempo en opción 1 produce más refuerzos que en opción 2 (rendimientos constantes), la distribución óptima es **especializarse completamente en opción 1**.

**Predicción del modelo de Staddon para programas RV concurrentes:**
**Preferencia exclusiva por la alternativa más rica.**

Formalmente: Si n₁ < n₂, entonces T₁ → máximo permitido, T₂ → 0 (dentro de límites de mantener algo de tiempo para "ocio" L y considerando que bliss points podrían sesgar ligeramente). El organismo dedica todo el tiempo operante disponible a la opción más rica.

Esta predicción contrasta con igualación. Si igualación rigiera programas RV, esperaríamos T₁/T₂ = r₁/r₂, no preferencia exclusiva. Como veremos, la evidencia empírica favorece preferencia exclusiva para RV, no igualación—una validación del modelo de optimización.

### Solución Gráfica para Programas IV Concurrentes

Ahora consideremos dos programas IV concurrentes: opción 1 con IV t₁, opción 2 con IV t₂.

**Diferencia crucial:** Las funciones de retroalimentación ahora exhiben rendimientos decrecientes:
- r₁ ≈ (T₁·k)/(T₁·k + t₁)
- r₂ ≈ (T₂·k)/(T₂·k + t₂)

**Representación gráfica:**

[Figura X+1.2: Espacio (T₁, T₂) similar. Pero ahora las curvas de iso-refuerzo (combinaciones que producen refuerzo total constante r₁ + r₂ = R̄) son **curvas cóncavas** (arqueadas hacia afuera desde el origen), no líneas rectas. Esto se debe a rendimientos decrecientes.]

Incrementar T₁ cuando T₁ es ya grande produce beneficio marginal pequeño en r₁. Para mantener refuerzo total constante al incrementar T₁, no necesitas reducir T₂ tanto. Las curvas de iso-refuerzo se "achatan" conforme te alejas del origen.

Para maximizar refuerzos totales, queremos alcanzar la curva de iso-refuerzo más alta (más alejada del origen) que aún sea compatible con la restricción temporal. Crucialmente, debido a la **concavidad de las curvas**, el máximo ya no ocurre en una esquina. En cambio, típicamente ocurre en **punto interior**—distribución con T₁ > 0 y T₂ > 0.

La condición matemática para el máximo es que la **tasa marginal de obtención de refuerzo** debe ser igual entre las dos alternativas:

**∂r₁/∂T₁ = ∂r₂/∂T₂**

Calculando estas derivadas (usando regla de la cadena):
**∂r₁/∂T₁ = k·t₁/(T₁·k + t₁)²**
**∂r₂/∂T₂ = k·t₂/(T₂·k + t₂)²**

Igualando:
**k·t₁/(T₁·k + t₁)² = k·t₂/(T₂·k + t₂)²**

Simplificando (cancelando k):
**t₁/(T₁·k + t₁)² = t₂/(T₂·k + t₂)²**

Para el **caso simétrico** donde t₁ = t₂ (ambos programas idénticos):
**(T₁·k + t₁)² = (T₂·k + t₂)²**

Dado que t₁ = t₂:
**T₁·k + t₁ = T₂·k + t₂**
**T₁·k = T₂·k**
**T₁ = T₂**

¡Resultado notable! Para programas IV simétricos, el modelo predice igualar tiempos: T₁ = T₂.

¿Y las tasas de refuerzo obtenidas? Substituyendo T₁ = T₂ en las funciones de retroalimentación:
**r₁ = (T₁·k)/(T₁·k + t₁)**
**r₂ = (T₂·k)/(T₂·k + t₂)**

Con t₁ = t₂ y T₁ = T₂, claramente r₁ = r₂. Entonces también igualamos refuerzos.

Para el **caso general** donde t₁ ≠ t₂, el análisis es más complejo, pero se puede demostrar (ver Staddon, 1979, Apéndice) que bajo supuestos razonables:

**T₁/T₂ ≈ r₁/r₂**

Es decir, la proporción de tiempos iguala aproximadamente la proporción de refuerzos obtenidos. ¡Esto es igualación!

**Predicción del modelo de Staddon para programas IV concurrentes:**
**Aproximadamente igualación de tiempos a refuerzos.**

La intuición es clara: en programas IV, debido a rendimientos decrecientes, no es óptimo especializarse exclusivamente. Mejor distribuir tiempo entre ambas para "cosechar" los rendimientos altos iniciales de cada una sin sufrir demasiado las reducciones marginales de visitar excesivamente una sola.

### Análisis Gráfico Detallado: Visualizando Optimización

Staddon utilizó extensamente representaciones gráficas para ilustrar su modelo. Consideremos un diagrama tridimensional donde los ejes son tiempo en opción 1 (eje x), tiempo en opción 2 (eje y), y ocio (eje z implícito, determinado por la restricción x + y + z = 1).

**Representación bidimensional simplificada:**

[Figura X+1.3: Gráfica con eje x = "Ocio (L)" de 0 a 1 (de derecha a izquierda), y eje y = "Consumo/Refuerzo (C)" de 0 a máximo. El "trabajo" (I) se deduce como 1 - L - C. Las curvas de indiferencia (iso-costo) son curvas convexas. Para programas RV, la restricción es una línea recta. El óptimo ocurre donde una línea recta (restricción RV) toca la curva de indiferencia más baja posible—típicamente en una esquina.]

[Figura X+1.4: Similar pero para programas IV. La restricción ahora es una curva cóncava (rendimientos decrecientes). El óptimo ocurre donde esta curva es tangente a una curva de iso-costo—típicamente en punto interior.]

Esta visualización hace evidente por qué RV produce especialización (restricción lineal toca curvas convexas en extremos) mientras IV produce distribución (restricción cóncava se tangentiza con curvas convexas en interior).

### Incorporación de "Ocio": Efectos en Programas de Razón

Hasta ahora hemos simplificado enfocándonos en T₁ y T₂. Pero Staddon enfatizó la importancia de considerar **"ocio" (L)**—todas las demás actividades. ¿Por qué importa?

Cuando forzas a un organismo a incrementar tiempo dedicado a respuestas operantes (T₁ + T₂ mayor), no solo redistribuyes entre T₁ y T₂; también reduces L. Si ocio es valioso (parámetro c grande en función de costo), incrementar trabajo operante tiene costo adicional: menos tiempo para otras actividades valiosas.

Incorporar L explícitamente modifica predicciones cuantitativas. La función de costo completa:

**C(T₁, T₂, L) = a(T₁⁰ - T₁)² + b(T₂⁰ - T₂)² + c(L⁰ - L)²**

con restricción T₁ + T₂ + L = 1.

**Predicción interesante:** Incrementar c (hacer ocio más valioso) lleva a responder menos en general. El organismo prefiere preservar más tiempo libre aceptando menos refuerzos totales. Esto captura **saciedad**: conforme el organismo acumula refuerzos (comida), c efectivamente incrementa (menos hambre, más valor de descanso), reduciendo motivación para responder.

Staddon mostró simulaciones donde variaciones en c producen **funciones de respuesta "bitónicas"** en programas de razón: incrementos iniciales en requisito de respuesta incrementan tasa de respuesta (para compensar y mantener refuerzos), pero incrementos más allá de cierto punto la reducen (porque el costo en ocio ya no se compensa).

[Figura X+1.5: Gráfica de "Tasa de Respuesta" (eje y) vs "Requisito del Programa RV" (eje x, de RV 1 a RV 160). La curva incrementa inicialmente, alcanza un máximo alrededor de RV 40-60, luego declina. Curvas para diferentes valores de c (peso de ocio): c pequeño produce curva alta y plana, c grande produce curva con pico pronunciado que declina rápidamente.]

Estos patrones bitónicos se observan empíricamente en datos de ratas y palomas (ver Parte 3 sobre evidencia empírica).

### Minimización vs Maximización: Dos Caras de la Misma Moneda

Es importante notar que minimizar costo C(·) es equivalente a maximizar "utilidad" U(·) donde U = -C. Staddon formuló su modelo como minimización porque conceptualmente enfatiza "desviación de lo ideal", pero matemáticamente es idéntico a un problema de maximización.

Esta equivalencia conecta el modelo de Staddon con el modelo de Rachlin que revisaremos a continuación, el cual explícitamente maximiza utilidad. Ambos enfoques son duales—dos formas de expresar la misma idea fundamental de optimización bajo restricciones.

---

## PARTE 3: MODELO DE MAXIMIZACIÓN DE UTILIDAD DE RACHLIN

### Fundamentos de Teoría Microeconómica

Mientras Staddon desarrollaba su modelo de minimización de distancia, Howard Rachlin y colaboradores (especialmente con economistas conductuales John Kagel y Raymond Battalio) aplicaban teoría microeconómica estándar al comportamiento operante. Su modelo (Rachlin et al., 1981; Rachlin, 1980) adopta el framework de maximización de utilidad bajo restricciones—el modelo canónico de elección del consumidor en economía.

La idea fundamental: los organismos tienen **preferencias** sobre combinaciones (paquetes o bundles) de bienes (actividades), representadas por **función de utilidad** U(·). Esta función asigna un número real a cada paquete posible, representando cuánta "satisfacción" proporciona ese paquete. Paquetes con mayor utilidad son preferidos.

Formalmente, un paquete es un vector (x₁, x₂, ..., xₙ) especificando cantidades de cada bien. La función U(x₁, x₂, ..., xₙ) debe satisfacer:
1. **Completitud:** Para cualesquiera dos paquetes A y B, podemos ordenarlos.
2. **Transitividad:** Si U(A) > U(B) y U(B) > U(C), entonces U(A) > U(C).
3. **Monotonicidad (típicamente):** Más de un bien es mejor, todo lo demás constante. ∂U/∂xᵢ > 0.

Propiedad crucial: **utilidad marginal decreciente**:

**∂²U/∂xᵢ² < 0**

La primera unidad de un bien proporciona mucha utilidad, la segunda algo menos, la tercera aún menos, etc. Matemáticamente, U(x) es función cóncava.

Ejemplos: U(x) = log(x) o U(x) = x^α donde 0 < α < 1. Con U(x) = √x: primera unidad incrementa utilidad de 0 a 1 (+1), segunda de 1 a √2 ≈ 1.41 (+0.41), tercera de 1.41 a √3 ≈ 1.73 (+0.32), etc.

¿Por qué asumir utilidad marginal decreciente? Intuitivamente, captura saciedad y diversidad. Una pizza cuando tienes mucha hambre proporciona enorme satisfacción; la quinta pizza del día proporciona mucho menos. Similarmente, el organismo prefiere diversidad: un paquete con algo de comida, algo de agua, algo de tiempo social, es mejor que un paquete con solo comida en igual cantidad total.

### Curvas de Indiferencia y Propiedades Geométricas

Una **curva de indiferencia** es el conjunto de todos los paquetes que proporcionan la misma utilidad. Matemáticamente, para valor fijo Ū:

**{(x₁, x₂) : U(x₁, x₂) = Ū}**

**Propiedades geométricas:**

**1. Pendiente Negativa:** Si ambos bienes son deseables (∂U/∂xᵢ > 0), para mantener utilidad constante al reducir x₁, debemos incrementar x₂. Curvas se inclinan hacia abajo.

**2. No se Cruzan:** Si dos curvas se cruzaran, el punto de intersección tendría dos niveles de utilidad simultáneamente, violando la definición de función.

**3. Convexas al Origen:** Debido a utilidad marginal decreciente, curvas son típicamente **convexas** (arqueadas hacia el origen). Intuitivamente: el organismo está dispuesto a substituir grandes cantidades del bien abundante por pequeñas del bien escaso para mantener utilidad constante.

**4. Más Alejadas del Origen son Mejores:** Curvas más alejadas representan mayor utilidad. "Más es mejor": paquete (10, 10) proporciona más utilidad que (5, 5).

[Figura X+1.6: Espacio (x₁, x₂). Tres curvas de indiferencia convexas, curvándose hacia el origen. La más cercana al origen está etiquetada U₁ (baja utilidad), la intermedia U₂, la más alejada U₃ (alta utilidad). Las curvas no se cruzan.]

La **tasa marginal de sustitución** (TMS o MRS en inglés) es la pendiente de la curva en un punto:

**TMS = -dx₂/dx₁ |_U=constante**

Representa cuántas unidades de x₂ está dispuesto a renunciar el organismo para obtener una unidad adicional de x₁, manteniendo satisfacción constante. Matemáticamente:

**TMS = (∂U/∂x₁) / (∂U/∂x₂)**

Es decir, razón de utilidades marginales. La convexidad implica que TMS disminuye al moverse hacia derecha (conforme x₁ incrementa y x₂ disminuye): cuanto más tengo de x₁ relativo a x₂, menos estoy dispuesto a renunciar de x₂ por más x₁.

### Frontera de Posibilidades de Producción (FPP)

Ahora introducimos restricciones. En economía estándar, un consumidor con ingreso I y bienes con precios p₁ y p₂ enfrenta:

**p₁x₁ + p₂x₂ ≤ I**

Esta línea recta con pendiente -p₁/p₂ define todas las combinaciones que el consumidor puede pagar.

En nuestro contexto conductual, la "moneda" no es dinero sino **tiempo** (o esfuerzo/respuestas). La analogía:
- Ingreso I → Tiempo total disponible T
- Precios → "Tiempo requerido por unidad de bien"
- Bienes x₁, x₂ → Refuerzos obtenidos r₁, r₂

Pero aquí los programas de reforzamiento entran crucialmente. Programas no especifican precios fijos; especifican **funciones de retroalimentación** no-lineales relacionando tiempo invertido con refuerzos obtenidos.

Rachlin et al. llamaron a estas restricciones **frontera de posibilidades de producción** (FPP). Es el conjunto de todas las combinaciones (r₁, r₂) alcanzables dadas funciones de retroalimentación y tiempo limitado.

**Para programas RV concurrentes:**
- r₁ = kT₁/n₁
- r₂ = kT₂/n₂
- Restricción temporal: T₁ + T₂ ≤ T

Substituyendo T₂ = T - T₁ en segunda ecuación:
**r₂ = k(T - T₁)/n₂ = (kT/n₂) - (k/n₂)T₁**

Pero T₁ = (n₁/k)r₁, entonces:
**r₂ = (kT/n₂) - (n₁/n₂)r₁**

Esta es la ecuación de la FPP para RV: **línea recta** con intersecciones (kT/n₁, 0) y (0, kT/n₂) y pendiente -(n₁/n₂).

[Figura X+1.7: Espacio (r₁, r₂). La FPP es una línea recta desde (kT/n₁, 0) hasta (0, kT/n₂). Curvas de indiferencia convexas. El óptimo donde una curva es tangente a la FPP está marcado con punto negro—típicamente en una esquina para FPP lineal.]

**Para programas IV concurrentes**, la FPP es **curva cóncava** (arqueada hacia afuera), reflejando rendimientos decrecientes.

[Figura X+1.8: Similar pero FPP ahora es curva cóncava. El óptimo (tangencia) ocurre en punto interior, no esquina.]

La **tasa marginal de transformación** (TMT o MRT) es la pendiente de FPP:

**TMT = -dr₂/dr₁ |_restricción**

Representa cuántos refuerzos de tipo 2 debemos renunciar para obtener uno adicional de tipo 1, dadas restricciones tecnológicas (programas). Para RV, TMT es constante. Para IV, TMT disminuye al moverse hacia derecha.

### Condición de Tangencia: TMS = TMT

El problema de optimización:

**Maximizar U(r₁, r₂)**
**Sujeto a: (r₁, r₂) está en la FPP**

Gráficamente, queremos alcanzar la curva de indiferencia más alta que aún toque FPP. El punto de contacto es el óptimo.

**Condición matemática:** En el óptimo, curva de indiferencia debe ser **tangente** a FPP:

**TMS = TMT**

O:
**(∂U/∂r₁) / (∂U/∂r₂) = -(dr₂/dr₁)|_restricción**

Intuitivamente: la tasa a la cual el organismo está dispuesto a substituir (reflejada en preferencias, TMS) debe igualar la tasa a la cual el ambiente permite hacer esa substitución (reflejada en restricciones, TMT). Si TMS > TMT, el organismo valora r₁ más relativamente de lo que "cuesta" obtenerlo, por lo que debería incrementar r₁. Solo cuando TMS = TMT no hay incentivo para cambiar—es equilibrio.

### Derivación Gráfica de Igualación para Programas IV

Apliquemos esto a programas IV concurrentes simétricos. Consideremos:
- Dos opciones con IV idénticos: t₁ = t₂ = t
- Función de utilidad simétrica: U(r₁, r₂)
- Utilidad marginal decreciente en ambos

Las funciones de retroalimentación IV:
**r₁ = (kT₁)/(kT₁ + t)**
**r₂ = (kT₂)/(kT₂ + t)**
con T₁ + T₂ = T.

**Análisis gráfico:**

[Figura X+1.9: Espacio (r₁, r₂). La FPP es curva cóncava simétrica (debido a t₁ = t₂). Las curvas de indiferencia son simétricas también (porque U es simétrica). Por simetría, el óptimo debe estar en la diagonal de 45° donde r₁ = r₂.]

Por simetría geométrica del problema (FPP simétrica, curvas de indiferencia simétricas), el punto de tangencia debe estar en la diagonal donde r₁ = r₂. Esto implica T₁ = T₂ (porque las funciones de retroalimentación también son simétricas).

Por lo tanto:
**T₁/T₂ = r₁/r₂ = 1**

¡Igualación perfecta!

**Para programas IV asimétricos** (t₁ ≠ t₂): El análisis es más complejo algebraicamente, pero se puede demostrar (ver Rachlin et al., 1981, Apéndice) que bajo supuestos razonables sobre forma de U(·), la solución aproxima:

**T₁/T₂ ≈ r₁/r₂**

La intuición: TMS = TMT se satisface aproximadamente cuando tiempos igualan refuerzos, debido a forma específica de las funciones de retroalimentación IV.

### Derivación Gráfica de Preferencia Exclusiva para Programas RV

Para programas RV, la FPP es **línea recta**. Las curvas de indiferencia son **convexas**. Un resultado geométrico estándar: cuando una línea recta contacta curvas convexas, el contacto ocurre en **punto extremo** (esquina), no punto interior.

[Figura X+1.10: FPP lineal desde (r₁^max, 0) hasta (0, r₂^max). Curvas de indiferencia convexas. La curva más alta que toca FPP lo hace en una esquina—digamos (r₁^max, 0) si opción 1 es más rica.]

Intuitivamente: supongamos óptimo estuviera en punto interior con r₁ > 0 y r₂ > 0. Debido a convexidad de curvas y linealidad de FPP, siempre habría curva ligeramente más alta que tocaría FPP en extremo. Por tanto, punto interior no puede ser óptimo.

**Predicción del modelo de Rachlin para programas RV:**
**Preferencia exclusiva o fuertemente sesgada hacia alternativa más rica.**

Esto coincide con Staddon y con evidencia empírica.
### Ajuste Empírico: Experimentos de Green, Kagel, & Battalio

Rachlin, Kagel, Battalio y Green condujeron elegantes experimentos para estimar empíricamente el exponente α en función de utilidad U(r₁, r₂) = r₁^α + r₂^α.

La lógica: midiendo cómo organismos distribuyen comportamiento ante diferentes programas, podemos inferir curvatura de su función de utilidad. Un α cercano a 1 indica substitución casi perfecta entre refuerzos (curvas de indiferencia casi lineales). Un α cercano a 0 indica complementariedad casi perfecta (curvas en forma de L). Un α intermedio (digamos 0.5) indica substitución imperfecta con utilidad marginal decreciente significativa.

**Procedimiento:** Presentaron a palomas programas IV concurrentes donde ambas alternativas entregaban comida, pero manipularon sistemáticamente razones de refuerzos disponibles (programando diferentes valores de intervalo). Midiendo distribuciones de respuestas o tiempos en equilibrio, estimaron α mediante ajuste de máxima verosimilitud.

**Resultados clave:**

1. **Green, Kagel, & Battalio (1987)** estimaron α ≈ 0.6-0.7 para palomas. Esto indica substitución imperfecta: los dos tipos de refuerzos son parcialmente substitutos pero no perfectamente. Convexidad de curvas de indiferencia es moderada.

2. Estos valores de α predicen aproximadamente igualación para programas IV concurrentes y preferencia fuerte (aunque quizá no perfectamente exclusiva) para programas RV concurrentes, consistente con observaciones empíricas.

3. La robustez del ajuste a través de múltiples experimentos y condiciones sugiere que el modelo captura algo real sobre preferencias de organismos.

**Ejemplo numérico ilustrativo:**

Considere dos programas IV concurrentes: IV 30-seg (opción 1) vs IV 60-seg (opción 2). La razón de tasas programadas es 2:1 (opción 1 dos veces más rica).

Con α = 0.7, las predicciones del modelo (derivadas mediante optimización numérica de U sujeto a FPP de los programas IV) son aproximadamente:
- T₁/T₂ ≈ 1.8 (ligero undermatching)
- r₁/r₂ ≈ 1.9 (cercano a 2:1)

Datos empíricos típicos muestran T₁/T₂ ≈ 1.7-1.9, coincidiendo bien con predicciones.

**Función Bitónica en Programas de Razón:**

Otro resultado importante fue la demostración de funciones de respuesta bitónicas en programas RV simples. Green et al. variaron requisito de razón de RV 1 a RV 160 y midieron tasa de respuesta en equilibrio.

[Figura X+1.11: Gráfica basada en datos reales. Eje x: "Requisito de Razón (n)" de 1 a 160. Eje y: "Tasa de Respuesta (resp/min)". Cuatro curvas (una por cada paloma) muestran patrón bitónico: incremento inicial hasta máximo alrededor de RV 40-60, luego declinación. Esto valida predicción de Staddon sobre rol del "ocio".]

Cuando requisito de razón es bajo (RV 1-20), incrementarlo lleva al organismo a incrementar tasa de respuesta para compensar y mantener refuerzos. Pero más allá de cierto punto (RV 60-80), incrementos adicionales en requisito llevan a reducción en tasa: el costo en "ocio" (tiempo dedicado a otras actividades) ya no se compensa por los refuerzos adicionales. El organismo prefiere "trabajar" menos y aceptar menos refuerzos.

Este patrón bitónico es predicción natural de modelos de optimización que incorporan explícitamente ocio con valor positivo (parámetro c en modelo de Staddon). No es predicción obvia de modelos más simples que ignoran actividades alternativas.

---

## PARTE 4: COMPARACIÓN, EVALUACIÓN Y SÍNTESIS

### Tabla Comparativa: Staddon vs Rachlin

| **Aspecto** | **Modelo de Staddon** | **Modelo de Rachlin** |
|-------------|----------------------|----------------------|
| **Marco Conceptual** | Minimización de distancia desde bliss point | Maximización de función de utilidad microeconómica |
| **Formulación Matemática** | C = a(T₁⁰-T₁)² + b(T₂⁰-T₂)² + c(L⁰-L)² | U = r₁^α + r₂^α, maximizar U sujeto a FPP |
| **Representación Geométrica** | Elipses de costo centradas en bliss point | Curvas de indiferencia convexas |
| **Restricciones Clave** | Temporal (T₁+T₂+L=1) + Retroalimentación | Frontera de Posibilidades de Producción (FPP) |
| **Predicción para IV** | Igualación aproximada (T₁/T₂ ≈ r₁/r₂) | Igualación (TMS = TMT → T₁/T₂ = r₁/r₂) |
| **Predicción para RV** | Preferencia exclusiva | Preferencia exclusiva (esquina de FPP lineal) |
| **Rol del "Ocio"** | Explícito (tercer comportamiento con costo c) | Implícito (puede incorporarse como tercer bien) |
| **Parámetros Libres** | a, b, c (pesos), T₁⁰, T₂⁰, L⁰ (bliss points) | α (exponente de utilidad) |
| **Origen Intelectual** | Ecología conductual, teoría forrajeo óptimo | Microeconomía, teoría del consumidor |
| **Énfasis** | Costo de desviación, optimización geométrica | Preferencias, substitución, utilidad marginal |

### Similitudes Fundamentales

A pesar de diferencias superficiales, ambos modelos son esencialmente **modelos de optimización restringida**:

1. **Ambos postulan función objetivo:** Staddon minimiza costo, Rachlin maximiza utilidad. Formulaciones duales—minimizar "anti-utilidad" es equivalente a maximizar utilidad.

2. **Ambos reconocen restricciones:** Tiempo es escaso, programas limitan qué distribuciones de refuerzos son alcanzables.

3. **Ambos derivan igualación para IV:** No es suposición ad hoc sino consecuencia matemática de optimización bajo rendimientos decrecientes.

4. **Ambos predicen preferencia exclusiva para RV:** Consecuencia de optimización bajo rendimientos constantes (linealidad).

5. **Ambos son estáticos:** Caracterizan equilibrio óptimo, no dinámica de cómo se alcanza.

### Diferencias Clave y sus Implicaciones

**1. Interpretabilidad de Parámetros:**
- Parámetros de Staddon (a, b, c, bliss points) son conceptualmente intuitivos pero difíciles de medir independientemente. ¿Cómo determinar T₁⁰ sin observar comportamiento bajo restricciones?
- Parámetro α de Rachlin puede estimarse empíricamente de datos de elección y tiene interpretación económica estándar (elasticidad de substitución). Facilita pruebas más rigurosas.

**2. Énfasis en "Ocio":**
- Staddon hace explícito rol de ocio (L) y predice efectos de saciedad y funciones bitónicas cuando c (costo de reducir ocio) es grande.
- Rachlin puede incorporar ocio como tercer bien, pero típicamente enfoca trade-offs entre dos refuerzos operantes. Incorporación requeriría análisis tridimensional.

**3. Conexiones Disciplinarias:**
- Staddon conecta con ecología conductual y teoría forrajeo, facilitando comparaciones entre laboratorio y conducta natural.
- Rachlin conecta con economía conductual y neuroeconomía, facilitando integraciones con estudios de toma de decisiones humanas y neuroimagen.

**4. Generalización:**
- Formulación de Rachlin basada en utilidad microeconómica se extiende naturalmente a situaciones con más alternativas, múltiples tipos de refuerzos, presupuestos variables.
- Formulación de Staddon con bliss points específicos puede requerir especificación ad hoc de cómo se determinan en situaciones novedosas.

A pesar de diferencias, convergencia de predicciones centrales sugiere que ambos capturan principios fundamentales correctos sobre optimización conductual.

### Limitaciones Compartidas: ¿Qué No Explican?

Aunque poderosos, estos modelos enfrentan limitaciones:

#### 1. Suponen Conocimiento Global del Entorno

Ambos asumen que el organismo tiene representación completa de funciones de retroalimentación: "conoce" que opción 1 es IV 60-seg, opción 2 es IV 30-seg, etc. Pero, ¿cómo se adquiere este conocimiento? Los modelos no especifican proceso de aprendizaje. En nuevo ambiente, el organismo debe explorar, estimar tasas mediante experiencia, actualizar representaciones. Los modelos son silenciosos sobre esta fase—solo caracterizan equilibrio una vez que conocimiento es perfecto.

#### 2. Son Estáticos, No Dinámicos

Predicen estado final de equilibrio, no trayectoria temporal. No especifican qué sucede momento a momento durante primeras 10, 100, o 1000 respuestas. Para entender transitorios, adquisición, extinción, y comportamiento en ambientes dinámicos (donde contingencias cambian), necesitamos modelos algorítmicos especificando reglas de actualización basadas en experiencia. Esto es tema del Capítulo X+2.

#### 3. Requieren Parámetros Difíciles de Estimar Independientemente

Los modelos tienen parámetros (a, b, c, bliss points en Staddon; α en Rachlin) que deben estimarse, típicamente ajustando a mismos datos que el modelo pretende explicar. Esto reduce poder predictivo a priori. Idealmente, querríamos medir estos parámetros independientemente (en tarea diferente) y luego usarlos para predecir comportamiento en programas concurrentes. Técnicamente difícil aunque no imposible.

#### 4. No Explican Undermatching sin Extensiones

Como documentamos en Capítulo X, igualación empírica típicamente exhibe **undermatching**: s ≈ 0.7-0.9 en lugar de 1.0 en ecuación generalizada B₁/B₂ = b(R₁/R₂)^s. Modelos de optimización básicos predicen s = 1 (igualación perfecta). Para explicar undermatching, debemos agregar supuestos: ruido en percepción de tasas, costo de cambiar entre alternativas, exploración continua adaptativa en ambientes inciertos, o sesgo hacia respuestas de menor esfuerzo. Estas extensiones son razonables pero reducen parsimonia.

#### 5. Problemas con Efectos de Contexto

Belke (1992) demostró que preferencia entre dos opciones depende no solo de sus razones relativas sino del contexto global: preferencias más extremas en contextos ricos que en contextos pobres, aun cuando razón relativa es idéntica.

**Diseño de Belke:**
- **Contexto Rico:** IV 30 vs IV 60 (razón 2:1)
- **Contexto Pobre:** IV 60 vs IV 120 (razón 2:1)

Modelos básicos de optimización predicen misma preferencia en ambos contextos (solo razón relativa importa). Pero organismos mostraron preferencias más extremas en Contexto Rico.

Para capturar efectos de contexto, necesitamos mecanismos adicionales: normalización por tasa total, efectos de contraste conductual, o representaciones de rango-frecuencia. Extensiones razonables pero más allá de modelos básicos.

### El Valor de los Modelos Normativos

A pesar de limitaciones, estos modelos tienen valor científico profundo:

**1. Fundamentación Normativa:** Proporcionan estándar contra el cual evaluar desempeño real. Si organismos se desvían sistemáticamente del óptimo, esto revela restricciones omitidas. Las desviaciones son informativas.

**2. Predicciones Cualitativas Robustas:** Predicciones centrales—igualación en IV, preferencia exclusiva en RV—no dependen de valores exactos de parámetros y han sido validadas extensamente. Sugiere que principios de optimización capturan algo fundamental.

**3. Unificación Conceptual:** Muestran que fenómenos aparentemente dispares (igualación, preferencia exclusiva, funciones bitónicas) pueden derivarse de principio unificador: optimización bajo restricciones. Simplifica y organiza entendimiento.

**4. Puente entre Disciplinas:** Conectan conducta operante con ecología conductual, economía, teoría de decisiones, y aprendizaje por refuerzo computacional. Facilitan integración interdisciplinaria.

**5. Guía para Modelos Algorítmicos:** Sabiendo qué debería ser óptimo restringe y guía desarrollo de modelos algorítmicos especificando cómo se implementa esa optimización. El próximo capítulo explorará estos algoritmos.

### Evidencia Empírica: Resumen de Hallazgos Clave

**Programas RV Concurrentes:**
- **Predicción:** Preferencia exclusiva por alternativa más rica
- **Evidencia:** Green, Rachlin, and Hanson (1983) y estudios subsecuentes con palomas muestran efectivamente fuerte preferencia (90-95% de respuestas) hacia opción mejor
- **Conclusión:** Favorece modelos de optimización sobre igualación como descripción de RV concurrentes

**Programas IV Concurrentes:**
- **Predicción:** Igualación aproximada
- **Evidencia:** Como documentamos en Capítulo X, igualación describe muy bien datos de IV concurrentes, aunque con undermatching (s ≈ 0.8-0.9)
- **Conclusión:** Modelos capturan cualitativamente igualación, aunque undermatching requiere explicación adicional

**Función Bitónica en Programas de Razón:**
- **Predicción:** Conforme incrementa requisito de razón, tasa de respuesta primero incrementa, alcanza máximo, luego declina
- **Evidencia:** Datos de ratas y palomas muestran efectivamente este patrón (ver Green et al., 1987)
- **Conclusión:** Valida predicción sobre rol del "ocio" y trade-offs con otras actividades valiosas

### Transición al Capítulo X+2: Necesidad de Modelos Algorítmicos

Los modelos de optimización molar nos dicen **qué** distribución conductual es óptima en equilibrio, pero no **cómo** los organismos alcanzan ese equilibrio mediante procesos operando en tiempo real.

Para explicar trayectorias temporales, aprendizaje, adaptación a ambientes cambiantes, y desviaciones sistemáticas del óptimo, necesitamos modelos especificando:

1. **Reglas de actualización:** ¿Cómo se actualizan estimaciones de tasas de refuerzo con cada experiencia? (Conectará con Rescorla-Wagner.)

2. **Reglas de elección local:** ¿Qué determina elección en cada momento dado conocimiento actual? (No necesariamente óptimo global.)

3. **Exploración vs explotación:** ¿Cómo balancea el organismo entre explotar conocimiento actual y explorar para refinar estimaciones?

4. **Sensibilidad a historia reciente:** ¿Cómo se ponderan experiencias recientes vs remotas?

El Capítulo X+2 abordará estos temas, explorando modelos algorítmicos de maximización local: melioration (Herrnstein & Vaughan), maximización momentánea (Shimp), y aprendizaje por refuerzo basado en valores Q. Veremos cómo reglas locales simples—que no requieren conocimiento global ni computación de óptimos—pueden aproximar (y a veces desviarse sistemáticamente de) las predicciones de modelos de optimización molar.

En particular, examinaremos evidencia de **suboptimalidad sistemática**: situaciones donde organismos convergen hacia distribuciones que son estables pero no óptimas. El experimento crítico de Herrnstein & Vaughan (1980) con programas RV-IV concurrentes mostrará que organismos pueden estabilizarse en distribuciones que obtienen 15-20% menos refuerzo que lo óptimo. Esto no es fallo o error—es consecuencia predecible de seguir reglas locales de melioration que, aunque típicamente adaptativas, pueden llevar a trampas en ciertas configuraciones de contingencias.

Estos hallazgos no invalidan modelos de optimización molar; más bien, revelan sus límites de aplicabilidad y motivan análisis algorítmico complementario. El nivel computacional nos dice qué sería óptimo si el organismo tuviera conocimiento perfecto y capacidad computacional ilimitada. El nivel algorítmico nos dice qué realmente ocurre con conocimiento imperfecto y reglas de procesamiento locales.

---

## TABLA RESUMEN DE CONCEPTOS CLAVE

| **Concepto** | **Descripción** | **Ecuación/Formalización** | **Contexto** |
|-------------|-----------------|---------------------------|-------------|
| **Punto de Felicidad (Bliss Point)** | Distribución preferida de actividades en ausencia de restricciones | (T₁⁰, T₂⁰, L⁰) | Staddon: punto de referencia para medir costo |
| **Función de Costo Cuadrática** | Costo de desviarse del bliss point, penaliza desviaciones proporcionalmente al cuadrado | C = a(T₁⁰-T₁)² + b(T₂⁰-T₂)² + c(L⁰-L)² | Staddon: función objetivo a minimizar |
| **Restricción Temporal** | Tiempo total debe distribuirse entre todas actividades | T₁ + T₂ + L = 1 | Restricción fundamental en ambos modelos |
| **Función de Retroalimentación RV** | Relación lineal entre tiempo dedicado y refuerzos obtenidos en programas de razón | r = kT/n | Caracteriza programas RV; rendimientos constantes |
| **Función de Retroalimentación IV** | Relación no-lineal con rendimientos decrecientes en programas de intervalo | r ≈ (kT)/(kT + t) | Caracteriza programas IV; crucial para derivar igualación |
| **Función de Utilidad** | Asigna valor a combinaciones de actividades o refuerzos | U(r₁, r₂) = r₁^α + r₂^α | Rachlin: función objetivo a maximizar |
| **Utilidad Marginal Decreciente** | Cada unidad adicional proporciona menos utilidad incremental | ∂²U/∂rᵢ² < 0 | Genera convexidad de curvas de indiferencia |
| **Curva de Indiferencia** | Combinaciones de dos bienes que proporcionan igual utilidad | {(r₁, r₂) : U(r₁, r₂) = Ū} | Rachlin: herramienta geométrica para visualizar preferencias |
| **Tasa Marginal de Sustitución (TMS)** | Cuánto de un bien dispuesto a renunciar por unidad del otro, manteniendo utilidad constante | TMS = (∂U/∂r₁) / (∂U/∂r₂) | Pendiente de curva de indiferencia; refleja preferencias |
| **Frontera de Posibilidades de Producción (FPP)** | Conjunto de combinaciones de refuerzos alcanzables dadas restricciones | Línea para RV, curva cóncava para IV | Restricción tecnológica impuesta por programas |
| **Tasa Marginal de Transformación (TMT)** | Cuántos refuerzos de un tipo deben renunciarse para obtener uno del otro | TMT = -dr₂/dr₁ (pendiente de FPP) | Refleja trade-offs impuestos por ambiente |
| **Condición de Tangencia** | En el óptimo, preferencias deben igualar restricciones | TMS = TMT | Rachlin: condición matemática para maximización |
| **Preferencia Exclusiva** | Dedicar todo tiempo operante a alternativa más rica | T₁ ≈ 1, T₂ ≈ 0 (o viceversa) | Predicción de ambos modelos para programas RV |
| **Igualación** | Proporciones de tiempo/respuestas igualan proporciones de refuerzos | T₁/T₂ = r₁/r₂ | Predicción de ambos modelos para programas IV |
| **Exponente α** | Parámetro en función de utilidad reflejando elasticidad de substitución | 0 < α < 1 típicamente | Rachlin: estimado empíricamente como α ≈ 0.6-0.7 en palomas |
| **Costo de Oportunidad** | Valor de alternativa no elegida; tiempo en A es tiempo no disponible para B | Implícito en restricción temporal | Concepto económico central en análisis de optimización |
| **Función Bitónica** | Función que incrementa, alcanza máximo, luego declina | Tasa de respuesta vs requisito de razón | Predicción de modelos con ocio explícito; validada empíricamente |

---

## SÍNTESIS CONCEPTUAL

Los modelos de optimización molar de Staddon y Rachlin representan el análisis de conducta de elección en el nivel computacional: especifican qué distribuciones conductuales serían óptimas bajo supuestos de que organismos, moldeados por selección natural, aproximan soluciones que maximizan fitness. Aunque difieren en formalismo—Staddon minimiza distancia desde bliss point, Rachlin maximiza utilidad microeconómica—ambos convergen en predicciones cruciales derivadas mediante análisis gráfico: preferencia exclusiva para programas RV concurrentes (donde rendimientos son constantes) e igualación para programas IV concurrentes (donde rendimientos son decrecientes). Estas predicciones no son postulados empíricos ad hoc sino consecuencias geométricas de optimización bajo restricciones. La validación empírica—especialmente preferencia exclusiva en RV, igualación aproximada en IV, y funciones bitónicas de respuesta—sugiere que principios de optimización capturan aspectos fundamentales de cómo comportamiento se adapta a contingencias. Sin embargo, estos modelos tienen limitaciones: son estáticos (no explican dinámicas temporales), requieren conocimiento global (no especifican aprendizaje), y no capturan naturalmente desviaciones como undermatching o efectos de contexto sin extensiones. Su valor radica en proporcionar estándares normativos contra los cuales evaluar desempeño real, revelando qué restricciones cognitivas deben incorporarse para explicar completamente comportamiento observado. Estos modelos establecen fundamento teórico para capítulos siguientes, donde exploraremos algoritmos locales que implementan aproximaciones a estos óptimos sin requerir computación global, conectando nivel computacional con mecanismos psicológicos y neurales que realmente operan en tiempo real.

---

## LECTURAS RECOMENDADAS

### Fundamentales (Comprensión Básica)

**Rachlin, H. (1980).** Economics and behavioral psychology. In J. E. R. Staddon (Ed.), *Limits to action: The allocation of individual behavior* (pp. 205-236). Academic Press.
- Introducción accesible a aplicación de teoría microeconómica al comportamiento operante. Presenta conceptos de curvas de indiferencia, FPP, y condición de tangencia con ejemplos conductuales claros. Énfasis en análisis gráfico.

**Staddon, J. E. R. (1979).** Operant behavior as adaptation to constraint. *Journal of Experimental Psychology: General, 108*(1), 48-67.
- Artículo seminal que introduce modelo de distancia mínima y cinco principios de optimización conductual. Matemáticas accesibles con énfasis conceptual y visualizaciones gráficas extensas.

**Allison, J. (1983).** *Behavioral economics.* Praeger Publishers.
- Libro de texto completo sobre economía conductual. Capítulos 3-5 cubren modelos de optimización, curvas de indiferencia, y aplicaciones a programas de reforzamiento con numerosas figuras y ejemplos.

### Avanzadas (Profundización Teórica)

**Rachlin, H., Battalio, R., Kagel, J., & Green, L. (1981).** Maximization theory in behavioral psychology. *Behavioral and Brain Sciences, 4*(3), 371-388.
- Presentación formal del modelo de maximización de utilidad con derivaciones completas. Incluye 28 comentarios de expertos y respuesta detallada de autores, ofreciendo panorama de debates en el campo.

**Staddon, J. E. R., & Motheral, S. (1978).** On matching and maximizing in operant choice experiments. *Psychological Review, 85*(5), 436-444.
- Análisis técnico de relación entre igualación y maximización. Muestra bajo qué condiciones coinciden y cuándo divergen. Incluye derivaciones algebraicas detalladas.

**Herrnstein, R. J., & Vaughan, W. (1980).** Melioration and behavioral allocation. In J. E. R. Staddon (Ed.), *Limits to action* (pp. 143-176). Academic Press.
- Aunque sobre melioration (tema de próximo capítulo), compara modelos de maximización global con reglas locales, estableciendo contrastes importantes. Esencial para entender transición entre capítulos.

### Experimentos Críticos

**Green, L., Kagel, J. H., & Battalio, R. C. (1987).** Consumption-leisure tradeoffs in pigeons: Effects of changing marginal wage rates. *Journal of the Experimental Analysis of Behavior, 47*(1), 17-28.
- Estimación empírica del exponente α mediante manipulación sistemática de "salarios" (tasas de refuerzo). Validación cuantitativa del modelo de Rachlin con ajustes estadísticos rigurosos.

**Baum, W. M., & Rachlin, H. C. (1969).** Choice as time allocation. *Journal of the Experimental Analysis of Behavior, 12*(6), 861-874.
- Experimento clásico demostrando que palomas distribuyen tiempo (no solo respuestas) entre alternativas concurrentes según tasas de refuerzo. Validación empírica de perspectiva molar y análisis de distribuciones temporales.

**Nevin, J. A. (1969).** Interval reinforcement of choice behavior in discrete trials. *Journal of the Experimental Analysis of Behavior, 12*(6), 875-885.
- Test crítico del modelo de maximización momentánea en ensayos discretos. Muestra que organismos no maximizan probabilidades instantáneas, favoreciendo modelos molares sobre locales.

### Aplicaciones y Extensiones

**Rachlin, H., & Green, L. (1972).** Commitment, choice and self-control. *Journal of the Experimental Analysis of Behavior, 17*(1), 15-22.
- Aplicación de teoría de optimización a problemas de autocontrol y elección intertemporal. Muestra cómo modelos explican conducta impulsiva y estrategias de precompromiso.

**Herrnstein, R. J., Loewenstein, G. F., Prelec, D., & Vaughan, W. (1993).** Utility maximization and melioration: Internalities in individual choice. *Journal of Behavioral Decision Making, 6*(3), 149-185.
- Integra perspectivas de utilidad con evidencia de suboptimalidad sistemática. Discute implicaciones para economía conductual, salud pública, y políticas de intervención.

**Madden, G. J., & Bickel, W. K. (Eds.). (2010).** *Impulsivity: The behavioral and neurological science of discounting.* American Psychological Association.
- Aplicaciones contemporáneas de modelos de optimización a descuento temporal, adicción, y toma de decisiones clínicas. Capítulo 2 conecta modelos de Rachlin con neurociencia.

### Conexiones con Neurociencia

**Glimcher, P. W. (2011).** *Foundations of neuroeconomic analysis.* Oxford University Press.
- Integra teoría de utilidad microeconómica con neurociencia de toma de decisiones. Capítulos 4-6 discuten cómo curvas de indiferencia y TMS podrían representarse neuralmente en córtex orbitofrontal y parietal.

**Padoa-Schioppa, C., & Assad, J. A. (2006).** Neurons in orbitofrontal cortex encode economic value. *Nature, 441*(7090), 223-226.
- Evidencia de que neuronas en córtex orbitofrontal codifican valor subjetivo (utilidad) de opciones de forma consistente con teoría microeconómica. Conexión directa con modelos de Rachlin.

**Schultz, W., Dayan, P., & Montague, P. R. (1997).** A neural substrate of prediction and reward. *Science, 275*(5306), 1593-1599.
- Aunque sobre error de predicción (tema de capítulos posteriores), establece que dopamina codifica señales de valor consistentes con teorías de optimización. Muestra que cerebro implementa computaciones que aproximan soluciones óptimas.

### Históricas (Contexto y Desarrollo)

**Premack, D. (1965).** Reinforcement theory. In D. Levine (Ed.), *Nebraska Symposium on Motivation* (Vol. 13, pp. 123-180). University of Nebraska Press.
- Trabajo fundacional que reinterpretó refuerzo en términos de restricciones temporales y probabilidades de respuesta, inspirando modelos de optimización posteriores. Introdujo principio de Premack sobre relaciones entre conductas.

**Herrnstein, R. J. (1970).** On the law of effect. *Journal of the Experimental Analysis of Behavior, 13*(2), 243-266.
- Desarrollo de ecuación cuantitativa de la ley del efecto. Aunque descriptiva, establece fenómenos que modelos de optimización intentan explicar. Punto de partida histórico para análisis molar de elección.

**Stephens, D. W., & Krebs, J. R. (1986).** *Foraging theory.* Princeton University Press.
- Texto clásico sobre teoría de forrajeo óptimo en ecología conductual. Capítulos 2-3 sobre teorema del valor marginal y modelos de optimización proporcionan contexto evolutivo y paralelos con conducta operante.

---

**FIN DEL CAPÍTULO X+1**
