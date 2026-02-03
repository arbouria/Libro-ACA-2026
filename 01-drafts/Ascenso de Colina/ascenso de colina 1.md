# # Capítulo 4: Ascenso de Colina
## Un Mecanismo de Adaptación Sin Aprendizaje

## Introducción

En el capítulo anterior vimos cómo la selección natural opera a escala filogenética para producir comportamiento adaptado. Pero ¿qué ocurre cuando un organismo debe adaptarse a variaciones impredecibles en su entorno *durante su vida individual*, sin poder recurrir al aprendizaje que integra experiencias pasadas?

Este capítulo introduce el primer "tornillo y tuerca" en nuestro cajón de herramientas de la adaptación: el **ascenso de colina** (*hill climbing*). Es un mecanismo elegantemente simple que permite a organismos muy básicos—incluso sin sistema nervioso—navegar eficientemente hacia recursos en entornos variables. Más importante aún, es un algoritmo de propósito general que reaparecerá una y otra vez en formas más sofisticadas cuando abordemos el aprendizaje propiamente dicho.

La estrategia pedagógica de este capítulo sigue una progresión que usaremos repetidamente a lo largo del curso:

1. **El problema adaptativo**: ¿Qué desafío enfrenta el organismo?
2. **El comportamiento observado**: ¿Cómo lo resuelve empíricamente?
3. **El algoritmo**: ¿Qué reglas o pasos generan ese comportamiento?
4. **La formalización**: ¿Cómo expresamos esas reglas matemáticamente?

Esta progresión te permite entender *por qué* necesitamos modelos formales: no son abstracciones gratuitas, sino herramientas para capturar con precisión los principios que operan en sistemas reales.

---

## El Problema Adaptativo

### El Desafío Fundamental

Incluso los organismos más simples—bacterias, plantas, amebas—enfrentan un problema biológico fundamental: **localizar y acceder a fuentes de energía distribuidas de forma variable e impredecible en el espacio**.

Una bacteria nadando en un medio acuoso, una planta verde buscando luz solar, una ameba (como la *Dictyostelium* o "salmonela", una de nuestras "mascotas nacionales" en el laboratorio) moviéndose hacia nutrientes químicos—todos comparten un desafío: ¿cómo moverse hacia una concentración mayor de aquello que necesitan, sin saber de antemano dónde está?

Este es un problema particularmente difícil para organismos que carecen de **receptores de distancia**—órganos sensoriales que permiten detectar recursos a la distancia, como la visión o el olfato en mamíferos. Sin estos receptores, el organismo no puede simplemente "ver" dónde está la comida y dirigirse hacia ella. Solo puede detectar si la concentración de nutrientes en su ubicación actual es mayor o menor que hace un momento.

### Restricciones del Sistema

El problema se complica por varias restricciones:

**1. Información local únicamente**: El organismo solo tiene acceso a información sobre su posición actual y, mediante memoria, su posición inmediatamente anterior. No tiene un "mapa" del entorno ni puede comparar simultáneamente múltiples ubicaciones distantes.

**2. Ruido sensorial**: La detección de cambios en concentración no es perfecta. Fluctuaciones aleatorias pueden hacer que una zona parezca momentáneamente mejor o peor de lo que realmente es.

**3. Tiempo y energía finitos**: Cada movimiento consume energía y tiempo. El organismo no puede explorar indefinidamente—debe encontrar un balance entre buscar y aprovechar lo que encuentra.

**4. Gradientes múltiples**: En entornos complejos puede haber múltiples fuentes de nutrientes. El organismo podría quedarse "atascado" en una fuente pequeña cercana, sin alcanzar una fuente mayor más alejada (el problema de los **máximos locales**).

Este problema no es exclusivo de organismos simples. Es el mismo desafío que enfrenta un robot explorando un terreno desconocido, un algoritmo de optimización buscando la mejor solución en un espacio de posibilidades, o incluso tú cuando buscas señal de wifi caminando por un edificio desconocido.

---

## El Comportamiento Observado

### Caso 1: Plantas Verdes y el Fototropismo

Las plantas verdes enfrentan una competencia feroz por la luz solar. Una plántula germinando en el suelo del bosque debe crecer hacia la luz, esquivando obstáculos—otras plantas, rocas—que bloquean su acceso al sol.

**Comportamiento observado**: Las plantas muestran tres comportamientos básicos coordinados:

1. **Rotación**: El tallo puede rotar, "barriendo" diferentes direcciones
2. **Crecimiento direccional**: Una vez que detecta mayor intensidad lumínica en una dirección, crece preferentemente hacia ese lado (fototropismo)
3. **Crecimiento vertical**: Simultáneamente, crece hacia arriba, alejándose del suelo

La combinación de estos tres comportamientos simples resulta en trayectorias sorprendentemente eficientes hacia la luz, incluso cuando ésta proviene de direcciones cambiantes o hay obstáculos en el camino.

### Caso 2: La Salmonela Navegando Gradientes Químicos

La bacteria *Salmonella* es notablemente exitosa en localizar alimento. En un experimento clásico, se introduce una pipeta capilar conteniendo nutrientes en agua con salmonelas nadando libremente. Después de algunos minutos, hay significativamente más bacterias *dentro* de la pipeta que afuera—las bacterias "encontraron" la fuente de alimento.

**¿Cómo lo hacen sin cerebro, sin ojos, sin mapa?**

La observación detallada del comportamiento de salmonelas individuales revela un patrón característico:

**Comportamiento 1: Maromas aleatorias** (*tumbling*)
- La bacteria gira sobre sí misma en direcciones aleatorias
- Esto reorienta su dirección de nado sin desplazamiento neto
- Es esencialmente **exploración**: muestrear diferentes direcciones

**Comportamiento 2: Nado en línea recta** (*running*)
- La bacteria nada en línea recta en la dirección actual
- Esto produce desplazamiento neto
- Es esencialmente **explotación**: aprovechar una dirección prometedora

**La regla de transición**: Lo crucial es cuándo la bacteria cambia de un comportamiento al otro. La transición está controlada por **cambios en la concentración química detectada**:

- Si la concentración está mejorando (la bacteria se mueve hacia mayor concentración), continúa nadando recto
- Si la concentración deja de mejorar o empeora, cambia a maromas, reorientándose aleatoriamente hasta que por casualidad apunta hacia una dirección donde la concentración mejora nuevamente

**Observación clave**: Las transiciones entre comportamientos están controladas por **cambios bruscos** en la concentración, no por valores absolutos. La bacteria es sensible a la *derivada temporal* de la concentración: ¿está mejorando o empeorando?

### La Adaptación Sensorial: El Problema del "Bueno Suficiente"

Hay una complicación adicional. Si la bacteria simplemente cambiara a nado recto tras el *primer* incremento detectado en concentración, probablemente no terminaría en la mejor ubicación posible—solo en la primera mejora que encontró.

Las bacterias resuelven esto mediante **adaptación sensorial**: después de un tiempo breve (menos de un minuto en salmonela), el sistema de detección "se acostumbra" al nivel actual de concentración. Lo que antes parecía "alta concentración" ahora se convierte en el nuevo punto de referencia "normal". 

Esto fuerza a la bacteria a seguir buscando mejoras: lo que momentos antes era suficientemente bueno para mantener el nado recto, ahora deja de serlo. La bacteria vuelve a dar maromas hasta encontrar una concentración aún mayor.

La adaptación sensorial implementa una forma de **insatisfacción adaptativa**: nunca contentarse completamente con lo actual, seguir buscando mientras haya tiempo y energía.

---

## El Algoritmo: Dos Variantes del Ascenso de Colina

Ahora que hemos visto el comportamiento empírico, podemos abstraer el algoritmo subyacente. Hay dos variantes principales.

### Variante I: Ascenso de Colina Simple

Esta es la versión más básica, análoga al comportamiento de la salmonela:

```
1. Almacenar el valor actual de la variable de interés (ej: concentración química)

2. Muestrear: Ejecutar una acción exploratoria aleatoria
   (ej: dar maromas, cambiar dirección)

3. Comparar: ¿El nuevo valor es mejor que el almacenado?
   
   SI es mejor → Cambiar a explotación
                 (ej: nadar recto en esa dirección)
                 
   NO es mejor → Continuar explorando
                 (seguir en paso 2)

4. Después de un tiempo: Adaptación sensorial
   → Actualizar el valor de referencia al actual
   → Regresar al paso 2
```

**Componentes clave**:
- **Memoria**: Retener el valor previo para comparación
- **Exploración aleatoria**: Generar variabilidad conductual
- **Comparación sucesiva**: Evaluar presente vs. pasado reciente
- **Explotación direccional**: Continuar en dirección prometedora
- **Adaptación**: Evitar estancamiento en máximos locales

### Variante II: Ascenso de Mayor Pendiente

Una versión ligeramente más sofisticada, análoga a cómo actuarías si estuvieras escalando el Ajusco con los ojos vendados:

```
1. Almacenar el valor actual

2. Muestrear múltiples direcciones:
   - Probar dirección 1, registrar valor
   - Probar dirección 2, registrar valor
   - Probar dirección 3, registrar valor
   - ...
   
3. Para cada muestra:
   ¿Es mejor que el mejor registrado hasta ahora?
   SI → Actualizar como "mejor hasta el momento"
   NO → Descartar

4. ¿Se ha muestreado suficientemente?
   NO → Regresar a paso 2
   SI → Moverse en la dirección del mejor valor encontrado

5. Adaptación sensorial, regresar a paso 1
```

Esta variante requiere más capacidad de memoria (almacenar múltiples valores simultáneamente) pero puede ser más eficiente en entornos ruidosos, donde un solo muestreo podría dar una impresión equivocada.

### Analogía: Buscando Señal de Wifi

Para hacer el algoritmo más intuitivo, imagina que estás en un edificio grande desconocido y tu teléfono tiene muy poca señal de wifi. Quieres encontrar un lugar con buena señal:

**Ascenso simple**: Caminas en una dirección aleatoria, verificas la señal. Si mejoró, sigues en esa dirección. Si empeoró, te detienes, giras aleatoriamente, y pruebas otra dirección.

**Ascenso de mayor pendiente**: Te detienes donde estás, das algunos pasos exploratorios en diferentes direcciones (norte, sur, este, oeste), verificas la señal en cada una, y luego caminas decididamente en la dirección que mostró la mayor mejora.

En ambos casos, estás haciendo **comparaciones sucesivas**: no puedes ver dónde está el router, solo puedes comparar "¿tengo más o menos señal que hace un momento?"

---

## Los Seis Ingredientes del Algoritmo

Ahora podemos destilar los componentes esenciales que cualquier implementación del ascenso de colina debe tener:

### 1. Detección de una Variable Biológicamente Importante

El organismo debe ser sensible a alguna propiedad del entorno que correlaciona con recursos o peligros. Para la salmonela, es la concentración de moléculas nutritivas. Para la planta, es la intensidad lumínica. Para ti buscando wifi, es la intensidad de la señal.

Esta variable funciona como una **señal de retroalimentación** que guía el comportamiento sin necesidad de representar explícitamente la ubicación del recurso.

### 2. Memoria del Valor Previo

El organismo debe retener, aunque sea brevemente, el valor de la variable en el momento inmediatamente anterior. Sin esta memoria, no hay base para comparación.

Esta memoria puede ser muy simple—no requiere almacenar una larga historia. Basta con retener "¿cuál era el valor hace un instante?"

### 3. Comparación: Presente vs. Pasado

El mecanismo central es una operación de comparación: 

**Valor(ahora) - Valor(antes) = Cambio**

Si Cambio > 0 → Las cosas están mejorando
Si Cambio ≤ 0 → Las cosas no mejoran (o empeoran)

Esta comparación sucesiva es diferente de la comparación *simultánea* que veremos en el siguiente capítulo (sistemas de retroalimentación con receptores bilaterales). Aquí, el organismo compara el mismo lugar en dos tiempos diferentes, no dos lugares al mismo tiempo.

### 4. Dos Comportamientos Contrastantes

El algoritmo requiere al menos dos modos conductuales:

**Exploración**: Comportamiento variable, aleatorio, que muestrea diferentes opciones
- Maromas en bacterias
- Rotación en plantas  
- Caminata aleatoria en tu búsqueda de wifi

**Explotación**: Comportamiento direccional, persistente, que aprovecha una dirección prometedora
- Nado recto en bacterias
- Crecimiento direccional en plantas
- Caminar decididamente en tu mejor dirección

Este contraste entre exploración y explotación es uno de los dilemas fundamentales de la adaptación y lo encontraremos en todos los niveles de complejidad que estudiaremos.

### 5. Regla de Transición

Una regla clara que determina cuándo cambiar de un modo al otro:

**SI (Cambio > umbral) ENTONCES Explotar**
**SI (Cambio ≤ umbral) ENTONCES Explorar**

El umbral puede ser cero (cualquier mejora es suficiente) o mayor que cero (se requiere una mejora sustancial). En entornos ruidosos, un umbral positivo ayuda a evitar responder a fluctuaciones aleatorias.

### 6. Adaptación Sensorial

Un mecanismo que gradualmente ajusta el punto de referencia para la comparación. Esto previene que el organismo se "contente" con la primera mejora que encuentra.

Formalmente, el valor de referencia "decae" o "se adapta" hacia el valor actual:

Referencia(nuevo) = (1-tasa) × Referencia(viejo) + tasa × Valor(actual)

Donde 'tasa' determina qué tan rápido el sistema se acostumbra al nivel actual. Una tasa alta significa adaptación rápida (más exploración continua). Una tasa baja significa el sistema mantiene memoria del pasado por más tiempo.

---

## Formalización Matemática

Ahora que entendemos los componentes del algoritmo, podemos expresarlo compactamente en forma matemática. Esto no añade misterio—simplemente captura en notación precisa lo que ya describimos en palabras.

### La Ecuación Central

El ascenso de colina puede representarse con una sola ecuación que combina comparación y adaptación:

**Y(t+1) = a·Y(t) + b·[X(t+1) - X(t)]**

Donde:
- **Y(t)** = Variable de decisión en el tiempo t
- **X(t)** = Valor de la variable ambiental (ej: concentración) en tiempo t  
- **a** = Parámetro de adaptación (0 < a < 1)
- **b** = Parámetro de sensibilidad al cambio (b > 0)

**Interpretando los términos**:

**a·Y(t)**: El término de **adaptación sensorial**
- Si a = 1 (sin adaptación): el valor previo de Y persiste completamente
- Si a < 1: el valor previo "decae" gradualmente hacia cero
- Cuanto menor es a, más rápido el sistema "olvida" estados previos

**b·[X(t+1) - X(t)]**: El término de **detección de cambio**
- [X(t+1) - X(t)] es simplemente: ¿mejoró o empeoró?
- b amplifica o atenúa la importancia de este cambio
- Un b grande significa el sistema es muy sensible a pequeños cambios
- Un b pequeño significa se requieren cambios grandes para afectar Y

### La Regla de Respuesta

La variable Y determina qué comportamiento se ejecuta:

**SI Y(t+1) > umbral → EXPLOTAR** (nado recto, crecimiento direccional)

**SI Y(t+1) ≤ umbral → EXPLORAR** (maromas, rotación)

El umbral es típicamente cero, pero puede ajustarse según el entorno.

### Dinámica del Sistema

Veamos qué pasa en una secuencia temporal:

**Tiempo 0**: 
- Y(0) = 0 (estado inicial neutral)
- X(0) = 5 (concentración inicial)

**Tiempo 1**: 
- X(1) = 7 (concentración mejoró)
- Y(1) = 0.9×0 + 0.5×(7-5) = 0 + 1.0 = 1.0
- Dado Y(1) > 0 → **Explotar** (nadar recto)

**Tiempo 2**: 
- X(2) = 9 (sigue mejorando)
- Y(2) = 0.9×1.0 + 0.5×(9-7) = 0.9 + 1.0 = 1.9
- Dado Y(2) > 0 → **Explotar** (seguir recto)

**Tiempo 3**: 
- X(3) = 9 (sin cambio)
- Y(3) = 0.9×1.9 + 0.5×(9-9) = 1.71 + 0 = 1.71
- Dado Y(3) > 0 → **Explotar** (pero decayendo)

**Tiempo 4**: 
- X(4) = 8 (empeoró ligeramente)
- Y(4) = 0.9×1.71 + 0.5×(8-9) = 1.54 - 0.5 = 1.04
- Dado Y(4) > 0 → **Explotar** (pero sigue decayendo)

**Tiempo 5**: 
- X(5) = 7 (sigue empeorando)
- Y(5) = 0.9×1.04 + 0.5×(7-8) = 0.94 - 0.5 = 0.44
- Dado Y(5) > 0 → **Explotar** (pero casi en umbral)

**Tiempo 6**: 
- X(6) = 6 (sigue empeorando)
- Y(6) = 0.9×0.44 + 0.5×(6-7) = 0.40 - 0.5 = -0.10
- Dado Y(6) < 0 → **EXPLORAR** (dar maromas, cambiar dirección)

El sistema mantiene la explotación mientras hay evidencia de que la dirección es buena, pero eventualmente la adaptación sensorial (el término a·Y) hace que el valor de Y decaiga. Si además la concentración deja de mejorar, Y cae por debajo del umbral y el sistema vuelve a explorar.

### Propiedades Matemáticas

**1. Balance exploración-explotación**: 
- Parámetro a bajo → adaptación rápida → más exploración
- Parámetro a alto → adaptación lenta → más explotación
- Parámetro b alto → sensible a cambios pequeños
- Parámetro b bajo → solo responde a cambios grandes

**2. Robustez al ruido**:
- El término a·Y actúa como un filtro de "inercia"
- Fluctuaciones momentáneas no cambian inmediatamente el comportamiento
- Se requiere evidencia sostenida de cambio

**3. Escape de máximos locales**:
- La adaptación garantiza que el sistema no se "contente"
- Incluso si está en un buen lugar, eventualmente volverá a explorar
- Esto permite encontrar fuentes mejores más alejadas

---

## Ascenso de Colina NO es Aprendizaje

Es crucial entender qué hace y qué *no* hace este mecanismo.

### Lo que SÍ hace:

**1. Adaptación en tiempo real**: El organismo ajusta su comportamiento momento a momento en respuesta a cambios en su entorno

**2. Navegación eficiente**: Encuentra gradientes y sigue hacia concentraciones mayores sin necesidad de mapa o receptores de distancia

**3. Balance exploración-explotación**: Automáticamente alterna entre buscar y aprovechar

**4. Robustez**: Funciona en entornos ruidosos y con múltiples fuentes

### Lo que NO hace:

**1. Integración de historia**: El organismo no acumula información de experiencias pasadas. Solo compara "ahora" vs. "hace un momento". Si repetimos la misma situación mañana, el organismo responde igual que hoy—no hay memoria de largo plazo.

**2. Predicción**: El mecanismo es puramente reactivo. Responde a cambios que ya ocurrieron, no anticipa cambios futuros.

**3. Representación**: No hay modelo interno del entorno. El organismo no "sabe" dónde están las fuentes, solo sigue gradientes locales.

**4. Aprendizaje propiamente dicho**: No hay cambio duradero en el sistema. Una bacteria que navegó exitosamente ayer no navega mejor hoy por haber tenido esa experiencia.

### La Distinción Clave

**Comportamiento adaptable** (con aprendizaje): El sistema cambia de forma duradera como resultado de la experiencia. Hay integración de historia.

**Comportamiento adaptativo sin aprendizaje** (ascenso de colina): El sistema responde flexiblemente al entorno actual pero no retiene información de experiencias previas.

El ascenso de colina es un mecanismo de **comparación sucesiva sin integración de historia**. En los próximos capítulos veremos mecanismos que sí integran historia—esos constituyen el aprendizaje propiamente dicho.

Sin embargo, el ascenso de colina es importante porque:
1. Resuelve eficientemente problemas reales de navegación
2. Puede implementarse con maquinaria neural/genética muy simple
3. Los mismos principios (comparación, adaptación, exploración-explotación) reaparecen en mecanismos de aprendizaje más sofisticados
4. Es un "building block" que puede combinarse con otros mecanismos

---

## Simulador Interactivo: Explora el Ascenso de Colina

![Screenshot del simulador mostrando una bacteria navegando hacia una fuente de nutrientes con visualización de su trayectoria y parámetros ajustables]

**🔗 [Abrir Simulador de Ascenso de Colina](https://www.bouzaslab25.com/simuladores/ascenso-colina)**

### ¿Qué Explorar?

**1. El efecto de la adaptación sensorial (parámetro a)**:
- Comienza con a = 0.9 (adaptación lenta). Observa cuánto tiempo el agente explota una dirección antes de volver a explorar.
- Cambia a a = 0.5 (adaptación rápida). ¿Qué pasa con la trayectoria? ¿Es más "nerviosa"?
- Prueba a = 0.99 (muy lenta). ¿El agente se "atasca" en máximos locales?

**2. El efecto de la sensibilidad al cambio (parámetro b)**:
- Con b = 0.1 (poco sensible), ¿cuánto tiene que cambiar la concentración para que el agente responda?
- Con b = 1.0 (muy sensible), ¿responde a fluctuaciones pequeñas (ruido)?

**3. Entornos con múltiples fuentes**:
- Coloca dos fuentes de nutrientes, una pequeña cerca del inicio y una grande lejos.
- ¿El agente encuentra la fuente grande? 
- ¿Qué combinación de parámetros ayuda a escapar de la fuente pequeña?

**4. Ruido ambiental**:
- Activa el ruido en la detección de concentración.
- ¿Cómo afecta la trayectoria?
- ¿Qué valores de a y b hacen el sistema más robusto al ruido?

### Ejercicios Sugeridos

- [ ] Reproduce la trayectoria en espiral que observas en bacterias reales
- [ ] Encuentra la combinación de parámetros que minimiza el tiempo para llegar a la fuente
- [ ] Compara las dos variantes (simple vs. mayor pendiente) en el mismo entorno
- [ ] Diseña un entorno donde el ascenso de colina falle (hint: piensa en "trampas" o valles)

**💡 Tip**: Si observas que el agente se mueve en círculos sin progreso, probablemente a es demasiado alto (adaptación muy lenta). Si el agente parece errático y nunca explota direcciones prometedoras, probablemente a es demasiado bajo o b es demasiado alto.

---

## Conexiones con Otros Capítulos

### Hacia Atrás: Selección Natural

El ascenso de colina es una instancia de **ensayo y error** análoga a la selección natural:
- **Variación**: La exploración aleatoria genera comportamiento variable
- **Selección**: La comparación determina qué variantes "sobreviven" (explotan)
- **Retención**: La explotación continúa mientras el gradiente es favorable

Pero a diferencia de la selección natural, opera en tiempo ontogenético (vida del individuo) no filogenético (generaciones).

### Hacia Adelante: Aprendizaje por Refuerzo

El ascenso de colina anticipa conceptos clave del aprendizaje:
- **Error de predicción**: [X(t+1) - X(t)] es un "error" entre lo esperado y lo observado
- **Actualización incremental**: Y se ajusta gradualmente, no en un solo paso
- **Exploración-explotación**: El dilema fundamental de todo aprendizaje

En capítulos posteriores veremos cómo el modelo de Rescorla-Wagner y las diferencias temporales formalizan estas ideas integrando historia.

### Lateral: Sistemas de Retroalimentación (Próximo Capítulo)

El ascenso de colina usa **comparación sucesiva** (presente vs. pasado en el mismo lugar).

En el siguiente capítulo veremos sistemas de retroalimentación que usan **comparación simultánea** (dos lugares diferentes al mismo tiempo, mediante receptores bilaterales).

Ambos son mecanismos de adaptación sin aprendizaje, pero difieren en el tipo de comparación.

---

## Resumen

**El problema**: Localizar recursos en entornos variables sin receptores de distancia ni mapa previo.

**La solución**: Ascenso de colina—un algoritmo de comparación sucesiva que alterna entre exploración aleatoria y explotación direccional, guiado por detección de cambios en una variable ambiental.

**Ingredientes clave**: Detección, memoria, comparación, dos modos conductuales, regla de transición, adaptación sensorial.

**Lo que NO es**: Aprendizaje. No hay integración de historia ni cambio duradero del sistema.

**Por qué importa**: Es un mecanismo simple pero poderoso que resuelve problemas reales. Los principios que lo componen—comparación, reducción de error, balance exploración-explotación—reaparecen en mecanismos más sofisticados.

**Lo que viene**: En el próximo capítulo veremos sistemas de retroalimentación, donde el comportamiento no solo responde al entorno sino que lo modifica, creando lazos cerrados de interdependencia organismo-entorno.

---

## Para Profundizar

**Lecturas sugeridas**:

1. **Berg, H.C. & Brown, D.A. (1972)**. "Chemotaxis in Escherichia coli analysed by three-dimensional tracking." *Nature, 239*, 500-504.
   - El paper clásico que caracterizó el comportamiento de "run and tumble" en bacterias.

2. **Schnitzer, M.J. (1993)**. "Theory of continuum random walks and application to chemotaxis." *Physical Review E, 48*(4), 2553-2568.
   - Formalización matemática rigurosa del ascenso de colina en bacterias.

3. **Russell, S. & Norvig, P. (2020)**. *Artificial Intelligence: A Modern Approach* (4th ed.), Capítulo 4: "Search in Complex Environments."
   - Tratamiento del ascenso de colina en el contexto de algoritmos de búsqueda en IA.

4. **Entorno de programación**: Si te interesa programar tus propios agentes con ascenso de colina, consulta el tutorial de Python disponible en la página del laboratorio.