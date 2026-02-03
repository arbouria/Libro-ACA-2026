# ---
title: "Modelo de Aprendizaje por Refuerzo"
author: "Arturo Bouzas" 
format: html
---
Como un resultado de la selección natural, los agentes biológicos son sistemas con mecanismos que les permiten detectar, predecir y controlar los sucesos biológicamente importantes (SBI). Recordemos que los SBI son sucesos con valor hedónico, también conocidos como refuerzos, los cuales incrementan el éxito reproductivo diferencial de los organismos. Para ejecutar estas funciones de detección, predicción y control de SBI los organismos necesitan hacer contacto con la estructura causal del entorno: estructura a la cual designamos bajo el término de *propiedades estadísticas del entorno*. 

Una parte de la estructura estadística de los SBI consiste de estímulos que se despliegan en el tiempo y en el espacio, los cuales en algunas ocasiones aparecen solos, mientras que en otras instancias aparecen seguidos (contiguos) de un refuerzo. Hay tiempos sin nubes y otros con nubes, estos últimos pueden ser seguidos o no de lluvia. La tarea para el organismo es determinar si existe una relación causal entre las nubes y la lluvia. Una segunda parte de la estructura estadística del entorno consiste del hecho de que, con relación al despliegue de respuestas de los organismos en el tiempo y en el espacio, algunas ocasiones estas respuestas van seguidas de un refuerzo y en otras ocasiones no. Hay veces en las que ustedes le dicen “hola” a una persona y otras en las que no. Después del “hola” ustedes pueden recibir, o no, otro “hola” de regreso. Los protocolos de condicionamiento clásico e instrumental definen, como una primera aproximación, las estructuras causales más simples que se estudiaron en buena parte del siglo XX. En los dos capítulos anteriores, resumimos la literatura empírica acerca del papel de la contigüidad en la asignación de crédito a estímulos y respuestas que permiten *predecir y controlar* los refuerzos. Presentamos evidencia que muestra que aunque la contigüidad es importante, esta no es ni necesaria, ni suficiente para la asignación de crédito.  

Para dar cuenta de los resultados empíricos presentados en los capítulos anteriores, en la segunda mitad del siglo XX se consolidó un modelo matemático, conocido como *Aprendizaje por Refuerzo*, junto con varias modificaciones del mismo. El propósito de este capítulo es presentar estos modelos y su desarrollo como respuesta a la evidencia sobre el papel de la contigüidad.


. 

## Curvas de Aprendizaje

El aprendizaje es un proceso dinámico, que describe los cambios en el comportamiento como una función de la experiencia de los organismos. Desde finales del siglo XIX se han obtenido “curvas de Aprendizaje” que describen cambios en alguna medida de ejecución de los organismos como una función de las ocasiones en las que los estímulos que encaran o las respuestas que despliegan van seguidos de un refuerzo. 

Como ilustración, presentamos dos ejemplos, el primero es la curva de adquisición y extinción de la frecuencia del reflejo de parpadeo, en un protocolo de condicionamiento clásico con humanos. Las curvas representan diferentes intensidades del soplo al ojo. (Parssey, 1948)

IMAGEN

Un segundo ejemplo es la curva de adquisición de la velocidad de tocar una palanca en un protocolo de condicionamiento instrumental con ratas (Ramond, 1954). Las dos curvas representan los datos obtenidos con diferentes niveles de privación.

IMAGEN

La siguiente curva de adquisición idealizada, captura los datos de adquisición presentados en las dos figuras anteriores. Podemos ver que es una curva negativamente acelerada de ganancias decrecientes, esto es, el impacto de que un refuerzo siga a una respuesta se va reduciendo conforme se acumulan las ocasiones en las que una respuesta va seguida de un refuerzo.

IMAGEN

Nota. Una alternativa teórica supone que el aprendizaje no es un proceso gradual, sino uno de cambio abrupto. Si este fuese el caso, las curvas de adquisición de crecimiento gradual decreciente podrían ser un artefacto de promediar la ejecución de animales con cambios *no* continuos en el aprendizaje. Considere el caso de un grupo de animales cuya ejecución es promediada. Uno de los animales empieza a responder al ensayo 10, otro al 20, otro al 30, otro al 40 y así hasta un animal que responde al ensayo 80: al promediar estos datos, la curva de aprendizaje aparecerá como una curva continua. Por esta razón, Skinner, Estes, Spence y más recientemente Gallistel argumentan en favor de analizar los datos de sujetos individuales y, preferentemente, registros acumulativos en lugar de los datos promediados. En ese mismo sentido, los modelos que presentaremos a continuación resultan válidos cuando los datos analizados provienen de sujetos individuales. 

Los modelos de refuerzo modelan la forma de las curvas de adquisición obtenidas empíricamente. El modelo de refuerzo más general es un sistema dinámico que describe los cambios en el valor de un estímulo y/o respuesta a lo largo del tiempo, como una función del número de ocasiones en las que un estímulo o una respuesta van seguidas de un refuerzo.

Pasen al simulador de ecuaciones en diferencia para entender los modelos dinámicos discretos.  

## Modelo de Refuerzo 

Los modelos de refuerzo le asignan un número a cada estímulo y/o respuesta: esta magnitud representa la calidad del estímulo/respuesta como predictor de un refuerzo. A lo largo del siglo XX, a esta magnitud se le conoció como fuerza del reflejo, fuerza del hábito, fuerza asociativa del estímulo y fuerza de la respuesta. Para nuestros propósitos el número refleja el *valor* predictivo de un estímulo o de una respuesta y simplemente le llamaremos el valor V del estímulo i, o el valor Q de la respuesta i.

El modelo de refuerzo propone que después de cada presentación de un estímulo o la emisión de una respuesta, su valor se actualiza como una función de si este va seguido o no de un refuerzo. Es importante señalar que el modelo asume que la actualización del valor de un estímulo o una respuesta solo ocurre en las ocasiones en las que estos se presentan. El valor predictivo de un tono solo se actualiza cuando el tono se presenta y no en su ausencia. Esto implica que el mero paso del tiempo sin el tono o la presentación de otros estímulos no alteran el valor del tono. Por esta razón, a estos modelos se les llama también modelos basados en ensayos. Esto es, la variable importante que determina el valor predictivo (la asignación de crédito) es el número de ocasiones en las que un estímulo o una respuesta son seguidos de un reforzador. Mientras mayor es este número, mayor será el valor adquirido por el estímulo o la respuesta. De forma complementaria, el valor de estos estímulos o respuestas decrementa cuando estos se presentan sin ser seguidos por el reforzador. 

En 1950, Bush y Mosteller propusieron una versión matemática del modelo de aprendizaje por refuerzo esbozado en el párrafo anterior. Esta versión sigue siendo la base que sustenta varios de los modelos más recientes, tanto en la psicología como en el aprendizaje de máquinas. 

La estructura matemática de los modelos de refuerzo tiene diferentes interpretaciones teóricas. Nosotros consideraremos dos:

1. Un proceso de carga - descarga y
2. Un proceso de reducción del error 
	 
### Proceso de carga - descarga

Los modelos de refuerzo son una propuesta de solución computacional a la asignación de crédito. La solución incluye dos pasos: el primero es la reducción del tamaño inicial del espacio de candidatos para incluir únicamente sucesos que son contiguos, similares, novedosos y evolutivamente relevantes con relación a los SBI. El segundo es un mecanismo que permita ir reduciendo, a través de la experiencia, el espacio de candidatos hasta terminar con uno solo. El modelo de refuerzo canónico combina un algoritmo de ascenso de colina con el sesgo de contigüidad. Bush y Mosteller (1951) formalizaron esta clase de modelos que, en diferentes variantes, han dominado la literatura teórica y experimental en el estudio del aprendizaje a partir de la década de los 70s del siglo pasado.

Como ya se dijo antes, la forma más literal de interpretar el modelo de refuerzo es como un proceso en el cual: cada refuerzo incrementa (carga, fortalece) el valor del estímulo / respuesta que le antecede y cada ocurrencia del estímulo / respuesta sin ser acompañado de un refuerzo decrementa (descarga) su valor. Este es un proceso en el que la variable $V$ se actualiza con cada ocurrencia del estímulo / respuesta como una función que varía dependiendo de si el estímulo/respuesta va seguida o no de un refuerzo. La carga de la batería de su celular es un ejemplo muy cercano a su vida cotidiana que ejemplifica el proceso descrito. Para que su celular funcione, ustedes tienen que conectarlo a una toma de corriente. Mientras está conectado, la carga de la batería se va actualizando hasta llegar a un punto máximo. Al usarlo sin tenerlo conectado, la batería se va descargando como una función del uso del celular sin una carga adicional.

Veamos cómo se aplica este modelo en el caso de un protocolo estándar de condicionamiento clásico: en este contexto, se observa un estímulo/respuesta candidato a la asignación de crédito y a cada presentación de él se le conoce como un ensayo. Cada ocurrencia de un ensayo puede estar acompañado o no de un SBI.  Consideremos que $Vx$ represente el valor predictivo de un estímulo $x$ . Nos interesa la dinámica del cambio en $Vx$ conforme un organismo experimenta ensayos en los que un estímulo condicionado $x$ va seguido de un refuerzo. Para facilitar la aplicación del modelo, supondremos que el tiempo es discreto y el subíndice $t$ representa el momento en que se presenta el estímulo $x$. La variable $Vx_t+1$ es el valor actualizado del estímulo $x$ en el siguiente ensayo $t+1$. La variable $R$ representa si se presentó o no un refuerzo después del estímulo $x$ . $R$ puede tener solo dos valores, uno si el refuerzo se presenta después del estímulo $x$ o cero si el estímulo $x$ se presenta sin ser seguido por el refuerzo.


Vamos a asumir que $Vx_t+1$ depende sólo de dos factores:
1. su valor acumulado hasta el ensayo inmediatamente anterior $Vx_t$
2. el valor de $R_t$ en el ensayo actual

$$
Vx_{t+1} = Vx_t + R
$$

3. La expresión anterior supone que el efecto del valor de V en el ensayo anterior tiene el mismo peso que el reforzador presentado o no en el momento actual. Nosotros deseamos que la ecuación capture la importancia relativa de las dos variables. Para ello, supondremos que el impacto de esas dos variables es una suma ponderada, donde el parámetro $a$ representa el peso de ponderación asignado a cada uno de los dos factores. Si el valor de $a$ esta entre cero y uno, los parámetros asociados con cada factor serán $a$ y $(1-a)$.

$$
Vx_{t+1} = (1-a)Vx_t + aR_t, \hspace{0.1cm} \text{ donde: } 0 < a < 1.
$$

La ecuación anterior es una ecuación recurrente, en la que en cada iteración (presentación del estímulo $x$) hay siempre un Vx viejo y un Vx nuevo. La ecuación describe la actualización de $Vx$ de ensayo a ensayo, como una función del valor de $Vx$ acumulado hasta el ensayo anterior y la presentación o ausencia del SBI. Vx_t es la integración, el acumulado, de todas las experiencias previas con el refuerzo. En cada ensayo, la Vx nueva del ensayo anterior se convierte en la Vx vieja del presente ensayo, contribuyendo a generar una nueva Vx. 
Pase al simulador x para revisar ecuaciones recurrentes.
 
El parámetro $a$, que multiplica al refuerzo, determina la velocidad del aprendizaje: mientras mayor sea su valor, más rápido será el aprendizaje. Una forma de entender el papel de $a$, es considerarlo como el parámetro que especifica la importancia de la experiencia acumulada hasta el momento (el valor del pasado), relativa a la ocurrencia o no de un refuerzo (el valor del presente). Valores cercanos a cero sugieren que la experiencia acumulada es más importante que una nueva experiencia con un refuerzo, resultando en poco aprendizaje, mientras que valores cercanos a uno sugieren que la presentación del refuerzo es más importante que la experiencia acumulada hasta ese momento, resultando en un rápido aprendizaje. Consideren una interacción de larga duración con una amistad que ha resultado en un valor alto para ustedes asociado con esa relación. Nos podemos preguntar cuál es el impacto de que una mañana esa amistad no los salude. Si el parámetro $a$ fuese cercano a cero, el no saludo no modificaría sustancialmente el valor V de la amistad, mientras que si el valor de $a$ fuese cercano a uno, a pesar de los años de experiencias positivas con esa amistad, su impacto en el valor V sería más significativo. 

Las siguientes figuras muestran los resultados, ensayo a ensayo, de una simulación con diferentes valores del parámetro $a$.

IMAGENES


### Reducción del error de predicción como motor del aprendizaje 

El reacomodo de los términos de la ecuación de carga -  descarga permite una interpretación alternativa del modelo de aprendizaje por refuerzo: esta vez en términos de un mecanismo de reducción en el error de predicción. Estos modelos representan hoy la versión dominante en la psicología del aprendizaje y las neurociencias. 

Arreglando los términos de la ecuación del integrador con fuga:

$$
V_{t+1} = (1-a)V_t + aR_t
$$

$$
V_{t+1} = V_t - aV_t + aR_t
$$ 

$$
V_{t+1} = V_t + a (R_t -V_t)
$$

Restándole $V_t$ a ambos lados de la ecuación anterior, dejando que $\Delta Vx = Vx_t+1 – Vx_t$ entonces el cambio de ensayo a ensayo es descrito, agrupando términos:

$$
\Delta Vx = V_t + a (R_t -V_t) - V_t
$$

$$
\Delta Vx = a(R_t – Vx_t)
$$

Esta segunda forma de la ecuación, enfatiza la magnitud del cambio momento a momento, en lugar del valor del estímulo momento a momento. 

En cualquiera de las dos formas de presentar la ecuación del integrador, el valor $V$ es una función de la diferencia entre el refuerzo obtenido y el valor del estímulo en el tiempo $t$. A esta diferencia dentro del paréntesis se le conoce como el error de predicción: la diferencia entre la $R$ que se obtiene y lo que se esperaba obtener, $V$. Cuando esta diferencia es igual a cero, no habrá cambios en el valor de $V$. Es por esta forma de la ecuación que estamos llamando a $V_t$ el valor predictivo de la respuesta. El parámetro $a$, entre $0$ y $1$, sigue representando la velocidad del aprendizaje, en este caso, la importancia del error de predicción. 

En la literatura contemporánea, a la ecuación anterior se le conoce como regla delta.

$$
V_{t+1} = V_t + a \Delta Vx
$$

donde $\delta = (\lambda_t - Vx_t)$ es el error de predicción, es decir, el motor del aprendizaje. Bajo el formato que enfatiza la magnitud del cambio, delta se incorpora a la ecuación de la siguiente forma:

$$
\Delta Vx = a \delta
$$

