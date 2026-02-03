# # Capítulo 7: Modelos de Aprendizaje por Refuerzo
## De la Intuición a la Ecuación

## Objetivos del Capítulo

Al finalizar este capítulo, deberás ser capaz de:

1. Comprender cómo los modelos de refuerzo formalizan la Ley del Efecto de Thorndike
2. Explicar qué son las curvas de aprendizaje y sus limitaciones como evidencia
3. Entender los modelos de refuerzo como sistemas dinámicos discretos
4. Interpretar la ecuación de Bush-Mosteller de tres formas complementarias: carga-descarga, reducción de error, y filtro exponencial
5. Explicar el papel del parámetro de aprendizaje α y sus implicaciones adaptativas
6. Conectar estos modelos formales con los hallazgos empíricos sobre contingencia de los capítulos anteriores

---

## Introducción: El Reto de Formalizar el Aprendizaje

Como resultado de la selección natural, los agentes biológicos son sistemas con mecanismos que les permiten **detectar, predecir y controlar** los sucesos biológicamente importantes (SBIs). Recordemos que los SBIs son sucesos con valor hedónico—también conocidos como reforzadores—que incrementan el éxito reproductivo diferencial de los organismos. Para ejecutar estas funciones de detección, predicción y control, los organismos necesitan hacer contacto con la **estructura causal del entorno**: estructura a la cual designamos bajo el término de *propiedades estadísticas del entorno*.

### Dos Caras de la Estructura Estadística

La estructura estadística relevante para el aprendizaje tiene dos componentes fundamentales:

**1. Relaciones E→SBI (Estímulos predicen reforzadores)**:
Estímulos que se despliegan en el tiempo y en el espacio, algunos seguidos de reforzadores, otros no. Hay tiempos sin nubes y otros con nubes; estos últimos pueden ser seguidos o no de lluvia. La tarea para el organismo es determinar si existe una relación causal entre las nubes y la lluvia.

**2. Relaciones R→SBI (Respuestas controlan reforzadores)**:
Con relación al despliegue de respuestas de los organismos, algunas ocasiones estas respuestas van seguidas de un reforzador y en otras ocasiones no. Hay veces en las que ustedes le dicen "hola" a una persona y otras en las que no. Después del "hola" pueden recibir, o no, otro "hola" de regreso.

Los protocolos de condicionamiento clásico e instrumental definen, como primera aproximación, las estructuras causales más simples que se estudiaron en buena parte del siglo XX.

### El Camino Recorrido

En los capítulos anteriores vimos:

**Capítulo 8 (Asignación de Crédito para Estímulos)**: La contigüidad no es ni necesaria ni suficiente. La contingencia—P(SBI|E) vs. P(SBI|no-E)—es lo crucial. Fenómenos como bloqueo y ensombrecimiento revelan competencia entre estímulos.

**Capítulo 9 (Asignación de Crédito para Respuestas)**: La contigüidad tampoco es necesaria ni suficiente para respuestas. Demoras de 30+ segundos no impiden aprendizaje. Los organismos son sensibles a P(SBI|R) vs. P(SBI|no-R) y pueden discriminar activamente si eventos son causados por ellos.

### El Desafío: De lo Empírico a lo Formal

La evidencia empírica nos dice **qué** aprenden los organismos (relaciones causales estadísticas, no meras contigüidades). Pero falta especificar **cómo** lo hacen. Necesitamos:

1. Un **algoritmo** que especifique paso a paso cómo se actualiza el conocimiento
2. Una **función** que transforme experiencia en valor predictivo/causal
3. Un **modelo** que genere predicciones cuantitativas testables

Para dar cuenta de los resultados empíricos, en la segunda mitad del siglo XX se consolidó un modelo matemático conocido como **Aprendizaje por Refuerzo**, junto con varias modificaciones del mismo. El propósito de este capítulo es presentar estos modelos y su desarrollo como respuesta a la evidencia sobre el papel de la contigüidad.

---

## Parte I: Curvas de Aprendizaje

### El Fenómeno: Cambio Gradual en la Ejecución

El aprendizaje es un **proceso dinámico** que describe los cambios en el comportamiento como una función de la experiencia de los organismos. Desde finales del siglo XIX (estudios sobre memoria de Ebbinghaus) se han obtenido "curvas de aprendizaje" que describen cambios en alguna medida de ejecución de los organismos como una función de las ocasiones en las que los estímulos que encaran o las respuestas que despliegan van seguidos de un reforzador.

**Características de las curvas de aprendizaje**:
- **Eje X (abscisa)**: Ensayos o respuestas reforzadas (indicador de experiencia)
- **Eje Y (ordenada)**: Medidas variadas de ejecución (indicadores del aprendizaje)
- **Forma típica**: Curva negativamente acelerada de ganancias decrecientes

### Ejemplo 1: Condicionamiento Clásico con Humanos

**Experimento de Parssey (1948)**: Curva de adquisición y extinción de la frecuencia del reflejo de parpadeo en un protocolo de condicionamiento clásico con humanos.

**Procedimiento**:
- EC: Tono
- EI: Soplo de aire al ojo (diferentes intensidades)
- RC: Parpadeo anticipatorio
- Medida: Número de respuestas anticipatorias por bloque de 5 ensayos

**Figura 7.1 debe mostrar** (basada en Parssey, 1948):
- Eje X: Bloques de 5 ensayos (ensayos reforzados 1-50, luego extinción 1-10)
- Eje Y: Número medio de respuestas anticipatorias
- 4 curvas para diferentes intensidades de soplo: 88, 66, 18, 7.5 lbs per sq. in.
- Mostrar adquisición gradual durante reforzamiento
- Mostrar extinción rápida cuando cesa el reforzamiento
- Patrón: Intensidad mayor del EI → adquisición más rápida y asíntota más alta

**Observación clave**: El impacto de cada ensayo adicional reforzado **disminuye** conforme se acumulan ensayos. Los primeros ensayos producen cambios grandes; los ensayos posteriores, cambios pequeños.

### Ejemplo 2: Condicionamiento Instrumental con Ratas

**Experimento de Ramond (1954)**: Curva de adquisición de la velocidad reciproca de latencia (1/latencia) de presionar una palanca en un protocolo de condicionamiento instrumental con ratas.

**Procedimiento**:
- R: Presionar palanca
- Ref: Comida
- Manipulación: Diferentes niveles de privación (22 horas vs. 4 horas)
- Medida: Velocidad recíproca de latencia (1/tiempo hasta responder)

**Figura 7.2 debe mostrar** (basada en Ramond, 1954):
- Eje X: Bloques de 4 ensayos (1-20)
- Eje Y: Velocidad recíproca de latencia (en segundos)
- 2 curvas: 22 HR. DEPRIVATION vs. 4 HR. DEPRIVATION
- Patrón: Mayor privación → adquisición más rápida y asíntota más alta
- Ambas curvas muestran crecimiento negativamente acelerado

### La Curva Idealizada

**Figura 7.3 debe mostrar**: Curva de adquisición idealizada
- Eje X: Bloques de ensayos (1-10)
- Eje Y: Fuerza de condicionamiento (unidades arbitrarias, 0-100)
- Forma: Curva suave, negativamente acelerada
- Anotaciones mostrando incrementos decrecientes:
  - Ensayo 1→2: +25 unidades
  - Ensayo 2→3: +20 unidades  
  - Ensayo 3→4: +16 unidades
  - Ensayo 4→5: +12 unidades
  - Etc., hasta asíntota ~90 unidades

Esta curva idealizada captura el patrón general: **ganancias decrecientes**. El impacto de que un reforzador siga a un estímulo/respuesta se va reduciendo conforme se acumulan las ocasiones en las que van seguidos de un reforzador.

### Problema Metodológico Crucial: ¿Gradual o Todo-o-Nada?

**La controversia Gallistel**:

Una alternativa teórica supone que el aprendizaje **no es un proceso gradual**, sino uno de **cambio abrupto** (todo-o-nada). Si este fuese el caso, las curvas de adquisición de crecimiento gradual decreciente podrían ser un **artefacto estadístico** de promediar la ejecución de animales con cambios discretos en el aprendizaje.

**El argumento**:

Considere el caso de un grupo de 8 animales cuya ejecución es promediada:
- Animal 1: Empieza a responder en ensayo 10
- Animal 2: Empieza a responder en ensayo 20
- Animal 3: Empieza a responder en ensayo 30
- Animal 4: Empieza a responder en ensayo 40
- Animal 5: Empieza a responder en ensayo 50
- Animal 6: Empieza a responder en ensayo 60
- Animal 7: Empieza a responder en ensayo 70
- Animal 8: Empieza a responder en ensayo 80

Al **promediar** estos datos, la curva de aprendizaje aparecerá como una curva continua y gradual, ¡aunque ningún animal individual muestre aprendizaje gradual!

**Figura 7.4 debe mostrar**:
- Panel A: Datos individuales de 8 animales (líneas escalonadas, cada una saltando de 0 a 1 en diferentes ensayos)
- Panel B: Promedio de los 8 animales (curva suave y gradual)
- Demostrar visualmente cómo el promedio crea la ilusión de gradualidad

**Implicaciones metodológicas**:

Por esta razón, **Skinner, Estes, Spence** y más recientemente **Gallistel** argumentan en favor de:
1. Analizar datos de **sujetos individuales**, no promedios de grupo
2. Usar **registros acumulativos** que preserven la microestructura temporal
3. Buscar evidencia de cambios discretos vs. continuos

**Nota para este curso**: Los modelos que presentaremos a continuación asumen aprendizaje gradual. Resultan válidos cuando:
- Los datos analizados provienen de sujetos individuales, O
- El aprendizaje genuinamente es gradual (no un artefacto de promediación)

Esta controversia sigue sin resolverse completamente y representa un área activa de investigación. Por ahora, trabajaremos con modelos graduales, teniendo en mente esta limitación.

---

## Parte II: Sistemas Dinámicos Discretos

### ¿Qué es un Sistema Dinámico?

El estudio del aprendizaje—la asignación de crédito—es una instancia de un **sistema dinámico**: un sistema cuyo valor cambia a lo largo del tiempo como una función de sus valores anteriores y de si ha encontrado o no refuerzos.

**Ejemplos cotidianos de sistemas dinámicos**:

Cuando el tiempo es discreto (días, ensayos, eventos), encontramos muchos sistemas similares al aprendizaje:

1. **Crecimiento económico**: Economía de mañana = f(economía de hoy, inversiones, shocks)
2. **Genética de poblaciones**: Frecuencia génica generación n+1 = f(frecuencia generación n, selección, mutación)
3. **Propagación de rumores**: Personas que conocen rumor mañana = f(personas hoy, tasa de contacto)
4. **Epidemias**: Casos de COVID día n+1 = f(casos día n, tasa de contagio, medidas de control)

En todos estos sistemas nos interesa:
- **Trayectoria**: ¿Cómo evoluciona el sistema momento a momento?
- **Equilibrio**: ¿Tiene un punto estable? ¿Hacia dónde converge?
- **Parámetros**: ¿Qué factores determinan velocidad de cambio y punto final?

### Ecuaciones en Diferencias

Para casos donde el tiempo es discreto (ensayos, días), los sistemas dinámicos pueden modelarse con **ecuaciones en diferencias**:

**Definición**: Ecuaciones recursivas que se aplican en cada momento del tiempo discreto *t*.

**Ejemplo 1: Crecimiento Epidémico Simple**

Supongamos que queremos modelar el crecimiento de casos de una epidemia (ej. COVID-19).

**Variables**:
- Y_t = número de casos en el día t
- Y_{t-1} = número de casos en el día anterior
- a = número promedio de personas que contagia cada infectado (ej. a = 2)

**Ecuación en diferencias**:

Y_t = a × Y_{t-1}

**Ejemplo numérico** con a = 2, Y_0 = 1:
- Día 0: Y_0 = 1
- Día 1: Y_1 = 2 × 1 = 2
- Día 2: Y_2 = 2 × 2 = 4
- Día 3: Y_3 = 2 × 4 = 8
- Día 4: Y_4 = 2 × 8 = 16
- ...
- Día t: Y_t = 2^t

**Patrón**: Crecimiento exponencial. Cada día duplica el número de casos.

**Figura 7.5 debe mostrar**:
- Eje X: Días (0-10)
- Eje Y: Número de casos (escala log)
- Curva exponencial creciente
- Anotaciones mostrando Y_0=1, Y_1=2, Y_2=4, Y_3=8, etc.

**Solución general**: Para esta ecuación simple, existe una solución cerrada:

Y_t = a^t × Y_0

Esta fórmula nos dice cuántos casos habrá en **cualquier** día t sin necesidad de iterar.

**Características de ecuaciones en diferencias**:
1. **Recursivas**: Output de hoy es input de mañana
2. **Iterativas**: Se aplican repetidamente, paso a paso
3. **Dependen de historia**: Estado actual depende de estado previo
4. **Parámetros determinan dinámica**: El valor de 'a' determina si crece, decrece, o se estabiliza

### De Epidemias a Aprendizaje

El aprendizaje funciona de manera análoga:

**En epidemias**: 
- Casos_mañana = f(Casos_hoy, Tasa de contagio)

**En aprendizaje**:
- Valor_próximo ensayo = f(Valor_ensayo actual, Ocurrió reforzador?)

La estructura matemática es la misma. Ahora veremos cómo especificar exactamente esa función f().

---

## Parte III: El Modelo de Bush-Mosteller (1951)

### Elementos Comunes a Modelos de Refuerzo

Todos los modelos de refuerzo comparten una estructura básica:

**1. Asignación de valor numérico**:
A cada estímulo y/o respuesta se le asigna un número—una magnitud que representa la disposición a emitirla, "cuánto se ha aprendido acerca de él".

**Evolución terminológica**:
- Thorndike: "Fuerza de conexión estímulo-respuesta"
- Hull: "Fuerza del hábito" (sHr)
- Spence: "Fuerza asociativa"
- Rescorla-Wagner: "Valor asociativo V"
- Aprendizaje por refuerzo moderno: "Valor Q" (para respuestas) o "Valor V" (para estados)

**Nuestra notación**:
- V = valor predictivo de un estímulo
- Q = valor de una respuesta
- Ambos reflejan **cuánto predice/controla** ese elemento la ocurrencia de reforzadores

**2. Actualización basada en experiencia**:
El algoritmo de refuerzo asume que después de cada presentación de un estímulo o emisión de una respuesta, la magnitud V o Q se actualiza como una función de si va seguida o no de un reforzador.

**3. Basado en ensayos**:
Crucial: La actualización solo ocurre cuando el estímulo/respuesta está presente. El valor predictivo de un tono solo se actualiza cuando el tono se presenta, no en su ausencia. Esto implica que el mero paso del tiempo sin el tono, o la presentación de otros estímulos, **no alteran** el valor del tono.

**4. Competencia por valor**:
Las diferentes respuestas/estímulos compiten por el tiempo/atención disponible. Aquellos con mayor V/Q tienen mayor probabilidad de ser seleccionados.

**5. Sistema de retroalimentación**:
El modelo es una instancia de un sistema de retroalimentación:
- Valor alto → Mayor respuesta → Más reforzadores → Incrementa valor (ciclo positivo)
- Valor bajo → Menor respuesta → Menos reforzadores → Permanece bajo (ciclo negativo)

### La Ecuación Fundamental de Bush-Mosteller

En 1951, **Robert Bush y Frederick Mosteller** propusieron una versión matemática del modelo de aprendizaje por refuerzo que sigue siendo la base de modelos más recientes, tanto en psicología como en aprendizaje de máquinas (machine learning) y neurociencia computacional.

**Escenario de aplicación**: Protocolo de condicionamiento clásico

**Variables**:
- V_t = valor predictivo del estímulo en el ensayo t
- V_{t+1} = valor actualizado en el siguiente ensayo t+1
- R_t = reforzador (1 si se presenta, 0 si no)
- α = parámetro de aprendizaje (0 < α < 1)

**Supuesto clave**: V_{t+1} depende solo de dos factores:
1. Valor acumulado hasta el ensayo anterior (V_t)
2. Si ocurrió o no un reforzador en el ensayo actual (R_t)

**Forma más simple** (suma ponderada):

V_{t+1} = (1-α) V_t + α R_t

Esta ecuación dice:
- El nuevo valor es una **combinación ponderada** de:
  - (1-α) × experiencia pasada acumulada (V_t)
  - α × experiencia presente (R_t)

**Interpretación del parámetro α**:
- α cercano a 0: La experiencia pasada domina → Aprendizaje lento
- α cercano a 1: La experiencia presente domina → Aprendizaje rápido
- α = 0.5: Pasado y presente tienen igual peso

**Propiedad importante**: Esta es una **ecuación recurrente**:
- En cada iteración hay siempre un V_viejo (del ensayo anterior) y un V_nuevo (del ensayo actual)
- El V_nuevo del ensayo actual se convierte en el V_viejo del siguiente ensayo
- Esta recursión captura la acumulación de experiencia a través del tiempo

---

## Parte IV: Tres Interpretaciones del Modelo

La estructura matemática de los modelos de refuerzo admite diferentes interpretaciones teóricas. Consideraremos tres perspectivas complementarias:

### Interpretación 1: Proceso de Carga-Descarga (Integrador con Fuga)

**Metáfora**: Una batería que se carga y descarga

La forma más literal de interpretar el modelo es como un proceso donde:
- Cada reforzador **incrementa** (carga, fortalece) el valor V
- Cada ocurrencia sin reforzador **decrementa** (descarga, debilita) el valor V

**Analogía cotidiana: La batería del celular**

Para que su celular funcione, tienen que conectarlo a una toma de corriente. Mientras está conectado, la carga de la batería se va actualizando hasta llegar a un punto máximo. Al usarlo sin tenerlo conectado, la batería se va descargando como función del uso sin carga adicional.

**En el modelo**:
- V_t es como el nivel de carga actual
- R_t = 1 es como conectar el cargador (incrementa V)
- R_t = 0 es como usar el celular desconectado (decrementa V)
- α determina qué tan rápido carga/descarga

**Visualización del proceso**:

**Figura 7.6 debe mostrar** (Respuesta a un solo reforzador):
- Panel superior: Input (pulso de reforzador en t=0)
- Panel inferior: Output (V_t a lo largo del tiempo)
- Mostrar: Incremento súbito en t=0, luego decaimiento exponencial
- Parámetros: α = 0.3, V_0 = 0, un solo reforzador

**Figura 7.7 debe mostrar** (Respuesta a tres reforzadores):
- Panel superior: Input (tres pulsos en t=0, 0.1, 0.2)
- Panel inferior: Output (V_t)
- Mostrar: Incrementos sucesivos, con decaimientos entre pulsos
- Acumulación gradual de valor

**Dinámica de carga**:

Cuando R = 1 (reforzador presente):
V_{t+1} = (1-α)V_t + α(1)
V_{t+1} = V_t + α(1 - V_t)

Interpretación: V aumenta en una fracción α de la **distancia que falta** hasta el máximo (1).

**Dinámica de descarga**:

Cuando R = 0 (no reforzador):
V_{t+1} = (1-α)V_t + α(0)
V_{t+1} = (1-α)V_t

Interpretación: V decrece proporcionalmente a su valor actual, multiplicado por (1-α).

**Ejemplo numérico de carga**:

Supongamos α = 0.5, R = 1 (reforzador constante), V_0 = 0

Iterando:
- V_0 = 0
- V_1 = 0.5 × 0 + 0.5 × 1 = 0.5
- V_2 = 0.5 × 0.5 + 0.5 × 1 = 0.75
- V_3 = 0.5 × 0.75 + 0.5 × 1 = 0.875
- V_4 = 0.5 × 0.875 + 0.5 × 1 = 0.9375
- ...
- V_∞ → 1.0

**Figura 7.8 debe mostrar** (α = 0.5):
- Eje X: Ensayo (0-30)
- Eje Y: Valor V (0-1)
- Curva de adquisición alcanzando asíntota ~1.0
- Anotaciones mostrando valores intermedios

**Ejemplo numérico de descarga**:

Ahora con α = 0.2, R = 1 (reforzador constante), V_0 = 0

Iterando:
- V_0 = 0
- V_1 = 0.8 × 0 + 0.2 × 1 = 0.2
- V_2 = 0.8 × 0.2 + 0.2 × 1 = 0.36
- V_3 = 0.8 × 0.36 + 0.2 × 1 = 0.488
- V_4 = 0.8 × 0.488 + 0.2 × 1 = 0.5904
- ...

**Figura 7.9 debe mostrar** (α = 0.2):
- Eje X: Ensayo (0-30)
- Eje Y: Valor V (0-1)
- Curva de adquisición más lenta que con α = 0.5
- Comparación visual con curva α = 0.5 superpuesta

**Comparación de velocidades de aprendizaje**:

**Figura 7.10 debe mostrar**:
- Múltiples curvas con diferentes α: 0.1, 0.3, 0.5, 0.7, 0.9
- Todas convergen a V = 1.0 pero a diferentes velocidades
- α mayor → convergencia más rápida

**Extinción**:

Note que si la respuesta no es reforzada (R = 0), la ecuación se reduce a:

V_{t+1} = (1-α)V_t

El valor decrece exponencialmente hacia cero.

**Figura 7.11 debe mostrar**:
- Eje X: Ensayos de extinción (0-50)
- Eje Y: Valor V (iniciando en 1.0)
- Curva de decaimiento exponencial
- Con α = 0.2, mostrar extinción más lenta que con α = 0.5

**Observación importante**: Durante el tiempo sin presentación del estímulo, el sistema **no se actualiza**. Solo hay cambios en los momentos en los que se presenta el estímulo/respuesta. Por eso le llamamos modelo "basado en ensayos".

### Interpretación 2: Reducción del Error de Predicción

El reacomodo de los términos de la ecuación de carga-descarga permite una interpretación alternativa, hoy dominante en psicología del aprendizaje y neurociencias.

**Manipulación algebraica**:

Partiendo de:
V_{t+1} = (1-α)V_t + αR_t

Expandiendo:
V_{t+1} = V_t - αV_t + αR_t

Factorizando:
V_{t+1} = V_t + α(R_t - V_t)

**Nueva perspectiva**: El cambio en V es proporcional a la **discrepancia** entre:
- R_t = lo que se obtiene (realidad)
- V_t = lo que se esperaba obtener (predicción)

**Definición formal**: **Error de Predicción (δ)**

δ_t = R_t - V_t

- Si δ > 0: Sorpresa positiva (reforzador inesperado) → Incrementa V
- Si δ = 0: Predicción perfecta → No hay cambio en V
- Si δ < 0: Sorpresa negativa (reforzador esperado no llega) → Decrementa V

**Ecuación en términos de δ**:

V_{t+1} = V_t + α δ_t

O enfatizando el cambio:

ΔV_t = V_{t+1} - V_t = α δ_t

**Interpretación**: El aprendizaje es proporcional al error de predicción.

En la literatura contemporánea, esta se conoce como la **Regla Delta**.

**¿Por qué es importante esta perspectiva?**

1. **Eficiencia computacional**: Solo aprendemos cuando nos equivocamos. Predicciones perfectas no requieren cambio.

2. **Conexión con neurociencia**: Las neuronas dopaminérgicas codifican exactamente este error de predicción δ (Schultz, Dayan, & Montague, 1997).

3. **Ascenso de colina**: El sistema se mueve en la dirección que reduce error hasta alcanzar predicción perfecta.

4. **Generalidad**: Esta formulación aplica igual a estímulos (condicionamiento clásico) y respuestas (condicionamiento instrumental).

**Ejemplo de dinámica del error**:

Considere α = 0.3, reforzamiento constante (R = 1), V_0 = 0

| Ensayo | V_t | R_t | δ_t = R - V | ΔV = α·δ | V_{t+1} |
|--------|-----|-----|-------------|----------|---------|
| 0 | 0.000 | 1 | 1.000 | 0.300 | 0.300 |
| 1 | 0.300 | 1 | 0.700 | 0.210 | 0.510 |
| 2 | 0.510 | 1 | 0.490 | 0.147 | 0.657 |
| 3 | 0.657 | 1 | 0.343 | 0.103 | 0.760 |
| 4 | 0.760 | 1 | 0.240 | 0.072 | 0.832 |
| ... | ... | ... | ... | ... | ... |

**Patrón observable**:
- Error de predicción δ **disminuye** ensayo a ensayo
- Cambio en V (ΔV) también **disminuye**
- Sistema converge a V = 1, donde δ = 0 (predicción perfecta)

**Figura 7.12 debe mostrar**:
- Dos paneles apilados verticalmente
- Panel superior: V_t a través de ensayos (curva creciente hacia 1)
- Panel inferior: δ_t a través de ensayos (curva decreciente hacia 0)
- Mostrar visualmente que conforme V sube, δ baja

**Conexión con fenómenos empíricos**:

Esta interpretación explica naturalmente:
1. **Curvas de adquisición negativamente aceleradas**: Conforme V aumenta, δ disminuye → cambios más pequeños
2. **Bloqueo** (veremos en cap. Rescorla-Wagner): Si otro estímulo ya predice perfectamente (δ=0), no hay aprendizaje adicional
3. **Extinción**: R = 0 pero V > 0 → δ negativo → V decrece

**Historia**: La ecuación fue propuesta por Bush y Mosteller (1951) y es el antecedente directo del modelo de Rescorla y Wagner (1972) que veremos en el próximo capítulo.

### Interpretación 3: Filtro Exponencial (Media Corrida Ponderada)

Existe una tercera forma de entender el modelo que conecta con teoría de señales y procesamiento de información.

**Problema computacional**: ¿Cómo estimar el valor "verdadero" de un estímulo/respuesta cuando la experiencia es ruidosa?

**Solución ingenua: Media aritmética**

La forma más obvia de estimar el valor de una respuesta sería computar la **media** de todos los reforzadores obtenidos:

V_t = (R_1 + R_2 + ... + R_t) / t

**Problemas**:
1. **Complejidad computacional**: Requiere mantener en memoria **todos** los valores R_1, R_2, ..., R_t
2. **Inflexibilidad**: Trata todos los reforzadores por igual, sin importar cuán antiguos sean
3. **Inadaptabilidad**: No puede adaptarse a entornos cambiantes

**Solución elegante: Media exponencial corrida**

Los modelos de refuerzo resuelven estos problemas mediante un **filtro exponencial** que:
- Solo requiere recordar el valor V anterior (no toda la historia)
- Pondera más los eventos recientes que los antiguos
- Puede adaptarse a cambios en las contingencias

**Desarrollo matemático**:

Partiendo de la ecuación Bush-Mosteller:
V_{t+1} = (1-α)V_t + αR_t

Podemos expandir recursivamente:
V_{t+1} = αR_t + (1-α)V_t
V_{t+1} = αR_t + (1-α)[αR_{t-1} + (1-α)V_{t-1}]
V_{t+1} = αR_t + α(1-α)R_{t-1} + (1-α)²V_{t-1}

Continuando la expansión:
V_{t+1} = αR_t + α(1-α)R_{t-1} + α(1-α)²R_{t-2} + α(1-α)³R_{t-3} + ...

**Insight clave**: V_t es un **promedio ponderado** de todos los reforzadores pasados, donde el peso asignado a cada reforzador decrece exponencialmente con su antigüedad.

**Pesos asignados a cada reforzador**:
- Reforzador más reciente (R_t): peso = α
- Un ensayo atrás (R_{t-1}): peso = α(1-α)
- Dos ensayos atrás (R_{t-2}): peso = α(1-α)²
- Tres ensayos atrás (R_{t-3}): peso = α(1-α)³
- ...

**Decaimiento exponencial de pesos**:

**Tabla ejemplo** (α = 0.3):

| Antigüedad | Peso |
|------------|------|
| R_t (ahora) | 0.300 |
| R_{t-1} (1 atrás) | 0.210 |
| R_{t-2} (2 atrás) | 0.147 |
| R_{t-3} (3 atrás) | 0.103 |
| R_{t-4} (4 atrás) | 0.072 |
| R_{t-5} (5 atrás) | 0.050 |
| R_{t-10} (10 atrás) | 0.014 |

**Figura 7.13 debe mostrar**:
- Eje X: Antigüedad (ensayos hacia atrás: 0, 1, 2, 3, ... 20)
- Eje Y: Peso asignado
- Tres curvas: α = 0.1, α = 0.3, α = 0.7
- Mostrar decaimiento exponencial más rápido con α mayor

**Interpretación del parámetro α como "ventana de memoria"**:

- **α grande** (ej. 0.7):
  - Peso fuerte en experiencias recientes
  - Olvida rápido el pasado
  - "Ventana de memoria" corta
  - Bueno para entornos cambiantes

- **α pequeño** (ej. 0.1):
  - Integra sobre muchos eventos pasados
  - Olvida lento
  - "Ventana de memoria" larga
  - Bueno para entornos estables con ruido

**Ventaja computacional**: Solo necesitamos recordar V_t (un número), no toda la secuencia R_1, R_2, ..., R_t.

**Conexión con ingeniería**: Esta es exactamente la estructura de filtros exponenciales usados en procesamiento de señales para:
- Suavizar datos ruidosos
- Tracking de objetivos en radar
- Pronósticos en series temporales
- Control de procesos

**Ejemplo concreto: Máquina Tragamonedas**

Imagine una máquina tragamonedas (one-armed bandit) donde cada jugada tiene probabilidad p = 0.3 de ganar.

Secuencia de resultados: 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, ...

**Con α = 0.3**:

| Ensayo | R_t | V_t (antes) | V_{t+1} (después) |
|--------|-----|-------------|-------------------|
| 1 | 0 | 0.000 | 0.000 |
| 2 | 1 | 0.000 | 0.300 |
| 3 | 0 | 0.300 | 0.210 |
| 4 | 0 | 0.210 | 0.147 |
| 5 | 1 | 0.147 | 0.403 |
| 6 | 1 | 0.403 | 0.582 |
| 7 | 0 | 0.582 | 0.407 |
| ... | ... | ... | ... |

Después de muchos ensayos, V converge a ≈ 0.3 (la probabilidad verdadera).

**Figura 7.14 debe mostrar**:
- Simulación de 200 ensayos con p = 0.3
- Mostrar R_t como barras (0 o 1)
- Superponer V_t como línea suave
- Mostrar convergencia hacia 0.3

**Propiedad importante**: El filtro exponencial converge al **valor esperado verdadero** E[R] en entornos estacionarios.

**Resumen de las tres interpretaciones**:

| Interpretación | Enfoque | Insight Clave |
|----------------|---------|---------------|
| **Carga-Descarga** | Mecánico | Reforzadores cargan, ausencias descargan |
| **Error de Predicción** | Computacional | Solo aprendemos de sorpresas |
| **Filtro Exponencial** | Estadístico | Promedio ponderado con olvido |

**Crucial**: Estas tres interpretaciones son **matemáticamente equivalentes**—solo cambia la perspectiva conceptual.

---

## Parte V: El Parámetro de Aprendizaje α

### Papel del Parámetro

El parámetro α (alpha) es central en el modelo y determina múltiples propiedades del aprendizaje.

**Interpretación según cada marco**:

1. **Como tasa de aprendizaje** (carga-descarga):
   - α = fracción del gap que se cierra en cada ensayo
   - α grande → aprendizaje rápido
   - α pequeño → aprendizaje lento

2. **Como ganancia del error** (reducción de error):
   - α = importancia dada a discrepancias
   - α grande → correcciones grandes
   - α pequeño → correcciones conservadoras

3. **Como factor de olvido** (filtro):
   - α = 1 - λ, donde λ es el "factor de memoria"
   - α grande → olvido rápido (memoria corta)
   - α pequeño → olvido lento (memoria larga)

### Velocidad de Convergencia

**Pregunta**: ¿Cuántos ensayos se requieren para alcanzar cierto % del asíntota?

**Solución analítica** (con R = 1 constante, V_0 = 0):

V_t = 1 - (1-α)^t

Para alcanzar 90% del asíntota (V = 0.9):
0.9 = 1 - (1-α)^t
(1-α)^t = 0.1
t = log(0.1) / log(1-α)

**Tabla de ensayos hasta 90% del asíntota**:

| α | Ensayos |
|---|---------|
| 0.1 | 22 |
| 0.2 | 11 |
| 0.3 | 7 |
| 0.5 | 4 |
| 0.7 | 2 |

**Figura 7.15 debe mostrar**:
- Múltiples curvas de adquisición con diferentes α
- Línea horizontal en V = 0.9
- Flechas indicando ensayos hasta alcanzar 0.9 para cada α

### El Dilema Fundamental: Estabilidad vs. Plasticidad

El parámetro α enfrenta un **trade-off** fundamental en entornos variables o ruidosos.

**Escenario 1: Entorno Constante con Ruido**

Máquina tragamonedas con p = 0.3 verdadera (pero resultados son estocásticos: 0, 1, 0, 1, 1, 0, ...)

**Con α grande** (ej. 0.8):
- Responde rápido a cada resultado
- V oscila mucho: después de ganar salta a ~0.8, después de perder cae a ~0.16
- **Problema**: Confunde **ruido** con **señal**
- Estimación ruidosa, alta varianza

**Con α pequeño** (ej. 0.1):
- Integra sobre muchos ensayos
- V se mantiene estable cerca de 0.3
- **Beneficio**: Filtra el ruido efectivamente
- Estimación suave, baja varianza

**Figura 7.16 debe mostrar**:
- Dos paneles para la misma secuencia de R_t
- Panel A: α = 0.8 (curva muy ruidosa oscilando)
- Panel B: α = 0.1 (curva suave convergiendo a 0.3)

**Escenario 2: Entorno Cambiante**

Máquina tragamonedas donde p cambia de 0.3 → 0.7 en el ensayo 100.

**Con α grande** (ej. 0.8):
- Detecta el cambio rápidamente
- V sube de ~0.3 a ~0.7 en pocos ensayos
- **Beneficio**: Adaptación rápida a nuevas contingencias

**Con α pequeño** (ej. 0.1):
- Tarda muchos ensayos en ajustarse
- V sube lentamente de 0.3 hacia 0.7
- **Problema**: Sigue usando información obsoleta del pasado
- Mal adaptado a cambios

**Figura 7.17 debe mostrar**:
- Dos paneles con cambio en p en ensayo 100
- Panel A: α = 0.8 (detecta cambio rápido)
- Panel B: α = 0.1 (detecta cambio lento)
- Línea vertical indicando momento del cambio

**Formalización del trade-off**:

**Con α cercano a 1**:
- ✓ Adaptación rápida a cambios
- ✗ Alta sensibilidad a ruido
- Interpretación: Todo ruido se ve como cambio genuino

**Con α cercano a 0**:
- ✓ Robustez contra ruido
- ✗ Lentitud para detectar cambios reales
- Interpretación: Todo cambio se ve como ruido transitorio

**No hay solución perfecta**: El valor óptimo de α depende de propiedades del entorno:
- ¿Qué tan variable/ruidoso es?
- ¿Qué tan frecuentemente cambian las contingencias?
- ¿Cuál es el costo relativo de error tipo I (falsos positivos) vs. tipo II (falsos negativos)?

### Implicaciones Evolutivas y Adaptativas

**Pregunta profunda**: Si α tiene este trade-off, ¿qué valor debería la evolución haber "seleccionado"?

**Respuesta corta**: Depende del nicho ecológico.

**Ambientes estables**:
- Contingencias cambian raramente
- Ruido es el problema principal
- Selección favorece α **pequeño**
- Ejemplo: Forrajeo en territorio estable con recursos predecibles

**Ambientes volátiles**:
- Contingencias cambian frecuentemente
- Detectar cambios rápido es crítico
- Selección favorece α **grande**
- Ejemplo: Depredador con estrategias cambiantes

**Solución sofisticada: α adaptativo**

En lugar de α fijo, el sistema podría **ajustar α** según detecte:
- Estabilidad detectada → reduce α (integra más)
- Volatilidad detectada → aumenta α (responde rápido)

**Evidencia empírica**: Hay estudios mostrando que humanos y animales ajustan tasas de aprendizaje según volatilidad percibida del entorno (Behrens et al., 2007; Nassar et al., 2010).

**En el capítulo sobre incertidumbre** (más adelante en el curso), revisaremos cómo resolver esta limitación del modelo de refuerzo mediante mecanismos de meta-aprendizaje.

---

## Parte VI: Conexión con Hallazgos Empíricos Previos

### ¿Cómo se Relaciona este Modelo con la Evidencia sobre Contingencia?

Recordemos los hallazgos clave de capítulos anteriores:

**Del Capítulo 8 (Estímulos)**:
- Contigüidad no es necesaria ni suficiente
- P(SBI|E) vs. P(SBI|no-E) determina aprendizaje
- Bloqueo: Competencia entre estímulos

**Del Capítulo 9 (Respuestas)**:
- Contigüidad no es necesaria ni suficiente
- P(SBI|R) vs. P(SBI|no-R) determina aprendizaje
- Organismos perciben causalidad activamente

**Pregunta crítica**: ¿El modelo de Bush-Mosteller captura estos fenómenos?

### Lo que el Modelo SÍ Captura

**1. Curvas de adquisición negativamente aceleradas** ✓

El modelo predice exactamente las curvas que vimos en Parte I:
- Cambios grandes al inicio (cuando V es bajo, δ es grande)
- Cambios pequeños después (cuando V se acerca al asíntota, δ es pequeño)

**2. Extinción** ✓

Cuando R cambia de 1 a 0:
- δ se vuelve negativo
- V decrece gradualmente
- Reproduce curvas de extinción empíricas

**3. Efecto de magnitud del reforzador** ✓

Si permitimos que R tenga valores > 1 (reforzador más grande):
- V alcanza asíntotas más altas
- Reproduce hallazgo de que reforzadores mayores → mayor aprendizaje

**4. Efecto de demora (parcialmente)** ~

Con modificaciones, puede incorporar efectos de demora mediante descuento temporal

### Lo que el Modelo NO Captura (Limitaciones Fundamentales)

**1. Sensibilidad a contingencia (no solo contigüidad)** ✗

El modelo de Bush-Mosteller solo se actualiza cuando el EC/respuesta ocurre seguido de reforzador. Pero los hallazgos empíricos muestran que los organismos son sensibles a:

P(SBI|E) **vs.** P(SBI|no-E)

El modelo no tiene forma de representar P(SBI|no-E) porque solo se actualiza cuando E está presente.

**Ejemplo del problema**:
- Condición A: P(SBI|E) = 0.5, P(SBI|no-E) = 0.0
- Condición B: P(SBI|E) = 0.5, P(SBI|no-E) = 0.5

El modelo predice **mismo aprendizaje** en ambas (porque solo ve P(SBI|E) = 0.5).

Pero empíricamente:
- Condición A: Fuerte aprendizaje (contingencia positiva)
- Condición B: No aprendizaje (contingencia cero)

**2. Bloqueo y competencia entre elementos** ✗

El modelo Bush-Mosteller actualiza cada estímulo independientemente. No hay competencia.

Pero empíricamente (experimento de Kamin):
- Fase 1: A → SBI (hasta asíntota)
- Fase 2: AB → SBI
- Resultado: B no se aprende (bloqueado por A)

El modelo predice que B **sí** debería aprenderse (porque va seguido del SBI).

**3. Ensombrecimiento** ✗

Similar al bloqueo: el modelo no puede capturar cómo estímulos más salientes roban crédito de estímulos menos salientes.

**4. Conducta inducida y variabilidad generada** ✗

El modelo asigna valor a estímulos/respuestas, pero no explica de dónde vienen las respuestas candidatas. No incorpora el mecanismo de generación de variabilidad que vimos en Cap. 9.

### La Solución: Modelo de Rescorla-Wagner (Próximo Capítulo)

Para resolver las limitaciones 1-3, **Rescorla y Wagner (1972)** modificaron el modelo de Bush-Mosteller de una forma crucial:

**Bush-Mosteller**: Cada elemento actualiza independientemente
**Rescorla-Wagner**: Elementos compiten por "crédito predictivo total limitado"

**Modificación clave**:

En lugar de:
ΔV_A = α(R - V_A)

Rescorla-Wagner propone:
ΔV_A = α(R - **ΣV**)

donde ΣV = suma de todos los elementos presentes.

Esta modificación permite capturar bloqueo, ensombrecimiento, y sensibilidad a contingencia.

**Lo veremos en detalle en el Capítulo 8.**

---

## Parte VII: Aplicación del Modelo a Diferentes Escenarios

### Escenario 1: Protocolo de Reforzamiento Parcial

**Situación**: Máquina tragamonedas donde cada jugada tiene probabilidad p de ganar.

**Parámetros**:
- p = 0.4 (probabilidad de reforzador)
- α = 0.3
- V_0 = 0

**Pregunta**: ¿A qué valor converge V?

**Análisis**:

En equilibrio (cuando E[ΔV] = 0):

E[ΔV] = E[α(R - V)]
0 = α E[R - V]
0 = α (E[R] - V)
V* = E[R] = p

**Predicción**: V converge a la **probabilidad de reforzamiento**.

Con p = 0.4, V* = 0.4

**Figura 7.18 debe mostrar**:
- Simulación de 200 ensayos
- Secuencia estocástica de R_t (0s y 1s con p = 0.4)
- V_t convergiendo a 0.4
- Línea horizontal en V = 0.4 mostrando asíntota teórica

**Generalización**: En reforzamiento parcial, V estima la probabilidad de reforzador.

### Escenario 2: Adquisición y Extinción

**Fase 1 - Adquisición** (50 ensayos, R = 1):
- V aumenta de 0 hacia 1
- Velocidad depende de α

**Fase 2 - Extinción** (50 ensayos, R = 0):
- V decrece de ~1 hacia 0
- Velocidad depende de α

**Figura 7.19 debe mostrar**:
- Dos fases claramente marcadas
- Panel A: Adquisición y extinción con α = 0.3
- Panel B: Adquisición y extinción con α = 0.1
- Mostrar que α más grande → adquisición y extinción más rápidas

**Observación interesante**: Con el mismo α, la adquisición y extinción tienen **tasas similares** (propiedad del modelo exponencial).

### Escenario 3: Reversión de Contingencia

**Protocolo**:
- Ensayos 1-100: E₁ → SBI, E₂ → nada
- Ensayos 101-200: E₁ → nada, E₂ → SBI (reversión)

**Predicciones del modelo**:
- V₁ aumenta en fase 1, luego decrece en fase 2
- V₂ permanece bajo en fase 1, luego aumenta en fase 2

**Figura 7.20 debe mostrar**:
- Dos líneas (V₁ y V₂) cruzándose en ensayo 100
- Línea vertical marcando momento de reversión
- V₁: sube luego baja
- V₂: bajo luego sube

**Aplicación**: Este escenario modela situaciones ecológicas donde contingencias cambian (ej. nuevo depredador, recurso agotado).

### Escenario 4: Diferente Tasa de Aprendizaje por Elemento

**Realidad biológica**: No todos los estímulos se aprenden a la misma velocidad.

**Modificación**:
- Estímulo saliente (luz brillante): α₁ = 0.5
- Estímulo tenue (luz débil): α₂ = 0.1

**Predicción**: Ambos convergen al mismo asíntota, pero a diferentes velocidades.

**Figura 7.21 debe mostrar**:
- Dos curvas de adquisición
- Estímulo saliente: Curva empinada
- Estímulo tenue: Curva gradual
- Ambas convergen a V = 1

**Relevancia**: Captura fenómeno de **relevancia biológica** discutido en Cap. 8.

---

## Parte VIII: Extensiones y Generalizaciones

### Modelo General para Elección

Hasta ahora hemos visto cómo se actualiza V. Pero en condicionamiento instrumental, necesitamos especificar cómo V se traduce en **elección de respuesta**.

**Situación**: Múltiples respuestas disponibles (R₁, R₂, ..., Rₙ), cada una con valor Q₁, Q₂, ..., Qₙ.

**Pregunta**: ¿Cuál respuesta ejecutar?

**Regla de elección más simple: Determinista**

P(Rᵢ) = 1 si Qᵢ = max(Q₁, Q₂, ..., Qₙ)
P(Rᵢ) = 0 en otro caso

**Problema**: No permite exploración. Respuesta sub-óptima nunca se actualiza.

**Regla de elección probabilística: Softmax**

P(Rᵢ) = exp(βQᵢ) / Σⱼ exp(βQⱼ)

donde β es "temperatura inversa" que controla grado de explotación vs. exploración.

**β grande**: Explotación (casi determinista)
**β pequeño**: Exploración (casi aleatorio)

**Nota**: Este tema se desarrolla extensivamente en Capítulos 10-11 sobre modelos de elección.

### Del Modelo de Bush-Mosteller a Q-Learning

En inteligencia artificial y neurociencia computacional, una extensión importante del modelo de Bush-Mosteller es **Q-Learning** (Watkins, 1989).

**Diferencia clave**: En entornos secuenciales, las acciones tienen consecuencias **inmediatas** y **futuras**.

**Modificación**:

En lugar de:
Q_{t+1} = Q_t + α(R_t - Q_t)

Q-Learning usa:
Q_{t+1} = Q_t + α(R_t + γ max(Q_{future}) - Q_t)

donde γ es factor de descuento y max(Q_{future}) es valor del mejor estado siguiente.

**Implicación**: El sistema aprende a maximizar **retorno acumulado futuro**, no solo reforzador inmediato.

**Nota**: Esto se verá en cursos avanzados (ACA II) y es el fundamento de Deep Reinforcement Learning moderno (AlphaGo, etc.).

---

## Conclusiones

### Logros del Modelo de Bush-Mosteller

1. **Formaliza la Ley del Efecto**: Especifica matemáticamente cómo reforzadores afectan aprendizaje

2. **Predice curvas de aprendizaje**: Captura forma negat

ivamente acelerada observada empíricamente

3. **Tres interpretaciones coherentes**: Carga-descarga, error de predicción, filtro exponencial

4. **Eficiencia computacional**: Solo requiere memoria de V actual, no toda la historia

5. **Aplicabilidad general**: Sirve para estímulos (condicionamiento clásico) y respuestas (instrumental)

6. **Fundamento de modelos modernos**: Base de Rescorla-Wagner, TD-learning, Q-learning

### Limitaciones Reconocidas

1. **No captura sensibilidad a contingencia completa**: Solo P(SBI|E), no P(SBI|no-E)

2. **No modela competencia entre elementos**: Bloqueo, ensombrecimiento requieren modificaciones

3. **α fijo problemático**: Trade-off entre estabilidad y plasticidad sin solución

4. **No explica origen de variabilidad**: Asume respuestas ya existen

5. **Basado en ensayos**: No captura dinámica temporal continua

**Estos problemas motivan extensiones que veremos en próximos capítulos.**

### Transición al Siguiente Capítulo

El modelo de Bush-Mosteller fue revolucionario, pero la evidencia empírica sobre bloqueo (Kamin, 1968) y contingencia (Rescorla, 1968) reveló la necesidad de modificaciones fundamentales.

**En el Capítulo 8**, veremos cómo **Rescorla y Wagner (1972)** modificaron el modelo para que elementos compitan por crédito limitado, resolviendo así las limitaciones 1 y 2.

La modificación es sutil pero profunda:

**Bush-Mosteller**: ΔV = α(R - V)
**Rescorla-Wagner**: ΔV = α(R - ΣV)

Esa simple Σ cambia todo.

---

## Ejercicios

### Ejercicios Conceptuales

**1. Interpretaciones del Modelo**

Explica en tus propias palabras las tres interpretaciones del modelo de Bush-Mosteller. Para cada interpretación, da un ejemplo cotidiano que la ilustre (diferente a los del capítulo).

**2. Gradual vs. Todo-o-Nada**

a) Explica el argumento de Gallistel sobre curvas de aprendizaje como artefactos.
b) ¿Qué tipo de evidencia empírica podría distinguir entre aprendizaje gradual vs. abrupto?
c) ¿Tiene sentido evolutivo que el aprendizaje sea gradual? Argumenta a favor y en contra.

**3. El Parámetro α**

Un estudiante dice: "α grande siempre es mejor porque aprendes más rápido". 

a) ¿Por qué esta afirmación es incorrecta?
b) Describe dos escenarios ecológicos donde α grande sería adaptativo y dos donde α pequeño sería mejor.
c) ¿Cómo podría un organismo "saber" qué valor de α usar?

**4. Limitaciones del Modelo**

a) ¿Por qué el modelo de Bush-Mosteller no puede explicar el bloqueo de Kamin?
b) ¿Qué modificación fundamental se requiere para capturar competencia entre estímulos?
c) ¿Esta limitación es un "bug" o un "feature" del modelo? Argumenta.

### Ejercicios Cuantitativos

**5. Iteración Manual**

Dado α = 0.4, V₀ = 0, y secuencia de reforzadores: 1, 1, 0, 1, 0, 0, 1

a) Calcula V₁, V₂, V₃, V₄, V₅, V₆, V₇ manualmente
b) Grafica V_t vs. ensayo
c) ¿Hacia qué valor parece converger?

**6. Análisis de Convergencia**

a) Demuestra algebraicamente que con R = 1 constante y V₀ = 0, la solución es: V_t = 1 - (1-α)^t
b) Usando esta fórmula, calcula cuántos ensayos se requieren para alcanzar V = 0.95 con α = 0.2
c) Repite para α = 0.5 y α = 0.8

**7. Reforzamiento Parcial**

Una máquina tragamonedas paga con probabilidad p = 0.25.

a) ¿A qué valor converge V en equilibrio?
b) Con α = 0.3, simula 100 ensayos (puedes usar Excel, Python, o R)
c) ¿Cuántos ensayos se requieren aproximadamente para estar dentro de ±0.05 del valor de equilibrio?

**8. Extinción**

Un estímulo fue reforzado hasta alcanzar V = 0.9, luego comienza extinción (R = 0).

a) Con α = 0.3, calcula los primeros 10 valores durante extinción
b) ¿Cuántos ensayos de extinción se requieren para que V caiga por debajo de 0.1?
c) Compara con α = 0.1. ¿Cuál extingue más rápido?

**9. Pesos en el Filtro Exponencial**

a) Para α = 0.25, calcula los pesos asignados a los últimos 10 reforzadores
b) ¿Qué fracción del peso total se acumula en los últimos 5 reforzadores?
c) ¿Cómo cambia esta fracción si α = 0.5?

**10. Efecto de Magnitud**

Considera dos reforzadores de diferente magnitud: R_pequeño = 0.5, R_grande = 1.0

a) Si ambos se presentan con igual frecuencia alternando, ¿a qué valor converge V?
b) Con α = 0.4, simula 20 ensayos alternando magnitudes
c) ¿Cómo afecta α la velocidad de convergencia?

### Ejercicios de Programación

**11. Simulador Básico**

Implementa el modelo de Bush-Mosteller en tu lenguaje preferido (Python, R, MATLAB, etc.).

a) Función que tome α, secuencia de R, y V₀, y devuelva trayectoria completa de V
b) Grafica adquisición con R = 1 constante para α = 0.1, 0.3, 0.5, 0.7, 0.9
c) Añade extinción después de 30 ensayos de adquisición

**12. Reforzamiento Parcial Estocástico**

a) Simula 200 ensayos con p = 0.3, α = 0.4
b) Grafica R_t (como barras) y V_t (como línea)
c) Repite 10 veces y grafica todas las trayectorias. ¿Qué observas?
d) Calcula media y varianza de V en últimos 50 ensayos

**13. Comparación de Parámetros**

Crea una grid de simulaciones:
- α = [0.1, 0.2, ..., 0.9]
- p = [0.2, 0.4, 0.6, 0.8]

Para cada combinación:
a) Simula 200 ensayos
b) Calcula ensayos hasta convergencia (V dentro de ±0.05 del equilibrio)
c) Crea heatmap: eje X = p, eje Y = α, color = ensayos hasta convergencia

**14. Ambiente Cambiante**

Implementa reversión de contingencia:
- Ensayos 1-100: p = 0.8
- Ensayos 101-200: p = 0.2

a) Simula con α = 0.1, 0.3, 0.5, 0.7
b) Grafica las 4 curvas en mismo panel
c) ¿Cuál α detecta el cambio más rápido?
d) ¿Cuál α es más estable en cada fase?

### Ejercicios Integradores

**15. Conexión con Capítulos Previos**

a) Relaciona el modelo de Bush-Mosteller con los experimentos de Dickinson (Cap. 9) sobre demora
b) ¿Cómo podría modificarse el modelo para incorporar efectos de demora?
c) Diseña un experimento que permita estimar α en ratas

**16. Aplicación Clínica**

En terapia cognitivo-conductual, se usa "exposición gradual" para tratar fobias.

a) Modela la exposición como ensayos donde E = fobia, R = 0 (no pasa nada malo)
b) Si V inicial = 0.9 (miedo alto), ¿cuántas sesiones de exposición se requieren para reducir a V = 0.2?
c) ¿Cómo afecta α (que podría variar entre pacientes) al número de sesiones necesarias?

**17. Diseño Experimental**

Diseña un experimento para distinguir empíricamente entre:
- Modelo Bush-Mosteller (elementos independientes)
- Modelo Rescorla-Wagner (elementos compiten)

a) Especifica procedimiento detallado
b) Predicciones cuantitativas de cada modelo
c) ¿Qué patrón de resultados favorecería cada modelo?

---

## Figuras Requeridas

**Curvas de Aprendizaje Empíricas**:
- Figura 7.1: Parssey (1948) - Parpadeo humanos
- Figura 7.2: Ramond (1954) - Presión palanca ratas  
- Figura 7.3: Curva idealizada negativamente acelerada

**Problema de Gradualidad**:
- Figura 7.4: Datos individuales vs. promedio

**Sistemas Dinámicos**:
- Figura 7.5: Ejemplo epidemia, crecimiento exponencial

**Carga-Descarga**:
- Figura 7.6: Respuesta a un pulso
- Figura 7.7: Respuesta a tres pulsos
- Figura 7.8: Adquisición α = 0.5
- Figura 7.9: Adquisición α = 0.2
- Figura 7.10: Comparación múltiples α
- Figura 7.11: Extinción

**Error de Predicción**:
- Figura 7.12: V y δ en paneles apilados

**Filtro Exponencial**:
- Figura 7.13: Decaimiento de pesos
- Figura 7.14: Simulación tragamonedas

**Parámetro α**:
- Figura 7.15: Velocidad convergencia
- Figura 7.16: Ruido (α grande vs. pequeño)
- Figura 7.17: Cambio (α grande vs. pequeño)

**Aplicaciones**:
- Figura 7.18: Reforzamiento parcial
- Figura 7.19: Adquisición-extinción
- Figura 7.20: Reversión contingencia
- Figura 7.21: Diferentes tasas de aprendizaje

---

## Lecturas Recomendadas

### Artículos Clásicos Fundamentales

**Bush, R. R., & Mosteller, F. (1951)**. A mathematical model for simple learning. *Psychological Review*, 58(5), 313-323.
- El artículo original que introduce el modelo—lectura esencial

**Estes, W. K. (1950)**. Toward a statistical theory of learning. *Psychological Review*, 57(2), 94-107.
- Modelo contemporáneo a Bush-Mosteller con enfoque probabilístico

**Rescorla, R. A., & Wagner, A. R. (1972)**. A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement. En A. H. Black & W. F. Prokasy (Eds.), *Classical conditioning II: Current research and theory*. Appleton-Century-Crofts.
- La extensión crucial que resuelve limitaciones del modelo Bush-Mosteller

### Sobre Curvas de Aprendizaje y Gradualidad

**Gallistel, C. R., Fairhurst, S., & Balsam, P. (2004)**. The learning curve: Implications of a quantitative analysis. *PNAS*, 101(36), 13124-13131.
- Argumenta contra aprendizaje gradual usando análisis cuantitativo sofisticado

**Gallistel, C. R., & Gibbon, J. (2000)**. Time, rate, and conditioning. *Psychological Review*, 107(2), 289-344.
- Perspectiva alternativa a modelos asociativos, enfatizando procesamiento temporal

### Aplicaciones Modernas

**Sutton, R. S., & Barto, A. G. (2018)**. *Reinforcement learning: An introduction* (2nd ed.). MIT Press. [Disponible gratis en línea]
- Capítulos 2-6 extienden Bush-Mosteller a aprendizaje por refuerzo moderno

**Dayan, P., & Daw, N. D. (2008)**. Decision theory, reinforcement learning, and the brain. *Cognitive, Affective, & Behavioral Neuroscience*, 8(4), 429-453.
- Conecta modelos computacionales con neurociencia

**Schultz, W., Dayan, P., & Montague, P. R. (1997)**. A neural substrate of prediction and reward. *Science*, 275(5306), 1593-1599.
- Evidencia que neuronas dopaminérgicas codifican error de predicción δ

### Textos de Referencia

**Rescorla, R. A. (1988)**. Pavlovian conditioning: It's not what you think it is. *American Psychologist*, 43(3), 151-160.
- Revisión accesible del modelo Rescorla-Wagner y evidencia empírica

**Mackintosh, N. J. (1974)**. *The psychology of animal learning*. Academic Press.
- Capítulos 3-4: Tratamiento clásico comprensivo de teorías asociativas

**Domjan, M. (2014)**. *The principles of learning and behavior* (7th ed.). Cengage Learning.
- Capítulo 4: Introducción pedagógica a modelos de condicionamiento

### Para Profundizar

**Pearce, J. M., & Hall, G. (1980)**. A model for Pavlovian learning: Variations in the effectiveness of conditioned but not of unconditioned stimuli. *Psychological Review*, 87(6), 532-552.
- Modelo alternativo donde α (atencionalidad) cambia con experiencia

**Miller, R. R., Barnet, R. C., & Grahame, N. J. (1995)**. Assessment of the Rescorla-Wagner model. *Psychological Bulletin*, 117(3), 363-386.
- Evaluación crítica comprehensiva del modelo R-W

**Niv, Y. (2009)**. Reinforcement learning in the brain. *Journal of Mathematical Psychology*, 53(3), 139-154.
- Revisión moderna conectando aprendizaje por refuerzo con neurobiología

---

## Notas Técnicas

### Nota 1: Solución Analítica de la Ecuación en Diferencias

Para el caso especial donde R_t = λ (constante), la ecuación:

V_{t+1} = (1-α)V_t + αλ

tiene solución cerrada:

V_t = λ + (V_0 - λ)(1-α)^t

**Derivación**:

Definiendo x_t = V_t - λ:

x_{t+1} = V_{t+1} - λ
x_{t+1} = (1-α)V_t + αλ - λ
x_{t+1} = (1-α)V_t - (1-α)λ
x_{t+1} = (1-α)(V_t - λ)
x_{t+1} = (1-α)x_t

Esta es ecuación geométrica con solución:
x_t = x_0 (1-α)^t

Sustituyendo de vuelta:
V_t - λ = (V_0 - λ)(1-α)^t
V_t = λ + (V_0 - λ)(1-α)^t

**Propiedades**:
- Si V_0 < λ: V aumenta exponencialmente hacia λ
- Si V_0 > λ: V decrece exponencialmente hacia λ  
- Si V_0 = λ: V permanece en λ
- Tasa de convergencia determinada por (1-α)

### Nota 2: Filtro Exponencial como Media Ponderada

La expansión completa del modelo muestra:

V_t = α Σᵢ₌₀^{t-1} (1-α)^i R_{t-i-1} + (1-α)^t V_0

Para t grande, el término (1-α)^t V_0 → 0, dejando:

V_t ≈ α Σᵢ₌₀^{∞} (1-α)^i R_{t-i-1}

Los pesos suman a 1:
α Σᵢ₌₀^{∞} (1-α)^i = α × 1/(1-(1-α)) = α × 1/α = 1

**Vida media del filtro**:

El tiempo para que un peso decaiga a la mitad:
(1-α)^τ = 0.5
τ = log(0.5) / log(1-α) ≈ 0.693 / α

Para α = 0.3: τ ≈ 2.3 ensayos

### Nota 3: Relación con Otros Modelos

**Bush-Mosteller vs. Hull**: 
- Hull usó multiplicación (Habit Strength = sHr × D × V)
- Bush-Mosteller usa suma ponderada
- Bush-Mosteller más tratable matemáticamente

**Bush-Mosteller vs. Rescorla-Wagner**:
- Único cambio: R - V_elemento → R - Σ V_todos
- Este cambio permite competencia entre elementos

**Bush-Mosteller vs. Temporal Difference (TD)**:
- TD añade bootstrapping: aprende de predicciones futuras
- TD(0) es casi idéntico a Bush-Mosteller
- TD(λ) generaliza eligibilidad de credit assignment

### Nota 4: Estabilidad y Puntos de Equilibrio

Un punto de equilibrio V* satisface:
V* = (1-α)V* + α E[R]

Resolviendo:
V* - (1-α)V* = α E[R]
αV* = α E[R]
V* = E[R]

**Conclusión**: El modelo converge al valor esperado del reforzador.

**Estabilidad**: Para 0 < α < 2, el equilibrio es globalmente estable (atractor).

Con α > 2, el sistema oscila y puede divergir (no biológicamente plausible).

### Nota 5: Generalización a Múltiples Estímulos

Si múltiples estímulos {E₁, E₂, ..., Eₙ} están presentes en un ensayo, el modelo Bush-Mosteller actualiza cada uno independientemente:

Para cada i en elementos presentes:
  V_{i,t+1} = (1-αᵢ)V_{i,t} + αᵢ R_t

**Problema**: No hay interacción entre elementos.

**Solución R-W**: Cambiar R_t por (R_t - Σⱼ V_{j,t}) donde suma es sobre todos elementos presentes.

Esta modificación introduce competencia y resuelve bloqueo, ensombrecimiento, etc.

