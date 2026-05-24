Formalización matemática del mejoramiento

El ejemplo numérico mostró que el sistema converge al punto de igualación, pero la demostración fue cualitativa: probamos dos puntos de partida y verificamos la dirección de movimiento en cada uno. Para entender por qué el sistema converge siempre — y no solo en esos casos particulares — necesitamos describir el mecanismo con mayor precisión. Esa descripción revela algo más profundo: el mejoramiento no es solo un modelo de elección, sino una instancia del mismo algoritmo de ascenso de colina que encontramos en los capítulos 4 y 5, operando ahora sobre una variable que el propio comportamiento del organismo contribuye a construir.

La señal de discrepancia

Escribamos la tasa de refuerzo local de cada opción con un símbolo compacto:

 

donde  es el número de reforzadores obtenibles en la sesión y  es la proporción de tiempo dedicada a esa opción. La variable que governa la decisión en el modelo de mejoramiento es la discrepancia entre las dos tasas locales:

 
 

(donde hemos escrito , dado que las dos proporciones suman uno). Esta discrepancia es exactamente la señal de error del sistema: cuando , la opción 1 es más rentable; cuando , lo es la opción 2; cuando , el sistema está en equilibrio.

La regla de mejoramiento dice que el organismo asigna más tiempo a la opción más rentable. En tiempo discreto, eso equivale a actualizar  en la dirección de :


donde  es un parámetro de paso que determina la velocidad de ajuste. Esta ecuación debe resultar familiar: tiene exactamente la misma arquitectura que la regla de actualización de Bush y Mosteller del capítulo 8 y la de Rescorla-Wagner del capítulo 11. En todos los casos, el estado actual se actualiza sumando un error — la discrepancia entre lo que hay y lo que debería haber — multiplicado por un parámetro de velocidad. La diferencia es que aquí el error no es la diferencia entre un resultado observado y uno predicho, sino la diferencia entre dos tasas de refuerzo local. La arquitectura del comparador es la misma; cambia la naturaleza de las variables que compara.

Por qué el sistema siempre converge

La pregunta central es si el proceso descrito por la ecuación de actualización converge al equilibrio desde cualquier punto de partida. Para responderla, hay que determinar qué le ocurre a la discrepancia  cuando  se mueve en su dirección.

Calculemos cómo cambia  al cambiar :

 
 
 

Ambos términos son negativos para cualquier valor de  en el intervalo . Por tanto:

 

Este resultado es el núcleo del argumento. Significa que la discrepancia  es una función estrictamente decreciente de : cada vez que el organismo aumenta el tiempo dedicado a la opción 1, la discrepancia disminuye. La regla de mejoramiento mueve a  en la dirección de , y eso reduce . Si , el organismo aumenta , lo que disminuye  —eventualmente hasta cero. Si , el organismo disminuye , lo que aumenta  —eventualmente hasta cero. En ambos casos el movimiento empuja al sistema hacia el punto donde . Hay exactamente un punto donde eso ocurre, y en ese punto las tasas locales son iguales: .

Esto es retroalimentación negativa en su forma más pura: la variable de control  cambia de signo cada vez que el organismo se aproxima demasiado a un extremo, corrigiendo el exceso. El equilibrio no es un atractor especial al que el sistema tiene que «apuntar»; es el único punto donde la señal de error desaparece.

La función potencial

Existe una manera de unificar las dos descripciones anteriores — el algoritmo de ascenso de colina y el sistema de retroalimentación negativa — en una sola imagen. Definamos la función:


Calculemos su derivada respecto a :

 
 
 

La derivada de  es exactamente la señal de discrepancia . Por tanto, la regla de actualización del mejoramiento puede escribirse como:

 

Esto es gradiente ascendente sobre : el organismo, al seguir la regla de mejoramiento, escala la función exactamente como la bacteria en el capítulo 4 escala el gradiente de concentración. El «paisaje» que el organismo navega no está en el entorno físico; está definido por los valores de los programas de refuerzo y la distribución de tiempo del propio organismo. Pero el algoritmo de navegación es el mismo.

¿Cuál es la cima de ese paisaje? La segunda derivada de :

 
 
 

 es estrictamente cóncava: no tiene máximos locales, solo un máximo global. Ese máximo se alcanza donde , es decir, donde , es decir, donde las tasas locales son iguales. Igualando:

 
 
 
 

La cima de la función potencial coincide exactamente con el punto de igualación. El organismo que sigue la regla de mejoramiento — sin conocer , sin calcular proporciones relativas, sin representar la ley de igualación — escala de manera implícita esta función hasta su único máximo. Igualación es la cima de la colina.

Iteración numérica

La tabla siguiente muestra el proceso de convergencia para el ejemplo IV 1' – IV 2' de una hora, partiendo de  y usando un paso :

0	0.500	120.0	60.0	+60.0	−62.38
1	0.620	96.8	79.0	+17.8	−57.71
2	0.656	91.5	87.1	+4.4	−57.31
3	0.664	90.3	89.4	+0.9	−57.29
4	0.666	90.1	89.9	+0.2	−57.29
5	0.667	90.0	90.0	≈ 0	−57.29
Pueden verse simultáneamente las tres descripciones del proceso. Como ascenso de colina:  crece monotónicamente en cada paso, aproximándose a su máximo global. Como reducción de error:  decrece en cada paso, aproximándose a cero. Como retroalimentación negativa: el sistema se ajusta en cada paso para corregir la discrepancia, y la corrección es proporcional al error.

Los tres son el mismo proceso descrito desde perspectivas distintas. El organismo no computa  ni calcula gradientes: solo compara, en cada oportunidad, las tasas locales de las dos opciones y se mueve hacia la más rentable. Pero ese algoritmo local tiene, como consecuencia global, maximizar  — y la cima de  es igualación.

[FIGURA 15.5: Dos paneles. Panel izquierdo:  en función de . Curva cóncava con máximo único en
. Los puntos de la iteración numérica se superponen como una trayectoria que escala la curva desde la izquierda. Panel derecho:  en función de  (número de iteraciones). Curva decreciente desde 60 hasta 0. Ambos paneles comparten el mismo eje de iteración, mostrando que el ascenso de  y la reducción de  son simultáneos. Paleta del libro.]