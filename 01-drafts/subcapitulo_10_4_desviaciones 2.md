# CAPÍTULO X - SUBCAPÍTULO 10.4
# DESVIACIONES DE IGUALACIÓN Y MECANISMOS DE CONTROL

---

## INTRODUCCIÓN

En el Subcapítulo 10.3 examinamos la ecuación de Herrnstein y cómo, al aplicarse a situaciones de elección concurrente, deriva matemáticamente la Ley de Igualación: R₁/R₂ = r₁/r₂. Este logro teórico—derivar un fenómeno empírico robusto desde principios generales—representa un hito en la formalización cuantitativa del comportamiento. La cancelación algebraica de los parámetros k y (r₁ + r₂ + R_e) produce automáticamente igualación, sugiriendo que este patrón conductual emerge de cómo el refuerzo controla respuestas individuales.

Sin embargo, la igualación perfecta—donde la razón de respuestas iguala exactamente la razón de refuerzos y donde la sensibilidad a = 1.0 y el sesgo b = 1.0—es más la excepción que la regla en datos experimentales. En la vasta mayoría de los experimentos de elección concurrente, se observan desviaciones sistemáticas de la igualación estricta.

Recordemos la forma **generalizada** de igualación que documentamos en el Subcapítulo 10.2:

**B₁/B₂ = b(r₁/r₂)^a**

o en forma logarítmica:

**log(B₁/B₂) = a·log(r₁/r₂) + log(b)**

donde:
- **a** (sensibilidad): mide qué tan sensible es la distribución de respuestas a diferencias en refuerzo
- **b** (bias/sesgo): mide preferencia inherente independiente de las razones de refuerzo

En la mayoría de los experimentos, **a < 1** (undermatching) y **b ≠ 1** (presencia de sesgo). ¿Qué factores causan estas desviaciones sistemáticas? ¿Cómo pueden los experimentadores manipularlas? ¿Qué nos dicen estas desviaciones sobre los mecanismos que controlan la elección?

Este subcapítulo examina precisamente estas preguntas. Analizaremos los determinantes del undermatching (la desviación más común), las causas del overmatching (menos común pero teóricamente importante), las fuentes del sesgo, y—crucialmente—cómo el **changeover delay (COD)** modula dramáticamente la sensibilidad de la elección. Al final, tendremos una comprensión completa de qué variables experimentales controlan los parámetros de la forma generalizada de igualación.

---

## UNDERMATCHING: LA DESVIACIÓN MÁS COMÚN

### Definición y Prevalencia

El **undermatching** (sub-igualación) ocurre cuando el parámetro de sensibilidad **a < 1**. En este caso, la distribución de respuestas es **menos extrema** que lo predicho por igualación estricta. Los organismos distribuyen su comportamiento más equitativamente entre alternativas de lo que la razón de refuerzos sugeriría.

Consideremos un ejemplo concreto:

**Condición experimental:**
- Alternativa 1: IV 30-seg → r₁ = 120 refuerzos/hora
- Alternativa 2: IV 120-seg → r₂ = 30 refuerzos/hora
- Razón de refuerzos: r₁/r₂ = 4.0

**Predicción de igualación estricta (a = 1):**
- B₁/B₂ = r₁/r₂ = 4.0
- Es decir, la paloma debería emitir 4 veces más respuestas en la Alternativa 1

**Resultado típico con undermatching (a = 0.8):**
- B₁/B₂ = (r₁/r₂)^0.8 = 4.0^0.8 = 3.03
- Es decir, la paloma emite solo ~3 veces más respuestas en la Alternativa 1

La paloma muestra preferencia por la alternativa más rica, pero la preferencia es **menos marcada** de lo predicho por igualación estricta. No distribuye sus respuestas tan desigualmente como la diferencia en refuerzos sugeriría.

### Prevalencia del Undermatching

El undermatching es el patrón **modal** (más común) en experimentos de elección concurrente. Meta-análisis de cientos de experimentos revelan:

- **Valores típicos de a:** Entre 0.7 y 0.9 en palomas
- **Frecuencia:** Más del 70% de los experimentos reportan a < 1.0
- **Igualación perfecta (a ≈ 1.0):** Relativamente rara, típicamente requiere condiciones experimentales cuidadosamente optimizadas

Esta ubicuidad del undermatching sugiere que no es simplemente "ruido experimental" o error de medición. Más bien, refleja procesos sistemáticos que reducen la sensibilidad del comportamiento a diferencias en refuerzo. ¿Cuáles son estos procesos?

---

## CAUSAS DEL UNDERMATCHING

### 1. Discriminabilidad Imperfecta de las Alternativas

Una causa fundamental del undermatching es la **discriminabilidad imperfecta**: cuando las alternativas son difíciles de distinguir perceptualmente, el organismo es menos sensible a las diferencias en refuerzo entre ellas.

#### Evidencia Experimental: Baum (1974)

William Baum realizó un experimento elegante manipulando sistemáticamente la discriminabilidad de dos alternativas. Palomas enfrentaban dos teclas que podían diferir en:

**Condición de Alta Discriminabilidad:**
- Tecla 1: Luz roja brillante
- Tecla 2: Luz verde brillante
- Resultado: a ≈ 0.9 (cercano a igualación)

**Condición de Baja Discriminabilidad:**
- Tecla 1: Tono 1000 Hz
- Tecla 2: Tono 1050 Hz (solo 5% de diferencia)
- Resultado: a ≈ 0.6 (undermatching pronunciado)

La interpretación es intuitiva: cuando las alternativas son perceptualmente similares, es más difícil para el organismo rastrear cuál está produciendo más refuerzos. Hay más "confusión" entre las alternativas, llevando a una distribución menos diferenciada de respuestas.

#### Implicaciones Teóricas

Este hallazgo sugiere que la igualación no es un proceso puramente "racional" o "computacional" que opera sobre representaciones abstractas de tasas de refuerzo. Más bien, está limitada por los **procesos perceptuales** básicos del organismo. Si el organismo no puede discriminar confiablemente qué alternativa acaba de reforzar, no puede distribuir comportamiento de manera óptimamente sensible a las diferencias en refuerzo.

Desde una perspectiva aplicada, esto significa que para obtener igualación cercana a perfecta en experimentos, se deben usar estímulos altamente discriminables. Teclas de diferentes colores, ubicaciones espaciales distantes, o modalidades sensoriales diferentes (visual vs. auditiva) producen mayor sensibilidad que estímulos dentro de la misma dimensión con diferencias sutiles.

### 2. Cambios Frecuentes Sin Changeover Delay

Otra causa importante de undermatching es el patrón de **alternación rápida** entre opciones cuando no hay costo por cambiar.

#### El Problema de la Alternación Rápida

En ausencia de un changeover delay (COD = 0 segundos), los organismos pueden adoptar una estrategia de "muestreo rápido": cambiar frecuentemente entre alternativas para "cosechar" refuerzos de ambas sin comprometerse sustancialmente con ninguna.

Consideremos la lógica desde la perspectiva del organismo:

- En programas IV, los refuerzos se hacen disponibles independientemente del comportamiento
- Una vez que un refuerzo está disponible en una alternativa, permanece disponible hasta ser recolectado
- Por lo tanto, el organismo puede "chequear" ambas alternativas frecuentemente
- Cada refuerzo disponible se recolecta con una sola respuesta

Este patrón de alternación rápida produce varias consecuencias:

1. **Reducción del tiempo efectivo:** El tiempo dedicado a cada alternativa se fragmenta en episodios muy breves
2. **Distribución menos diferenciada:** Ambas alternativas reciben muchos "chequeos", produciendo razones de respuesta menos extremas
3. **Undermatching severo:** En casos extremos, a puede aproximarse a 0.3-0.5

#### Evidencia Experimental: Catania (1966)

Charles Catania demostró este fenómeno dramáticamente:

**Condición Sin COD (0 seg):**
- Palomas mostraban alternación muy rápida (cambios cada 2-3 segundos)
- a ≈ 0.4 (undermatching extremo)
- Distribución de respuestas casi indiferente a razones de refuerzo

**Condición Con COD (2 seg):**
- Palomas mostraban episodios más largos en cada alternativa
- a ≈ 0.9 (cercano a igualación)
- Distribución de respuestas claramente sensible a razones de refuerzo

Este resultado tiene implicaciones profundas: la estructura temporal del procedimiento experimental—específicamente, si hay un costo por cambiar—afecta dramáticamente la sensibilidad conductual. No es suficiente especificar las tasas de refuerzo programadas; también debemos especificar las reglas sobre cambios entre alternativas.

### 3. Experiencia Limitada

Un tercer factor que afecta el undermatching es la cantidad de **experiencia** del organismo con las contingencias.

#### Efectos del Entrenamiento Extenso

Múltiples estudios han documentado que con entrenamiento prolongado, **a tiende a incrementarse**, aproximándose a 1.0:

**Primeras 10 sesiones:**
- a ≈ 0.6-0.7
- Distribución relativamente indiferenciada

**Después de 30-50 sesiones:**
- a ≈ 0.8-0.9
- Distribución más sensible a diferencias en refuerzo

**Después de >100 sesiones (raro en la práctica):**
- a ≈ 0.9-1.0
- Igualación cercana a perfecta

#### Interpretación: Aprendizaje de las Contingencias

Esta mejora gradual sugiere que la igualación no es una respuesta "instintiva" o "refleja" a diferencias en refuerzo. Más bien, requiere que el organismo **aprenda** las contingencias—específicamente, que adquiera representaciones precisas de las tasas de refuerzo asociadas con cada alternativa.

En las etapas tempranas del entrenamiento, estas representaciones son ruidosas o imprecisas. Con experiencia extensa, se vuelven más precisas, permitiendo una distribución conductual más finamente calibrada.

Esta interpretación conecta la igualación con modelos más generales de aprendizaje asociativo. Así como en el modelo de Rescorla-Wagner los valores asociativos V se aproximan gradualmente a sus valores asintóticos, la distribución conductual en elección concurrente se aproxima gradualmente a igualación con experiencia acumulada.

---

## EL CHANGEOVER DELAY (COD): ANÁLISIS DETALLADO

El changeover delay merece atención especial porque es **la variable experimental más poderosa** para controlar undermatching. Su efecto es tan robusto que prácticamente todos los experimentos de elección concurrente modernos lo utilizan.

### Definición y Procedimiento

El **changeover delay (COD)** es un período de tiempo **después de cambiar** de una alternativa a otra durante el cual **no puede obtenerse refuerzo** en la nueva alternativa, incluso si un refuerzo está disponible.

Procedimiento específico:

1. Organismo responde en Alternativa 1
2. Organismo cambia a Alternativa 2 (primera respuesta en tecla 2)
3. **COD se activa:** Durante los siguientes X segundos, respuestas en Alternativa 2 no producen refuerzo
4. Después de X segundos, refuerzos programados en Alternativa 2 están nuevamente disponibles
5. Si el organismo cambia de nuevo a Alternativa 1, el COD se reactiva para Alternativa 1

Valores típicos de COD: 1-3 segundos

### Función del COD: Simular Costos de Cambio Ecológicos

¿Por qué implementar un COD? La justificación teórica es que en ambientes naturales, cambiar entre actividades o parches de recursos típicamente implica **costos temporales**:

**Ejemplos ecológicos:**
- **Forrajeo espacial:** Un ave que cambia entre dos parcelas de semillas debe volar entre ellas—tiempo durante el cual no puede comer
- **Caza de presas:** Un predador que cambia de tipo de presa debe reorientarse, buscar, acercarse—actividades que consumen tiempo
- **Actividades humanas:** Cambiar entre tareas laborales requiere reconfiguración mental, recuperación de materiales, etc.

El COD captura estos costos de cambio de una manera simple y controlada experimentalmente. Al introducir un pequeño "costo temporal" por cambiar, hace que el procedimiento de laboratorio se aproxime más a la estructura de decisiones en ambientes naturales.

### Efectos del COD sobre la Sensibilidad (a)

La relación entre duración del COD y sensibilidad no es simple—tiene una forma no-monotónica:

#### COD = 0 segundos (Sin costo de cambio)

**Patrón conductual:**
- Alternación muy rápida entre opciones
- Episodios breves (<5 segundos) en cada alternativa
- Muchos cambios por minuto (>20)

**Efecto sobre sensibilidad:**
- a ≈ 0.3-0.5 (undermatching extremo)
- Distribución de respuestas casi indiferente a razones de refuerzo

**Interpretación:** Sin costo de cambio, la estrategia óptima a corto plazo es "muestrear" ambas alternativas frecuentemente. Esto produce distribuciones poco diferenciadas.

#### COD = 1-3 segundos (Costo moderado)

**Patrón conductual:**
- Episodios más largos en cada alternativa (10-30 segundos)
- Cambios menos frecuentes (~5-10 por minuto)
- Distribución temporal más comprometida

**Efecto sobre sensibilidad:**
- a ≈ 0.8-1.0 (igualación cercana a perfecta)
- Distribución de respuestas claramente sensible a razones de refuerzo

**Interpretación:** Un costo moderado hace que cambiar sea menos atractivo a menos que la alternativa actual sea genuinamente inferior. Esto permite que las preferencias "verdaderas" se expresen.

#### COD > 5 segundos (Costo alto)

**Patrón conductual:**
- Episodios muy largos en cada alternativa (>60 segundos)
- Cambios muy infrecuentes (<3 por minuto)
- En casos extremos, preferencia casi exclusiva

**Efecto sobre sensibilidad:**
- a puede reducirse nuevamente a 0.6-0.8
- En casos extremos, puede aparecer overmatching (a > 1)

**Interpretación:** CODs muy largos "desacoplan" las respuestas de los refuerzos inmediatos. El organismo puede "olvidar" qué alternativa acaba de producir refuerzo, o el costo de cambiar puede ser tan alto que induce una estrategia casi exclusiva.

### Interpretación Teórica del COD

El COD tiene múltiples efectos teóricamente importantes:

**1. Desacopla Cambios de Refuerzo Inmediato:**
Sin COD, la primera respuesta después de cambiar puede ser reforzada inmediatamente. Esto crea una contingencia problemática: el acto de cambiar queda cercano temporalmente al refuerzo, potencialmente reforzando la estrategia de cambio rápido.

Con COD, esta contingencia se rompe. El refuerzo después de cambiar está necesariamente demorado por al menos X segundos, reduciendo la probabilidad de reforzar inadvertidamente el cambio en sí.

**2. Permite Expresión de Preferencias Genuinas:**
Al introducir un costo por cambiar, el COD hace que "valga la pena" permanecer en una alternativa solo si es genuinamente preferida. Reduce cambios impulsivos o estratégicos sin fundamento en diferencias de valor.

**3. Aproxima Estructura Ecológica:**
Como mencionamos, muchas situaciones naturales involucran costos temporales por cambiar entre actividades. El COD hace que el procedimiento de laboratorio capture esta característica estructural.

### Valores Óptimos de COD

Basándonos en décadas de investigación, las recomendaciones para diseño experimental son:

**Para producir igualación cercana a perfecta:**
- COD = 1.5-3.0 segundos (valores más comunes en la literatura)
- Evitar COD = 0 (produce undermatching severo)
- Evitar COD > 5 seg (puede producir efectos complejos)

**Para estudiar dinámica de cambio:**
- Variar sistemáticamente COD entre condiciones
- Examinar cómo cambian patrones temporales y sensibilidad

---

## OVERMATCHING: LA DESVIACIÓN MENOS COMÚN

### Definición y Características

El **overmatching** (sobre-igualación) ocurre cuando **a > 1**. En este caso, la distribución de respuestas es **más extrema** que lo predicho por igualación estricta. Los organismos distribuyen su comportamiento más desigualmente entre alternativas de lo que la razón de refuerzos sugeriría.

**Ejemplo:**

**Condición experimental:**
- r₁/r₂ = 4.0

**Predicción de igualación estricta (a = 1):**
- B₁/B₂ = 4.0

**Resultado con overmatching (a = 1.2):**
- B₁/B₂ = 4.0^1.2 = 5.28
- Preferencia más extrema que predicción de igualación

### Prevalencia y Condiciones

El overmatching es **considerablemente menos común** que undermatching:

- Reportado en <15% de experimentos estándar
- Típicamente requiere condiciones experimentales específicas
- Frecuentemente asociado con procedimientos no-estándar

### Causas Identificadas del Overmatching

#### 1. Programas Concurrentes RV-RV (No IV-IV)

La causa más robusta de overmatching es el uso de **programas de razón variable concurrentes** en lugar de programas IV.

**Herrnstein y Loveland (1975):**
- Procedimiento: Concurrentes RV-RV con diferentes razones
- Resultado: Preferencia casi exclusiva por la alternativa más rica
- Interpretación: a >> 1 (en casos extremos, preferencia exclusiva)

¿Por qué RV-RV produce overmatching/exclusividad?

Recordemos que en programas RV, la función de retroalimentación es **lineal**: r = R/n. Cada respuesta adicional produce el mismo incremento marginal en refuerzos. No hay rendimientos decrecientes.

Por lo tanto, desde una perspectiva de **maximización**, la estrategia óptima es responder exclusivamente a la alternativa con el requisito menor (el RV más rico). Cualquier respuesta dedicada a la alternativa más pobre es "desperdiciada"—podría haber producido más refuerzos si se hubiera emitido en la alternativa más rica.

Los organismos aproximan esta estrategia de maximización, produciendo preferencias muy extremas o exclusivas.

#### 2. Alta Discriminabilidad + COD Largo

Algunos experimentos han reportado overmatching leve (a = 1.1-1.3) con programas IV-IV cuando se combinan:

- Alternativas extremadamente discriminables (e.g., colores muy contrastantes + posiciones espaciales distintas)
- COD relativamente largo (4-6 segundos)

**Interpretación tentativa:**
Alta discriminabilidad permite rastrear diferencias en refuerzo con precisión. COD largo induce episodios muy largos en cada alternativa, llevando a distribuciones más "comprometidas" o "polarizadas".

Sin embargo, esta combinación de factores es relativamente rara y los efectos son pequeños comparados con el overmatching robusto observado en RV-RV.

### Evidencia Limitada

Es importante notar que la evidencia para overmatching con programas IV-IV estándar es **considerablemente más limitada** que la evidencia para undermatching. La mayoría de los experimentos bien controlados con IV-IV producen a < 1 o a ≈ 1, raramente a > 1.

Esto sugiere que overmatching no es un fenómeno tan general o robusto como undermatching. Requiere condiciones específicas (principalmente RV-RV) para manifestarse consistentemente.

---

## BIAS (SESGO): PREFERENCIAS INDEPENDIENTES DEL REFUERZO

### Definición del Parámetro b

El parámetro **b** (bias/sesgo) en la forma generalizada de igualación mide **preferencia inherente** por una alternativa que es independiente de las razones de refuerzo programadas.

Matemáticamente, en la ecuación:

**B₁/B₂ = b(r₁/r₂)^a**

- Si **b = 1**: sin sesgo (preferencia neutral)
- Si **b > 1**: sesgo hacia Alternativa 1
- Si **b < 1**: sesgo hacia Alternativa 2 (equivalente a sesgo hacia Alt 2 de magnitud 1/b)

### Interpretación Conceptual

El sesgo representa el valor de B₁/B₂ cuando r₁/r₂ = 1 (cuando ambas alternativas producen el mismo refuerzo). Es decir, es la preferencia "basal" cuando las contingencias son equitativas.

En forma logarítmica, esto es más claro:

**log(B₁/B₂) = a·log(r₁/r₂) + log(b)**

Aquí, **log(b)** es simplemente el intercepto de la recta—la preferencia cuando log(r₁/r₂) = 0.

---

## FUENTES DEL SESGO

### 1. Posición Espacial

Una de las fuentes más comunes de sesgo es la **preferencia por posición espacial** de las alternativas.

#### Evidencia en Palomas

Muchas palomas muestran preferencia consistente por:
- **Disco derecho** (más común): b ≈ 1.2-1.5 favoreciendo derecha
- **Disco izquierdo** (menos común): b ≈ 0.7-0.8 (sesgo hacia izquierda)

Esta preferencia aparece incluso cuando ambos discos producen exactamente el mismo refuerzo (r₁ = r₂).

#### Evidencia en Ratas

Ratas frecuentemente muestran preferencias por palancas basadas en posición:
- Algunos animales prefieren palanca derecha
- Otros prefieren palanca izquierda
- Preferencias pueden ser estables a través de meses

#### Interpretación: Lateralización y Hábitos Motores

Las preferencias por posición probablemente reflejan:
- **Lateralización cerebral:** Asimetrías hemisféricas en control motor
- **Hábitos motores:** Tendencias a orientarse en ciertas direcciones
- **Experiencia previa:** Historia de refuerzo en configuraciones espaciales anteriores

### 2. Características del Estímulo

Diferencias en las **características perceptuales** de las alternativas pueden crear preferencias intrínsecas.

#### Color

Algunos organismos muestran preferencias por ciertos colores:
- Palomas: frecuentemente prefieren rojo > verde > azul
- Estas preferencias pueden reflejar sensibilidad espectral del sistema visual

#### Brillo

Estímulos más brillantes pueden ser preferidos sobre estímulos tenues, independientemente del refuerzo.

#### Modalidad Sensorial

Si una alternativa es visual y la otra auditiva, pueden aparecer sesgos basados en qué modalidad es más saliente o preferida.

### 3. Tipo de Respuesta (Topografía)

Si las dos alternativas requieren **respuestas topográficamente diferentes**, puede haber sesgo basado en la facilidad o "naturalidad" de cada respuesta.

**Ejemplo:**
- Alternativa 1: Picar disco (respuesta natural para palomas)
- Alternativa 2: Presionar palanca con pata (respuesta menos natural)
- Resultado probable: Sesgo hacia picar, independientemente del refuerzo

### 4. Historia Experimental

La **experiencia previa** del organismo puede crear sesgos persistentes:

**Ejemplo:**
- Paloma fue entrenada previamente con disco izquierdo produciendo refuerzo más rico
- En nueva condición con refuerzo equitativo (r₁ = r₂), puede persistir preferencia por izquierda
- Este sesgo "heredado" puede persistir durante 10-20 sesiones antes de extinguirse

---

## CONTROL EXPERIMENTAL DEL SESGO

Dado que el sesgo es una "molestia" desde la perspectiva de estudiar sensibilidad a refuerzo, los experimentadores han desarrollado múltiples estrategias para controlarlo.

### 1. Contrabalanceo de Asignaciones

**Estrategia:** Asignar programas a posiciones de manera balanceada entre sujetos.

**Ejemplo con 6 palomas:**
- Palomas 1-3: IV 60-seg en disco izquierdo, IV 120-seg en disco derecho
- Palomas 4-6: IV 120-seg en disco izquierdo, IV 60-seg en disco derecho

Al promediar entre sujetos, sesgos por posición se cancelan.

### 2. Reversiones (Diseño de Reversión)

**Estrategia:** Cambiar la asignación de programas a posiciones dentro del mismo sujeto.

**Secuencia típica:**
- Fase 1 (sesiones 1-20): IV 60-seg izquierda, IV 120-seg derecha
- Fase 2 (sesiones 21-40): IV 120-seg izquierda, IV 60-seg derecha (¡reversión!)
- Comparar preferencias en ambas fases

Si hay sesgo por posición (digamos, preferencia por izquierda):
- Fase 1: Sesgo favorece alternativa más rica (ambos en misma dirección)
- Fase 2: Sesgo favorece alternativa más pobre (opuestos)

Al promediar o comparar fases, se puede aislar el efecto del refuerzo del efecto de la posición.

### 3. Condiciones de Control (r₁ = r₂)

**Estrategia:** Incluir condiciones donde ambas alternativas producen el mismo refuerzo.

**Ejemplo:**
- Concurrentes IV 60-seg IV 60-seg

En esta condición, igualación estricta predice B₁/B₂ = 1.0 (indiferencia).

Cualquier desviación de 1.0 indica sesgo:
- Si B₁/B₂ = 1.3 → sesgo hacia Alternativa 1 (b = 1.3)
- Si B₁/B₂ = 0.8 → sesgo hacia Alternativa 2 (b = 0.8)

Esta estimación directa de b puede usarse para "corregir" datos en otras condiciones.

### 4. Estimación Estadística de b

**Estrategia:** Usar regresión para estimar simultáneamente a y b de datos de múltiples condiciones.

Recordando la forma logarítmica:

**log(B₁/B₂) = a·log(r₁/r₂) + log(b)**

Esta es una ecuación de regresión lineal donde:
- Variable dependiente: log(B₁/B₂)
- Variable independiente: log(r₁/r₂)
- Pendiente: a (sensibilidad)
- Intercepto: log(b) (sesgo)

Al ajustar esta regresión a datos de 5-10 condiciones con diferentes razones de refuerzo, se obtienen estimaciones estadísticas de ambos parámetros.

---

## EVIDENCIA EMPÍRICA: ESTUDIOS SISTEMÁTICOS

### Baum (1974, 1979): Estudios Fundacionales

William Baum condujo una serie de experimentos sistemáticos examinando parámetros de la forma generalizada.

#### Manipulación de Discriminabilidad (Baum 1974)

**Procedimiento:**
- Variar discriminabilidad de alternativas
- Medir a en cada condición

**Resultados:**
- Alta discriminabilidad (colores diferentes): a ≈ 0.9
- Baja discriminabilidad (tonos similares): a ≈ 0.6
- Relación monotónica: mayor discriminabilidad → mayor a

#### Manipulación de COD (Baum 1974)

**Procedimiento:**
- Variar duración de COD (0, 1, 2, 4, 8 segundos)
- Medir a en cada condición

**Resultados:**
- COD = 0 seg: a ≈ 0.4
- COD = 2 seg: a ≈ 0.9
- COD = 4 seg: a ≈ 0.85
- COD = 8 seg: a ≈ 0.75

Función no-monotónica: a aumenta de 0 a 2 seg, luego disminuye levemente con CODs más largos.

### Davison y McCarthy (1988): Meta-Análisis

Davison y McCarthy realizaron un meta-análisis comprehensivo de más de 100 estudios de elección concurrente, examinando distribuciones de parámetros.

#### Distribución de Sensibilidad (a)

**Resultados clave:**
- **Media:** a ≈ 0.8
- **Mediana:** a ≈ 0.85
- **Rango modal:** 0.7-0.9
- **Proporción con a < 1:** ~75%
- **Proporción con a ≈ 1 (0.95-1.05):** ~20%
- **Proporción con a > 1:** ~5%

**Conclusión:** Undermatching es el patrón modal; igualación perfecta es relativamente rara.

#### Distribución de Sesgo (b)

**Resultados clave:**
- **Media:** b ≈ 1.0 (cuando se contrabalancean posiciones)
- **Desviación estándar:** ~0.3
- **Rango modal:** 0.8-1.2
- **Variabilidad entre sujetos:** Considerable (algunos sujetos muestran b = 0.6, otros b = 1.5)

**Conclusión:** Sesgo es variable pero usualmente controlable mediante contrabalanceo y reversiones.

#### Factores que Producen Igualación Cercana a Perfecta

Davison y McCarthy identificaron combinaciones de condiciones que consistentemente producen a ≈ 1:

1. **Alta discriminabilidad** (colores diferentes, posiciones espaciales distantes)
2. **COD óptimo** (2-3 segundos)
3. **Entrenamiento extenso** (>30 sesiones por condición)
4. **Control de sesgo** (contrabalanceo o reversiones)
5. **Programas IV-IV** (no RV-RV)

Cuando estas condiciones se satisfacen, a se aproxima a 1.0 en >60% de sujetos.

---

## SÍNTESIS: MECANISMOS DE CONTROL EXPERIMENTAL

Basándonos en décadas de investigación, podemos sintetizar las mejores prácticas para diseño experimental en estudios de elección:

### Para Maximizar Sensibilidad (a cercano a 1)

1. **Usar alta discriminabilidad:**
   - Colores muy diferentes (rojo vs. verde, no rojo vs. naranja)
   - Posiciones espaciales distantes
   - Estímulos en diferentes modalidades si es posible

2. **Implementar COD óptimo:**
   - 2-3 segundos es el rango más robusto
   - Evitar COD = 0 (undermatching severo)
   - Evitar COD > 5 seg (efectos complejos)

3. **Proporcionar entrenamiento extenso:**
   - Mínimo 20-30 sesiones por condición
   - Criterio de estabilidad: <10% variación en últimas 5 sesiones

4. **Usar programas IV-IV:**
   - Evitar RV-RV (produce preferencia exclusiva)
   - IV-IV con tasas apropiadas (no extremos como IV 10-seg)

### Para Controlar Sesgo (b)

1. **Contrabalancear asignaciones** entre sujetos
2. **Usar diseño de reversión** dentro de sujetos
3. **Incluir condiciones de control** (r₁ = r₂)
4. **Estimar b estadísticamente** mediante regresión

### Para Estudiar Desviaciones Sistemáticas

Si el objetivo es **estudiar** undermatching (no minimizarlo):

1. **Manipular discriminabilidad** sistemáticamente
2. **Variar COD** en amplio rango
3. **Usar sujetos con experiencia limitada**
4. **Examinar diferencias individuales** en a y b

---

## TRANSICIÓN AL SUBCAPÍTULO 10.5

Ahora tenemos una descripción cuantitativa completa de la conducta de elección. La Ley de Igualación (B₁/B₂ = r₁/r₂) captura el fenómeno fundamental descubierto por Herrnstein en 1961. La ecuación de Herrnstein (Subcapítulo 10.3) proporciona una derivación teórica elegante de este fenómeno. La forma generalizada (B₁/B₂ = b(r₁/r₂)^a) captura desviaciones sistemáticas de igualación perfecta.

Además, sabemos qué variables experimentales modulan estos parámetros:
- **Sensibilidad (a):** Discriminabilidad, COD, experiencia
- **Sesgo (b):** Posición, características estimulares, historia

Mediante control experimental apropiado, podemos producir igualación cercana a perfecta (a ≈ 1, b ≈ 1) o manipular sistemáticamente desviaciones.

Pero una descripción cuantitativa, por precisa que sea, no es una explicación completa. La pregunta interpretativa fundamental permanece: **¿Por qué los organismos igualan?**

¿Es igualación el resultado de una **estrategia adaptativa de maximización global**, donde el organismo computa (de alguna manera) la distribución que maximiza su tasa total de refuerzo? ¿O emerge de **reglas locales más simples**—como comparar tasas locales de refuerzo momento a momento—que no requieren representación de medidas globales?

Además, hemos asumido que las tasas de refuerzo r₁ y r₂ son cantidades bien definidas y estables. Pero ¿qué ocurre cuando la estructura temporal importa? ¿Qué pasa si las tasas de refuerzo varían momento a momento, o si diferentes partes del ambiente producen diferentes tasas locales?

Finalmente, ¿cómo afecta el **contexto** más amplio? Si un organismo enfrenta elección entre A y B, ¿importa si hay una tercera opción C disponible, o si el contexto general de refuerzo es rico versus pobre?

El siguiente subcapítulo introduce estas interpretaciones teóricas contrastantes y la evidencia experimental que las evalúa. Examinaremos:
- **Maximización global:** ¿Optimización de medidas agregadas?
- **Melioration:** ¿Igualación de tasas locales?
- **Efectos temporales:** ¿Sensibilidad a tasa local versus global?
- **Efectos de contexto:** ¿Violaciones de independencia de alternativas?

Sin embargo, dado que estos temas son extensos y técnicamente complejos, proporcionaremos solo una introducción en el Capítulo X. Los Capítulos X+1 (Modelos de Optimización Molar) y X+2 (Modelos de Optimización Local y Aprendizaje por Refuerzo) desarrollarán estos modelos en profundidad, explorando sus fundamentos matemáticos, predicciones empíricas, y conexiones con neurociencia y aprendizaje computacional.

---

## CONCEPTOS CLAVE

- **Undermatching (a < 1):** Distribución de respuestas menos extrema que predicción de igualación; patrón más común (~75% de estudios)
- **Causas de undermatching:** Discriminabilidad imperfecta, alternación rápida sin COD, experiencia limitada
- **Discriminabilidad:** Similaridad perceptual entre alternativas; menor discriminabilidad → menor sensibilidad (a más bajo)
- **Changeover Delay (COD):** Período después de cambiar durante el cual no puede obtenerse refuerzo; simula costos ecológicos de cambio
- **Efecto del COD sobre a:** Relación no-monotónica; COD óptimo (2-3 seg) maximiza sensibilidad; COD=0 o COD>5 reducen sensibilidad
- **Overmatching (a > 1):** Distribución más extrema que igualación; menos común (~5% de estudios); principalmente con RV-RV concurrentes
- **Bias/Sesgo (b):** Preferencia inherente independiente de razones de refuerzo; b=1 es neutral, b>1 sesgo hacia Alt 1, b<1 sesgo hacia Alt 2
- **Fuentes de sesgo:** Posición espacial, características estimulares (color, brillo), tipo de respuesta, historia experimental
- **Control de sesgo:** Contrabalanceo entre sujetos, reversiones dentro de sujetos, condiciones control (r₁=r₂), estimación estadística
- **Condiciones para igualación perfecta:** Alta discriminabilidad + COD óptimo + entrenamiento extenso + IV-IV + control de sesgo

---

## OBJETIVOS DE APRENDIZAJE

Al completar este subcapítulo, el estudiante debe ser capaz de:

1. Definir undermatching y overmatching en términos del parámetro de sensibilidad a
2. Explicar por qué undermatching es el patrón más común en experimentos de elección concurrente
3. Describir tres causas principales de undermatching: discriminabilidad imperfecta, alternación rápida, experiencia limitada
4. Explicar cómo la discriminabilidad de alternativas afecta la sensibilidad conductual, con referencia al estudio de Baum (1974)
5. Definir el changeover delay (COD) y explicar su función como simulador de costos ecológicos de cambio
6. Describir la relación no-monotónica entre duración de COD y sensibilidad, identificando el rango óptimo (2-3 segundos)
7. Explicar por qué programas RV-RV concurrentes producen overmatching/preferencia exclusiva mientras IV-IV producen igualación
8. Definir el parámetro de sesgo (b) e identificar sus principales fuentes (posición, estímulos, historia)
9. Describir cuatro estrategias para control experimental del sesgo
10. Sintetizar las condiciones experimentales necesarias para producir igualación cercana a perfecta (a ≈ 1, b ≈ 1)

---

**FIN DEL SUBCAPÍTULO 10.4**
