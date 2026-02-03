# #Aprendizaje por Refuerzo y Filtros
###Arturo Bouzas
####ACA II 2020
###Sistemas Dinámicos
El estudio del aprendizaje, la asignación de crédito, es una instancia de un sistema dinámico. Un sistema cuyo valor cambia a lo largo del tiempo, como una función de sus valores anteriores. 
Cuando el tiempo es discreto, encontramos muchos ejemplos de sistemas dinámicos, crecimiento económico, cambios en las frecuencias de genes en una población, propagación de rumores y actualmente una pandemia. En estos sistemas, nos interesa determinar su trayectoria a lo largo del tiempo, determinar si tiene un equilibrio y encontrar cuál es ese. Por ejemplo, en el caso de una epidemia, como la del covid 9, deseamos describir los cambios en contagios cada día transcurrido y sí tiene un equilibrio. 
###Ecuaciones en Diferencia
Las ecuaciones en diferencia representan el comportamiento dinámico y son ecuaciones recursivas, que  operan en cada momento en el tiempo $t$.
Considere el caso más sencillo, en que el valor cada momento en el tiempo es simplemente el valor inicial mas 1.
$$Y_t= Y_{t-1} +1$$
si el primer valor de $Y(0) = 0$,

 $$Y_1 = Y_0+1 = 1$$
 $$Y_2 = Y_1+1 = 2$$
 $$Y_3 = Y_2+1 = 3$$
    $$.$$
    $$.$$
    
El crecimiento geométrico de una epidemia proporciona un ejemplo ya interesante:
$$Y_t= aY_{t-1}$$

para valores de $a$ mayores a 1, 
$Y_0 =1$, $Y_1=a$, $Y_2=a^2$, $Y_3=a^3$
La solución general es $$Y_t= a^t$$

###Predicción y Filtros
Vimos que aprendizaje por refuerzo es un proceso de actualización de las predicciones que hace un organismo, que resultan de comparar el resultado obtenido con la predicción.
$$V_{t+1}= V_t + \alpha \delta$$
donde 
$$\delta= (R-V_t)$$
Aceptando que aprendizaje por refuerzo representa una tarea de predicción a partir de las experiencias con un conjunto de observaciones, podemos preguntarnos acerca de posibles reglas para hacer la predicción.
En una serie de encuentros en el tiempo, la regla más sencilla para predecir la siguiente observación es el promedio de las observaciones hasta ese momento. Considere el caso del número de contagios de covid en nuestro país.Para LG y para nosotros es importante predecir el número de contagios que habrá mañana y cuál es la tendencia  que muestra. 
La estrategia más sencilla sería obtener el promedio de todos los contagios a partir del primero de marzo de este año.
Sumamos todos los casos diarios y los dividimos por el número de días observados (del primero de marzo hasta hoy).
$$\mu_n = \frac {1}{n}\sum_{i=1}^ {t} x_i$$
La estrategia tiene dos problemas:
1. Le asigna un mismo peso a todos los días y
2. No toma en cuenta el ruido en los datos.

###Medias (medianas) corridas
Para resolver el problema del ruido (los fines de semana se trabaja menos en la recopilación de los datos), necesitamos un filtro.
El propósito del filtro es alisar (suavizar) los datos. Se les conoce como media o mediana corrida. Consiste en seleccionar una ventana de cierto número de observaciones, obtener su media o mediana y substituir ese número por el centro de la ventana. La ventana se desliza una observación a la derecha y se repite la operación de obtener su media o mediana. 
Considere los siguientes números de contagios diarios en miles
25 28 22 30 27 15 20 100 27 32 39 40 18 22 44 30 35
Usemos una mediana corrida de tres. Obtenemos la mediana de los tres primeros números y nos movemos un día a la derecha.
25 28 27 27 20 20 27 32 39 39 22 22 30 30
noten que el primer y último número de la serie no pertenecen a una ventana de tres y desaparecen. El valor raro de 100 desaparece.
Mediana corrida de 5
27 27 22 27 27 32 33 32 32 39 30 30.
La técnica es útil para alisar datos (experiencias) y ver tendencias.
Sin embargo tiene  dos problemas, computacionalmente es costoso y le da el mismo peso a todos los eventos independientemente de que tan atrás hayan ocurrido. En muchas circunstancias pareciera más razonable darle un menor peso a los acontecimientos mas alejados del presente. 
###Media Exponencial Corrida (MEC)
Una forma de ver el problema que enfrenta un organismo para asignar valor a una respuesta, es considerar el caso más sencillo. Considere una máquina tragamonedas, conocidas en ingles como "one arm bandit". En esa máquina cada respuesta es reforzada de acuerdo a una probabilidad constante (en Psicología los llamamos programas de refuerzo variable).  

![-w1103](media/16028706424735/16028949027703.jpg)

Considere una secuencia de resultados probabilisticos para una respuesta:
1100010011100011001101001111
Para predecir el siguiente resultado se puede computar la media de todos los resultados obtenidos
$$V_t = \frac {1}{t}\sum_{i=1}^ {t} r_i$$
Para pasar de esta forma de expresar la media a la ecuación de reducción de error, presento una forma alternativa de expresar la media (ver Finch). 
$$\mu_n = \frac {1}{n}\sum_{i=1}^ {n} x_i$$ 
1. a la $\sum x_i$ la vamos a descomponer en dos términos, $x_n$ y $\sum_{i=1}^ {n-1} x_i$
$$ = \frac {1}{n}(x_n+\sum_{i=1}^ {n-1} x_i)$$
1. Noten que si dividimos el segundo término entre el numero de observaciones  hasta antes de $n$, $(n-1)$, tendremos  la media $\mu_{n-1}$
$$\mu_{n-1} = \frac {1}{n-1}\sum_{i=1}^ {n-1} x_i$$
2. multiplicando por $(n-1)$ ahora podemos substituir la segunda sumatoria 
 $$(n-1)\mu_{n-1} = \sum_{i=1}^ {n-1} x_i$$
3. regresando a 1. podemos usar $(n-1)\mu_{n-1}$
$$ \mu_n= \frac {1}{n}(x_n+(n-1)\mu_{n-1})$$
4. Expandimos:
$$ \mu_n= \frac {1}{n}(x_n+n\mu_{n-1}-\mu_{n-1})$$
5. Reacomodando términos obtenemos la ecuación:
$$\mu_n = \mu_{n-1}+\frac {1}{n}(x_n - \mu_{n-1})$$
Noten que es la misma ecuación de la media simple con iguales pesos de ponderación $n$ y nos recuerda en forma a la ecuación de reducción de error.

###Diferentes pesos de ponderación como función del tiempo.
En un promedio ponderado, se suma el producto de cada observación es multiplicada por un peso diferente y se divide por la suma de todos los pesos. (recuerde que en la media aritmética, cada observación es multiplicada por 1.
Media Corrida Ponderada (MCP)
$$MCP= \frac {\sum_{i=1}^{n}w_ix_i}{\sum_{i=1}^{n}w_i}$$
Dejamos que para cada observación, el peso de ponderación sea la razón del peso más reciente dividido por total de pesos.
$$W_n= \sum_{í=1}^{n}w_i$$
$$peso de ponderación = \frac{w_i}{W_n}$$

###Q learning
Para distinguir entre aprendizaje acerca del valor de un estímulo y de una respuesta, cambiaremos $V$ por $Q$ para denotar el valor de una respuesta. La ecuación es la misma:
$$Q_t = \frac {1}{t}\sum_{i=1}^ {t} r_i$$
Para reducir los recuersos necesarios para computar la media desde el primer evento, usamos la estrategia presentada arriba y expresamos la ecuación para el momento inmediatamente anterior:
$$Q_{t-1 }= \frac {1}{t-1}\sum_{i=1}^ {t-1} r_i$$
expandemos las dos ecuaciones:

$Q_t= \frac{1}{t}(r_1+r_2+r_3...r_{t-1}+r_t)$

$Q_{t-1}= \frac{1}{t-1}(r_1+r_2+r_3...r_{t-1})$

Multiplicamos la última ecuación por $(t-1)$

$(t-1)Q_{t-1}= r_1+r_2+r_3...r_{t-1}$

Puede ver que las dos ecuaciones comparten todos los términos hasta la penúltima observación $r_n-1)$. Ya tenemos una expresión para estas observaciones comunes: $(t-1)Q_{t-1}$

Así que substituyendo
$$Q_t=\frac{1}{t}((t-1)Q_{t-1} +r_t))$$
y arreglando términos
$$Q_t= Q_{t-1} + \frac{1}{t}(r_t-Q_{t-1})$$
Justo la regla delta.
En conclusión, el modelo de aprendizaje por refuerzo puede verse de tres formas diferentes:
1. Un modelo de un integrador con fuga de carga descarga
$$Q_t= (1-a)Q_{t-1} + ar_t$$
esta es la interpretación original, en la cual un refuerzo incrementa la "fuerza de una respuesta" y decrece con cada ocasión en la cual la respuesta no es seguida por un refuerzo.
2. Un modelo de reducción de error de predicción 
$$Q_t= Q_{t-1} + \alpha(r_t-Q_{t-1})$$
Es hoy en día la interpretación dominante, que implica que el aprendizaje es el resultado de un proceso de ascenso de colina en la dirección de el menor error de prediccióm
3. Un modelo de un filtro de media exponencial corrida. con $\frac {w_{n,n}}{W} = \alpha$
$$Q_t= (1-a)Q_{t-1} + ar_t$$
La tercera interpretación implica que el valor de la respuesta sigue al promedio de refuerzo que produce, con una ponderación que le atribuya más peso a los refuerzos más recientes.

