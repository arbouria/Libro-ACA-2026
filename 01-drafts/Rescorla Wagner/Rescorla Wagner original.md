# ---
title: El Modelo de Rescorla y Wagner
author: Arturo Bouzas
format: html
---
En el capítulo anterior, vimos que el modelo de aprendizaje por refuerzo, conocido también como modelo de *aprendizaje de error de predicción* captura razonablemente bien la adquisición de valor predictivo cuando un estímulo o respuesta van seguidos de un refuerzo. En este capítulo veremos que este modelo *no* puede dar cuenta de los resultados presentados en el capítulo sobre asignación de crédito, los cuales ilustran la importancia de una serie de correlaciones: aquellas que sostiene el EC o la respuesta con la aparición del refuerzo; aquellas que sostiene el EC con otros estímulos presentes (elementos del contexto); y aquellas que existen previamente entre otros estímulos distintos y el refuerzo actual. Originalmente, estos últimos resultados indujeron interpretaciones que enfatizaban que la asignación de crédito a un estímulo o respuesta dependía de que estos fueran seguidos de un refuerzo que era *sorpresivo, inesperado,  informativo, o que atraía la atención. * En 1972, Rescorla y Wagner presentaron un modelo que daba cuenta de los resultados que muestran que la mera contigüidad no es un factor necesario ni suficiente para la asignación de crédito. El modelo es una extensión del principio de la reducción de error, que captura la intuición acerca del papel de la sorpresa como un modelo matemático: todo ello sin hacer referencia a procesos atencionales que se suponían difíciles de evaluar con sujetos no humanos. Este modelo sigue siendo hasta la fecha el motor de la investigación en aprendizaje. 

## Modelo de Rescorla y Wagner

El modelo de Rescorla y Wagner incluye dos grandes componentes. El primer componente es el *Modelo de Refuerzo* de Bush y Mosteller, el cual hemos visto que establece la reducción en el error de predicción como el motor del aprendizaje. El segundo componente es un modelo de la forma en la que un organismo percibe estímulos compuestos. En particular, este modelo supone que los organismos perciben a los estímulos, por ejemplo un rostro, como un conjunto de elementos separables: en este caso, un rostro se percibe en términos de ojos, nariz, labios, entre otros. El modelo asume que todos estos elementos compiten entre ellos por la asignación de crédito.

El modelo de aprendizaje utilizado por Rescorla y Wagner es una variante del modelo de la reducción en el error de la predicción (también conocido como la regla delta).  

$$
Vx_{t+1}= Vx_t + a (R_t - Vx_t), \text{  donde:  } 0<a<1.   
$$

Para entender el segundo componente del modelo de Rescorla y Wagner, consideremos por un momento las características del entorno modelado. Hasta antes de los años 60s del siglo pasado, los investigadores limitaban sus experimentos a protocolos en los que se presentaba un solo estímulo condicionado. Sin embargo, los entornos reales no consisten de elementos que aparecen aisladamente y cuyo único aspecto complejo es la variabilidad en su distancia temporal respecto al SBI. Por el contrario, los organismos encaran entornos en los que múltiples estímulos se presentan simultáneamente y en ocasiones de manera contigua con los refuerzos. Una comida que nos enferma o que nos produce un gran placer es en sí misma un compuesto de múltiples estímulos: el plato en que se sirve, el mantel bajo el plato, cómo se ve, su aroma, la música que se está escuchando, la persona que la sirve. Más aún, cada uno de nosotros tenemos experiencias diferenciadas con cada uno de estos elementos por separado, correlacionados con otros o con el mismo reforzador. Hemos comido en ese mantel otras comidas, con platos y aromas diferentes. El modelo de Rescorla y Wagner describe el algoritmo, la regla por la cual se le asigna crédito a cada elemento de la experiencia con una comida. En ese sentido, el modelo le da respuesta a la pregunta: ¿Cómo puede un organismo extraer relaciones de “causalidad” en ésta red de diversas experiencias? En resumen, el modelo de Rescorla y Wagner captura los principios que describen la asignación de crédito a los distintos elementos de un estímulo compuesto que es seguido por un reforzador. Al mismo tiempo, el modelo especifica el efecto que juega la experiencia previa del agente con cada uno de los elementos por separado dentro de la asignación de crédito. 

### Supuestos del Modelo de Rescorla y Wagner

#### El supuesto de la separabilidad de los estímulos. 

Los estímulos en compuesto están conformados por elementos (estímulos) separables. Desde esta perspectiva, una cara, por ejemplo, no es un estímulo integrado, sino un conjunto de elementos (ojos, boca, orejas, nariz, etc.).

#### El supuesto del valor predictivo de los elementos

Cada elemento de un compuesto, sea un estímulo o una respuesta, tienen un número ligado a ellos; a este número le llamamos Valor. El valor puede tomar números positivos pero también negativos. Cuando el valor es positivo predice la ocurrencia de un refuerzo, cuando es negativo predice su ausencia. Por esta razón, a dicho número también se le conoce como el valor predictivo del estímulo. El valor (V) se actualiza en cada ocasión que se presenta el estímulo o respuesta (EC) y el cambio en la magnitud del mismo depende de si el EC se presenta acompañado o no de un suceso biológicamente importante (R). La relación entre el valor y alguna medida de comportamiento es únicamente ordinal. Las diferencias en valor sólo predicen diferencias en el ordenamiento de alguna medida del comportamiento. En otras palabras, un elemento de un estímulo compuesto (por ejemplo, la nariz en los rostros) con un valor predictivo V de 1 no induce el doble de respuestas en un agente con relación a otro elemento del estímulo compuesto que tenga un valor de 0.5 (por ejemplo, el vello en los rostros): lo único que nos señalan estos valores numéricos es que el agente le está asignando mayor crédito por la ocurrencia del refuerzo a la nariz con relación al vello de los sujetos, y que el agente responderá más ante estímulos que contengan narices que ante estímulos que contengan vello (sin especificar cuantitativa ni precisamente esta diferencia de respuestas).

#### La regla de integración del valor de los elementos

El modelo computa por separado, para cada uno de los elementos de un compuesto, su valor predictivo V, y el valor predictivo del compuesto es la suma de los valores predictivos de cada uno de sus elementos. Si el compuesto incluye dos estímulos A y B, se computan por separado VA y VB. La fuerza de la predicción del compuesto es la suma de los Vs es, en nuestro caso:

$$
V_{total} = V_{A}+ V_{B}. 
$$

#### La regla de la actualización del valor predictivo de los elementos.

La ecuación de Rescorla y Wagner mantiene el supuesto de que la asignación de crédito a cada uno de los elementos de un compuesto es una función de la discrepancia entre lo que se obtiene y lo que se espera obtener. La contribución de Rescorla y Wagner es suponer que lo que se espera obtener dada la presentación de un compuesto es el resultado de la suma del valor predictivo de todos los elementos presentes simultáneamente ($V_{total}$).

$$
Vx_{t+1} = Vx_t + a(R-V_{total_t})
$$

Recuerden que en nuestro protocolo, R es un valor binario que representa la presentación ($R=1$) o no ($R=0$) de un refuerzo. Como en la ecuación de Bush y Mosteler, *a* es un parámetro de aprendizaje que determina la importancia del error de predicción. 

La ecuación especifica la reducción del error de predicción como motor del aprendizaje y, como puede verse en el simulador, este modelo produce curvas de aprendizaje de ganancias decrecientes, en las cuales el cambio en V es cada vez más pequeño conforme el error de predicción se reduce. La parte novedosa de la ecuación consiste en tomar como predicción la suma del valor de todos los elementos presentes: lo cual nos conduce al último supuesto del modelo…

#### Competencia entre los elementos de un compuesto

Los elementos separados compiten entre sí por el valor predictivo del compuesto que conforman. Recordemos que el valor predictivo total de un estímulo compuesto es limitado, lo que implica que mientras mayor sea el valor de uno de los elementos, quedará menos “valor predictivo” para ser distribuido a los demás elementos del compuesto.

### La ecuación de Rescorla y Wagner

$$
Vx_{t+1} = Vx_t + \alpha \beta(R-V_{total_t})
$$

En ocasiones la ecuación de Rescorla y Wagner se representa en términos de los cambios de ensayo a ensayo.

$$
\Delta Vx =Vx_{t+1} - Vx_t
$$

Las preguntas que emergen al considerar este modelo son: primero, ¿de qué variables depende el parámetro “a”? y segundo, ¿es “a” el único parámetro que determina la velocidad del aprendizaje? Empíricamente, podemos considerar dos variables: en primer lugar, la naturaleza del refuerzo. Por ejemplo, más y mejor comida produce un aprendizaje más rápido. Una segunda variable es la naturaleza del estímulo predictor. Un estímulo más intenso o sobresaliente produce curvas de aprendizaje más aceleradas. La importancia de este segundo elemento -la saliencia del EC- se representa en la ecuación con un parámetro adicional de aprendizaje que llamaremos beta, el cual también adquiere valores entre cero y uno y también se multiplica por el error de predicción para ponderar su importancia relativa.

$$
\Delta Vx = \alpha \beta (R-V_{total_t})
$$

Para ayudar a entender el modelo de Rescorla y Wagner en su aplicación a la vida cotidiana, consideren el siguiente escenario. Un amigo al que ustedes visitan con frecuencia consiguió un nuevo perro. A ustedes les gustaría saber si este es un perro al que se le puede acariciar sin temor a que este los muerda. El perro es un compuesto de múltiples elementos: tamaño, hocico, ojos, orejas, tipo de pelo, entre otros. Su primera respuesta ante ese nuevo perro va a ser el resultado de la suma de los valores predictivos de los distintos elementos que lo componen, adquiridos de sus múltiples experiencias con otros perros. Por ejemplo, imaginemos que en algún momento del pasado se encontraron con un perro pequeño y chato que nunca trató de morderlos; posteriormente, cuando se encuentran con el perro de su amigo que comparte el mismo tamaño chico de aquel perro pero que tiene un hocico largo, su predicción sobre si este los morderá será la suma de lo que para ustedes predicen, por separado, su tamaño y su tipo de hocico. En este caso, el tamaño (y no el tipo de hocico) del perro de su amigo tendrá un valor predictivo en el sentido de que el animal no les morderá. Por otra parte, si el perro de su amigo intenta morderlos, el valor de los dos atributos se actualizará a través del error de predicción. Es decir, si la suma de los valores predictivos de los elementos del perro de su amigo predijo en un inicio que este no los mordería, y este efectivamente procede a morderlos, entonces habrá un error de predicción que actualizará el valor de cada uno de los elementos que conforman al perro. De esta forma, el elemento del tamaño chico del perro perderá su valor como un predictor de una “no mordida”, mientras que el elemento del “hocico largo” adquirirá valor como un predictor de una “mordida”. 

### Aplicación del modelo de Rescorla y Wagner al experimento de ensombrecimiento

Considere el protocolo experimental mostrado en la figura x. Hay tres grupos, para el grupo G1 en cada ensayo se presenta un compuesto de dos estímulos (tono y luz) seguidos por el acceso a alimento. Para otros dos grupos solo se les presenta el tono o la luz, cada uno seguido de comida. Vamos a suponer que el tono y la luz no son igualmente sobresalientes (es decir, tienen betas diferentes). Para el grupo G1, el error de predicción es $R$ menos la suma del valor adquirido en cada ensayo por los elementos del compuesto, para el cual: $V_{total} =  V_{luz} + V_{Tono}$. Para los otros dos grupos, el error de predicción es R menos el valor de cada elemento por separado, $V_T$ o $V_L$. En la simulación puede verse que cuando se tiene un tono ligeramente más sobresaliente que la luz en el grupo con el estímulo compuesto, ni el tono ni la luz alcanzan valores cercanos a $R$. En los grupos en los cuales los dos estímulos se presentan por separado, ambos estímulos alcanzan valores que se aproximan a $1$, el valor de $R$.

imagen

### Aplicación del modelo de Rescorla y Wagner al experimento de bloqueo

La figura x muestra el protocolo experimental del procedimiento de bloqueo. Existen dos grupos, los cuales tienen en común el que se les presenta un compuesto de un tono y una luz, seguidos por el acceso a comida. Ambos grupos difieren en que para uno de ellos, al cual llamaremos el grupo de bloqueo, en una primera fase se le presenta solo el tono seguido de la comida. El otro grupo, un control, no tiene esta experiencia. Para el grupo de bloqueo, que recibe en la fase 1 la experiencia con el tono seguido de la comida, al final de esa fase el valor (R - Vtono) es casi cero y el valor del tono VT es igual a R. En lenguaje menos técnico, el tono predice perfectamente la presentación de la comida. 

Para este grupo en la fase  en el primer ensayo de esa fase $V_{total} = V_T + V_L = (R + 0)$ y consecuentemente $(R - V_{total}) =  (R - R +0) = 0$. Computando la actualización del valor de la luz:
$V_{L+1} = V_L + a (R - V_{total}) = 0 + a (1 - 1) = 0$.

Vemos que no se le asigna valor al elemento luz. En resumen, cuando el elemento de un compuesto ya predice la presentación del refuerzo, el otro elemento del compuesto no adquiere valor predictivo, tal y como puede verse en el resultado de la simulación presentada en la Figura x.

imagen

### Predicción contraintuitiva del modelo de Rescorla y Wagner

Cualquier versión del modelo de refuerzo predice que un refuerzo adicional debe incrementar, aunque sea por un monto muy pequeño, el valor predictivo de un estímulo. Sin embargo, veamos qué predice el modelo de Rescorla y Wagner en el siguiente protocolo. A un grupo lo exponemos a tres fases de entrenamiento. En la primera fase, un tono es seguido de comida durante 60 ensayos. En una segunda fase, una luz es el estímulo condicionado y es seguida de comida durante otros 60 ensayos. En la tercera fase, la final, a los sujetos experimentales se les presenta el compuesto tono-luz, seguido de comida durante 60 ensayos. Al inicio de la tercera fase, $VL = R$; $VT = R$ y $V_{total} = 2R$, de tal forma que el error de predicción para ambos estímulos, será $R - 2R$, por lo que $V_{t+1}$ será un número negativo y veremos un decremento en el valor predictivo para los dos estímulos. Interesantemente, se ha encontrado evidencia empírica que respalda esta predicción contraintuitiva del modelo. La siguiente figura muestra el resultado de la simulación.

imagen

### Aplicación del modelo de Rescorla y Wagner a estudios de protocolos de correlaciones

Un reto importante para la ecuación de Rescorla y Wagner es dar cuenta de los resultados de los experimentos de Rescorla en los que se manipula la relación de contingencia: esto es, experimentos en los que se manipula la probabilidad de la presentación del refuerzo, dada la presencia o ausencia del EC. Recuerden que en esos experimentos, se encontró que manteniendo constante la probabilidad de refuerzo en la presencia del estímulo condicionado, el crédito que se le asigna depende de la probabilidad de refuerzo en su ausencia. Sin embargo, de acuerdo a una interpretación literal de la ecuación de Rescorla y Wagner, el error de predicción para el estímulo condicionado es independiente de la aparición o no aparición del refuerzo en la ausencia del EC. La solución propuesta por Rescorla y Wagner para que su modelo de cuenta de estos hechos empíricos es considerar al contexto en el que se presenta el EC como un estímulo más. El contexto es el interior del espacio experimental e incluye, entre otros elementos, la iluminación, el olor y la textura del espacio. De esta forma, el protocolo de los experimentos de Rescorla incluye dos estímulos: el compuesto del estímulo condicionado junto con el contexto; y un segundo estímulo, el contexto solo. En el caso del procedimiento con igual probabilidad de refuerzo en la presencia y la ausencia del EC, la ecuación de Rescorla y Wagner interpreta el experimento como uno de bloqueo en el que el contexto X es el mejor predictor del refuerzo y termina bloqueando la asignación de crédito al estímulo condicionado. 

Una forma de evaluar su comprensión del modelo de Rescorla y Wagner es considerar cuál sería su predicción para un experimento con protocolo no correlacionado (sin correlación entre el EC y $R$), en el cual los refuerzos que se presentan durante el intervalo entre ensayos son señalados con un tercer estímulo diferente al estímulo condicionado. ¿Qué cambios se pueden esperar en la asignación de crédito el estímulo condicionado? 

### El modelo de Rescorla y Wagner e inhibición condicionada

Hasta este punto, hemos argumentado que de acuerdo al modelo de Rescorla y Wagner, tanto estímulos como respuestas adquieren un valor que les permite predecir la presencia de un refuerzo, pero siguiendo este modelo ¿pueden los estímulos/respuestas predecir la ausencia de un refuerzo? En este apartado le daremos respuesta a esa pregunta.

Poder predecir la *no* ocurrencia de ciertos refuerzos, tiene importantes ventajas competitivas para el organismo, en particular, le permite acomodar su distribución de comportamientos de una mejor manera. La señal de que un depredador no va a aparecer, le permite a la potencial presa buscar su alimento sin interrupciones; de igual manera, la señal que predice que no habrá comida, le permite al organismo reorientar su comportamiento hacia la búsqueda de otros refuerzos.  Al estudio de este fenómeno se le conoce como *inhibición condicionada*.

El estudio de la inhibición condicionada tardó décadas en despegar por dos razones. La primera está relacionada con la estructura del modelo original de aprendizaje por refuerzo, que no permite valores negativos para el valor de un estímulo. Si la mayor parte del ﬂujo de estímulos y respuestas no van seguidos de un refuerzo, ¿que se aprende acerca de estos eventos? Imaginen que se encuentran con una persona paseando a un perro que los ignora completamente. Consideremos qué predice el modelo de refuerzo sobre lo que ustedes aprenderán acerca de esa persona. En este episodio, el perro no era un suceso biológicamente importante -ni les gruñó, ni les movió la cola- consecuentemente $R$ es igual a cero. Adicionalmente, la persona era un desconocido que no predice nada, su $V$ es por lo tanto igual a cero. De acuerdo al modelo de refuerzo, el cambio en el valor predictivo de la persona ($Vx$) es una función del error de predicción ($R - Vx$), en este caso ($0 - 0$) y por lo tanto no habría tampoco ningún cambio en Vx. En otras palabras, si dado un estímulo, nada se espera y nada se obtiene, ese estímulo no predice nada. 

A diferencia del modelo de refuerzo tradicional, el modelo de Rescorla y Wagner permite que un estímulo tenga un valor negativo y sea un predictor de la ausencia de un reforzador. Regresemos a nuestro ejemplo de una persona paseando a un perro, excepto que esta vez, imaginemos que el perro les gruñe de forma amenazante. Después de muchos encuentros similares, la persona paseando al perro se convierte en el predictor de un perro agresivo. En un siguiente encuentro, la persona que pasea al perro va acompañada de su pareja y el perro esta vez no les gruñe, *generando un error de predicción* con valor negativo. Después de muchos encuentros de este tipo, la pareja de la persona que pasea al perro se convierte en un inhibidor condicionado, el cual predice la no ocurrencia del gruñido del perro.  Recordando que en la ausencia de un refuerzo, R es igual a cero, el error de predicción es negativo sólo si el estímulo neutro aparece en compuesto con un estímulo con valor positivo. De esa forma $V_{total} > 0$ y el error de predicción $(R - V_{total}) < 0$. 

En conclusión, de acuerdo a Rescorla y Wagner, un estímulo/ respuesta se convierte en un inhibidor condicionado, solo si hay un error de predicción negativo como resultado de presentarlo en compuesto con un predictor de refuerzo.

La segunda razón que dificulta el estudio de la inhibición condicionada es la dificultad para distinguir empíricamente entre un estímulo neutro -es decir, uno que no predice nada- y un estímulo que predice la ausencia de algo. En este tema, la contribución de Rescorla es también un punto de partida. En 1969, propuso dos protocolos necesarios para argumentar y sostener que un estímulo era un inhibidor condicionado. 

En un primer protocolo, conocido como de *sumación*, se compara, por un lado, la respuesta a un estímulo condicionado $A$ con valor positivo presentado individualmente; con, por otra parte, la respuesta ante un compuesto del estímulo $A$ acompañado de un estímulo $X$. Nuestro objetivo es determinar si $X$ es un inhibidor condicionado. Si la respuesta al compuesto $AX$ es menor u opuesta a la respuesta observada ante el estímulo $A$ presentado individualmente, podríamos concluir que el estímulo $X$ es un inhibidor condicionado. Regresando a nuestro ejemplo, podemos argumentar que la pareja del paseador de perro es un inhibidor condicionado, si el perro no gruñe cuando la pareja acompaña al paseador y sí gruñe cuando este va acompañado únicamente de su paseador. Sin embargo, Rescorla señala que estos resultados tienen una segunda interpretación: es posible que la atención dirigida al estímulo $X$ (la pareja) reduzca la atención dirigida al estímulo $A$ (el paseador) resultando en la menor respuesta al perro. En resumen, $X$ no sería un predictor de la ausencia de gruñido (no sería un inhibidor condicionado), simplemente, $X$ contribuiría a que se ignore a $A$. Las siguientes dos figuras muestran el protocolo de sumación y el resultado de una simulación.


IMAGENES


De acuerdo a Rescorla, para descartar la interpretación alternativa del protocolo de sumación en términos de atención se requiere de una prueba adicional. A esta se le conoce como *prueba de retardo* y consiste en comparar la curva de adquisición de valor predictivo de un estímulo neutral A presentado individualmente, con la presentación -también individual- de un estímulo $X$ que se entrenó como un inhibitorio y que tiene un valor negativo. Si el aprendizaje es más lento para el segundo estímulo $X$, podríamos concluir que este se trata de un estímulo inhibitorio. La figura x muestra los resultados de la simulación con este protocolo.

IMAGEN


Sin embargo, otra posible explicación de los resultados de la prueba de retardo  hace también referencia a procesos de atención. Es posible que por el entrenamiento previo, el estímulo $X$ deje de activar los procesos de atención y que por lo tanto la demora en el aprendizaje de su valor predictivo se deba a la falta de atención que este recibe en comparación con la atención que recibe el estímulo novedoso neutral. Sin embargo, noten que en el protocolo de sumación, la explicación alternativa para dar cuenta de una menor respuesta del organismo ante el estímulo compuesto ($X+EC$) era una mayor atención otorgada al estímulo $X$, el cual desviaba la atención del estímulo EC; mientras tanto, en el protocolo de retardo, la explicación alternativa para dar cuenta de la menor respuesta ante el estímulo $X$ es una menor atención asignada al estímulo $X$ debido a la familiaridad con este estímulo. Por lo tanto, Rescorla propone que para concluir que un estímulo/respuesta es un inhibidor, este debe pasar tanto la prueba de sumación como la de retardo. No resulta plausible que un estimulo reciba menos atención en una circunstancia y el mismo reciba mayor atención en la otra circunstancia: por lo cual, si el estímulo actúa como inhibidor en ambas circunstancias, esto significa que su efecto no se debe a meros procesos atencionales de novedad/habituación, sino que efectivamente, el organismo considera a este estímulo como un predictor de la ausencia de un SBI. En otras palabras, dado que la variable de atención tiene efectos contrarios en las dos pruebas: al encontrar un estímulo que pasa ambas pruebas, se eliminan las explicaciones alternativas de más y de menor atención, y se puede considerar a este estímulo como un inhibidor condicionado.

### Algunos problemas con el modelo de Rescorla y Wagner

Dentro de la Psicología, pocos modelos han sido tan exitosos como el de Rescorla y Wagner en dar cuenta de una amplia gama de resultados, abrir nuevas rutas de investigación y capturar formalmente explicaciones alternativas al papel de la contigüidad en la asignación de crédito. Sin embargo, como ocurre con cualquier otro modelo, hay un número de sus predicciones que no tienen sustento empírico. Estas fallas han dado lugar a extensiones de modelos y a modelos alternativos que veremos en otro capítulo. A continuación presentamos dos de las predicciones erróneas. Seleccionamos estas por su fácil comprensión y por ser las que han dado lugar a modelos alternativos.

##### Supuesto de que la extinción reduce el valor de un estímulo/respuesta a cero

En extinción, el refuerzo que previamente seguía a un estímulo o respuesta deja de presentarse. En este caso $R$ cambia de un valor de $1$ a $0$. El modelo asume que no habrá un error de predicción cuando el valor del estímulo sea igual a $R$, esto es, cuando el valor del estímulo sea también cero. Consecuentemente, para Rescorla y Wagner, el impacto de un estímulo que fue extinguido, debe ser el mismo que el de un estímulo neutral dado que para ambos estímulos $V = 0$.

Sin embargo, hay una multitud de reportes que señalan que el mero paso del tiempo produce una recuperación espontánea del efecto que originalmente tenía un  estímulo que ha atravesado un proceso de extinción. Adicionalmente, se ha encontrado que estímulos previamente extinguidos adquieren valor predictivo más rápido que estímulos neutrales, a pesar de que se supone que ambos inician con un valor igual a cero. Esta literatura y los modelos para dar cuenta de ella la presentamos en el capítulo sobre extinción.

#### Inhibición latente

Consideremos el siguiente protocolo experimental. En una primera fase, a un grupo se le presenta, durante 60 ensayos, un estímulo neutral que no es seguido por un refuerzo; y en una segunda fase, la presentación de este mismo estímulo sí va seguida de un refuerzo. A un segundo grupo, solo se les presenta la segunda fase, sin darle la experiencia con el estímulo solo. A este protocolo se le conoce como inhibición latente. De acuerdo a Rescorla y Wagner, el valor de los dos estímulos debería ser el mismo. Sin embargo, una enorme literatura reporta que la preexposición a un estímulo sin refuerzo demora la subsecuente adquisición de valor cuando ese estímulo va acompañado de un refuerzo. 

El fenómeno de la inhibición latente ha generado una importante alternativa teórica al modelo de Rescorla y Wagner, la cual revisaremos en otro capítulo y que pone el énfasis en la *atención* asignada a un estímulo cuando este es seguido de un refuerzo inesperado. Inhibición latente sería el resultado de la falta de atención que se le asigna a un estímulo que fue presentado por muchos ensayos sin ser seguido por ningún refuerzo, y que por lo tanto, desde la perspectiva del organismo, no predice que algo importante ocurrirá.

