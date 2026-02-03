#   
---

### **Introducción al Nuevo Enfoque**

Para enriquecer el material, propongo organizarlo en torno a los **tres niveles de análisis de David Marr**, un marco conceptual influyente en las ciencias cognitivas. Este enfoque nos permite entender cualquier sistema de procesamiento de información (como el cerebro o un robot) desde tres perspectivas complementarias y jerárquicas:

1. **Nivel Computacional:** ¿Cuál es el **problema** que el sistema resuelve y **por qué**? ¿Cuál es la lógica de la solución?  
2. **Nivel Algorítmico y de Representación:** ¿**Cómo** resuelve el problema el sistema? ¿Qué **algoritmos** y **representaciones** utiliza?  
3. **Nivel de Implementación:** ¿Con **qué** se implementa físicamente el algoritmo? ¿Cuál es el sustrato material (hardware)?

Este marco es ideal para tus notas, ya que el material actual ya contiene los elementos para cada nivel. Simplemente los organizaremos bajo esta estructura y haremos las conexiones con la IA más explícitas.

---

### **Propuesta de Notas del Curso Mejoradas**

Aquí tienes una versión reescrita de las notas, integrando los conceptos solicitados.

#### **Tema 2: Evolución y Principios del Comportamiento Adaptable**

**Introducción: El Problema Fundamental de la Supervivencia**

El problema biológico más fundamental para cualquier organismo es la gestión de la energía1. La vida consume energía constantemente, y esta debe ser reabastecida para mantener el metabolismo y, en última instancia, permitir la reproducción2. La selección natural opera sobre el éxito reproductivo, el cual depende directamente de las acciones que un organismo realiza: encontrar comida, evitar depredadores, y reproducirse3. Estas acciones compiten entre sí por un recurso finito: el tiempo4444.

Para entender cómo la psicología del aprendizaje aborda este desafío, utilizaremos los tres niveles de análisis de David Marr.

---

#### **Nivel 1: La Teoría Computacional del Comportamiento Adaptable (El "Qué" y el "Porqué")**

Este nivel describe el objetivo principal del sistema y la lógica de su estrategia, independientemente de cómo se implemente.

* **El Objetivo (¿Qué se busca?):** El objetivo es distribuir el comportamiento en el tiempo de manera que se maximice el beneficio biológico (acceso a *Sucesos Biológicamente Importantes* o SBI) al menor costo posible55. Los SBI son consecuencias que impactan el éxito reproductivo, como el alimento, la seguridad o la aceptación social6666. No se limitan a necesidades básicas, sino a cualquier variable correlacionada con el éxito reproductivo7777.  
* **Las Restricciones (Las reglas del juego):** La solución a este problema de optimización está sujeta a restricciones:

  * **Restricción Lineal del Tiempo:** El tiempo es finito. El tiempo dedicado a una actividad es tiempo que no se puede dedicar a otras8888. Esto crea una competencia inherente entre todos los comportamientos posibles99. La relación se puede expresar como T=t1​+t2​+...+tn​10101010.  
  *   
  * **Restricciones del Entorno (Propiedades Estadísticas):** Los SBI no están disponibles de forma constante. Su disponibilidad puede ser constante o variable, creando diferentes tipos de problemas adaptativos11111111.  
  *   
* **La Lógica de la Evolución (¿Por qué surgen las soluciones?):** La selección natural ofrece dos tipos de soluciones dependiendo de la variabilidad del entorno:

  * **En Entornos Estables:** Cuando las condiciones ambientales son predecibles y constantes a lo largo de generaciones, la selección natural "codifica" soluciones en forma de **comportamiento adaptado**1212121212121212. Estos son programas conductuales fijos como reflejos, instintos o sesgos13131313.  
  *   
  * **En Entornos Variables e Inciertos:** Cuando las condiciones cambian dentro de la vida de un organismo, la selección favorece mecanismos que permiten el ajuste en tiempo real. Esto da origen al **comportamiento adaptable**, que es lo que llamamos **Aprendizaje**14141414141414. La tarea del organismo es reducir la incertidumbre sobre la ocurrencia de los SBI para poder predecirlos y actuar en consecuencia15151515.  
  *   
* **Conexión con IA y Aprendizaje de Máquina:**

  * El Nivel Computacional se corresponde directamente con el marco del **Aprendizaje por Refuerzo (Reinforcement Learning \- RL)**.  
  * El **agente** (organismo) debe aprender una **política** (distribución del comportamiento) para maximizar una **señal de recompensa** (acceso a los SBI) que obtiene de un **entorno** (el mundo con sus propiedades estadísticas).  
  * El problema de la "distribución óptima" 1616 es análogo a encontrar la "política óptima" en RL.  
  * 

---

#### **Nivel 2: Algoritmos y Representaciones (El "Cómo")**

Este nivel describe los algoritmos (las reglas paso a paso) y las representaciones (la forma de almacenar información) que se usan para resolver el problema computacional.

* **El Problema Central: La Asignación de Crédito:** Si un organismo tiene éxito, ¿cómo sabe qué acción específica o qué señal del entorno fue la responsable? Este es el "problema de la asignación de crédito"17. Para resolverlo, los organismos deben detectar las regularidades estadísticas del entorno18.  
* **Representaciones: ¿Qué se aprende?** Los organismos representan y aprenden sobre las relaciones entre los SBI y cuatro propiedades clave del mundo191919:  
  * **Tiempo:** ¿Cuándo ocurren los SBI? 202020  
  *   
  * **Lugar:** ¿Dónde ocurren los SBI? 212121  
  *   
  * **Covarianza con Estímulos:** ¿Qué señales predicen la ocurrencia de los SBI? (Estructura causal)222222.  
  *   
  * **Covarianza con el Comportamiento:** ¿Qué acciones producen los SBI?232323.  
  *   
* **Algoritmos: ¿Cómo se aprende?** La psicología del aprendizaje ha estudiado diversos algoritmos que los organismos usan para detectar estas regularidades:

  * **Optimización por Ascenso de Colina (Hill Climbing):** Un mecanismo general de reducción de error donde el organismo ajusta su comportamiento gradualmente para moverse hacia un "pico" de mayor beneficio en el "paisaje adaptativo"24242424.  
  *   
  * **Sistemas de Retroalimentación:** Mecanismos que ajustan la acción futura basándose en el error de la acción pasada2525.  
  *   
  * **Mecanismos Asociativos:** Consideran la covarianza (asociación) como el elemento básico del aprendizaje, del cual se derivan las adaptaciones espaciales y temporales26.  
  *   
  * **Detección de Tasas:** Los organismos no solo detectan eventos individuales, sino también características de segundo orden como la **tasa de ocurrencia** de SBI (\# de eventos / tiempo) 27272727, y ajustan su comportamiento en consecuencia28282828.  
  *   
* **Desafíos Algorítmicos Adicionales:**

  * **Control de Estímulos:** Las regularidades pueden cambiar dependiendo del contexto (ej. noche/día)29292929.  
  *   
  * **Estados Ocultos y Extinción:** El entorno puede cambiar sin una señal externa obvia. El organismo debe inferir si un cambio es temporal o permanente30303030. Esto se estudia clásicamente bajo el fenómeno de la **extinción**31313131.  
  *   
  * **Incertidumbre de Nivel Superior:** La incertidumbre sobre las tasas, tiempos o covarianzas puede ser **esperada** (lanzar una moneda justa) o **inesperada** (la moneda está sesgada y el sesgo cambia con el tiempo)323232323232323232.  
  *   
* **Conexión con IA y Aprendizaje de Máquina:**

  * El **problema de asignación de crédito** es el desafío central en el Aprendizaje por Refuerzo, especialmente con recompensas demoradas. Algoritmos como *Temporal Difference (TD) Learning* y *Q-Learning* son soluciones para esto.  
  * La **detección de covarianzas** es análoga al aprendizaje supervisado y a los modelos asociativos en redes neuronales.  
  * El **control por estímulos** es similar al concepto de *Contextual Bandits* en IA.  
  * El problema de los **estados ocultos** se modela en IA usando *Modelos Ocultos de Márkov (HMM)* y *Procesos de Decisión de Márkov Parcialmente Observables (POMDPs)*.  
  * La **detección de tasas** es fundamental en los algoritmos de RL, donde se estima el valor de un estado o acción como una tasa de recompensa futura esperada.

---

#### **Nivel 3: Implementación Física (El "Con Qué")**

Este nivel describe el "hardware" o sustrato físico en el que se ejecutan los algoritmos.

* **En Organismos Biológicos:** La implementación es el **sistema nervioso**3333. La selección natural opera sobre las estructuras (genes, neuronas, circuitos) que subyacen a los mecanismos del comportamiento adaptable34343434. Por ejemplo, la plasticidad sináptica es un mecanismo de hardware fundamental para el aprendizaje.  
* **En Sistemas Artificiales (Robots):** La implementación consiste en **circuitos de silicio (CPUs, GPUs), sensores (cámaras, sonares) y actuadores (motores, ruedas)**35353535. El diseño de un robot como Wall-E en un entorno variable requiere que el ingeniero modele las propiedades estadísticas de ese entorno y las incorpore en el software del robot, que corre sobre este hardware36363636. Un robot diseñado para un entorno fijo no necesitaría estos complejos mecanismos de aprendizaje37373737.  
* **Conexión con IA y Aprendizaje de Máquina:**

  * Este nivel representa la diferencia entre el *software* (el modelo de IA, el algoritmo de aprendizaje) y el *hardware* (los chips de Nvidia, Google TPUs, etc.) sobre el que se entrena y se ejecuta.  
  * El campo de la **computación neuromórfica** intenta construir chips que imiten la estructura y el funcionamiento del cerebro biológico, uniendo así la implementación biológica y artificial.

**Conclusión del Curso**

El objeto de estudio de la Psicología del Aprendizaje es la **adaptabilidad del comportamiento**38383838. Al analizar este fenómeno a través de los niveles de Marr, vemos que el aprendizaje no es un proceso arbitrario, sino una solución elegante moldeada por la evolución para resolver el problema fundamental de la supervivencia en mundos inciertos y cambiantes. El estudio de soluciones óptimas 39 y de los algoritmos y heurísticos que las generan 40404040 nos permite entender la profunda lógica de la mente.

---

### **Propuesta de Nueva Presentación de Diapositivas (Esquema)**

**Título: La Lógica del Comportamiento Adaptable: De la Evolución a la IA**

* **Diapositiva 1: Título**

  * Evolución de la Adaptabilidad del Comportamiento  
  * Arturo Bouzas, ACA I, 2023  
* **Diapositiva 2: El Problema Fundamental**

  * El problema biológico: reabastecer la energía consumida41.  
  *   
  * La solución depende de las acciones: buscar alimento, evitar depredadores, reproducirse42.  
  *   
  * ¡Estas acciones compiten por un recurso limitado: el **tiempo**\! 43434343  
  *   
* **Diapositiva 3: Un Marco para Entender: Los 3 Niveles de David Marr**

  * Para entender un sistema complejo (cerebro, robot), necesitamos 3 niveles de análisis:  
    * **Computacional:** ¿Qué problema resuelve y por qué? (LA META)  
    * **Algorítmico:** ¿Cómo lo resuelve? (LA RECETA)  
    * **Implementación:** ¿Con qué está hecho? (EL HARDWARE)  
  * *Sugerencia: Usar un diagrama simple que ilustre los tres niveles.*  
* **Diapositiva 4: Nivel 1: Computacional \- La Meta**

  * **Meta:** Maximizar el acceso a Sucesos Biológicamente Importantes (SBI)44444444.  
  *   
  * **Restricción:** El tiempo es finito (T=t1+t2+...)45454545.  
  *   
  * La naturaleza tiene dos soluciones dependiendo del entorno:  
    * **Entorno Estable \-\> Comportamiento Adaptado** (instintos, reflejos)46464646.  
    *   
    * **Entorno Variable \-\> Comportamiento Adaptable** (APRENDIZAJE)47474747.  
    *   
* **Diapositiva 5: Nivel 1 \- Conexión con IA**

  * El problema computacional es idéntico al del **Aprendizaje por Refuerzo (RL)**.  
  * Organismo \= Agente  
  * Distribución de Comportamiento \= Política  
  * SBI \= Recompensa  
  * *Sugerencia: Usar un diagrama simple del ciclo Agente-Entorno de RL.*  
* **Diapositiva 6: Nivel 2: Algorítmico \- La Receta**

  * **Problema central:** Asignación de Crédito. ¿Qué causó el SBI?48.  
  *   
  * **Algoritmo:** Detectar las regularidades (propiedades estadísticas) del entorno49.  
  *   
  * Los organismos buscan 4 tipos de regularidades:  
    * **Cuándo** (Tiempo) y **Dónde** (Lugar)50.  
    *   
    * **Qué predice** (Covarianza con estímulos)51.  
    *   
    * **Qué funciona** (Covarianza con la acción)52.  
    *   
* **Diapositiva 7: Nivel 2 \- Ejemplos de Algoritmos**

  * Ascenso de Colina (Optimización)53535353.  
  *   
  * Aprendizaje Asociativo54.  
  *   
  * Detección de Tasas de ocurrencia de SBI55555555.  
  *   
  * Manejo de Contexto (Control de Estímulos) 56565656 y Estados Ocultos (Extinción)57575757.  
  *   
* **Diapositiva 8: Nivel 2 \- Conexión con IA**

  * **Asignación de Crédito** \-\> Algoritmos de RL (Q-Learning).  
  * **Covarianza con Estímulos** \-\> Aprendizaje Supervisado.  
  * **Estados Ocultos** \-\> Modelos Ocultos de Márkov (HMM).  
  * Los algoritmos que estudiamos en psicología tienen contrapartes matemáticas en la IA.  
* **Diapositiva 9: Nivel 3: Implementación \- El Hardware**

  * **Biología:** El Sistema Nervioso. Neuronas, sinapsis, plasticidad58585858.  
  *   
  * **Robótica (ej. Wall-E):** Sensores, motores, chips de silicio (CPU/GPU)59595959.  
  *   
  * *Imagen de Wall-E junto a una imagen de una red neuronal.*  
* **Diapositiva 10: Nivel 3 \- Conexión con IA**

  * Software vs. Hardware.  
  * El mismo algoritmo de IA (ej. una red neuronal) puede correr en un celular o en un supercomputador.  
  * **Computación Neuromórfica:** Chips que imitan la arquitectura del cerebro.  
* **Diapositiva 11: Conclusión**

  * El estudio del aprendizaje es el estudio de la **adaptabilidad del comportamiento**60606060.  
  *   
  * El marco de Marr nos ayuda a organizar el problema en tres niveles: la meta, la receta y el hardware.  
  * Entender el problema de adaptación nos permite ver los profundos paralelos entre la Psicología, la Evolución y la Inteligencia Artificial.

Espero que esta propuesta sea de gran utilidad para mejorar tus materiales de curso. Es un enfoque que prepara a los estudiantes para una visión moderna e interdisciplinaria de la psicología del aprendizaje.

# **Comportamiento Adaptable: Un Análisis Multinivel de la Psicología del Aprendizaje y la Inteligencia Artificial**

## **Introducción: El Problema Fundamental de la Adaptación**

Todo sistema biológico se enfrenta a un problema fundamental e ineludible: la supervivencia y la reproducción en un mundo de recursos finitos y peligros omnipresentes. La base de este desafío es energética; el simple hecho de existir consume energía, y esta debe ser reabastecida constantemente a través de la acción.1 Este imperativo biológico ha esculpido, a través de la selección natural, dos grandes clases de soluciones conductuales que operan en escalas de tiempo radicalmente diferentes. La comprensión de esta distinción es el punto de partida para cualquier estudio científico del aprendizaje.

La primera solución es el **comportamiento adaptado**. Este se refiere a los rasgos conductuales que son el resultado de un lento proceso de selección natural a lo largo de innumerables generaciones.1 En entornos donde las condiciones relevantes son estables y predecibles —por ejemplo, la física de la gravedad, los ciclos de día y noche, o la presencia constante de un depredador particular—, la evolución puede "codificar" soluciones óptimas directamente en la estructura y el cableado del organismo. Estos comportamientos, que en psicología conocemos como reflejos, instintos o sesgos innatos, son eficientes y fiables, pero fundamentalmente rígidos.1 Son la respuesta de la filogenia a las invariantes del mundo.

Sin embargo, la mayoría de los entornos no son estables. Son variables, volátiles e inciertos.1 La disponibilidad de alimento, la ubicación de las parejas o la estrategia de un depredador pueden cambiar de forma impredecible dentro de la vida de un solo organismo. En tales mundos, un programa conductual fijo sería una sentencia de muerte. Esto da lugar a la segunda gran solución: la capacidad para el

**comportamiento adaptable**. Este concepto, que será el foco central de nuestro análisis y que en gran medida equipararemos con el "aprendizaje", se refiere a la modificación del comportamiento dentro de la vida de un individuo para ajustarse a las propiedades estadísticas cambiantes de su entorno.1 La selección natural, en este caso, no favorece un comportamiento específico, sino los

*mecanismos* que permiten la flexibilidad y el ajuste en tiempo real. La capacidad de aprender es, en sí misma, una adaptación evolutiva a la incertidumbre.

Para diseccionar esta compleja capacidad de aprendizaje, necesitamos un andamiaje teórico que nos permita analizarla desde múltiples perspectivas sin perdernos en los detalles. El marco más poderoso para esta tarea fue propuesto por el neurocientífico y científico cognitivo David Marr.2 Marr argumentó que cualquier sistema de procesamiento de información, ya sea un cerebro o un ordenador, debe ser entendido en tres niveles de análisis distintos pero complementarios 2:

1. **El Nivel Computacional:** Define el *qué* y el *porqué*. ¿Cuál es el objetivo fundamental del sistema? ¿Qué problema está resolviendo y cuál es la lógica de la estrategia para resolverlo?.4  
2. **El Nivel Algorítmico (o de Representación):** Define el *cómo*. ¿Qué representaciones de la información de entrada y salida utiliza el sistema? ¿Qué algoritmo o proceso paso a paso transforma la entrada en la salida?.6  
3. **El Nivel de Implementación:** Define el *sustrato físico*. ¿Cómo se realiza físicamente el algoritmo y la representación? ¿Cuál es el "hardware" —ya sean neuronas y sinapsis o chips de silicio— que ejecuta el proceso?.7

Adoptar el marco de Marr nos permite organizar el vasto campo de la psicología del aprendizaje de una manera coherente. Nos ayuda a ver cómo diferentes teorías, que a primera vista pueden parecer contradictorias, podrían en realidad estar describiendo el mismo fenómeno en distintos niveles de análisis.4 Más importante aún, proporciona un puente conceptual riguroso entre la psicología, la neurociencia y la inteligencia artificial (IA), campos que, como veremos, están convergiendo en una ciencia unificada del comportamiento adaptable.9 Este informe utilizará los niveles de Marr como su principio organizador para explorar el problema del aprendizaje, desde su propósito fundamental hasta su encarnación física.

## **Sección 1: El Nivel Computacional — ¿Qué Problema Resuelve el Aprendizaje?**

En el nivel computacional, nos abstraemos de los mecanismos específicos del cerebro o de los detalles de un algoritmo de IA para centrarnos en la naturaleza del problema que el aprendizaje está diseñado para resolver. La pregunta fundamental es: ¿cuál es la meta del comportamiento adaptable y cuáles son las restricciones bajo las cuales debe operar?

### **1.1 El Objetivo Último: Predecir y Controlar los Sucesos Biológicamente Importantes (SBI)**

El objetivo computacional del aprendizaje puede definirse formalmente como la asignación óptima del comportamiento para maximizar la obtención de consecuencias positivas y minimizar las negativas a lo largo del tiempo, con el fin último de aumentar el éxito reproductivo.1 Estas consecuencias, que en la literatura psicológica se conocen como "refuerzos" o "castigos", se denominan aquí

**Sucesos Biológicamente Importantes (SBI)** para enfatizar su origen y función evolutiva.1 Un SBI es cualquier evento que tiene un impacto, directo o indirecto, en la aptitud de un organismo. Esto incluye no solo necesidades básicas como comida, agua o seguridad, sino también reforzadores secundarios o abstractos como la aceptación social, que puede ser un proxy del acceso futuro a recursos y parejas.1

Este problema de optimización no ocurre en el vacío. Los organismos operan bajo un conjunto estricto de restricciones. La más fundamental es la **restricción lineal del tiempo**: el tiempo es un recurso finito, y cada comportamiento consume una porción de él. La asignación de tiempo a una actividad, como buscar comida, se produce a expensas de otras, como buscar pareja o vigilar a los depredadores.1 Esto se puede expresar con la ecuación

T=t1​+t2​+...+tn​, donde T es el tiempo total disponible y ti​ es el tiempo dedicado a cada uno de los n comportamientos posibles.1 Por lo tanto, el problema computacional es maximizar la ganancia de SBI dentro de este "presupuesto" de tiempo limitado.

La Inteligencia Artificial, y en particular el campo del **Aprendizaje por Refuerzo (RL)**, ha formalizado este mismo problema. En el paradigma del RL, un *agente* (el organismo) interactúa con un *entorno* en una secuencia de pasos de tiempo. En cada paso, el agente observa un *estado* y elige una *acción*. El entorno responde con una *recompensa* (un escalar que cuantifica el SBI) y un nuevo estado.11 El objetivo del agente es aprender una

*política* —una estrategia que mapea estados a acciones— que maximice la recompensa acumulada a largo plazo.13 Para dar cuenta de la preferencia por las recompensas inmediatas sobre las futuras, a menudo se introduce un factor de descuento,

γ, que pondera las recompensas futuras. Así, el objetivo es maximizar el *retorno esperado*, la suma de las recompensas futuras descontadas.11 Esta formulación matemática del RL es una descripción precisa y universal del problema computacional que enfrentan todos los organismos que aprenden.

### **1.2 Un Paradigma Formal: La Teoría del Forrajeo Óptimo y el Teorema del Valor Marginal**

Mucho antes del auge del RL moderno, los ecólogos del comportamiento desarrollaron teorías computacionales notablemente similares para entender cómo los animales buscan comida. La **Teoría del Forrajeo Óptimo (OFT, por sus siglas en inglés)** es un ejemplo perfecto de un análisis a nivel computacional.14 Postula que la selección natural ha favorecido patrones de forrajeo que maximizan la ganancia neta de energía (la "moneda") por unidad de tiempo, dadas las "restricciones" del entorno.14

Un modelo clásico dentro de la OFT es el **Teorema del Valor Marginal (MVT)**, propuesto por Eric Charnov en 1976\.16 El MVT aborda un problema específico: un animal se alimenta en un entorno donde la comida se encuentra en "parcelas" discretas (por ejemplo, un arbusto con bayas, una flor con néctar). A medida que el animal consume el recurso en una parcela, la tasa de ganancia de energía disminuye (rendimientos decrecientes). El animal debe decidir cuándo abandonar la parcela actual y gastar tiempo y energía viajando a una nueva. El MVT proporciona una solución óptima y elegante: el animal debe abandonar la parcela cuando su tasa instantánea de ingesta de energía cae por debajo de la tasa de ingesta promedio de todo el hábitat.16

Este modelo hace predicciones claras y comprobables. Por ejemplo, los animales deberían permanecer más tiempo en las parcelas si el tiempo de viaje entre ellas es mayor.16 Estas predicciones han sido confirmadas cualitativamente en numerosos estudios, desde pájaros carboneros grandes (great tits) hasta humanos recogiendo manzanas.16 El MVT es un ejemplo paradigmático de una teoría computacional porque especifica el objetivo (maximizar la tasa de energía a largo plazo) y la estrategia óptima para lograrlo, sin hacer referencia a los mecanismos neuronales o los procesos cognitivos subyacentes.

Curiosamente, las desviaciones del comportamiento real con respecto a las predicciones del MVT también son informativas. A menudo, los animales permanecen en una parcela más tiempo de lo que predice el modelo.19 Esto no significa que los animales sean "subóptimos", sino que el modelo computacional original podría ser incompleto. Quizás los animales no solo están maximizando la energía, sino también la obtención de

*información* sobre la calidad del entorno, un bien que tiene valor para decisiones futuras.19 Esto demuestra la potencia del análisis computacional: nos permite formular hipótesis precisas sobre los objetivos del comportamiento y refinar nuestra comprensión de esos objetivos a través de la experimentación.

### **1.3 El Desafío Universal: El Problema de la Asignación de Crédito**

Resolver el problema computacional de la optimización de SBI se enfrenta a una dificultad fundamental: el **problema de la asignación de crédito**.1 Este problema se refiere a la dificultad de determinar qué acciones o qué estímulos ambientales son responsables de un resultado particular, especialmente cuando hay un retraso temporal entre la causa y el efecto.21

Imaginemos a un jugador de ajedrez que gana una partida. Recibe una gran recompensa (+1) al final, pero ¿cuál de sus 40 movimientos fue el decisivo? ¿Fue el brillante sacrificio de un peón en la jugada 15, o fue un error sutil de su oponente en la jugada 32?.23 De manera similar, un animal puede realizar una larga secuencia de comportamientos —salir de la madriguera, evitar a un depredador, seguir un rastro de olor, cavar— para finalmente encontrar comida. ¿Cómo atribuye el "crédito" de la recompensa a la secuencia correcta de acciones?

Este problema es central tanto para la neurociencia como para la IA. A nivel neuronal, se pregunta cómo una sinapsis individual "sabe" que su fortalecimiento contribuyó a un comportamiento exitoso que ocurrió segundos o minutos después.21 En IA, es el desafío de actualizar millones de parámetros en una red neuronal basándose en un resultado final.23

Como se describe en los materiales de origen, el problema de la asignación de crédito se puede dividir en dos subtipos principales 1:

1. **Asignación de Crédito Estímulo-Resultado:** ¿Qué señal del entorno predijo de manera fiable el SBI? Si un sonido de campana precede consistentemente a la comida, el organismo debe asignar el crédito predictivo a la campana. Este es el dominio del condicionamiento clásico o pavloviano.  
2. **Asignación de Crédito Acción-Resultado:** ¿Cuál de mis propias acciones causó el SBI? Si presionar una palanca produce una bolita de comida, el organismo debe asignar el crédito causal a la acción de presionar. Este es el dominio del condicionamiento instrumental u operante.

La complejidad de los algoritmos que exploraremos en la siguiente sección es una consecuencia directa de la necesidad de resolver este problema fundamental de la asignación de crédito.

### **1.4 La Estructura del Problema: Propiedades Estadísticas del Entorno**

Para que un sistema de aprendizaje pueda resolver el problema de la asignación de crédito, debe ser capaz de detectar las regularidades estadísticas del entorno. Estas regularidades son, en esencia, los "datos" de entrada para el algoritmo de aprendizaje. Un organismo que puede detectar estas propiedades y ajustar su comportamiento en consecuencia asignará su presupuesto de tiempo de manera más óptima.1 Basándonos en los materiales de base, podemos categorizar estas propiedades en varios niveles de complejidad 1:

* **Regularidades de Primer Orden:** Son las covarianzas más básicas que un organismo debe aprender.  
  * **Temporal:** ¿*Cuándo* ocurren los SBI? La regularidad temporal es la base del condicionamiento.  
  * **Espacial:** ¿*Dónde* ocurren los SBI? Esto es fundamental para la navegación y la creación de mapas del entorno.  
  * **Covarianza con Estímulos:** ¿*Qué* predice los SBI? Un organismo debe aprender que las nubes oscuras covarían con la lluvia, o que un cierto olor covaría con la presencia de un depredador.  
  * **Covarianza con Acciones:** ¿*Qué acciones* producen SBI? Este es el núcleo del aprendizaje instrumental; descubrir la estructura causal entre el comportamiento y sus consecuencias.  
* **Regularidades de Orden Superior:** Estas son propiedades más complejas del entorno que requieren mecanismos de aprendizaje más sofisticados.  
  * **Control de Estímulos (Dependencia del Contexto):** Las regularidades de primer orden a menudo no son universales; dependen del contexto. Una señal puede predecir comida en el laboratorio, pero no en la naturaleza. Un comportamiento puede ser recompensado en presencia de los padres, pero castigado en presencia de los compañeros. La capacidad de modular el comportamiento en función de estas señales contextuales se conoce como control por el estímulo.1 Los experimentos clásicos con palomas, que aprenden a picotear una tecla en presencia de una luz verde pero no de una roja, son un ejemplo canónico de este proceso.24  
  * **Tasa de Ocurrencia:** Los organismos no solo son sensibles a eventos individuales, sino también a la *tasa* de ocurrencia de esos eventos (número de eventos por unidad de tiempo).1 Como vimos en el MVT, la tasa de recompensa es una variable crucial. La sensibilidad a la tasa es fundamental para las teorías modernas del aprendizaje y la toma de decisiones.  
  * **Niveles de Incertidumbre:** Existe una distinción crucial entre la *incertidumbre esperada* (riesgo) y la *incertidumbre inesperada* (volatilidad o cambio de régimen).1 El riesgo es la incertidumbre dentro de un modelo estable del mundo (por ejemplo, la probabilidad de 0.5 de cara al lanzar una moneda justa). La volatilidad es cuando los propios parámetros del modelo cambian con el tiempo (por ejemplo, si la moneda se vuelve sesgada). Un sistema de aprendizaje avanzado debe ser capaz de distinguir entre una racha de mala suerte (riesgo) y un cambio fundamental en las reglas del juego (volatilidad), y ajustar su tasa de aprendizaje en consecuencia.

En resumen, el nivel computacional nos dice que el aprendizaje es un proceso de optimización bajo restricciones, cuyo objetivo es predecir y controlar los SBI. Este proceso se enfrenta al desafío universal de la asignación de crédito y opera sobre los datos proporcionados por las complejas regularidades estadísticas del entorno. Con esta definición del problema en mente, ahora podemos pasar al nivel algorítmico para explorar *cómo* los sistemas biológicos y artificiales intentan resolverlo.

## **Sección 2: El Nivel Algorítmico — ¿Cómo se Resuelve el Problema del Aprendizaje?**

Si el nivel computacional define el *qué* y el *porqué* del aprendizaje, el nivel algorítmico se ocupa del *cómo*. Explora los procesos y las representaciones que los organismos y las máquinas utilizan para alcanzar los objetivos computacionales. Históricamente, en psicología, el debate sobre el "cómo" del aprendizaje se ha centrado en una tensión fundamental entre dos grandes familias de teorías: las asociativas y las cognitivas.26 En lugar de verlas como mutuamente excluyentes, las presentaremos como dos clases de algoritmos fundamentalmente diferentes, cada una con sus propias fortalezas, debilidades y análogos directos en la inteligencia artificial.

### **2.1 Algoritmos Asociativos: Aprender como Mapeo Directo de Políticas y Valores (RL sin Modelo)**

El enfoque asociativo, con raíces en el conductismo de Thorndike y Skinner, postula que el aprendizaje consiste en la formación de vínculos o asociaciones directas.28 Estas pueden ser entre un estímulo y una respuesta (S-R) o entre un estímulo y un valor o resultado (S-O). La característica clave de estos algoritmos es que aprenden una

*política* reactiva o un *valor* para cada situación, sin construir una representación interna explícita de la estructura causal del mundo.27 En la terminología de la IA, esto se conoce como

**Aprendizaje por Refuerzo sin Modelo (Model-Free RL)**. Es computacionalmente eficiente y rápido en la ejecución, pero a menudo resulta en un comportamiento inflexible y "habitual".29

#### **2.1.1 Un Algoritmo Fundacional: El Modelo de Rescorla-Wagner**

El modelo de Rescorla-Wagner (R-W), propuesto en 1972, fue un gran avance sobre las teorías asociativas simples porque formalizó una idea crucial: el aprendizaje es impulsado por la **sorpresa** o el **error de predicción**.30 No es la mera contigüidad de un estímulo condicionado (EC) y un estímulo incondicionado (EI) lo que produce el aprendizaje, sino la medida en que el EI es inesperado.30

El modelo se captura en una simple pero poderosa ecuación que describe el cambio en la fuerza asociativa (V) de un estímulo X en un ensayo dado:

ΔVX​=αX​β(λ−ΣV)  
Donde:

* ΔVX​ es el cambio en la fuerza asociativa del estímulo X.  
* αX​ es la saliencia (notabilidad) del EC (X).  
* β es la saliencia o tasa de aprendizaje asociada con el EI.  
* λ es la máxima fuerza asociativa que el EI puede soportar (lo que es posible aprender).  
* ΣV es la fuerza asociativa total de *todos* los estímulos presentes en el ensayo (lo que ya se espera).32

El término clave es (λ−ΣV), el **error de predicción**. Si lo que ocurre (λ) es mayor que lo que se esperaba (ΣV), el error es positivo y la fuerza asociativa aumenta (aprendizaje excitatorio). Si lo que ocurre es menor que lo esperado, el error es negativo y la fuerza asociativa disminuye (aprendizaje inhibitorio). Si lo que ocurre es exactamente lo que se esperaba, el error es cero y no hay aprendizaje.30

Este elegante modelo puede explicar una amplia gama de fenómenos del condicionamiento clásico que eran problemáticos para teorías más simples:

* **Adquisición:** En los primeros ensayos, ΣV es cercano a cero, por lo que el error de predicción es grande y el aprendizaje es rápido. A medida que V aumenta, el error disminuye y el aprendizaje se ralentiza, produciendo la clásica curva de aprendizaje asintótica.  
* **Bloqueo:** Si un estímulo A ya ha sido condicionado hasta el punto en que VA​ es cercano a λ, y luego se presenta un compuesto AX seguido del EI, la expectativa total ΣV=VA​+VX​≈λ+0=λ. El término de error (λ−ΣV) es cercano a cero. Como resultado, ΔVX​ es casi nulo, y no se aprende nada sobre el estímulo X.30 El aprendizaje previo sobre A "bloquea" el aprendizaje sobre X.

#### **2.1.2 Un Algoritmo Más Potente: Aprendizaje por Diferencia Temporal (TD)**

El modelo R-W es poderoso, pero está limitado principalmente a explicar cómo se aprende sobre eventos que ocurren en un solo paso. No aborda directamente el problema de la asignación de crédito temporal, es decir, cómo aprender en tareas secuenciales donde las recompensas son demoradas. La solución a este problema es el **aprendizaje por diferencia temporal (TD)**, el algoritmo central de la mayoría de los sistemas de RL sin modelo modernos.11

El aprendizaje TD es una generalización brillante de la idea de corrección de errores de R-W. En lugar de comparar la predicción con el resultado final real, el aprendizaje TD compara una predicción en un momento dado con una predicción ligeramente posterior y más precisa.33 La idea central es que la predicción en el siguiente estado, al estar más cerca de la recompensa final, es una mejor fuente de información para actualizar la predicción actual.

El **error de predicción de TD** se calcula como:

δt​=rt+1​+γV(st+1​)−V(st​)  
Donde:

* δt​ es el error TD en el tiempo t.  
* rt+1​ es la recompensa inmediata recibida después de la transición.  
* V(st​) es el valor estimado (recompensa futura total esperada) del estado actual.  
* V(st+1​) es el valor estimado del siguiente estado.  
* γ es el factor de descuento.

El término (rt+1​+γV(st+1​)) representa una estimación más precisa del valor de estar en st​. El algoritmo utiliza la diferencia entre esta nueva estimación y la antigua (V(st​)) para actualizar V(st​), acercándola a la "verdad". Al propagar este error hacia atrás en el tiempo, un agente TD puede aprender una **función de valor** que asigna a cada estado una predicción precisa de la recompensa acumulada a largo plazo que puede esperar de ese estado en adelante, resolviendo así el problema de la asignación de crédito temporal.33

### **2.2 Algoritmos Cognitivos: Aprender como la Construcción de Modelos del Mundo (RL Basado en Modelo)**

En contraste con el enfoque asociativo, el enfoque cognitivo postula que el aprendizaje implica la construcción de una representación interna rica y estructurada del entorno, a menudo llamada **mapa cognitivo** o **modelo del mundo**.26 Este modelo no solo codifica qué hacer, sino que representa las relaciones causales y espaciales del entorno: "si estoy en el lugar A y voy al norte, llegaré al lugar B". En la terminología de la IA, esto se conoce como

**Aprendizaje por Refuerzo Basado en Modelo (Model-Based RL)**. Este enfoque es computacionalmente más exigente, ya que requiere aprender y almacenar un modelo, pero permite un comportamiento mucho más flexible y "dirigido a metas".20

#### **2.2.1 La Evidencia Clásica: Los Mapas Cognitivos de Tolman**

La evidencia más influyente a favor de los algoritmos cognitivos proviene de los experimentos pioneros de Edward C. Tolman en las décadas de 1930 y 1940\. Tolman desafió directamente la visión conductista de que el aprendizaje era simplemente el fortalecimiento de cadenas de respuestas S-R.34

En su experimento más famoso de **aprendizaje latente**, Tolman y Honzik (1930) utilizaron tres grupos de ratas en un laberinto complejo 36:

1. **Grupo 1 (Recompensa Continua):** Recibía comida al final del laberinto en cada ensayo. Como era de esperar, su número de errores disminuyó gradualmente.  
2. **Grupo 2 (Sin Recompensa):** Nunca recibió comida. Su rendimiento no mejoró significativamente.  
3. **Grupo 3 (Recompensa Retrasada):** No recibió recompensa durante los primeros 10 días, pero a partir del día 11, encontró comida al final del laberinto.

El resultado crucial provino del Grupo 3\. Durante los primeros 10 días, su comportamiento era indistinguible del Grupo 2\. Sin embargo, tan pronto como se introdujo la recompensa en el día 11, su rendimiento mejoró drásticamente, y en el día 12 ya era tan bueno como el del Grupo 1, que había sido recompensado desde el principio.37

Tolman argumentó que la única forma de explicar este cambio repentino era que las ratas del Grupo 3 habían estado aprendiendo la estructura del laberinto durante los primeros 10 días, construyendo un "mapa cognitivo" sin ninguna recompensa. Este aprendizaje permaneció **latente** (oculto) hasta que se proporcionó una motivación (la comida) para demostrarlo.36 En otros experimentos, demostró que las ratas que habían aprendido una ruta podían tomar atajos novedosos si la ruta original estaba bloqueada, un comportamiento que es casi imposible de explicar con cadenas S-R rígidas, pero que es trivial si la rata puede "consultar" su mapa mental para planificar una nueva ruta.39

#### **2.2.2 La Implementación en IA: Aprendizaje por Refuerzo Basado en Modelo**

El aprendizaje por refuerzo basado en modelo es la formalización computacional de la idea de Tolman.20 En este enfoque, el agente de IA utiliza su experiencia no para aprender directamente una política o valores (como en el RL sin modelo), sino para aprender un

**modelo del mundo**. Este modelo consta de dos partes:

1. Un **modelo de transición**, P(s′∣s,a): predice la probabilidad de pasar al estado s′ si se realiza la acción a en el estado s.  
2. Un **modelo de recompensa**, R(s,a): predice la recompensa que se recibirá al realizar la acción a en el estado s.

Una vez que el agente ha aprendido este modelo, puede utilizarlo para la **planificación**. Puede "simular" mentalmente secuencias de acciones y sus consecuencias sin tener que ejecutarlas físicamente en el mundo real. Por ejemplo, puede utilizar un algoritmo de búsqueda, como la búsqueda en árbol, para explorar diferentes trayectorias en su modelo interno y encontrar la que conduce a la mayor recompensa acumulada. Esta capacidad de planificación es lo que dota al agente de una enorme flexibilidad. Si el entorno cambia (por ejemplo, una recompensa se mueve a una nueva ubicación), el agente solo necesita actualizar su modelo y luego puede planificar inmediatamente un nuevo curso de acción óptimo, al igual que las ratas de Tolman encontraban un atajo.

La siguiente tabla resume y contrasta estos dos enfoques algorítmicos, que representan no solo un debate histórico en psicología, sino también una distinción fundamental en la inteligencia artificial moderna.

| Característica | Enfoque Asociativo / Sin Modelo (Model-Free) | Enfoque Cognitivo / Basado en Modelo (Model-Based) |
| :---- | :---- | :---- |
| **Conocimiento Aprendido** | Valores de acciones (Q-values), política directa (S-R). "Qué tan bueno es hacer X aquí". | Un modelo del mundo (mapa). "Si hago X aquí, iré a Y". |
| **Proceso Principal** | Ensayo y error, corrección de error de predicción. | Planificación, deliberación, simulación. |
| **Flexibilidad Conductual** | Baja. Lento para adaptarse a cambios (e.g., si una recompensa se mueve). Es "habitual". | Alta. Rápido para adaptarse a cambios. Es "dirigido a metas". |
| **Costo Computacional** | Bajo. Simplemente recupera un valor almacenado. | Alto. La planificación puede ser muy lenta y exigir muchos recursos. |
| **Teoría Psicológica Clave** | Conductismo (Thorndike, Skinner), Teoría Asociativa (Rescorla). | Psicología Cognitiva (Tolman). |
| **Algoritmo Central en IA** | Q-Learning, SARSA, Aprendizaje por Diferencia Temporal (TD). | Búsqueda en árboles (Tree Search), Programación Dinámica, Planificación. |
| **Ejemplo Clásico** | Una paloma picoteando una tecla por hábito para obtener comida. | Una rata tomando un atajo en un laberinto cuando su ruta habitual está bloqueada. |
| **Sustrato Neural Primario** | Ganglios basales (especialmente estriado dorsolateral), sistema de dopamina. | Hipocampo, corteza prefrontal/orbitofrontal. |

El reconocimiento de que estos dos tipos de algoritmos coexisten ha llevado a una comprensión mucho más matizada del aprendizaje. En lugar de un debate sobre qué teoría es "correcta", la investigación moderna se centra en cómo los organismos combinan estos sistemas.27 Para tareas rutinarias y bien aprendidas, el sistema sin modelo, rápido y eficiente, es ideal. Para problemas nuevos o cuando el entorno cambia inesperadamente, se necesita el sistema basado en modelo, más lento pero flexible. El cerebro parece ser un sistema híbrido que aprovecha lo mejor de ambos mundos.

## **Sección 3: El Nivel de Implementación — ¿Cómo se Realiza Físicamente el Aprendizaje?**

El nivel final del análisis de Marr nos lleva del "qué" y el "cómo" al sustrato físico: ¿cómo se implementan estos algoritmos en el "hardware" biológico del cerebro o en el silicio de los ordenadores?.5 Esta investigación revela una convergencia asombrosa, donde los conceptos abstractos de los algoritmos de aprendizaje encuentran correlatos directos en la actividad de circuitos neuronales específicos.

### **3.1 La Implementación Neural del Aprendizaje Asociativo / Sin Modelo**

Uno de los descubrimientos más espectaculares de la neurociencia computacional es la implementación física del algoritmo de aprendizaje por diferencia temporal (TD). Durante décadas, los neurocientíficos supieron que las neuronas del mesencéfalo que producen el neurotransmisor **dopamina** estaban implicadas en la recompensa y la motivación. Sin embargo, el trabajo de Wolfram Schultz y sus colegas en la década de 1990 reveló que estas neuronas no responden a la recompensa en sí misma, sino al **error de predicción de la recompensa**.13

Los experimentos de registro de la actividad de neuronas dopaminérgicas individuales en monos mientras realizaban tareas de condicionamiento mostraron un patrón que se ajustaba perfectamente a la señal del error TD (δ):

* **Recompensa Inesperada:** Cuando el mono recibía una recompensa que no esperaba (por ejemplo, una gota de zumo), las neuronas dopaminérgicas mostraban un breve y fuerte estallido de actividad por encima de su línea de base. Esto corresponde a un δ\>0.13  
* **Recompensa Esperada:** Una vez que el mono aprendía que una señal (por ejemplo, una luz) predecía la recompensa, las neuronas dopaminérgicas dejaban de responder a la recompensa en sí. En cambio, su estallido de actividad se desplazaba a la aparición de la señal predictiva. En el momento de la recompensa, la actividad no cambiaba, ya que la recompensa era totalmente esperada. Esto corresponde a un δ=0.13  
* **Omisión de una Recompensa Esperada:** Si la señal predictiva aparecía pero la recompensa esperada no se entregaba, las neuronas dopaminérgicas mostraban una pausa en su actividad, cayendo por debajo de su línea de base en el momento en que la recompensa debería haber llegado. Esto corresponde a un δ\<0.13

Esta señal de error de predicción de recompensa codificada por la dopamina se transmite a regiones cerebrales clave como los **ganglios basales**, y en particular el **estriado**.29 Se cree que esta señal de dopamina actúa como un "profesor" global, modulando la plasticidad sináptica en el estriado. Específicamente, fortalece las conexiones sinápticas que estaban activas justo antes de un resultado mejor de lo esperado (un estallido de dopamina) y debilita las que precedieron a un resultado peor de lo esperado (una pausa de dopamina). Este mecanismo es la implementación física de la actualización de la función de valor en un algoritmo de RL sin modelo, como Q-learning o SARSA. El estriado dorsolateral, en particular, está implicado en el aprendizaje de hábitos S-R, la manifestación conductual del control sin modelo.27

### **3.2 La Implementación Neural del Aprendizaje Cognitivo / Basado en Modelo**

Si el sistema dopamina/ganglios basales implementa el aprendizaje sin modelo, ¿dónde reside el modelo del mundo? La evidencia apunta a un circuito cerebral diferente, centrado en el **hipocampo** y la **corteza prefrontal (CPF)**.

* **El Hipocampo como Mapa Cognitivo:** El hipocampo ha estado asociado durante mucho tiempo con la memoria espacial y episódica.26 El descubrimiento de las "células de lugar" (place cells) en el hipocampo de las ratas por John O'Keefe proporcionó un correlato neural directo para la idea de un mapa cognitivo.40 Estas neuronas se activan selectivamente cuando el animal se encuentra en una ubicación específica de su entorno. Colectivamente, la actividad de estas células forma un mapa neural del espacio. Esta estructura es el candidato ideal para el sustrato físico del mapa cognitivo de Tolman, proporcionando la representación espacial necesaria para la navegación flexible y la planificación de rutas.20  
* **La Corteza Prefrontal como Planificador:** Tener un mapa no es suficiente; se necesita un sistema que pueda "leer" el mapa y utilizarlo para planificar acciones dirigidas a un objetivo. Este papel recae en la corteza prefrontal, especialmente en la **corteza orbitofrontal (COF)**.20 La CPF es crucial para las funciones ejecutivas, la toma de decisiones y el comportamiento dirigido a metas. Se cree que la CPF integra la información sobre los objetivos actuales del organismo con el modelo del mundo proporcionado por el hipocampo y otras áreas corticales. Al hacerlo, puede simular los resultados potenciales de diferentes planes de acción y seleccionar el más adecuado para la situación actual, una función central del control basado en modelo.20

La existencia de estos dos sistemas neuronales distintos y disociables —uno para el aprendizaje habitual y otro para la planificación flexible— proporciona una poderosa evidencia de implementación para la distinción algorítmica entre los sistemas de RL sin modelo y basado en modelo.

### **3.3 Implementación en Sistemas Artificiales**

En los sistemas artificiales, los algoritmos de aprendizaje se implementan en hardware de silicio. El análogo de una neurona es un "nodo" o "unidad" en una **Red Neuronal Artificial (RNA)**, y las "fuerzas sinápticas" son los "pesos" numéricos de las conexiones entre estos nodos.23

El aprendizaje en las RNA consiste en ajustar estos pesos para que la red produzca la salida deseada para una entrada dada. En el aprendizaje supervisado, esto se logra a menudo mediante el algoritmo de retropropagación del error (backpropagation). En el aprendizaje por refuerzo, los algoritmos como el aprendizaje TD se utilizan para ajustar los pesos con el fin de maximizar la recompensa futura.21

Un ejemplo emblemático es la **Red Q Profunda (DQN, por sus siglas en inglés)**, desarrollada por DeepMind. Este sistema combinó el aprendizaje TD con una red neuronal profunda para aprender a jugar a videojuegos de Atari a un nivel sobrehumano.42 La red neuronal actuaba como un aproximador de funciones, tomando los píxeles de la pantalla del juego como entrada y produciendo los valores Q (el valor esperado de tomar cada acción posible) como salida. La red se entrenaba utilizando el error de predicción TD para ajustar sus pesos, aprendiendo así directamente una política de juego exitosa a partir de la experiencia de ensayo y error, un claro ejemplo de un sistema de RL sin modelo implementado en silicio. Los sistemas basados en modelo, por su parte, utilizan redes neuronales para aprender los modelos de transición y recompensa del entorno, que luego se utilizan para la planificación.

La convergencia es notable: tanto el cerebro como las máquinas más avanzadas parecen haber llegado a soluciones algorítmicas similares para el problema del comportamiento adaptable, aunque sus implementaciones físicas sean radicalmente diferentes.

## **Conclusión: Hacia una Ciencia Integrada del Comportamiento Adaptable**

El viaje a través de los tres niveles de análisis de Marr nos ha proporcionado una perspectiva unificada y poderosa sobre el comportamiento adaptable. Hemos pasado de una pregunta fundamentalmente biológica a los algoritmos abstractos que la resuelven y, finalmente, a su encarnación física en cerebros y máquinas. Este enfoque multinivel no solo organiza el conocimiento existente, sino que también disuelve dicotomías históricas y revela principios profundos y compartidos.

Comenzamos con el **nivel computacional**, definiendo el aprendizaje como la solución al problema de optimizar la obtención de Sucesos Biológicamente Importantes en un mundo incierto y con recursos limitados. Este marco, ejemplificado por la Teoría del Forrajeo Óptimo, nos permite comprender el *propósito* del aprendizaje y el desafío central que debe superar: el problema de la asignación de crédito.

Luego, en el **nivel algorítmico**, vimos cómo el histórico debate entre las teorías asociativas y cognitivas puede reformularse como la existencia de dos clases de soluciones complementarias. El enfoque asociativo, formalizado como RL sin modelo, aprende políticas habituales y eficientes a través de la corrección de errores de predicción. El enfoque cognitivo, formalizado como RL basado en modelo, aprende mapas o modelos del mundo que permiten una planificación flexible y dirigida a metas. La conclusión clave no es que uno sea superior al otro, sino que el cerebro es un sistema híbrido que despliega el algoritmo más adecuado para la tarea en cuestión: el hábito para lo familiar, la deliberación para lo novedoso.27

Finalmente, en el **nivel de implementación**, encontramos una confirmación física de esta dualidad algorítmica. El sistema de dopamina del mesencéfalo y los ganglios basales implementan una señal de error de predicción TD, el núcleo del aprendizaje sin modelo. Por otro lado, el circuito hipocampo-corteza prefrontal proporciona el sustrato para los mapas cognitivos y la planificación, el núcleo del aprendizaje basado en modelo. La convergencia de la evidencia conductual, algorítmica y neuroanatómica refuerza la validez de este marco integrado.

La psicología del aprendizaje, por lo tanto, se encuentra en el centro de una empresa científica apasionante y convergente. Proporciona los fenómenos conductuales fundamentales, las preguntas iniciales y las intuiciones teóricas que han guiado la investigación durante un siglo. La inteligencia artificial ofrece el lenguaje matemático y las herramientas computacionales para formalizar estas intuiciones, crear modelos precisos y generar nuevas hipótesis comprobables.10 La neurociencia, a su vez, proporciona el anclaje biológico, revelando cómo estos algoritmos cobran vida en el único sistema que, hasta la fecha, ha dominado verdaderamente el arte del comportamiento adaptable: el cerebro. El estudio de cómo los agentes, biológicos o artificiales, aprenden a prosperar en la incertidumbre es un gran desafío compartido, y el progreso futuro dependerá de la continua y fructífera colaboración entre estos campos.

Claro, aquí tienes una presentación en formato de diapositivas basada en la investigación.

---

### **Presentación: Comportamiento Adaptable**

**Diapositiva 1: Título**

Comportamiento Adaptable: Un Análisis Multinivel

Una perspectiva desde la Psicología del Aprendizaje, la Neurociencia y la Inteligencia Artificial

---

**Diapositiva 2: El Problema Fundamental**

**El Problema Biológico: Supervivencia y Energía**

* Todo organismo enfrenta un desafío central: reabastecer la energía que consume para existir. 1  
* La solución a este problema se manifiesta a través de la **acción**.  
* La selección natural moldea las acciones que maximizan el éxito reproductivo:  
  * Obtener alimento.  
  * Evitar depredadores.  
  * Encontrar pareja. 1

---

**Diapositiva 3: Dos Soluciones Evolutivas**

**Adaptado vs. Adaptable**

* **Comportamiento Adaptado:**  
  * Solución para entornos **estables y predecibles**.  
  * Resultado de la selección natural a lo largo de generaciones.  
  * Comportamientos "codificados": reflejos, instintos.  
  * Son eficientes, pero **rígidos**. 1  
* **Comportamiento Adaptable (Aprendizaje):**  
  * Solución para entornos **variables, volátiles e inciertos**.  
  * Modificación del comportamiento **dentro de la vida** de un individuo.  
  * La selección natural favorece los *mecanismos* de flexibilidad.  
  * Es una adaptación a la **incertidumbre**. 1

---

**Diapositiva 4: Un Marco para Entender la Complejidad**

Los Niveles de Análisis de David Marr

Para entender un sistema de procesamiento de información (cerebro o IA), debemos analizarlo en tres niveles complementarios: 2

1. **Nivel Computacional:** ¿*Qué* problema resuelve el sistema y *por qué*? (El objetivo). 5  
2. **Nivel Algorítmico:** ¿*Cómo* lo resuelve? (La representación y el proceso). 6  
3. **Nivel de Implementación:** ¿En *qué sustrato físico* se realiza? (El hardware: neuronas o silicio). 6

*Este marco nos permite conectar la Psicología, la IA y la Neurociencia.* 2

---

**Diapositiva 5: Nivel 1: Computacional**

**¿Qué Problema Resuelve el Aprendizaje?**

---

**Diapositiva 6: El Objetivo Computacional**

**Predecir y Controlar Sucesos Biológicamente Importantes (SBI)**

* **Objetivo:** Maximizar la obtención de consecuencias positivas (recompensas) y minimizar las negativas (castigos) a lo largo del tiempo. 1  
* **SBI:** Cualquier evento que impacta la aptitud (comida, seguridad, aceptación social). 1  
* **Restricción Fundamental:** El tiempo es finito. Asignar tiempo a una acción (ej. buscar comida) se lo quita a otras (ej. buscar pareja). 1  
  * T=t1​+t2​+...+tn​

---

**Diapositiva 7: La Formalización en IA: Aprendizaje por Refuerzo (RL)**

**El Agente y su Entorno**

* Un **agente** (organismo) interactúa con un **entorno**.  
* Observa un **estado**, elige una **acción**.  
* Recibe una **recompensa** (el SBI) y un nuevo estado.  
* **Meta:** Aprender una **política** (estrategia) que maximice la recompensa acumulada a largo plazo. 8

*El RL es una descripción matemática universal del problema del aprendizaje.*

---

**Diapositiva 8: Un Paradigma Clásico: Teoría del Forrajeo Óptimo (OFT)**

**Maximizando la Ganancia de Energía**

* La OFT postula que la selección natural favorece patrones de búsqueda de alimento que maximizan la ganancia neta de energía por unidad de tiempo. 11  
* **Modelo Clásico: Teorema del Valor Marginal (MVT)** 13  
  * **Problema:** ¿Cuándo debe un animal abandonar una "parcela" de comida que se está agotando para buscar una nueva?  
  * **Solución Óptima:** Debe irse cuando la tasa de ganancia de energía en la parcela actual cae por debajo de la tasa promedio del hábitat. 15

---

**Diapositiva 9: El Desafío Universal**

**El Problema de la Asignación de Crédito**

* ¿Cómo determinar qué acciones o estímulos son responsables de un resultado, especialmente cuando hay un retraso temporal? 16  
* **Ejemplo en Ajedrez:** Ganas una partida. ¿Cuál de los 40 movimientos fue el decisivo? 18  
* **Tipos de Asignación:**  
  1. **Estímulo-Resultado:** ¿Qué señal predijo el SBI? (Condicionamiento Clásico).  
  2. **Acción-Resultado:** ¿Qué acción causó el SBI? (Condicionamiento Instrumental). 1

---

**Diapositiva 10: Nivel 2: Algorítmico**

**¿Cómo se Resuelve el Problema del Aprendizaje?**

---

**Diapositiva 11: Dos Familias de Algoritmos**

**Asociativo vs. Cognitivo**

* **Enfoque Asociativo (Conductismo):**  
  * El aprendizaje es la formación de vínculos directos (Estímulo-Respuesta).  
  * Aprende una política reactiva y "habitual".  
  * **En IA: Aprendizaje por Refuerzo sin Modelo (Model-Free RL).** 19  
* **Enfoque Cognitivo (Tolman):**  
  * El aprendizaje es la construcción de un "mapa cognitivo" o modelo del mundo.  
  * Permite un comportamiento flexible y "dirigido a metas".  
  * **En IA: Aprendizaje por Refuerzo Basado en Modelo (Model-Based RL).** 19

---

**Diapositiva 12: Algoritmo Asociativo Clave: Rescorla-Wagner**

**El Aprendizaje es Impulsado por la Sorpresa**

* El aprendizaje no depende de la simple contigüidad, sino del **error de predicción**. 21  
* **Ecuación:** ΔVX​=αβ(λ−ΣV)  
  * (λ−ΣV) es el **error de predicción**: la diferencia entre lo que ocurre (λ) y lo que se esperaba (ΣV).  
* Si el resultado es inesperado, el error es grande y se aprende.  
* Si el resultado es esperado, el error es cero y no hay aprendizaje. 21  
* **Explica fenómenos como el "bloqueo".** 23

---

**Diapositiva 13: Algoritmo Asociativo Moderno: Aprendizaje por Diferencia Temporal (TD)**

**Resolviendo el Retraso Temporal**

* El algoritmo central del RL moderno. Generaliza la idea de Rescorla-Wagner para secuencias de acciones. 10  
* En lugar de comparar la predicción con el resultado final, la compara con una predicción posterior (y más precisa).  
* **Error de Predicción TD:** δt​=rt+1​+γV(st+1​)−V(st​)  
* Este error se propaga hacia atrás en el tiempo, permitiendo asignar crédito a acciones lejanas a la recompensa. 24

---

**Diapositiva 14: Evidencia Clásica del Enfoque Cognitivo**

**Los Mapas Cognitivos de Tolman**

* Tolman desafió la idea de que el aprendizaje era solo formar cadenas Estímulo-Respuesta. 25  
* **Experimento de Aprendizaje Latente (1930):** 27  
  * **Grupo 1 (Recompensa):** Mejoró gradualmente.  
  * **Grupo 2 (Sin recompensa):** No mejoró.  
  * **Grupo 3 (Recompensa tardía):** No mejoró durante 10 días. Al recibir recompensa el día 11, su rendimiento se disparó, igualando al Grupo 1\. 29  
* **Conclusión:** Las ratas del Grupo 3 construyeron un "mapa cognitivo" del laberinto sin recompensa. El aprendizaje estaba **latente** hasta que hubo una motivación para usarlo. 25

---

**Diapositiva 15: Resumen de Algoritmos: Sin Modelo vs. Basado en Modelo**

| Característica | Sin Modelo (Asociativo) | Basado en Modelo (Cognitivo) |
| :---- | :---- | :---- |
| **Qué aprende** | Valores, hábitos (S-R) | Un mapa/modelo del mundo |
| **Proceso** | Ensayo y error | Planificación, simulación |
| **Flexibilidad** | Baja (lento a cambios) | Alta (rápido a cambios) |
| **Costo Computacional** | Bajo (rápido) | Alto (lento) |
| **Teoría Psicológica** | Conductismo, Rescorla | Cognitivismo, Tolman |
| **Algoritmo en IA** | Q-Learning, TD Learning | Búsqueda en Árbol, Planificación |
| **Sustrato Neural** | Ganglios basales, Dopamina | Hipocampo, Corteza Prefrontal |

---

**Diapositiva 16: Nivel 3: Implementación**

**¿Cómo se Realiza Físicamente el Aprendizaje?**

---

**Diapositiva 17: La Implementación del Aprendizaje "Sin Modelo"**

**El Sistema de Dopamina como Señal de Error**

* El trabajo de Wolfram Schultz demostró que las neuronas de **dopamina** no codifican la recompensa en sí, sino el **error de predicción de la recompensa**. 10  
* **Recompensa inesperada:** Estallido de dopamina (δ\>0).  
* **Recompensa esperada:** Sin cambio en la dopamina (δ=0).  
* **Omisión de recompensa esperada:** Pausa en la dopamina (δ\<0).  
* Esta señal de dopamina se proyecta a los **ganglios basales** y modula la plasticidad sináptica, implementando físicamente el algoritmo de aprendizaje TD. 10

---

**Diapositiva 18: La Implementación del Aprendizaje "Basado en Modelo"**

**El Circuito del Mapa y el Planificador**

* **Hipocampo (El Mapa):**  
  * Contiene "células de lugar" (*place cells*) que se activan en ubicaciones específicas del entorno. 30  
  * Colectivamente, forman un mapa neural del espacio.  
  * Es el sustrato físico del "mapa cognitivo" de Tolman. 31  
* **Corteza Prefrontal (El Planificador):**  
  * Crucial para la toma de decisiones y el comportamiento dirigido a metas.  
  * Utiliza el "mapa" del hipocampo para simular y planificar acciones futuras. 20

---

**Diapositiva 19: La Implementación en IA**

**Redes Neuronales Artificiales (RNA)**

* **Análogo de la neurona:** Un "nodo" o "unidad".  
* **Análogo de la sinapsis:** Un "peso" numérico en la conexión.  
* El aprendizaje consiste en ajustar estos pesos para minimizar el error. 18  
* **Ejemplo: DeepMind DQN**  
  * Combinó el aprendizaje TD con redes neuronales profundas.  
  * Aprendió a jugar videojuegos de Atari a nivel sobrehumano a partir de los píxeles de la pantalla.  
  * Un ejemplo claro de un sistema "sin modelo" implementado en silicio. 33

---

**Diapositiva 20: Conclusión**

**Hacia una Ciencia Integrada del Comportamiento Adaptable**

---

**Diapositiva 21: Síntesis de los Tres Niveles**

* **Computacional:** Definimos el aprendizaje como un problema de optimización para predecir y controlar los SBI, enfrentando el desafío de la asignación de crédito. 4  
* **Algorítmico:** Vimos que la dicotomía histórico-psicológica (asociativo vs. cognitivo) corresponde a dos familias de algoritmos en IA (sin modelo vs. basado en modelo) que coexisten en el cerebro. 19  
* **Implementación:** Encontramos los sustratos físicos para estos dos sistemas: el circuito dopamina/ganglios basales para el aprendizaje habitual y el circuito hipocampo/CPF para la planificación flexible. 10

---

**Diapositiva 22: La Convergencia de Campos**

* La **Psicología** proporciona los fenómenos conductuales y las preguntas fundamentales.  
* La **Inteligencia Artificial** ofrece el lenguaje matemático y los modelos formales para probar hipótesis. 34  
* La **Neurociencia** revela el anclaje biológico, mostrando cómo se implementan los algoritmos.

*El estudio del comportamiento adaptable es un gran desafío compartido que requiere la colaboración continua entre estos campos.*

---

**Diapositiva 23: Preguntas y Discusión**

**Gracias**

\<\!DOCTYPE html\>  
\<html lang="es" class="scroll-smooth"\>  
\<head\>  
    \<meta charset="UTF-8"\>  
    \<meta name="viewport" content="width=device-width, initial-scale=1.0"\>  
    \<title\>Comportamiento Adaptable: Una Exploración Interactiva\</title\>  
    \<\!-- Chosen Palette: Warm Neutral Academia \--\>  
    \<\!-- Application Structure Plan: The application is structured as a single-page exploratory tool following David Marr's three levels of analysis (Computational, Algorithmic, Implementation). This top-down approach is pedagogically sound, starting with the 'why' (the problem), moving to the 'how' (the solutions/algorithms), and finishing with the 'what' (the physical substrate). A sticky top navigation allows users to jump between these core sections, facilitating both linear learning and non-linear exploration. Key concepts are reinforced with interactive charts and diagrams (e.g., MVT simulation, Rescorla-Wagner model, Tolman's rats, Dopamine firing signals), transforming passive reading into active engagement. This structure was chosen to make a complex, multi-disciplinary topic digestible and to explicitly highlight the parallels between psychology and AI within a coherent framework. \--\>  
    \<\!-- Visualization & Content Choices:   
        \- Goal: Explain the core problem of resource allocation. \-\> Method: Simple HTML/CSS diagram for the Time Constraint formula. \-\> Interaction: Static visual aid. \-\> Justification: A simple, clear representation of a foundational concept.  
        \- Goal: Demonstrate an optimal solution to a foraging problem. \-\> Method: Interactive Line Chart (Chart.js) for the Marginal Value Theorem. \-\> Interaction: User clicks a button to change 'travel time', which updates the chart to show the new optimal 'leave time'. \-\> Justification: Dynamically shows how optimal strategy changes with environmental constraints.  
        \- Goal: Compare Associative vs. Cognitive learning. \-\> Method: Two-column layout with interactive charts. Rescorla-Wagner model shown with a Bar Chart (Chart.js) updated by user-run 'trials'. Tolman's latent learning shown with a Line Chart (Chart.js) where a user can 'introduce reward' to see the dramatic performance shift. \-\> Justification: Allows direct comparison and makes abstract models tangible through simulation.  
        \- Goal: Illustrate the neural basis of learning signals. \-\> Method: Clickable HTML/CSS brain diagram and a dynamic Line Chart (Chart.js) for dopamine firing. \-\> Interaction: User clicks brain regions for info and selects reward scenarios ('unexpected', 'expected', 'omitted') to see the corresponding dopamine signal on the chart. \-\> Justification: Connects abstract algorithmic concepts (prediction error) to concrete, observable neural phenomena.  
        \- Library/Method: All charts use Chart.js on a \<canvas\> element. Diagrams and layouts use structured HTML with Tailwind CSS.  
    \--\>  
    \<\!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. \--\>  
    \<script src="https://cdn.tailwindcss.com"\>\</script\>  
    \<script src="https://cdn.jsdelivr.net/npm/chart.js"\>\</script\>  
    \<style\>  
        body {  
            font-family: 'Inter', sans-serif;  
        }  
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700\&display=swap');  
        .chart-container {  
            position: relative;  
            width: 100%;  
            max-width: 600px;  
            margin-left: auto;  
            margin-right: auto;  
            height: 300px;  
            max-height: 400px;  
        }  
        @media (min-width: 768px) {  
            .chart-container {  
                height: 350px;  
            }  
        }  
        .nav-active {  
            color: \#0d9488; /\* teal-600 \*/  
            border-bottom-color: \#0d9488;  
        }  
    \</style\>  
\</head\>  
\<body class="bg-slate-50 text-slate-800"\>

    \<header class="bg-white/80 backdrop-blur-lg sticky top-0 z-50 border-b border-slate-200"\>  
        \<nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"\>  
            \<div class="flex justify-between items-center h-16"\>  
                \<h1 class="text-xl md:text-2xl font-bold text-teal-700"\>Comportamiento Adaptable\</h1\>  
                \<div class="hidden md:flex items-center space-x-8"\>  
                    \<a href="\#computacional" class="nav-link text-gray-600 hover:text-teal-600 transition-colors duration-300 border-b-2 border-transparent pb-1"\>Nivel Computacional\</a\>  
                    \<a href="\#algoritmico" class="nav-link text-gray-600 hover:text-teal-600 transition-colors duration-300 border-b-2 border-transparent pb-1"\>Nivel Algorítmico\</a\>  
                    \<a href="\#implementacion" class="nav-link text-gray-600 hover:text-teal-600 transition-colors duration-300 border-b-2 border-transparent pb-1"\>Nivel de Implementación\</a\>  
                \</div\>  
                \<div class="md:hidden"\>  
                    \<button id="menu-btn" class="text-slate-600 focus:outline-none"\>  
                        \<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"\>\<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"\>\</path\>\</svg\>  
                    \</button\>  
                \</div\>  
            \</div\>  
            \<div id="mobile-menu" class="hidden md:hidden py-2"\>  
                \<a href="\#computacional" class="block py-2 px-4 text-sm text-gray-600 hover:bg-teal-50"\>Nivel Computacional\</a\>  
                \<a href="\#algoritmico" class="block py-2 px-4 text-sm text-gray-600 hover:bg-teal-50"\>Nivel Algorítmico\</a\>  
                \<a href="\#implementacion" class="block py-2 px-4 text-sm text-gray-600 hover:bg-teal-50"\>Nivel de Implementación\</a\>  
            \</div\>  
        \</nav\>  
    \</header\>

    \<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12"\>  
          
        \<div class="text-center mb-12"\>  
            \<h2 class="text-3xl md:text-4xl font-bold text-slate-900 mb-4"\>Un Análisis Multinivel del Aprendizaje\</h2\>  
            \<p class="max-w-3xl mx-auto text-lg text-slate-600"\>  
                Esta aplicación explora el comportamiento adaptable a través de los tres niveles de análisis de David Marr. Conectaremos conceptos fundamentales de la psicología del aprendizaje con los avances en inteligencia artificial para construir una comprensión unificada de cómo los sistemas inteligentes, biológicos o artificiales, se adaptan a su entorno.  
            \</p\>  
        \</div\>

        \<\!-- SECCIÓN 1: NIVEL COMPUTACIONAL \--\>  
        \<section id="computacional" class="mb-16 scroll-mt-16"\>  
            \<div class="bg-white p-6 md:p-8 rounded-xl shadow-sm border border-slate-200"\>  
                \<span class="inline-block bg-teal-100 text-teal-800 text-sm font-semibold px-3 py-1 rounded-full mb-4"\>Nivel 1\</span\>  
                \<h3 class="text-3xl font-bold text-teal-700 mb-4"\>El Nivel Computacional: ¿Qué problema resuelve el aprendizaje?\</h3\>  
                \<p class="text-slate-600 mb-6 text-lg"\>  
                    Este nivel define el \*\*QUÉ\*\* y el \*\*PORQUÉ\*\*. Se enfoca en el objetivo fundamental del sistema y la lógica de la estrategia para resolverlo, abstrayéndose de los mecanismos específicos. El problema central es la supervivencia: optimizar la obtención de recursos y minimizar los peligros en un mundo incierto.  
                \</p\>

                \<div class="grid md:grid-cols-2 gap-8"\>  
                    \<div class="bg-slate-100 p-6 rounded-lg"\>  
                        \<h4 class="font-bold text-xl mb-3 text-slate-800"\>Objetivo: Maximizar los SBI\</h4\>  
                        \<p class="text-slate-600 mb-4"\>El fin último del aprendizaje es predecir y controlar la ocurrencia de \*\*Sucesos Biológicamente Importantes (SBI)\*\* —eventos como comida, agua, peligro o pareja que impactan la supervivencia y reproducción. Esto debe hacerse bajo una restricción fundamental: el tiempo es finito.\</p\>  
                        \<div class="bg-white p-4 rounded-md text-center shadow-inner"\>  
                            \<p class="font-mono text-lg text-slate-700"\>T \= t\<sub\>1\</sub\> \+ t\<sub\>2\</sub\> \+ ... \+ t\<sub\>n\</sub\>\</p\>  
                            \<p class="text-sm text-slate-500 mt-2"\>El tiempo total (T) es la suma del tiempo dedicado a cada comportamiento (t).\</p\>  
                        \</div\>  
                    \</div\>  
                    \<div class="bg-slate-100 p-6 rounded-lg"\>  
                        \<h4 class="font-bold text-xl mb-3 text-slate-800"\>El Reto: Asignación de Crédito\</h4\>  
                        \<p class="text-slate-600 mb-4"\>¿Cómo sabe un organismo qué acción específica o qué señal del entorno fue la responsable de un SBI, especialmente cuando hay un retraso? Este es el \<span class="font-semibold text-teal-700"\>problema de la asignación de crédito\</span\>, un desafío universal para el aprendizaje.\</p\>  
                        \<div class="flex space-x-4"\>  
                             \<div class="flex-1 text-center p-3 bg-white rounded-md shadow-inner"\>  
                                \<p class="font-semibold"\>Estímulo-Resultado\</p\>  
                                \<p class="text-sm text-slate-500"\>(Cond. Clásico)\</p\>  
                            \</div\>  
                            \<div class="flex-1 text-center p-3 bg-white rounded-md shadow-inner"\>  
                                \<p class="font-semibold"\>Acción-Resultado\</p\>  
                                \<p class="text-sm text-slate-500"\>(Cond. Instrumental)\</p\>  
                            \</div\>  
                        \</div\>  
                    \</div\>  
                \</div\>

                \<div class="mt-8 pt-8 border-t border-slate-200"\>  
                    \<h4 class="text-2xl font-bold text-center mb-4 text-slate-800"\>Un Modelo Computacional: Teoría del Forrajeo Óptimo\</h4\>  
                    \<p class="text-slate-600 text-center max-w-2xl mx-auto mb-6"\>El \<span class="font-semibold"\>Teorema del Valor Marginal\</span\> predice cómo un animal decide cuándo abandonar una parcela de comida. La solución óptima es irse cuando la tasa de ganancia en la parcela actual cae por debajo de la tasa promedio del hábitat.\</p\>  
                    \<div class="chart-container"\>  
                        \<canvas id="mvtChart"\>\</canvas\>  
                    \</div\>  
                    \<div class="text-center mt-4"\>  
                        \<p class="text-slate-600 mb-2"\>Simula el efecto del tiempo de viaje entre parcelas:\</p\>  
                        \<button id="mvt-btn" class="bg-teal-600 text-white font-semibold px-4 py-2 rounded-md hover:bg-teal-700 transition-colors"\>Cambiar Tiempo de Viaje\</button\>  
                    \</div\>  
                \</div\>  
            \</div\>  
        \</section\>

        \<\!-- SECCIÓN 2: NIVEL ALGORÍTMICO \--\>  
        \<section id="algoritmico" class="mb-16 scroll-mt-16"\>  
            \<div class="bg-white p-6 md:p-8 rounded-xl shadow-sm border border-slate-200"\>  
                \<span class="inline-block bg-amber-100 text-amber-800 text-sm font-semibold px-3 py-1 rounded-full mb-4"\>Nivel 2\</span\>  
                \<h3 class="text-3xl font-bold text-amber-700 mb-4"\>El Nivel Algorítmico: ¿Cómo se resuelve el problema?\</h3\>  
                \<p class="text-slate-600 mb-6 text-lg"\>  
                    Este nivel describe el \*\*CÓMO\*\*. Explora los procesos, representaciones y algoritmos que transforman la información de entrada (experiencia) en una salida (comportamiento adaptado). Aquí encontramos la conexión directa entre las teorías psicológicas y los modelos de IA.  
                \</p\>  
                  
                \<div class="grid md:grid-cols-2 gap-8"\>  
                    \<\!-- Columna 1: Asociativo / Sin Modelo \--\>  
                    \<div class="border border-slate-200 p-6 rounded-lg"\>  
                        \<h4 class="text-2xl font-bold text-slate-800 mb-2"\>Enfoque Asociativo (RL Sin Modelo)\</h4\>  
                        \<p class="text-slate-600 mb-4"\>Aprende políticas de acción directas (hábitos) o valores para cada situación. Es computacionalmente rápido y eficiente, pero inflexible.\</p\>  
                          
                        \<div class="mt-4"\>  
                            \<h5 class="font-bold text-lg mb-2"\>Psicología: Modelo Rescorla-Wagner\</h5\>  
                            \<p class="text-sm text-slate-600 mb-4"\>El aprendizaje es impulsado por el \<span class="font-semibold"\>error de predicción\</span\>: la diferencia entre lo que ocurre ($\\lambda$) y lo que se esperaba ($\\Sigma V$).\</p\>  
                             \<div class="chart-container" style="height:250px;"\>  
                                \<canvas id="rwChart"\>\</canvas\>  
                            \</div\>  
                            \<div class="text-center mt-4"\>  
                                \<button id="rw-trial-btn" class="bg-amber-500 text-white font-semibold px-4 py-2 rounded-md hover:bg-amber-600 transition-colors"\>Ejecutar Ensayo\</button\>  
                                \<button id="rw-reset-btn" class="bg-slate-200 text-slate-700 font-semibold px-4 py-2 rounded-md hover:bg-slate-300 transition-colors"\>Reiniciar\</button\>  
                            \</div\>  
                        \</div\>  
                    \</div\>

                    \<\!-- Columna 2: Cognitivo / Con Modelo \--\>  
                    \<div class="border border-slate-200 p-6 rounded-lg"\>  
                        \<h4 class="text-2xl font-bold text-slate-800 mb-2"\>Enfoque Cognitivo (RL Basado en Modelo)\</h4\>  
                        \<p class="text-slate-600 mb-4"\>Construye un "mapa cognitivo" o modelo interno del mundo. Permite la planificación y un comportamiento flexible, pero es computacionalmente costoso.\</p\>

                        \<div class="mt-4"\>  
                            \<h5 class="font-bold text-lg mb-2"\>Psicología: Mapas Cognitivos de Tolman\</h5\>  
                            \<p class="text-sm text-slate-600 mb-4"\>Los organismos aprenden la estructura del entorno incluso sin recompensa (aprendizaje latente), lo que les permite planificar rutas novedosas.\</p\>  
                             \<div class="chart-container" style="height:250px;"\>  
                                \<canvas id="tolmanChart"\>\</canvas\>  
                            \</div\>  
                            \<div class="text-center mt-4"\>  
                                \<button id="tolman-reward-btn" class="bg-amber-500 text-white font-semibold px-4 py-2 rounded-md hover:bg-amber-600 transition-colors"\>Introducir Recompensa (Día 11)\</button\>  
                                \<button id="tolman-reset-btn" class="bg-slate-200 text-slate-700 font-semibold px-4 py-2 rounded-md hover:bg-slate-300 transition-colors"\>Reiniciar\</button\>  
                            \</div\>  
                        \</div\>  
                    \</div\>  
                \</div\>  
            \</div\>  
        \</section\>

        \<\!-- SECCIÓN 3: NIVEL DE IMPLEMENTACIÓN \--\>  
        \<section id="implementacion" class="mb-16 scroll-mt-16"\>  
            \<div class="bg-white p-6 md:p-8 rounded-xl shadow-sm border border-slate-200"\>  
                \<span class="inline-block bg-sky-100 text-sky-800 text-sm font-semibold px-3 py-1 rounded-full mb-4"\>Nivel 3\</span\>  
                \<h3 class="text-3xl font-bold text-sky-700 mb-4"\>El Nivel de Implementación: ¿Cómo se realiza físicamente?\</h3\>  
                \<p class="text-slate-600 mb-6 text-lg"\>  
                    Este nivel se pregunta por el \*\*SUSTRATO FÍSICO\*\*. ¿Cómo se implementan los algoritmos en el "hardware" biológico del cerebro o en los chips de silicio? Aquí, la neurociencia revela los mecanismos que dan vida a los algoritmos del aprendizaje.  
                \</p\>  
                  
                \<div class="grid md:grid-cols-5 gap-8"\>  
                    \<div class="md:col-span-2"\>  
                        \<h4 class="text-2xl font-bold text-slate-800 mb-4"\>Circuitos Cerebrales del Aprendizaje\</h4\>  
                        \<p class="text-slate-600 mb-6"\>Diferentes algoritmos de aprendizaje son implementados por distintos circuitos cerebrales. Haz clic en las áreas para ver su función.\</p\>  
                        \<div class="relative w-full max-w-xs mx-auto"\>  
                            \<div class="aspect-square bg-slate-200 rounded-full flex items-center justify-center"\>  
                                \<p class="text-slate-500 text-sm"\>Cerebro\</p\>  
                            \</div\>  
                            \<button class="brain-region absolute p-2 text-xs bg-amber-200 text-amber-800 rounded-full shadow-lg hover:scale-110 transition-transform" style="top: 20%; left: 65%;"\>CPF\</button\>  
                            \<button class="brain-region absolute p-2 text-xs bg-amber-200 text-amber-800 rounded-full shadow-lg hover:scale-110 transition-transform" style="top: 40%; left: 25%;"\>Hipocampo\</button\>  
                            \<button class="brain-region absolute p-2 text-xs bg-teal-200 text-teal-800 rounded-full shadow-lg hover:scale-110 transition-transform" style="top: 50%; left: 55%;"\>G. Basales\</button\>  
                            \<button class="brain-region absolute p-2 text-xs bg-teal-200 text-teal-800 rounded-full shadow-lg hover:scale-110 transition-transform" style="top: 65%; left: 40%;"\>Dopamina (VTA/SNc)\</button\>  
                        \</div\>  
                        \<div id="brain-info-box" class="mt-4 p-4 bg-slate-100 rounded-lg text-slate-700 text-sm hidden"\>  
                            \<h5 id="brain-info-title" class="font-bold mb-1"\>\</h5\>  
                            \<p id="brain-info-text"\>\</p\>  
                        \</div\>  
                    \</div\>  
                    \<div class="md:col-span-3"\>  
                        \<h4 class="text-2xl font-bold text-slate-800 mb-4"\>La Dopamina como Señal de Error de Predicción\</h4\>  
                        \<p class="text-slate-600 mb-6"\>Las neuronas de dopamina no codifican la recompensa en sí, sino el \<span class="font-semibold"\>error de predicción\</span\>, una implementación física perfecta del algoritmo de Aprendizaje por Diferencia Temporal (TD).\</p\>  
                        \<div class="chart-container"\>  
                            \<canvas id="dopamineChart"\>\</canvas\>  
                        \</div\>  
                        \<div class="text-center mt-4 space-x-2"\>  
                            \<button class="dopamine-btn bg-sky-500 text-white font-semibold px-3 py-1 rounded-md text-sm" data-type="unexpected"\>Recompensa Inesperada\</button\>  
                            \<button class="dopamine-btn bg-slate-200 text-slate-700 font-semibold px-3 py-1 rounded-md text-sm" data-type="expected"\>Recompensa Esperada\</button\>  
                            \<button class="dopamine-btn bg-slate-200 text-slate-700 font-semibold px-3 py-1 rounded-md text-sm" data-type="omitted"\>Recompensa Omitida\</button\>  
                        \</div\>  
                    \</div\>  
                \</div\>

            \</div\>  
        \</section\>

        \<footer class="text-center mt-16 pt-8 border-t border-slate-200"\>  
            \<h3 class="text-2xl font-bold text-slate-800 mb-3"\>Conclusión: Hacia una Ciencia Integrada\</h3\>  
            \<p class="max-w-3xl mx-auto text-slate-600"\>  
                El enfoque de Marr nos permite ver la psicología del aprendizaje, la neurociencia y la inteligencia artificial no como campos separados, sino como facetas de una misma empresa: entender cómo los sistemas inteligentes se adaptan. La psicología define el problema, la IA lo formaliza y la neurociencia revela su implementación biológica.  
            \</p\>  
        \</footer\>

    \</main\>

    \<script\>  
    document.addEventListener('DOMContentLoaded', function () {  
        // Mobile menu toggle  
        const menuBtn \= document.getElementById('menu-btn');  
        const mobileMenu \= document.getElementById('mobile-menu');  
        menuBtn.addEventListener('click', () \=\> {  
            mobileMenu.classList.toggle('hidden');  
        });

        // Active nav link highlighting on scroll  
        const sections \= document.querySelectorAll('section');  
        const navLinks \= document.querySelectorAll('.nav-link');  
        window.addEventListener('scroll', () \=\> {  
            let current \= '';  
            sections.forEach(section \=\> {  
                const sectionTop \= section.offsetTop;  
                if (pageYOffset \>= sectionTop \- 80\) {  
                    current \= section.getAttribute('id');  
                }  
            });

            navLinks.forEach(link \=\> {  
                link.classList.remove('nav-active');  
                if (link.getAttribute('href').includes(current)) {  
                    link.classList.add('nav-active');  
                }  
            });  
        });

        // Chart.js global settings  
        Chart.defaults.font.family \= "'Inter', sans-serif";  
        Chart.defaults.plugins.tooltip.backgroundColor \= 'rgba(0, 0, 0, 0.7)';  
        Chart.defaults.plugins.tooltip.titleFont \= { weight: 'bold' };

        // \--- MVT Chart \---  
        let mvtTravelTime \= 5; // Start with short travel time  
        const mvtCtx \= document.getElementById('mvtChart').getContext('2d');  
        const gainFunction \= Array.from({length: 20}, (\_, i) \=\> 100 / (i \+ 1));  
          
        function getMvtData(travelTime) {  
            const averageRate \= 100 / (5 \+ travelTime); // Simplified average rate  
            const optimalTime \= gainFunction.findIndex(gain \=\> gain \< averageRate);  
            return {  
                labels: Array.from({length: 20}, (\_, i) \=\> \`t=${i+1}\`),  
                datasets: \[{  
                    label: 'Ganancia en la Parcela',  
                    data: gainFunction,  
                    borderColor: '\#0d9488', // teal-600  
                    backgroundColor: 'rgba(13, 148, 136, 0.1)',  
                    fill: true,  
                    tension: 0.4,  
                }, {  
                    label: 'Tasa Promedio del Hábitat',  
                    data: Array(20).fill(averageRate),  
                    borderColor: '\#f59e0b', // amber-500  
                    borderDash: \[5, 5\],  
                    fill: false,  
                }, {  
                    label: 'Punto Óptimo de Salida',  
                    data: Array(20).fill(null).map((\_, i) \=\> i \=== optimalTime ? gainFunction\[optimalTime\] : null),  
                    pointBackgroundColor: '\#ef4444', // red-500  
                    pointRadius: 8,  
                    pointHoverRadius: 10,  
                    fill: false,  
                    type: 'scatter',  
                }\]  
            };  
        }

        const mvtChart \= new Chart(mvtCtx, {  
            type: 'line',  
            data: getMvtData(mvtTravelTime),  
            options: {  
                responsive: true,  
                maintainAspectRatio: false,  
                plugins: {  
                    title: { display: true, text: 'Decisión de abandonar una parcela de comida' },  
                    tooltip: {  
                        callbacks: {  
                            label: function(context) {  
                                if (context.dataset.label \=== 'Punto Óptimo de Salida' && context.parsed.y \!== null) {  
                                    return \` Salir en t=${context.parsed.x \+ 1}\`;  
                                }  
                                return \`${context.dataset.label}: ${context.parsed.y.toFixed(2)}\`;  
                            }  
                        }  
                    }  
                },  
                scales: {  
                    y: { title: { display: true, text: 'Tasa de Ganancia de Energía' } },  
                    x: { title: { display: true, text: 'Tiempo en la Parcela' } }  
                }  
            }  
        });

        document.getElementById('mvt-btn').addEventListener('click', () \=\> {  
            mvtTravelTime \= mvtTravelTime \=== 5 ? 15 : 5;  
            const newData \= getMvtData(mvtTravelTime);  
            mvtChart.data.datasets \= newData.datasets;  
            mvtChart.update();  
        });

        // \--- Rescorla-Wagner Chart \---  
        const rwCtx \= document.getElementById('rwChart').getContext('2d');  
        let v\_A \= 0; // Associative strength for stimulus A  
        let v\_B \= 0; // Associative strength for stimulus B  
        const alpha \= 0.5, beta \= 0.5, lambda \= 1;  
          
        const rwChart \= new Chart(rwCtx, {  
            type: 'bar',  
            data: {  
                labels: \['V(A)', 'V(B)'\],  
                datasets: \[{  
                    label: 'Fuerza Asociativa',  
                    data: \[v\_A, v\_B\],  
                    backgroundColor: \['rgba(245, 158, 11, 0.6)', 'rgba(100, 116, 139, 0.6)'\],  
                    borderColor: \['rgb(245, 158, 11)', 'rgb(100, 116, 139)'\],  
                    borderWidth: 1  
                }\]  
            },  
            options: {  
                responsive: true,  
                maintainAspectRatio: false,  
                scales: { y: { beginAtZero: true, max: 1.2, title: {display: true, text: 'V'} } },  
                plugins: { title: { display: true, text: 'ΔV \= αβ(λ \- ΣV)' } }  
            }  
        });

        document.getElementById('rw-trial-btn').addEventListener('click', () \=\> {  
            let error \= lambda \- (v\_A \+ v\_B);  
            let delta\_v\_A \= alpha \* beta \* error;  
            v\_A \= Math.min(v\_A \+ delta\_v\_A, lambda);  
            rwChart.data.datasets\[0\].data \= \[v\_A, v\_B\];  
            rwChart.update();  
        });  
        document.getElementById('rw-reset-btn').addEventListener('click', () \=\> {  
            v\_A \= 0; v\_B \= 0;  
            rwChart.data.datasets\[0\].data \= \[v\_A, v\_B\];  
            rwChart.update();  
        });

        // \--- Tolman's Latent Learning Chart \---  
        const tolmanCtx \= document.getElementById('tolmanChart').getContext('2d');  
        const days \= Array.from({length: 17}, (\_, i) \=\> \`Día ${i+1}\`);  
        let group1\_errors \= \[10, 8, 6, 5, 4, 3, 2.5, 2.2, 2, 2, 2, 2, 2, 2, 2, 2, 2\];  
        let group2\_errors \= \[10, 10.5, 11, 10, 10.8, 10.2, 10.5, 10.3, 10, 9.8, 10, 10.1, 10.2, 10, 9.9, 10, 10\];  
        let group3\_base\_errors \= \[10, 10.2, 10.8, 11, 10.5, 10.4, 10.6, 10, 10.2, 10.3, 10.1\];  
        let group3\_reward\_errors \= \[6, 4, 3, 2.5, 2, 2\];  
        let group3\_errors \= \[...group3\_base\_errors, null, null, null, null, null, null\];

        const tolmanChart \= new Chart(tolmanCtx, {  
            type: 'line',  
            data: {  
                labels: days,  
                datasets: \[  
                    { label: 'Grupo 1 (Recompensa)', data: group1\_errors, borderColor: '\#0d9488', tension: 0.1, fill: false },  
                    { label: 'Grupo 2 (Sin Recompensa)', data: group2\_errors, borderColor: '\#64748b', tension: 0.1, fill: false },  
                    { label: 'Grupo 3 (Recompensa Retardada)', data: group3\_errors, borderColor: '\#f59e0b', tension: 0.1, fill: false },  
                \]  
            },  
            options: {  
                responsive: true,  
                maintainAspectRatio: false,  
                scales: { y: { beginAtZero: true, title: {display: true, text: 'Errores Promedio'} } },  
                plugins: { title: { display: true, text: 'Experimento de Aprendizaje Latente' } }  
            }  
        });

        document.getElementById('tolman-reward-btn').addEventListener('click', () \=\> {  
             tolmanChart.data.datasets\[2\].data \= \[...group3\_base\_errors, ...group3\_reward\_errors\];  
             tolmanChart.update();  
        });  
        document.getElementById('tolman-reset-btn').addEventListener('click', () \=\> {  
             tolmanChart.data.datasets\[2\].data \= \[...group3\_base\_errors, null, null, null, null, null, null\];  
             tolmanChart.update();  
        });  
          
        // \--- Brain Region Info Box \---  
        const brainRegions \= document.querySelectorAll('.brain-region');  
        const brainInfoBox \= document.getElementById('brain-info-box');  
        const brainInfoTitle \= document.getElementById('brain-info-title');  
        const brainInfoText \= document.getElementById('brain-info-text');

        const brainData \= {  
            'CPF': { title: 'Corteza Prefrontal (CPF)', text: 'Sede de la planificación, toma de decisiones y comportamiento dirigido a metas. Utiliza el "mapa" para la deliberación (Control Basado en Modelo).', class: 'bg-amber-100' },  
            'Hipocampo': { title: 'Hipocampo', text: 'Fundamental para la memoria espacial y episódica. Crea y almacena los "mapas cognitivos" del entorno (Control Basado en Modelo).', class: 'bg-amber-100' },  
            'G. Basales': { title: 'Ganglios Basales', text: 'Reciben la señal de dopamina para fortalecer o debilitar conexiones. Cruciales para la formación de hábitos (Control Sin Modelo).', class: 'bg-teal-100' },  
            'Dopamina (VTA/SNc)': { title: 'Sistema Dopaminérgico', text: 'Genera la señal de error de predicción de recompensa. No codifica la recompensa, sino la "sorpresa". Es el motor del aprendizaje Sin Modelo.', class: 'bg-teal-100' }  
        };  
          
        brainRegions.forEach(btn \=\> {  
            btn.addEventListener('click', () \=\> {  
                const regionName \= btn.textContent;  
                const data \= brainData\[regionName\];  
                brainInfoTitle.textContent \= data.title;  
                brainInfoText.textContent \= data.text;  
                brainInfoBox.className \= \`mt-4 p-4 rounded-lg text-slate-700 text-sm ${data.class}\`;  
            });  
        });

        // \--- Dopamine Firing Chart \---  
        const dopamineCtx \= document.getElementById('dopamineChart').getContext('2d');  
        const baseFiring \= Array(20).fill(1);  
        let currentDopamineData \= \[...baseFiring\];

        const dopamineChart \= new Chart(dopamineCtx, {  
            type: 'line',  
            data: {  
                labels: Array.from({length: 20}, (\_, i) \=\> i),  
                datasets: \[{  
                    label: 'Tasa de Disparo de Dopamina',  
                    data: currentDopamineData,  
                    borderColor: '\#0ea5e9', // sky-500  
                    backgroundColor: 'rgba(14, 165, 233, 0.1)',  
                    fill: true,  
                    stepped: true  
                }\]  
            },  
            options: {  
                responsive: true,  
                maintainAspectRatio: false,  
                scales: {   
                    y: { min: \-1, max: 5, title: { display: true, text: 'Actividad Relativa' } },  
                    x: { ticks: { display: false } }  
                },  
                plugins: {   
                    title: { display: true, text: 'Señal Neuronal de Error de Predicción' },  
                    legend: { display: false },  
                    annotation: {  
                        annotations: {  
                            line1: {  
                                type: 'line',  
                                xMin: 5, xMax: 5,  
                                borderColor: 'rgb(255, 99, 132)',  
                                borderWidth: 2,  
                                borderDash: \[6, 6\],  
                                label: { content: 'Señal', enabled: true, position: 'start' }  
                            },  
                            line2: {  
                                type: 'line',  
                                xMin: 15, xMax: 15,  
                                borderColor: 'rgb(255, 99, 132)',  
                                borderWidth: 2,  
                                borderDash: \[6, 6\],  
                                label: { content: 'Recompensa', enabled: true, position: 'start' }  
                            }  
                        }  
                    }  
                }  
            }  
        });

        document.querySelectorAll('.dopamine-btn').forEach(btn \=\> {  
            btn.addEventListener('click', (e) \=\> {  
                document.querySelectorAll('.dopamine-btn').forEach(b \=\> b.classList.replace('bg-sky-500', 'bg-slate-200').classList.replace('text-white','text-slate-700'));  
                e.target.classList.replace('bg-slate-200', 'bg-sky-500').classList.replace('text-slate-700','text-white');

                const type \= e.target.dataset.type;  
                let newData \= \[...baseFiring\];  
                switch(type) {  
                    case 'unexpected': // Positive prediction error  
                        newData\[15\] \= 4; newData\[16\] \= 4;  
                        break;  
                    case 'expected': // No prediction error  
                        newData\[5\] \= 4; newData\[6\] \= 4;  
                        break;  
                    case 'omitted': // Negative prediction error  
                        newData\[5\] \= 4; newData\[6\] \= 4;  
                        newData\[15\] \= 0; newData\[16\] \= 0;  
                        break;  
                }  
                dopamineChart.data.datasets\[0\].data \= newData;  
                dopamineChart.update();  
            });  
        });

    });  
    \</script\>  
\</body\>  
\</html\>

