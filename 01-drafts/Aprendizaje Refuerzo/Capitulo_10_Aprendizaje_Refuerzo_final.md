# Capítulo 10: Modelos de Aprendizaje por Refuerzo {#sec-modelos-refuerzo}

## Objetivos del Capítulo

Al finalizar este capítulo, deberías ser capaz de explicar cómo los modelos formales de aprendizaje por refuerzo traducen la Ley del Efecto de Thorndike en ecuaciones matemáticas precisas que generan predicciones cuantitativas. Comprenderás que las curvas de aprendizaje representan sistemas dinámicos discretos, y que el modelo de Bush-Mosteller admite tres interpretaciones complementarias que son matemáticamente equivalentes: carga-descarga de un integrador con fuga, reducción del error de predicción, y filtrado exponencial de experiencias pasadas. Reconocerás el papel crítico del parámetro alpha como determinante de la tasa de aprendizaje y comprenderás sus implicaciones adaptativas para balancear la importancia relativa del pasado versus el presente. Finalmente, entenderás cómo estos modelos formalizan los principios de asignación de crédito discutidos en capítulos anteriores, y cómo la perspectiva de filtros conecta el aprendizaje con problemas más generales de estimación y predicción en sistemas dinámicos.

---

## Introducción: De la Descripción a la Formalización

Como resultado de la selección natural, los agentes biológicos son sistemas con mecanismos que les permiten detectar, predecir y controlar los sucesos biológicamente importantes (SBI). Recordemos que los SBI son sucesos con valor hedónico—también conocidos como reforzadores—los cuales incrementan el éxito reproductivo diferencial de los organismos. Para ejecutar estas funciones de detección, predicción y control de SBI, los organismos necesitan hacer contacto con la estructura causal del entorno: estructura a la cual designamos bajo el término de propiedades estadísticas del entorno.

Una parte de la estructura estadística de los SBI consiste de estímulos que se despliegan en el tiempo y en el espacio, los cuales en algunas ocasiones aparecen solos, mientras que en otras instancias aparecen seguidos (contiguos) de un refuerzo. Hay tiempos sin nubes y otros con nubes; estos últimos pueden ser seguidos o no de lluvia. La tarea para el organismo es determinar si existe una relación causal entre las nubes y la lluvia. Una segunda parte de la estructura estadística del entorno consiste del hecho de que, con relación al despliegue de respuestas de los organismos en el tiempo y en el espacio, algunas ocasiones estas respuestas van seguidas de un refuerzo y en otras ocasiones no. Hay veces en las que ustedes le dicen "hola" a una persona y otras en las que no. Después del "hola" ustedes pueden recibir, o no, otro "hola" de regreso.

Los protocolos de condicionamiento clásico e instrumental definen, como una primera aproximación, las estructuras causales más simples que se estudiaron en buena parte del siglo XX. En los dos capítulos anteriores, resumimos la literatura empírica acerca del papel de la contigüidad en la asignación de crédito a estímulos y respuestas que permiten predecir y controlar los refuerzos. Presentamos evidencia que muestra que aunque la contigüidad es importante, esta no es ni necesaria ni suficiente para la asignación de crédito. Los organismos son sensibles a contingencias estadísticas—relaciones de probabilidad condicional—no meramente a proximidad temporal. Pueden aprender con demoras sustanciales entre eventos, y detectan activamente si un evento fue causado por su acción o ocurrió independientemente.

Esta evidencia empírica nos dice qué aprenden los organismos. Pero para construir una ciencia genuinamente predictiva del aprendizaje, necesitamos especificar cómo lo hacen. Necesitamos un algoritmo que describa paso a paso cómo se actualiza el conocimiento, una función que transforme experiencia en valor predictivo, y un modelo que genere predicciones cuantitativas testables. Para dar cuenta de los resultados empíricos presentados en los capítulos anteriores, en la segunda mitad del siglo XX se consolidó un modelo matemático, conocido como Aprendizaje por Refuerzo, junto con varias modificaciones del mismo. El propósito de este capítulo es presentar estos modelos y su desarrollo como respuesta a la evidencia sobre el papel de la contigüidad.

---

## Parte I: Curvas de Aprendizaje como Datos

### El Fenómeno Empírico

El aprendizaje es un proceso dinámico, que describe los cambios en el comportamiento como una función de la experiencia de los organismos. Desde finales del siglo XIX se han obtenido "curvas de aprendizaje" que describen cambios en alguna medida de ejecución de los organismos como una función de las ocasiones en las que los estímulos que encaran o las respuestas que despliegan van seguidos de un refuerzo.

Como ilustración, presentamos dos ejemplos. El primero es la curva de adquisición y extinción de la frecuencia del reflejo de parpadeo en un protocolo de condicionamiento clásico con humanos. Las curvas representan diferentes intensidades del soplo al ojo (Passey, 1948). El procedimiento consistió en presentar un tono (EC) seguido por un soplo de aire al ojo (EI) de diferentes intensidades. La medida dependiente fue el número de respuestas de parpadeo anticipatorio (RC) por bloque de cinco ensayos. Los resultados mostraron que intensidades mayores del EI producían adquisición más rápida y una asíntota más alta en el condicionamiento.

[FIGURA 10.1: Curvas de adquisición y extinción del reflejo de parpadeo según Passey (1948)]

Un segundo ejemplo es la curva de adquisición de la velocidad de tocar una palanca en un protocolo de condicionamiento instrumental con ratas (Ramond, 1954). Las dos curvas representan los datos obtenidos con diferentes niveles de privación. El procedimiento consistió en entrenar ratas a presionar una palanca para obtener comida, con un grupo sometido a 22 horas de privación y otro a solo 4 horas. La medida dependiente fue la velocidad recíproca de latencia (1/tiempo hasta responder), la cual incrementó más rápidamente y alcanzó una asíntota más alta para el grupo con mayor privación.

[FIGURA 10.2: Curvas de adquisición de presión de palanca según Ramond (1954)]

### La Forma Característica

La siguiente curva de adquisición idealizada captura los datos de adquisición presentados en las dos figuras anteriores. Podemos ver que es una curva negativamente acelerada de ganancias decrecientes. Esto es, el impacto de que un refuerzo siga a una respuesta se va reduciendo conforme se acumulan las ocasiones en las que una respuesta va seguida de un refuerzo. Los primeros ensayos reforzados producen cambios grandes en la ejecución; los ensayos posteriores producen cambios cada vez menores, hasta que la curva se aproxima a una asíntota.

[FIGURA 10.3: Curva de adquisición idealizada mostrando ganancias decrecientes]

### Una Controversia Metodológica Importante

Una alternativa teórica supone que el aprendizaje no es un proceso gradual, sino uno de cambio abrupto. Si este fuese el caso, las curvas de adquisición de crecimiento gradual decreciente podrían ser un artefacto de promediar la ejecución de animales con cambios no continuos en el aprendizaje. Considere el caso de un grupo de animales cuya ejecución es promediada. Uno de los animales empieza a responder al ensayo 10, otro al 20, otro al 30, otro al 40 y así hasta un animal que responde al ensayo 80. Al promediar estos datos, la curva de aprendizaje aparecerá como una curva continua, aunque ningún animal individual muestre un proceso gradual.

Por esta razón, Skinner, Estes, Spence y más recientemente Gallistel argumentan en favor de analizar los datos de sujetos individuales y, preferentemente, registros acumulativos en lugar de los datos promediados. En ese mismo sentido, los modelos que presentaremos a continuación resultan válidos cuando los datos analizados provienen de sujetos individuales, o cuando el aprendizaje genuinamente es gradual y no un artefacto de promediación.

Los modelos de refuerzo modelan la forma de las curvas de adquisición obtenidas empíricamente. El modelo de refuerzo más general es un sistema dinámico que describe los cambios en el valor de un estímulo y/o respuesta a lo largo del tiempo, como una función del número de ocasiones en las que un estímulo o una respuesta van seguidas de un refuerzo.

---

## Parte II: Sistemas Dinámicos Discretos

### Ecuaciones en Diferencias

Antes de presentar el modelo de refuerzo específico, es necesario introducir el concepto de sistemas dinámicos discretos y ecuaciones en diferencias. El estudio del aprendizaje, la asignación de crédito, es una instancia de un sistema dinámico: un sistema cuyo valor cambia a lo largo del tiempo como una función de sus valores anteriores. Cuando el tiempo es discreto (ensayos, días, eventos), encontramos muchos ejemplos de sistemas dinámicos: crecimiento económico, cambios en las frecuencias de genes en una población, propagación de rumores y, actualmente, una pandemia. En estos sistemas, nos interesa determinar su trayectoria a lo largo del tiempo, determinar si tiene un equilibrio y encontrar cuál es ese.

Las ecuaciones en diferencias representan el comportamiento dinámico y son ecuaciones recursivas que operan en cada momento en el tiempo t. Considere el caso más sencillo, en que el valor en cada momento es simplemente el valor inicial más 1:

$$Y_t = Y_{t-1} + 1$$

Si el primer valor de $Y_0 = 0$, entonces:

$$Y_1 = Y_0 + 1 = 1$$
$$Y_2 = Y_1 + 1 = 2$$
$$Y_3 = Y_2 + 1 = 3$$

La secuencia continúa indefinidamente, representando crecimiento lineal constante.

### Un Ejemplo más Interesante: Crecimiento Exponencial

El crecimiento geométrico de una epidemia proporciona un ejemplo ya interesante. Considere el caso de una epidemia, como la del COVID-19. Deseamos describir los cambios en contagios cada día transcurrido y si tiene un equilibrio. Si cada persona infectada contagia en promedio a 1.5 personas por día, la ecuación en diferencias que describe el crecimiento de la epidemia es:

$$Y_t = aY_{t-1}$$

Para valores de $a$ mayores a 1 (en nuestro ejemplo, $a = 1.5$), si comenzamos con $Y_0 = 1$ persona infectada:

$$Y_1 = 1.5 \times 1 = 1.5$$
$$Y_2 = 1.5 \times 1.5 = 2.25$$
$$Y_3 = 1.5 \times 2.25 = 3.375$$

La solución general es $Y_t = a^t$. Cuando $a > 1$, el sistema crece exponencialmente sin límite. Cuando $a < 1$, decae exponencialmente hacia cero. Cuando $a = 1$, permanece constante en su valor inicial.

[FIGURA 10.4: Simulador de ecuaciones en diferencias mostrando diferentes valores de $a$]

Este marco de ecuaciones en diferencias será la base para entender el modelo de aprendizaje por refuerzo como un sistema dinámico discreto donde el "estado" del sistema es el valor predictivo de un estímulo o respuesta, y donde este estado se actualiza en cada ensayo basándose en la experiencia con reforzadores.

---

## Parte III: El Modelo de Refuerzo Canónico

### Asignando Valor a Estímulos y Respuestas

Los modelos de refuerzo le asignan un número a cada estímulo y/o respuesta: esta magnitud representa la calidad del estímulo/respuesta como predictor de un refuerzo. A lo largo del siglo XX, a esta magnitud se le conoció como fuerza del reflejo, fuerza del hábito, fuerza asociativa del estímulo y fuerza de la respuesta. Para nuestros propósitos, el número refleja el valor predictivo de un estímulo o de una respuesta, y simplemente le llamaremos el valor $V$ del estímulo $i$, o el valor $Q$ de la respuesta $i$.

El modelo de refuerzo propone que después de cada presentación de un estímulo o la emisión de una respuesta, su valor se actualiza como una función de si este va seguido o no de un refuerzo. Es importante señalar que el modelo asume que la actualización del valor de un estímulo o una respuesta solo ocurre en las ocasiones en las que estos se presentan. El valor predictivo de un tono solo se actualiza cuando el tono se presenta y no en su ausencia. Esto implica que el mero paso del tiempo sin el tono o la presentación de otros estímulos no alteran el valor del tono. Por esta razón, a estos modelos se les llama también modelos basados en ensayos.

Esto es, la variable importante que determina el valor predictivo (la asignación de crédito) es el número de ocasiones en las que un estímulo o una respuesta son seguidos de un reforzador. Mientras mayor es este número, mayor será el valor adquirido por el estímulo o la respuesta. De forma complementaria, el valor de estos estímulos o respuestas decrementa cuando estos se presentan sin ser seguidos por el reforzador.

### La Formalización de Bush y Mosteller

En 1950, Bush y Mosteller propusieron una versión matemática del modelo de aprendizaje por refuerzo esbozado en el párrafo anterior. Esta versión sigue siendo la base que sustenta varios de los modelos más recientes, tanto en la psicología como en el aprendizaje de máquinas.

La estructura matemática de los modelos de refuerzo tiene diferentes interpretaciones teóricas. Nosotros consideraremos tres:

1. Un proceso de carga-descarga
2. Un proceso de reducción del error de predicción
3. Un filtro exponencial que pondera el pasado

Veremos que estas tres interpretaciones son matemáticamente equivalentes: describen exactamente el mismo proceso computacional desde diferentes perspectivas conceptuales.

---

## Parte IV: Primera Interpretación—Carga y Descarga

### La Metáfora del Integrador con Fuga

Los modelos de refuerzo son una propuesta de solución computacional a la asignación de crédito. La solución incluye dos pasos: el primero es la reducción del tamaño inicial del espacio de candidatos para incluir únicamente sucesos que son contiguos, similares, novedosos y evolutivamente relevantes con relación a los SBI. El segundo es un mecanismo que permita ir reduciendo, a través de la experiencia, el espacio de candidatos hasta terminar con uno solo. El modelo de refuerzo canónico combina un algoritmo de ascenso de colina con el sesgo de contigüidad. Bush y Mosteller (1951) formalizaron esta clase de modelos que, en diferentes variantes, han dominado la literatura teórica y experimental en el estudio del aprendizaje a partir de la década de los 70s del siglo pasado.

La forma más literal de interpretar el modelo de refuerzo es como un proceso en el cual cada refuerzo incrementa (carga, fortalece) el valor del estímulo/respuesta que le antecede y cada ocurrencia del estímulo/respuesta sin ser acompañado de un refuerzo decrementa (descarga) su valor. Este es un proceso en el que la variable $V$ se actualiza con cada ocurrencia del estímulo/respuesta como una función que varía dependiendo de si el estímulo/respuesta va seguido o no de un refuerzo.

La carga de la batería de su celular es un ejemplo muy cercano a su vida cotidiana que ejemplifica el proceso descrito. Para que su celular funcione, ustedes tienen que conectarlo a una toma de corriente. Mientras está conectado, la carga de la batería se va actualizando hasta llegar a un punto máximo. Al usarlo sin tenerlo conectado, la batería se va descargando como una función del uso del celular sin una carga adicional.

### Desarrollo de la Ecuación

Veamos cómo se aplica este modelo en el caso de un protocolo estándar de condicionamiento clásico. En este contexto, se observa un estímulo/respuesta candidato a la asignación de crédito, y a cada presentación de él se le conoce como un ensayo. Cada ocurrencia de un ensayo puede estar acompañado o no de un SBI. Consideremos que $V_x$ represente el valor predictivo de un estímulo $x$. Nos interesa la dinámica del cambio en $V_x$ conforme un organismo experimenta ensayos en los que un estímulo condicionado $x$ va seguido de un refuerzo.

Para facilitar la aplicación del modelo, supondremos que el tiempo es discreto y el subíndice $t$ representa el momento en que se presenta el estímulo $x$. La variable $V_{x,t+1}$ es el valor actualizado del estímulo $x$ en el siguiente ensayo $t+1$. La variable $R$ representa si se presentó o no un refuerzo después del estímulo $x$. $R$ puede tener solo dos valores: uno si el refuerzo se presenta después del estímulo $x$, o cero si el estímulo $x$ se presenta sin ser seguido por el refuerzo.

Vamos a asumir que $V_{x,t+1}$ depende sólo de dos factores:

1. Su valor acumulado hasta el ensayo inmediatamente anterior $V_{x,t}$
2. El valor de $R_t$ en el ensayo actual

La expresión más simple sería:

$$V_{x,t+1} = V_{x,t} + R_t$$

Sin embargo, la expresión anterior supone que el efecto del valor de $V$ en el ensayo anterior tiene el mismo peso que el reforzador presentado o no en el momento actual. Nosotros deseamos que la ecuación capture la importancia relativa de las dos variables. Para ello, supondremos que el impacto de esas dos variables es una suma ponderada, donde el parámetro $\alpha$ representa el peso de ponderación asignado a cada uno de los dos factores. Si el valor de $\alpha$ está entre cero y uno, los parámetros asociados con cada factor serán $\alpha$ y $(1-\alpha)$.

$$V_{x,t+1} = (1-\alpha)V_{x,t} + \alpha R_t, \quad \text{donde: } 0 < \alpha < 1$$

Esta es la ecuación fundamental del modelo de Bush-Mosteller. Es una ecuación recurrente, en la que en cada iteración (presentación del estímulo $x$) hay siempre un $V_x$ viejo y un $V_x$ nuevo. La ecuación describe la actualización de $V_x$ de ensayo a ensayo, como una función del valor de $V_x$ acumulado hasta el ensayo anterior y la presentación o ausencia del SBI. $V_{x,t}$ es la integración, el acumulado, de todas las experiencias previas con el refuerzo. En cada ensayo, la $V_x$ nueva del ensayo anterior se convierte en la $V_x$ vieja del presente ensayo, contribuyendo a generar una nueva $V_x$.

### El Papel del Parámetro Alpha

El parámetro $\alpha$, que multiplica al refuerzo, determina la velocidad del aprendizaje: mientras mayor sea su valor, más rápido será el aprendizaje. Una forma de entender el papel de $\alpha$ es considerarlo como el parámetro que especifica la importancia de la experiencia acumulada hasta el momento (el valor del pasado), relativa a la ocurrencia o no de un refuerzo (el valor del presente).

Valores cercanos a cero sugieren que la experiencia acumulada es más importante que una nueva experiencia con un refuerzo, resultando en poco aprendizaje. Valores cercanos a uno sugieren que la presentación del refuerzo es más importante que la experiencia acumulada hasta ese momento, resultando en un rápido aprendizaje.

Consideren una interacción de larga duración con una amistad que ha resultado en un valor alto para ustedes asociado con esa relación. Nos podemos preguntar cuál es el impacto de que una mañana esa amistad no los salude. Si el parámetro $\alpha$ fuese cercano a cero, el no saludo no modificaría sustancialmente el valor $V$ de la amistad, mientras que si el valor de $\alpha$ fuese cercano a uno, a pesar de los años de experiencias positivas con esa amistad, su impacto en el valor $V$ sería más significativo.

[FIGURAS 10.5-10.7: Simulaciones mostrando adquisición con diferentes valores de alpha]

---

## Parte V: Segunda Interpretación—Reducción del Error de Predicción

### Reacomodando la Ecuación

El reacomodo de los términos de la ecuación de carga-descarga permite una interpretación alternativa del modelo de aprendizaje por refuerzo: esta vez en términos de un mecanismo de reducción en el error de predicción. Estos modelos representan hoy la versión dominante en la psicología del aprendizaje y las neurociencias.

Arreglando los términos de la ecuación del integrador con fuga:

$$V_{t+1} = (1-\alpha)V_t + \alpha R_t$$

$$V_{t+1} = V_t - \alpha V_t + \alpha R_t$$

$$V_{t+1} = V_t + \alpha(R_t - V_t)$$

Restándole $V_t$ a ambos lados de la ecuación anterior, y dejando que $\Delta V_x = V_{x,t+1} - V_{x,t}$, entonces el cambio de ensayo a ensayo es descrito, agrupando términos:

$$\Delta V_x = V_t + \alpha(R_t - V_t) - V_t$$

$$\Delta V_x = \alpha(R_t - V_{x,t})$$

Esta segunda forma de la ecuación enfatiza la magnitud del cambio momento a momento, en lugar del valor del estímulo momento a momento.

### El Error de Predicción como Motor del Aprendizaje

En cualquiera de las dos formas de presentar la ecuación del integrador, el valor $V$ es una función de la diferencia entre el refuerzo obtenido y el valor del estímulo en el tiempo $t$. A esta diferencia dentro del paréntesis se le conoce como el error de predicción: la diferencia entre la $R$ que se obtiene y lo que se esperaba obtener, $V$. Cuando esta diferencia es igual a cero, no habrá cambios en el valor de $V$. Es por esta forma de la ecuación que estamos llamando a $V_t$ el valor predictivo de la respuesta.

El parámetro $\alpha$, entre 0 y 1, sigue representando la velocidad del aprendizaje, en este caso, la importancia del error de predicción. En la literatura contemporánea, a la ecuación anterior se le conoce como regla delta:

$$V_{t+1} = V_t + \alpha \delta$$

donde $\delta = (R_t - V_{x,t})$ es el error de predicción, es decir, el motor del aprendizaje. Bajo el formato que enfatiza la magnitud del cambio, delta se incorpora a la ecuación de la siguiente forma:

$$\Delta V_x = \alpha \delta$$

Esta interpretación del modelo conecta directamente con los hallazgos empíricos de los capítulos anteriores. Cuando los organismos aprenden contingencias estadísticas en lugar de meras contigüidades, están esencialmente comparando el valor esperado de un reforzador con el valor obtenido. El error de predicción cuantifica precisamente esta discrepancia. Si un estímulo predice perfectamente un reforzador ($V = R$ siempre), el error es cero y no hay más aprendizaje. Si un estímulo es seguido inesperadamente por un reforzador ($R > V$), el error es positivo y el valor incrementa. Si un estímulo esperado no produce el reforzador ($R < V$), el error es negativo y el valor decrementa.

Esta perspectiva de reducción de error ha sido extraordinariamente influyente en neurociencia. Las neuronas dopaminérgicas en el mesencéfalo de mamíferos codifican precisamente esta señal de error de predicción, incrementando su actividad cuando un reforzador es mayor de lo esperado, y reduciendo su actividad cuando es menor de lo esperado. Este descubrimiento, realizado por Wolfram Schultz y colaboradores en la década de 1990, representa uno de los vínculos más directos entre modelos computacionales de aprendizaje y mecanismos neurales.

---

## Parte VI: Tercera Interpretación—Filtros y Predicción

### El Problema de la Predicción

Hasta ahora hemos presentado el modelo de aprendizaje por refuerzo desde dos perspectivas: carga-descarga y reducción de error de predicción. Existe una tercera forma de conceptualizar el mismo proceso matemático que conecta el aprendizaje con un problema más general en estadística y procesamiento de señales: el problema de estimar el valor esperado de una variable ruidosa a partir de una secuencia de observaciones.

Vimos que el aprendizaje por refuerzo es un proceso de actualización de las predicciones que hace un organismo, que resultan de comparar el resultado obtenido con la predicción. Aceptando que el aprendizaje por refuerzo representa una tarea de predicción a partir de las experiencias con un conjunto de observaciones, podemos preguntarnos acerca de posibles reglas para hacer la predicción.

Considere el caso del número de contagios de COVID en nuestro país. Para el gobierno y para nosotros es importante predecir el número de contagios que habrá mañana y cuál es la tendencia que muestra. En una serie de encuentros en el tiempo, la regla más sencilla para predecir la siguiente observación es el promedio de las observaciones hasta ese momento.

### El Promedio Simple y sus Limitaciones

La estrategia más sencilla sería obtener el promedio de todos los contagios a partir del primero de marzo. Sumamos todos los casos diarios y los dividimos por el número de días observados:

$$\mu_n = \frac{1}{n}\sum_{i=1}^n x_i$$

Esta estrategia tiene dos problemas importantes:

1. Le asigna un mismo peso a todos los días, sin importar qué tan lejanos en el pasado ocurrieron
2. No toma en cuenta el ruido en los datos (por ejemplo, los fines de semana se trabaja menos en la recopilación de datos)

Para muchas situaciones, pareciera más razonable darle un menor peso a los acontecimientos más alejados del presente. Un evento que ocurrió hace un mes debería tener menos influencia en nuestra predicción de mañana que un evento que ocurrió ayer.

### Medias Corridas como Filtros

Para resolver el problema del ruido, necesitamos un filtro. El propósito del filtro es alisar (suavizar) los datos. Una técnica común es la media o mediana corrida. Consiste en seleccionar una ventana de cierto número de observaciones, obtener su media o mediana, y sustituir ese número por el centro de la ventana. La ventana se desliza una observación a la derecha y se repite la operación.

Considere los siguientes números de contagios diarios en miles:

25, 28, 22, 30, 27, 15, 20, 100, 27, 32, 39, 40, 18, 22, 44, 30, 35

Usando una mediana corrida de tres, obtenemos la mediana de los tres primeros números y nos movemos un día a la derecha:

25, 28, 27, 27, 20, 20, 27, 32, 39, 39, 22, 22, 30, 30

Noten que el primer y último número de la serie no pertenecen a una ventana de tres y desaparecen. El valor raro de 100 (un outlier) desaparece, revelando la tendencia subyacente.

Con mediana corrida de 5:

27, 27, 22, 27, 27, 32, 33, 32, 32, 39, 30, 30

La técnica es útil para alisar datos (experiencias) y ver tendencias. Sin embargo, tiene dos problemas: computacionalmente es costoso (requiere almacenar y ordenar múltiples valores), y le da el mismo peso a todos los eventos dentro de la ventana independientemente de qué tan atrás hayan ocurrido.

### De la Media Simple a la Regla Delta

Considere una máquina tragamonedas, conocidas en inglés como "one-arm bandit". En esa máquina, cada respuesta es reforzada de acuerdo a una probabilidad constante. Considere una secuencia de resultados probabilísticos para una respuesta:

1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1

Para predecir el siguiente resultado, se puede computar la media de todos los resultados obtenidos:

$$V_t = \frac{1}{t}\sum_{i=1}^t r_i$$

Ahora presentaremos una forma alternativa de expresar la media que nos llevará directamente a la ecuación de reducción de error. La demostración procede de la siguiente manera:

$$\mu_n = \frac{1}{n}\sum_{i=1}^n x_i$$

Vamos a descomponer la sumatoria en dos términos: $x_n$ y $\sum_{i=1}^{n-1} x_i$:

$$= \frac{1}{n}\left(x_n + \sum_{i=1}^{n-1} x_i\right)$$

Noten que si dividimos el segundo término entre el número de observaciones hasta antes de $n$, $(n-1)$, tendremos la media $\mu_{n-1}$:

$$\mu_{n-1} = \frac{1}{n-1}\sum_{i=1}^{n-1} x_i$$

Multiplicando por $(n-1)$, ahora podemos sustituir la segunda sumatoria:

$$(n-1)\mu_{n-1} = \sum_{i=1}^{n-1} x_i$$

Regresando a nuestra ecuación original, podemos usar $(n-1)\mu_{n-1}$:

$$\mu_n = \frac{1}{n}(x_n + (n-1)\mu_{n-1})$$

Expandimos:

$$\mu_n = \frac{1}{n}(x_n + n\mu_{n-1} - \mu_{n-1})$$

Reacomodando términos obtenemos la ecuación:

$$\mu_n = \mu_{n-1} + \frac{1}{n}(x_n - \mu_{n-1})$$

¡Esta es exactamente la misma forma que la ecuación de reducción de error de predicción! La única diferencia es que en la media simple, el "parámetro de aprendizaje" es $\alpha = 1/n$, lo cual significa que disminuye conforme se acumulan más observaciones. Con 10 observaciones, $\alpha = 0.1$; con 100 observaciones, $\alpha = 0.01$.

### Media Exponencial Corrida (MEC)

La limitación de la media simple es que le da el mismo peso a todas las observaciones. Para darle más peso a las observaciones recientes, usamos una media ponderada donde los pesos decaen exponencialmente hacia el pasado. Esta es precisamente la interpretación de la ecuación de Bush-Mosteller con un $\alpha$ constante.

En un promedio ponderado, se suma el producto de cada observación multiplicada por un peso diferente y se divide por la suma de todos los pesos:

$$MCP = \frac{\sum_{i=1}^n w_i x_i}{\sum_{i=1}^n w_i}$$

En el caso de la media exponencial corrida, dejamos que los pesos decaigan exponencialmente. Si expandimos completamente la ecuación de Bush-Mosteller iterando hacia atrás, obtenemos:

$$V_t = \alpha R_t + \alpha(1-\alpha)R_{t-1} + \alpha(1-\alpha)^2 R_{t-2} + \ldots + (1-\alpha)^t V_0$$

Esta expresión revela que $V_t$ es un promedio ponderado de todos los reforzadores pasados, donde los pesos decaen exponencialmente. El reforzador más reciente tiene peso $\alpha$, el anterior tiene peso $\alpha(1-\alpha)$, el siguiente tiene peso $\alpha(1-\alpha)^2$, y así sucesivamente. Cada reforzador adicional en el pasado es ponderado por un factor adicional de $(1-\alpha)$.

Para verificar que estos pesos suman correctamente a 1 (asumiendo que el término $(1-\alpha)^t V_0$ se vuelve negligible para $t$ grande), usamos la serie geométrica:

$$\sum_{i=0}^{\infty} \alpha(1-\alpha)^i = \alpha \times \frac{1}{1-(1-\alpha)} = \alpha \times \frac{1}{\alpha} = 1$$

Los pesos efectivamente suman a 1, confirmando que $V_t$ es un promedio ponderado apropiado.

### La "Vida Media" del Filtro

El parámetro $\alpha$ determina qué tan rápido decaen los pesos hacia el pasado. Podemos definir la "vida media" del filtro como el número de ensayos que toma para que un peso decaiga a la mitad de su valor inicial:

$$(1-\alpha)^{\tau} = 0.5$$

Resolviendo para $\tau$:

$$\tau = \frac{\log(0.5)}{\log(1-\alpha)} \approx \frac{0.693}{\alpha}$$

Para $\alpha = 0.3$, la vida media es aproximadamente 2.3 ensayos. Para $\alpha = 0.1$, la vida media es aproximadamente 6.9 ensayos. Esto significa que con $\alpha = 0.3$, un reforzador de hace 2-3 ensayos tiene solo la mitad del peso que el reforzador más reciente. Con $\alpha = 0.1$, se requieren 7 ensayos para el mismo decaimiento.

Esta perspectiva de filtro exponencial conecta el aprendizaje por refuerzo con un problema fundamental en procesamiento de señales: cómo estimar una señal subyacente a partir de observaciones ruidosas. El organismo enfrenta el problema de que los reforzadores individuales son eventos discretos (0 o 1), pero desea estimar la probabilidad subyacente de reforzamiento (un número continuo entre 0 y 1). La media exponencial corrida proporciona una solución computacionalmente eficiente que pondera apropiadamente las observaciones recientes sin requerir almacenar todo el historial de experiencias.

---

## Parte VII: Tres Interpretaciones, Un Proceso

Hemos presentado tres formas diferentes de conceptualizar la ecuación de Bush-Mosteller:

**1. Modelo de un integrador con fuga (carga-descarga)**:

$$V_{t+1} = (1-\alpha)V_t + \alpha R_t$$

Esta es la interpretación original, en la cual un refuerzo incrementa la "fuerza de una respuesta" y decrece con cada ocasión en la cual la respuesta no es seguida por un refuerzo.

**2. Modelo de reducción de error de predicción**:

$$V_{t+1} = V_t + \alpha(R_t - V_t)$$

Es hoy en día la interpretación dominante, que implica que el aprendizaje es el resultado de un proceso de ascenso de colina en la dirección del menor error de predicción.

**3. Modelo de un filtro de media exponencial corrida**:

$$V_t = \alpha \sum_{i=0}^{t-1} (1-\alpha)^i R_{t-i-1} + (1-\alpha)^t V_0$$

Esta interpretación implica que el valor de la respuesta sigue al promedio de refuerzo que produce, con una ponderación que le atribuye más peso a los refuerzos más recientes.

Estas tres interpretaciones son matemáticamente equivalentes: describen exactamente el mismo proceso computacional. La elección de cuál interpretación usar depende del contexto y del aspecto del proceso que deseamos enfatizar. La interpretación de carga-descarga es intuitiva y conecta con metáforas físicas. La interpretación de reducción de error conecta con principios generales de optimización y con mecanismos neurales. La interpretación de filtrado conecta con teoría de procesamiento de señales y estimación estadística.

---

## Conceptos Clave y Síntesis

Este capítulo ha presentado la formalización matemática del aprendizaje asociativo mediante el modelo de Bush-Mosteller, un sistema dinámico discreto que actualiza el valor predictivo de estímulos y respuestas basándose en experiencia con reforzadores. El modelo captura las curvas de aprendizaje empíricamente observadas: adquisición negativamente acelerada durante el reforzamiento y extinción durante su ausencia.

Vimos que las curvas de aprendizaje agregadas pueden ser artefactos de promediación, y que el análisis de sujetos individuales es preferible cuando es posible. El modelo de Bush-Mosteller resulta apropiado cuando el aprendizaje genuinamente es gradual, no un proceso de todo-o-nada.

La ecuación fundamental admite tres interpretaciones complementarias. Como integrador con fuga, conceptualiza el aprendizaje como carga y descarga de fuerza asociativa. Como reducción de error de predicción, enfatiza que el motor del aprendizaje es la discrepancia entre lo esperado y lo obtenido. Como filtro exponencial, revela que el organismo está estimando el valor esperado del reforzador mediante un promedio ponderado que favorece experiencias recientes.

El parámetro $\alpha$ determina la tasa de aprendizaje y representa un compromiso adaptativo fundamental: valores altos permiten aprendizaje rápido pero alta susceptibilidad al ruido; valores bajos producen estimaciones estables pero lentas para detectar cambios genuinos en las contingencias. La selección natural ha ajustado este parámetro para balancear estos requerimientos conflictivos según el nicho ecológico de cada especie.

Crucialmente, el modelo de Bush-Mosteller formaliza los principios de asignación de crédito discutidos en capítulos anteriores. La actualización basada en error de predicción captura cómo los organismos son sensibles a contingencias estadísticas más que a meras contigüidades. La estructura basada en ensayos respeta el hallazgo de que solo los estímulos y respuestas presentes pueden ser actualizados. Y el marco de filtrado exponencial proporciona un mecanismo computacionalmente eficiente para estimar relaciones causales a partir de experiencias secuenciales ruidosas.

Este modelo es la base para extensiones más sofisticadas que examinaremos en capítulos subsecuentes. El modelo de Rescorla-Wagner modifica la ecuación de error para incluir competencia entre múltiples estímulos, explicando fenómenos como bloqueo y ensombrecimiento. Los algoritmos de diferencias temporales extienden el modelo para aprendizaje con secuencias de estados y recompensas demoradas. Y los modelos de atención ajustan $\alpha$ dinámicamente basándose en la predictabilidad de cada estímulo. Pero todos estos modelos heredan la estructura fundamental del modelo de Bush-Mosteller presentado en este capítulo.

---

## Lecturas Recomendadas

**Artículos Clásicos Fundamentales:**

- Bush, R. R., & Mosteller, F. (1951). "A mathematical model for simple learning." *Psychological Review*, 58(5), 313-323. [El artículo original que introduce el modelo—lectura esencial]

- Estes, W. K. (1950). "Toward a statistical theory of learning." *Psychological Review*, 57(2), 94-107. [Modelo contemporáneo a Bush-Mosteller con enfoque probabilístico]

**Sobre Curvas de Aprendizaje y Gradualidad:**

- Gallistel, C. R., Fairhurst, S., & Balsam, P. (2004). "The learning curve: Implications of a quantitative analysis." *PNAS*, 101(36), 13124-13131. [Argumenta contra aprendizaje gradual usando análisis cuantitativo sofisticado]

- Gallistel, C. R., & Gibbon, J. (2000). "Time, rate, and conditioning." *Psychological Review*, 107(2), 289-344. [Perspectiva alternativa a modelos asociativos, enfatizando procesamiento temporal]

**Aplicaciones Modernas:**

- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. [Capítulos 2-6 extienden Bush-Mosteller a aprendizaje por refuerzo moderno; disponible gratis en línea]

- Schultz, W., Dayan, P., & Montague, P. R. (1997). "A neural substrate of prediction and reward." *Science*, 275(5306), 1593-1599. [Evidencia que neuronas dopaminérgicas codifican error de predicción]

- Dayan, P., & Daw, N. D. (2008). "Decision theory, reinforcement learning, and the brain." *Cognitive, Affective, & Behavioral Neuroscience*, 8(4), 429-453. [Conecta modelos computacionales con neurociencia]

**Textos de Referencia:**

- Rescorla, R. A. (1988). "Pavlovian conditioning: It's not what you think it is." *American Psychologist*, 43(3), 151-160. [Revisión accesible del modelo Rescorla-Wagner y evidencia empírica]

- Mackintosh, N. J. (1974). *The Psychology of Animal Learning*. Academic Press. [Capítulos 3-4: Tratamiento clásico comprensivo de teorías asociativas]

- Domjan, M. (2014). *The Principles of Learning and Behavior* (7th ed.). Cengage Learning. [Capítulo 4: Introducción pedagógica a modelos de condicionamiento]

**Para Profundizar:**

- Pearce, J. M., & Hall, G. (1980). "A model for Pavlovian learning: Variations in the effectiveness of conditioned but not of unconditioned stimuli." *Psychological Review*, 87(6), 532-552. [Modelo alternativo donde α (atencionalidad) cambia con experiencia]

- Miller, R. R., Barnet, R. C., & Grahame, N. J. (1995). "Assessment of the Rescorla-Wagner model." *Psychological Bulletin*, 117(3), 363-386. [Evaluación crítica comprehensiva del modelo R-W]

- Niv, Y. (2009). "Reinforcement learning in the brain." *Journal of Mathematical Psychology*, 53(3), 139-154. [Revisión moderna conectando aprendizaje por refuerzo con neurobiología]

---

## Ejercicios

### Ejercicios Conceptuales

**1. Análisis de la Controversia sobre Gradualidad**

Gallistel argumenta que el aprendizaje podría no ser gradual sino un proceso de todo-o-nada, y que las curvas graduales son artefactos de promediación.

a) Diseñe un experimento que permita distinguir entre estas dos hipótesis. Especifique qué datos recolectaría, cómo los analizaría, y qué patrón de resultados favorecería la hipótesis de aprendizaje gradual versus la hipótesis de todo-o-nada.

b) Si el aprendizaje realmente fuera de todo-o-nada, ¿qué implicaciones tendría esto para la validez del modelo de Bush-Mosteller? ¿Seguiría siendo útil el modelo incluso si el aprendizaje no es gradual a nivel individual? Justifique su respuesta.

c) Considere un grupo de 10 animales donde cada uno muestra aprendizaje de todo-o-nada pero en diferentes momentos (ensayos 5, 10, 15, 20, 25, 30, 35, 40, 45, 50). Si promediamos sus datos y ajustamos el modelo de Bush-Mosteller a este promedio, ¿qué valor de α esperaría obtener? ¿Sería este α interpretable como "tasa de aprendizaje" del organismo individual?

**2. Tres Interpretaciones, Un Proceso**

El modelo de Bush-Mosteller admite tres interpretaciones: carga-descarga, reducción de error, y filtro exponencial.

a) Para cada interpretación, identifique una situación aplicada o un fenómeno empírico donde esa interpretación específica proporciona la mejor intuición para entender el proceso. Por ejemplo, ¿en qué contexto es más útil pensar en "carga-descarga" versus "reducción de error"?

b) Explique por qué la equivalencia matemática entre estas tres interpretaciones es significativa. ¿Qué nos dice sobre la naturaleza del aprendizaje que un mismo proceso pueda ser conceptualizado de formas tan diferentes?

c) La interpretación de filtro exponencial sugiere que el organismo está "estimando" la probabilidad de reforzamiento. ¿Esto implica que el organismo realiza un cálculo consciente? ¿Cómo reconcilia esta interpretación estadística con el hecho de que insectos simples también muestran aprendizaje por refuerzo?

**3. El Parámetro Alpha y sus Implicaciones Adaptativas**

El parámetro α determina la velocidad de aprendizaje y representa un compromiso entre estabilidad y plasticidad.

a) En un ambiente completamente estable (las contingencias nunca cambian), ¿qué valor de α sería óptimo? ¿Y en un ambiente extremadamente volátil donde las contingencias cambian constantemente? Justifique matemáticamente usando la ecuación del modelo.

b) Considere dos especies: una que vive en un hábitat estacional predecible (flores abundantes en primavera, escasas en invierno) y otra que vive en un ambiente impredecible (disponibilidad de alimento aleatoria día a día). ¿Qué diferencias esperaría en sus valores de α? ¿Qué presiones selectivas habrían dado forma a estos valores?

c) En humanos, hay evidencia de que α puede cambiar dinámicamente dependiendo del contexto (mayor en situaciones de incertidumbre alta). Proponga un mecanismo computacional simple que permitiría ajustar α basándose en la volatilidad percibida del ambiente. ¿Cómo "mediría" un organismo la volatilidad para ajustar su α apropiadamente?

**4. Limitaciones del Modelo de Bush-Mosteller**

Aunque el modelo de Bush-Mosteller captura muchos fenómenos, tiene limitaciones conocidas.

a) El modelo actualiza cada estímulo/respuesta independientemente. Explique por qué esto es problemático para fenómenos como bloqueo y ensombrecimiento discutidos en el Capítulo 8. ¿Qué tendría que cambiar en la ecuación para capturar competencia entre estímulos?

b) El modelo asume que α es constante a través del aprendizaje. Sin embargo, hay evidencia de que la atención a un estímulo cambia con la experiencia (modelo de Pearce-Hall). ¿En qué situaciones sería adaptativo que α disminuyera con la experiencia? ¿Y en qué situaciones sería adaptativo que aumentara?

c) El modelo es "basado en ensayos": solo actualiza valores cuando los estímulos/respuestas están presentes. ¿Qué fenómenos de aprendizaje requieren procesos que operen incluso en ausencia del estímulo? (Pista: considere consolidación de memoria, "latent inhibition", efectos de espaciamiento temporal).

**5. Interpretación del Error de Predicción**

La interpretación de reducción de error sugiere que δ = (R - V) es el motor del aprendizaje.

a) ¿Qué signo tiene δ cuando un reforzador esperado no ocurre (extinción)? ¿Y cuando un reforzador inesperado ocurre (adquisición)? Trace un gráfico de δ a lo largo de ensayos durante: (i) adquisición inicial, (ii) extinción después de adquisición completa, (iii) readquisición después de extinción.

b) En neurociencia, las neuronas dopaminérgicas codifican δ. Estas neuronas incrementan disparo para δ > 0 y reducen disparo para δ < 0. Si farmacológicamente bloquearas estos receptores dopaminérgicos, ¿qué predicción hace el modelo sobre el aprendizaje? ¿Se detendría completamente, o habría efectos diferenciales en adquisición versus extinción?

c) Algunos autores argumentan que los organismos no minimizan error absoluto sino error al cuadrado (δ²). ¿Cuál sería la diferencia práctica entre minimizar |δ| versus δ²? ¿Cómo cambiaría la ecuación de actualización si usáramos δ² en lugar de δ?

### Ejercicios Cuantitativos

**6. Simulación de Adquisición y Extinción**

Un estímulo X se presenta en ensayos discretos. En ensayos 1-20, X es seguido por refuerzo (R=1). En ensayos 21-40, X se presenta solo (R=0). Use α = 0.3 y V₀ = 0.

a) Calcule V manualmente para los primeros 5 ensayos de adquisición y los primeros 5 ensayos de extinción. Muestre todos los cálculos usando la ecuación V_{t+1} = (1-α)V_t + αR_t.

b) Derive la solución analítica para V_t durante adquisición constante (R=1 siempre). Su solución debe ser de la forma V_t = f(t, α). Verifique que su solución coincide con los valores calculados en (a).

c) En equilibrio (t → ∞), ¿qué valor alcanza V durante adquisición? ¿Y durante extinción? Demuestre matemáticamente que estos son puntos de equilibrio (valores donde V_{t+1} = V_t).

d) Calcule cuántos ensayos se requieren para que V alcance 95% de su valor asintótico durante adquisición. Compare este número para α = 0.1, α = 0.3, y α = 0.5. ¿Qué patrón observa?

**7. Análisis del Filtro Exponencial**

La interpretación de filtro exponencial muestra que V_t es un promedio ponderado de reforzadores pasados con pesos que decaen exponencialmente.

a) Para α = 0.4, calcule los pesos asignados a los últimos 5 reforzadores: w_0 (más reciente), w_1, w_2, w_3, w_4. Use la fórmula w_i = α(1-α)^i. Verifique que Σw_i se aproxima a 1.

b) Calcule la "vida media" τ del filtro para α = 0.2, α = 0.4, y α = 0.6 usando τ = 0.693/α. Interprete: ¿cuántos ensayos atrás tiene un reforzador solo 50% del peso del reforzador actual?

c) Considere una secuencia de reforzadores: R = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]. Calcule V_{10} usando dos métodos: (i) iteración directa de V_{t+1} = (1-α)V_t + αR_t con V_0 = 0.5, α = 0.3, y (ii) la fórmula de promedio ponderado V_t = Σ[α(1-α)^i R_{t-i}]. Verifique que producen el mismo resultado.

d) En la fórmula de promedio ponderado, hay un término adicional (1-α)^t V_0 que representa la contribución del valor inicial. ¿Para qué valor de t este término se vuelve < 0.01 (esencialmente negligible)? Evalúe para α = 0.2 y α = 0.5.

**8. Reforzamiento Parcial y Probabilístico**

Un estímulo X predice refuerzo con probabilidad p = 0.6 (reforzamiento parcial).

a) En equilibrio, ¿qué valor de V espera que alcance el estímulo? Demuestre que V* = p independientemente del valor de α. (Pista: En equilibrio, el valor esperado de actualización debe ser cero: E[V_{t+1} - V_t] = 0).

b) Simule 50 ensayos con p = 0.6 y α = 0.3. Genere una secuencia aleatoria de 0s y 1s con probabilidad 0.6 de 1s (puede usar: R = [1,1,0,1,0,1,1,1,0,0,1,0,1,1,0,...]). Calcule V_t para cada ensayo y grafique V vs. t. ¿Observa que V converge cerca de 0.6?

c) La varianza de V en equilibrio depende de α y p. Intuitivamente, ¿esperaría mayor varianza con α grande o pequeño? ¿Y con p cercano a 0.5 o cercano a 1? Justifique sin cálculos formales.

d) Compare la velocidad de convergencia (ensayos hasta alcanzar 95% del valor asintótico) para dos condiciones: (i) reforzamiento continuo (p=1.0) con α = 0.3, versus (ii) reforzamiento parcial (p=0.6) con α = 0.3. ¿Cuál converge más rápido? ¿Por qué?

**9. De Media Simple a Media Exponencial**

Derive la equivalencia entre diferentes formas de actualización.

a) Demuestre algebraicamente que la media simple μ_n = (1/n)Σx_i puede expresarse como μ_n = μ_{n-1} + (1/n)(x_n - μ_{n-1}). Muestre todos los pasos de la derivación presentada en el capítulo.

b) La media simple usa α = 1/n (decrece con experiencia). La media exponencial usa α constante. Calcule V_t para ambos métodos usando la secuencia R = [1,1,0,1,0] con V_0 = 0:
   - Media simple: α_t = 1/t
   - Media exponencial: α = 0.4 (constante)
   Compare los valores finales V_5 para ambos métodos.

c) ¿Bajo qué condiciones es preferible una media simple (α decreciente) versus una media exponencial (α constante)? Considere: (i) ambiente estacionario sin cambios, (ii) ambiente con cambios ocasionales pero infrecuentes, (iii) ambiente altamente volátil con cambios constantes.

d) Proponga una "regla de actualización de α" que combine lo mejor de ambos mundos: empiece con α alto para aprendizaje rápido inicial, pero decrezca α gradualmente para estabilidad una vez que se ha acumulado experiencia. Especifique una función α_t = f(t) concreta.

### Ejercicios Aplicados

**10. Diseño de Intervención: Hábitos Problemáticos**

Una persona ha desarrollado el hábito de revisar redes sociales cada vez que se sienta a trabajar (R: revisar redes → Reforzador: contenido entretenido). Después de 200 repeticiones, V es alto.

a) Use el modelo para estimar cuántos ensayos de extinción (sentarse a trabajar SIN revisar redes) se requerirían para que V decaiga a 10% de su valor original. Asuma α = 0.2. Muestre sus cálculos.

b) En la práctica, la extinción pura (nunca revisar redes al sentarse) es difícil de mantener. Proponga un protocolo de "extinción gradual" donde la probabilidad de revisar redes decrezca gradualmente: p = 0.8 (semana 1), p = 0.6 (semana 2), p = 0.4 (semana 3), etc. ¿Cómo cambiaría esto la trayectoria de V comparado con extinción pura?

c) Algunos terapeutas proponen "sustitución de hábitos": reemplazar revisar redes con una actividad alternativa reforzante (ej. 2 min de meditación → calma). Use el modelo para explicar cómo esto podría facilitar la extinción del hábito original. ¿Qué suposiciones necesita hacer sobre competencia entre respuestas?

d) Desde la perspectiva de filtro exponencial, explique por qué la consistencia es crítica para extinguir hábitos. ¿Qué sucede si la persona "recae" ocasionalmente y revisa redes? Use el concepto de vida media del filtro en su explicación.

**11. Aplicación Clínica: Aversiones Alimentarias en Quimioterapia**

Un paciente de quimioterapia desarrolla aversión a su comida favorita (pasta) después de comerla antes de un tratamiento que causa náusea severa.

a) Modele la adquisición de la aversión. Asuma que antes del tratamiento, V_pasta = 0.8 (altamente positivo por años de experiencias previas). El tratamiento induce R = -1 (náusea). Use α = 0.6 (aversiones a sabores tienen α alto). ¿Qué valor alcanza V_pasta después de un solo ensayo? ¿Cuántos ensayos adicionales se requerirían para que V_pasta sea negativo?

b) Para extinguir la aversión, el paciente debe comer pasta sin experimentar náusea (R = 0). ¿Cuántos ensayos de extinción se requerirían para que V_pasta regrese a 0.5? Use la misma α = 0.6.

c) En la práctica, se recomienda espaciar la exposición a la comida varios días después del tratamiento, cuando la náusea ha pasado. Pero el modelo es "basado en ensayos"—no incluye efectos del tiempo entre ensayos. Proponga una modificación al modelo que incorpore decaimiento temporal: si pasan T días sin exposición, V decae hacia un valor neutral. Especifique la forma de esta función de decaimiento.

d) Algunos oncólogos sugieren que el paciente consuma un "sabor señuelo" (ej. caramelo de menta) justo antes de quimio, para que la aversión se asocie con el señuelo en lugar de comidas nutritivas importantes. Use los conceptos del Capítulo 8 (bloqueo) para explicar por qué esto funcionaría. ¿El modelo de Bush-Mosteller simple capturaría este efecto, o requeriría la extensión de Rescorla-Wagner?

**12. Caso de Aprendizaje de Máquinas: Recomendaciones Personalizadas**

Un sistema de recomendación de películas usa aprendizaje por refuerzo para predecir si al usuario le gustará una película. R = 1 si el usuario califica ≥4 estrellas, R = 0 si califica <4 estrellas.

a) El sistema tiene α = 0.1 fijo para todas las películas. Explique por qué esto es problemático: ¿qué diferencias esperaría entre el aprendizaje sobre preferencias estables (ej. "me gustan películas de ciencia ficción") versus preferencias volátiles (ej. "mi estado de ánimo actual")?

b) Proponga un algoritmo que ajuste α dinámicamente para cada usuario basándose en la consistencia de sus calificaciones pasadas. Si un usuario califica consistentemente ciencia ficción con 5 estrellas, ¿qué α debería usarse? ¿Y si un usuario califica aleatoriamente?

c) El sistema inicialmente no sabe nada sobre un nuevo usuario (V = 0.5 para todos los géneros). Después de 10 películas, el usuario ha calificado: [Sci-Fi: 5, 4, 5], [Romance: 2, 1, 2], [Acción: 3, 4, 3, 2]. Use α = 0.3 para calcular V_SciFi, V_Romance, y V_Acción después de estas 10 películas. Muestre cálculos para al menos un género.

d) El dilema exploración-explotación: el sistema debe balancear recomendar géneros con V alto (explotación) versus probar géneros con V incierto (exploración). Proponga una regla de selección que use los valores V pero que ocasionalmente explore. (Pista: regla ε-greedy o softmax).

**13. Análisis de Datos Reales: Curvas de Extinción**

Se le proporcionan datos de extinción de una paloma entrenada a picotear una tecla. Durante adquisición (100 ensayos), cada picoteo fue reforzado. Durante extinción, se registró el número de picoteos en bloques de 10 ensayos:

Bloque: 1,  2,  3,  4,  5,  6,  7,  8,  9,  10
Picoteos: 85, 72, 58, 49, 38, 32, 25, 22, 18, 15

a) Ajuste el modelo de Bush-Mosteller a estos datos de extinción. Asuma que V al inicio de extinción = 1.0, y que el número de picoteos es proporcional a V (Picoteos ≈ 100×V). Estime α usando los primeros 3 bloques. Muestre sus cálculos.

b) Use el α estimado para predecir el número de picoteos en bloques 4-10. Calcule el error de predicción para cada bloque (predicción - dato real). ¿El modelo se ajusta bien?

c) Note que el decaimiento no es perfectamente exponencial—hay más picoteos de lo esperado en bloques tardíos (8-10). Proponga dos explicaciones teóricas: (i) α cambia durante extinción, (ii) hay conductas "espontáneas" no reforzadas que mantienen algo de V. ¿Cómo distinguiría entre estas hipótesis?

d) Si re-entrenara a la misma paloma después de extinción completa (readquisición), ¿esperaría que el aprendizaje fuera más rápido que la adquisición original? El modelo simple de Bush-Mosteller predice que no (V regresó a 0). Pero empíricamente, la readquisición es más rápida. ¿Qué procesos adicionales no capturados por el modelo podrían explicar esto?

---

**Fin del Capítulo 10**
