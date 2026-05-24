### Formalización matemática del mejoramiento

El ejemplo numérico mostró que el sistema converge al punto de igualación, pero la demostración fue cualitativa: probamos dos puntos de partida y verificamos la dirección de movimiento en cada uno. Para entender *por qué* el sistema converge siempre — y no solo en esos casos particulares — necesitamos describir el mecanismo con mayor precisión. Esa descripción revela algo más profundo: el mejoramiento no es solo un modelo de elección, sino una instancia del mismo algoritmo de ascenso de colina que encontramos en los capítulos 4 y 5, operando ahora sobre una variable que el propio comportamiento del organismo contribuye a construir.

#### La variable de decisión: La señal de discrepancia

Escribamos la tasa de refuerzo local de cada opción como:

$$\rho_i = \frac{r_i}{T_i}$$

donde $r_i$ es el número de reforzadores obtenibles en la sesión y $T_i$ es la proporción de tiempo dedicada a esa opción. La variable que govierna la decisión en el modelo de mejoramiento es la *discrepancia* entre las dos tasas locales:

$$\Delta = \rho_1 - \rho_2 = \frac{r_1}{T_1} - \frac{r_2}{1 - T_1}$$

(donde hemos escrito $T_2 = 1 - T_1$, dado que las dos proporciones suman uno). Esta es la señal de error del sistema: cuando $\Delta > 0$, la opción 1 es más rentable; cuando $\Delta < 0$, lo es la opción 2; cuando $\Delta = 0$, las tasas son iguales y el organismo no tiene incentivo para redistribuir su tiempo. La regla de mejoramiento dice que el organismo se mueve en la dirección de $\Delta$: aumenta $T_1$ cuando $\Delta > 0$, lo disminuye cuando $\Delta < 0$. Una forma simple de escribir, en tiempo discreto,  esta regla es:

$$T_1(n+1) = T_1(n) + \alpha \cdot \Delta(n)$$

donde $\alpha > 0$ es un parámetro  que determina la velocidad de ajuste y que representa la importancia de la diferencia entre las dos tasas locales de refuerzo. Esta ecuación debe resultar familiar: tiene exactamente la misma arquitectura que la regla de actualización de Bush y Mosteller del capítulo 8 y la de Rescorla-Wagner del capítulo 11. En todos los casos, el estado actual se actualiza sumando una discrepancia entre dos variables,  multiplicada por un parámetro de velocidad. La diferencia es que aquí el error no es la diferencia entre un resultado observado y uno predicho, sino la diferencia entre dos tasas de refuerzo local. La arquitectura del comparador es la misma; cambia la naturaleza de las variables que compara.

#### Por qué el sistema siempre converge

La pregunta central es si el proceso descrito por la ecuación de actualización converge al equilibrio desde cualquier punto de partida. Para responderla, hay que determinar qué le ocurre a la discrepancia $\Delta$ cuando $T_1$ se mueve en su dirección.

Consideremos el caso en que $\Delta > 0$ — la opción 1 es más rentable — y el organismo, siguiendo la regla, dedica más tiempo a esa opción. Aumentar $T_1$ produce dos efectos simultáneos que operan en la misma dirección:

**Efecto sobre $\rho_1$:** Al aumentar $T_1$, el denominador de $r_1 / T_1$ crece, de modo que $\rho_1$ *disminuye*. La opción que recibe más tiempo se vuelve menos rentable por visita.

**Efecto sobre $\rho_2$:** Dado que $T_1 + T_2 = 1$, al aumentar $T_1$ se reduce $T_2$. El denominador de $r_2 / T_2$ se achica, de modo que $\rho_2$ *aumenta*. La opción que recibe menos tiempo se vuelve más rentable por visita.

Ambos efectos empujan $\Delta = \rho_1 - \rho_2$ hacia cero: el primer término cae, el segundo sube. El organismo que sigue la regla de mejoramiento activa automáticamente un mecanismo de corrección: al moverse hacia la opción más rentable, erosiona su propia ventaja y eleva la rentabilidad de la opción que está dejando. El sistema se regula a sí mismo.

Este argumento es simétrico: en el caso en que $\Delta < 0$, el organismo aumenta $T_2$, lo que reduce $\rho_2$ y eleva $\rho_1$, volviendo a empujar $\Delta$ hacia cero. En cualquier dirección que se encuentre el desequilibrio, el movimiento lo corrige.

Esto es retroalimentación negativa en su forma más pura: la variable de control (decisión) $\Delta$ cambia de signo cada vez que el organismo se aproxima demasiado a un extremo, corrigiendo el exceso. El equilibrio no es un atractor especial al que el sistema tiene que «apuntar»; es el único punto donde la señal de error desaparece.

#### Un único punto de equilibrio

¿Cuántos puntos de equilibrio tiene este sistema? La respuesta emerge de observar cómo se comportan $\rho_1$ y $\rho_2$ como funciones de $T_1$.

Conforme $T_1$ crece de 0 a 1, la tasa local $\rho_1 = r_1 / T_1$ decrece sin parar: empieza en valores muy altos (cuando $T_1$ es casi cero) y llega a $r_1$ (cuando $T_1 = 1$). La tasa local $\rho_2 = r_2 / (1 - T_1)$ hace exactamente lo contrario: empieza en $r_2$ (cuando $T_1$ es casi cero) y crece sin límite conforme $T_1$ se acerca a 1. Una función estrictamente decreciente y una estrictamente creciente se cruzan exactamente una vez. Ese cruce es el único equilibrio del sistema.

En ese cruce, $\rho_1 = \rho_2$, es decir:

$$\frac{r_1}{T_1^*} = \frac{r_2}{T_2^*}$$

Reorganizando:

$$\frac{T_1^*}{T_2^*} = \frac{r_1}{r_2}$$

Que es la ley de igualación. El único punto donde el sistema deja de moverse es, por construcción aritmética, el punto de igualación.

#### Iteración numérica

La tabla siguiente muestra el proceso de convergencia para el ejemplo IV 1' – IV 2' de una hora, partiendo de $T_1 = 0.5$ y usando un paso $\alpha = 0.002$:

| $n$ | $T_1$ | $\rho_1 = r_1/T_1$ | $\rho_2 = r_2/T_2$ | $\Delta = \rho_1 - \rho_2$ | $V(T_1)$ |
|----:|------:|-------------------:|-------------------:|---------------------------:|---------:|
| 0 | 0.500 | 120.0 | 60.0 | **+60.0** | −62.38 |
| 1 | 0.620 | 96.8 | 79.0 | **+17.8** | −57.71 |
| 2 | 0.656 | 91.5 | 87.1 | **+4.4** | −57.31 |
| 3 | 0.664 | 90.3 | 89.4 | **+0.9** | −57.29 |
| 4 | 0.666 | 90.1 | 89.9 | **+0.2** | −57.29 |
| 5 | 0.667 | 90.0 | 90.0 | **≈ 0** | −57.29 |

Pueden observarse en la tabla los mismos dos fenómenos que describimos cualitativamente. Conforme $T_1$ crece, $\rho_1$ cae de 120 a 90 y $\rho_2$ sube de 60 a 90: los dos efectos simultáneos que reducen $\Delta$. Y $\Delta$ decrece de 60 a casi cero en cinco pasos, cada uno más pequeño que el anterior, hasta que el sistema se detiene en el único punto donde no hay incentivo para seguir moviéndose. Como retroalimentación negativa: el sistema se ajusta en cada paso para corregir la discrepancia, y la corrección es proporcional al error.

Esta secuencia es idéntica, en su lógica, al ascenso de colina que describimos en el capítulo 4. Allí, la bacteria comparaba la concentración actual con la anterior y se movía en la dirección del gradiente; aquí, el organismo compara las tasas locales de dos opciones y se mueve hacia la más rentable. En ambos casos, el movimiento sigue la dirección de una señal de discrepancia, y esa señal disminuye con cada paso. La cima de la colina que el mejoramiento escala es el punto donde la discrepancia desaparece, y ese punto resulta ser algebraicamente idéntico al punto de igualación.

**[FIGURA 15.5: Dos paneles. Panel izquierdo: $V(T_1)$ en función de $T_1$. Curva cóncava con máximo único en $T_1^* = 2/3$. Los puntos de la iteración numérica se superponen como una trayectoria que escala la curva desde la izquierda. Panel derecho: $\Delta$ en función de $n$ (número de iteraciones). Curva decreciente desde 60 hasta 0. Ambos paneles comparten el mismo eje de iteración, mostrando que el ascenso de $V$ y la reducción de $\Delta$ son simultáneos. Paleta del libro.]**
