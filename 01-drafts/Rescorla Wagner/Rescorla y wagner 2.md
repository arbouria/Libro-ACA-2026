#   # Capítulo 8: El Modelo de Rescorla y Wagner

## Introducción

En el capítulo anterior, vimos que el modelo de aprendizaje por refuerzo, conocido también como modelo de *aprendizaje de error de predicción*, captura razonablemente bien la adquisición de valor predictivo cuando un estímulo o respuesta van seguidos de un refuerzo. En este capítulo veremos que este modelo *no* puede dar cuenta de los resultados presentados en el capítulo sobre asignación de crédito, los cuales ilustran la importancia de una serie de correlaciones: aquellas que sostiene el EC o la respuesta con la aparición del refuerzo; aquellas que sostiene el EC con otros estímulos presentes (elementos del contexto); y aquellas que existen previamente entre otros estímulos distintos y el refuerzo actual.

Originalmente, estos resultados indujeron interpretaciones que enfatizaban que la asignación de crédito a un estímulo o respuesta dependía de que estos fueran seguidos de un refuerzo que era *sorpresivo, inesperado, informativo, o que atraía la atención*. En 1972, Rescorla y Wagner presentaron un modelo que daba cuenta de los resultados que muestran que la mera contigüidad no es un factor necesario ni suficiente para la asignación de crédito. El modelo es una extensión del principio de la reducción de error, que captura la intuición acerca del papel de la sorpresa como un modelo matemático: todo ello sin hacer referencia a procesos atencionales que se suponían difíciles de evaluar con sujetos no humanos.

Este modelo sigue siendo hasta la fecha el motor de la investigación en aprendizaje.

---

## Parte I: Recordatorio del Modelo de Bush-Mosteller

Antes de adentrarnos en la innovación de Rescorla y Wagner, es crucial recordar el modelo de Bush y Mosteller que vimos en el capítulo anterior. Este modelo captura el principio básico de la **reducción de error de predicción**:

$$V_{x,t+1} = V_{x,t} + \alpha(R_t - V_{x,t})$$

Donde:
- $V_{x,t}$ es el valor predictivo del estímulo $x$ en el ensayo $t$
- $R_t$ es el refuerzo recibido (1 si está presente, 0 si está ausente)
- $\alpha$ es la tasa de aprendizaje (0 < α < 1)
- $(R_t - V_{x,t})$ es el **error de predicción**

### Características clave del modelo Bush-Mosteller

1. **Motor del aprendizaje**: El error de predicción impulsa el cambio en el valor
2. **Ganancias decrecientes**: A medida que V se aproxima a R, el aprendizaje se desacelera
3. **Asíntota**: El valor converge hacia R cuando no hay más error
4. **Limitación crítica**: Solo considera *un elemento a la vez*

Esta última característica es la que el modelo de Rescorla y Wagner revoluciona. Bush-Mosteller puede explicar cómo un tono aislado adquiere valor predictivo cuando se presenta antes de comida, pero **no puede explicar** qué ocurre cuando múltiples estímulos compiten por predecir el mismo refuerzo.

---

## Parte II: La Innovación de Rescorla y Wagner - Dos Componentes Fundamentales

El modelo de Rescorla y Wagner incluye dos grandes componentes que lo distinguen de su predecesor:

### Componente 1: El Motor de Bush-Mosteller

Mantiene el principio de reducción de error de predicción como motor fundamental del aprendizaje. La diferencia crucial está en *qué* se compara con el refuerzo.

### Componente 2: Modelo de Percepción de Estímulos Compuestos

Este es el aporte revolucionario. El modelo supone que los organismos perciben a los estímulos complejos como conjuntos de **elementos separables** que **compiten entre sí** por asignarse el crédito del refuerzo.

Un rostro, por ejemplo, no se procesa como una unidad integrada, sino como un conjunto de elementos: ojos, nariz, boca, orejas, contorno facial. Cada elemento puede adquirir independientemente valor predictivo, pero todos compiten por un "presupuesto" limitado de valor total.

### La Intuición Central

Imaginen que prueban un platillo nuevo en un restaurante y les encanta. El platillo es un compuesto de múltiples elementos:
- El plato en que se sirve
- Los ingredientes principales
- Las especias
- La presentación
- El ambiente del restaurante
- La compañía con quien comen

¿Cómo determina su sistema de aprendizaje qué elemento(s) "causaron" su placer? El modelo de Rescorla y Wagner propone que cada elemento compite por explicar el resultado. Si ya saben que disfrutan la compañía de su acompañante (ese elemento ya tiene valor alto), quedará menos "crédito" disponible para asignárselo a los ingredientes del platillo.

---

## Parte III: Supuestos Formales del Modelo de Rescorla y Wagner

### Supuesto 1: Separabilidad de los Estímulos

Los estímulos compuestos están conformados por elementos (estímulos) **separables**. 

- Una cara no es un estímulo integrado único
- Es un conjunto de elementos: ojos, boca, orejas, nariz, etc.
- Cada elemento puede procesarse independientemente
- Esta separabilidad permite competencia entre elementos

### Supuesto 2: Valor Predictivo de los Elementos

Cada elemento tiene un **número** (valor) asociado que representa su capacidad predictiva:

- $V$ puede ser **positivo**: predice la *presencia* de un refuerzo
- $V$ puede ser **negativo**: predice la *ausencia* de un refuerzo  
- $V$ puede ser **cero**: no predice nada (estímulo neutral)

**Relación con la conducta**: El valor es solo **ordinalmente** (no cuantitativamente) relacionado con la respuesta. Un elemento con $V=1$ no produce el doble de respuestas que uno con $V=0.5$; solo indica mayor predicción y probablemente más respuesta, pero sin especificar la proporción exacta.

### Supuesto 3: Regla de Integración - La Suma de Valores

El valor predictivo de un compuesto es la **suma aritmética** de los valores de sus elementos:

$$V_{total} = V_A + V_B + V_C + ... + V_n$$

Si un compuesto incluye un tono y una luz:

$$V_{total} = V_{tono} + V_{luz}$$

Esta suma representa la predicción total del organismo sobre si el refuerzo aparecerá.

### Supuesto 4: Actualización Basada en V_total

La innovación central. El cambio en el valor de cada elemento depende de la discrepancia entre el refuerzo obtenido y **la suma de todos los valores presentes**:

$$\Delta V_x = \alpha \beta (R - V_{total})$$

No es $(R - V_x)$ como en Bush-Mosteller, sino $(R - V_{total})$.

Esta modificación aparentemente pequeña tiene consecuencias profundas:

- El error de predicción es **compartido** por todos los elementos
- Todos los elementos presentes se actualizan con base en el **mismo error**
- Si el error es cero para el compuesto, **ningún elemento** cambia su valor

### Supuesto 5: Competencia entre Elementos

La consecuencia directa de usar $V_{total}$: los elementos **compiten** por un valor predictivo limitado.

El valor predictivo total está **limitado** por $R$. Cuando $V_{total}$ alcanza $R$, no queda error de predicción y el aprendizaje se detiene. Si un elemento ya "capturó" la mayor parte del valor predictivo, queda poco o nada disponible para otros elementos.

**Analogía económica**: Imaginen un presupuesto fijo ($R$) que debe distribuirse entre varios departamentos (elementos). Si un departamento ya gastó casi todo el presupuesto, los demás tienen muy poco margen para obtener recursos.

---

## Parte IV: La Ecuación Completa de Rescorla y Wagner

### Forma Básica

$$\Delta V_x = \alpha \beta (R - V_{total})$$

O en forma recursiva:

$$V_{x,t+1} = V_{x,t} + \alpha \beta (R_t - V_{total,t})$$

### Los Parámetros α y β

**¿Por qué dos parámetros de aprendizaje?**

Empíricamente, dos factores distintos afectan la velocidad del aprendizaje:

**α (alfa)** - Asociabilidad/efectividad del **refuerzo**:
- Captura propiedades del SBI
- Más comida → mayor α
- Mejor calidad de comida → mayor α
- Depende de la motivación del sujeto
- Varía con el tipo de refuerzo

**β (beta)** - Asociabilidad/saliencia del **estímulo condicionado**:
- Captura propiedades del EC
- Estímulo más intenso → mayor β
- Estímulo más sobresaliente → mayor β
- Varía entre modalidades sensoriales
- Puede variar entre individuos

Ambos parámetros toman valores entre 0 y 1, y se **multiplican** por el error de predicción:

$$\Delta V_x = \alpha \beta (R - V_{total})$$

El producto $\alpha\beta$ determina la **velocidad efectiva de aprendizaje** para cada elemento.

### Forma Alternativa - En Términos de Cambio

A veces es útil expresar el modelo en términos del cambio en valor:

$$\Delta V_x = V_{x,t+1} - V_{x,t} = \alpha \beta (R - V_{total})$$

Esta forma hace explícito que el cambio en cada ensayo es proporcional al error de predicción.

---

## Parte V: Aplicación 1 - Ensombrecimiento (Overshadowing)

El ensombrecimiento es un fenómeno donde un estímulo más saliente "eclipsa" el aprendizaje de un estímulo menos saliente cuando ambos se presentan juntos.

### Protocolo Experimental

**Grupo 1 (Compuesto)**: Tono + Luz → Comida (60 ensayos)
**Grupo 2 (Control Tono)**: Tono → Comida (60 ensayos)  
**Grupo 3 (Control Luz)**: Luz → Comida (60 ensayos)

### Supuestos para la Simulación

- $\beta_{tono} = 0.4$ (más saliente)
- $\beta_{luz} = 0.2$ (menos saliente)
- $\alpha = 0.2$ (igual para todos los grupos)
- $R = 1$ cuando hay comida

### Predicciones del Modelo

**Para Grupo 1 (Compuesto)**:

En cada ensayo:
$$V_{total} = V_{tono} + V_{luz}$$
$$\Delta V_{tono} = \alpha \beta_{tono}(R - V_{total}) = 0.2 \times 0.4 \times (1 - V_{total})$$
$$\Delta V_{luz} = \alpha \beta_{luz}(R - V_{total}) = 0.2 \times 0.2 \times (1 - V_{total})$$

Noten que:
1. Ambos elementos se actualizan con el **mismo error** $(R - V_{total})$
2. Pero el tono cambia **más rápido** (β más alta)
3. A medida que $V_{total} \to 1$, el error $\to 0$
4. El tono "captura" más valor antes de que se acabe el error

**Resultado**: Al final del entrenamiento:
- $V_{tono} \approx 0.67$
- $V_{luz} \approx 0.33$
- $V_{total} \approx 1.0$

**Para Grupos Control**:

Cada estímulo alcanza $V \approx 1.0$ porque no hay competencia.

### Comparación entre Condiciones

| Condición | $V_{tono}$ final | $V_{luz}$ final | Interpretación |
|-----------|------------------|-----------------|----------------|
| Tono solo | ~1.0 | N/A | Sin competencia |
| Luz sola | N/A | ~1.0 | Sin competencia |
| Compuesto | ~0.67 | ~0.33 | Ensombrecimiento |

El estímulo más saliente (tono) **ensombrece** al menos saliente (luz) en el grupo de compuesto. Ningún elemento alcanza el valor que alcanzaría si fuera presentado solo.

### Especificación de Figura 8.1

**Título**: Ensombrecimiento: Competencia entre elementos de distinta saliencia

**Descripción**: 
- Gráfica con tres paneles (o líneas en un mismo panel)
- Eje X: Ensayos (1-60)
- Eje Y: Valor Predictivo (V) (0-1.0)
- Panel A: Grupo Compuesto
  - Línea sólida azul: $V_{tono}$ (asíntota ~0.67)
  - Línea sólida roja: $V_{luz}$ (asíntota ~0.33)
  - Línea punteada negra: $V_{total}$ (asíntota ~1.0)
- Panel B: Controles
  - Línea azul: Tono solo (asíntota ~1.0)
  - Línea roja: Luz sola (asíntota ~1.0)
  
**Nota en pie de figura**: El tono más saliente (β=0.4) alcanza mayor valor que la luz menos saliente (β=0.2) cuando se entrenan juntos, pero ambos alcanzan valores menores que cuando se entrenan solos. Este es el fenómeno de ensombrecimiento.

---

## Parte VI: Aplicación 2 - Bloqueo (Blocking)

El bloqueo es quizás el resultado más contraintuitivo y más importante que el modelo de Rescorla y Wagner explica.

### Protocolo Experimental

**Grupo Experimental (Bloqueo)**:
- Fase 1: Tono → Comida (60 ensayos)
- Fase 2: Tono + Luz → Comida (60 ensayos)

**Grupo Control**:
- Fase 1: (sin entrenamiento)
- Fase 2: Tono + Luz → Comida (60 ensayos)

### Predicción Intuitiva vs. Modelo R-W

**Intuición de contigüidad**: En ambos grupos, la luz es seguida de comida en la Fase 2. Por tanto, ambos grupos deberían aprender sobre la luz igualmente.

**Predicción R-W**: El grupo experimental NO aprenderá sobre la luz porque el tono ya predice perfectamente la comida.

### Análisis Cuantitativo - Grupo Experimental

**Fase 1**: Solo Tono → Comida

Ensayo inicial:
- $V_{tono} = 0$
- Error = $1 - 0 = 1$
- $\Delta V_{tono} = \alpha\beta_{tono}(1) > 0$

Después de 60 ensayos:
- $V_{tono} \approx 1.0$
- Error $\approx 0$

**Fase 2**: Compuesto (Tono + Luz) → Comida

Primer ensayo de Fase 2:
- $V_{tono} \approx 1.0$ (de Fase 1)
- $V_{luz} = 0$ (nunca antes presentada)
- $V_{total} = 1.0 + 0 = 1.0$
- Error = $R - V_{total} = 1 - 1 = 0$

$$\Delta V_{luz} = \alpha\beta_{luz}(0) = 0$$

El error de predicción es **cero** desde el primer ensayo de Fase 2. No hay aprendizaje sobre la luz.

Este análisis revela la esencia del bloqueo: cuando un elemento ya predice perfectamente el refuerzo, **no hay error de predicción** que asignar a elementos nuevos.

### Análisis Cuantitativo - Grupo Control

**Fase 2**: Compuesto (Tono + Luz) → Comida

Primer ensayo:
- $V_{tono} = 0$
- $V_{luz} = 0$
- $V_{total} = 0$
- Error = $1 - 0 = 1$

Ambos elementos adquieren valor, similar al ensombrecimiento visto anteriormente.

### Comparación de Resultados

| Grupo | $V_{tono}$ final | $V_{luz}$ final | Mecanismo |
|-------|------------------|-----------------|-----------|
| Bloqueo | ~1.0 | ~0.0 | Tono bloquea la luz |
| Control | ~0.6 | ~0.4 | Ensombrecimiento mutuo |

### Especificación de Figura 8.2

**Título**: Bloqueo: El aprendizaje previo previene el aprendizaje nuevo

**Descripción**:
- Dos paneles verticales (Grupo Experimental vs. Control)
- Eje X: Ensayos de Fase 2 (1-60)
- Eje Y: Valor Predictivo (0-1.0)
- Línea vertical punteada separando Fase 1 y Fase 2
- Grupo Experimental:
  - Pre-Fase 2: $V_{tono}$ ya en 1.0
  - Línea azul ($V_{tono}$): mantiene ~1.0
  - Línea roja ($V_{luz}$): se mantiene en ~0.0
- Grupo Control:
  - Pre-Fase 2: ambos valores en 0
  - Línea azul ($V_{tono}$): aumenta a ~0.6
  - Línea roja ($V_{luz}$): aumenta a ~0.4

**Nota**: El entrenamiento previo del tono "bloquea" completamente el aprendizaje sobre la luz en el grupo experimental, a pesar de que la luz es seguida de comida igual que en el control.

---

## Parte VII: Aplicación 3 - Sobreexpectativa (Overexpectation)

Esta es una de las predicciones más contraintuitivas del modelo: que reforzar más puede producir una *disminución* en el valor predictivo.

### El Problema Contraintuitivo

Pregunta: ¿Puede el refuerzo adicional *reducir* el valor predictivo de un estímulo?

**Intuición**: Más refuerzo debería siempre incrementar (o al menos mantener) el valor.

**Predicción R-W**: En ciertas circunstancias, más refuerzo puede *reducir* valores.

### Protocolo Experimental

**Fase 1**: 
- Tono → Comida (60 ensayos)
- Luz → Comida (60 ensayos)

**Fase 2**:
- Tono + Luz → Comida (60 ensayos)

### Análisis Cuantitativo

**Al final de Fase 1**:
- $V_{tono} \approx 1.0$
- $V_{luz} \approx 1.0$

**Primer ensayo de Fase 2**:
- $V_{total} = V_{tono} + V_{luz} = 1.0 + 1.0 = 2.0$
- $R = 1$ (solo aparece una porción de comida)
- Error = $R - V_{total} = 1 - 2 = -1$

¡El error es **negativo**!

$$\Delta V_{tono} = \alpha\beta_{tono}(-1) < 0$$
$$\Delta V_{luz} = \alpha\beta_{luz}(-1) < 0$$

Ambos valores **disminuyen** a pesar de que el refuerzo está presente.

### ¿Por qué ocurre esto?

El organismo "espera" 2 unidades de comida (porque cada estímulo individualmente predice 1 unidad), pero solo obtiene 1 unidad. Esta **sobrepedicción** genera un error negativo que reduce los valores.

### Asíntota de Fase 2

Los valores disminuyen hasta que:
$$V_{tono} + V_{luz} = 1$$

Por ejemplo:
- $V_{tono} \approx 0.5$
- $V_{luz} \approx 0.5$

En este punto, la predicción total coincide con el refuerzo obtenido y el error se hace cero.

### Implicaciones Teóricas

Este resultado es **imposible de explicar** sin el componente de $V_{total}$:
- Un modelo como Bush-Mosteller **no puede predecir** que el refuerzo cause disminución
- Solo al considerar la **suma de elementos** emerge esta predicción
- Es un test crítico del modelo: si no se observa empíricamente, el modelo fallaría

### Evidencia Empírica

Experimentos de Kremer (1978) y Rescorla (2006) confirmaron esta predicción contraintuitiva, proporcionando fuerte apoyo al modelo.

### Especificación de Figura 8.3

**Título**: Sobreexpectativa: Refuerzo que reduce valor predictivo

**Descripción**:
- Panel único con dos fases
- Eje X: Ensayos totales (Fase 1: 1-120, Fase 2: 121-180)
- Eje Y: Valor Predictivo (0-1.2)
- Línea vertical en ensayo 120 separando fases
- Fase 1 (ensayos 1-120):
  - Línea azul ($V_{tono}$): aumenta a 1.0
  - Línea roja ($V_{luz}$): aumenta a 1.0
  - Se entrenan por separado (mostrar como segmentos discontinuos alternados si se desea)
- Fase 2 (ensayos 121-180):
  - Línea azul ($V_{tono}$): *disminuye* de 1.0 a ~0.5
  - Línea roja ($V_{luz}$): *disminuye* de 1.0 a ~0.5
  - Línea punteada negra ($V_{total}$): disminuye de 2.0 a ~1.0

**Nota**: Al inicio de Fase 2, la suma de valores (2.0) excede el refuerzo disponible (1.0), generando un error negativo que reduce ambos valores hasta que la suma iguala al refuerzo.

---

## Parte VIII: Aplicación 4 - Contingencia y el Papel del Contexto

Recordemos del capítulo anterior que Rescorla demostró que la contigüidad no es suficiente: lo que importa es la **contingencia** - la diferencia entre $P(R|EC)$ y $P(R|\neg EC)$.

### El Reto para el Modelo

**Problema**: La ecuación básica de R-W:
$$\Delta V_{EC} = \alpha\beta(R - V_{total})$$

...solo considera lo que pasa cuando el EC **está presente**. ¿Cómo puede capturar el efecto de lo que pasa en **ausencia** del EC?

### La Solución: El Contexto como Estímulo

Rescorla y Wagner proponen que el **contexto** (el ambiente experimental) es también un estímulo que:
- Está **siempre presente**
- Puede adquirir valor predictivo
- Compite con otros estímulos por el valor

Elementos del contexto:
- Paredes de la cámara experimental
- Iluminación
- Ruidos de fondo
- Olores
- Textura del piso

### Reinterpretación de los Protocolos de Contingencia

**Verdaderamente correlacionado**: $P(R|EC) > P(R|\neg EC)$

Durante EC:
- Presentes: EC + Contexto
- $V_{total} = V_{EC} + V_{Contexto}$

Durante ausencia de EC (ITI):
- Presente: solo Contexto
- $V_{total} = V_{Contexto}$

**No correlacionado**: $P(R|EC) = P(R|\neg EC)$

Durante EC:
- Presentes: EC + Contexto
- Refuerzo con probabilidad p

Durante ITI:
- Presente: solo Contexto  
- Refuerzo con la misma probabilidad p

### Análisis del Caso No Correlacionado

Supongamos $P(R|EC) = P(R|\neg EC) = 0.5$

**Fase inicial**:
- Contexto se entrena en ambos tipos de ensayos
- $V_{Contexto}$ aumenta hacia 0.5
- En ensayos con EC: $V_{total} = V_{EC} + V_{Contexto}$

**A medida que el contexto aprende**:
- El contexto ya predice el refuerzo probabilístico
- Cuando aparece el EC junto al contexto: **bloqueo**
- El EC no puede adquirir valor porque el contexto ya "explica" el refuerzo

**Asíntota**:
- $V_{Contexto} \approx 0.5$
- $V_{EC} \approx 0$

El modelo R-W predice correctamente que no habrá condicionamiento cuando la contingencia es cero.

### Caso Verdaderamente Correlacionado

Supongamos $P(R|EC) = 1.0$ y $P(R|\neg EC) = 0.5$

**Dos tipos de ensayos**:

*Ensayos con EC*:
- $V_{total} = V_{EC} + V_{Contexto}$
- $R = 1$ (siempre)
- Error = $1 - (V_{EC} + V_{Contexto})$

*Ensayos sin EC (solo contexto)*:
- $V_{total} = V_{Contexto}$
- $R$ probabilístico (0.5)
- Error variable

**Dinámica**:
- El contexto adquiere $V \approx 0.5$ (por los ensayos ITI)
- En ensayos con EC, error inicial = $1 - 0.5 = 0.5$
- El EC adquiere el valor residual: $V_{EC} \approx 0.5$
- Suma total: $V_{EC} + V_{Contexto} \approx 1.0$

El modelo predice condicionamiento proporcional a la **diferencia** en probabilidades de refuerzo.

### Predicción Crítica

Si "eliminamos" el condicionamiento al contexto (por ejemplo, presentando refuerzos del ITI con otra señal), el EC debería adquirir más valor.

**Protocolo de prueba**:
- Grupo 1: EC → R (p=1.0); ITI: Contexto → R (p=0.5)
- Grupo 2: EC → R (p=1.0); ITI: **Señal X** → R (p=0.5)

**Predicción**: Grupo 2 debería mostrar más condicionamiento al EC porque la Señal X, no el contexto, compite con el EC.

Esta predicción ha sido confirmada experimentalmente.

### Especificación de Figura 8.4

**Título**: El contexto como estímulo: Bloqueando el aprendizaje del EC

**Descripción**:
- Dos paneles (Contingencia Positiva vs. No Correlacionado)
- Eje X: Ensayos (1-100)
- Eje Y: Valor Predictivo (0-1.0)
- Panel A (Contingencia positiva: p(R|EC)=1, p(R|~EC)=0.5):
  - Línea azul: $V_{EC}$ → asíntota ~0.5
  - Línea verde: $V_{Contexto}$ → asíntota ~0.5
  - Línea punteada: $V_{total}$ en ensayos con EC → asíntota ~1.0
- Panel B (No correlacionado: p(R|EC)=p(R|~EC)=0.5):
  - Línea azul: $V_{EC}$ → se mantiene en ~0
  - Línea verde: $V_{Contexto}$ → asíntota ~0.5
  
**Nota**: Cuando la contingencia es cero (Panel B), el contexto "bloquea" completamente el aprendizaje del EC al ya explicar la ocurrencia probabilística del refuerzo.

---

## Parte IX: Inhibición Condicionada

Hasta ahora hemos discutido estímulos **excitatorios** (V > 0) que predicen la *presencia* de refuerzo. Pero el modelo R-W también permite **inhibidores condicionados** (V < 0) que predicen la *ausencia* de refuerzo.

### ¿Por qué es Importante la Inhibición?

Predecir cuándo *no* ocurrirá un refuerzo tiene ventajas adaptativas:

- **Para presas**: Señal de "seguridad" (depredador no aparecerá) permite forrajear sin interrupciones
- **Para forrajeadores**: Señal de "no comida" permite reorientar búsqueda a otros lugares
- **En general**: Optimiza distribución de comportamiento

### El Problema con Bush-Mosteller

El modelo original no permite valores negativos:

**Escenario**: Persona paseando perro que ignora al observador
- $R = 0$ (sin gruñido ni cola movimiento)
- $V_{persona} = 0$ (desconocido)
- Error = $R - V = 0 - 0 = 0$
- $\Delta V = 0$

No hay aprendizaje. La persona sigue siendo neutral.

### La Solución de R-W: Valores Negativos

El modelo R-W *permite* que V sea negativo, representando predicción de ausencia.

**¿Cómo se genera un valor negativo?**

Requiere un **error de predicción negativo**:
$$Error = R - V_{total} < 0$$

Esto solo ocurre cuando:
- $R = 0$ (no hay refuerzo)
- $V_{total} > 0$ (se esperaba refuerzo)

**Implicación crítica**: Un inhibidor solo se forma cuando un estímulo neutro aparece en **compuesto** con un excitador.

### Protocolo para Crear un Inhibidor

**Fase 1**: Establecer un excitador
- Tono → Comida (60 ensayos)
- Resultado: $V_{tono} \approx 1.0$

**Fase 2**: Crear el inhibidor
- Tono + Luz → Sin comida (60 ensayos)
- Tono solo → Comida (ensayos intercalados)

### Análisis Cuantitativo

**Primer ensayo de no refuerzo con compuesto**:
- $V_{tono} \approx 1.0$
- $V_{luz} = 0$
- $V_{total} = 1.0$
- $R = 0$
- Error = $0 - 1.0 = -1.0$

$$\Delta V_{luz} = \alpha\beta_{luz}(-1.0) < 0$$

La luz adquiere **valor negativo**.

**A medida que avanza el entrenamiento**:
- $V_{luz}$ disminuye (se hace más negativo)
- $V_{tono}$ se mantiene alto (por ensayos intercalados de refuerzo)
- En ensayos de compuesto: $V_{total} = V_{tono} + V_{luz}$ se aproxima a 0
- Error en compuesto → 0

**Asíntota**:
- $V_{tono} \approx 1.0$ (mantenido por ensayos reforzados)
- $V_{luz} \approx -1.0$ (inhibidor condicionado)
- En compuesto: $V_{total} = 1.0 + (-1.0) = 0$ → sin error

### Ejemplo Cotidiano Ampliado

**Situación**: Persona paseando un perro agresivo

**Fase 1**: 
- Persona sola con perro → Perro gruñe
- $V_{persona} \to 1.0$ (predice gruñido)

**Fase 2**:
- Persona + Pareja con perro → Perro NO gruñe
- Persona sola con perro → Perro SÍ gruñe (ensayos intercalados)

**Resultado**:
- $V_{pareja} \to -1.0$ (inhibidor)
- La pareja predice ausencia de gruñido

### Las Pruebas de Rescorla para Inhibición

El problema empírico: ¿Cómo distinguir un **inhibidor** (V < 0) de un estímulo **neutral** (V = 0)?

Rescorla (1969) propuso dos pruebas necesarias:

#### Prueba 1: Sumación

**Protocolo**:
1. Establecer excitador A en grupo aparte
2. Probar respuesta a A solo
3. Probar respuesta a compuesto A + X

**Predicción para inhibidor**:
- Respuesta a A + X < Respuesta a A solo
- Porque $V_A + V_X < V_A$ si $V_X < 0$

**Interpretación alternativa**: 
X simplemente distrae atención de A (no es verdaderamente inhibitorio).

#### Prueba 2: Retardo (Retardation)

**Protocolo**:
1. Entrenar X como inhibidor
2. Fase de adquisición: X → Comida (muchos ensayos)
3. Comparar con control neutral Y → Comida

**Predicción para inhibidor**:
- X debe tardar **más** en adquirir valor excitatorio
- Porque empieza en V < 0, no en V = 0

**Interpretación alternativa**:
X pierde atención por familiaridad (habituación), no por ser inhibitorio.

#### La Lógica de las Dos Pruebas

Las interpretaciones alternativas son **contradictorias**:
- Sumación: X recibe *más* atención (distrae de A)
- Retardo: X recibe *menos* atención (habituado)

Si X **pasa ambas pruebas**, las explicaciones atencionales se contradicen entre sí y se descartan. La única explicación consistente es que X es genuinamente inhibitorio.

### Análisis Cuantitativo de las Pruebas

**Prueba de Sumación**:

Estímulo A solo (excitador con $V_A = 1.0$):
- $V_{total} = 1.0$
- Respuesta proporcional a 1.0

Compuesto A + X (donde $V_X = -0.8$):
- $V_{total} = 1.0 + (-0.8) = 0.2$
- Respuesta proporcional a 0.2

Respuesta al compuesto es **menor** → pasa prueba.

**Prueba de Retardo**:

Control neutral Y:
- Ensayo 1: $V_Y = 0$, Error = $1-0=1$
- Aprendizaje rápido desde 0

Inhibidor X ($V_X = -0.8$):
- Ensayo 1: $V_X = -0.8$, Error = $1-(-0.8)=1.8$
- Pero debe subir desde -0.8 a valores positivos
- Requiere más ensayos para cruzar 0 y mostrar excitación

X aprende **más lento** → pasa prueba.

### Especificación de Figuras 8.5 y 8.6

**Figura 8.5: Creación de un Inhibidor Condicionado**

**Descripción**:
- Panel único
- Eje X: Ensayos (1-100)
- Eje Y: Valor Predictivo (-1.0 a 1.0)
- Línea azul ($V_{tono}$): se mantiene en ~1.0
- Línea roja ($V_{luz}$): disminuye de 0 a ~-1.0
- Línea punteada negra ($V_{total}$ en compuesto): disminuye de ~1.0 a ~0

**Nota**: Ensayos no reforzados del compuesto Tono+Luz (con $V_{tono}$ alto) generan errores negativos que convierten a la luz en un inhibidor condicionado.

**Figura 8.6: Pruebas de Inhibición Condicionada**

**Dos paneles**:

Panel A - Prueba de Sumación:
- Eje X: Condición (A solo, A+X)
- Eje Y: Respuesta (escala arbitraria 0-10)
- Barra 1 (A solo): altura ~8
- Barra 2 (A+X): altura ~2
- Muestra reducción en respuesta

Panel B - Prueba de Retardo:
- Eje X: Ensayos de adquisición (1-60)
- Eje Y: Valor Predictivo (-1.0 a 1.0)
- Línea azul (Control Y): aumenta rápido de 0 a ~1.0
- Línea roja (Inhibidor X): aumenta lento de -0.8 a ~1.0
- Cruza 0 mucho después que el control

**Nota**: Un verdadero inhibidor debe pasar ambas pruebas para descartar explicaciones atencionales alternativas.

---

## Parte X: Problemas y Limitaciones del Modelo de Rescorla y Wagner

Ningún modelo es perfecto. A pesar de su enorme éxito, el modelo R-W hace predicciones que no se sostienen empíricamente. Estas "fallas" han sido cruciales para el desarrollo de teorías más completas.

### Problema 1: Extinción No Reduce el Valor a Cero

#### La Predicción del Modelo

En extinción:
- EC se presenta sin SBI
- $R = 0$
- Error $= 0 - V_{EC}$
- $V_{EC}$ disminuye hacia 0

Cuando $V_{EC} = 0$:
- Error $= 0 - 0 = 0$
- No más cambios

**Predicción**: Un estímulo extinguido (V=0) debe ser funcionalmente idéntico a un estímulo neutral (V=0).

#### La Evidencia Empírica Contradice

**Hallazgo 1: Recuperación Espontánea**

Después de extinción completa:
- Pasar tiempo sin exposición
- Probar el EC nuevamente
- **Resultado**: Reaparece respuesta condicionada

Implicación: El valor extinguido no es realmente cero; está "suprimido" pero puede recuperarse.

**Hallazgo 2: Readquisición Rápida**

Comparar dos condiciones:
- Grupo 1: Estímulo neutral A → Refuerzo
- Grupo 2: Estímulo extinguido X → Refuerzo

**Predicción R-W**: Aprendizaje igual (ambos en V=0)

**Resultado**: Grupo 2 aprende **más rápido**

Implicación: El estímulo extinguido "recuerda" su historia, aunque su valor aparente sea cero.

#### Explicaciones Alternativas

Estos hallazgos han motivado teorías que enfatizan:
- **Efectos de contexto**: La extinción es contextual
- **Múltiples estados**: El organismo "infiere" qué "reglas" están vigentes
- **Inhibición activa**: La extinción crea una asociación inhibitoria, no borra la excitatoria

### Problema 2: Inhibición Condicionada No Se Extingue

#### La Predicción del Modelo

Extinguir un inhibidor ($V_X < 0$):
- Presentar X solo (sin SBI)
- $R = 0$
- Ensayo inicial: Error $= 0 - (-0.5) = 0.5$ (positivo)
- $\Delta V_X > 0$
- X debería aumentar hacia 0

**Predicción**: La inhibición debería extinguirse con presentaciones del inhibidor solo.

#### La Evidencia Contradice

**Hallazgo**: Presentar un inhibidor sin consecuencias (sin SBI) **no reduce** su valor inhibitorio.

Ejemplo experimental:
- Fase 1: Crear inhibidor (ej. A+ / AX-)
- Fase 2: Presentar X solo repetidamente
- Fase 3: Probar inhibición con sumación
- **Resultado**: X sigue siendo inhibitorio

#### Análisis del Problema

¿Por qué el modelo falla aquí?

Cuando X se presenta solo:
- No hay excitador presente
- El organismo ya "sabe" que sin excitador, no habrá refuerzo
- No hay violación de expectativa
- No hay información nueva

La inhibición parece requerir **falsación activa**: necesitaríamos presentar X seguido de refuerzo para eliminar su valor inhibitorio.

#### Implicación Teórica

La inhibición puede ser **cualitativamente diferente** de la excitación, no simplemente el extremo negativo de una misma dimensión.

### Problema 3: Inhibición Latente

Este es quizás el problema más importante porque motiva modelos alternativos centrados en atención.

#### El Protocolo

**Grupo Experimental**:
- Fase 1: X solo (sin refuerzo, 60 ensayos)
- Fase 2: X → Refuerzo (60 ensayos)

**Grupo Control**:
- Fase 1: (sin entrenamiento)
- Fase 2: X → Refuerzo (60 ensayos)

#### Predicción de R-W

**Fase 1 (Experimental)**:
- $V_X = 0$ (inicialmente)
- $R = 0$ (sin refuerzo)
- Error $= 0 - 0 = 0$
- $\Delta V_X = 0$
- **Al final**: $V_X = 0$

**Fase 2 (ambos grupos)**:
- Ambos empiezan con $V_X = 0$
- **Predicción**: Aprendizaje idéntico

#### Hallazgo Empírico

**Resultado**: Grupo Experimental aprende **más lento** que Control en Fase 2.

Este fenómeno se conoce como **Inhibición Latente** (latent inhibition).

#### ¿Por Qué el Modelo Falla?

El modelo asume que el parámetro $\beta_X$ (saliencia del estímulo) es **fijo**. 

Pero el hallazgo sugiere que:
- La pre-exposición **reduce** $\beta_X$
- El estímulo "pierde atención"
- El aprendizaje subsecuente es más lento

La pre-exposición sin consecuencias le "enseña" al organismo que X no predice nada importante → reduce atención → retarda aprendizaje futuro.

#### Modelo Alternativo: Pearce y Hall (1980)

Este hallazgo motivó un modelo alternativo que enfatiza cambios en $\beta$ (atención) en lugar de solo cambios en $V$.

**Idea central**: La atención a un estímulo depende de si es seguido de eventos **sorpresivos**.

### Especificación de Figuras 8.7 y 8.8

**Figura 8.7: Inhibición Latente**

**Descripción**:
- Dos fases separadas por línea vertical
- Eje X: Ensayos (Fase 1: 1-60, Fase 2: 61-120)
- Eje Y: Valor Predictivo (0-1.0)
- Línea azul (Grupo Pre-expuesto):
  - Fase 1: plana en 0
  - Fase 2: aumenta *lentamente* a ~1.0
- Línea roja (Grupo Control):
  - Fase 1: sin datos
  - Fase 2: aumenta *rápidamente* a ~1.0

**Nota**: La pre-exposición al estímulo sin refuerzo retarda el aprendizaje subsecuente, violando la predicción de R-W de que ambos grupos deberían aprender igualmente.

**Figura 8.8: No Extinción de Inhibición**

**Descripción**:
- Panel único con tres fases
- Eje X: Ensayos
- Eje Y: Valor Predictivo (-1.0 a 1.0)
- Fase 1 (Creación): $V_X$ disminuye a -0.8
- Fase 2 (Extinción): $V_X$ se mantiene en -0.8 (debería subir según R-W)
- Fase 3 (Prueba de sumación): efecto inhibitorio se mantiene

**Nota**: Presentar el inhibidor solo no reduce su valor inhibitorio, contradiciendo la predicción de R-W de extinción simétrica.

---

## Parte XI: El Modelo de Pearce y Hall - Atención y Sorpresa

El problema de la inhibición latente llevó a Pearce y Hall (1980) a proponer un modelo alternativo que enfatiza **cambios en la atención** en lugar de solo cambios en asociación.

### La Intuición Central

**R-W**: El aprendizaje cambia la **efectividad del refuerzo** (a través del error de predicción).

**Pearce-Hall**: El aprendizaje también cambia la **efectividad del EC** (a través de atención dinámica).

Ambos comparten: El **error de predicción** es el motor, pero opera de manera diferente.

### Formulación del Modelo

El modelo tiene **dos componentes**:

**Ecuación 1**: Cambio en asociación (similar a R-W)

$$V_{t+1} = V_t + \alpha\beta_t\lambda$$

Donde $\lambda$ representa el refuerzo (equivalente a R en R-W).

**Ecuación 2**: Cambio en atención (la innovación)

$$\beta_{t+1} = |\lambda_t - V_{total,t}|$$

¡La atención ($\beta$) en el siguiente ensayo depende del **valor absoluto del error de predicción** en el ensayo actual!

### Diferencias Clave con R-W

| Aspecto | R-W | Pearce-Hall |
|---------|-----|-------------|
| ¿Qué cambia? | Valor (V) | Valor (V) **y** Atención (β) |
| Rol del error | Cambia V | Cambia β |
| β es... | Fijo | Dinámico |
| Énfasis en... | Efectividad del refuerzo | Efectividad del EC |

### Explicación de Inhibición Latente

**Fase 1**: X presentado sin refuerzo
- $\lambda = 0$
- $V_X = 0$
- Error $= |0 - 0| = 0$
- $\beta_{X,t+1} = 0$ → **atención se reduce**

**Fase 2**: X → Refuerzo
- Inicial: $\beta_X \approx 0$ (baja atención)
- Error alto ($|\lambda - 0|$ grande) pero...
- $\beta$ baja implica poco aprendizaje inicialmente
- $\beta$ aumenta gradualmente con los errores

**Grupo Control**:
- Inicial: $\beta_X$ alto (estímulo novedoso)
- Aprendizaje rápido desde el inicio

Resultado: Pre-exposición reduce β → retarda aprendizaje posterior.

### Explicación Alternativa del Bloqueo

**Fase 1**: Tono → Comida
- Error inicial grande → $\beta_{tono}$ alto
- Con aprendizaje: error → 0 → $\beta_{tono}$ → 0

**Fase 2**: Tono + Luz → Comida
- Error $\approx$ 0 (tono ya predice)
- $\beta_{tono} \approx 0$ (bajo porque error fue bajo en Fase 1)
- $\beta_{luz} \approx 0$ (porque error es bajo en compuesto)
- Poco aprendizaje sobre la luz

Explicación: La luz no adquiere **atención** porque aparece cuando no hay sorpresas.

### Comparación de Mecanismos

**R-W explica bloqueo**:
- No hay error de predicción → no hay cambio en V

**Pearce-Hall explica bloqueo**:
- No hay error de predicción → no hay atención → no hay aprendizaje

Ambos predicen el mismo resultado, pero por mecanismos diferentes.

### Implicaciones para Comprensión del Aprendizaje

El aprendizaje requiere **dos ingredientes**:
1. **Atención al EC** (controlado por historia de sorpresas)
2. **Refuerzo** (evento biológicamente importante)

El aprendizaje es el producto de:
$$\text{Aprendizaje} \propto \text{Atención} \times \text{Refuerzo}$$

Sin sorpresas pasadas → sin atención actual → sin aprendizaje futuro.

### Limitaciones de Pearce-Hall

El modelo de Pearce-Hall **no** puede explicar algunos fenómenos que R-W sí explica:

- **Sobreexpectativa**: P-H no predice la reducción de valores
- **Bloqueo en ensayo único**: En algunos casos, un solo ensayo de compuesto puede bloquear
- **Extinción rápida**: P-H predice que la extinción debería ser muy lenta (porque el error es grande inicialmente)

### Modelos Híbridos

La evidencia sugiere que **ambos mecanismos** operan:
- El error de predicción cambia **valores** (R-W)
- El error de predicción cambia **atención** (P-H)

Modelos modernos (ej. Le Pelley, 2004) integran ambos procesos.

### Especificación de Figura 8.9

**Título**: Comparación de Rescorla-Wagner y Pearce-Hall en Inhibición Latente

**Descripción**:
- Dos paneles (uno por modelo)
- Eje X: Ensayos de Fase 2 (adquisición)
- Eje Y izquierdo: V (0-1.0)
- Eje Y derecho: β (0-1.0, solo panel Pearce-Hall)

Panel A - Rescorla-Wagner:
- Línea azul sólida (Pre-expuesto): curva de aprendizaje
- Línea roja sólida (Control): curva de aprendizaje
- **Ambas idénticas** (falla del modelo)

Panel B - Pearce-Hall:
- Línea azul sólida (V pre-expuesto): curva lenta
- Línea roja sólida (V control): curva rápida
- Línea azul punteada (β pre-expuesto): empieza bajo, aumenta gradualmente
- Línea roja punteada (β control): empieza alto
- **Diferencia explicada por β dinámico**

**Nota**: Solo el modelo de Pearce-Hall, con su atención dinámica, puede capturar el efecto de retardo en inhibición latente.

---

## Parte XII: Conclusiones e Integración

### Principios Unificadores: Mecanismos de Ascenso de Colina

En capítulos anteriores exploramos diferentes formas de comportamiento adaptable:
- Comparaciones sucesivas (kinesis, habituación)
- Comparaciones simultáneas (taxis)
- Asignación de crédito (aprendizaje asociativo)

Todos estos fenómenos pueden describirse como instancias de un **modelo general de ascenso de colina basado en reducción de error**.

### El Comparador Universal

La estructura fundamental:

```
Entrada → Comparador → Ajuste de Comportamiento/Valor
            ↑
         Referencia
```

**Diferencias entre mecanismos**:

1. **Qué se compara**:
   - Habituación: Estímulo actual vs. estímulo previo inmediato
   - Aprendizaje: Refuerzo obtenido vs. refuerzo predicho

2. **Fuente de la referencia**:
   - Taxis: Comparación espacial simultánea
   - Habituación: Memoria de corto plazo (ensayo anterior)
   - Aprendizaje: Memoria de largo plazo (valor acumulado V)

3. **Proceso de memoria**:
   - Sin memoria: Taxis
   - Memoria de corto plazo: Habituación
   - Memoria de largo plazo con integración: Aprendizaje

### Rescorla-Wagner como Instancia de Ascenso de Colina

El modelo R-W es un algoritmo de **ascenso de colina** en el espacio de valores predictivos:

**Superficie a escalar**: Precisión de predicción (minimizar error)

**Gradiente**: Error de predicción $(R - V_{total})$

**Paso**: Ponderado por $\alpha\beta$

**Asíntota**: Cumbre local donde error = 0

### Dos Innovaciones Clave de R-W

#### Innovación 1: Competencia (V_total)

**Antes de R-W** (Bush-Mosteller):
- Elementos aprenden independientemente
- $\Delta V_X = \alpha(R - V_X)$

**Con R-W**:
- Elementos comparten un "presupuesto" de valor
- $\Delta V_X = \alpha\beta(R - V_{total})$

Esta simple modificación genera:
- Ensombrecimiento
- Bloqueo
- Sobreexpectativa
- Efectos de contexto

#### Innovación 2: Valores Negativos

**Antes de R-W**:
- V restringido a $[0, \infty)$
- Solo excitación

**Con R-W**:
- V en $(-\infty, +\infty)$
- Excitación **e** inhibición

Permite:
- Inhibidores condicionados
- Señales de seguridad
- Predicción de ausencias

### Extensión: Pearce-Hall

Pearce-Hall agrega una **tercera dimensión dinámica**: atención.

No solo cambia el valor (V), también cambia la receptividad del EC (β).

**Resultado**: Un sistema más flexible que modula no solo *qué* se aprende (V) sino *cuánta atención se presta* (β).

### La Importancia de las "Fallas"

Los problemas del modelo R-W no son fracasos científicos; son **pistas**:

- **Recuperación espontánea** → El aprendizaje es contextual
- **No extinción de inhibición** → Inhibición puede ser cualitativa diferente
- **Inhibición latente** → La atención es dinámica

Cada "falla" ha generado modelos más ricos y comprehensivos.

### Relevancia Contemporánea

El modelo R-W (1972) sigue siendo **fundamental** en:

**Neurociencia**:
- Neuronas dopaminérgicas codifican errores de predicción
- Arquitectura similar en corteza y ganglios basales

**Aprendizaje automático**:
- Temporal Difference (TD) learning es una extensión directa
- Algoritmos de Q-learning y SARSA usan principios idénticos
- Redes neuronales con backpropagation usan descenso de gradiente (minimización de error)

**Psicología clínica**:
- Modelos de ansiedad y trastornos de estrés postraumático
- Protocolos de exposición y prevención de respuesta

### Lecciones Clave

1. **Simplicidad y poder**: Una ecuación simple puede explicar fenómenos complejos
2. **Competencia ubica**: Los recursos limitados generan competencia, que estructura el aprendizaje
3. **Sorpresa es informativa**: Solo los eventos inesperados inducen cambio
4. **Múltiples niveles de plasticidad**: No solo cambian asociaciones (V), también atención (β)
5. **Los modelos evolucionan**: Las "fallas" son oportunidades para entendimiento más profundo

---

## Ejercicios

### Ejercicios Conceptuales

**Ejercicio 1: Distinguiendo Bush-Mosteller de Rescorla-Wagner**

Para cada escenario, indique si el modelo de Bush-Mosteller y el de Rescorla-Wagner hacen predicciones idénticas o diferentes. Si son diferentes, explique por qué.

a) Un tono se presenta 60 veces seguido de comida.

b) Un tono se presenta 60 veces junto con una luz, ambos seguidos de comida.

c) Primero un tono solo se presenta 60 veces con comida; luego el tono junto con una luz se presentan 60 veces con comida.

**Ejercicio 2: Conceptos Clave**

Defina con sus propias palabras:

a) Error de predicción

b) V_total

c) Competencia entre elementos

d) Inhibidor condicionado

e) Ensombrecimiento vs. Bloqueo (¿en qué se diferencian?)

**Ejercicio 3: Análisis de Protocolo**

Considere el siguiente protocolo experimental:

- Fase 1: Tono (T) → Comida (30 ensayos)
- Fase 2: Tono + Luz (TL) → Comida (30 ensayos)
- Fase 3: Tono + Luz + Textura (TLX) → Comida (30 ensayos)

¿Qué predice el modelo R-W sobre el valor adquirido por la textura (X)? Explique el razonamiento.

**Ejercicio 4: Inhibición Condicionada**

Explique por qué un inhibidor condicionado:
a) Solo puede formarse en presencia de un excitador
b) No se extingue fácilmente con presentaciones del estímulo solo
c) Debe pasar dos pruebas (sumación y retardo) para confirmarse

**Ejercicio 5: Aplicación Cotidiana**

Piense en una situación de su vida donde haya experimentado:
a) Bloqueo (algo que no aprendió porque ya sabía otra cosa)
b) Inhibición latente (algo que tardó en aprender por familiaridad previa)

Describa cada situación y explique cómo R-W o Pearce-Hall lo explicaría.

### Ejercicios Cuantitativos

**Ejercicio 6: Cálculo Básico**

Dados los siguientes parámetros:
- $\alpha = 0.3$
- $\beta_{tono} = 0.5$
- $\beta_{luz} = 0.3$
- $R = 1$

Situación: Un tono y una luz se presentan juntos (compuesto), seguidos de comida.

Estado inicial:
- $V_{tono} = 0$
- $V_{luz} = 0$

Calcule:
a) $V_{total}$ en el ensayo 1
b) El error de predicción en el ensayo 1
c) $\Delta V_{tono}$ en el ensayo 1
d) $\Delta V_{luz}$ en el ensayo 1
e) $V_{tono}$ y $V_{luz}$ después del ensayo 1

**Ejercicio 7: Bloqueo Cuantitativo**

Parámetros:
- $\alpha = 0.25$
- $\beta_{tono} = 0.4$
- $\beta_{luz} = 0.4$
- $R = 1$

Protocolo:
- Fase 1: Tono solo → Comida (suficientes ensayos para que $V_{tono} = 1.0$)
- Fase 2: Tono + Luz → Comida

Calcule para el **primer ensayo de Fase 2**:
a) $V_{total}$ inicial
b) Error de predicción
c) $\Delta V_{luz}$
d) ¿Por qué la luz no aprende?

**Ejercicio 8: Sobreexpectativa**

Parámetros:
- $\alpha = 0.2$
- $\beta$ = 0.5 para ambos estímulos
- $R = 1$

Fase 1 (entrenamientos separados hasta asíntota):
- Tono → Comida: $V_{tono} = 1.0$
- Luz → Comida: $V_{luz} = 1.0$

Calcule para el **primer ensayo de Fase 2** (Tono + Luz → Comida):
a) $V_{total}$
b) Error de predicción (nótese el signo)
c) $\Delta V_{tono}$
d) $\Delta V_{luz}$
e) Después de este ensayo, ¿aumentaron o disminuyeron los valores?

**Ejercicio 9: Creando un Inhibidor**

Parámetros:
- $\alpha = 0.3$
- $\beta_T = 0.5$ (tono)
- $\beta_L = 0.5$ (luz)

Fase 1: Tono → Comida (hasta $V_{tono} = 1.0$)

Fase 2: Tono + Luz → Sin comida

Para el **primer ensayo de Fase 2**:
a) $V_{total}$ (inicial)
b) $R$
c) Error de predicción
d) $\Delta V_{luz}$
e) Nuevo $V_{luz}$ después del ensayo

**Ejercicio 10: Simulación Multi-Ensayo**

Simule 10 ensayos del siguiente protocolo:

Parámetros: $\alpha = 0.2$, $\beta = 0.5$, $R = 1$

Protocolo: Tono solo → Comida

Complete la tabla:

| Ensayo | V_inicial | Error | ΔV | V_final |
|--------|-----------|-------|-----|---------|
| 1 | 0 | | | |
| 2 | | | | |
| ... | | | | |
| 10 | | | | |

Grafique V vs. Ensayo. ¿Qué patrón observa?

### Ejercicios de Programación

**Ejercicio 11: Simulador Básico de R-W**

Escriba una función que implemente el modelo de Rescorla-Wagner:

```python
def rescorla_wagner(n_trials, alpha, beta, R, V_initial=0):
    """
    Simula el aprendizaje de R-W para un solo estímulo.
    
    Parámetros:
    -----------
    n_trials : int
        Número de ensayos
    alpha : float
        Parámetro de asociabilidad del refuerzo
    beta : float
        Parámetro de saliencia del estímulo
    R : float or list
        Refuerzo (escalar o lista de valores por ensayo)
    V_initial : float
        Valor inicial del estímulo
        
    Retorna:
    --------
    V_history : list
        Historia de valores en cada ensayo
    """
    # Su código aquí
    pass
```

Pruebe su función con:
- 60 ensayos
- α = 0.2, β = 0.5
- R = 1 (constante)
- V inicial = 0

Grafique la curva de aprendizaje.

**Ejercicio 12: Simulador de Compuestos**

Extienda el simulador para manejar dos estímulos en compuesto:

```python
def rw_compound(n_trials, alpha, beta1, beta2, R, V1_initial=0, V2_initial=0):
    """
    Simula aprendizaje R-W para un compuesto de dos estímulos.
    
    Retorna:
    --------
    V1_history, V2_history : lists
        Historias de valores de cada estímulo
    """
    # Su código aquí
    pass
```

Use esta función para simular ensombrecimiento:
- 60 ensayos
- α = 0.2
- β1 = 0.4 (tono, más saliente)
- β2 = 0.2 (luz, menos saliente)

Grafique ambas curvas en la misma figura. Añada una línea para V_total.

**Ejercicio 13: Simulador de Bloqueo**

Implemente una simulación de bloqueo con dos fases:

```python
def blocking_simulation(n_phase1, n_phase2, alpha, beta_A, beta_X, R):
    """
    Simula el protocolo de bloqueo.
    
    Fase 1: A → R (n_phase1 ensayos)
    Fase 2: AX → R (n_phase2 ensayos)
    
    Retorna:
    --------
    phase1_VA, phase2_VA, phase2_VX : lists
        Historias de valores
    """
    # Su código aquí
    pass
```

Compare con un grupo control (sin Fase 1) en la misma gráfica.

**Ejercicio 14: Contingencia y Contexto**

Simule el efecto de contingencia usando el contexto como estímulo:

Condición verdaderamente correlacionada:
- Con EC: EC + Contexto → R (siempre)
- Sin EC: Contexto solo → R (50% de ensayos)

Condición no correlacionada:
- Con EC: EC + Contexto → R (50% de ensayos)
- Sin EC: Contexto solo → R (50% de ensayos)

Implemente ambas condiciones y grafique V_EC y V_Contexto para cada una.

**Ejercicio 15: Inhibición Condicionada**

Simule la creación de un inhibidor condicionado:

Fase 1: A → R (30 ensayos)
Fase 2: 
- A → R (15 ensayos intercalados)
- AX → No R (15 ensayos intercalados)

Grafique V_A y V_X a lo largo de ambas fases. V_X debería volverse negativo.

**Ejercicio 16: Modelo de Pearce-Hall**

Implemente el modelo básico de Pearce-Hall:

```python
def pearce_hall(n_trials, alpha, beta_initial, lam):
    """
    Simula el modelo de Pearce-Hall.
    
    Parámetros:
    -----------
    beta_initial : float
        Atención inicial al estímulo
    lam : float or list
        Refuerzo (equivalente a R)
        
    Retorna:
    --------
    V_history, beta_history : lists
        Historias de valor y atención
    """
    V = 0
    beta = beta_initial
    V_history = [V]
    beta_history = [beta]
    
    for trial in range(n_trials):
        # Su código aquí
        # Actualice V usando beta actual
        # Actualice beta usando error absoluto
        pass
    
    return V_history, beta_history
```

Simule inhibición latente:
- Grupo pre-expuesto: 60 ensayos sin R, luego 60 con R
- Grupo control: solo 60 ensayos con R

Compare las curvas de aprendizaje y las curvas de atención.

### Ejercicios Integradores

**Ejercicio 17: Diseño Experimental**

Diseñe un experimento que permita distinguir empíricamente entre las predicciones del modelo de Rescorla-Wagner y el de Pearce-Hall.

Especifique:
a) Protocolo detallado
b) Predicción de R-W
c) Predicción de Pearce-Hall
d) Qué resultados apoyarían cada modelo

**Ejercicio 18: Aplicación Clínica**

Un paciente desarrolla aversión a la comida del hospital después de quimioterapia (náusea):

a) Modele este escenario con R-W. ¿Qué elementos podrían adquirir valor?
b) ¿Cómo podría el contexto hospitalario contribuir?
c) Diseñe un protocolo de extinción informado por el modelo.
d) ¿Por qué podría haber recuperación espontánea de la aversión?

**Ejercicio 19: Análisis de Artículo**

Lea uno de los artículos seminales:

- Rescorla, R.A., & Wagner, A.R. (1972). A theory of Pavlovian conditioning.
- Pearce, J.M., & Hall, G. (1980). A model for Pavlovian learning.

Identifique:
a) Problema empírico que motiva el modelo
b) Supuestos clave del modelo
c) Predicción novedosa más importante
d) Una limitación reconocida por los autores

**Ejercicio 20: Extensión Teórica**

Proponga una modificación al modelo R-W que podría resolver uno de sus problemas (extinción, no-extinción de inhibición, o inhibición latente).

Especifique:
a) Qué componente modificaría
b) Cómo quedaría la ecuación modificada
c) Cómo esta modificación resolvería el problema
d) Qué nuevas predicciones generaría

---

## Especificaciones de Figuras Adicionales

### Figura 8.10: Resumen de Fenómenos Explicados por R-W

**Descripción**:
- Diagrama de flujo o tabla visual
- 5 paneles pequeños, uno por fenómeno:
  1. Condicionamiento simple (V aumenta a R)
  2. Ensombrecimiento (dos elementos comparten valor)
  3. Bloqueo (elemento pre-entrenado bloquea nuevo)
  4. Sobreexpectativa (suma excede R, valores disminuyen)
  5. Inhibición (valor negativo)

Cada panel muestra:
- Protocolo esquemático (arriba)
- Predicción gráfica (abajo)

**Título**: Cinco fenómenos clave explicados por el modelo de Rescorla-Wagner

### Figura 8.11: Comparación Bush-Mosteller vs. R-W

**Descripción**:
- Dos paneles lado a lado
- Mismo protocolo en ambos: TL → R (compuesto)
- Panel A (Bush-Mosteller):
  - Dos curvas independientes
  - Ambas alcanzan R ≈ 1.0
- Panel B (Rescorla-Wagner):
  - Dos curvas interdependientes
  - V_tono > V_luz
  - V_total ≈ 1.0

**Título**: Diferencia fundamental: independencia (B-M) vs. competencia (R-W)

### Figura 8.12: Diagrama Conceptual del Modelo R-W

**Descripción**:
- Diagrama de bloques mostrando flujo de información:
  1. Inputs: EC₁, EC₂, ..., ECₙ (con β asociadas)
  2. Bloque suma: Σ Vi → V_total
  3. Comparador: R - V_total → Error
  4. Multiplicador: Error × α × βᵢ → ΔVᵢ
  5. Actualización: Vi,new = Vi,old + ΔVi
  6. Loop de retroalimentación

**Título**: Arquitectura computacional del modelo de Rescorla-Wagner

### Figura 8.13: Espacio de Parámetros α y β

**Descripción**:
- Gráfica de contorno 2D
- Eje X: α (0 a 1)
- Eje Y: β (0 a 1)
- Líneas de contorno muestran velocidad de aprendizaje (αβ)
- Ejemplos marcados:
  - Punto A: α=0.1, β=0.5 (refuerzo débil, EC saliente)
  - Punto B: α=0.5, β=0.1 (refuerzo fuerte, EC poco saliente)
  - Punto C: α=0.5, β=0.5 (ambos moderados)

**Título**: Velocidad de aprendizaje como función de α (refuerzo) y β (saliencia del EC)

---

## Notas Técnicas

### Nota Técnica 1: Convergencia Matemática

El modelo R-W garantiza convergencia bajo ciertas condiciones.

**Para un solo estímulo**:

$$V_{t+1} = V_t + \alpha\beta(R - V_t)$$
$$V_{t+1} = (1 - \alpha\beta)V_t + \alpha\beta R$$

Esta es una ecuación de diferencia lineal de primer orden. La solución es:

$$V_t = R(1 - (1-\alpha\beta)^t)$$

Cuando $t \to \infty$ y $0 < \alpha\beta < 1$:

$$V_{\infty} = R$$

**Para compuestos** (dos elementos A y B):

Asíntota cuando error = 0:
$$R = V_A + V_B$$

Pero la distribución específica entre A y B depende de la historia de entrenamiento y las β relativas. No hay solución única analítica sin especificar el protocolo completo.

### Nota Técnica 2: Relación con Descenso de Gradiente

El modelo R-W puede verse como descenso de gradiente sobre una función de error cuadrática.

**Función de error**:
$$E = \frac{1}{2}(R - V_{total})^2$$

**Gradiente respecto a Vi**:
$$\frac{\partial E}{\partial V_i} = -(R - V_{total})$$

**Actualización por descenso de gradiente**:
$$\Delta V_i = -\eta \frac{\partial E}{\partial V_i} = \eta(R - V_{total})$$

Donde η es la tasa de aprendizaje.

Comparando con R-W:
$$\Delta V_i = \alpha\beta_i(R - V_{total})$$

Vemos que $\alpha\beta_i$ juega el papel de la tasa de aprendizaje, pero específica para cada elemento.

### Nota Técnica 3: Estabilidad del Sistema

Para un sistema con n elementos, la matriz de actualización es:

$$\mathbf{V}_{t+1} = \mathbf{V}_t + \boldsymbol{\alpha}\boldsymbol{\beta}(R - \mathbf{1}^T\mathbf{V}_t)$$

Donde:
- $\mathbf{V}_t$ es un vector nx1 de valores
- $\boldsymbol{\alpha}\boldsymbol{\beta}$ es un vector nx1 de tasas de aprendizaje
- $\mathbf{1}$ es un vector de unos

El sistema es estable (converge) si todos los eigenvalues de la matriz de iteración tienen magnitud < 1.

Para el caso simple, esto se reduce a requerir:
$$0 < \alpha\beta_i < 2$$

Típicamente, $\alpha, \beta \in (0,1)$ garantiza convergencia.

### Nota Técnica 4: Extensiones del Modelo

**Modificación de Mackintosh (1975)**: Atención inversa

$$\beta_{t+1} = \beta_t + \gamma(|R - V_x| - |R - V_{total}|)$$

La atención aumenta si el estímulo es mejor predictor que otros.

**Modificación de Le Pelley (2004)**: Híbrido

Combina cambios de atención estilo Pearce-Hall (aumenta con sorpresa) y Mackintosh (aumenta con relevancia predictiva).

**TD-learning (Sutton & Barto)**: Predicción temporal

$$\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$

Donde el error considera no solo refuerzo inmediato sino valor futuro descontado.

---

## Lecturas Recomendadas

### Artículos Fundacionales

**Esencial** (lectura obligatoria):
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement. In A. H. Black & W. F. Prokasy (Eds.), *Classical Conditioning II: Current Research and Theory* (pp. 64-99). Appleton-Century-Crofts.

**Muy recomendado**:
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning: Variations in the effectiveness of conditioned but not of unconditioned stimuli. *Psychological Review, 87*(6), 532-552.

### Revisiones y Síntesis

- Miller, R. R., Barnet, R. C., & Grahame, N. J. (1995). Assessment of the Rescorla-Wagner model. *Psychological Bulletin, 117*(3), 363-386.
  - *Evaluación comprehensiva de éxitos y limitaciones del modelo*

- Siegel, S., & Allan, L. G. (1996). The widespread influence of the Rescorla-Wagner model. *Psychonomic Bulletin & Review, 3*(3), 314-321.
  - *Impacto del modelo en múltiples áreas*

- Le Pelley, M. E. (2004). The role of associative history in models of associative learning: A selective review and a hybrid model. *Quarterly Journal of Experimental Psychology, 57B*(3), 193-243.
  - *Integración de modelos de atención*

### Evidencia Empírica Clave

**Bloqueo**:
- Kamin, L. J. (1968). "Attention-like" processes in classical conditioning. In M. R. Jones (Ed.), *Miami Symposium on the Prediction of Behavior: Aversive Stimulation* (pp. 9-31). University of Miami Press.
  - *El descubrimiento original del bloqueo*

**Sobreexpectativa**:
- Kremer, E. F. (1978). The Rescorla-Wagner model: Losses in associative strength in compound conditioned stimuli. *Journal of Experimental Psychology: Animal Behavior Processes, 4*(1), 22-36.

- Rescorla, R. A. (2006). Deepened extinction from compound stimulus presentation. *Journal of Experimental Psychology: Animal Learning and Cognition, 32*(2), 135-144.

**Inhibición latente**:
- Lubow, R. E., & Moore, A. U. (1959). Latent inhibition: The effect of nonreinforced pre-exposure to the conditional stimulus. *Journal of Comparative and Physiological Psychology, 52*(4), 415-419.
  - *Descubrimiento original del fenómeno*

**Contingencia**:
- Rescorla, R. A. (1968). Probability of shock in the presence and absence of CS in fear conditioning. *Journal of Comparative and Physiological Psychology, 66*(1), 1-5.
  - *Demostración clásica de que la contigüidad no es suficiente*

### Neurociencia y Implementación

- Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science, 275*(5306), 1593-1599.
  - *Neuronas dopaminérgicas codifican errores de predicción al estilo R-W*

- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.
  - *Capítulos 6 y 7: TD-learning como extensión de R-W*

- Niv, Y., & Schoenbaum, G. (2008). Dialogues on prediction errors. *Trends in Cognitive Sciences, 12*(7), 265-272.
  - *Puente entre modelos computacionales y neurobiología*

### Aplicaciones Clínicas

- Craske, M. G., Treanor, M., Conway, C. C., Zbozinek, T., & Vervliet, B. (2014). Maximizing exposure therapy: An inhibitory learning approach. *Behaviour Research and Therapy, 58*, 10-23.
  - *Aplicación de principios de aprendizaje asociativo a tratamiento de ansiedad*

- Bouton, M. E. (2002). Context, ambiguity, and unlearning: Sources of relapse after behavioral extinction. *Biological Psychiatry, 52*(10), 976-986.
  - *Relevancia de contexto para extinción clínica*

### Textos Avanzados

- Pearce, J. M. (2008). *Animal Learning and Cognition: An Introduction* (3rd ed.). Psychology Press.
  - *Capítulos 3-5: Tratamiento comprehensivo de R-W y alternativas*

- Bouton, M. E. (2016). *Learning and Behavior: A Contemporary Synthesis* (2nd ed.). Sinauer Associates.
  - *Capítulos 4-5: Contexto moderno del modelo*

### Recursos Computacionales

- McLaren, I. P. L., & Mackintosh, N. J. (2000). An elemental model of associative learning: I. Latent inhibition and perceptual learning. *Animal Learning & Behavior, 28*(3), 211-246.
  - *Implementación computacional detallada*

- Simulation tools:
  - *Sniffy, the Virtual Rat* (software educativo para simular R-W)
  - Código Python en: https://github.com/SussilloDavid/rw-model

---

## Glosario de Términos

**Asociabilidad (α, β)**: Parámetros que determinan la velocidad de aprendizaje. α captura propiedades del refuerzo, β del estímulo condicionado.

**Bloqueo (Blocking)**: Fenómeno donde el aprendizaje previo de un elemento impide el aprendizaje de un elemento nuevo en compuesto.

**Competencia**: Proceso por el cual elementos de un compuesto "compiten" por un valor predictivo limitado.

**Contingencia**: Relación probabilística entre eventos; diferencia entre P(R|EC) y P(R|~EC).

**Ensombrecimiento (Overshadowing)**: Fenómeno donde un elemento más saliente reduce el aprendizaje de un elemento menos saliente en un compuesto.

**Error de predicción**: Discrepancia entre refuerzo obtenido (R) y refuerzo esperado (V_total); motor del aprendizaje.

**Inhibición condicionada**: Proceso por el cual un estímulo adquiere valor negativo y predice la ausencia de refuerzo.

**Inhibición latente**: Retardo en el aprendizaje causado por pre-exposición al EC sin refuerzo.

**Prueba de retardo**: Test para inhibición condicionada; el supuesto inhibidor debería tardar más en adquirir valor excitatorio.

**Prueba de sumación**: Test para inhibición condicionada; el supuesto inhibidor debería reducir la respuesta a un excitador cuando se presentan juntos.

**Recuperación espontánea**: Reaparición de respuesta condicionada extinguida después del paso del tiempo.

**Saliencia**: Propiedad del EC que determina cuánta atención recibe (capturada por β).

**Separabilidad**: Supuesto de que estímulos compuestos se procesan como conjuntos de elementos independientes.

**Sobreexpectativa**: Fenómeno donde la suma de valores excede el refuerzo disponible, causando reducción de valores.

**V_total**: Suma de los valores predictivos de todos los elementos presentes simultáneamente.

**Valor predictivo (V)**: Número asociado a un elemento que representa su capacidad de predecir refuerzo (positivo) o su ausencia (negativo).

---

## Reflexión Final

El modelo de Rescorla y Wagner representa uno de los logros más significativos de la psicología del aprendizaje del siglo XX. Su elegancia matemática, poder explicativo, y capacidad de generar predicciones contraintuitivas lo han mantenido vigente por más de 50 años.

Pero quizás su contribución más profunda es conceptual: nos enseñó que el aprendizaje no es una simple registración de contigüidades, sino un proceso activo de construcción de modelos predictivos del mundo. Los organismos no aprenden asociaciones ciegamente; extraen estructura causal de experiencias complejas, compitiendo explicaciones alternativas unas contra otras.

Esta visión del aprendizaje como **inferencia** sobre estructura causal ha influenciado campos tan diversos como neurociencia cognitiva, aprendizaje automático, economía conductual, y psicología clínica. El principio del error de predicción como motor de cambio aparece una y otra vez, desde neuronas dopaminérgicas hasta algoritmos de deep learning.

Las limitaciones del modelo no son fracasos, sino invitaciones a teorizar más profundamente. Nos han llevado a considerar:
- La plasticidad de la atención (Pearce-Hall)
- La importancia del contexto (Bouton)
- Múltiples sistemas de memoria (Wagner)
- Inferencia Bayesiana sobre estructura causal (modelos contemporáneos)

En última instancia, Rescorla y Wagner nos dieron no solo un modelo matemático, sino una forma de pensar sobre cómo los organismos extraen sentido de un mundo complejo e incierto. Y esa forma de pensar continúa evolucionando, enriquecida por evidencia empírica, implementación neurobiológica, y formalización computacional.

El viaje desde la simple ley de contigüidad de Pavlov hasta los modelos contemporáneos de aprendizaje e inferencia es un testimonio del poder del método científico: observación cuidadosa, formalización matemática, predicción y prueba, refinamiento iterativo. Cada "falla" del modelo ha sido un paso hacia comprensión más profunda.

Como estudiantes de comportamiento adaptable, llevamos con nosotros no solo ecuaciones y protocolos, sino una apreciación por la complejidad de los procesos que permiten a los organismos navegar y prosperar en entornos cambiantes. El modelo de Rescorla y Wagner es un hito en ese viaje de comprensión, no el destino final, sino un faro que ilumina el camino hacia adelante.

---

**Fin del Capítulo 8**