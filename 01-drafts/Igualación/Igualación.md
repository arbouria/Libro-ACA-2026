# # ---
title: "Elección Recurrente: Igualación"
author: "Arturo Bouzas"
format: html
---
Consideren las siguientes situaciones: a un agente se le presentan dos bolsas, y se le **informa** que una contiene $100,000 y la otra $100 a la vez que se le pide que opte por una de ellas; en un segundo escenario, al agente se le lleva a un restaurante que no volverá a visitar y se le pide elegir entre uno u otro platillo. En ambos ejemplos, la elección puede hacerse exclusivamente a partir del valor de las opciones en el momento de la elección, y anteriormente hemos visto que el agente selecciona la opción con mayor valor en el momento de decisión. Estas situaciones de elección son instancias de sistemas abiertos sin retroalimentación y siguiendo a Gallistel (fecha), les llamamos protocolos de *optar*.  En las últimas décadas, la mayoría de la investigación psicológica con participantes humanos ha utilizado este tipo de protocolo. 


Consideren ahora un experimento similar: en lugar de informar al agente acerca del contenido de las bolsas en un inicio, a este se le presentan las opciones como bolsas cerradas, y a través de múltiples iteraciones, el agente tiene que explorar y **aprender** acerca de los montos de dinero de las distintas bolsas o de la calidad de las distintas opciones ofrecidas por el restaurante. La presentación recurrente de las oportunidades de elección crea nuevos problemas de adaptación para el agente. Como vimos en las notas anteriores, el agente debe resolver el dilema de exploración - explotación y debe determinar si las consecuencias de las opciones cambian como una función de las elecciones y el paso del tiempo, o si estas son fijas e independientes de las elecciones y del tiempo. En un ejemplo no ya de una elección entre varios platillos de un restaurante sino de una elección entre acudir a uno de varios restaurantes, el agente debe visitar los distintos locales un buen número de veces antes de tomar la decisión de pasar a explotar uno. Sin embargo, aún tras haber estimado la opción con mayor valor y haber comenzado a explotar una opción elegida, el agente debe mantener cierta flexibilidad para modificar su elección, en aras de poder determinar si la calidad de los restaurantes varía aleatoriamente con el paso del tiempo (debido a factores como los cambios de cocinero, por ejemplo). En estos casos, la regla de elegir la opción que instantáneamente tiene más valor no es la que a largo plazo proporciona la mayor cantidad de refuerzos. En los experimentos con estos protocolos observamos una regla de respuesta probabilística.

## Elección Recurrente

Fuera del laboratorio, lo común para los humanos y para muchas otras especies son situaciones en las cuales los individuos pueden elegir entre dos o más acciones o parcelas de forma repetida y continua, y en las cuales las elecciones alteran las opciones futuras de refuerzo. Estos problemas de adaptación son ejemplos de sistemas de retroalimentación cerrados y, siguiendo a Gallistel, les llamamos *problemas de asignación* de respuestas, tiempo o esfuerzo. Un estudiante a lo largo del día va asignando su tiempo a diferentes actividades: desayunar, transportarse, pasar tiempo en el salón de clases, estudiar en la biblioteca, conversar con amistades, ver a su pareja, ejercitarse. Al final del día, habrá una distribución de tiempos asignados a las diferentes actividades. Resulta importante considerar que cada una de estas actividades es en sí otro espacio de posibles acciones a las que se les puede dedicar tiempo. Por ejemplo, cuando están en el salón de clases, pueden atender lo que presenta el profesor o pueden ver las noticias en su celular, mandar un WA o fantasear. De esta forma, podemos estudiar problemas de asignación a diferentes escalas temporales, pero todas bajo el mismo esquema.  

Un ejemplo adicional lo proporciona el forrajeo de una abeja que enfrenta dos diferentes parcelas con flores con polen. En este entorno, mientras más tiempo pasa la abeja visitando las flores de una de las parcelas, la disponibilidad del polen dentro de la misma va disminuyendo; al mismo tiempo, las flores en la otra parcela siguen llenas de polen. La abeja enfrenta dos problemas de adaptación: el primero es decidir cuánto tiempo agregado dedicarle a cada una de las dos parcelas como una función de la distribución de flores con alimento en cada una de las parcelas. Normalmente, en el contexto de asignación, la regla es distribuir el comportamiento a lo largo del tiempo de una forma que produzca la mayor ganancia posible. El segundo problema de adaptación es la decisión de cuándo salirse de una de las parcelas para visitar la otra. En estas notas, nos centraremos en el estudio del primer problema de adaptación: la distribución de respuestas y tiempos. 

La forma más sencilla de estudiar experimentalmente protocolos de elección recurrente se desarrolló en el laboratorio de Skinner y se conoce como *programas de refuerzo concurrentes*. El protocolo consiste en presentarle a un organismo dos o más opciones de respuesta -teclas iluminadas en el caso de las palomas- que se encuentran disponibles todo el tiempo y que siguen programas individuales e independientes de refuerzo. (Figura). En estas notas, revisaremos los resultados obtenidos en el estado de equilibrio, una vez que los agentes han aprendido acerca de las consecuencias de cada opción de respuesta. La variable que se estudia es la distribución de respuestas o tiempos asignados.

$$
\frac{R_1} {(R_1 +R_2)}
$$


imagen


En los estudios que reportamos, el animal es expuesto a un par de programas de refuerzo dentro de sesiones diarias hasta que la distribución de respuestas a las distintas opciones disponibles se vuelve estable y deja de cambiar día con día. Esto toma entre 30 y 45 días. Esta rutina se repite para todos los pares de programas que se están estudiando. De cada par, se usan para el análisis los últimos cinco días en los que las elecciones son estables.


## La Ley de Igualación

En 1961, Richard Herrnstein (ver foto)

imagen

reportó los resultados del primer estudio con programas concurrentes, en el que la respuesta de picar una de dos teclas era reforzada de acuerdo a un programa de intervalo variable. Recuerden que en estos programas el refuerzo se presenta tras la primera respuesta después de que haya transcurrido un tiempo aleatorio desde el último refuerzo. Un detalle muy importante que debe tenerse presente bajo este tipo de programa es que una vez que un refuerzo está disponible, la oportunidad de obtenerlo se retiene hasta que el animal responde a esa opción. 

Herrnstein encontró que en éstos programas la tasa relativa de respuestas (su proporción) iguala la tasa relativa de reforzadores obtenidos:

$$
\frac {R_1} {(R_1 + R_2)} = \frac {r_1} {(r_1 + r_2)}
$$

El resultado es muy robusto y se ha reportado en un sinnúmero de especies. A esta relación entre tasas relativas de respuesta y refuerzo se le conoce como la *ley de igualación* y en la última década del siglo pasado fue la ley más citada en la literatura psicológica. En la siguiente figura pueden verse los resultados de tres palomas: cada punto representa los datos de los últimos cinco días para cada par de valores de los programas de intervalo variable. La proporción de respuestas (tasas relativas) va de cero a uno. (Figura). 

imagen

Igualación sería un resultado trivial, si por cada refuerzo hubiese solo una respuesta, sin embargo, el patrón de igualación en los refuerzos también se puede obtener con un rango muy amplio de tasas relativas de respuesta que van más allá de la tasa específica del patrón de igualación.

 Una forma más directa de estudiar la relación entre patrones de respuesta y patrones de refuerzo en protocolos de elección recurrente, es estudiando el **tiempo** asignado por los organismos a las diferentes opciones de refuerzo, en lugar de estudiar el número de respuestas discretas asignadas a las distintas opciones. Desde este enfoque, Rachlin y Baum estudiaron el comportamiento de las palomas: para ello, emplearon un espacio rectangular con un piso conectado a interruptores que permite medir el tiempo que una paloma pasa en cada lado del espacio rectangular. En cada uno de los dos extremos del espacio experimental había un comedero que asignaba comida de acuerdo a programas independientes de refuerzo de intervalo variable. En este experimento también se encontró que el tiempo relativo asignado por el organismo a un lugar iguala el refuerzo relativo obtenido en dicho lugar.

$$
\frac {T_1} {(T_1 + T_2)} = \frac {r_1} {(r_1 + r_2)}
$$

### Desviaciones de Igualación

La igualación de las tasas relativas de respuesta al valor de las tasas relativas de refuerzo es un fenómeno muy robusto cuando ambas opciones de respuesta son reforzadas de acuerdo a programas de intervalo variable, sin embargo, se han encontrado desviaciones respecto al patrón de igualación cuando uno de los programas de refuerzo se cambio a otra regla, o cuando se establecen distintos  tipos de reforzadores para las dos respuestas. Baum () reconoció dos tipos de desviaciones de igualación: 
Introducir el ejemplo de “ver Salir a alguien con una cantidad de frijoles de diferente tipo”. ¿Es el resultado de preferencias o de precios?

1. *Sesgos*. Si en una visita al supermercado les ofrecen probar, sin ningún costo, frijoles negros o bayos, algunos de Uds. preferirán la prueba de los frijoles negros. Dada esa preferencia, si compran frijoles y ambos tienen el mismo precio, comprarán los frijoles negros. Sin embargo, qué frijoles deciden comprar depende de la diferencia en su precio modelada por su preferencia. Cuando los reforzadores para las dos respuestas son diferentes, por ejemplo, cuando una de las dos variedades de frijoles negros o bayos les brinda mayor satisfacción debido a su sabor particular, es posible que exista una preferencia por uno de ellos: esta preferencia tendrá un impacto sobre cada combinación de razones de refuerzo. Cuando esta razón es igual pero todavía se presentan diferencias en la tasa relativa de refuerzo, esta diferencia es un indicador del sesgo del organismo en favor de uno de los reforzadores. Los resultados se verían como los de la figura x: en ella, la tasa relativa de respuesta se aleja de 0.5, aún cuando la tasa relativa de refuerzo es igual para las dos opciones. 

imagen

2. *Sensibilidad*. En una misma visita al supermercado, un mismo producto que desean comprar es ofrecido por dos marcas distintas a precios diferentes: uno cuesta $11.00 y el otro $5.50. La diferencia en precio es de 2 a 1, sin embargo, los valores numéricos son difíciles de discriminar y para algunos de Uds. esta diferencia será percibida como de 3 a 1, mientras que para otros, la diferencia se percibirá como de 1.5 a 1. Sensibilidad es una segunda desviación de igualación, que ocurre cuando los organismos no son linealmente sensibles a la diferencia entre las tasas de refuerzo. Esto puede deberse a distinciones en la importancia de las diferencias en el valor de las opciones o a la dificultad para discriminar entre ellas. La figura x muestra como se vería la relación entre tasas relativas de respuesta y de refuerzo bajo distintos valores de sensibilidad. Cuando la tasa relativa de respuesta no es muy sensible a las tasas de refuerzo para cada respuesta, observamos valores cercanos a la indiferencia (panel de la izquierda en la figura) y a este resultado se le conoce como sub igualación. Cuando la tasa relativa de respuestas sobrevalora las diferencias en las tasas de respuesta, observamos que se prefiere mayoritariamente la mejor opción (panel derecho en la figura) y a este fenómeno se le conoce como sobre-igualación. 

En resumen, el sesgo hace referencia a la preferencia del organismo por una de las opciones, la cual tiene un efecto multiplicativo al de la tasa de ocurrencia de los reforzadores para determinar las tasas de respuesta. El otro factor de desviación respecto a igualación es la sensibilidad del agente ante las diferencias en las tasas de ocurrencia de los refuerzos de las distintas opciones. Vamos a asumir que el sesgo y la sensibilidad varían independientemente el uno del otro.

imagen
 
### Ley generalizada de Igualación

Para modelar el sesgo y la sensibilidad, Baum propuso una extensión de la ley de igualación que se conoce como la *Ley Generalizada de Igualación* y que captura las dos clases de desviaciones revisadas en la sección anterior.
Primero propuso expresar la ley en términos de razones entre las distintas respuestas y los distintos refuerzos; y no de proporción entre una respuesta y el total de las respuestas o entre un refuerzo y el total de los refuerzos:

$$
\frac {R_1} {R_2} = \frac {r_1} {r_2}
$$

Como un segundo paso, Baum propuso que la razón de refuerzo es transformada por el agente, como una función de potencia con dos parámetros, similar a la propuesta por S. S. Stevens (AÑO) en la psicofísica sensorial. 

$$
\frac{R_1}{R_2} = \alpha \left( \frac{r_1}{ r_2} \right)^\beta
$$

Donde el parámetro $\beta$ representa que tan *sensible* es la razón de respuesta a los cambios en la razón de refuerzos y el parámetro $\alpha$ representa el *sesgo** en la preferencia por una alternativa sobre otra.

Una forma, visualmente más clara de ver la ecuación anterior, es su transformación logarítmica:

$$
\log \frac{B_1}{B_2} = \beta \log\frac{r_1}{r_2} + \log \alpha
$$

En la figura x podemos ver su comportamiento y en el simulador uds. pueden jugar con diferentes valores de los parámetros de sesgo y sensibilidad. Podemos ver que bajo la transformación logarítmica, la ecuación de potencia se convierte en una familia de líneas rectas en las que $\beta$ es la pendiente de la función y $\alpha$ es su intercepto. Cuando la sensibilidad es igual a uno y no hay sesgo (es decir, $\alpha$  = 0), la ecuación es la ley de igualación y la línea recta parte del origen. Los valores de $\alpha$ positivos o negativos generan líneas rectas paralelas a la recta de igualación. Los valores del parámetro de sensibilidad $\beta$ menores a uno representan sub-igualación y los valores mayores a uno representan sobre-igualación. En el primer caso, la importancia de la diferencia entre los refuerzos se empequeñece psicológicamente y en el segundo caso la misma diferencia se agranda.

imagen

En el marco de referencia de los modelos de elección basados en el valor de las consecuencias, la ecuación generalizada de igualación resulta ser una instancia de una regla de respuesta en la que la probabilidad de cada respuesta es una función de la diferencia entre reforzadores:

$$
P(a_1)= F(\lambda(Qa_1 -Qa_2))
$$

En nuestro caso, el parámetro $\beta$ es $\lambda$ y la función $F$ es una función logística aplicada a la diferencia de los logaritmos de los dos refuerzos:

$$
\log \frac{R_1}{R_2} = \beta (\log{r_1} - \log{r_2}) + \log \alpha
$$

La ecuación generalizada de igualación puede emplearse para distintos usos: ya sea evaluar la preferencia entre diferentes refuerzos (representada por el valor del parámetro alfa); investigar bajo qué condiciones se obtiene igualación perfecta, es decir, cuando $\alpha = 1$ y $\beta = 1$ o finalmente, establecer la forma en la que las diferencias en refuerzo son transformadas en distintas distribuciones del comportamiento. El parámetro $\beta$ puede interpretarse en al menos dos formas, primero como una propiedad del sistema: de la misma forma que el exponente para las funciones psicofísicas varía dependiendo de la dimensión sensorial, la sensibilidad beta podría variar dependiendo del tipo de refuerzo. En segundo lugar, beta también puede interpretarse como el resultado de un conjunto de manipulaciones experimentales y restricciones perceptuales del sistema que imponen límites en la discriminabilidad de las diferencias de refuerzos. Para dar un ejemplo de estas dos interpretaciones plausibles ante un único fenómeno de discriminación: consideremos la diferencia en el refuerzo que generan dos sabores placenteros distintos, esta diferencia es mucho más fácil de distinguir que aquella los refuerzos que otorgan dos sonidos melódicos distintos. Esta diferencia en la facilidad o dificultad para discriminar entre dos estímulos podría deberse a una propiedad intrínseca de los sabores como fenómeno respecto a los sonidos (interpretación 1), aunque también podría deberse a que nuestro sistema sensorial (el sistema sensorial humano) tiene una mayor facilidad para distinguir refuerzos por vía de la modalidad gustativa que por vía de la modalidad auditiva (interpretación 2). La segunda interpretación sugiere que esta dificultad discriminativa podría no presentarse en otras especies con sistemas sensoriales distintos, por ejemplo, en los murciélagos, que poseen sistemas auditivos más agudos que nosotros.


### Igualación como un Mecanismo Adaptable

Una respuesta común al principio de igualación es considerarlo como una instancia de un mecanismo de adaptación, seleccionado para maximizar el total de refuerzos disponibles. Para atender esta posibilidad, es necesario conocer la función que relaciona, por un lado, a la suma del total de los refuerzos, y por el otro, a las distribuciones relativas de respuesta. Con ello, se puede evaluar si el patrón de respuesta de igualación corresponde al máximo de la función. 

$$
r_{total}= f\left(\frac{R_1}{R_1 + R_2}\right)
$$


Dado que en programas de IV los refuerzos no se cancelan hasta que se obtienen, al animal le conviene seguir visitando ambas opciones y de esa forma obtener todos los reforzadores posibles. Sin embargo, el número de posibles distribuciones de respuestas que garantizarían obtener todos los refuerzos es enorme. El organismo podría hacerlo simplemente alternando constantemente cada respuesta (0.5) o pasando casi todo el tiempo en una de las opciones con una ocasional visita a la opción no atendida. Lo sorprendente es que dentro de ese amplio rango de posibles tasas relativas de respuesta que producen maximización, lo que se observa empíricamente es la proporción de respuesta a cada opción que iguala la tasa de refuerzo relativa. La importancia de la igualación es que representa la solución observada, en equilibrio, a la multiplicidad de formas de maximizar el refuerzo total en programas concurrentes de intervalo variable.

#### ¿Es Maximización el Mecanismo que Subyace a Igualación?

Una pregunta muy diferente a la de si la igualación es un comportamiento adaptable es la de si, bajo condiciones de equilibrio, la maximización de la tasa de reforzamiento global es el “mecanismo” que guía el comportamiento del organismo y el cual subyace al patrón de respuestas observado en igualación. En otras notas veremos modelos en los que se maximizan diferentes variables, pero en estas nos concentramos en la maximización del número de refuerzos totales. Para comprender la pregunta, es necesario considerar que los fenómenos de maximización e igualación implican que los algoritmos que los organismos computan son diferentes para cada modelo. De acuerdo a esta versión de la maximización como mecanismo subyacente a la igualación, el algoritmo no distingue entre las dos respuestas disponibles y el refuerzo asociado con cada una de ellas: en lugar de ello, este solo computa y actualiza dos variables, la suma de refuerzos y la tasa relativa de respuestas. Noten que, debido a esto último, este modelo de acción no es una instancia de un modelo de elección basado en el valor de las respuestas individuales. En cambio, este modelo asume que los organismos cuentan con solo dos contadores, uno para la tasa relativa de respuestas y otro para la suma de los reforzadores obtenidos por las dos respuestas, sin distinguir entre su origen. Un reloj acumula el tiempo total *T*,  durante el cual las dos respuestas se encuentran disponibles. El resultado del contador del total de refuerzos se divide entre el tiempo T. En estos casos, el organismo busca acceder al mayor número de refuerzos por unidad de tiempo. Este número de {r/T} representa la *ganancia* asociada con cada distribución posible de respuestas. Además, dentro de un proceso de ascenso de colina, como el visto en las notas x, la tasa relativa de respuesta se mueve en la dirección de una mayor tasa global de refuerzo hasta alcanzar un máximo, el cual puede ser local. 

#### Igualación y Rentabilidad de las Respuestas

Otra explicación que puede dar cuenta del patrón de respuesta de igualación es que los organismos buscan igualar la rentabilidad de sus respuestas o tiempos. La rentabilidad es el número de refuerzos que se obtienen por tiempo o respuestas invertidos en una opción. Cuando ustedes deciden entre planes de ahorro bancario, la primera pregunta que hacen es cuál es la tasa de interés anual, lo que les permite saber cuánto ganarán anualmente por cada $1,000 pesos depositados en su cuenta. Igualación sugiere que esto es exactamente lo que hacen los agentes con la asignación de sus respuestas y tiempos: específicamente, igualación plantea que la regla que siguen los agentes es distribuir sus respuestas y tiempos de tal forma que, en equilibrio, las dos opciones tengan la misma rentabilidad. 
En concreto, bajo este modelo computacional, el organismo en esencia registra la tasa de refuerzo asociada con cada opción de respuesta disponible y luego distribuye sus respuestas proporcionalmente en cada opción para igualar las rentabilidades.
Igualación para respuestas y tiempos también puede expresarse en forma de razones, esto es, en lugar de hablar de una frecuencia relativa de 6 de 8 (0.75) refuerzos para una respuesta, hablamos de una razón de 6 a 2 (3) refuerzos para esa respuesta:

$$
\frac {T_1} {T_2} = \frac {r_1} {r_2}
$$

$$
\frac {R_1} {R_2} = \frac {r_1} {r_2}
$$

Reacomodando términos:

$$
\frac {r_1}{T_1} = \frac {r_2} {T_2} \text{ y } \frac {r_1}{R_1} = \frac {r_2} {R_2}
$$

Esta nueva forma de expresar la ley de igualación refleja que lo que se iguala es la rentabilidad de las distintas opciones de respuesta y/o tiempo. De este modo, lo que los organismos igualan son lo que podemos llamar como *tasas locales de refuerzo*. Así, cuando un organismo sigue la ley de igualación, este experimentará tasas iguales de reforzamiento local en todas las opciones disponibles. Es decir, si el organismo recibe un reforzador por cada 30 respuestas a la Opción A, este ajustará su número de respuestas a la Opción B para igualar la tasa de reforzamiento local de un reforzador por cada 30 respuestas. De manera similar, si el organismo recibe un reforzador por cada 30 segundos dedicados a la Opción A, este ajustará sus respuestas para recibir un reforzador por cada 30 segundos dedicados a la Opción B.

Es importante recalcar que para igualar las tasas de refuerzo local (la tasa de refuerzo por respuesta o por unidad de tiempo) el número de respuestas emitido por el organismo a las distintas opciones puede variar sustancialmente. 

Por ejemplo: 

-Si la Opción A brinda 1 reforzador por cada 30 respuestas y la Opción B brinda 1 reforzador por cada 60 respuestas, igualar las tasas de refuerzo locales requeriría que el organismo respondiera dos veces más a la Opción B que a la Opción A. 

-Si distintos programas IV concurrentes se encuentran operando (por ejemplo, IV 30 s para la Opción A e IV 60 s para la Opción B), igualar las tasas de refuerzo local implicaría asignar distintas cantidades de tiempo y respuestas a cada opción. 

El organismo esencialmente ajusta su comportamiento para obtener un “mismo rendimiento” sobre el tiempo/energía que invierte en todas las alternativas, lo que frecuentemente resulta en una distribución bastante desigual de respuestas. 

También, vale la pena notar que igualdad en las tasas de reforzamiento locales (rentabilidad) ocurre naturalmente a través de la distribución del comportamiento del organismo, independientemente de los diferentes programas de intervalo variable programados para cada opción.

Computacionalmente, considerar que el algoritmo de igualación opera dentro de programas concurrentes de dos respuestas implica que los agentes tienen cuatro contadores, dos para respuestas y dos para reforzadores, y adicionalmente, disponen de dos relojes que se echan a andar cuando cambian a una de las opciones y que se detienen cuando regresan a la opción visitada anteriormente. Estos relojes se usan para computar las tasas locales de refuerzo. 

Aqui falta el ejemplo numerico.

#### Maximización vs Rentabilidad

¿Es posible distinguir entre estas dos interpretaciones de la elección en programas concurrentes? Consideren el siguiente escenario. Una estudiante es la única heredera de dos tías de edad avanzada. El monto de la herencia que le deja una de ellas depende del número de visitas que la sobrina le haga; por otra parte, la cantidad que le deja la otra tía tiene un tope máximo y solo depende de que ella la visite ocasionalmente. El escenario de las tías ilustra un programa concurrente, con una de las opciones reforzada con un programa de intervalo variable y la otra con un programa de razón variable. En este escenario, la estrategia óptima de la sobrina es asignar la mayor parte de sus visitas a la tía más demandante, la que ejemplifica un programa de razón, y visitar ocasionalmente a la tía que ejemplifica el programa de intervalo. 

Herrnstein y Heyman (), llevaron al laboratorio el escenario recién descrito. Expusieron a las palomas a programas concurrentes razón variable - intervalo variable. En este arreglo, una de las respuestas es reforzada de acuerdo a una regla temporal (programa de intervalo variable), mientras que el refuerzo para la otra respuesta depende del número de ellas (programa de razón variable).

Para entender la lógica del experimento, se debe tener presente que en programas de razón variable, la rentabilidad de la respuesta es el número de respuestas necesario para obtener un refuerzo. Por ejemplo, la rentabilidad de un programa de razón variable 30 para una de las opciones es un reforzador por cada treinta respuestas invertidas (1/30). De acuerdo a la ley de igualación, en un programa concurrente RV30 - IVx, el número de respuestas por refuerzo dentro del programa de intervalo debe ser también de 30. Sin embargo, de acuerdo a una regla de maximización global, la distribución óptima sería responder mayoritariamente en la opción reforzada con el programa de razón y visitar ocasionalmente la opción reforzada de acuerdo al programa de intervalo. 

La siguiente figura muestra los resultados obtenidos por Heyman y Herrnstein. Puede verse que la distribución de respuestas de las palomas iguala la distribución de refuerzos, con un sesgo en favor del programa de razón. El patrón de igualación obtenido en este programa favorece al algoritmo de rentabilidad por encima del de maximización. Experimentos más recientes confirman este resultado y resaltan la utilidad de separar el sesgo por una opción (en este caso la opción RV) de la sensibilidad de los organismos hacia las diferencias en refuerzo de los dos programas.   

