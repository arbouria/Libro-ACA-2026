# ## # Sistemas de Retroalimentación: El Robot con Visión Estéreo
*"El comportamiento inteligente es, en esencia, la reducción continua de la discrepancia entre dónde estás y dónde quieres estar."*
En el capítulo anterior, dejamos a nuestro robot (o bacteria) navegando con un solo sensor. Su vida era dura: tenía que moverse, equivocarse y retroceder para saber si iba por buen camino. Era una comparación **sucesiva** (Tiempo $t$ vs. Tiempo $t-1$).
Pero la evolución no se detuvo ahí. Dio un salto de ingeniería monumental: **La Simetría Bilateral**.
¿Qué pasa si le damos al robot **dos sensores** (dos ojos, dos oídos, dos fosas nasales) separados por una pequeña distancia? Ahora el robot no necesita moverse para saber la dirección de la señal. Puede hacer una comparación **simultánea** en el espacio.
Bienvenidos al mundo de las **Taxias** y la **Teoría de Control**.
# 1\. El Problema: Orientación Eficiente
Volvamos al análisis de Marr.
* **La Meta:** Alinear el cuerpo hacia una fuente de estimulación (luz, olor, sonido).
* **La Restricción:** Queremos hacerlo *rápido* y sin gastar energía nadando en la dirección equivocada (como hacía la bacteria con sus maromas aleatorias).
* **La Solución:** Usar la diferencia de intensidad entre dos puntos para calcular el giro exacto.

⠀2. La Solución Biológica: Tropotaxias
Imaginemos una polilla volando hacia un foco, o un robot simple de dos ruedas con dos sensores de luz frontales ($Ojo_{Izquierdo}$ y $Ojo_{Derecho}$).
El algoritmo, conocido en biología como **Tropotaxia**, es elegantemente simple:
1. **Medir:** El sistema lee la intensidad en ambos sensores al mismo tiempo.
2. **Comparar:** Calcula la diferencia ($\Delta = Ojo_{Izquierdo} - Ojo_{Derecho}$).
3. **Actuar:**
   * Si $Ojo_{Izquierdo} > Ojo_{Derecho}$: La luz viene de la izquierda. **Gira a la Izquierda.**
   * Si $Ojo_{Derecho} > Ojo_{Izquierdo}$: La luz viene de la derecha. **Gira a la Derecha.**
   * Si $Ojo_{Izquierdo} == Ojo_{Derecho}$: La luz está justo enfrente. **Sigue Recto.**

⠀A diferencia del ascenso de colina, aquí no hay azar. El movimiento es determinista y fluido. El robot parece "atraído" por la luz como si hubiera una cuerda invisible.
# 3\. El Nivel Algorítmico: El Bucle de Retroalimentación Negativa
Lo que acabamos de describir es el concepto más importante en la historia de la ingeniería: el **Feedback Loop** (Bucle de Retroalimentación).
Todo sistema de control, desde el termostato de tu casa hasta el sistema que mantiene tu cuerpo a 36.5°C (homeostasis), funciona con este diagrama:
1. **El Estado Deseado (Set Point):** ¿Qué queremos? (Ej. Mirar directo a la luz. Ángulo de error = 0).
2. **El Estado Actual:** ¿Qué tenemos? (Ej. Estoy mirando 30° a la derecha).
3. **La Señal de Error:** La discrepancia ($Meta - Actual$).
4. **El Controlador:** Convierte el error en acción. "Si el error es -30°, gira las ruedas a la izquierda con fuerza $X$".

⠀Se llama **Retroalimentación Negativa** porque la acción del sistema busca *restar* o *negar* el error. Si hace calor, el aire acondicionado enfría. Si me desvío a la derecha, giro a la izquierda.
# 4\. Formalización Matemática: La Función de Control
Podemos modelar este comportamiento con una ecuación lineal simple. Sea $\omega$ la velocidad de giro (qué tan rápido damos la vuelta):
$$\omega = k (S_{izq} - S_{der})$$
Donde:
* $(S_{izq} - S_{der})$ es la **Señal de Error**.
* $k$ es la **Ganancia** del sistema.

⠀¿Qué es la Ganancia ($k$)?
Es la "personalidad" del robot.
* **Ganancia Alta:** El robot es nervioso. Ante una pequeña diferencia de luz, da un giro brusco. Llega rápido a la meta, pero puede oscilar (pasarse de largo y tener que corregir).
* **Ganancia Baja:** El robot es perezoso. Gira muy lentamente. Es estable, pero tarda mucho en orientarse.

⠀::: {.callout-note}
# Conexión Clínica
Piensa en una persona tratando de mantener el equilibrio (homeostasis emocional).
Una "ganancia excesiva" podría parecerse a la ansiedad o labilidad emocional: reacciones exageradas ante pequeños errores ("pequeñas desviaciones"). Una "ganancia muy baja" podría parecerse a la depresión o apatía: incapacidad para corregir el rumbo ante problemas graves.
:::
# 5\. Limitaciones: La Tiranía del Presente
Los sistemas de retroalimentación son fantásticos, pero tienen un defecto fundamental que justifica el resto de este curso:
**Son puramente reactivos.**
Para que el sistema de retroalimentación actúe, **primero tiene que haber un error**.
* El termostato no enciende *antes* de que haga frío. Enciende *porque* ya hace frío.
* La polilla no gira *antes* de desviarse. Gira *porque* ya se desvió.

⠀El robot de retroalimentación vive esclavizado en el presente. No puede anticipar. Si la luz se mueve detrás de un obstáculo, el robot se detiene o choca.
Para sobrevivir en un mundo complejo, no basta con corregir errores; hay que **prevenirlos**. Necesitamos un robot que pueda decir: *"Escuché un tono, y eso significa que en 5 segundos aparecerá comida/luz"*.
Eso nos lleva a nuestro siguiente gran salto evolutivo: **El Aprendizaje Predictivo (Pavlov y Rescorla-Wagner)**.


