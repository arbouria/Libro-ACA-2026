# CAPÍTULO X+1
# MODELOS DE OPTIMIZACIÓN Y MAXIMIZACIÓN LOCAL

---

## INTRODUCCIÓN

En el Capítulo X analizamos cómo los organismos distribuyen su comportamiento en situaciones de elección recurrente, documentando el fenómeno de igualación: la tendencia robusta a distribuir respuestas proporcionalmente a los refuerzos obtenidos. Este patrón cuantitativo—capturado elegantemente por la ecuación generalizada de igualación—se observa consistentemente en diversas especies, programas de reforzamiento, y tipos de reforzadores. Sin embargo, describir un fenómeno empírico no es lo mismo que explicarlo. Saber que los organismos igualan no nos dice *por qué* igualan, ni qué mecanismos psicológicos o computacionales producen este patrón observable.

La transición de la descripción a la explicación requiere desarrollar modelos teóricos que especifiquen los procesos subyacentes. En este capítulo examinaremos cinco familias principales de modelos que intentan explicar la igualación y otros fenómenos de elección:

Primero, exploraremos **modelos de optimización molar** (Staddon, Rachlin) que asumen que los organismos maximizan alguna medida global de valor a lo largo del tiempo. Estos modelos adoptan una perspectiva normativa, preguntando qué distribuciones de comportamiento serían óptimas bajo ciertas restricciones, y prediciendo que los organismos evolucionados se aproximarán a esas soluciones óptimas. Veremos cómo, bajo supuestos específicos, estos modelos pueden derivar formalmente la igualación como una consecuencia de maximización.

Segundo, analizaremos **modelos de maximización local** (melioration, maximización momentánea) que proponen que los organismos siguen reglas locales simples—como "cambiar hacia la alternativa con mayor tasa local de refuerzo"—sin necesidad de representar o computar medidas globales. Estos modelos operan en una escala temporal más corta y no requieren que el organismo tenga "conocimiento" de las contingencias completas del ambiente.

Tercero, examinaremos **modelos de aprendizaje por refuerzo** basados en valores Q aprendidos, donde el organismo actualiza gradualmente estimaciones del valor esperado de cada alternativa a través de la experiencia. Estos modelos especifican explícitamente el algoritmo de aprendizaje (típicamente reglas de actualización tipo Bush-Mosteller o Rescorla-Wagner) y conectan directamente con la literatura de condicionamiento clásico que estudiamos en capítulos previos.

Cuarto, estudiaremos **reglas de respuesta** (softmax, probit, regla de Luce) que especifican cómo los valores—sean aprendidos o conocidos—se traducen en distribuciones probabilísticas de acción. Estas reglas abordan el problema de cómo pasar de representaciones internas de valor a comportamiento observable, incorporando variabilidad estocástica y el dilema fundamental de exploración versus explotación.

Finalmente, revisaremos brevemente **perspectivas alternativas** basadas en modelos de activación (Baum, Killeen) que reconceptualizan fundamentalmente el papel del refuerzo, sugiriendo que los refuerzos no "fortalecen" respuestas sino que inducen o activan repertorios conductuales que compiten por tiempo.

Un tema central que emergerá es que estos modelos no son necesariamente competitivos sino complementarios, operando en diferentes niveles de análisis. Siguiendo la taxonomía de Marr (1982), podemos distinguir entre: (1) el **nivel computacional** que especifica qué problema se está resolviendo y por qué (modelos de optimización), (2) el **nivel algorítmico** que especifica qué procedimientos se ejecutan para resolver el problema (melioration, valores Q, reglas de actualización), y (3) el **nivel implementacional** que especifica cómo esos algoritmos se realizan en mecanismos neurales o psicológicos (reglas de respuesta, circuitos neuronales). Diferentes modelos dentro de nuestra clasificación pueden corresponder a diferentes niveles de esta jerarquía explicativa.

La estructura de este capítulo refleja esta organización conceptual. Comenzaremos con modelos que operan en escalas temporales largas y requieren representaciones globales (optimización molar), progresaremos hacia modelos que operan en escalas más cortas con representaciones más locales (melioration, valores Q), y finalmente examinaremos los mecanismos que traducen representaciones en acciones (reglas de respuesta). Al final, compararemos las predicciones de estos modelos en situaciones experimentales críticas, evaluaremos su adecuación empírica, y discutiremos sus conexiones con neurociencia cognitiva y aplicaciones.

---

## PARTE 1: MODELOS DE OPTIMIZACIÓN MOLAR

### Fundamentos de Teoría de Optimización Conductual

La aplicación de teoría de optimización al comportamiento animal tiene una larga historia en biología evolutiva. La lógica fundamental es elegante: si el comportamiento ha sido moldeado por selección natural operando durante millones de generaciones, entonces debemos esperar que los organismos se comporten de manera que maximicen fitness—supervivencia y reproducción diferencial. Dado que la obtención de recursos (alimento, agua, pareja) contribuye directamente al fitness, podríamos predecir que los organismos distribuirán su comportamiento de forma que maximice la tasa de obtención de recursos sujeto a restricciones físicas, temporales y fisiológicas.

Esta perspectiva, desarrollada extensamente en ecología conductual (Stephens & Krebs, 1986), fue introducida al análisis experimental del comportamiento principalmente por John Staddon (1979, 1983) y Howard Rachlin y colaboradores (Rachlin, Battalio, Kagel, & Green, 1981). Staddon argumentó que el análisis de optimización proporciona un marco conceptual unificador para entender el control del comportamiento por sus consecuencias. En lugar de postular "leyes del efecto" empíricas, podemos derivar predicciones cuantitativas precisas preguntando: dado un conjunto de restricciones, ¿qué distribución de comportamiento maximizaría el valor obtenido?

Staddon (1979) articuló cinco principios fundamentales que guían el análisis de optimización conductual:

**Principio 1: Competencia Temporal.** El tiempo es un recurso limitado que debe distribuirse entre actividades mutuamente excluyentes. Un organismo no puede simultáneamente forrajear en dos ubicaciones distintas, o ejecutar dos respuestas incompatibles. Esta restricción temporal fundamental significa que incrementar el tiempo dedicado a una actividad necesariamente reduce el tiempo disponible para otras.

**Principio 2: La Distribución como Unidad de Análisis.** El comportamiento debe analizarse en términos de distribuciones temporales a lo largo de períodos extendidos, no respuestas individuales. La pregunta relevante no es "¿debería emitir esta respuesta en este momento?" sino "¿qué proporción de mi tiempo total debo dedicar a esta actividad versus otras?" Esta perspectiva molar es esencial porque las consecuencias del comportamiento se acumulan temporalmente.

**Principio 3: Restricciones.** Los organismos operan bajo múltiples restricciones: físicas (un organismo no puede estar en dos lugares simultáneamente), temporales (24 horas por día), fisiológicas (capacidad limitada de procesamiento de alimento), y ambientales (las contingencias programadas del ambiente). Cualquier análisis de optimización debe especificar explícitamente las restricciones bajo las cuales opera el organismo.

**Principio 4: Ordenamiento por Valor.** El organismo puede ordenar diferentes estados o outcomes por su valor biológico. Este supuesto—que existe alguna métrica común de valor—es necesario para que tenga sentido hablar de "maximización". Sin un ordenamiento de preferencias, no hay base para seleccionar entre alternativas.

**Principio 5: Equilibrio Maximiza Valor.** Finalmente, el comportamiento en equilibrio corresponde a la distribución que maximiza valor sujeto a las restricciones. Esta es la predicción central: observaremos que los organismos convergen hacia distribuciones óptimas (o cuasi-óptimas en presencia de ruido o limitaciones cognitivas).

Es crucial entender que estos principios no constituyen afirmaciones empíricas sino más bien un *framework* conceptual. La pregunta empírica es: ¿qué tan bien describen las predicciones de modelos de optimización el comportamiento observable? Como veremos, la respuesta es compleja: en algunas situaciones los organismos se comportan de forma notablemente cercana a lo óptimo; en otras, exhiben desviaciones sistemáticas que revelan los límites del análisis de optimización.

### Modelo de Distancia Mínima de Staddon

El modelo de Staddon (1979) para elección en programas concurrentes adopta un enfoque geométrico intuitivo. La idea central es que cada organismo tiene un **punto de felicidad** (bliss point) representando la distribución ideal de actividades en ausencia de restricciones ambientales. Sin embargo, las contingencias del ambiente—las funciones de retroalimentación de los programas de reforzamiento—imponen restricciones que típicamente impiden alcanzar el punto de felicidad. El organismo debe entonces seleccionar la distribución factible que se encuentre más cerca del punto de felicidad.

Formalmente, supongamos que un organismo en una situación de elección concurrente debe distribuir su tiempo entre tres actividades: responder a la opción 1 (R₁), responder a la opción 2 (R₂), y actividades alternativas (L, de "leisure" o tiempo libre). Sea T₁ la proporción de tiempo dedicada a opción 1, T₂ a opción 2, y L a actividades alternativas. La restricción temporal fundamental es:

**T₁ + T₂ + L = 1**

En ausencia de restricciones adicionales, el organismo preferiría la distribución (T₁⁰, T₂⁰, L⁰) que llamamos el punto de felicidad. Este punto representa las proporciones ideales basadas en la "utilidad intrínseca" de cada actividad.

El modelo postula que las desviaciones del punto de felicidad generan **costo psicológico**, formalizado como una función cuadrática:

**C = a(T₁⁰ - T₁)² + b(T₂⁰ - T₂)² + c(L⁰ - L)²**

donde a, b, c son parámetros positivos que determinan la importancia relativa de cada actividad. Esta función cuadrática implica que las desviaciones pequeñas del punto de felicidad son menos costosas que desviaciones grandes (costos crecientes marginalmente), y que desviaciones en cualquier dirección (más o menos) son igualmente costosas.

El problema de optimización es minimizar C sujeto a las restricciones temporales y a las funciones de retroalimentación de los programas. Para programas RV concurrentes, donde las funciones de retroalimentación son lineales (r = R/n), Staddon demostró que la solución óptima es típicamente una **solución de esquina**: el organismo debe dedicar todo su tiempo a una sola alternativa. Esto predice preferencia exclusiva en RV-RV, consistente con datos empíricos.

Para programas IV concurrentes, donde las funciones de retroalimentación son no-lineales con rendimientos decrecientes, Staddon mostró que bajo supuestos específicos sobre los parámetros, la solución óptima puede aproximarse a igualación: T₁/T₂ ≈ r₁/r₂. La intuición es que las curvas de indiferencia convexas y las restricciones no-lineales (cóncavas) se intersectan en un punto interior donde la tangencia produce igualación de tasas.

**Evaluación Crítica:** El modelo de Staddon proporciona fundamentación formal rigurosa y predice correctamente la diferencia entre RV y IV. Sin embargo, enfrenta limitaciones importantes: (1) el punto de felicidad es difícil de medir independientemente, (2) tiene múltiples parámetros libres que pueden ajustarse para acomodar diversos patrones, y (3) no especifica el proceso de aprendizaje mediante el cual se adquiere conocimiento de las funciones de retroalimentación.

### Modelo de Maximización de Utilidad de Rachlin

Howard Rachlin y colaboradores (Rachlin et al., 1981) desarrollaron un enfoque alternativo basado explícitamente en teoría microeconómica de elección del consumidor. Su modelo adopta el concepto de **función de utilidad**—una representación matemática de las preferencias del organismo sobre diferentes combinaciones de reforzadores.

Una función de utilidad U(r₁, r₂) asigna un número real a cada combinación posible de refuerzos obtenidos, donde valores más altos representan mayor "satisfacción" o "valor" subjetivo. Una propiedad fundamental típicamente asumida es **utilidad marginal decreciente**: el incremento en utilidad producido por una unidad adicional de un reforzador disminuye conforme ya se ha obtenido más de ese reforzador. Matemáticamente: ∂U/∂r₁ > 0 (más es mejor) pero ∂²U/∂r₁² < 0 (cada unidad adicional contribuye menos).

Una forma funcional común es U(r₁, r₂) = u(r₁) + u(r₂) donde u(r) = r^α con 0 < α < 1. Esta función exhibe utilidad marginal decreciente.

Dado U(r₁, r₂), podemos definir **curvas de indiferencia**: conjuntos de combinaciones (r₁, r₂) que producen el mismo nivel de utilidad. Estas curvas tienen propiedades geométricas importantes: (1) pendiente negativa, (2) convexas hacia el origen, (3) no se intersectan, y (4) más alto es mejor.

La pendiente de una curva de indiferencia se llama **tasa marginal de sustitución** (MRS): MRS = (∂U/∂r₁)/(∂U/∂r₂). Esta tasa indica cuántas unidades de r₂ el organismo está dispuesto a renunciar para obtener una unidad adicional de r₁, manteniendo utilidad constante.

Las contingencias del ambiente determinan qué combinaciones (r₁, r₂) son factibles, definiendo la **frontera de posibilidades de producción** (FPP). Para programas IV con funciones de retroalimentación hiperbólicas, la FPP es típicamente cóncava. Para programas RV con retroalimentación lineal, la FPP es una línea recta.

El problema del organismo es maximizar U(r₁, r₂) sujeto a la FPP. Geométricamente, la solución es el punto en la FPP que alcanza la curva de indiferencia más alta, caracterizado por la **condición de tangencia**: MRS = MRT, donde MRT (tasa marginal de transformación) es la pendiente de la FPP.

Para programas IV simétricos con función de utilidad aditivamente separable, Rachlin et al. (1981) mostraron que la condición de tangencia produce aproximadamente: T₁/T₂ ≈ r₁/r₂ (igualación).

Para programas RV-RV, con FPP lineal y curvas de indiferencia estrictamente convexas, la tangencia típicamente ocurre en una **solución de esquina**: el organismo dedica todo su tiempo a una sola opción, prediciendo preferencia exclusiva.

**Ajuste Empírico:** Green, Kagel, y Battalio (1987) realizaron experimentos donde variaron sistemáticamente las tasas de dos tipos de reforzadores en programas concurrentes. Ajustando el modelo a estos datos, estimaron funciones de utilidad u(r) = r^α con α ≈ 0.5-0.8, confirmando utilidad marginal decreciente.

**Evaluación Crítica:** El modelo de Rachlin tiene la ventaja de que las funciones de utilidad pueden estimarse empíricamente, a diferencia del punto de felicidad de Staddon. Sin embargo, comparte limitaciones similares: asume conocimiento global de funciones de retroalimentación, es estático (no especifica dinámica de aprendizaje), y las predicciones dependen de formas funcionales específicas.

---

## PARTE 2: MODELOS DE MAXIMIZACIÓN LOCAL

Los modelos de optimización molar que acabamos de revisar proporcionan fundamentación normativa elegante para igualación, pero enfrentan dificultades conceptuales y empíricas. Una perspectiva alternativa, desarrollada principalmente por Herrnstein y colaboradores, propone que el comportamiento de elección puede emerger de **reglas locales** simples que operan momento a momento, sin requerir representación de medidas globales.

### Melioration: Formalización Dinámica de Maximización Local

La teoría de **melioration** (del latín "melior" = mejor), desarrollada por Herrnstein y Vaughan (1980), proporciona una formalización rigurosa de maximización local. El concepto central es la **tasa local de refuerzo**: la cantidad de refuerzos obtenidos por unidad de tiempo invertida en una alternativa.

Formalmente:

**ρ₁ = r₁/T₁** (refuerzos de opción 1 / tiempo dedicado a opción 1)
**ρ₂ = r₂/T₂** (refuerzos de opción 2 / tiempo dedicado a opción 2)

Estas tasas locales contrastan con la tasa global de refuerzo R_global = (r₁ + r₂)/(T₁ + T₂ + L). La distinción es crucial: ρ₁ mide la "productividad" de la alternativa 1 cuando se está utilizando, mientras R_global mide productividad promedio sobre todo el tiempo disponible.

Melioration propone una regla dinámica simple: **Si ρ₁ > ρ₂, incrementar T₁ (dedicar más tiempo a opción 1); Si ρ₂ > ρ₁, incrementar T₂**. Matemáticamente:

**dT₁/dt = k(ρ₁ - ρ₂)**

donde k > 0 es una constante que determina la velocidad de ajuste.

El sistema alcanza equilibrio cuando dT₁/dt = 0, lo cual requiere ρ₁ = ρ₂, es decir: r₁/T₁ = r₂/T₂, o reordenando: **T₁/T₂ = r₁/r₂**. ¡Esta es precisamente la igualación de tasas locales!

**Evidencia de Suboptimalidad:** La predicción más sorprendente de melioration es que puede producir conducta subóptima. Herrnstein y Vaughan (1980) diseñaron un experimento con RV 40 versus IV 30-seg. La función de retroalimentación para RV es lineal (r₁ = R₁/40), mientras para IV es no-lineal con rendimientos decrecientes.

El análisis de maximización global muestra que el óptimo es dedicar mayoría de respuestas al IV. Sin embargo, melioration predice que el organismo dedicará mayoría al RV, porque el equilibrio local (ρ₁ = ρ₂) es subóptimo globalmente.

Herrnstein y Vaughan encontraron que palomas convergieron a un equilibrio donde dedicaban ~60-70% de respuestas al RV, obteniendo aproximadamente 15-20% menos refuerzo total del que obtendrían con la distribución óptima global. Este hallazgo crucial distingue entre maximización global y local, favoreciendo melioration.

**Evaluación Crítica:** Melioration proporciona un algoritmo plausible cognitivamente que explica tanto igualación como suboptimalidad. Sin embargo, no especifica sobre qué ventana temporal se calculan las tasas locales ρ. Ventanas diferentes producen dinámicas diferentes, aunque la predicción de equilibrio permanece robusta.

### Modelo de Valor Q y Aprendizaje por Refuerzo

Los modelos de aprendizaje por refuerzo formalizan explícitamente el proceso de aprendizaje. En estos modelos, el organismo mantiene representaciones internas del **valor esperado** de cada acción, denotados Q₁ y Q₂.

La regla de actualización más ampliamente usada es:

**Q_i(t+1) = Q_i(t) + α[r_i(t) - Q_i(t)]**

donde α ∈ (0,1) es la tasa de aprendizaje y [r_i(t) - Q_i(t)] es el error de predicción. Esta regla es idéntica a la regla de Rescorla-Wagner para condicionamiento clásico, sugiriendo que condicionamiento clásico y operante comparten mecanismos fundamentales.

Tener valores Q no es suficiente para determinar comportamiento; necesitamos **reglas de respuesta** que traduzcan valores en probabilidades de elección. Una regla simple es **greedy**: siempre elegir la alternativa con mayor Q. Sin embargo, esta regla es completamente determinística, contradice la variabilidad observada, y puede quedar atrapada en subóptimos locales.

Una regla más sofisticada es **softmax**:

**P(elegir i) = exp(βQ_i) / Σ_j exp(βQ_j)**

donde β es un parámetro de sensibilidad. Con β bajo, la elección es casi aleatoria (exploración); con β alto, es casi determinística (explotación); con β intermedio, hay balance entre ambos.

Crucialmente, con β = 1 y valores Q convergidos a tasas de refuerzo, softmax produce: P(elegir i) = Q_i / Σ_j Q_j, que es idéntica a la regla de acción proporcional de Luce (1959) y produce igualación.

**Limitación Crítica:** El modelo básico Q trata cada alternativa independientemente. Belke (1992) demostró efectos de **contexto**: palomas mostraron preferencias más extremas en contextos ricos (IV 30 vs 60) que en contextos pobres (IV 60 vs 120), aunque la razón relativa era idéntica (2:1). Modelos básicos Q no capturan estos efectos; se requieren extensiones con normalización por tasa total o modelos de rango-frecuencia.

---

## PARTE 3: REGLAS DE RESPUESTA Y EXPLORACIÓN-EXPLOTACIÓN

Representar valores no es suficiente para generar comportamiento. Necesitamos **reglas de respuesta** que traduzcan valores internos en distribuciones probabilísticas de acción. Esta sección examina las principales reglas propuestas, organizadas alrededor del dilema fundamental de **exploración versus explotación**.

### El Dilema Exploración-Explotación

Supongamos que un organismo ha aprendido Q₁ = 0.7 y Q₂ = 0.5. ¿Cómo debe actuar? Una aproximación simple es siempre elegir la opción con mayor Q (regla greedy). Sin embargo, Q son estimaciones basadas en muestras finitas y podrían ser incorrectas. Si el organismo sigue greedy estrictamente, nunca volverá a muestrear opción 2, y nunca descubrirá si Q₂ está subestimado.

Este es el **dilema exploración-explotación**: elegir entre explotar el conocimiento actual (maximizar refuerzos inmediatos) versus explorar para mejorar estimaciones (invertir en obtener información).

El dilema se estudia formalmente en el **problema de bandidos multi-brazo**: n máquinas tragamonedas con probabilidades desconocidas p_i, T ensayos, objetivo de maximizar refuerzos totales. Si las probabilidades fueran conocidas, la solución sería trivial (siempre jugar el mejor brazo). Pero las probabilidades son desconocidas y deben estimarse mediante experiencia, creando el dilema.

### Reglas Determinísticas: Greedy y ε-Greedy

La regla **greedy pura** siempre elige i = argmax Q_j. Es extremadamente simple pero tiene problemas: (1) organismos reales muestran variabilidad, y (2) puede quedar atrapada en subóptimos.

La regla **ε-greedy** introduce exploración: con probabilidad (1-ε) explotar (elegir argmax Q_j), con probabilidad ε explorar (elegir aleatoriamente). Ventajas: simple, garantiza exploración continua. Desventajas: explora ciegamente, ε es parámetro libre.

### Fundamentos Psicofísicos: Teoría de Thurstone

Para desarrollar reglas con fundamentación psicológica, recurrimos a psicofísica. Louis Thurstone (1927) propuso que sensaciones internas son variables aleatorias con ruido: S_A ~ Normal(I_A, σ²). La decisión se basa en comparar sensaciones: elegir A si S_A > S_B. La probabilidad es:

**P(elegir A) = Φ((I_A - I_B)/σ)**

donde Φ es la CDF normal. Esto produce funciones psicométricas sigmoides observadas experimentalmente.

Extendiendo a elección con valores Q con ruido de representación, obtenemos la **regla probit**: P(elegir 1) = Φ((Q₁ - Q₂)/σ).

### Regla Softmax y Conexión con Igualación

La **función logística** f(x) = 1/(1+e^(-x)) es matemáticamente más conveniente que Φ y produce predicciones casi idénticas. Aplicada a elección:

**P(elegir 1) = exp(βQ₁) / [exp(βQ₁) + exp(βQ₂)]**

Generalizando a n alternativas:

**P(elegir i) = exp(βQ_i) / Σ_j exp(βQ_j)**

Esta es la regla **softmax**. El parámetro β controla sensibilidad:
- β → 0: elección aleatoria (máxima exploración)
- β → ∞: greedy determinístico (solo explotación)
- β intermedio: balance

Crucialmente, con β = 1, softmax toma la forma P(elegir i) = Q_i / Σ_j Q_j, idéntica a la regla de acción proporcional de Luce (1959). Con valores Q convergidos a tasas de refuerzo, esto produce igualación. Por lo tanto, **igualación puede emerger de una regla de respuesta softmax con β ≈ 1**, sin necesidad de un mecanismo especial de "distribución proporcional".

Luce también consideró la forma generalizada P(elegir i) = Q_i^λ / Σ_j Q_j^λ donde λ es sensibilidad: λ=1 produce igualación, λ<1 produce undermatching, λ>1 produce overmatching. El undermatching típicamente observado (s ≈ 0.7-0.9) puede interpretarse como λ ligeramente bajo, reflejando exploración continua adaptativa.

### Evidencia Empírica

Krageloh, Davison, y Elliffe (2005) estimaron β ≈ 1.5-2.5 en palomas. Gallistel et al. (2001) encontraron que ratas ajustan dinámicamente exploración: β bajo temprano (exploración), β alto después (explotación). Daw et al. (2006) mostraron con fMRI que softmax ajusta mejor que otras reglas en humanos, con β variando entre individuos (β ≈ 1-5), y que actividad en corteza prefrontal correlaciona con nivel de exploración.

---

## PARTE 4: COMPARACIÓN DE MODELOS Y PERSPECTIVAS ALTERNATIVAS

### Evaluación Comparativa de Predicciones

La siguiente tabla resume predicciones de los principales modelos en situaciones experimentales críticas:

| **Modelo** | **IV-IV** | **RV-RV** | **RV-IV** | **Undermatching** | **Contexto** |
|------------|-----------|-----------|-----------|-------------------|-------------|
| **Staddon** | ✓ Igualación | ✓ Exclusiva | Parámetros | Posible | ✗ IIA |
| **Rachlin** | ✓ Igualación | ✓ Exclusiva | Máx global | No | ✗ IIA |
| **Melioration** | ✓ ρ₁=ρ₂ | ✓ Exclusiva | ✓ Subóptimo | Ventanas | Parcial |
| **Q+Softmax** | ✓ β apropiado | ✓ β alto | ✓ Actualización | ✓ β subóptimo | ✗ Extensión |

**Situación IV-IV:** Todos los modelos predicen igualación. Esta convergencia significa que IV-IV no discrimina entre modelos, pero también sugiere que igualación es robusta, emergiendo de principios muy generales.

**Situación RV-RV:** Igualación simple predice distribución proporcional, pero datos muestran preferencia casi exclusiva (~90%+). Staddon, Rachlin, melioration, y Q+softmax con β alto todos predicen exclusividad correctamente.

**Situación RV-IV:** Maximización global (Rachlin) predice mayoría al IV, pero datos muestran sobre-respuesta al RV (Herrnstein & Heyman, 1979; Herrnstein & Vaughan, 1980). Melioration predice correctamente este patrón subóptimo. Este es el resultado crucial que distingue maximización local de global.

**Undermatching:** Q+softmax explica mediante β subóptimo; Luce mediante λ<1. Desde perspectiva normativa, undermatching puede ser adaptativamente óptimo bajo incertidumbre: exploración continua protege contra cambios no detectados en contingencias.

**Efectos de Contexto:** Belke (1992) mostró preferencias más extremas en contextos ricos. Modelos básicos con independencia de alternativas no capturan esto. Se requieren extensiones con normalización por tasa total o modelos de rango-frecuencia.

### Síntesis Integrativa: Niveles de Marr

Ningún modelo único captura todos los fenómenos. Los modelos son complementarios, operando en diferentes niveles:

**Nivel Computacional (¿Qué y Por Qué?):**
Optimización (Staddon, Rachlin) especifica qué sería óptimo hacer. Proporciona fundamentación evolutiva: selección natural favorece aproximaciones a lo óptimo.

**Nivel Algorítmico (¿Cómo?):**
Melioration y Q-learning especifican algoritmos que aproximan optimización sin requerir sabiduría global. Son computacionalmente factibles y adaptativos.

**Nivel Implementacional (¿Con Qué Mecanismos?):**
Reglas de respuesta (softmax/probit) especifican cómo valores se traducen en acciones mediante circuitos neurales con ruido.

Implicación: Los organismos no "ejecutan" optimización global explícitamente. Evolución ha seleccionado algoritmos locales simples que típicamente producen aproximaciones razonables al óptimo.

### Perspectivas Alternativas: Modelos de Activación

**Modelo de Baum (2025):** Refuerzos no fortalecen respuestas sino que inducen actividades que compiten por tiempo. Programas RV inducen menos tiempo perdido → tasas altas; IV inducen más actividades alternativas → tasas bajas. Igualación emerge de equilibrio en competencia de actividades. Ventaja: evita circularidad de "fortalecimiento". Limitación: menos preciso cuantitativamente, identificación de actividades puede ser circular.

**Modelo de Killeen (2023):** Refuerzos activan organismo incrementando nivel general de actividad/arousal. Activación disipa exponencialmente: A(t) = A₀ exp(-t/τ). Probabilidad de respuesta proporcional a activación. RV mantiene activación alta → tasas altas; IV permite disipación → tasas bajas. Ventaja: explicación unificada. Limitación: "activación" es constructo ambiguo.

**Evaluación:** Estas perspectivas son valiosas conceptualmente: nos recuerdan que "fortalecimiento" es supuesto teórico, no hecho observable. Sin embargo, actualmente tienen menor precisión cuantitativa y evidencia empírica que modelos establecidos.

---

## PARTE 5: SÍNTESIS Y CONEXIONES

### Integración de Conceptos Principales

Este capítulo examinó cinco familias de modelos: (1) optimización molar (normativo/computacional), (2) melioration (algorítmico/dinámico), (3) Q-learning (algorítmico/computacional), (4) reglas de respuesta (implementacional), y (5) modelos de activación (alternativa conceptual).

La síntesis integrativa basada en niveles de Marr proporciona marco unificador: optimización especifica objetivos normativos seleccionados evolutivamente; melioration y Q-learning son algoritmos proxy factibles; softmax/probit son implementaciones neuronales.

### Convergencia y Divergencia

**Convergencia en IV-IV:** Todos predicen igualación, sugiriendo robustez del fenómeno.

**Divergencias Informativas:** RV-RV (exclusividad vs igualación), RV-IV (suboptimalidad), contexto (sensibilidad global). Estas divergencias favorecen modelos locales con sensibilidad contextual.

### Limitaciones y Fenómenos No Explicados

Variabilidad individual en parámetros (s, β), ajuste dinámico de exploración, transferencia entre contextos, interacción con otros procesos (pavloviano, descuento temporal), múltiples reforzadores.

### Conexiones con Capítulos Previos

**Condicionamiento Clásico:** Q-learning usa regla idéntica a Rescorla-Wagner (Q ← Q + α[r - Q]), sugiriendo mecanismos compartidos. Evidencia neural: dopamina codifica errores de predicción en paradigmas pavlovianos y operantes.

**Capítulo X:** Este capítulo proporciona explicaciones mecanísticas de fenómenos descritos allí (igualación, undermatching, diferencias RV-IV, COD).

**Psicofísica:** Teoría de Thurstone sobre ruido sensorial fundamenta reglas probabilísticas (probit, softmax), unificando discriminación perceptual y elección conductual.

### Anticipación de Aprendizaje por Refuerzo Avanzado

Los conceptos aquí (valores Q, error de predicción, softmax, exploración-explotación) son fundamentos para modelos avanzados:
- **Ambientes multi-estado:** Q(s,a) dependiente de estado y acción
- **Temporal Difference Learning:** TD(0), SARSA, Q-learning
- **Modelos Actor-Critic:** Separar valores (critic) de selección (actor)
- **Policy Optimization:** Policy gradient, PPO, TRPO
- **Deep RL:** DQN, A3C con redes neuronales

### Conexiones con Neurociencia

**Dopamina y Errores de Predicción:** Schultz et al. (1997) demostraron que neuronas dopaminérgicas codifican δ = r - Q. Ráfaga de disparos si r > Q, pausa si r < Q, sin cambio si r ≈ Q. Correspondencia notable con algoritmo Q-learning.

**Representación de Valores:** Núcleo accumbens codifica Q, corteza orbitofrontal representa outcomes esperados.

**Selección de Acción:** Estriado dorsal implementa selección mediante vías directa (facilita) e indirecta (inhibe).

**Exploración-Explotación:** Corteza prefrontal dorsolateral correlaciona con nivel de exploración; corteza cingulada anterior monitorea conflicto y errores.

### Relevancia Aplicada

**Economía Conductual:** Melioration explica presente-sesgo, adicción, ahorro insuficiente—casos donde maximización local produce suboptimalidad global.

**Manejo de Recursos:** Modelos de forrajeo óptimo predicen distribución de animales en hábitats, informan estrategias de conservación.

**Diseño de Interfaces:** Principios de exploración-explotación informan diseño de videojuegos, sistemas de recomendación, interfaces adaptativas.

**Intervenciones Clínicas:** Entender melioration ayuda diseñar intervenciones para auto-control, adicción, TDAH (modular exploración-explotación).

**Educación:** Sistemas de tutoría adaptativa ajustan dificultad basándose en errores de predicción del estudiante.

---

## TABLA RESUMEN: CONCEPTOS CLAVE

| **Concepto** | **Descripción** | **Ecuación** | **Contexto** |
|--------------|----------------|-------------|-------------|
| **Punto de Felicidad** | Distribución ideal de actividades sin restricciones | (T₁⁰, T₂⁰, L⁰) | Modelo de Staddon |
| **Función de Costo** | Penalización por desviaciones del punto de felicidad | C = a(T₁⁰-T₁)² + b(T₂⁰-T₂)² + c(L⁰-L)² | Optimización |
| **Función de Utilidad** | Preferencias sobre combinaciones de reforzadores | U(r₁,r₂); u(r)=r^α | Modelo de Rachlin |
| **Curvas de Indiferencia** | Conjuntos de (r₁,r₂) con igual utilidad | {(r₁,r₂): U=k} | Teoría de utilidad |
| **MRS** | Tasa marginal de sustitución | (∂U/∂r₁)/(∂U/∂r₂) | Optimización |
| **FPP** | Frontera de posibilidades de producción | Definida por funciones de retroalimentación | Restricciones |
| **Tasa Local** | Refuerzos por tiempo invertido | ρᵢ = rᵢ/Tᵢ | Melioration |
| **Regla de Melioration** | Cambiar hacia mayor tasa local | dT₁/dt = k(ρ₁ - ρ₂) | Maximización local |
| **Valores Q** | Utilidad esperada aprendida | Q₁, Q₂ | Q-learning |
| **Actualización Q** | Aprendizaje por error de predicción | Qᵢ ← Qᵢ + α[rᵢ - Qᵢ] | Bush-Mosteller |
| **Error de Predicción** | Diferencia refuerzo vs predicción | δ = r - Q | Señal de aprendizaje |
| **Regla Greedy** | Siempre elegir mayor Q | i = argmax Qⱼ | Explotación pura |
| **ε-Greedy** | Explotar (1-ε), explorar ε | P(explotar)=1-ε | Balance simple |
| **Softmax** | Elección proporcional a exp(βQ) | P(i) = exp(βQᵢ)/Σⱼexp(βQⱼ) | Regla estándar |
| **Parámetro β** | Sensibilidad/temperatura inversa | β→0: aleatorio; β→∞: determinístico | Control exploración |
| **Regla Probit** | Basada en ruido gaussiano | P(1) = Φ((Q₁-Q₂)/σ) | Thurstone |
| **Regla de Luce** | Proporcional con exponente | P(i) = Qᵢ^λ/ΣⱼQⱼ^λ | Acción proporcional |

---

## SÍNTESIS CONCEPTUAL

Los modelos de optimización molar proporcionan fundamentación normativa elegante para igualación, demostrando que bajo supuestos plausibles, igualar tasas de refuerzo es óptimo. Sin embargo, estos modelos requieren conocimiento global y no especifican mecanismos de aprendizaje. Los modelos de maximización local—particularmente melioration y aprendizaje por refuerzo basado en valores Q—ofrecen algoritmos computacionalmente factibles que operan sobre información local. Crucialmente, estos modelos predicen conducta subóptima en situaciones donde funciones de retroalimentación lineales (RV) y no-lineales (IV) se combinan, predicción confirmada empíricamente. Las reglas de respuesta (softmax, probit, Luce) especifican cómo valores internos se traducen en acciones probabilísticas, incorporando el dilema fundamental de exploración-explotación. Con parámetro de sensibilidad apropiado (β≈1), softmax produce igualación naturalmente, sugiriendo que igualación no requiere mecanismo especial sino que emerge de reglas de decisión probabilísticas generales. El undermatching típicamente observado puede reflejar β ligeramente subóptimo que mantiene exploración continua—adaptativo en ambientes naturales donde contingencias cambian. La convergencia de predicciones en IV-IV sugiere robustez de igualación, mientras divergencias en RV-RV y RV-IV permiten discriminar entre modelos, favoreciendo maximización local sobre global. Los modelos operan en niveles complementarios de la jerarquía de Marr: optimización especifica objetivos computacionales, melioration y Q-learning especifican algoritmos, y softmax especifica implementación. Esta arquitectura multinivel, con conexiones profundas a neurociencia (dopamina=error de predicción) y aplicaciones (economía conductual, diseño de interfaces), proporciona marco comprehensivo para entender elección adaptativa.

---

## LECTURAS RECOMENDADAS

### Lecturas Fundamentales

**Herrnstein, R. J., & Vaughan, W. (1980).** Melioration and behavioral allocation. En J. E. R. Staddon (Ed.), *Limits to Action: The Allocation of Individual Behavior* (pp. 143-176). New York: Academic Press.

**Rachlin, H., Battalio, R., Kagel, J., & Green, L. (1981).** Maximization theory in behavioral psychology. *Behavioral and Brain Sciences*, 4, 371-388.

**Sutton, R. S., & Barto, A. G. (2018).** *Reinforcement Learning: An Introduction* (2nd ed.). Cambridge, MA: MIT Press.

### Lecturas Avanzadas

**Staddon, J. E. R. (1979).** Operant behavior as adaptation to constraint. *Journal of Experimental Psychology: General*, 108, 48-67.

**Daw, N. D. (2013).** Advanced reinforcement learning. En P. W. Glimcher & E. Fehr (Eds.), *Neuroeconomics* (2nd ed., pp. 299-320). London: Academic Press.

**Luce, R. D. (1959).** *Individual Choice Behavior.* New York: Wiley.

### Experimentos Críticos

**Herrnstein, R. J., & Heyman, G. M. (1979).** Is matching compatible with reinforcement maximization on concurrent variable-interval, variable-ratio? *JEAB*, 31, 209-223.

**Belke, T. W. (1992).** Stimulus preference and the transitivity of preference. *Animal Learning & Behavior*, 20, 401-406.

### Neurociencia

**Schultz, W., Dayan, P., & Montague, P. R. (1997).** A neural substrate of prediction and reward. *Science*, 275, 1593-1599.

**Daw, N. D., O'Doherty, J. P., Dayan, P., Seymour, B., & Dolan, R. J. (2006).** Cortical substrates for exploratory decisions in humans. *Nature*, 441, 876-879.

### Modelos Alternativos

**Baum, W. M. (2025).** Molar versus molecular analyses of choice. *Perspectives on Behavior Science*, 48, 1-18.

**Killeen, P. R. (2023).** A model of activation in operant conditioning. *JEAB*, 120, 123-145.

### Aplicaciones

**Green, L., & Myerson, J. (2004).** A discounting framework for choice with delayed and probabilistic rewards. *Psychological Bulletin*, 130, 769-792.

**Stephens, D. W., & Krebs, J. R. (1986).** *Foraging Theory.* Princeton, NJ: Princeton University Press.

---

**FIN DEL CAPÍTULO X+1**
