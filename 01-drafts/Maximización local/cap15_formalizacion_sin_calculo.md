### Formalización matemática del mejoramiento

El ejemplo numérico mostró que el sistema converge al punto de igualación, pero la demostración fue cualitativa: probamos dos puntos de partida y verificamos la dirección de movimiento en cada uno. Para entender *por qué* el sistema converge siempre — y no solo en esos casos particulares — hay que examinar con más cuidado qué le ocurre a las tasas locales cuando el organismo redistribuye su tiempo. Al hacerlo, aparece una conexión directa con el algoritmo de ascenso de colina del capítulo 4 y con los sistemas de retroalimentación negativa del capítulo 5.

#### La señal de discrepancia

Llamemos $\rho_i = r_i / T_i$ a la tasa local de refuerzo de la opción $i$. La variable que gobierna la decisión en el mejoramiento es la *discrepancia* entre las dos tasas:

$$\Delta = \rho_1 - \rho_2$$

Esta es la señal de error del sistema: cuando $\Delta > 0$, la opción 1 es más rentable; cuando $\Delta < 0$, lo es la opción 2; cuando $\Delta = 0$, las tasas son iguales y el organismo no tiene incentivo para redistribuir su tiempo. La regla de mejoramiento dice que el organismo se mueve en la dirección de $\Delta$: aumenta $T_1$ cuando $\Delta > 0$, lo disminuye cuando $\Delta < 0$.

Esta arquitectura — estado actual actualizado por una señal de discrepancia — es la misma que la regla de Bush y Mosteller del capítulo 8 y la de Rescorla-Wagner del capítulo 11. En todos los casos, el sistema compara dos cantidades, calcula su diferencia y se ajusta para reducirla. La diferencia es que aquí las cantidades comparadas no son una predicción y un resultado observado, sino dos tasas de refuerzo local. El comparador es el mismo; cambia lo que compara.

#### Por qué el movimiento siempre reduce la discrepancia

La pregunta central es si, al seguir la regla de mejoramiento, la discrepancia $\Delta$ siempre se reduce. La respuesta depende de un hecho aritmético simple sobre las tasas locales: qué les ocurre cuando el organismo redistribuye su tiempo.

Consideremos el caso en que $\Delta > 0$ — la opción 1 es más rentable — y el organismo, siguiendo la regla, dedica más tiempo a esa opción. Aumentar $T_1$ produce dos efectos simultáneos que operan en la misma dirección:

**Efecto sobre $\rho_1$:** Al aumentar $T_1$, el denominador de $r_1 / T_1$ crece, de modo que $\rho_1$ *disminuye*. La opción que recibe más tiempo se vuelve menos rentable por visita.

**Efecto sobre $\rho_2$:** Dado que $T_1 + T_2 = 1$, al aumentar $T_1$ se reduce $T_2$. El denominador de $r_2 / T_2$ se achica, de modo que $\rho_2$ *aumenta*. La opción que recibe menos tiempo se vuelve más rentable por visita.

Ambos efectos empujan $\Delta = \rho_1 - \rho_2$ hacia cero: el primer término cae, el segundo sube. El organismo que sigue la regla de mejoramiento activa automáticamente un mecanismo de corrección: al moverse hacia la opción más rentable, erosiona su propia ventaja y eleva la rentabilidad de la opción que está dejando. El sistema se regula a sí mismo.

Este argumento es simétrico: en el caso en que $\Delta < 0$, el organismo aumenta $T_2$, lo que reduce $\rho_2$ y eleva $\rho_1$, volviendo a empujar $\Delta$ hacia cero. En cualquier dirección que se encuentre el desequilibrio, el movimiento lo corrige.

#### Un único punto de equilibrio

¿Cuántos puntos de equilibrio tiene este sistema? La respuesta emerge de observar cómo se comportan $\rho_1$ y $\rho_2$ como funciones de $T_1$.

Conforme $T_1$ crece de 0 a 1, la tasa local $\rho_1 = r_1 / T_1$ decrece sin parar: empieza en valores muy altos (cuando $T_1$ es casi cero) y llega a $r_1$ (cuando $T_1 = 1$). La tasa local $\rho_2 = r_2 / (1 - T_1)$ hace exactamente lo contrario: empieza en $r_2$ (cuando $T_1$ es casi cero) y crece sin límite conforme $T_1$ se acerca a 1. Una función estrictamente decreciente y una estrictamente creciente se cruzan exactamente una vez. Ese cruce es el único equilibrio del sistema.

En ese cruce, $\rho_1 = \rho_2$, es decir:

$$\frac{r_1}{T_1^*} = \frac{r_2}{T_2^*}$$

Reorganizando:

$$\frac{T_1^*}{T_2^*} = \frac{r_1}{r_2}$$

Que es la ley de igualación. El único punto donde el sistema deja de moverse es, por construcción aritmética, el punto de igualación.

#### La iteración como ascenso de colina

La tabla siguiente muestra el proceso de convergencia para el ejemplo IV 1'–IV 2' de una hora, partiendo de $T_1 = 0.50$:

| $n$ | $T_1$ | $\rho_1$ | $\rho_2$ | $\Delta = \rho_1 - \rho_2$ | Movimiento |
|----:|------:|---------:|---------:|---------------------------:|:----------:|
| 0 | 0.500 | 120.0 | 60.0 | +60.0 | → más $T_1$ |
| 1 | 0.620 |  96.8 | 78.9 | +17.8 | → más $T_1$ |
| 2 | 0.656 |  91.5 | 87.1 |  +4.4 | → más $T_1$ |
| 3 | 0.664 |  90.3 | 89.4 |  +0.9 | → más $T_1$ |
| 4 | 0.666 |  90.1 | 89.9 |  +0.2 | → más $T_1$ |
| 5 | 0.667 |  90.0 | 90.0 |  ≈ 0 | equilibrio |

Pueden observarse en la tabla los mismos dos fenómenos que describimos cualitativamente. Conforme $T_1$ crece, $\rho_1$ cae de 120 a 90 y $\rho_2$ sube de 60 a 90: los dos efectos simultáneos que reducen $\Delta$. Y $\Delta$ decrece de 60 a casi cero en cinco pasos, cada uno más pequeño que el anterior, hasta que el sistema se detiene en el único punto donde no hay incentivo para seguir moviéndose.

Esta secuencia es idéntica, en su lógica, al ascenso de colina que describimos en el capítulo 4. Allí, la bacteria comparaba la concentración actual con la anterior y se movía en la dirección del gradiente; aquí, el organismo compara las tasas locales de dos opciones y se mueve hacia la más rentable. En ambos casos, el movimiento sigue la dirección de una señal de discrepancia, y esa señal disminuye con cada paso. La cima de la colina que el mejoramiento escala es el punto donde la discrepancia desaparece, y ese punto resulta ser algebraicamente idéntico al punto de igualación.

**[FIGURA 15.5: Dos paneles con el mismo eje horizontal (pasos de iteración, $n = 0$ a $5$). Panel superior: las dos tasas locales $\rho_1$ y $\rho_2$ como funciones de $n$. $\rho_1$ comienza alta y decrece; $\rho_2$ comienza baja y crece; las dos curvas se cruzan en el paso 5 en $\rho = 90$. Panel inferior: la discrepancia $\Delta = \rho_1 - \rho_2$ como función de $n$. Parte en 60 y converge a 0, mostrando la reducción monótona del error. Paleta del libro: azul para $\rho_1$, gris para $\rho_2$, naranja para $\Delta$.]**
