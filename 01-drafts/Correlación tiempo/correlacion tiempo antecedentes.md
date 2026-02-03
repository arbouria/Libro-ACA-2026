# ---

### **Notas de Curso: Modelos Cuantitativos del Aprendizaje Asociativo (Basados en Tasas e Información)**

**Introducción: Un Cambio de Paradigma en el Aprendizaje Asociativo**

Tradicionalmente, el aprendizaje asociativo se ha entendido como la formación y modificación de conexiones (asociaciones) en la mente o el cerebro, fortalecidas por reforzadores y debilitadas por la ausencia de los mismos. Sin embargo, la investigación reciente, especialmente aquella que se centra en el papel del tiempo, ha modificado nuestra comprensión. La nueva perspectiva propone que una asociación no es una conexión alterada en el cerebro, sino un **hecho medible sobre la distribución de eventos en el tiempo**. El aprendizaje asociativo es, entonces, el proceso de **percibir estas asociaciones temporales y decidir actuar sobre ellas**.

Este enfoque es fundamentalmente distinto de modelos como el de Rescorla-Wagner y sus descendientes, que se basan en la actualización de reglas delta y la probabilidad de reforzamiento.

**1\. Conceptos Fundamentales: Tasas vs. Probabilidades e Informatividad**

* **La Distinción Crítica: Tasa vs. Probabilidad**

  * Durante mucho tiempo, se confundió la **probabilidad** de reforzamiento (conteo de éxitos dividido por el total de éxitos y fracasos) con la **tasa** de reforzamiento (conteo dividido por la duración del intervalo).  
  * Esta distinción es **fundamental**. Los modelos tradicionales fallaron al atribuir eficacia causal a "no-reforzadores" (∼R), que no tienen atributos físicos ni momentos específicos de ocurrencia, lo que los hace imposibles de contar en muchos casos (ej. reforzadores distribuidos aleatoriamente por un proceso de Poisson).  
  * El éxito de la formalización del aprendizaje asociativo reside en cambiar el enfoque de la probabilidad a la **tasa de reforzamiento**.  
* **Informatividad (ι): La Variable Empírica Esencial**

  * La informativad es el **cociente entre una tasa condicional y una tasa incondicional**. Es la variable empírica esencial, reemplazando a la probabilidad de reforzamiento.  
  * **Ejemplo**: Si un sujeto está en una cámara por 6 horas (21,600 segundos) y luego suena un ruido (CS) por 1 segundo, seguido de un choque.  
    * Tasa contextual de choque (incondicional): λR|C \= 1 choque / 21,600 segundos.  
    * Tasa condicional durante el CS: λR|CS \= 1 choque / 1 segundo.  
    * La informativad (ι) es la relación entre estas tasas: **ι \= λR|CS / λR|C \= (1/1s) / (1/21600s) \= 21600**.  
    * Este valor de 21600 es una "coincidencia muy fuerte", lo que intuitivamente justificaria un aprendizaje en una sola exposición.  
* **Información Comunicada: El Logaritmo de la Informatividad**

  * La información comunicada entre eventos conductuales y de reforzamiento temporalmente asociados es el **logaritmo de la informativad**.  
  * En el ejemplo anterior, log₂ (21600) \= **14.4 bits**. Esto representa la cantidad de información comunicada por el CS sobre cuándo esperar el próximo choque.  
  * Esta medida se basa en la teoría de la información de Shannon. Reduce la incertidumbre del receptor sobre cuándo esperar el próximo choque.

**2\. Implicaciones Cruciales: Invariancia de Escala Temporal y Aprendizaje en una Sola Exposición**

* **Invariancia de Escala Temporal**: El aprendizaje asociativo es **invariante a la escala temporal**. Esto significa que los eventos perceptiblemente asociados pueden estar arbitrariamente muy separados en el tiempo.

  * No existen "ventanas de asociabilidad" ni "rastros de elegibilidad que decaen". La creencia generalizada de una "ventana crítica" para la formación de asociaciones es **simplemente falsa**.  
  * **Ejemplo**: El aprendizaje de aversión al sabor con retrasos de horas entre el sabor y la náusea se explica por la invarianza de la escala temporal. Lo que importa son las latencias relativas, no sus valores absolutos.  
* **Aprendizaje en una Sola Exposición ("One-Shot Learning")**

  * Contrario a la idea de que el aprendizaje debe progresar mediante pequeños cambios (como en los modelos de descenso de gradiente), el aprendizaje en una sola exposición se observa en protocolos pavlovianos y operantes cuando la asociación estadística es suficientemente fuerte.  
  * Esto es posible porque la medida de informativad y su fiabilidad (ver nDKL más adelante) tiene en cuenta las duraciones de los intervalos.  
  * En experimentos operantes, se ha observado aprendizaje en una sola exposición a pesar de retrasos de reforzamiento de minutos (más de cuatro órdenes de magnitud más largos de lo convencional), cuando la informativad era alta.

**3\. La Ley de la Tasa de Aprendizaje**

* La **tasa de aprendizaje** (definida operacionalmente como el recíproco de los reforzamientos necesarios para la adquisición de una respuesta condicionada) es una **función casi escalar de la separación temporal relativa**, medida por la informativad.  
* **α \= 1 / Reforzamientos\_a\_Adquisición ≈ (1/k) \* ι**.  
* **k** es una constante que representa la informativad necesaria para la adquisición en una sola exposición en el sujeto mediano.  
* **Implicación Contraintuitiva**: Los investigadores que agrupan los ensayos con la esperanza de acortar el tiempo de entrenamiento logran el efecto contrario. Intervalos interensayo (ITIs) más largos (lo que aumenta la informativad) conducen a una adquisición más rápida (menos reforzamientos).  
* **Efecto del Reforzamiento Parcial**: El reforzamiento parcial **no tiene efecto** sobre el número de reforzamientos necesarios para la adquisición. Esto se debe a que reduce tanto la tasa condicional como la contextual por el mismo factor, dejando la informativad sin cambios y, por lo tanto, la tasa de aprendizaje igual.  
* Esta ley es robusta y se ha demostrado en diversas especies y protocolos.

**4\. ¿Qué hay en la Cabeza? Perceptos y Mapas Temporales**

* En el cerebro, lo que hay son **perceptos**: perceptos de tasas de reforzamiento, informativad, asociaciones y su fiabilidad.  
* Estos perceptos son el resultado de **computaciones** que los extraen de señales sensoriales, así como de conteos y duraciones.  
* Las tasas percibidas de reforzamiento son funciones escalares de las tasas de reforzamiento medidas. Esto sugiere que el cerebro computa y recuerda las tasas de reforzamiento.  
* **El Mapa Temporal**: La computación de una tasa implica un **mapa temporal**, un registro de eventos pasados con marcas de tiempo. Este mapa permite "mirar hacia atrás en el tiempo" para calcular duraciones (el denominador de la tasa). No hay "asociaciones aristotélicas" que se actualicen en este modelo.

**5\. Medida de Fiabilidad: La Estadística nDKL**

* Para juzgar la **fiabilidad** de las estimaciones de parámetros estocásticos (incluso con un tamaño de muestra de 1), se utiliza la estadística **nDKL** (Kullback-Leibler Divergence).  
* **nDKL(λR|CS || λR|C) \= (n\_R|CS / (1 \+ n\_R|CS/n\_R|C)) \* (ln(λ\_R|CS / λ\_R|C) \+ (λ\_R|C / λ\_R|CS) \- 1\)**.  
* Esta estadística es superior a las pruebas convencionales porque se aplica cuando n=1 y captura la asimetría de la divergencia.  
* Tiene implicaciones neurobiológicas: la divergencia representa el número promedio de bits de memoria adicionales necesarios si se codifican los intervalos con una distribución incorrecta. Esto vincula la nueva concepción con la idea de que el propósito del aprendizaje asociativo es la **predicción**.

**6\. Asignación de Crédito**

* El problema de la asignación de crédito es determinar qué predictores (CS, contexto, respuesta) reciben el crédito por un reforzamiento.  
* En el enfoque basado en tasas, la asignación de crédito se reduce a **resolver un sistema de ecuaciones simultáneas**.  
* Las tasas de reforzamiento observadas son las cantidades conocidas. Las tasas que deben atribuirse a los posibles predictores son las incógnitas.  
* La solución se obtiene mediante la inversión de una matriz de **probabilidades temporales** (razones de duraciones acumulativas).  
* Este modelo es **explícito y no tiene parámetros libres**, a diferencia de los modelos de actualización de reglas delta.  
* **Ejemplo de Rescorla (1968)**:  
  * Grupo experimental (CS predice choque): El crédito se atribuyó completamente al CS de tono.  
  * Grupo de control aleatorio (choques distribuidos aleatoriamente): El crédito se atribuyó completamente a la cámara de prueba (el contexto).  
* El modelo distingue entre lo que se puede esperar en un contexto (tasa contextual) y la tasa atribuida al contexto en sí, lo que explica por qué las ratas del grupo experimental temían la cámara a pesar de no atribuirle directamente el choque.

**7\. Detección de Cambios (Extinción)**

* Los modelos tradicionales no pueden explicar la **extinción** y la recuperación del aprendizaje. El problema es la dificultad de contar o atribuir causalidad a los "no-reforzamientos" cuando los eventos son aleatorios.  
* **El efecto de extinción por reforzamiento parcial**: Contrariamente a la intuición, el reforzamiento parcial *aumenta* el número de ensayos no reforzados consecutivos necesarios para la extinción. Es un efecto escalar: si 1 de cada 10 ensayos es reforzado, se necesitan 10 veces más ensayos no reforzados para extinguir la respuesta.  
* Los cerebros actúan como **detectores ideales de cambios en las tasas relativas**. Utilizan un algoritmo de análisis en tiempo real en el mapa temporal para detectar cambios (codos en el registro acumulativo) y estimar cuándo ocurrieron.  
* Este algoritmo usa la estadística **nDKL** para comparar secuencias de estimaciones de tasas. Cuando hay un cambio, los valores de nDKL aumentan hasta un máximo en el punto del cambio, luego disminuyen.  
* La extinción se entiende como el proceso de aprender que "lo que era cierto, ya no lo es" ("eso fue entonces, esto es ahora").

**8\. Ecuación de Tasa de Salida y la Ley de Igualación (Matching Law)**

* En protocolos de intervalo variable concurrente (VI), los animales no aumentan la probabilidad momentánea de irse de una ubicación a medida que el tiempo de permanencia se alarga (los tiempos de permanencia tienen distribución exponencial). Esto sugiere una **política innata** de recolección de información más que un comportamiento condicionado.  
* Esta política incluye:  
  1. Programar las salidas con un **proceso de Poisson** para distribuir los tiempos de permanencia exponencialmente, "blanqueando" los datos y evitando el aliasing (confusión de periodos).  
  2. Escalar las tasas de este proceso por la **tasa contextual de reforzamiento**, ajustando la actividad al contexto.  
  3. Proporcionar las duraciones de permanencia a las tasas de reforzamiento esperadas, lo que lleva a la **Ley de Igualación de Herrnstein**.  
* La **Ecuación de Tiempo de Permanencia (Eq. 8\)** explica cuantitativamente los resultados de "preferencia revelada" de Belke (1992) y Gibbon (1995). Los animales no "elegían", sino que se marchaban cuando el proceso de Poisson que programa las salidas se agotaba.

**Conclusiones y Consecuencias Ontológicas**

Esta reconceptualización del aprendizaje asociativo ofrece una comprensión **cuantitativamente coherente** de un amplio rango de resultados experimentales que habían resistido una explicación rigurosa durante décadas.

* El enfoque en las tasas y la informativad, junto con las herramientas de la teoría de la información, unifica la comprensión de fenómenos pavlovianos y operantes.  
* Cambia el estatus ontológico de la "asociación": ya no son entidades mentales hipotéticas o cambios en las conexiones interneuronales. Son **hechos estadísticos medibles sobre la distribución de eventos en el tiempo**, que existen independientemente de la mente y el cerebro.  
* Los **perceptos** de estas asociaciones son los símbolos en la memoria sobre los cuales opera la maquinaria computacional del cerebro para generar el comportamiento inteligente.  
* Esta visión **socava las bases conceptuales de muchos modelos actuales** que buscan los "engramas" (rastros de memoria) como enlaces asociativos o que equiparan el funcionamiento del cerebro con el de los Grandes Modelos de Lenguaje (LLMs) basados en "pesos de conexión". Los LLMs, de hecho, simulan estas asociaciones con maquinaria de procesamiento de símbolos, no las realizan físicamente como se ha conceptualizado tradicionalmente.

Este marco proporciona una base sólida y empíricamente apoyada para entender cómo los cerebros aprenden y se adaptan a su entorno temporal.

**Informativeness** (informatividad), denotada por la letra griega iota (), es un concepto fundamental en la reconceptualización del aprendizaje asociativo. Se define como:

* **La relación (o ratio) de una tasa condicional a una tasa incondicional**.  
* Específicamente, es **la relación entre la tasa de refuerzo condicional a un estímulo condicional (CS) y la tasa de refuerzo en el contexto** en el que ocurren tanto el CS como el refuerzo. En el aprendizaje operante, es el factor por el cual una respuesta reduce el tiempo de espera esperado para el siguiente refuerzo.

**Cálculo y Distinción Clave:**

* Se calcula como el **cociente de dos tasas** (recuentos divididos por duraciones), no como una probabilidad. Por ejemplo, si la tasa contextual de choque es 1 choque/21,600 segundos y la tasa durante un CS de 1 segundo es 1 choque/1 segundo, la informativeness sería 21,600.  
* La distinción entre tasa y probabilidad es crucial; el fracaso en diferenciar entre ellas ha sido un problema común en la concepción tradicional del aprendizaje asociativo.

**Rol Central y Propiedades:**

* Es la **variable empírica esencial** en la comprensión reconceptualizada del aprendizaje asociativo.  
* Su papel central **unifica la comprensión de los fenómenos pavlovianos y operantes/instrumentales**, revelando comunalidades cuantitativas y conceptuales inesperadas.  
* El **logaritmo de la informativeness** es la cantidad de información comunicada entre eventos temporalmente asociados. Esto mide la fuerza de la asociación estocástica.  
* El aprendizaje asociativo es **invariante a la escala de tiempo** (time-scale invariant). Esto significa que eventos percibidos como asociados pueden estar arbitrariamente separados en el tiempo, ya que las unidades de tiempo en las estimaciones de tasas se cancelan. Lo que importa son las latencias relativas, no sus valores absolutos.  
* La informativeness determina la **tasa de aprendizaje** (learning rate). Operacionalmente definida como el recíproco de los refuerzos necesarios antes de la aparición de una respuesta condicionada, la tasa de aprendizaje es una función casi escalar de la separación temporal relativa, medida por la informativeness. Esto explica el aprendizaje en un solo ensayo (one-shot learning) cuando la informativeness es suficientemente alta.

**Otras Aplicaciones y Consecuencias:**

* La informativeness es crucial para medir la **confiabilidad de una asociación** a través de la estadística nDKL (Kullback-Leibler divergence).  
* Es la variable en la **ecuación de detección de cambios** (change-detection equation), lo que permite una explicación rigurosa del efecto de extinción por refuerzo parcial.  
* Su recíproco es un elemento clave en la **asignación de crédito** (assignment of credit) en modelos de aprendizaje asociativo, donde ayuda a determinar qué predictores reciben crédito por un refuerzo.

En resumen, la informativeness es una medida estadística que cuantifica la relación temporal y la información que un evento (como un CS o una respuesta) comunica sobre la probabilidad de ocurrencia de otro evento (como un refuerzo), siendo fundamental para comprender cómo los cerebros perciben y actúan sobre las asociaciones en el mundo.

Los datos temporales juegan un rol **fundamental** en la medición de asociaciones, ya que la reconceptualización del aprendizaje asociativo ha cambiado el enfoque de la probabilidad de refuerzo a la **tasa de refuerzo**. Esta distinción es crucial para una comprensión precisa de cómo se forman y perciben las asociaciones.

Aquí se detalla el rol de los datos temporales:

1. **La Importancia de las Tasas sobre las Probabilidades:**

   * Tradicionalmente, la comprensión del aprendizaje asociativo se ha basado en la **probabilidad de refuerzo**. Sin embargo, esta conceptualización ha sido problemática porque **una probabilidad es una proporción entre el número de éxitos y la suma de éxitos y fracasos**, sin considerar la duración del intervalo en el que se realizó el conteo.  
   * Por el contrario, **una tasa es un conteo dividido por la duración (T) del intervalo durante el cual se realiza el conteo**. La incapacidad de diferenciar entre tasa y probabilidad ha sido un problema común y persiste en la concepción tradicional del aprendizaje asociativo.  
   * El problema surge, en parte, de la idea de que las asociaciones residen en la mente (y por lo tanto en el cerebro) y que los refuerzos fortalecen las conexiones, mientras que los "no refuerzos" (\~R) las debilitan. Sin embargo, los **"no refuerzos" no tienen atributos físicos y no pueden excitar sensores ni localizarse en el tiempo**, lo que impide contar su ocurrencia y atribuirles eficacia causal, especialmente cuando los refuerzos se distribuyen aleatoriamente en el tiempo. Modelos basados en la regla delta, como el modelo de Rescorla-Wagner, no pueden explicar los hechos cuantitativos sobre la extinción por esta razón.  
2. **Informativeness: La Variable Esencial basada en Tasas Temporales:**

   * La **informativeness** (denotada por ) se define como la **relación (o cociente) de una tasa condicional a una tasa incondicional**. Específicamente, es la relación entre la tasa de refuerzo condicional a un estímulo condicional (CS) y la tasa de refuerzo en el contexto.  
   * Es la **variable empírica esencial** para la comprensión reconceptualizada del aprendizaje asociativo. Su papel central **unifica la comprensión de los fenómenos pavlovianos y operantes/instrumentales**, revelando comunalidades cuantitativas y conceptuales inesperadas.  
   * Un ejemplo extremo ilustra su valor: si un sujeto ha estado en una cámara de prueba durante 6 horas (21,600 segundos) y luego se activa un ruido durante 1 segundo, seguido de una descarga, la tasa contextual de descarga es 1/21,600s y la tasa durante el CS es 1/1s. La informativeness es 21,600. La probabilidad de refuerzo, en este caso, sería 1 para ambos predictores después del primer refuerzo, lo que haría imposible el "aprendizaje en un solo ensayo" (one-shot learning) si la probabilidad impulsara el aprendizaje.  
3. **Consecuencias y Aplicaciones de la Informativeness y los Datos Temporales:**

   * **Invarianza a la Escala de Tiempo (Time-Scale Invariance):** Dado que las unidades de tiempo en las estimaciones de tasas se cancelan en la informativeness, el aprendizaje asociativo es **invariante a la escala de tiempo**. Esto significa que eventos asociados pueden estar arbitrariamente separados en el tiempo, refutando la noción de "ventanas de asociabilidad" o "rastros de elegibilidad que se desvanecen". Esto explica el aprendizaje de aversión al veneno en un solo ensayo con horas de retraso entre el sabor y las náuseas.  
   * **Cálculo de la Información Comunicada:** El **logaritmo de la informativeness** es la cantidad de información comunicada entre eventos temporalmente asociados. Esto mide la fuerza de la asociación estocástica. Rescorla ya había enfatizado que el refuerzo dependía de si el CS comunicaba información sobre dónde encontrar el refuerzo en el tiempo.  
   * **Tasa de Aprendizaje:** La informativeness determina la **tasa de aprendizaje** (definida como el recíproco de los refuerzos necesarios antes de la aparición de una respuesta condicionada). Una informativeness suficientemente alta puede llevar al **aprendizaje en un solo ensayo** (one-shot learning) en protocolos pavlovianos y operantes.  
   * **Mapa Temporal y Percepción de Asociaciones:** Para computar las tasas, el cerebro debe mantener un **"mapa temporal"**, que es un registro con sellos de tiempo de eventos pasados. Este mapa permite "mirar hacia atrás en el tiempo" para calcular duraciones acumuladas y tasas. La percepción de la asociación es el logaritmo de la informativeness percibida, que es el logaritmo de la tasa de refuerzo percibida durante el CS dividida por la tasa de refuerzo percibida en el contexto experimental.  
   * **Fiabilidad de la Asociación y Detección de Cambios:** La informativeness es crucial para medir la **fiabilidad de una asociación** a través de la estadística nDKL (divergencia de Kullback-Leibler), que puede calcularse con un tamaño de muestra de 1\. Esta misma estadística se utiliza en un algoritmo de **detección de cambios**, lo que proporciona una explicación rigurosa del efecto de extinción por refuerzo parcial. Los modelos tradicionales basados en la regla delta no pueden explicar estos fenómenos porque promedian los cambios en lugar de detectarlos.  
   * **Asignación de Crédito:** En el enfoque basado en tasas, la asignación de crédito se reduce a resolver un sistema de ecuaciones simultáneas donde las **tasas observadas son las cantidades conocidas**, y los coeficientes son **probabilidades temporales** (razones de duraciones acumuladas). Estas probabilidades temporales son observadas y carecen de unidades de tiempo (time-scale invariant). Este modelo explica fenómenos como el bloqueo y el ensombrecimiento de manera explícita y sin parámetros libres.

En síntesis, la **reconcepción del aprendizaje asociativo se basa en la percepción de asociaciones temporales medibles, las cuales se cuantifican mediante la informativeness, una razón de tasas que incorpora duraciones temporales**. Este enfoque, impulsado por los datos temporales, ofrece una comprensión matemáticamente coherente y cuantitativa de una amplia gama de resultados experimentales que han resistido explicaciones durante décadas.

¡Excelente\! Es un gran desafío integrar y contrastar la información de múltiples fuentes sobre un tema tan complejo como el aprendizaje asociativo. La "informativeness" es un concepto clave para entender las diferencias y avances en este campo.

A continuación, un texto que integra los artículos previos, señalando similitudes y diferencias en sus enfoques sobre el aprendizaje asociativo:

---

### **La "Informativeness" como eje de una reconceptualización del Aprendizaje Asociativo frente a Modelos Tradicionales y Bayesianos**

La comprensión del **aprendizaje asociativo** ha evolucionado significativamente, transitando de modelos centrados en la probabilidad de refuerzo hacia aquellos que priorizan la **tasa de refuerzo** y la **información temporal**. Este cambio fundamental subraya el papel central de la **"informativeness"** (informatividad), un concepto crucial en esta reconceptualización.

**La Informativeness: Una Medida Fundamental Basada en el Tiempo**

La "informativeness" (denotada por $\\iota$) se define como la **relación (o cociente) de una tasa condicional a una tasa incondicional**. Específicamente, en el aprendizaje pavloviano, es la relación entre la tasa de refuerzo condicional a un estímulo condicional (CS) y la tasa de refuerzo en el contexto experimental. En el aprendizaje operante, representa el factor por el cual una respuesta reduce el tiempo de espera esperado para el siguiente refuerzo.

Este concepto se calcula como el cociente de dos tasas (recuentos divididos por duraciones), lo que lo diferencia fundamentalmente de la probabilidad, que es una proporción de éxitos sobre éxitos y fracasos sin considerar el tiempo. Esta distinción es crucial, ya que la incapacidad de diferenciar entre tasa y probabilidad ha sido un problema persistente en la concepción tradicional del aprendizaje asociativo.

Las propiedades clave de la informativeness y los datos temporales son:

* **Invarianza a la Escala de Tiempo (Time-Scale Invariance)**: Dado que las unidades de tiempo en las estimaciones de tasas se cancelan en el cálculo de la informativeness, el aprendizaje asociativo es **invariante a la escala de tiempo**. Esto significa que los eventos percibidos como asociados pueden estar arbitrariamente separados en el tiempo, refutando la noción de "ventanas de asociabilidad" o "rastros de elegibilidad que se desvanecen". Un ejemplo elocuente es el aprendizaje de aversión al veneno en una sola exposición, incluso con horas de retraso entre el sabor y las náuseas.  
* **Medición de Información**: El **logaritmo de la informativeness** es la cantidad de información comunicada entre eventos temporalmente asociados, midiendo la fuerza de la asociación estocástica.  
* **Determinación de la Tasa de Aprendizaje (Learning Rate Law)**: La informativeness determina la tasa de aprendizaje, definida operacionalmente como el recíproco de los refuerzos necesarios antes de la aparición de una respuesta condicionada. Una informativeness suficientemente alta puede conducir al **aprendizaje en una sola exposición (one-shot learning)** en protocolos pavlovianos y operantes.  
* **Mapa Temporal**: Para computar las tasas, el cerebro debe mantener un "mapa temporal", un registro con sellos de tiempo de eventos pasados que permite "mirar hacia atrás en el tiempo" para calcular duraciones acumuladas y tasas.

**Contrastes con los Modelos Tradicionales: Rescorla-Wagner y Error de Predicción de Recompensa (RPE)**

Los modelos tradicionales de aprendizaje asociativo, como el influyente **modelo de Rescorla-Wagner (RW)**, explican el aprendizaje a través de la reducción gradual de **errores de predicción**. La fuerza de una asociación se actualiza en cada "ensayo" basándose en la diferencia entre el resultado experimentado y el predicho (error de predicción). Esta actualización es proporcional al tamaño del error de predicción, lo que explica fenómenos como el bloqueo. El RW modela el aprendizaje como un proceso de **descenso de gradiente**, lo que implica cambios pequeños y graduales.

Sin embargo, el modelo RW y sus descendientes, basados en la **regla delta**, han mostrado **limitaciones significativas**:

* **Manejo del Tiempo**: No están intrínsecamente equipados para explicar los efectos del intervalo CS-US ni el espaciado entre ensayos en el aprendizaje. Tienden a discretizar el tiempo en estados, lo que fija una escala de tiempo intrínseca que no se alinea con la invarianza a la escala de tiempo observada empíricamente.  
* **"No Refuerzos"**: Atribuyen eficacia causal a "no refuerzos" (\~R), eventos sin atributos físicos que no pueden localizarse en el tiempo, lo que impide contar su ocurrencia y atribuirles causalidad, especialmente cuando los refuerzos se distribuyen aleatoriamente en el tiempo. Esto los hace incapaces de explicar hechos cuantitativos sobre la extinción.  
* **Aprendizaje en un Solo Ensayo**: Su naturaleza de descenso de gradiente hace que el aprendizaje en un solo ensayo sea conceptualmente imposible si la probabilidad impulsara el aprendizaje.  
* **Parámetros Libres**: A menudo requieren múltiples parámetros libres que se ajustan en simulaciones para replicar resultados experimentales, a diferencia de modelos basados en tasas sin parámetros o con parámetros estimados experimentalmente.

**Avances con Enfoques Bayesianos y Causales**

La insatisfacción con el modelo RW llevó a la búsqueda de explicaciones más completas y basadas en principios, incluyendo la adopción de tratamientos **bayesianos**. Los tratamientos bayesianos parten de la premisa de que los animales aprenden porque tienen **incertidumbre** sobre algún estado subyacente del ambiente y hacen observaciones ruidosas que se relacionan con este estado. El aprendizaje implica procesar estas observaciones para inferir el estado y, así, cambiar el grado de incertidumbre.

1. **Filtro de Kalman y sus Extensiones**:

   * El **filtro de Kalman** asume que las características latentes (pesos o asociaciones entre estímulos y resultados) pueden cambiar con el tiempo (por ejemplo, mediante un paseo aleatorio gaussiano).  
   * Si bien la inferencia en el filtro de Kalman se basa en un error de predicción similar al del modelo de Rescorla-Wagner, su **diferencia crítica es que toma en cuenta la incertidumbre del animal** en el proceso de aprendizaje.  
   * La tasa de aprendizaje (ganancia de Kalman) se ajusta en función de la incertidumbre.  
   * Puede explicar fenómenos complejos como el **bloqueo hacia atrás (backward blocking)** debido a los componentes fuera de la diagonal de la matriz de covarianza, que representan anti-correlación en las estimaciones individuales.  
   * Modelos más avanzados como el **Filtro Gaussiano Jerárquico** (Hierarchical Gaussian Filter) o el **filtro de Kalman volátil** permiten que la varianza de la caminata aleatoria (que impulsa el cambio de pesos) varíe con el tiempo, lo que acelera el aprendizaje en entornos volátiles.  
2. **Modelos de Causa Latente (Latent Cause Models)**:

   * Asumen que el aprendizaje implica no solo la relación estímulo-resultado, sino también el **contexto o la estructura en la que ocurre el aprendizaje**.  
   * La **extinción** se explica de forma característica: puede ocurrir por un cambio en la asociación dentro de la causa actual (desaprendizaje) o por la inferencia de una **nueva causa** que no esté "contaminada" por asociaciones pasadas. Esto proporciona una explicación rigurosa de fenómenos como la recuperación espontánea de la extinción.  
3. **Aprendizaje Causal Temporal (Temporal Causal Learning \- TCL)**:

   * Propone un marco **bayesiano** que **sintetiza modelos de error de predicción y modelos temporales**.  
   * Su suposición central es la **invarianza a la escala de tiempo**, formulada como un modelo generativo jerárquico que explica cuantitativamente la **dependencia de la adquisición en ley de potencia con la relación C/T** (intervalo recompensa-recompensa / intervalo señal-recompensa).  
   * A diferencia de los modelos tradicionales, TCL asume que los animales **aprenden distribuciones de intervalos** (histogramas) entre estímulos y recompensas, utilizando una escala de tiempo **logarítmica**.  
   * Predice **curvas de aprendizaje discontinuas** y **escalamiento de Weber-law-like** en los perfiles de respuesta.  
   * Propone reglas de actualización para el aprendizaje de distribuciones de intervalos (que se asemejan a señales de RPE) y para el aprendizaje de asociaciones causales, prediciendo **señales neuronales distintas**.  
   * Reproduce fenómenos clásicos como la extinción (independiente de la escala de tiempo), el bloqueo y la degradación de contingencia.  
4. **Contingencia Neta Ajustada para Relaciones Causales (Adjusted Net Contingency for Causal Relations \- ANCCR)**:

   * Una alternativa destacada a la hipótesis del error de predicción de recompensa por diferencia temporal (TDRPE) en la señalización de **dopamina**.  
   * Postula que los animales infieren predicciones aprendiendo la **causa retrospectiva de las recompensas**. Esto se logra midiendo si una señal **precede consistentemente** a una recompensa más de lo esperado por azar.  
   * La **dopamina mesolímbica** se propone como la señal de la **significatividad aprendida (learned meaningfulness)**, funcionando como una **compuerta para el aprendizaje retrospectivo**. Cuando la dopamina es alta, la significatividad aprendida es alta, lo que desencadena el aprendizaje retrospectivo.  
   * Aunque ANCCR es consistente con los hallazgos centrales de TDRPE en el condicionamiento simple (como la respuesta de dopamina a la señal baja al principio y alta al final del aprendizaje, y la respuesta a la recompensa alta al principio y baja al final), experimentos diseñados para distinguirlos han mostrado que la dopamina se alinea con ANCCR, no con TDRPE.  
   * ANCCR aborda las suposiciones temporales problemáticas de TDRL que resultan en una representación no escalable del tiempo.  
   * Propone que la dopamina actúa como un **modulador de la tasa de aprendizaje**.

**Similitudes y Diferencias Clave entre Enfoques**

* **Paso de Probabilidad a Tasa/Tiempo**: Una **similitud fundamental** entre los modelos más recientes (Gallistel & Gibbon, bayesianos, TCL, ANCCR) es su énfasis en el **tiempo, las tasas y los intervalos** sobre las probabilidades para explicar el aprendizaje. Esto representa una divergencia significativa de los modelos clásicos como Rescorla-Wagner.  
* **Incertidumbre y Enfoque Bayesiano**: Los modelos bayesianos (Kalman, HGF, Causa Latente, TCL) y los basados en la Teoría de la Información (Gallistel & Gibbon) incorporan explícitamente la **incertidumbre** en sus marcos. Utilizan medidas de información (entropía, nDKL) para cuantificar la incertidumbre y la fiabilidad de las asociaciones.  
* **Invarianza a la Escala de Tiempo**: Esta es una característica **crucial y compartida** por los enfoques más modernos (Gallistel & Gibbon, TCL, ANCCR) para explicar el aprendizaje con retrasos largos y los efectos de la relación C/T. Esto desafía la creencia arraigada en una "ventana crítica" para la formación de asociaciones.  
* **El Papel de la Dopamina**:  
  * **TDRPE (clásico)**: La dopamina señala el error de predicción, funcionando como una señal de enseñanza.  
  * **ANCCR**: La dopamina señaliza **asociaciones causales** y/o la **significatividad aprendida**, actuando como un modulador de la tasa de aprendizaje para el aprendizaje retrospectivo.  
  * **TCL**: Predice la existencia de **dos señales de aprendizaje distintas**: una similar a la RPE para las distribuciones de intervalos (pesos temporales) y otra para las asociaciones causales (log-verosimilitud relativa).  
* **Curvas de Adquisición (Aprendizaje)**:  
  * Los modelos **RW** y de error de predicción generalmente predicen una **adquisición gradual y desacelerada**.  
  * En contraste, los modelos basados en tasas (como Gallistel) han presentado evidencia de **aumentos lineales** en la tasa de respuesta (y, por lo tanto, el aprendizaje) a lo largo de los ensayos, lo que se explica por una disminución lineal en la **incertidumbre epistémica**.  
  * TCL puede reproducir tanto curvas de aprendizaje discontinuas como la aparición abrupta de una respuesta, a pesar de que las señales subyacentes se asemejen a un RPE gradual.  
* **Asignación de Crédito**:  
  * **RW**: Resuelve el problema de la asignación de crédito mediante el error de predicción.  
  * **Gallistel (basado en tasas)**: Propone que la asignación de crédito se resuelve mediante un sistema de ecuaciones simultáneas donde las tasas observadas son las cantidades conocidas y los coeficientes son probabilidades temporales (razones de duraciones acumuladas). Este enfoque es explícito y sin parámetros libres.  
  * **ANCCR**: Utiliza los efectos causales directos y las asociaciones observadas.  
* **Extinción y Refuerzo Parcial**:  
  * Los modelos **RW** y basados en la regla delta han tenido dificultades para explicar consistentemente los resultados experimentales de la extinción y los efectos del refuerzo parcial.  
  * Los **modelos de causa latente** ofrecen una explicación al inferir nuevas causas.  
  * **TCL** también proporciona una explicación consistente de la extinción (independiente de la escala de tiempo).  
  * El enfoque de Gallistel, con su algoritmo de **detección de cambios** que utiliza la estadística nDKL (divergencia de Kullback-Leibler), ofrece una explicación rigurosa del efecto de extinción por refuerzo parcial, al detectar cambios en las tasas y truncar los datos en el mapa temporal.

En resumen, la "informativeness" y el énfasis en los datos temporales han sido catalizadores para una **reconceputalización profunda del aprendizaje asociativo**. Esta evolución ha llevado a modelos, como los bayesianos, TCL y ANCCR, que ofrecen explicaciones más coherentes y cuantitativas para una amplia gama de fenómenos de aprendizaje, superando las limitaciones de las teorías tradicionales al integrar la incertidumbre, la invarianza a la escala de tiempo y el papel dinámico de neuromoduladores como la dopamina en la formación de asociaciones y la inferencia causal.

¡Claro que sí\! Gracias por proporcionarme estos artículos adicionales. A partir de la información en estas fuentes, puedo integrar y presentar una gran cantidad de evidencia empírica que enriquece nuestra comprensión del aprendizaje asociativo.

Aquí están los hallazgos empíricos clave y las explicaciones detalladas que se desprenden de los nuevos documentos:

* **La Informatividad (Relación C/T) como Determinante del Aprendizaje:**

  * La investigación ha demostrado consistentemente que **la tasa de aprendizaje se escala directamente con la relación entre la duración del intervalo estímulo-incondicionado (US)-US y el tiempo entre los US (la suma del Intervalo entre Ensayos (ITI) y el intervalo Condicionado (CS)-US)**. Esta relación se conoce como la **relación C/T (Ciclo/Ensayo) o "informatividad"**.  
  * Un metaanálisis que combinó datos de pichones reveló que la velocidad de aprendizaje (medida como el número de ensayos hasta la adquisición de la respuesta) dependía de esta relación, explicando completamente los efectos del espaciado de los ensayos y la contigüidad CS-US.  
  * Estudios recientes y a gran escala con ratas **confirmaron estos hallazgos:** el número de ensayos necesarios para que las ratas aprendieran disminuía a medida que aumentaba la informatividad, mostrando una sorprendente concordancia con los datos de pichones.  
  * La adquisición inicial de la respuesta en ratas fue determinada por la relación C/T. Una **ley cuantitativa con un único parámetro bien establecido** se ajusta a los datos de comportamiento en diversas especies (pichones, conejos, ratones, ratas), protocolos y tipos de reforzamiento con una precisión sin precedentes en la historia del estudio del aprendizaje asociativo.  
  * Un estudio sugirió que el tiempo acumulado en el contexto de condicionamiento, en lugar del número de ensayos, es el determinante principal de la adquisición de la respuesta, aunque se ha detectado un efecto del número de ensayos en diseños intra-sujetos cuando las pruebas se realizan después de pocos ensayos.  
  * Un estudio de comparación de modelos **favoreció decisivamente la ley C/T** sobre la ley I/T (información/Ensayo) para predecir el número de ensayos hasta la adquisición.  
* **Rol de la Dopamina en el Aprendizaje Asociativo y Causal:**

  * La **liberación de dopamina en el estriado ventral refleja los cambios predichos por las señales en las tasas de reforzamiento**, lo que es consistente con que los sujetos comprendan las relaciones temporales entre los eventos de la tarea.  
  * Si bien la hipótesis más aceptada es que la dopamina mesolímbica transmite una **señal de error de predicción de recompensa por diferencia temporal (TDRPE)**, existe evidencia considerable y creciente **inconsistente con esta hipótesis**.  
  * Una teoría alternativa, **Contingencia Neta Ajustada para Relaciones Causales (ANCCR)**, propone que la dopamina es una señal de enseñanza para el aprendizaje causal.  
  * El modelo ANCCR infiere si una señal es una causa de recompensa midiendo si precede a la recompensa más de lo esperado por azar. Este modelo es **consistente con simulaciones de resultados clásicos que apoyan la hipótesis de TDRPE** (como las respuestas dopaminérgicas a la magnitud y probabilidad de la recompensa, el bloqueo, el desbloqueo, la sobreexpectativa y la inhibición condicionada).  
  * Los datos experimentales han mostrado que las dinámicas de liberación de dopamina en el Núcleo Accumbens (NAcc) son **inconsistentes con la TDRPE en múltiples experimentos, pero sí consistentes con el algoritmo de aprendizaje causal ANCCR**. Incluso, los "errores de predicción" relacionados con las tasas de eventos forman parte del marco ANCCR.  
  * A pesar de las promesas de ANCCR, **un estudio reciente encontró que el modelo ANCCR no pudo explicar cualitativa o cuantitativamente los resultados experimentales** en un paradigma con degradación de contingencia y recompensas señalizadas, mientras que un modelo de aprendizaje por diferencia temporal basado en estados de creencia sí lo hizo.  
* **Aprendizaje Dependiente del Contexto y Teoría de las Causas Latentes:**

  * Las diversas funciones del contexto en el aprendizaje (como su papel competitivo, modulador o ignorado) pueden explicarse por **diferentes interpretaciones causales del entorno** inferidas por los animales.  
  * Una **teoría bayesiana** que infiere la estructura causal latente que mejor explica el historial de entrenamiento de un animal puede dar cuenta de fenómenos como la **renovación dependiente del contexto** (ABA y ABC) y la **inhibición latente**.  
  * En la renovación, el modelo predice que cuando el animal regresa a un contexto de condicionamiento previo, infiere que la causa latente original está activa nuevamente, lo que lleva a la reaparición de la respuesta condicionada.  
  * Para la inhibición latente, el modelo explica que la pre-exposición a un estímulo en el mismo contexto que el condicionamiento posterior ralentiza el aprendizaje, porque el animal atribuye una causa latente común a ambas fases. Sin embargo, si la pre-exposición y el condicionamiento ocurren en **contextos diferentes, el efecto de retardo se atenúa**, ya que es más probable que se infieran causas latentes distintas.  
  * Las **lesiones hipocampales** en animales, que alteran su capacidad para inferir nuevos agrupamientos de causas, resultan en un comportamiento cualitativamente similar al observado en las simulaciones del modelo restringido, lo que sugiere un papel crítico del hipocampo en la inferencia de causas latentes.  
* **Limitaciones del Modelo de Rescorla-Wagner (RW):**

  * El modelo de Rescorla-Wagner y sus derivados **presentan problemas fundamentales** al abordar el tiempo y la contingencia en el aprendizaje asociativo.  
  * El modelo RW asume que el aprendizaje se basa en **"ensayos" discretos y la coincidencia temporal**, lo cual es problemático cuando los reforzamientos se programan aleatoriamente (como en los procesos de Poisson), ya que no hay un número definible de "no reforzamientos".  
  * La **dependencia de parámetros libres** que se ajustan para "predecir" los resultados de cada experimento reduce su capacidad predictiva genuina, ya que con suficientes parámetros un modelo puede "contornear" datos aleatorios.  
  * El modelo **no puede explicar fenómenos como la inhibición latente o el condicionamiento de segundo orden** porque no predice aprendizaje en ausencia de errores de predicción.  
  * Además, el modelo RW **no es aplicable directamente al condicionamiento de compuestos seriales** y sus predicciones sobre la tasa de adquisición son inconsistentes con la ley de escala I/T observada empíricamente.  
  * Las ideas de Rescorla (1967, 1968\) sobre la importancia de la información y la contingencia fueron, lamentablemente, **ignoradas en su modelo con Wagner**, llevando a un tratamiento del tiempo empíricamente indefendible en la teoría asociativa.  
* **Evidencia de Aprendizaje de un Solo Ensayo y PREE:**

  * Se observa **aprendizaje asociativo de un solo ensayo** tanto en protocolos pavlovianos como operantes cuando la asociación estadística es suficientemente fuerte.  
  * El **efecto de extinción por reforzamiento parcial (PREE)**, en el cual la extinción es más lenta después de un reforzamiento intermitente, puede no afectar la tasa de aprendizaje si la informatividad (relación C/T) permanece constante, aunque algunos modelos de causas latentes tienen dificultades para explicar este efecto sin suposiciones adicionales sobre las representaciones de la tasa de reforzamiento.  
* **Substratos Neurales de la Incertidumbre y el Conocimiento Relacional:**

  * Estudios sobre los sustratos neurales de los cálculos de incertidumbre han implicado la **corteza cingulada, la corteza prefrontal rostrolateral (polo frontal) y la corteza prefrontal dorsolateral**, así como los sistemas dopaminérgico, colinérgico y noradrenérgico.  
  * Además, existe evidencia creciente que apoya el papel crítico del **sistema hipocampal-entorinal y la corteza prefrontal ventromedial (vmPFC)** en la representación de conocimiento relacional más sofisticado y la estructura de diferentes tipos de dimensiones de tareas.

Estos hallazgos demuestran una evolución significativa en la comprensión del aprendizaje, alejándose de modelos simplistas basados en la contigüidad y avanzando hacia teorías que consideran el papel de la información, la inferencia causal y las complejidades temporales en cómo los organismos aprenden y se adaptan a su entorno.

¡Claro\! Aquí tienes dos presentaciones detalladas, una para ti (con un enfoque más experto) y otra para estudiantes (con un enfoque introductorio), basándome en la información proporcionada en los materiales y nuestra conversación.

---

## **Presentación 1: Para el Experto**

### **Profundización en la Teoría de la Información y el Filtro de Kalman en el Aprendizaje Asociativo: Una Perspectiva Basada en Tasas y Reconocimiento Bayesiano**

Esta presentación profundiza en dos marcos teóricos fundamentales que han revolucionado la comprensión del aprendizaje asociativo, particularmente en el condicionamiento clásico y operante: la Teoría de la Información (a través de la Estimación de Tasas, RET) y el Filtro de Kalman, enmarcados en una perspectiva bayesiana que enfatiza el rol de la incertidumbre.

#### **I. Teoría de la Información y Estimación de Tasas (RET)**

La Teoría de la Información, formalizada por Shannon, proporciona las herramientas para **cuantificar la incertidumbre y la información** \[Latham.pdf\]. En el aprendizaje asociativo, esto se traduce en una visión radicalmente diferente de cómo los organismos adquieren conocimiento sobre las relaciones entre eventos.

* **Fundamentos y Críticas a Modelos Tradicionales:**

  * Los modelos clásicos de condicionamiento, como el de Rescorla-Wagner (RW), se centran en la **contigüidad temporal y las probabilidades** de los eventos. Sin embargo, Rescorla (1967, 1968\) ya había demostrado que la **contingencia** (qué tan informativo es un EC sobre un EI) es el factor crucial, no solo el emparejamiento temporal.  
  * Una crítica central a los modelos basados en la probabilidad (como RW) es su dependencia de la noción de "ensayos" discretos, lo cual es problemático en entornos de tiempo continuo donde los refuerzos se programan estocásticamente (ej., procesos de Poisson). No hay una forma "principial" de definir ensayos no reforzados, y al hacer los "ensayos" hipotéticos cada vez más cortos, la probabilidad de refuerzo se desvanece, haciendo que la teoría pierda su capacidad predictiva.  
  * RET, en contraste, se basa en la **estimación de tasas de refuerzo** (eventos por unidad de tiempo) en lugar de probabilidades. Las tasas, a diferencia de las probabilidades, tienen unidades temporales y pueden ser aditivas, lo que es crucial para la asignación de crédito.  
* **Informatividad (Relación C/T) y su Medición:**

  * La **informatividad (ɩ)** es una **relación adimensional** que compara la tasa de refuerzo en presencia del Estímulo Condicionado (EC), λR|CS, con la tasa de refuerzo contextual, λR|C.  
  * **Gibbon y Balsam (1981)** la denominaron **relación C/T** (Ciclo/Tiempo), donde C es el intervalo promedio US-US (o duración del ciclo) y T es la duración del EC.  
  * El **logaritmo de la informativad es la información mutua**, que cuantifica la reducción de incertidumbre (entropía) sobre el EI que proporciona el EC. Cuantifica los "bits" de información comunicados por el EC.  
  * La informativdad es el **parámetro clave que determina la velocidad de adquisición** del condicionamiento. Valores altos de informativdad (ej., \>100) pueden llevar a un **aprendizaje de un solo ensayo (one-shot learning)**.  
  * La **curva de aprendizaje se escala con el logaritmo de la relación C/T**. Esto explica por qué el espaciamiento entre ensayos y la contigüidad temporal son interdependientes en la tasa de aprendizaje.  
* **Asignación de Crédito:**

  * La teoría de la información ofrece una solución al problema de la asignación de crédito, es decir, cómo los sujetos atribuyen el refuerzo a eventos, estados o contextos simultáneos.  
  * Esto se basa en la **aditividad de las tasas de refuerzo**. La informativdad es crucial; la información sobre el EI proporcionada por un EC se atribuye a ese EC, lo que reduce la información atribuida al contexto simultáneamente presente.  
  * Esto explica fenómenos como el **bloqueo (blocking)** y el **superaprendizaje (overshadowing)**, donde un EC previamente condicionado o más saliente reduce el aprendizaje de otro EC redundante.  
* **Incertidumbre y Divergencia de Kullback-Leibler (DKL):**

  * La **entropía (H)** mide la incertidumbre de un sistema sobre sus posibles estados \[Latham.pdf\]. La información es la reducción de esta incertidumbre \[Latham.pdf\].  
  * La **Divergencia de Kullback-Leibler (DKL)** cuantifica la divergencia entre dos distribuciones \[Latham.pdf\]. Se utiliza como una medida de la **fuerza de la evidencia** de que dos distribuciones (ej., la de refuerzo en presencia del EC y en su ausencia) difieren \[Latham.pdf\].  
  * El **costo de codificación acumulado (nDKL)** mide los bits de memoria "desperdiciados" al codificar datos bajo una suposición incorrecta sobre su distribución, reflejando la fuerza de la evidencia de la diferencia.  
* **Aplicaciones y Hallazgos Neurobiológicos:**

  * RET explica fenómenos como la **inhibición latente** (exposición previa al EC reduce el aprendizaje posterior) y los **efectos de recuperación post-entrenamiento** (ej., des-superaprendizaje) al manipular la informativdad de los estímulos.  
  * La teoría predice que el aprendizaje es **invariante a la escala temporal**; es decir, lo que importa son las relaciones relativas entre las duraciones de los eventos, no sus valores absolutos. Esto explica por qué el condicionamiento por aversión al veneno puede ocurrir con horas de retraso.  
  * La **liberación de dopamina** en el estriado ventral refleja cambios predichos por el EC en las tasas de refuerzo. Esto apoya la idea de que los animales comprenden las relaciones temporales métricas entre los eventos de la tarea. Sin embargo, la señalización de dopamina es objeto de debate, con el modelo ANCCR (Adjusted Net Contingency for Causal Relations) proponiendo que la dopamina señala asociaciones causales en lugar del error de predicción de recompensa por diferencia temporal (TDRPE). Aunque las predicciones del ANCCR pueden parecerse a las del TDRPE en diseños estándar, tests correlacionales y causales han encontrado que la dopamina se ajusta más a la señalización del ANCCR en ciertos escenarios.

#### **II. El Filtro de Kalman y el Aprendizaje Bayesiano**

El filtro de Kalman es un **modelo canónico en el condicionamiento clásico** que explica cómo la incertidumbre impulsa el aprendizaje. Se inscribe en el marco más amplio del **aprendizaje bayesiano de refuerzo**, donde la inferencia probabilística es clave.

* **Propósito y Fundamentos:**

  * El filtro de Kalman estima estados a lo largo del tiempo a partir de **observaciones incompletas y ruidosas**.  
  * A diferencia de las reglas de aprendizaje tradicionales (ej., Rescorla-Wagner), los modelos bayesianos, como el filtro de Kalman, **integran explícitamente la incertidumbre del animal** en el proceso de aprendizaje.  
  * **Tratamientos bayesianos** implican dos componentes:  
    1. **Modelo Generativo del Entorno:** Una representación probabilística del mundo que especifica propiedades como la **volatilidad** (cambios impredecibles) y el **ruido de las observaciones**. En el KF estándar, asume que las asociaciones son **pesos aditivos lineales**.  
    2. **Modelo de Reconocimiento:** Actualiza las creencias del animal (expectativas previas) con las nuevas observaciones (probabilidades) para generar nuevas creencias (expectativas posteriores). La operación de este modelo es el algoritmo de aprendizaje.  
* **Dinámica del Aprendizaje y Manejo de la Incertidumbre:**

  * El filtro de Kalman se basa en el **mismo error de predicción que Rescorla-Wagner** \[Dayan.pdf, Gershman15\_KTD.pdf\].  
  * La **ganancia de Kalman (αi(n))** actúa como la tasa de aprendizaje, pero, a diferencia de RW, **se ajusta dinámicamente con el tiempo en función de la incertidumbre** \[Dayan.pdf\]. Las tasas son más altas para estímulos cuyos pesos son inciertos \[Dayan.pdf\].  
  * La incertidumbre disminuye con cada observación y aumenta debido a un "paseo aleatorio" (random walk) en los pesos, modelando la volatilidad del entorno \[Dayan.pdf\]. Para entornos donde la incertidumbre sobre la asociación también es ignorada o cambia, se utilizan modelos como el **Filtro Gaussiano Jerárquico** o el **Filtro de Kalman volátil**.  
* **Explicación de Fenómenos de Aprendizaje:**

  * El filtro de Kalman explica fenómenos como el **bloqueo y el superaprendizaje**, donde la aditividad en la predicción está ligada a la competencia en el aprendizaje \[Dayan.pdf, 182, 186, 264\]. También captura la **anticorrelación de estimaciones** cuando múltiples elementos se asocian con el mismo resultado \[Dayan.pdf\].  
  * Puede modelar la **inhibición latente**, ya que la exposición previa al EC reduce la incertidumbre posterior y, por tanto, la ganancia de Kalman (tasa de aprendizaje) \[Dayan.pdf, 193, 235\].  
  * Explica una gama más amplia de **fenómenos de recuperación post-entrenamiento**, como el desbloqueo (unblocking) y la sobreexpectativa (unoverexpectation), donde el entrenamiento compuesto lleva a la adquisición de covarianza negativa entre los elementos del estímulo \[Dayan.pdf, 182, 192, 392\].  
  * **Aprendizaje dependiente del contexto:** Los modelos bayesianos pueden explicar cómo el contexto (el entorno donde ocurre el aprendizaje) influye en la recuperación y transferencia del aprendizaje. Esto se logra mediante la **inferencia bayesiana sobre estructuras causales latentes**. Las diferentes funciones del contexto (competencia, modulación, irrelevancia) se corresponden con distintas interpretaciones causales del entorno.  
* **Limitaciones y Extensiones:**

  * El filtro de Kalman convencional es un **modelo a nivel de ensayo** y no puede explicar las actualizaciones de valor **dentro del ensayo** (within-trial value updates) ni fenómenos como el condicionamiento de segundo orden \[Dayan.pdf, 267\].  
  * El **Filtro de Kalman de Diferencia Temporal (Kalman TD)** es una extensión que **unifica las fortalezas del filtro de Kalman y el aprendizaje TD** \[Dayan.pdf, 178, 179, 185, 188, 267\]. Es un **modelo en tiempo real** que representa una distribución sobre los pesos y puede capturar la estructura dentro del ensayo y la revaluación retrospectiva \[Dayan.pdf, 185, 188, 267\]. Puede explicar fenómenos complejos que ninguno de los modelos por sí solo puede justificar, como el superaprendizaje y el condicionamiento de segundo orden o la extinción de segundo orden \[Dayan.pdf\].

#### **III. Conclusión**

La adopción de marcos como la Teoría de la Información y el Aprendizaje Bayesiano (incluido el Filtro de Kalman y sus extensiones) representa un cambio fundamental en la modelización del aprendizaje asociativo. Estos enfoques superan las limitaciones de los modelos tradicionales basados en contigüidad y probabilidad, al proporcionar **explicaciones cuantitativas, basadas en tasas y sensibles a la incertidumbre del organismo**. Este cambio no solo mejora la comprensión de una amplia gama de fenómenos conductuales, sino que también ofrece un marco más robusto para investigar los mecanismos neurobiológicos subyacentes, como la dinámica de la dopamina, proporcionando un puente más sólido entre la computación y la representación en el aprendizaje asociativo.

---

## **Presentación 2: Para Estudiantes**

### **Explorando el Aprendizaje: Cómo los Animales Usan la Información y Predicen Eventos**

¡Hola a todos\! Hoy vamos a hablar de cómo los animales, ¡y también nosotros\!, aprendemos a anticipar lo que va a pasar en el mundo. No es tan simple como parece, y para entenderlo, vamos a usar ideas de dos áreas geniales: la Teoría de la Información y algo llamado el Filtro de Kalman.

#### **Parte 1: ¡La Información es Clave\! (Teoría de la Información)**

Imagina que eres un ratón en un laboratorio. Una luz se enciende (ese es el Estímulo Condicionado o EC), y un momento después, recibes una pequeña descarga (el Estímulo Incondicionado o EI). ¿Cómo aprende el ratón que la luz predice la descarga?

* **No es solo "juntos":**

  * Antes, se pensaba que aprender era solo que el EC y el EI ocurrieran "juntos" o muy cerca en el tiempo.  
  * Pero ¡sorpresa\! Investigaciones clave demostraron que lo que realmente importa es si el EC te da **información nueva y útil** sobre el EI. Es como un detective: no solo la presencia de pistas, sino cuánto te ayudan a resolver el misterio.  
* **¿Qué es la "Informatividad"?**

  * En lugar de solo ver si algo ocurre o no, pensamos en **tasas**: cuántas descargas por minuto cuando la luz está encendida, versus cuántas descargas por minuto cuando la luz está apagada (el "fondo" o contexto).  
  * La "Informatividad" es una medida de esto. Es una **relación entre la tasa de refuerzo durante el EC y la tasa de refuerzo en el contexto**.  
  * **Imagina:** Si la luz se enciende y la tasa de descargas sube mucho, la luz es muy informativa. Si la tasa es la misma con o sin la luz, la luz no te da ninguna información.  
* **La Informatividad y la Velocidad de Aprendizaje:**

  * ¡Esta es la parte interesante\! Cuanto **más alta sea la informativdad, más rápido aprenderá el animal**.  
  * A veces, si la informativdad es *muy* alta (por ejemplo, el EC es una señal perfecta), el aprendizaje puede ocurrir en un **solo ensayo** (¡"one-shot learning"\!). Es como aprender algo al instante porque la señal es súper clara.  
  * Esto explica por qué la forma en que espaciamos los "ensayos" (el tiempo entre ellos) es tan importante. No es solo el tiempo, sino cómo afecta la *informatividad*.  
* **¿Quién se Lleva el Crédito?**

  * A veces, hay varias pistas al mismo tiempo. Por ejemplo, una luz y un sonido se encienden juntos antes de la descarga. ¿Cuál de los dos recibe el "crédito" por predecir la descarga?.  
  * Esta teoría dice que la forma en que el animal "asigna el crédito" se basa en cómo cada pista individualmente (y en relación con el contexto) reduce la incertidumbre sobre la descarga.  
  * Esto nos ayuda a entender el **bloqueo**: si ya sabes que la luz predice la descarga, y luego añades un sonido a la luz, es probable que no aprendas mucho sobre el sonido, porque la luz ya se llevó todo el crédito informativo.  
* **El Tiempo Importa, ¡pero de otra manera\!**

  * La teoría dice que el aprendizaje es **independiente de la escala temporal**. Esto significa que, si las relaciones de tiempo (las *proporciones* de tiempo) son las mismas, un animal puede aprender una asociación con un retraso de segundos o incluso de horas. ¡Piensa en la aversión al veneno, donde un sabor puede asociarse con la náusea horas después\!.  
* **La Dopamina y la Información:**

  * ¿Cómo sabe el cerebro todo esto? La **dopamina**, una sustancia química en el cerebro, parece estar involucrada. Se ha visto que los niveles de dopamina cambian para reflejar lo bien que las señales predicen las recompensas.

#### **Parte 2: El Cerebro como un "Filtro" Inteligente (El Filtro de Kalman y Aprendizaje Bayesiano)**

Ahora, veamos cómo el cerebro maneja la incertidumbre de una manera muy inteligente, como un "filtro" sofisticado.

* **¿Por qué un "Filtro"?**

  * El cerebro está constantemente tratando de adivinar el "estado" real del mundo, incluso cuando las señales que recibe son incompletas o ruidosas. El **Filtro de Kalman** es una herramienta matemática que hace exactamente esto: estima lo que está pasando, incluso con información imperfecta.  
  * En el aprendizaje, la **incertidumbre es el motor**. Los animales aprenden *porque* hay cosas inciertas en el mundo que necesitan predecir.  
* **Aprendizaje "Inteligente":**

  * A diferencia de modelos más simples que aprenden a una velocidad fija, los modelos como el Filtro de Kalman son más "inteligentes". Tienen una **tasa de aprendizaje que se ajusta a la incertidumbre**.  
  * Esto significa que si el animal está muy inseguro sobre algo, aprenderá rápidamente. A medida que se vuelve más seguro, su ritmo de aprendizaje se ralentiza.  
* **El Contexto Importa, ¡y mucho\!**

  * El **entorno o contexto** (por ejemplo, la habitación donde se aprende) no es solo un fondo pasivo. Puede influir en el aprendizaje de diferentes maneras.  
  * Los modelos bayesianos sugieren que el cerebro **infiere la "estructura causal"** del entorno. Por ejemplo, si aprendes algo en la habitación A, y luego se "extingue" en la habitación B, cuando vuelvas a la habitación A, el aprendizaje original puede "volver" (fenómeno de renovación) porque el contexto te indica que estás en una situación diferente.  
* **Modelos Aún Más Avanzados:**

  * Existen versiones más complejas, como el **Filtro de Kalman de Diferencia Temporal (Kalman TD)**, que combinan las fortalezas del Filtro de Kalman con otras ideas de aprendizaje para entender cómo el cerebro predice recompensas futuras y actualiza esas predicciones en tiempo real.

#### **Conclusión**

En resumen, la ciencia del aprendizaje ha avanzado mucho más allá de la simple idea de "asociaciones". Ahora entendemos que el cerebro es un sistema increíblemente sofisticado que constantemente **procesa información, maneja la incertidumbre y ajusta su aprendizaje** basándose en qué tan informativas son las señales sobre los eventos futuros. Esto nos da una imagen mucho más completa y fascinante de cómo aprendemos y predecimos el mundo que nos rodea.

Este documento es una guía de estudio exhaustiva sobre teorías y modelos computacionales del aprendizaje, enfocándose en cómo los sistemas, incluidos los cerebros, adquieren y procesan información para adaptarse a su entorno. Se estructura en tres secciones principales: la primera explora los conceptos fundamentales de la teoría de la información según Gallistel, como la entropía y la información mutua, y su aplicación para entender la fiabilidad del "aprendizaje de una sola toma". La segunda sección detalla modelos computacionales propuestos por Gershman y otros, incluyendo los modelos de aprendizaje por diferencia temporal (TD) y la representación del tiempo, además de la inferencia bayesiana en el aprendizaje causal. Finalmente, la tercera parte vincula la teoría con la práctica, presentando hallazgos experimentales con ratas y la relación con las respuestas dopaminérgicas, y discute cómo estos modelos abordan el problema de asignación de crédito en el aprendizaje por refuerzo sin recurrir a conceptos tradicionales.

Temas clave

Teoría de Información

Modelos Computacionales

Aprendizaje Reforzado

Inferencia Bayesiana

Hallazgos Experimentales

Teorí

1. Teorías y Modelos del Aprendizaje Computacional  
2. Claro, aquí tienes una guía de estudio detallada para ayudarte a repasar el material de origen, incluyendo un cuestionario, preguntas de ensayo y un glosario.  
3. Guía de Estudio: Teorías de Aprendizaje y Modelos Computacionales  
4. Esta guía de estudio está diseñada para revisar los conceptos clave, las metodologías y las conclusiones presentadas en los documentos de Gallistel y Gershman. Presta especial atención a la terminología, las ecuaciones fundamentales y las interpretaciones de los hallazgos experimentales.  
5. I. Conceptos Fundamentales de la Teoría de la Información (Gallistel)  
6. •  
7. Información y Entropía:  
8. ◦  
9. Definición de entropía (H) como medida de incertidumbre de una distribución de probabilidad.  
10. ◦  
11. Unidades de entropía: nats y bits.  
12. ◦  
13. Cómo la entropía se relaciona con la predictibilidad de eventos.  
14. ◦  
15. Concepto de "información disponible" y su relación con el error de medición.  
16. •  
17. Información Mutua (I(x,y)):  
18. ◦  
19. Definición como la reducción promedio de incertidumbre sobre una variable al observar otra.  
20. ◦  
21. Propiedad de simetría: I(x, y) \= I(y, x).  
22. ◦  
23. Interpretación psicológica y neurocientífica.  
24. •  
25. Contingencia Temporal Invariante:  
26. ◦  
27. La importancia del momento en el aprendizaje por refuerzo.  
28. ◦  
29. Conceptos de marcos de referencia temporales: prospectivo y retrospectivo.  
30. ◦  
31. Medidas de información mutua prospectiva y retrospectiva (I(r; R) e I(r; R)).  
32. •  
33. Medición de la Fortaleza de la Evidencia:  
34. ◦  
35. Estadística nDKL como medida de la significancia de la información mutua.  
36. ◦  
37. Distribución de nDKL cuando no hay divergencia (Gamma(0.5,1)).  
38. ◦  
39. Conversión de nDKL a valores p.  
40. ◦  
41. Justificación del "aprendizaje de una sola toma" (one-shot learning) basada en nDKL.  
42. •  
43. Modelado del Aprendizaje y Detección de Cambios:  
44. ◦  
45. La función imax y su uso en la detección de cambios en la tasa o probabilidad de refuerzo.  
46. ◦  
47. El criterio de decisión como único parámetro libre en el modelo de detección de cambios (especialmente en datos de extinción).  
48. •  
49. Estimación de Parámetros Estocásticos:  
50. ◦  
51. Fiabilidad de las estimaciones obtenidas de una muestra de tamaño 1\.  
52. ◦  
53. Uso de priores de Jeffreys para estimaciones bayesianas.  
54. ◦  
55. Formas matemáticas de las distribuciones posteriores (Beta, Gamma, Normal-Gamma) y sus hiperparámetros.  
56. ◦  
57. Fórmulas de actualización para estos parámetros.  
58. II. Modelos Computacionales del Aprendizaje (Gershman, Qian, Namboodiri)  
59. •  
60. Modelos de Aprendizaje por Diferencia Temporal (TD):  
61. ◦  
62. Concepto de error de predicción de recompensa (TD error, δt).  
63. ◦  
64. Cálculo de δt \= rt \+ γV(st+1) \- V(st).  
65. ◦  
66. V(st) como el valor esperado de un estado.  
67. ◦  
68. Factores que afectan la predicción de los modelos TD (representación de estado).  
69. ◦  
70. Aplicación en el modelado de respuestas a olores y señales de dopamina.  
71. •  
72. Representación del Tiempo en el Cerebro:  
73. ◦  
74. "Células de tiempo" (time cells) y su actividad en intervalos específicos.  
75. ◦  
76. Escalas de tiempo espaciadas logarítmicamente (τµ+1 \= (1 \+ k)τµ).  
77. ◦  
78. Funciones de densidad de probabilidad (ϕµ(t)) que cubren el eje del intervalo.  
79. •  
80. Inferencias Bayesianas en el Aprendizaje Causal:  
81. ◦  
82. El uso de la regla de Bayes para actualizar las probabilidades de las causas (πi).  
83. ◦  
84. Log-verosimilitud relativa (ℓi) en la inferencia causal.  
85. ◦  
86. Distribuciones Dirichlet-multinomial para el muestreo de índices de tiempo.  
87. ◦  
88. Cálculo de verosimilitudes logarítmicas para intervalos cue-recompensa y recompensa-recompensa.  
89. ◦  
90. Aproximaciones de Stirling para grandes n y np.  
91. •  
92. Modelos de Contexto:  
93. ◦  
94. Modelos de contexto irrelevante (M1), modulador (M2) y aditivo (M3).  
95. ◦  
96. Actualización de pesos (w) y ganancia de Kalman (gn) en estos modelos.  
97. ◦  
98. Predicciones sobre resultados futuros usando la expectativa predictiva posterior.  
99. •  
100. Filtros de Partículas:  
101. ◦  
102. Generación de partículas muestreando desde el modelo generativo.  
103. ◦  
104. Aproximación de la posterior mediante una suma ponderada de funciones delta.  
105. ◦  
106. Importancia de los pesos de las partículas (wt).  
107. •  
108. Modelo de Estado-Creencia (Belief-State Model):  
109. ◦  
110. Concepto de que el animal mantiene un modelo interno del entorno.  
111. ◦  
112. Representación de las observaciones en un vector multidimensional.  
113. ◦  
114. El parámetro de concentración α y su influencia en la creencia previa sobre el número de causas.  
115. ◦  
116. La relación entre el modelo de estado-creencia y las respuestas de dopamina.  
117. III. Hallazgos Experimentales y Aplicaciones  
118. •  
119. Experimentos con Ratas:  
120. ◦  
121. Estudios con protocolos de contingencia negativa para evaluar el poder explicativo de la informatividad.  
122. ◦  
123. Patrones temporales de respuesta dentro de los estímulos (CS).  
124. ◦  
125. Tasas de poke asintóticas y velocidad de adquisición.  
126. ◦  
127. Experimentos de aprendizaje operante con retrasos en el refuerzo (2-min y 16-min).  
128. ◦  
129. Impacto de la preexposición al contexto en la adquisición.  
130. •  
131. Respuestas Dopaminérgicas:  
132. ◦  
133. Dopamina como señal de error de predicción de recompensa.  
134. ◦  
135. Modelos que recapitulan la dinámica de la dopamina y la actividad axonal de calcio.  
136. ◦  
137. Modulación de la respuesta de dopamina en diferentes condiciones de aprendizaje (condicionamiento, degradación, recompensa señalizada, extinción).  
138. •  
139. El Problema de Asignación de Crédito (Credit Assignment Problem):  
140. ◦  
141. Por qué es un problema central en el aprendizaje por refuerzo.  
142. ◦  
143. Cómo las teorías de la información y los modelos computacionales abordan este problema, obviando la necesidad de "ventanas de asociabilidad" o "trazas de elegibilidad".  
144. ◦  
145. La capacidad del cerebro para resolver el problema de asignación de crédito.  
146. \--------------------------------------------------------------------------------  
147. Cuestionario de Preguntas Cortas  
148. Responde a cada pregunta en 2-3 oraciones.  
149. 1\.  
150. ¿Qué es la entropía en el contexto de la teoría de la información y qué nos dice sobre una distribución de probabilidad?  
151. 2\.  
152. Explica la importancia de la estadística nDKL en el "aprendizaje de una sola toma" según Gallistel.  
153. 3\.  
154. ¿Cómo se relaciona el "criterio de decisión" con la función imax en el modelo de detección de cambios de Gallistel, particularmente en el contexto de los datos de extinción?  
155. 4\.  
156. Describe brevemente cómo se representan las "células de tiempo" en los modelos computacionales y qué implicación tiene su espaciado logarítmico.  
157. 5\.  
158. ¿Cuál es la función principal de los modelos de aprendizaje por diferencia temporal (TD) y qué señal clave utilizan para el aprendizaje?  
159. 6\.  
160. En el marco bayesiano, ¿cómo se calcula la log-verosimilitud relativa (ℓi) y qué papel juega en la inferencia causal?  
161. 7\.  
162. Menciona y describe brevemente dos de los tres modelos de contexto (M1, M2, M3) discutidos en los textos.  
163. 8\.  
164. Según los experimentos con ratas, ¿qué efecto tienen los retrasos prolongados en el refuerzo sobre el aprendizaje operante y cómo se midió esto?  
165. 9\.  
166. ¿Cómo abordan los modelos presentados el "problema de asignación de crédito" en el aprendizaje por refuerzo, y qué conceptos tradicionales buscan evitar?  
167. 10\.  
168. Explica por qué la información mutua no puede ser negativa en el contexto de estos estudios.  
169. \--------------------------------------------------------------------------------  
170. Clave de Respuestas del Cuestionario  
171. 1\.  
172. \*\*¿Qué es la entropía en el contexto de la teoría de la información y qué nos dice sobre una distribución de probabilidad?\*\*La entropía (H) es una medida de la incertidumbre o aleatoriedad de una distribución de probabilidad. Una entropía alta indica una mayor incertidumbre sobre el resultado de un evento, mientras que una entropía baja sugiere una mayor predictibilidad o menos incertidumbre.  
173. 2\.  
174. \*\*Explica la importancia de la estadística nDKL en el "aprendizaje de una sola toma" según Gallistel.\*\*La estadística nDKL permite juzgar la fiabilidad de las estimaciones de parámetros estocásticos obtenidas de una muestra de tamaño 1\. Su cálculo permite determinar cuándo el aprendizaje de una sola toma está justificado por una evidencia fuerte, lo que se asume que explica las circunstancias en las que los cerebros llegan a la misma conclusión.  
175. 3\.  
176. \*\*¿Cómo se relaciona el "criterio de decisión" con la función imax en el modelo de detección de cambios de Gallistel, particularmente en el contexto de los datos de extinción?\*\*El criterio de decisión es el único parámetro en el modelo de detección de cambios de Gallistel. Cuando la función imax detecta un cambio, este criterio se utiliza para estimar el refuerzo en el que ocurrió el cambio. Al aplicar el modelo a los datos de extinción, se estima el criterio de decisión, lo que lo convierte en un parámetro no libre para análisis posteriores.  
177. 4\.  
178. \*\*Describe brevemente cómo se representan las "células de tiempo" en los modelos computacionales y qué implicación tiene su espaciado logarítmico.\*\*Las "células de tiempo" son unidades que se activan en intervalos de tiempo específicos después de un estímulo. En algunos modelos, las escalas de tiempo de estas células están espaciadas logarítmicamente (τµ+1 \= (1 \+ k)τµ), lo que permite que las funciones de densidad de probabilidad cubran un amplio rango de duraciones de intervalo.  
179. 5\.  
180. \*\*¿Cuál es la función principal de los modelos de aprendizaje por diferencia temporal (TD) y qué señal clave utilizan para el aprendizaje?\*\*Los modelos TD simulan cómo los animales aprenden a predecir futuras recompensas basándose en la experiencia. La señal clave que utilizan es el "error de predicción de recompensa" (TD error, δt), que se calcula como la diferencia entre la recompensa obtenida más el valor futuro descontado y el valor predicho del estado actual.  
181. 6\.  
182. \*\*En el marco bayesiano, ¿cómo se calcula la log-verosimilitud relativa (ℓi) y qué papel juega en la inferencia causal?\*\*La log-verosimilitud relativa (ℓi) se calcula como el logaritmo de la razón de la verosimilitud de observar los datos dada una causa 'i' en comparación con una causa de referencia 'r'. Juega un papel crucial en la regla de Bayes, permitiendo actualizar las probabilidades posteriores de las causas basándose en la evidencia observada.  
183. 7\.  
184. \*\*Menciona y describe brevemente dos de los tres modelos de contexto (M1, M2, M3) discutidos en los textos.\*\*El modelo de contexto irrelevante (M1) asume que la media de la recompensa depende linealmente de las características del estímulo. El modelo de contexto modulador (M2) propone que los pesos de las características del estímulo son específicos para cada contexto, lo que significa que el efecto de un estímulo en la recompensa varía según el contexto.  
185. 8\.  
186. \*\*Según los experimentos con ratas, ¿qué efecto tienen los retrasos prolongados en el refuerzo sobre el aprendizaje operante y cómo se midió esto?\*\*Los experimentos demostraron que los retrasos prolongados en el refuerzo (2 y 16 minutos) resultaban en una adquisición más lenta del aprendizaje operante, ya que las ratas presionaban la palanca menos que sus contrapartes control. Esto se midió observando las tasas de presión de palanca y la información mutua prospectiva y retrospectiva a lo largo del tiempo de entrenamiento.  
187. 9\.  
188. \*\*¿Cómo abordan los modelos presentados el "problema de asignación de crédito" en el aprendizaje por refuerzo, y qué conceptos tradicionales buscan evitar?\*\*Los modelos abordan el problema de asignación de crédito al permitir que el sistema compute la información mutua entre respuestas y refuerzos a través de estimaciones de parámetros de distribución, obviando la necesidad de postular "ventanas de asociabilidad", "trazas de elegibilidad" o "estados" intermedios.  
189. 10\.  
190. \*\*Explica por qué la información mutua no puede ser negativa en el contexto de estos estudios.\*\*La información mutua se define como la reducción promedio de incertidumbre. Dado que la incertidumbre (entropía) es una cantidad no negativa, y la información mutua es una medida de cuánto se reduce esa incertidumbre, el valor mínimo posible para la información mutua es cero (cuando las variables son independientes y no hay reducción de incertidumbre). Por lo tanto, no puede ser negativa.  
191. \--------------------------------------------------------------------------------  
192. Preguntas en Formato de Ensayo  
193. 1\.  
194. Discute la relación entre la entropía, la información disponible y la información mutua. ¿Cómo se utilizan estos conceptos para comprender el procesamiento de la información en el cerebro según Gallistel?  
195. 2\.  
196. Compara y contrasta las perspectivas sobre el aprendizaje por refuerzo ofrecidas por los modelos basados en la teoría de la información (Gallistel) y los modelos de diferencia temporal (Gershman, Qian). ¿Cuáles son las fortalezas y debilidades de cada enfoque en la explicación del comportamiento?  
197. 3\.  
198. Analiza la importancia del tiempo en el aprendizaje, tanto desde la perspectiva de la contingencia temporal invariante de Gallistel como desde la representación del tiempo en las "células de tiempo" de Gershman. ¿Cómo influyen estas representaciones temporales en la adquisición del conocimiento y la toma de decisiones?  
199. 4\.  
200. Explica en detalle el "problema de asignación de crédito" en el aprendizaje por refuerzo. ¿Cómo proponen los autores (Gallistel y Gershman) que el cerebro resuelve este problema, y qué implicaciones tienen sus modelos para nuestra comprensión de la cognición animal?  
201. 5\.  
202. Describe cómo se utiliza la inferencia bayesiana en los modelos computacionales de aprendizaje presentados. Incluye una discusión sobre la actualización de probabilidades, el uso de priors y la importancia de la verosimilitud en la formación de nuevas asociaciones.  
203. \--------------------------------------------------------------------------------  
204. Glosario de Términos Clave  
205. •  
206. Adquisición (Acquisition): El proceso mediante el cual un organismo aprende una nueva respuesta o asociación. En el contexto de los estudios, a menudo se mide por la tasa de poke asintótica o los pellets hasta la adquisición.  
207. •  
208. Aprendizaje de una sola toma (One-shot learning): La capacidad de aprender de manera efectiva de un solo ensayo o una cantidad mínima de datos, justificada por una fuerte evidencia estadística (e.g., alta nDKL).  
209. •  
210. Células de tiempo (Time cells): Neuronas o unidades computacionales que se activan en un momento específico o en un intervalo de tiempo después de un evento inicial, lo que se cree que codifica la información temporal en el cerebro.  
211. •  
212. Contingencia: La relación probabilística entre un estímulo (CS) y un resultado (US) o entre una respuesta y un refuerzo. En los textos, se enfatiza la contingencia temporal invariante.  
213. •  
214. Criterio de decisión (Decision criterion): Un umbral utilizado en los modelos de detección de cambios para determinar cuándo se ha producido un cambio significativo en la tasa o probabilidad de refuerzo.  
215. •  
216. Distribución Gamma (Gamma distribution): Una distribución de probabilidad continua utilizada para modelar la distribución del nDKL en ausencia de divergencia, así como otras variables relacionadas con el tiempo de espera.  
217. •  
218. DKL (Kullback-Leibler divergence): Una medida de la diferencia entre dos distribuciones de probabilidad. Se utiliza en el nDKL para cuantificar la fuerza de la evidencia estadística.  
219. •  
220. Entropía (Entropy, H): En la teoría de la información, una medida de la incertidumbre o la aleatoriedad inherente a una distribución de probabilidad.  
221. •  
222. Error de predicción de recompensa (Reward-prediction error, RPE, δ): En los modelos de diferencia temporal (TD), la discrepancia entre la recompensa esperada y la recompensa realmente recibida, que impulsa el aprendizaje.  
223. •  
224. Extinción: La disminución o desaparición de una respuesta condicionada cuando el estímulo condicionado se presenta repetidamente sin el estímulo incondicionado o cuando una respuesta ya no es reforzada.  
225. •  
226. Ganancia de Kalman (Kalman gain, gn): Un vector de tasas de aprendizaje utilizado en modelos de inferencia probabilística (como los modelos de contexto) para actualizar las estimaciones de los pesos basándose en nuevos datos.  
227. •  
228. Hiperparámetros (Hyperparameters): Parámetros de las distribuciones previas en la inferencia bayesiana que controlan la forma de la distribución posterior.  
229. •  
230. Información mutua (Mutual information, I(x,y)): Una medida de la cantidad de información que dos variables aleatorias comparten; cuantifica la reducción de incertidumbre sobre una variable al observar la otra.  
231. •  
232. Informatividad (Informativeness, ι\~T): Una medida relacionada con la información mutua que cuantifica la fuerza de la relación entre estímulos y resultados en protocolos de condicionamiento.  
233. •  
234. Intervalo inter-refuerzo (Inter-reinforcement interval, IRI): El tiempo entre refuerzos sucesivos.  
235. •  
236. Jeffreys prior: Un tipo de distribución previa no informativa utilizada en la inferencia bayesiana, a menudo elegida por su invarianza bajo reparametrizaciones.  
237. •  
238. Lambert W function: Una función matemática utilizada para resolver ecuaciones que involucran exponenciales y productos, aparece en las expresiones para la tasa de adquisición en algunos modelos.  
239. •  
240. Log-verosimilitud (Log-likelihood): El logaritmo de la función de verosimilitud, utilizado en la inferencia bayesiana para simplificar cálculos y manejar números muy pequeños o muy grandes.  
241. •  
242. Nats: Una unidad de información o entropía basada en el logaritmo natural (base e).  
243. •  
244. nDKL: Una estadística de información-teórica que mide la fiabilidad o la significancia de la información mutua, especialmente útil con tamaños de muestra pequeños.  
245. •  
246. Priors: En la inferencia bayesiana, la distribución de probabilidad de un parámetro antes de observar los datos.  
247. •  
248. Problema de asignación de crédito (Credit assignment problem): El desafío de determinar qué acciones o eventos en el pasado son responsables de un resultado particular (positivo o negativo) en el presente, crucial en el aprendizaje por refuerzo.  
249. •  
250. Prospective mutual information (I(r; R)): Una medida de cuánto predice una respuesta la espera del siguiente refuerzo.  
251. •  
252. Retrospective mutual information (I(r; R)): Una medida de cuánto predice el refuerzo más reciente la ocurrencia de la respuesta que lo precedió.  
253. •  
254. Trazas de elegibilidad (Eligibility traces): Conceptos en algunos modelos de aprendizaje (especialmente en TD) que representan el historial reciente de las variables de estado y acción, para asignar crédito a eventos que ocurrieron en el pasado.  
255. •  
256. Valor (Value, V(st)): En los modelos de aprendizaje por refuerzo, la expectativa de la recompensa total futura que se puede obtener a partir de un estado dado.

257. ## Studiochevron\_rightNota

258. collapse\_content  
259. delete  
260. (Las respuestas guardadas son de solo lectura)  
261. Claro, aquí tienes una guía de estudio detallada para ayudarte a repasar el material de origen, incluyendo un cuestionario, preguntas de ensayo y un glosario.

262. ## Guía de Estudio: Teorías de Aprendizaje y Modelos Computacionales

263. Esta guía de estudio está diseñada para revisar los conceptos clave, las metodologías y las conclusiones presentadas en los documentos de Gallistel y Gershman. Presta especial atención a la terminología, las ecuaciones fundamentales y las interpretaciones de los hallazgos experimentales.

264. ### I. Conceptos Fundamentales de la Teoría de la Información (Gallistel)

     * Información y Entropía:Definición de entropía (H) como medida de incertidumbre de una distribución de probabilidad.  
     * Unidades de entropía: nats y bits.  
     * Cómo la entropía se relaciona con la predictibilidad de eventos.  
     * Concepto de "información disponible" y su relación con el error de medición.  
     * Información Mutua (I(x,y)):Definición como la reducción promedio de incertidumbre sobre una variable al observar otra.  
     * Propiedad de simetría: I(x, y) \= I(y, x).  
     * Interpretación psicológica y neurocientífica.  
     * Contingencia Temporal Invariante:La importancia del momento en el aprendizaje por refuerzo.  
     * Conceptos de marcos de referencia temporales: prospectivo y retrospectivo.  
     * Medidas de información mutua prospectiva y retrospectiva (I(r; R) e I(r; R)).  
     * Medición de la Fortaleza de la Evidencia:Estadística nDKL como medida de la significancia de la información mutua.  
     * Distribución de nDKL cuando no hay divergencia (Gamma(0.5,1)).  
     * Conversión de nDKL a valores p.  
     * Justificación del "aprendizaje de una sola toma" (one-shot learning) basada en nDKL.  
     * Modelado del Aprendizaje y Detección de Cambios:La función imax y su uso en la detección de cambios en la tasa o probabilidad de refuerzo.  
     * El criterio de decisión como único parámetro libre en el modelo de detección de cambios (especialmente en datos de extinción).  
     * Estimación de Parámetros Estocásticos:Fiabilidad de las estimaciones obtenidas de una muestra de tamaño 1\.  
     * Uso de priores de Jeffreys para estimaciones bayesianas.  
     * Formas matemáticas de las distribuciones posteriores (Beta, Gamma, Normal-Gamma) y sus hiperparámetros.  
     * Fórmulas de actualización para estos parámetros.

265. ### II. Modelos Computacionales del Aprendizaje (Gershman, Qian, Namboodiri)

     * Modelos de Aprendizaje por Diferencia Temporal (TD):Concepto de error de predicción de recompensa (TD error, δt).  
     * Cálculo de δt \= rt \+ γV(st+1) \- V(st).  
     * V(st) como el valor esperado de un estado.  
     * Factores que afectan la predicción de los modelos TD (representación de estado).  
     * Aplicación en el modelado de respuestas a olores y señales de dopamina.  
     * Representación del Tiempo en el Cerebro:"Células de tiempo" (time cells) y su actividad en intervalos específicos.  
     * Escalas de tiempo espaciadas logarítmicamente (τµ+1 \= (1 \+ k)τµ).  
     * Funciones de densidad de probabilidad (ϕµ(t)) que cubren el eje del intervalo.  
     * Inferencias Bayesianas en el Aprendizaje Causal:El uso de la regla de Bayes para actualizar las probabilidades de las causas (πi).  
     * Log-verosimilitud relativa (ℓi) en la inferencia causal.  
     * Distribuciones Dirichlet-multinomial para el muestreo de índices de tiempo.  
     * Cálculo de verosimilitudes logarítmicas para intervalos cue-recompensa y recompensa-recompensa.  
     * Aproximaciones de Stirling para grandes n y np.  
     * Modelos de Contexto:Modelos de contexto irrelevante (M1), modulador (M2) y aditivo (M3).  
     * Actualización de pesos (w) y ganancia de Kalman (gn) en estos modelos.  
     * Predicciones sobre resultados futuros usando la expectativa predictiva posterior.  
     * Filtros de Partículas:Generación de partículas muestreando desde el modelo generativo.  
     * Aproximación de la posterior mediante una suma ponderada de funciones delta.  
     * Importancia de los pesos de las partículas (wt).  
     * Modelo de Estado-Creencia (Belief-State Model):Concepto de que el animal mantiene un modelo interno del entorno.  
     * Representación de las observaciones en un vector multidimensional.  
     * El parámetro de concentración α y su influencia en la creencia previa sobre el número de causas.  
     * La relación entre el modelo de estado-creencia y las respuestas de dopamina.

266. ### III. Hallazgos Experimentales y Aplicaciones

     * Experimentos con Ratas:Estudios con protocolos de contingencia negativa para evaluar el poder explicativo de la informatividad.  
     * Patrones temporales de respuesta dentro de los estímulos (CS).  
     * Tasas de poke asintóticas y velocidad de adquisición.  
     * Experimentos de aprendizaje operante con retrasos en el refuerzo (2-min y 16-min).  
     * Impacto de la preexposición al contexto en la adquisición.  
     * Respuestas Dopaminérgicas:Dopamina como señal de error de predicción de recompensa.  
     * Modelos que recapitulan la dinámica de la dopamina y la actividad axonal de calcio.  
     * Modulación de la respuesta de dopamina en diferentes condiciones de aprendizaje (condicionamiento, degradación, recompensa señalizada, extinción).  
     * El Problema de Asignación de Crédito (Credit Assignment Problem):Por qué es un problema central en el aprendizaje por refuerzo.  
     * Cómo las teorías de la información y los modelos computacionales abordan este problema, obviando la necesidad de "ventanas de asociabilidad" o "trazas de elegibilidad".  
     * La capacidad del cerebro para resolver el problema de asignación de crédito.

267. ## Cuestionario de Preguntas Cortas

268. Responde a cada pregunta en 2-3 oraciones.  
     * ¿Qué es la entropía en el contexto de la teoría de la información y qué nos dice sobre una distribución de probabilidad?  
     * Explica la importancia de la estadística nDKL en el "aprendizaje de una sola toma" según Gallistel.  
     * ¿Cómo se relaciona el "criterio de decisión" con la función imax en el modelo de detección de cambios de Gallistel, particularmente en el contexto de los datos de extinción?  
     * Describe brevemente cómo se representan las "células de tiempo" en los modelos computacionales y qué implicación tiene su espaciado logarítmico.  
     * ¿Cuál es la función principal de los modelos de aprendizaje por diferencia temporal (TD) y qué señal clave utilizan para el aprendizaje?

