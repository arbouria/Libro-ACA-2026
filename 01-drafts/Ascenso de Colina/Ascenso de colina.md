# ## # Ascenso de Colina: Navegación en la Oscuridad
*"Si no puedes ver la cima, al menos asegúrate de que tu próximo paso te lleve más arriba."*
En el capítulo anterior, definimos que nuestro objetivo es construir modelos. Ahora, pondremos manos a la obra con el problema más básico que enfrenta cualquier organismo: **La Navegación**.
Imaginemos a nuestro robot (o a un organismo primitivo) con una restricción severa: **Está ciego.** No tiene cámaras, ni ojos, ni nariz que le diga "la comida está a 10 metros a la derecha". Solo tiene un sensor que le dice cómo se siente *aquí y ahora*.
¿Cómo puede este agente ciego encontrar la fuente de energía sin morir de hambre vagando al azar?
# 1\. El Nivel Computacional: El Montañista Ciego
Definamos el problema usando la estrategia de Marr:
* **La Meta:** Maximizar el acceso a un recurso (comida, calor, luz). Imaginemos esto como llegar a la cima de una montaña de "comida".
* **El Entorno:** Un gradiente de concentración. Hay más comida en el centro y menos en la periferia.
* **La Restricción:** El agente es **puntual**. Solo percibe la concentración en su ubicación actual $(x, y)$. No puede ver a distancia (no hay percepción distal).

⠀Este problema es idéntico al de un montañista perdido en el Ajusco en una noche de niebla espesa. Quiere llegar a la cima, pero solo puede sentir la inclinación bajo sus pies.
# 2\. La Solución Biológica: Kinesis y Bacterias
La naturaleza resolvió este problema hace millones de años. El ejemplo clásico no es un animal complejo, sino organismos unicelulares como la *Salmonella* o la *E. coli* (y funcionalmente similar a como se comportan ciertas amebas).
Si observamos a una bacteria en el microscopio, su comportamiento parece errático, casi "borracho". A esto se le llama **Kinesis** (movimiento sin orientación direccional).
1. **Nado Recto:** La bacteria avanza en línea recta.
2. **Tumble (Maroma):** De repente, se detiene, gira al azar y sale disparada en otra dirección.

⠀La Demostración Empírica:
Si ponemos a la bacteria en agua pura, los nados y las maromas son aleatorios. La bacteria no va a ningún lado (se difunde).
Pero si ponemos una gota de azúcar en un extremo, algo cambia. La bacteria sigue nadando y dando maromas, pero —y esto es clave— los nados son más largos cuando se acerca al azúcar y las maromas son más frecuentes cuando se aleja.
El resultado macroscópico: La bacteria "trepa" el gradiente de azúcar. No es una búsqueda aleatoria; es una **caminata aleatoria sesgada** (Biased Random Walk).
# 3\. El Nivel Algorítmico: Detectando el Cambio
¿Cómo sabe la bacteria que se está acercando si no puede ver la meta?
La respuesta es la Memoria. La bacteria no compara el espacio (izquierda vs. derecha), compara el tiempo (Ahora vs. Hace un momento).
El algoritmo de Ascenso de Colina (Hill Climbing) funciona así:
1. **Muestrear:** Medir la concentración actual ($X_t$).
2. **Comparar:** ¿Es $X_t$ mayor que la medición anterior ($X_{t-1}$)?
   * Calculamos el cambio: $\Delta X = X_t - X_{t-1}$.
3. **Decidir (Regla de Acción):**
   * **Si $\Delta X > 0$ (Mejoró):** ¡Sigue así! Suprime la maroma y sigue nadando recto. (**Explotación**).
   * **Si $\Delta X < 0$ (Empeoró):** ¡Error! Detente, da una maroma y prueba una dirección nueva al azar. (**Exploración**).

⠀Este mecanismo transforma el tiempo en espacio. La bacteria "infiere" la dirección correcta basándose en si la vida está mejorando o empeorando paso a paso.
# 4\. El Modelo Matemático: Dinámica de Sistemas
Podemos formalizar este algoritmo verbal en un sistema de ecuaciones dinámicas. Este es nuestro primer "modelo de juguete" del curso.
Definimos $Y_t$ como el estado interno del agente (su "nivel de activación" para dar una maroma).
$$Y_{t+1} = a Y_t + b(X_{t+1} - X_t)$$
Desglosemos la ecuación:
* $X_{t+1} - X_t$: Es el **Detector de Cambio** (la derivada discreta). Es el motor del sistema. Si el entorno no cambia, este término es cero.
* $b$: Es la **Ganancia** (sensibilidad). Qué tanto le importa el cambio al organismo.
* $a Y_t$: Es la **Memoria** (o inercia). El estado actual depende del estado anterior, ponderado por un factor de decaimiento $a$.

⠀La Regla de Decisión (Umbral):
Para conectar esto con la conducta observable (nadar vs. girar), añadimos una regla de salida:
* Si $Y_{t+1} > \text{Umbral}$ $\rightarrow$ **Nadar Recto** (Suprimir maroma).
* Si $Y_{t+1} < \text{Umbral}$ $\rightarrow$ **Girar** (Iniciar maroma).

⠀Esta ecuación simple captura la esencia de la adaptación reactiva: el comportamiento es función de la historia inmediata de cambios en el entorno.
# 5\. Una Herramienta Conceptual: Exploración vs. Explotación
Este humilde algoritmo nos introduce al dilema más fundamental del comportamiento adaptable, uno que reaparecerá cuando estudiemos Inteligencia Artificial y Economía:
**El Dilema de Exploración - Explotación.**
* **Explotación (Nado Recto):** Aprovechar lo que sabes que funciona. "Si estoy subiendo la colina, sigo caminando en esta dirección". Es eficiente, pero arriesgado si la colina se acaba.
* **Exploración (Maroma):** Probar algo nuevo y desconocido. "Si estoy bajando, giro al azar". Es costoso (puedo girar hacia un lugar peor), pero es la única forma de descubrir nuevas oportunidades.

⠀El peligro de los Máximos Locales:
El algoritmo de Ascenso de Colina tiene un defecto fatal. Si el montañista ciego llega a una pequeña loma (un máximo local), pensará que está en la cima del Everest. Cualquier paso que dé lo llevará hacia abajo, así que se quedará ahí atrapado.
Para escapar de los máximos locales, los organismos (y los algoritmos avanzados) necesitan un poco de "ruido" o aleatoriedad constante. Necesitan seguir explorando un poco, incluso cuando creen que ya ganaron.

### Conclusión del Capítulo
El Ascenso de Colina demuestra que no se necesita un cerebro complejo para parecer inteligente. Con un sensor, una memoria de corto plazo y un comparador, un organismo puede resolver problemas vitales de navegación.
Sin embargo, este método es lento y peligroso (requiere moverse para saber si te equivocaste). ¿Qué pasaría si tuviéramos **dos sensores** en lugar de uno? Eso nos lleva al siguiente nivel de sofisticación: **Los Sistemas de Retroalimentación (Taxias).**





