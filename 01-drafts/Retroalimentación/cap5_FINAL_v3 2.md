
# Capítulo 5: Algoritmos de Comparación Simultánea  y Sistemas de Retroalimentación
## El caso de las Taxias

*"El comportamiento inteligente es, en esencia, la reducción continua de la discrepancia entre dónde estás y dónde quieres estar."*

En el capítulo anterior dejamos a nuestra bacteria navegando con un solo sensor. Su vida era difícil: tenía que moverse, esperar, comparar el presente con el pasado inmediato, y ajustar su comportamiento en consecuencia. Esa estrategia—comparar *ahora* con *hace un momento* en el mismo lugar—es lo que llamamos comparación sucesiva, y es el principio detrás del ascenso de colina.

Pero la evolución no se detuvo ahí. La aparición de la simetría bilateral en los animales representó un salto de ingeniería radical: en lugar de un sensor que se mueve para comparar el mundo en distintos tiempos, el organismo dispone ahora de dos sensores separados que comparan el mundo en distintos lugares *al mismo tiempo*. Con este arreglo, la dirección de la fuente queda codificada directamente en la diferencia entre lo que detecta el lado izquierdo y lo que detecta el lado derecho, sin necesidad de moverse primero para saberlo.

Este capítulo introduce el mecanismo que hace posible esa hazaña: los **sistemas de retroalimentación**. Son la segunda "tuerca y tornillo" del repertorio de mecanismos adaptativos sin aprendizaje, y reaparecerán—en formas cada vez más sofisticadas—a lo largo del resto del libro. Al final del capítulo veremos también por qué estos sistemas, por elegantes que sean, tienen una limitación fundamental que justifica la existencia misma del aprendizaje: son completamente esclavos del presente, incapaces de anticipar lo que viene.


## 5.1 El Problema: Orientarse en el Espacio

Imagina a una polilla nocturna. En algún punto del espacio, a una distancia desconocida, hay una fuente de luz. No tiene mapa, no tiene distancia, no tiene brújula. Solo tiene lo que sus dos ojos detectan en este momento: dos intensidades luminosas, una para cada lado de su cuerpo. El problema adaptativo es claro: ¿cómo usas esa información mínima para orientar tu cuerpo hacia la fuente?

Nota que esto es un problema diferente al que resolvía la bacteria. La bacteria no necesitaba saber *hacia dónde* está el nutriente—solo necesitaba saber si estaba mejorando o empeorando. Su solución era estadística: si la concentración mejora, sigue; si empeora, cambia de rumbo al azar. Eso funciona, pero es lento y sinuoso. La polilla, en cambio, puede extraer información *direccional* de sus dos receptores, lo que le permite orientarse directa y rápidamente hacia la fuente. Esta ganancia de eficiencia tiene un costo: requiere el hardware de la simetría bilateral, que es estructuralmente más complejo.

El mismo problema—localizar y orientarse hacia o alejándose de una fuente puntual de estimulación—aparece en múltiples modalidades sensoriales a lo largo del reino animal. La fototaxia de polillas y cucarachas, la quimiotaxia de insectos siguiendo plumas de feromonas, la fonotaxia de grillos hembra localizando machos que cantan, la termotaxia de serpientes detectando presas de sangre caliente: todos son casos del mismo problema computacional resuelto con el mismo principio básico. La diversidad es en el tipo de estímulo; el mecanismo subyacente es el mismo.

[FIGURA 1: Trayectorias de fototaxia positiva y negativa en un tubo (diapositiva 8 de la presentación). El organismo en el centro mueve hacia la fuente de luz (positiva, izquierda) o se aleja de ella (negativa, derecha), mostrando el patrón de espiral en ambos casos.]


## 5.2 La Solución: Comparación Simultánea

Considera el caso más simple: un robot pequeño con dos ruedas y dos sensores de luz, uno en el lado izquierdo y uno en el derecho. La regla de comportamiento puede ser tan simple como ésta: si el sensor izquierdo detecta más luz que el derecho, gira a la izquierda; si el sensor derecho detecta más, gira a la derecha; si ambos detectan igual, sigue recto. Este mecanismo—conocido en biología como **tropotaxia**—es la solución más elegante posible al problema de orientación: la dirección del error queda codificada directamente en el signo de la diferencia entre sensores.

La elegancia se vuelve evidente cuando se compara con la alternativa de un solo sensor. Un organismo con un solo ojo compuesto necesita moverse para comparar el presente con el pasado; un organismo con dos ojos compuestos no necesita moverse en absoluto para saber en qué dirección está la fuente. La información está disponible instantáneamente, en el espacio, sin costo de movimiento.

Un experimento clásico ilustra el punto con claridad sorprendente: si se cubre uno de los ojos compuestos de una polilla con pintura opaca, el comportamiento cambia radicalmente. En lugar de aproximarse a la fuente de luz en espiral, la polilla vuela en círculos continuos. La explicación es directa: con solo un ojo funcional, la comparación siempre favorece ese lado; la señal de "gira hacia la izquierda" (o derecha) nunca se cancela porque no hay información desde el lado opuesto. El resultado es un giro continuo, sin orientación. Este experimento—y su variante con cucarachas, donde el giro continuo va en la dirección opuesta al ojo descubierto, porque la cucaracha huye de la luz en lugar de aproximarse—es evidencia directa de que el comportamiento normal depende de la *diferencia* entre sensores, no del nivel absoluto de estimulación en ninguno de ellos.

Otro experimento particularmente revelador usa dos fuentes de luz de igual intensidad colocadas a igual distancia del organismo. Si la conducta está controlada por la diferencia bilateral, la predicción es que el animal debería moverse en línea recta entre ambas fuentes—porque mientras estén equidistantes, ambos ojos reciben la misma estimulación, la diferencia es cero, y no hay señal de giro. Eso es exactamente lo que ocurre. Solo cuando la proximidad a una de las fuentes rompe la simetría el animal gira bruscamente. Difícilmente podría diseñarse un experimento más limpio para demostrar que el controlador es la disparidad, no la intensidad absoluta.

[FIGURA 2: Trayectorias de cochinilla con dos fuentes equidistantes (diapositiva 11 de la presentación). Las trayectorias reales muestran el movimiento en línea recta entre fuentes y el brusco cambio de dirección al acercarse a una de ellas.]


## 5.3 El Mecanismo General: El Sistema de Retroalimentación

Lo que acabamos de describir es un ejemplo de un mecanismo mucho más general, ubicuo en la biología y la ingeniería: el **sistema de retroalimentación** (o *feedback loop*). Vale la pena entender su estructura abstracta, porque la misma arquitectura reaparecerá docenas de veces en el resto del curso, desde la regulación de glucosa en sangre hasta los modelos computacionales del condicionamiento.

Estamos acostumbrados a pensar en la relación organismo-entorno como unidireccional: el entorno produce un estímulo, el organismo produce una respuesta. Pero esta imagen es incompleta en la mayoría de los casos conductualmente interesantes, porque la respuesta del organismo modifica el entorno, lo cual modifica el estímulo que controla la respuesta. La temperatura alta produce sudoración, la sudoración reduce la temperatura, la temperatura reducida disminuye la sudoración. El bebé recién nacido succiona, la succión extrae leche y —crucialmente— la tasa de succión estimula la producción de leche por parte de la madre, de modo que el comportamiento del bebé modifica una variable del entorno externo (la disponibilidad de leche) que a su vez controla ese mismo comportamiento. En todos estos casos, la causalidad no va de A a B sino que forma un lazo cerrado donde A y B se codeterminan mutuamente.

Formalmente, un sistema de retroalimentación está definido por **dos ecuaciones simultáneas**. La primera es la *función de control* o función del organismo:

**C = G(X)**

Esta ecuación describe cómo el organismo transforma una propiedad del entorno (X, el estímulo que controla el comportamiento) en una respuesta (C, el comportamiento). En fototaxia: C es la tasa de giro, X es la disparidad bilateral entre los dos ojos.

La segunda ecuación es la *función de retroalimentación* o función del entorno:

**X = E(C)**

Esta ecuación describe cómo el comportamiento modifica la propiedad del entorno. En fototaxia: el giro (C) modifica el ángulo entre el organismo y la fuente, lo que modifica la disparidad bilateral (X).

Nótese que las dos ecuaciones están acopladas: C depende de X, pero X depende de C. No son independientes—lo que hace que el sistema sea interesante y que su análisis requiera herramientas distintas a las de las funciones simples.

[FIGURA 3a: Diagrama clásico O(x)/E(y): dos cajas en lazo cerrado, "Controlling stimulus (x)" entrando a la caja del Organismo O(x), cuya salida "Response (y)" entra a la caja del Entorno E(y), cuya salida vuelve como x. Diapositiva 19 de la presentación.]

En la implementación biológica concreta, el lazo tiene cuatro componentes reconocibles. El **sensor** mide el estado actual de la variable relevante—los ojos compuestos de la mariposa que detectan intensidad luminosa bilateral. El **comparador** calcula la discrepancia entre el estado actual y el estado deseado: el circuito neural que resta la activación de un ojo de la del otro, produciendo la *señal de error*. El **controlador** transforma esa señal de error en una acción—la regla que convierte la disparidad bilateral en una tasa de giro. El **efector** ejecuta la acción—los músculos de las alas que producen el giro—y al hacerlo modifica el ángulo entre el organismo y la fuente, cerrando el lazo.

[FIGURA 3b: Diagrama moderno con Desired Output → Comparator → Error signal → Effectors (calefactor/AC) → Output, con Sensor + Feedback signal completando el lazo. Diapositiva 25 de la presentación.]

[FIGURA 3c: Diagrama de la mariposa: Set point (45°) → Comparador (E_Angle) → Controller (Flying Decision-making circuit) → Actor (Wing) → Flying, con Sensor (Compound eyes) + señal de Angle completando el lazo. Diapositiva 28 de la presentación.]

Esto contrasta con los *sistemas abiertos*, donde el comportamiento responde al entorno pero no modifica la variable que lo controla. Un calefactor encendido permanentemente sin importar la temperatura del cuarto es un sistema abierto. La respuesta de una planta que cierra sus hojas ante la vibración es un sistema abierto: el cierre de las hojas no cambia las vibraciones del entorno. El lengüetazo de una rana capturando una mosca es otro ejemplo clásico: una vez iniciado, el movimiento se ejecuta hasta completarse sin corrección durante su trayectoria. Y, crucialmente, cubrir un ojo en el experimento de tropotaxia transforma al organismo en un sistema abierto: la comparación siempre favorece el mismo lado, el giro nunca recibe señal de corrección, y el resultado es rotación indefinida.

Se habla de **retroalimentación negativa** cuando el comportamiento tiende a *reducir* la señal de error—cuando la acción del sistema contrarresta la desviación que la provocó. El nombre puede sonar paradójico ("negativa" no connota algo malo), pero refleja la matemática: la acción tiene signo opuesto al error. La termorregulación es el ejemplo paradigmático: si la temperatura corporal sube, el organismo transpira y dilata vasos periféricos; si baja, tirita y contrae vasos. El comportamiento *niega* la desviación, de ahí el nombre.

Existe también la **retroalimentación positiva**, donde el comportamiento *amplifica* la señal de error en lugar de reducirla. La apertura de canales de sodio durante un potencial de acción neuronal es el ejemplo canónico: la entrada de iones positivos despolariza la membrana, lo que abre más canales, en una cascada que solo se detiene cuando todos los canales están abiertos. Las contracciones durante el parto siguen la misma lógica. La retroalimentación positiva es útil para producir transiciones rápidas y decisivas entre estados, pero es inherentemente inestable y no puede servir como mecanismo de orientación.

Vale la pena detenerse un momento a notar que en este capítulo, igual que en el anterior, hemos aplicado sin nombrarlo el análisis de tres niveles que introdujo el Cap. 1. El nivel computacional es el problema adaptativo: orientarse hacia una fuente de estimulación de forma rápida y robusta. El nivel algorítmico es el mecanismo: comparación simultánea de dos receptores bilaterales, cálculo de una señal de error, y función de control que transforma ese error en una tasa de giro. El nivel de implementación —los circuitos neurales específicos, los fotorreceptores, los músculos— varía entre especies y no necesitamos especificarlo para entender cómo funciona el sistema. Esta separación de niveles no es solo un ejercicio filosófico: es lo que nos permite reconocer que una polilla, un robot de dos ruedas y un sistema de climatización doméstico comparten la misma arquitectura algorítmica aunque sus implementaciones físicas no tengan nada en común.


## 5.4 La Formalización: Ganancia, Dinámica y las Cuatro Preguntas

Ante cualquier sistema de retroalimentación concreto, conviene hacerse las mismas cuatro preguntas en orden. Primero: ¿tiene el sistema un equilibrio? Segundo: ¿cuál es ese equilibrio? Tercero: ¿cómo llega el sistema al equilibrio—cuál es su dinámica? Cuarto: ¿cómo responde ante una perturbación abrupta? Estas preguntas estructuran el análisis tanto del sistema de fototaxia más simple como del mecanismo de homeostasis más complejo, y las encontraremos repetidas en forma más sofisticada cuando lleguemos a los modelos de aprendizaje.

Apliquémoslas al sistema de fototaxia. Para hacerlo concreto, necesitamos la función de control. Sea ω la *tasa de giro* del organismo, S_izq la estimulación que recibe el sensor izquierdo, y S_der la del sensor derecho. La función de control es:

**ω = k · (S_der − S_izq)**

La diferencia (S_der − S_izq) es la señal de error: codifica tanto la magnitud de la desviación como su dirección. Si S_der > S_izq, la fuente está a la derecha, el error es positivo, y ω es positivo (giro a la derecha). Si S_izq > S_der, la fuente está a la izquierda, el error es negativo, y ω es negativo (giro a la izquierda). Si ambas son iguales, el error es cero y el organismo sigue recto.

El parámetro **k** es la *ganancia* del sistema, y puede interpretarse de manera intuitiva como **qué tan importante es para el organismo una diferencia dada entre sus sensores**. Un k alto significa que diferencias pequeñas en estimulación producen giros grandes: la disparidad bilateral tiene mucho peso en el control del comportamiento. Un k bajo significa que se necesitan diferencias grandes para producir giros apreciables: el organismo es relativamente insensible a disparidades pequeñas. Esta interpretación —la ganancia como peso o importancia de una señal de discrepancia— reaparecerá en formas más sofisticadas en capítulos posteriores, cuando veamos cómo el aprendizaje modifica qué tanto le "importa" a un organismo la diferencia entre lo que predijo y lo que ocurrió.

En fototaxia positiva (aproximación a la fuente), k > 0. En fototaxia negativa (como la cucaracha huyendo de la luz), k < 0: ante más luz en el lado derecho, el organismo gira hacia la *izquierda*, alejándose. El signo de k define si el sistema busca o evita la fuente.

**Primera pregunta: ¿tiene equilibrio?** Sí. El equilibrio ocurre cuando ω = 0, es decir, cuando la señal de error es cero.

**Segunda pregunta: ¿cuál es el equilibrio?** La señal de error es cero cuando S_der = S_izq, lo que ocurre cuando el organismo apunta directamente hacia la fuente (ángulo θ = 0°). Hay un segundo equilibrio matemático en θ = 180° (apuntando directamente en sentido opuesto), pero es inestable: cualquier perturbación mínima empuja al sistema lejos de ese punto y lo lleva hacia θ = 0°. El equilibrio adaptativo —orientado hacia la fuente— es el único estable.

**Tercera pregunta: ¿cuál es la dinámica?** Aquí está el punto pedagógicamente más importante, y se puede entender sin cálculo diferencial. La señal de error—la disparidad bilateral—es mayor cuando el ángulo θ es grande (estás muy desviado de la fuente), y más pequeña cuando θ es pequeño (ya casi estás orientado correctamente). Esto significa que el giro correctivo es grande cuando más lo necesitas y se va volviendo cada vez más sutil conforme te acercas al equilibrio. El sistema nunca se "detiene en seco" —el giro simplemente se va haciendo imperceptiblemente pequeño. Esta convergencia que se desacelera al acercarse al equilibrio produce el patrón de trayectoria observado en los experimentos: no una línea recta, sino una **espiral que se cierra progresivamente** hacia la fuente. Cuanto mayor el ángulo inicial, mayor la curvatura; cuanto más cercano al equilibrio, más recta la trayectoria.

[FIGURA 4a: Trayectorias reales de polillas en experimento (diapositiva 16/30 de la presentación). Panel (a): trayectoria circular cuando hay un solo ojo funcional (fiber optic bundle). Panel (b): trayectoria en zigzag de aproximación. Estos son datos reales, no ilustraciones.]

[FIGURA 4b: Gráfica de Transitorio vs. Estado Estacionario (diapositiva 37 de la presentación). Muestra comportamiento (eje vertical) vs. tiempo (eje horizontal): fase transitoria de ajuste seguida de estado estacionario (steady state), luego perturbación y nuevo transitorio.]

La distinción entre **transitorio** y **estado estacionario** es importante. El transitorio es el período de ajuste desde las condiciones iniciales hasta el equilibrio—la espiral de aproximación. El estado estacionario es el comportamiento una vez alcanzado el equilibrio—el organismo orientado hacia la fuente. Cuando ocurre una perturbación (una ráfaga de viento que desvía a la polilla), el sistema entra en un nuevo transitorio que lo lleva de vuelta al estado estacionario. La capacidad de recuperarse de perturbaciones —robustez— es una de las ventajas fundamentales de los sistemas de retroalimentación negativa.

**Cuarta pregunta: ¿cómo responde ante perturbación?** Una polilla volando hacia una fuente de luz con θ ≈ 0° recibe una ráfaga de viento que la desvía a θ = 30°. Sin retroalimentación, continuaría en esa dirección desviada indefinidamente. Con retroalimentación: el nuevo ángulo genera nueva disparidad bilateral, nueva señal de error, nuevo giro correctivo, y la polilla vuelve al equilibrio. La perturbación es compensada sin ninguna "decisión" explícita, simplemente por la estructura del lazo. Una ventaja adicional de esta arquitectura es que la robustez es **independiente de la ganancia k**: tanto un organismo joven con músculos débiles (k pequeño) como uno adulto con músculos fuertes (k grande) alcanzarán θ = 0°, solo que a velocidades distintas.

[FIGURA 5: Trayectorias con ojo cubierto (diapositiva 13 de la presentación). Filas: oscuridad, luz arriba, haz de luz. Columnas: ojo izquierdo ciego vs. ojo derecho ciego. Muestra que la dirección del giro continuo depende de qué ojo está disponible, evidencia directa del mecanismo bilateral.]

---

> **[SIMULADOR 1 — Fototaxia básica]**
> 
> El siguiente código para Google Colab simula un robot de dos ruedas con dos sensores de luz que se aproxima a una fuente puntual. Puedes modificar la ganancia k y el ángulo inicial para explorar cómo cambia la trayectoria.
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> 
> def simular_fototaxia(theta0_deg, k=1.0, dt=0.05, T=15):
>     """
>     theta: ángulo entre organismo y fuente (grados)
>     k: ganancia del sistema (k>0 = fototaxia positiva)
>     """
>     theta = np.radians(theta0_deg)
>     thetas = [theta]
>     t = 0
>     times = [0]
>     
>     while t < T:
>         # Señal de error (proporcional a sin(theta) para fuente a distancia constante)
>         error = np.sin(theta)
>         # Función de control
>         omega = k * error
>         # Actualización del ángulo
>         theta = theta - omega * dt
>         t += dt
>         thetas.append(np.degrees(theta))
>         times.append(t)
>     
>     plt.figure(figsize=(8, 4))
>     plt.plot(times, thetas)
>     plt.axhline(0, color='r', linestyle='--', label='equilibrio (θ=0°)')
>     plt.xlabel('Tiempo')
>     plt.ylabel('Ángulo θ (grados)')
>     plt.title(f'Convergencia hacia la fuente (k={k}, θ₀={theta0_deg}°)')
>     plt.legend()
>     plt.grid(True)
>     plt.show()
>     return thetas
> 
> # Prueba con distintas ganancias
> for k_val in [0.3, 1.0, 3.0]:
>     simular_fototaxia(theta0_deg=75, k=k_val)
> ```

---


## 5.5 Regulación y Servomecanismos

Hasta aquí hemos hablado de fototaxia como si el set point (el "estado deseado") fuera siempre el mismo: ángulo cero, fuente al frente. Pero hay una distinción útil entre dos clases de sistemas de retroalimentación que aparecen con frecuencia en biología y que corresponden a problemas adaptativos diferentes.

En los sistemas de **regulación**, el set point es interno al organismo y permanece relativamente fijo: la temperatura corporal de un mamífero (≈37°C), la concentración de glucosa en sangre, el pH de los fluidos internos. El propósito de estos sistemas es mantener una variable fisiológica dentro de un rango estrecho a pesar de perturbaciones externas. El entorno cambia—hace calor, hace frío, comes mucho o poco—pero el organismo corrige continuamente para mantener su estado interno estable. Este tipo de regulación es lo que Cannon llamó homeostasis, y es una de las características más notables de los organismos de sangre caliente.

Los sistemas de **servomecanismo**, en cambio, tienen un set point externo y variable: lo que el sistema persigue cambia de posición en el tiempo. La fototaxia es un servomecanismo cuando la fuente de luz se mueve: el sistema no persigue un ángulo fijo abstracto, sino la posición real de una fuente que puede desplazarse. Un misil teledirigido es el ejemplo tecnológico paradigmático—no persigue un punto fijo en el espacio, sino un avión que se mueve. Los sistemas de seguimiento ocular (cómo tus ojos rastrean un objeto en movimiento) son servomecanismos biológicos sofisticados.

La diferencia importa porque tiene implicaciones sobre las limitaciones de cada tipo de sistema. Un sistema de regulación puede fallar si la perturbación excede su capacidad correctiva (fiebre muy alta, hipotermia severa). Un servomecanismo puede fallar si el objetivo se mueve más rápido de lo que el sistema puede seguir—hay un límite de velocidad de seguimiento, llamado ancho de banda, más allá del cual el sistema pierde el objetivo.


## 5.6 La Limitación Fundamental: Esclavos del Presente

Los sistemas de retroalimentación son elegantes y poderosos, pero comparten con el ascenso de colina una limitación fundamental que no puede resolverse con más ganancia ni más sensores: son completamente **reactivos**. Para que actúen, primero tiene que haber un error. Y eso significa que siempre van un paso atrás.

El termostato no enciende *antes* de que la temperatura baje. Enciende *porque* ya bajó. La polilla no gira *antes* de desviarse de la fuente. Gira *porque* ya se desvió. El sistema de retroalimentación vive permanentemente en el presente, respondiendo a lo que ya ocurrió, incapaz de prepararse para lo que va a ocurrir.

La analogía de la regadera de agua caliente ilustra bien las consecuencias de esta reactividad. Si hay una demora significativa entre el momento en que giras la perilla y el momento en que sientes el cambio de temperatura en el agua, tiendes a sobrecompensar: "¡demasiado fría!" [giras mucho hacia caliente] "¡ahora demasiado caliente!" [giras mucho hacia fría] y así sucesivamente, oscilando alrededor de la temperatura deseada sin llegar a ella. El problema no es la falta de retroalimentación—hay retroalimentación perfectamente funcional. El problema es que la retroalimentación es tardía: para cuando llegas a la temperatura que querías, ya la información viajó de regreso y la corrección llegó a destiempo.

En entornos reales, las demoras son ubicuas. El sistema nervioso tarda en procesar información sensorial. Los músculos tardan en responder a señales motoras. El entorno tarda en cambiar en respuesta al comportamiento. Cada una de estas demoras puede desestabilizar un sistema de retroalimentación pura, convirtiendo la convergencia suave en oscilaciones indeseables. La evolución ha desarrollado múltiples estrategias para minimizar estas demoras—vías neurales rápidas, respuestas musculares anticipatorias—pero en última instancia ninguna elimina el problema por completo: la retroalimentación pura siempre reacciona después del hecho.

[FIGURA 5: Diagrama comparando comportamiento de sistema con demora pequeña (convergencia suave) vs. demora grande (oscilaciones). Puede generarse con Simulador 2.]

---

> **[SIMULADOR 2 — Efecto de la demora]**
> 
> Este simulador añade una demora al sistema de fototaxia para mostrar cómo produce oscilaciones.
> 
> ```python
> from collections import deque
> 
> def simular_con_demora(theta0_deg, k=1.0, delay_steps=5, dt=0.05, T=20):
>     """
>     delay_steps: número de pasos de tiempo de demora entre error y corrección
>     """
>     theta = np.radians(theta0_deg)
>     buffer_omega = deque([0.0] * delay_steps, maxlen=delay_steps)
>     thetas = [np.degrees(theta)]
>     t = 0
>     times = [0]
>     
>     while t < T:
>         error = np.sin(theta)
>         omega_actual = buffer_omega.popleft()
>         buffer_omega.append(k * error)
>         theta = theta - omega_actual * dt
>         t += dt
>         thetas.append(np.degrees(theta))
>         times.append(t)
>     
>     plt.figure(figsize=(8, 4))
>     plt.plot(times, thetas)
>     plt.axhline(0, color='r', linestyle='--', label='equilibrio')
>     plt.xlabel('Tiempo')
>     plt.ylabel('Ángulo θ (grados)')
>     plt.title(f'Con demora de {delay_steps} pasos (k={k})')
>     plt.legend()
>     plt.grid(True)
>     plt.show()
> 
> simular_con_demora(theta0_deg=75, k=1.0, delay_steps=0)   # sin demora
> simular_con_demora(theta0_deg=75, k=1.0, delay_steps=10)  # con demora
> ```

---


## 5.7 El Conductor y las Gasolineras: Por Qué el Mundo Requiere Anticipación

Considera ahora un problema diferente, más cotidiano, que lleva la limitación de la retroalimentación pura a su punto más claro.

Un conductor que viaja en carretera entre ciudades necesita recargar gasolina en algún punto del trayecto. En principio, podría resolver este problema con retroalimentación pura: cuando el tanque llegue a cero, detener el coche y buscar una gasolinera. El error (tanque vacío) dispara la respuesta (buscar gasolinera). Problema: para cuando el error se materializa, ya es demasiado tarde. En carretera abierta, el tanque vacío puede dejarte varado entre gasolineras.

Una estrategia apenas un poco mejor es fijar un umbral más alto: cuando el tanque llegue a la reserva (un cuarto), buscar gasolinera. Esto es retroalimentación mejorada, pero sigue siendo reactiva: espera a que el estado del sistema alcance un nivel de alerta antes de actuar. En una ciudad con gasolineras cada dos kilómetros, esa estrategia funciona. En carretera del norte de México, donde pueden pasar cien kilómetros entre gasolineras, puede no ser suficiente.

La solución real que adoptan los conductores experimentados es cualitativamente diferente: aprenden la *distribución espacial* de las gasolineras en su ruta habitual. Saben que en tal tramo hay gasolinera en el kilómetro 45, en el kilómetro 130, y en el kilómetro 210. Con ese conocimiento, el conductor carga gasolina *no cuando el tanque está bajo*, sino *antes de un tramo largo sin estaciones*. El comportamiento ya no responde al estado actual del tanque; responde a una predicción sobre necesidades futuras basada en conocimiento aprendido del entorno. Esto es anticipación, no reacción.

La diferencia entre el conductor novato y el experimentado no es una diferencia en el hardware del sistema de control—ambos tienen los mismos instrumentos en el tablero, el mismo tanque, los mismos pies. La diferencia es que el conductor experimentado ha aprendido relaciones en el mundo que le permiten predecir: "si no cargo aquí, más adelante habrá problemas". Ese aprendizaje—la adquisición de conocimiento sobre relaciones predictivas en el entorno—es precisamente lo que los sistemas de retroalimentación pura no pueden hacer.

A este tipo de control —donde el comportamiento se ajusta basándose en una predicción del estado futuro en lugar de en el error presente— se le llama control anticipatorio o feedforward. La distinción respecto a la retroalimentación (feedback) es precisa: en el feedback, la señal que controla el comportamiento es el error actual; en el feedforward, es una predicción del error futuro derivada de un modelo aprendido del entorno. El conductor experimentado opera en modo feedforward respecto a la gasolina: carga antes de que aparezca el error, porque ha aprendido que cierta señal presente predice una necesidad futura. Nótese que el feedforward no reemplaza a la retroalimentación —la complementa. Si una gasolinera esperada está cerrada, el conductor reactiva inmediatamente la estrategia reactiva. Los sistemas biológicos más robustos combinan ambos lazos: el feedback garantiza la corrección cuando algo sale mal; el feedforward evita que salga mal en primer lugar.

Y con eso llegamos al umbral del problema que ocupará el resto del libro.


## 5.8 De la Reactividad a la Predicción: El Puente Hacia el Aprendizaje

El capítulo anterior y este han explorado mecanismos adaptativos que funcionan sin aprendizaje: el ascenso de colina y la retroalimentación basada en comparación simultánea. Ambos son herramientas poderosas para problemas relativamente estables y locales. Pero ambos comparten la misma limitación: responden al mundo tal como es *ahora*, no al mundo tal como *será*.

Para sobrevivir en un mundo donde eventos pasados predicen eventos futuros, un organismo necesita algo más: necesita poder modificar su comportamiento basándose en experiencia acumulada. Necesita poder aprender que cierto estímulo predice cierta consecuencia, y ajustar su conducta *antes* de que la consecuencia llegue. En términos del conductor: necesita aprender que cierta señal en el entorno (kilómetro X, tipo de carretera) predice escasez de gasolineras adelante, y actuar en consecuencia.

Esto es el condicionamiento asociativo, y es el tema central del resto del libro. Los mecanismos que veremos—condicionamiento Pavloviano, aprendizaje instrumental, modelos de reducción de error—son todos soluciones al mismo problema fundamental: ¿qué predice qué? ¿qué acción produce qué consecuencia? Cuando un organismo resuelve ese problema, ya no vive esclavizado al presente. Puede anticipar, prepararse, y actuar sobre el futuro antes de que llegue.

---

> **[SIMULADOR 3 — Reactivo vs. Anticipatorio]**
> 
> Este simulador compara dos conductores en una ruta con gasolineras distribuidas irregularmente: uno reactivo (carga cuando el tanque alcanza 15%) y uno anticipatorio (carga antes de tramos largos). Puedes modificar la distribución de gasolineras para ver cuándo cada estrategia falla.
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> 
> # Ruta de 500 km con gasolineras en posiciones irregulares
> GASOLINERAS_KM = [40, 90, 250, 280, 450]  # solo hay gasolineras aquí
> AUTONOMIA_KM = 100  # el tanque lleno alcanza 100 km
> UMBRAL_REACTIVO = 0.15  # carga cuando queda 15% del tanque
> 
> def simular_conductor(reactivo=True):
>     posicion = 0
>     tanque = 1.0  # 1.0 = lleno
>     eventos = []
>     varado = False
>     
>     while posicion < 500 and not varado:
>         # Avanzar 10 km
>         consumo = 10 / AUTONOMIA_KM
>         
>         # ¿Hay gasolinera aquí?
>         en_gasolinera = any(abs(posicion - g) < 5 for g in GASOLINERAS_KM)
>         
>         if reactivo:
>             # Carga si está en gasolinera y el tanque está bajo
>             if en_gasolinera and tanque < UMBRAL_REACTIVO:
>                 eventos.append((posicion, 'carga'))
>                 tanque = 1.0
>         else:
>             # Anticipatorio: carga si está en gasolinera y hay tramo largo ahead
>             km_prox_gasolinera = min(
>                 (g - posicion for g in GASOLINERAS_KM if g > posicion), 
>                 default=500
>             )
>             gasolina_necesaria = km_prox_gasolinera / AUTONOMIA_KM + 0.1  # margen
>             if en_gasolinera and tanque < gasolina_necesaria:
>                 eventos.append((posicion, 'carga'))
>                 tanque = 1.0
>         
>         tanque -= consumo
>         posicion += 10
>         
>         if tanque <= 0:
>             eventos.append((posicion, 'varado'))
>             varado = True
>             break
>     
>     return posicion, eventos, varado
> 
> pos_r, ev_r, varado_r = simular_conductor(reactivo=True)
> pos_a, ev_a, varado_a = simular_conductor(reactivo=False)
> 
> print(f"Conductor REACTIVO:      llegó a km {pos_r:.0f}{'  ← VARADO' if varado_r else ' (llegó)'}")
> print(f"Conductor ANTICIPATORIO: llegó a km {pos_a:.0f}{'  ← VARADO' if varado_a else ' (llegó)'}")
> print(f"\nGasolineras en: {GASOLINERAS_KM}")
> print(f"Prueba cambiar la distribución de gasolineras para ver cuándo cada estrategia falla.")
> ```

---


## Resumen del Capítulo

Este capítulo presentó el segundo mecanismo adaptativo fundamental del libro: los sistemas de retroalimentación basados en comparación simultánea. El contraste con el ascenso de colina es revelador:

| Característica | Ascenso de Colina (Cap. 4) | Taxias / Retroalimentación (Cap. 5) |
|:---|:---|:---|
| Tipo de comparación | Sucesiva (ahora vs. antes) | Simultánea (derecha vs. izquierda) |
| Sensores requeridos | Uno solo | Bilaterales (dos) |
| Información direccional | No (solo tendencia local) | Sí (dirección inmediata) |
| Velocidad de convergencia | Lenta, sinuosa | Rápida, espiral |
| Requiere memoria | Sí (valor previo) | No (comparación instantánea) |
| Robustez ante perturbaciones | Moderada | Alta |

Ambos mecanismos son adaptativos, precisamente ubicados, y complementarios. Muchos organismos los usan en diferentes contextos o en combinación. Lo que ambos comparten es la limitación que abre la puerta al aprendizaje: son reactivos. No tienen historia, no tienen predicción, no tienen modelo del futuro. El conductor experimentado que carga gasolina antes de los tramos largos está haciendo algo que ninguno de estos mecanismos puede hacer por sí solo: actuar en el presente basándose en lo que sabe que vendrá.

Esa capacidad—aprender relaciones predictivas y usarlas para anticipar—es el tema central del resto del libro.


## Ejercicios de Reflexión

**1.** Para cada comportamiento, decide si es (A) ascenso de colina, (B) taxia, (C) retroalimentación con set point interno (regulación), o (D) sistema abierto sin retroalimentación: (a) un murciélago ajusta la dirección de vuelo basándose en diferencias de tiempo entre la llegada del eco a cada oído; (b) una planta cierra sus hojas al detectar vibración; (c) un humano mantiene su temperatura corporal en 37°C mediante sudoración y tiriteo; (d) un caracol navega hacia mayor humedad comparando su situación actual con la de hace un minuto.

**2.** Dibuja el diagrama de lazo de retroalimentación para la termorregulación en un mamífero. Identifica el sensor, el comparador, el controlador, el efector, y la función de retroalimentación. ¿Cuál es el set point? ¿Cuál es la señal de error cuando la temperatura ambiente baja bruscamente?

**3.** Considera la ecuación de control ω = k·(S_der − S_izq) con k = 2. Si S_der = 8 y S_izq = 5, ¿cuál es el giro? ¿En qué dirección está la fuente? ¿Qué ocurre con el ángulo θ en el siguiente instante? Ahora imagina que el sistema gira y en el siguiente paso S_der = 6.5 y S_izq = 6.5. ¿Qué significa eso para el comportamiento?

**4.** El capítulo menciona que la demora entre detección de error y ejecución de respuesta puede desestabilizar un sistema de retroalimentación. Usa el Simulador 2 para explorar con qué valor de `delay_steps` el sistema comienza a oscilar para k = 1.0. ¿Qué pasa si reduces k a la mitad? ¿Por qué la ganancia y la demora interactúan?

**5.** Diseña el sistema de retroalimentación para un robot que debe seguir una línea negra en el piso usando dos sensores de luz en la parte frontal inferior. Especifica: (a) cuál es la señal de error, (b) cómo varía el signo de k según si el robot va hacia la línea o se aleja, (c) qué ocurre cuando el robot cruza la línea completamente y ambos sensores ven blanco.

**6.** El ejemplo del conductor y las gasolineras ilustra la transición de reactivo a anticipatorio. Piensa en un ejemplo de tu propia vida donde aplicas una estrategia anticipatoria en lugar de reactiva. ¿Qué señal usas como predictor? ¿Cuándo y cómo aprendiste que esa señal predice la necesidad futura? ¿Recuerdas haber fallado (estrategia reactiva) antes de aprender la estrategia anticipatoria?


## Lecturas Recomendadas

**Fraenkel, G. S., & Gunn, D. L. (1961).** *The Orientation of Animals: Kineses, Taxes and Compass Reactions.* Dover. — El tratado clásico. Los capítulos 2–4 son accesibles y cubren la evidencia experimental en taxias con más detalle del que fue posible aquí.

**Braitenberg, V. (1984).** *Vehicles: Experiments in Synthetic Psychology.* MIT Press. — Una joya conceptual. Muestra cómo comportamientos sorprendentemente complejos emergen de sistemas de retroalimentación simple. Lectura altamente recomendada; es breve y completamente accesible.

**Powers, W. T. (1973).** *Behavior: The Control of Perception.* Aldine. — Un argumento radical: todo comportamiento animal es, fundamentalmente, control de percepción mediante retroalimentación. Controversial pero influyente, y relevante para entender la perspectiva del control como alternativa al enfoque estímulo-respuesta.

**Ashby, W. R. (1956).** *An Introduction to Cybernetics.* Chapman & Hall. — Los fundamentos matemáticos de los sistemas de retroalimentación, escritos con la claridad inusual de quien sabe exactamente lo que quiere decir. Los capítulos 1–3 son suficientes para los propósitos de este curso.

---

*En el próximo capítulo comenzamos el Bloque I: El problema de la asignación de crédito.  El primer problema: cuando múltiples eventos preceden una consecuencia, ¿cómo determina el organismo cuáles son predictivos y cuáles son accidentales?*

---