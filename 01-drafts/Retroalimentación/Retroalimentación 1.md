# # Capítulo 5: Taxias y Sistemas de Retroalimentación
## Comparación Simultánea y el Poder de los Lazos Cerrados

## Introducción

En el capítulo anterior vimos cómo organismos muy simples pueden navegar gradientes de recursos mediante **comparación sucesiva**: comparar el presente con el pasado inmediato y ajustar el comportamiento en consecuencia. La bacteria compara la concentración *ahora* versus *hace un momento* y decide si seguir nadando o cambiar de dirección.

Pero hay otra forma fundamental de resolver problemas de navegación y orientación: la **comparación simultánea**. En lugar de comparar el mismo punto del espacio en dos tiempos diferentes, el organismo compara *dos puntos diferentes del espacio al mismo tiempo*. Esto requiere receptores bilaterales—ojos, antenas, sensores químicos—colocados en lados opuestos del cuerpo.

Este capítulo introduce el segundo "tornillo y tuerca" en nuestro cajón de herramientas: los **sistemas de retroalimentación**. Son mecanismos elegantes donde el comportamiento no solo responde al entorno, sino que simultáneamente *modifica* el entorno que lo controla, creando un lazo cerrado de interdependencia. John Dewey tenía razón: la unidad fundamental de análisis no es el estímulo ni la respuesta aislados, sino la **relación dinámica entre organismo y entorno**.

Los sistemas de retroalimentación son ubicuos en biología—desde la regulación de temperatura corporal hasta el seguimiento visual de objetos en movimiento—y reaparecerán de formas cada vez más sofisticadas cuando abordemos el aprendizaje. Más importante aún, al final del capítulo veremos que los sistemas de retroalimentación *por sí solos* tienen una limitación crítica: solo pueden responder *después* de detectar un error. Esto nos llevará naturalmente a la necesidad de mecanismos que puedan **anticipar** el futuro—el tema central del aprendizaje asociativo.

---

## Parte I: El Problema Adaptativo

### El Desafío de la Orientación

Imagina ser una polilla nocturna volando en la oscuridad. Detectas el olor de flores con néctar en algún lugar cercano, pero ¿en qué dirección exactamente? O eres una cucaracha que detecta luz—señal de peligro que indica un depredador potencial—y necesitas alejarte lo más rápido posible. ¿Cómo te orientas hacia o en contra de una fuente de estimulación sin un "mapa" del entorno?

**El problema adaptativo fundamental**: Localizar y orientarse hacia (o alejarse de) una fuente de estimulación espacialmente localizada que es importante para la supervivencia.

### Variantes del Problema

Este problema tiene múltiples variantes según el tipo de estímulo:

**Fototaxia**: Orientación hacia o alejándose de luz
- Polillas volando hacia llamas (fototaxia positiva)
- Cucarachas huyendo de la luz (fototaxia negativa)  
- Larvas de moscas evitando exposición lumínica

**Quimiotaxia**: Orientación hacia o alejándose de gradientes químicos
- Insectos localizando feromonas sexuales
- Bacterias navegando hacia nutrientes (ya vimos esto en Cap. 4, pero con mecanismo diferente)

**Fonotaxia**: Orientación hacia o alejándose de sonidos
- Grillos machos localizando cantos de hembras
- Murciélagos usando ecolocalización

**Termotaxia**: Orientación hacia o alejándose de temperatura
- Serpientes detectando presas de sangre caliente
- Insectos buscando microclimas óptimos

En todos estos casos, el organismo debe resolver el mismo problema computacional: **¿en qué dirección está la fuente?**

### Restricciones del Sistema

A diferencia del ascenso de colina que vimos en el capítulo anterior, el comportamiento de taxias tiene una ventaja crítica:

**1. Receptores bilaterales**: El organismo tiene dos receptores espacialmente separados (ojos izquierdo y derecho, antenas, sensores químicos en ambos lados del cuerpo).

**2. Comparación espacial directa**: Puede comparar la intensidad de estimulación *simultáneamente* en ambos lados del cuerpo, no solo sucesivamente en el tiempo.

**3. Direccionalidad inmediata**: La *diferencia* en estimulación entre receptores codifica directamente la dirección de la fuente.

Pero también tiene restricciones:

**4. Información local**: Solo sabe sobre el gradiente *en su ubicación actual*, no sobre el campo completo.

**5. Ambigüedad en fuentes múltiples**: Si hay múltiples fuentes, el comportamiento puede ser subóptimo.

**6. Requiere gradiente estable**: En entornos muy turbulentos, las señales pueden ser demasiado ruidosas.

---

## Parte II: El Comportamiento Observado

### Caso 1: Polillas y la Llama Fatal

Las polillas nocturnas muestran un comportamiento icónico: vuelan directamente hacia fuentes de luz artificial, a menudo con consecuencias fatales cuando la fuente es una llama. Este es un ejemplo dramático de **fototaxia positiva**.

**Comportamiento observado en laboratorio**:

**Configuración**: Una polilla liberada en una habitación oscura con una sola fuente de luz (lámpara).

**Patrón de vuelo**: La polilla no vuela en línea recta hacia la luz. En cambio, muestra una **trayectoria espiral** que gradualmente converge hacia la fuente.

**Detalle crucial**: Si se cubre uno de los ojos compuestos de la polilla (con pintura opaca, por ejemplo), el comportamiento cambia dramáticamente: la polilla vuela en **círculos continuos** en lugar de aproximarse a la luz.

**Interpretación**: El comportamiento normal depende de comparar la intensidad lumínica detectada por ambos ojos simultáneamente. Cuando solo un ojo funciona, la comparación siempre favorece ese lado, resultando en giro continuo.

### Caso 2: Cucarachas Huyendo de la Luz

Las cucarachas muestran el patrón opuesto: **fototaxia negativa**. Cuando se enciende una luz, corren rápidamente alejándose de la fuente.

**Experimento clásico** (Fraenkel & Gunn, 1940):

**Configuración**: Cucarachas en una arena circular con una lámpara en un borde.

**Resultado**: Las cucarachas se acumulan en el lado opuesto a la lámpara, habiendo corrido en trayectorias que las alejan de la fuente lumínica.

**Variante experimental**: Si se les cubre un ojo, las cucarachas corren en círculos (dirección opuesta al ojo funcional), alejándose inicialmente pero eventualmente dando vueltas sin escape efectivo.

**Nota fascinante**: La dirección del giro depende de *cuál* ojo se cubre. Ojo izquierdo cubierto → giro hacia la derecha. Ojo derecho cubierto → giro hacia la izquierda.

### Caso 3: Cochinillas Entre Dos Luces

Un experimento particularmente revelador involucra presentar *dos* fuentes de luz equidistantes:

**Configuración**: Una cochinilla (isópodo terrestre) colocada exactamente a mitad de camino entre dos lámparas de igual intensidad.

**Predicción del mecanismo**: Si el comportamiento está controlado por comparación bilateral, la cochinilla debería moverse en **línea recta** entre ambas fuentes (donde la estimulación de ambos ojos es igual).

**Resultado observado**: Exactamente eso. La cochinilla corre en línea recta hasta acercarse mucho a una de las fuentes, momento en el que la proximidad rompe la simetría y la cochinilla gira bruscamente hacia esa fuente.

**¿Por qué línea recta?** Porque mientras ambas fuentes están equidistantes, la diferencia en estimulación entre ojos izquierdo y derecho es **cero**. No hay señal de error que indique "girar a la izquierda" o "girar a la derecha", entonces el organismo simplemente avanza recto.

Este resultado es evidencia directa de que la taxia está controlada por la **disparidad bilateral en estimulación**, no por la intensidad absoluta.

### El Patrón General: Trayectorias Espirales

Un patrón común emerge de estos estudios: cuando hay una sola fuente y el organismo parte de una posición angular con respecto a ella, la trayectoria no es una línea recta sino una **espiral logarítmica** que converge hacia (fototaxia positiva) o diverge de (fototaxia negativa) la fuente.

**¿Por qué espiral?**

La magnitud del giro es proporcional al ángulo entre la dirección del organismo y la fuente. Cuanto mayor el ángulo, mayor la disparidad bilateral, mayor el giro. A medida que el organismo se orienta hacia la fuente, el ángulo disminuye, la disparidad disminuye, el giro se hace más sutil, resultando en una aproximación progresivamente más directa—la forma matemática de esto es una espiral.

---

## Parte III: El Mecanismo—Sistemas de Retroalimentación

### Qué es un Sistema de Retroalimentación

Un **sistema de retroalimentación** es una configuración donde:

1. El **comportamiento** (output del organismo) es una función de alguna **variable del entorno** (input al organismo)
2. **Simultáneamente**, ese comportamiento **modifica** la variable del entorno
3. Creando un **lazo cerrado**: comportamiento → entorno → comportamiento → entorno...

**Diagrama conceptual**:

```
         ┌─────────────────────────────┐
         │                             │
         ▼                             │
    ENTORNO (X)  ─────────►  ORGANISMO │
         │                      │      │
         │                      ▼      │
         │                 Comportamiento (Y)
         │                             │
         └─────────────────────────────┘
              (Comportamiento modifica X)
```

**Contraste con sistema abierto**:

En un sistema **abierto** (sin retroalimentación):
- El comportamiento responde al entorno
- Pero el comportamiento *no altera* la variable del entorno que lo controla

Ejemplo: Una planta que cierra sus hojas al detectar vibración (respuesta sísmica). El cierre de hojas no cambia las vibraciones en el entorno—es una respuesta "abierta".

Ejemplo: La respuesta balística de una rana capturando una mosca. El lengüetazo se ejecuta completamente sin corrección durante su trayectoria.

### Componentes de un Sistema de Retroalimentación

Todo sistema de retroalimentación tiene los siguientes elementos:

#### 1. Sensor / Receptor
Detecta el valor actual de la variable de interés.

**En fototaxia**: Los dos ojos compuestos que detectan intensidad lumínica.

#### 2. Comparador
Computa la diferencia entre:
- Un **valor deseado** (set point) 
- El **valor actual** detectado por el sensor

**En fototaxia**: Un circuito neural que resta la activación del ojo izquierdo de la del ojo derecho (o viceversa). El resultado es la **señal de error**.

Señal de error = Estimulación(ojo derecho) - Estimulación(ojo izquierdo)

Si error > 0 → Fuente está a la derecha
Si error < 0 → Fuente está a la izquierda  
Si error = 0 → Fuente está directamente al frente (o no hay fuente)

#### 3. Controlador (Función de Control)
Transforma la señal de error en un comportamiento.

**En fototaxia**: 
- Tasa de giro = k × (señal de error)

Donde k es una constante de sensibilidad. Si k es grande, pequeñas disparidades producen giros grandes. Si k es pequeño, se requieren grandes disparidades para generar giros.

En **fototaxia positiva**: k > 0 (giras hacia el lado con mayor estimulación)
En **fototaxia negativa**: k < 0 (giras alejándote del lado con mayor estimulación)

#### 4. Efector / Actuador
El sistema motor que ejecuta el comportamiento.

**En fototaxia**: Los músculos de las alas o patas que producen el giro.

#### 5. Función de Retroalimentación (Entorno)
Describe cómo el comportamiento modifica la variable del entorno.

**En fototaxia**: 
- Un giro cambia el ángulo θ entre el organismo y la fuente
- El cambio en θ cambia la disparidad bilateral en estimulación
- Porque la geometría determina cuánta luz llega a cada ojo

**Ejemplo numérico**:
- Fuente de luz fija en posición (10, 10)
- Polilla en posición (0, 0), orientación θ = 45°
- Ojo derecho recibe más luz (está más cerca de 10,10)
- Señal de error > 0
- Polilla gira a la derecha, digamos 5°
- Nuevo θ = 40°
- Nueva disparidad bilateral (menor que antes)
- Nueva señal de error (menor que antes)
- Nuevo giro (menor que antes)
- ...y así sucesivamente hasta θ ≈ 0

### Tipos de Sistemas de Retroalimentación

Hay dos tipos fundamentales:

#### Retroalimentación Negativa
El comportamiento **reduce** la señal de error.

**Características**:
- Conduce al sistema hacia un **punto de equilibrio**
- Es **auto-corregible**: perturbaciones son contrarrestadas
- Típico en sistemas de **regulación** y **seguimiento**

**Ejemplos biológicos**:
- Fototaxia positiva (reduce disparidad hasta orientarse hacia luz)
- Termorregulación (sudoración reduce temperatura corporal)
- Regulación de glucosa en sangre (insulina reduce niveles altos)
- Control postural (ajustes musculares corrigen desviaciones)

**Diagrama de flujo**:
```
Error grande → Comportamiento fuerte → Error se reduce → Comportamiento se debilita → ...
```

El sistema se **estabiliza** en el punto donde error = 0.

#### Retroalimentación Positiva
El comportamiento **aumenta** la señal de error.

**Características**:
- **Amplifica** desviaciones en lugar de corregirlas
- Conduce a cambios **explosivos** o **runaway**
- Típicamente **inestable** (no alcanza equilibrio)
- Útil para transiciones rápidas entre estados

**Ejemplos biológicos**:
- Potencial de acción neuronal (entrada de Na+ abre más canales de Na+)
- Contracciones durante parto (oxitocina aumenta contracciones, contracciones liberan más oxitocina)
- Coagulación sanguínea (cada factor activa más del siguiente)
- Pánico en multitudes (cada persona corriendo induce a más personas a correr)

**En el contexto de taxias**: Un sistema de fototaxia con retroalimentación positiva sería uno donde el organismo gira *alejándose* de la luz cuando detecta disparidad, pero su giro *aumenta* la disparidad en lugar de reducirla. Esto generaría giros acelerados hasta que el organismo pierde completamente la señal. No es adaptativo para orientación, pero podría serlo para escape rápido.

### Regulación vs. Servomecanismos

Hay una distinción útil entre dos clases de sistemas de retroalimentación:

#### Regulación
El **set point** (valor deseado) es **interno** al organismo y típicamente fijo.

**Ejemplo**: Termorregulación en mamíferos
- Set point = 37°C (determinado fisiológicamente)
- Sensor = Termorreceptores en hipotálamo
- Error = 37° - Temperatura actual
- Controlador = Si error > 0 (demasiado frío) → tiritar, vasoconstricción
                Si error < 0 (demasiado caliente) → sudar, vasodilatación

**Objetivo**: Mantener una variable fisiológica en un rango estrecho a pesar de perturbaciones externas.

#### Servomecanismo
El **set point** es **externo** y puede ser **variable**.

**Ejemplo**: Fototaxia
- Set point = "disparidad bilateral = 0" (orientación directa hacia fuente)
- Pero la *ubicación* de la fuente puede cambiar
- Si la fuente se mueve, el set point efectivo se mueve
- El organismo debe *seguir* el objetivo móvil

**Ejemplo tecnológico**: Misil teledirigido
- Set point = posición del avión objetivo (¡está moviéndose!)
- Sensor = Radar que detecta posición del avión
- Error = Posición objetivo - Posición del misil
- Controlador = Ajusta aletas para reducir error
- El avión se mueve → nuevo error → nuevo ajuste → ...

Los servomecanismos son fundamentales para comportamiento de **seguimiento** (pursuit, tracking). El organismo no solo busca un estado fijo, sino que *persigue* un objetivo dinámico.

---

## Parte IV: Formalización Matemática

### El Sistema de Ecuaciones Acopladas

Un sistema de retroalimentación se describe mediante dos ecuaciones que operan simultáneamente:

**Ecuación 1: Función de Control (Organismo)**

Y = G(X)

Donde:
- Y = Comportamiento (ej: tasa de giro)
- X = Variable del entorno (ej: disparidad bilateral)
- G = Función de control (cómo el organismo transforma X en Y)

**Ecuación 2: Función de Retroalimentación (Entorno)**

X = E(Y)

Donde:
- E = Función de retroalimentación (cómo el comportamiento Y modifica la variable X)

**El lazo cerrado**: Y depende de X, pero X depende de Y. No son independientes—están **acopladas**.

### Caso Específico: Fototaxia Simple

Hagamos esto concreto con fototaxia:

**Variables**:
- θ(t) = Ángulo entre dirección del organismo y fuente de luz en tiempo t
- ω(t) = Tasa de giro (velocidad angular) en tiempo t
- I_L(t), I_R(t) = Intensidad lumínica en ojo izquierdo y derecho

**Función de Control**:

ω(t) = k × [I_R(t) - I_L(t)]

Donde k > 0 para fototaxia positiva, k < 0 para fototaxia negativa.

**Función de Retroalimentación**:

La disparidad bilateral depende del ángulo θ. Si la fuente está a distancia d constante:

I_R(t) ≈ I₀ × [1 + α×sin(θ)]
I_L(t) ≈ I₀ × [1 - α×sin(θ)]

Donde:
- I₀ = Intensidad promedio
- α = Constante geométrica (depende de separación entre ojos)
- Sin(θ) captura cómo el ángulo afecta cuál ojo está "más cerca" de la fuente

Entonces:
I_R - I_L ≈ 2×I₀×α×sin(θ)

Sustituyendo en la función de control:

ω(t) = k × 2×I₀×α×sin(θ)

Simplificando con una constante combinada K = k×2×I₀×α:

**ω(t) = K×sin(θ)**

Finalmente, el giro cambia el ángulo:

**dθ/dt = -ω(t) = -K×sin(θ)**

(El signo negativo aparece porque un giro a la derecha *reduce* el ángulo θ)

### Análisis de Equilibrio

Un **equilibrio** es un estado donde las variables dejan de cambiar.

En nuestro sistema, esto ocurre cuando dθ/dt = 0, es decir:

-K×sin(θ) = 0

Soluciones:
- θ = 0° (organismo apunta directamente hacia la fuente)
- θ = 180° (organismo apunta directamente *alejándose* de la fuente)
- θ = ±360°, ±720°, ... (equivalentes a 0° y 180° por periodicidad)

**¿Cuál equilibrio es estable?**

- **θ = 0°**: Si el organismo se desvía ligeramente (digamos θ = 5°), entonces sin(5°) > 0, entonces ω > 0, entonces el organismo gira de vuelta hacia 0°. Es un **equilibrio estable** (atractor).

- **θ = 180°**: Si el organismo se desvía ligeramente (digamos θ = 175°), entonces sin(175°) > 0, entonces el organismo gira *alejándose* de 180°, no hacia él. Es un **equilibrio inestable** (repulsor).

**Interpretación biológica**: El sistema de fototaxia positiva converge naturalmente hacia orientación directa (θ = 0°) y repele orientación opuesta. Esto es exactamente lo que queremos para aproximarse a la fuente.

### Dinámica: Trayectorias Hacia el Equilibrio

¿Cómo evoluciona θ(t) a lo largo del tiempo?

Podemos resolver la ecuación diferencial:

dθ/dt = -K×sin(θ)

Para condiciones iniciales θ(0) = θ₀, la solución no tiene forma cerrada simple, pero podemos **simularla numéricamente** o analizar cualitativamente.

**Análisis cualitativo**:

**Caso 1: θ₀ pequeño** (digamos 10°)
- sin(θ₀) es pequeño → dθ/dt es pequeño → cambio gradual
- θ decae hacia 0° lentamente

**Caso 2: θ₀ moderado** (digamos 45°)  
- sin(45°) ≈ 0.707 → dθ/dt es sustancial → cambio más rápido
- θ decae hacia 0° más rápidamente que en Caso 1

**Caso 3: θ₀ grande** (digamos 85°)
- sin(85°) ≈ 0.996 → dθ/dt es muy grande → cambio muy rápido
- θ decae hacia 0° muy rápidamente inicialmente, luego se desacelera cerca del equilibrio

**Patrón general**: La tasa de corrección es mayor cuando el error es grande, y se vuelve más sutil cerca del equilibrio. Esto produce **convergencia asintótica**: el sistema se acerca cada vez más al equilibrio pero técnicamente nunca lo alcanza en tiempo finito (en la práctica, llega a "suficientemente cerca").

### Simulador Conceptual (Pseudocódigo)

```python
# Parámetros
K = 1.0          # Constante de control
dt = 0.01        # Paso de tiempo
T_max = 10       # Tiempo total de simulación

# Condiciones iniciales
theta = 60       # Ángulo inicial (grados)
time = 0

# Simulación
while time < T_max:
    # Función de control
    omega = K * sin(theta * pi/180)  # Convertir a radianes
    
    # Actualización de ángulo (integración de Euler)
    theta = theta - omega * dt
    
    # Avanzar tiempo
    time = time + dt
    
    # Registrar para graficar
    print(time, theta)
```

**Resultado esperado**: θ decae exponencialmente desde 60° hacia 0°, con mayor tasa de cambio inicialmente.

---

## Parte V: Propiedades de los Sistemas de Retroalimentación

### Ventaja 1: Auto-Corrección ante Perturbaciones

Una propiedad poderosa de la retroalimentación negativa: el sistema **corrige automáticamente** perturbaciones externas.

**Ejemplo**: Una polilla está volando hacia una fuente de luz (θ ≈ 0°) cuando una ráfaga de viento la desvía (θ salta a 20°).

**Sin retroalimentación**: La polilla continuaría en la dirección perturbada indefinidamente.

**Con retroalimentación**: 
- Nuevo θ = 20° genera nuevo error
- Error genera giro correctivo
- Polilla retorna hacia θ = 0°
- ¡Perturbación es compensada sin "decisión" explícita!

Esto hace que el comportamiento sea **robusto**: funciona a pesar de variabilidad e impredecibilidad en el entorno.

### Ventaja 2: Independencia de Parámetros del Controlador

Otra propiedad notable: el **equilibrio** (hacia dónde converge el sistema) es independiente de la magnitud de K en la función de control.

**Demostración**:
- Con K = 1.0, el equilibrio es θ = 0°
- Con K = 0.5 (respuesta más débil), el equilibrio *sigue siendo* θ = 0°
- Con K = 2.0 (respuesta más fuerte), el equilibrio *sigue siendo* θ = 0°

**Lo que cambia**: La **velocidad** con la que se alcanza el equilibrio.
- K grande → convergencia rápida (pero posible oscilación si K es *demasiado* grande)
- K pequeño → convergencia lenta (pero suave)

**Implicación biológica**: Un organismo joven con músculos débiles (K pequeño) y uno adulto con músculos fuertes (K grande) ambos alcanzarán la fuente de luz, solo que a diferentes velocidades. El sistema es robusto ante variación individual en fuerza de respuesta.

### Ventaja 3: Seguimiento de Objetivos Móviles

Cuando el set point es externo y variable (servomecanismo), el sistema puede **seguir** cambios en el objetivo.

**Ejemplo**: La fuente de luz se mueve lentamente de izquierda a derecha.

**Comportamiento del sistema**:
- Inicialmente θ = 0° (orientado hacia fuente)
- Fuente se mueve → θ ya no es 0° → genera error
- Error genera giro hacia nueva posición
- Si la fuente se mueve lentamente, el sistema *rastrea* continuamente, manteniendo θ ≈ 0°

**Límite**: Si la fuente se mueve *demasiado rápido*, el sistema no puede seguir el ritmo. Hay un **ancho de banda** limitado—el sistema puede seguir cambios lentos pero no cambios arbitrariamente rápidos.

### Limitación 1: Respuesta Solo *Después* del Error

**Problema crítico**: Un sistema de retroalimentación puro solo responde *después* de detectar un error. No puede anticipar.

**Ejemplo problemático**: Imagina que la fuente de luz se apaga súbitamente.

**Respuesta del sistema**:
- Error salta a cero (no hay disparidad bilateral)
- ω = 0 (sin giro)
- El organismo continúa en línea recta en cualquier dirección que estaba moviéndose
- No hay "búsqueda" activa de la fuente perdida

Otro ejemplo: Un depredador persiguiendo presa con retroalimentación pura siempre va *hacia donde la presa está ahora*, no *hacia donde estará*. Si la presa hace un giro brusco, el depredador debe esperar a detectar el nuevo error antes de ajustar—siempre va un paso atrás.

### Limitación 2: Inestabilidad con Demoras

Si hay **demoras** significativas entre detección de error y ejecución de respuesta, el sistema puede volverse inestable.

**Ejemplo**: Imagina que el circuito neural que procesa la disparidad bilateral toma 100 ms. Durante esos 100 ms, el organismo sigue girando basándose en información *antigua*.

**Consecuencia**: El organismo puede "sobrepasar" (overshoot) el objetivo, generando un error en la dirección opuesta, luego sobrepasar nuevamente, resultando en **oscilaciones** alrededor del equilibrio en lugar de convergencia suave.

**Analogía cotidiana**: Ajustar la temperatura de la regadera. Si hay mucha demora entre que giras la perilla y sientes el cambio de temperatura, tiendes a sobrecompensar ("¡demasiado fría! [gira mucho hacia caliente] ...¡demasiado caliente! [gira mucho hacia fría]...") resultando en oscilaciones molestas.

**Solución biológica**: Evolucionar procesamiento neural rápido para minimizar demoras. O evolucionar mecanismos de **amortiguamiento** que reduzcan la ganancia K cuando se detecta oscilación.

### Limitación 3: Máximos Locales con Fuentes Múltiples

Con múltiples fuentes, el sistema puede quedar "atrapado" en un equilibrio sub-óptimo.

**Ejemplo**: Dos fuentes de luz, una débil pero cercana (Fuente A), otra intensa pero lejana (Fuente B).

**Comportamiento posible**:
- Organismo se orienta hacia Fuente A (más cercana)
- Alcanza equilibrio (θ_A ≈ 0°)
- Aunque Fuente B es más intensa, el sistema no "sabe" buscarla porque ya está en equilibrio local
- Resultado: El organismo se queda en la fuente sub-óptima

Esto es análogo al problema de máximos locales que vimos en ascenso de colina. Los sistemas de retroalimentación pura no tienen mecanismo de "exploración" que permita escapar equilibrios locales para buscar mejores alternativas.

---

## Parte VI: Comparación con Ascenso de Colina

Es instructivo contrastar los dos mecanismos que hemos visto:

| Característica | Ascenso de Colina (Cap. 4) | Taxias/Retroalimentación (Cap. 5) |
|----------------|---------------------------|----------------------------------|
| **Tipo de comparación** | Sucesiva (ahora vs. antes) | Simultánea (derecha vs. izquierda) |
| **Receptores necesarios** | Uno solo | Bilaterales (dos) |
| **Información espacial directa** | No (solo gradiente local) | Sí (dirección inmediata) |
| **Velocidad de convergencia** | Lenta (trayectoria sinuosa) | Rápida (trayectoria casi directa) |
| **Necesita memoria** | Sí (valor previo) | No (comparación instantánea) |
| **Adaptación sensorial** | Sí (evita estancamiento) | No necesario |
| **Robustez ante perturbaciones** | Moderada | Alta |
| **Aplicabilidad** | Universal (cualquier gradiente) | Requiere simetría bilateral |

**Cuándo es mejor ascenso de colina**:
- Organismos sin receptores bilaterales (bacterias, organismos unicelulares)
- Gradientes químicos turbulentos donde comparación simultánea sería ruidosa
- Cuando se requiere mecanismo simple (mínima complejidad neural)

**Cuándo es mejor retroalimentación (taxias)**:
- Organismos con receptores bilaterales (casi todos los animales)
- Fuentes estacionarias o lentamente móviles
- Cuando se requiere convergencia rápida (escape de depredadores, captura de presa)

**Uso combinado**: Muchos organismos usan *ambos* mecanismos en diferentes contextos. Una bacteria podría usar ascenso de colina para gradientes químicos (sin sentido direccional claro) pero taxias para gradientes de luz si tiene fotorreceptores bilaterales.

---

## Parte VII: Extensión Crítica—Anticipación y Predicción

### El Problema Fundamental de los Sistemas Reactivos

Todo lo que hemos visto hasta ahora—ascenso de colina y sistemas de retroalimentación—son mecanismos **reactivos**. Responden a condiciones actuales:

- Ascenso de colina: "¿La concentración mejoró *ahora* comparado con *antes*?"
- Retroalimentación: "¿La disparidad *ahora* indica error?"

Pero el mundo biológico está lleno de situaciones donde reaccionar al presente **no es suficiente**. Necesitas **anticipar** el futuro.

### Casos donde la Reactividad Falla

**Caso 1: Seguimiento de Presas Móviles**

Un halcón persiguiendo un ratón que corre en zigzag. Si el halcón usa retroalimentación pura:
- Detecta posición del ratón *ahora*
- Ajusta vuelo hacia esa posición
- Pero para cuando llega, el ratón ya se movió
- El halcón siempre va *hacia donde el ratón estaba*, no *hacia donde estará*

**Solución requerida**: Predecir la trayectoria futura del ratón basándose en su velocidad y dirección, y volar hacia el **punto de intercepción predicho**.

**Caso 2: Preparación ante Eventos Futuros**

Un animal que necesita almacenar comida para el invierno. Si usa retroalimentación pura:
- Detecta abundancia de comida *ahora* (verano)
- Come hasta saciarse
- No hay error, no hay ajuste
- El invierno llega → hambruna

**Solución requerida**: Usar señales presentes (días acortándose, temperatura bajando) como **predictores** de futuras condiciones (escasez invernal), y ajustar comportamiento *ahora* (almacenar comida) basándose en esa predicción.

**Caso 3: Evitar Costos de Demora**

En muchos contextos, hay un **costo** asociado con demoras en la respuesta. Ejemplos:
- Un organismo que espera hasta estar *muy* deshidratado para buscar agua podría no encontrarla a tiempo
- Un depredador que espera hasta estar *muy* hambriento para cazar tiene menos energía para la caza
- Un estudiante que espera hasta la *víspera* del examen para estudiar... bueno, ya sabes

**Solución requerida**: **Anticipar** la necesidad futura y actuar *antes* de que se vuelva crítica.

### De Retroalimentación a Predicción: El Modelo Interno

La limitación fundamental de la retroalimentación pura es que solo mira *hacia atrás* (estado actual vs. deseado) sin mirar *hacia adelante* (estado futuro probable).

Para superar esto, los organismos necesitan desarrollar **modelos internos del mundo**—representaciones de cómo el entorno funciona—que permitan **simulación mental** de futuros posibles.

**Componentes de un modelo interno**:

1. **Representación del estado actual**: ¿Dónde estoy? ¿Qué está pasando ahora?

2. **Modelo de transición**: ¿Si hago X, cómo cambiará el mundo? (Física intuitiva, teoría de la mente del depredador/presa)

3. **Simulación hacia adelante**: Ejecutar mentalmente el modelo: "Si corro hacia el norte, el depredador me cortará el camino... mejor corro hacia el este donde hay cobertura"

4. **Evaluación de consecuencias**: ¿Ese futuro simulado es bueno o malo para mí? (Predicción de recompensa/castigo)

5. **Selección de acción**: Elegir la acción cuya consecuencia futura predicha es mejor.

### Retroalimentación Predictiva

Una extensión sofisticada es combinar retroalimentación con predicción:

**Sistema tradicional**:
- Error = Estado deseado - Estado actual
- Respuesta basada en error actual

**Sistema predictivo**:
- Error predicho = Estado deseado - Estado futuro estimado
- Respuesta basada en error *futuro anticipado*

**Ejemplo concreto**: Control motor en humanos lanzando una pelota a una canasta.

**Sin predicción**:
- Ejecutas movimiento
- Observas trayectoria de pelota
- Detectas error ("va muy a la izquierda")
- Ajustas próximo lanzamiento
- Este es **aprendizaje por ensayo-error**—lento y costoso

**Con predicción**:
- Antes de soltar pelota, tu cerebelo **simula** la trayectoria basándose en modelo interno de física y tu fuerza muscular actual
- Predices "con esta fuerza, irá muy a la izquierda"
- **Ajustas antes de lanzar**
- Resultado: Precisión mucho mayor desde primeros intentos

Este tipo de control se llama **control anticipatorio** o **feedforward control**, y es fundamental en habilidades motoras expertas.

### El Puente hacia el Aprendizaje Asociativo

Y aquí llegamos al punto crucial que conecta este capítulo con el resto del curso:

**¿Cómo adquieren los organismos modelos internos que permiten predicción?**

**Respuesta**: A través del **aprendizaje asociativo**.

El aprendizaje asociativo es fundamentalmente sobre descubrir **relaciones predictivas** en el mundo:
- Ciertos eventos (estímulos condicionados, EC) **predicen** otros eventos (estímulos incondicionados, EI)
- Ciertas acciones en ciertos contextos **predicen** ciertas consecuencias (recompensas, castigos)

**Ejemplo clásico—Condicionamiento Pavloviano**:
- Tono (EC) → 5 segundos → Comida (EI)
- Después de varios emparejamientos, el perro **anticipa** la comida cuando escucha el tono
- La salivación ya no es solo una respuesta **reactiva** a la comida, sino una respuesta **predictiva** al tono que señala comida futura

**Ejemplo operante—Ratas y palancas**:
- Presionar palanca → 1 segundo → Comida
- La rata aprende que presionar **predice** comida
- El comportamiento cambia de exploratorio a dirigido hacia la meta, **anticipando** la recompensa

En ambos casos, el organismo está construyendo un modelo: "X predice Y". Esto le permite **actuar en anticipación** de Y, no solo reaccionar cuando Y ocurre.

### Sistemas de Retroalimentación que Incorporan Predicción

Los sistemas más sofisticados combinan ambos elementos:

**Lazo 1: Retroalimentación Clásica (Correctiva)**
- Detecta error actual
- Corrige desviaciones que ya ocurrieron
- Garantiza estabilidad

**Lazo 2: Anticipación Basada en Aprendizaje (Predictiva)**
- Usa señales tempranas para predecir errores futuros
- Ajusta antes de que el error se materialice
- Mejora eficiencia

**Ejemplo integrado—Control de temperatura corporal avanzado**:

**Solo retroalimentación**:
- Temperatura baja → tiritar
- Espera hasta que hace frío para reaccionar

**Con aprendizaje predictivo**:
- Asociación aprendida: "Viento frío → temperatura bajará pronto"
- Al detectar viento frío, **antes** de que baje temperatura corporal, el organismo aumenta metabolismo anticipadamente
- Previene el problema en lugar de solo reaccionar

**Ejemplo integrado—Persecución de presa**:

**Solo retroalimentación**:
- Depredador va hacia posición actual de presa
- Siempre va un paso atrás

**Con aprendizaje predictivo**:
- El depredador aprende patrones de movimiento típicos ("cuando persigo conejos, suelen girar bruscamente cada 5 segundos")
- Anticipa el giro y ajusta trayectoria *antes* de que ocurra
- Intercepta en lugar de simplemente seguir

---

## Parte VIII: Formalizando la Extensión Predictiva

### Modelo de Retroalimentación con Predicción a Un Paso

Podemos extender nuestro modelo matemático para incluir predicción simple:

**Sistema básico** (reactivo):
```
Error(t) = SetPoint - X(t)
Y(t) = G(Error(t))
```

**Sistema predictivo** (un paso hacia adelante):
```
X_predicho(t+1) = X(t) + f(X(t), contexto)
Error_predicho(t) = SetPoint - X_predicho(t+1)
Y(t) = G(Error_predicho(t))
```

Donde `f(X(t), contexto)` es un **modelo aprendido** de cómo cambia X.

**Ejemplo—Seguimiento de presa móvil**:

X(t) = posición de presa en tiempo t
f(X(t)) = velocidad actual de presa (asumiendo movimiento constante)

Predicción simple:
X_predicho(t+1) = X(t) + velocidad(t) × Δt

El depredador ajusta su comportamiento basándose en dónde *estará* la presa, no dónde *está*.

### Predicción Multi-Paso y Horizonte Temporal

Sistemas más sofisticados pueden predecir múltiples pasos hacia adelante:

```
X_predicho(t+1) = X(t) + f₁(X(t))
X_predicho(t+2) = X_predicho(t+1) + f₂(X_predicho(t+1))
X_predicho(t+3) = X_predicho(t+2) + f₃(X_predicho(t+2))
...
```

**Problema**: Cada paso adicional acumula **error de predicción**. Predecir el futuro muy lejano es inherentemente incierto.

**Solución biológica**: Balancear entre:
- **Horizonte corto** (pocas predicciones hacia adelante): Más preciso pero menos preparado
- **Horizonte largo** (muchas predicciones hacia adelante): Más preparado pero menos preciso

Diferentes comportamientos requieren diferentes horizontes:
- Capturar presa rápida: Horizonte de ~1 segundo
- Almacenar comida para invierno: Horizonte de ~meses
- Planificación humana: Horizonte de años (pero con enorme incertidumbre)

---

## Conclusión: El Camino Adelante

### Lo que Lograste en Este Capítulo

Has dominado el segundo "tornillo y tuerca" fundamental:

1. **Comparación simultánea** mediante receptores bilaterales como forma de extraer información direccional del entorno

2. **Sistemas de retroalimentación** como mecanismo general donde comportamiento y entorno se influyen mutuamente en un lazo cerrado

3. **Equilibrios y dinámica** de estos sistemas—cómo convergen hacia estados estables y responden a perturbaciones

4. **Ventajas** de la retroalimentación (auto-corrección, robustez) y **limitaciones** (solo reactiva, no anticipatoria)

5. **La necesidad crítica de predicción** para superar limitaciones de sistemas puramente reactivos

### Por Qué Este Capítulo es el Puente Crucial

Este capítulo cierra el **Bloque 0: Fundamentos de Mecanismos Sin Aprendizaje** y establece explícitamente **por qué necesitamos aprendizaje**.

**Recapitulación del argumento**:

**Capítulo 3 (Selección Natural)**: Los organismos están moldeados por presiones evolutivas para maximizar supervivencia y reproducción. Pero la evolución es lenta—opera a escala filogenética.

**Capítulo 4 (Ascenso de Colina)**: Para entornos variables dentro de la vida del organismo, evolucionan mecanismos de adaptación rápida sin necesidad de historia experiencial. Pero son limitados—solo navegan gradientes locales sin "saber" a dónde van.

**Capítulo 5 (Retroalimentación)**: Con receptores bilaterales, los organismos obtienen información direccional y pueden usar retroalimentación para aproximarse eficientemente a objetivos. Pero siguen siendo **reactivos**—responden a lo que está pasando *ahora*, no anticipan lo que pasará *después*.

**La limitación compartida**: Ninguno de estos mecanismos puede **aprender de la experiencia para predecir y anticipar** eventos futuros.

Y esa es precisamente la función del aprendizaje asociativo, que abordaremos en los próximos capítulos.

### Adelante: El Problema de la Asignación de Crédito

Imagina este problema:

Un organismo realiza múltiples acciones en una secuencia compleja. Al final, recibe una recompensa (encuentra comida) o un castigo (encuentra depredador).

**Pregunta crucial**: ¿Cuál de las acciones (o señales ambientales) en esa secuencia fue **responsable** del resultado? ¿A cuál asignarle "crédito" (si hubo recompensa) o "culpa" (si hubo castigo)?

**Ejemplos del problema**:
- Una rata presiona palanca, gira en círculo, presiona palanca otra vez, lame el piso, luego aparece comida. ¿Qué causó la comida?
- Un niño come desayuno, juega con un perro, toca una planta, luego le sale un sarpullido. ¿Qué causó la alergia?
- Un estudiante lee el libro, asiste a clase, hace los ejercicios, platica con compañeros, luego saca buena calificación. ¿Qué contribuyó al éxito?

Este es el **problema de la asignación de crédito**, y es el tema central de los próximos cinco capítulos (Bloques I y II del curso).

Los mecanismos que verás—condicionamiento Pavloviano, aprendizaje instrumental, modelos de reducción de error—son todas soluciones a este problema fundamental: **¿Qué predice qué?** y **¿Qué acción causa qué consecuencia?**

Una vez que entiendas cómo se resuelve la asignación de crédito, entenderás cómo los organismos construyen modelos internos del mundo que permiten **predicción, anticipación, y planeación**—las capacidades que distinguen sistemas que solo reaccionan de sistemas que genuinamente aprenden.

---

## Ejercicios de Reflexión

**1. Identificando Tipo de Sistema**

Para cada comportamiento, identifica si es:
- (A) Ascenso de colina (comparación sucesiva)
- (B) Taxias (comparación simultánea)  
- (C) Retroalimentación con set point interno (regulación)
- (D) Retroalimentación con set point externo (servomecanismo)
- (E) Sistema abierto (sin retroalimentación)

a) Un murciélago ajusta la dirección de su vuelo basándose en diferencias de tiempo entre llegada de eco en ambos oídos
b) Una planta cierra sus hojas cuando detecta vibración (respuesta sísmica)
c) Un humano mantiene su temperatura corporal en 37°C mediante sudoración/tiritona
d) Un caracol navega hacia humedad mayor comparando su situación actual vs. hace un minuto
e) Una mosca robótica sigue una línea negra en el piso usando dos fotosensores, uno a cada lado

**2. Análisis de Equilibrio**

Considera un sistema de retroalimentación donde:
- Y(t) = 3 × [10 - X(t)]  (función de control)
- X(t+1) = X(t) + 0.5 × Y(t)  (función de retroalimentación)

a) ¿Cuál es el equilibrio del sistema?
b) Si X(0) = 5, ¿X aumentará o disminuirá?
c) Si X(0) = 15, ¿X aumentará o disminuirá?
d) ¿Es el equilibrio estable o inestable?

**3. Diseñando Comportamiento Adaptativo**

Eres ingeniero robótico diseñando un robot que debe:
- Moverse por un almacén oscuro
- Localizar una estación de carga que emite luz infrarroja
- Aproximarse y conectarse para recargar baterías

**Preguntas**:
a) ¿Qué sensores necesita el robot?
b) ¿Usarías ascenso de colina, taxias, o ambos? ¿Por qué?
c) ¿Qué es la señal de error en tu sistema?
d) ¿Qué ocurre si hay múltiples estaciones de carga?
e) ¿Cómo harías el sistema robusto ante que alguien mueva la estación mientras el robot se aproxima?

**4. Predicción vs. Reacción**

Para cada escenario, identifica si un sistema puramente reactivo (retroalimentación) sería suficiente, o si se requiere predicción/anticipación. Justifica.

a) Un termostato manteniendo la temperatura de una casa
b) Un portero de fútbol atajando un tiro penal
c) Un ave migratoria preparándose para el invierno
d) Un sistema de piloto automático en un avión manteniendo altitud
e) Un humano decidiendo si llevar paraguas basándose en nubes en el cielo

**5. Extensión Creativa**

El capítulo mencionó que organismos necesitan "anticipar el futuro" para superar limitaciones de retroalimentación pura.

Diseña un ejemplo concreto de tu vida cotidiana donde:
- Identificas una señal temprana X
- Que predice un evento futuro Y
- Y ajustas tu comportamiento Z *antes* de que Y ocurra
- De forma que evitas un costo o obtienes un beneficio

Especifica: ¿Cómo aprendiste que X predice Y? ¿Cuántos emparejamientos X→Y fueron necesarios? ¿Alguna vez X falló en predecir Y (falsa alarma)?

---

## Lecturas Recomendadas

### Esenciales

- **Fraenkel, G. S., & Gunn, D. L. (1961).** *The Orientation of Animals: Kineses, Taxes and Compass Reactions*. Dover.
  - El tratado clásico sobre taxias. Capítulos 2-4 son particularmente accesibles.

- **Braitenberg, V. (1984).** *Vehicles: Experiments in Synthetic Psychology*. MIT Press.
  - Una joya. Muestra cómo comportamientos sorprendentemente complejos emergen de sistemas de retroalimentación simples.

- **Powers, W. T. (1973).** *Behavior: The Control of Perception*. Aldine.
  - Argumento radical: todo comportamiento es control de percepción mediante retroalimentación. Controversial pero influyente.

### Profundización Técnica

- **Ashby, W. R. (1956).** *An Introduction to Cybernetics*. Chapman & Hall.
  - Fundamentos matemáticos de sistemas de retroalimentación. Capítulos 1-3 son suficientes para este curso.

- **Wiener, N. (1948).** *Cybernetics: Or Control and Communication in the Animal and the Machine*. MIT Press.
  - El libro que fundó el campo. Denso pero históricamente importante.

### Aplicaciones Modernas

- **Webb, B. (2001).** "Can robots make good models of biological behaviour?" *Behavioral and Brain Sciences*, 24, 1033-1050.
  - Cómo robots basados en retroalimentación simple replican comportamientos de insectos.

- **Bialek, W. (2012).** *Biophysics: Searching for Principles*. Princeton. [Capítulo 4]
  - Sistemas de retroalimentación en biología molecular y celular. Más avanzado pero excelente.

---

**Fin del Capítulo 5**

En el próximo capítulo comenzamos el **Bloque I: Asignación de Crédito** con una introducción al condicionamiento Pavloviano y el problema central: cuando múltiples eventos preceden una recompensa o castigo, ¿cómo determina el organismo cuál(es) son predictivos y cuál(es) son irrelevantes?
