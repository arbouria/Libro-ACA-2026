# Capítulo 16: Optimización en Equilibrio

## Arturo Bouzas
## Borrador muy preliminar

Todas las variantes de la ley del efecto coinciden en un punto: las respuestas que producen consecuencias biológicamente importantes aumentan en frecuencia. Si esa fuera la única información que el concepto nos proporcionara, difícilmente le asignaríamos el estatus de una ley, y su utilidad práctica sería muy limitada. Consideremos el caso de una madre que quiere modificar la conducta de su hijo. La sola recomendación de reforzar la conducta deseada no le resulta totalmente útil. Querría saber si es necesario reforzar cada instancia de la respuesta o solo algunas de ellas. Querría saber si el décimo refuerzo tiene el mismo impacto que el segundo. Y, sobre todo, querría saber qué diferencia hace seguir distintas reglas para la entrega del refuerzo. En el capítulo sobre programas de refuerzo respondimos a la última pregunta con una descripción cualitativa: los patrones de respuesta difieren según el programa. Pero la madre todavía no sabe, de manera cuantitativa, qué tasa de respuesta producirá un programa de intervalo variable de treinta segundos frente a uno de dos minutos, ni por qué los programas de razón producen tasas de respuesta tan distintas a los de intervalo aun cuando la tasa promedio de refuerzo sea la misma.

Lo que hace falta es especificar la *función* que describe la relación entre la tasa de respuesta del organismo y la tasa de refuerzo que obtiene:

$$R = f(r)$$

Encontrar esa función, y entender qué principio la genera, es el problema central de este capítulo. Veremos que la respuesta no es simplemente una ecuación de ajuste, sino que emerge de un principio general: el comportamiento distribuye su tiempo entre actividades que compiten entre sí, y lo hace de la mejor manera posible dentro de las restricciones que el entorno impone.

---

## Las dos funciones empíricas

Antes de presentar los modelos conviene documentar con precisión lo que hay que explicar. Los experimentos sobre programas simples revelan dos formas funcionales que cualquier modelo serio debe poder derivar.

### Programas de intervalo variable

Catania y Reynolds (1968) publicaron el primer estudio sistemático de la relación entre la tasa de respuesta y la tasa de refuerzo en programas de intervalo variable. El protocolo fue cuidadoso: expusieron palomas a múltiples valores de intervalo variable, esperaron en cada caso hasta que el comportamiento se estabilizara — el *equilibrio* del que habla el título de este capítulo — y registraron la tasa de respuesta correspondiente. Al graficar la tasa de respuesta en función de la tasa de refuerzo, obtuvieron una curva de ganancias decrecientes: la tasa de respuesta crece rápidamente cuando la tasa de refuerzo pasa de cero a valores moderados, pero los incrementos adicionales producen efectos cada vez menores. La función se aplana hasta acercarse asintóticamente a un máximo. Docenas de experimentos posteriores, en diferentes especies y distintas topografías de respuesta, replicaron la misma forma (de Villiers y Herrnstein, 1976).

**[FIGURA 17.1: Función de respuesta para programas de intervalo variable. Eje horizontal: tasa de refuerzo (refuerzos/hora). Eje vertical: tasa de respuesta (respuestas/minuto). Curva de ganancias decrecientes que se aplana hacia una asíntota. Puntos de datos estilizados de Catania y Reynolds (1968). Paleta del libro.]**

### Programas de razón variable

Los programas de razón variable producen un patrón radicalmente diferente. Aquí la variable independiente no es la tasa de refuerzo directamente sino el *valor del programa* — cuántas respuestas se requieren por refuerzo en promedio. La relación entre ambas variables es determinista: un programa RV-10 produce exactamente un refuerzo por cada diez respuestas, de modo que un organismo que responde a 100 resp/min obtiene 10 refuerzos/min. A diferencia del intervalo variable, donde el tiempo acumula oportunidades independientemente de la respuesta, en la razón variable el refuerzo solo ocurre si la respuesta ocurre — y en una proporción fija.

Lo que se observa empíricamente es una función *bitónica*: la tasa de respuesta aumenta conforme aumenta el valor del programa (y por tanto disminuye la tasa de refuerzo), llega a un máximo, y luego disminuye cuando el programa se vuelve todavía más exigente. Un organismo responde más bajo un RV-20 que bajo un RV-5, pero responde menos bajo un RV-80 que bajo un RV-20. La paradoja — más exigencia produce, hasta cierto punto, más respuesta, y luego menos — es aparente. Más adelante veremos exactamente por qué ocurre.

**[FIGURA 17.2: Función de respuesta para programas de razón variable. Eje horizontal: tasa de refuerzo (refuerzos/hora, que decrece conforme el valor del programa aumenta). Eje vertical: tasa de respuesta (respuestas/minuto). Función bitónica con máximo a valores intermedios del programa. Datos estilizados de Staddon (1983, Figura 8.6). Paleta del libro.]**

La pregunta que nos deja este contraste es precisa: ¿por qué la misma variable — la tasa de respuesta de un organismo entrenado con consecuencias contingentes — produce una función monótona bajo programas de intervalo y una función bitónica bajo programas de razón? ¿Hay un principio que derive las dos formas a partir de una misma arquitectura, simplemente porque las restricciones que los dos tipos de programas imponen son diferentes? Sí, y ese principio es la optimización bajo restricciones.

---

## Qué significa optimizar bajo restricciones

La Introducción de este libro identificó, entre los algoritmos fundamentales del comportamiento adaptable, uno que todavía no habíamos formalizado: encontrar la mejor distribución posible de comportamiento dadas las limitaciones del entorno. Ese es exactamente el marco que ahora desarrollamos.

Hay dos ingredientes necesarios para cualquier modelo de optimización. El primero es una descripción del *espacio de posibilidades*: qué distribuciones de comportamiento son siquiera alcanzables. Las restricciones — de tiempo, de programas, de capacidad — delimitan ese espacio. El segundo es una descripción del *valor* de cada distribución posible: qué tan buena es cada combinación de comportamientos para el organismo. La solución del modelo es la distribución de mayor valor dentro del espacio alcanzable.

Lo que hace especialmente fecundo este marco no es la noción de maximización en sí — esa aparece en muchos contextos — sino el papel de las *restricciones*. Cada minuto dedicado a un comportamiento es un minuto menos disponible para todos los demás. No es una metáfora: es una consecuencia aritmética de que el tiempo total es finito. Este hecho elemental — que los comportamientos compiten por el tiempo — implica que toda elección lleva consigo un *costo de oportunidad*: lo que se deja de hacer al hacer algo. Un estudiante que dedica dos horas adicionales a preparar un examen no incurre solo en el costo del esfuerzo cognitivo: incurre también en el costo de las dos horas de descanso o de vida social que no ocurrieron. Si ese costo no se contabiliza, el análisis del comportamiento queda incompleto.

Los programas de refuerzo hacen visible esta estructura de costos porque controlan experimentalmente la relación entre comportamientos. Cuando la madre del inicio pregunta qué tasa de respuesta producirá un programa determinado, la respuesta depende de cuánto vale el refuerzo *en relación con* las demás actividades que compiten con la respuesta, y de cuánto trabajo requiere el programa para obtenerlo. La optimización convierte esa intuición en un modelo con predicciones concretas.

---

## Todo el comportamiento tiene valor

Este enfoque exige un cambio en el inventario de lo que se valúa. Hasta ahora hemos distinguido entre una *respuesta* (presionar una palanca, picar una tecla) y su *consecuencia* (comida, acceso a agua). Los modelos de optimización proponen que esa distinción es arbitraria.

La propuesta original fue de David Premack (1965). Para Premack, la distinción entre respuesta y consecuencia es solo una distinción de roles en un procedimiento experimental, no una diferencia de naturaleza. La comida al final de la presión de la palanca es *comer* — un comportamiento con su propia tasa de ocurrencia, su propio tiempo de ejecución, y su propio valor. La distinción correcta no es entre respuesta y reforzador, sino entre comportamientos con *menos acceso del preferido* y comportamientos con *más acceso del preferido*. El refuerzo, en este marco, no es una cosa: es una relación de valor relativo entre comportamientos. Para medirlo, Premack propuso observar cuánto tiempo dedica el organismo a cada comportamiento cuando no hay restricciones externas — esa distribución libre es la *distribución preferida* y su forma mide el valor relativo de cada actividad.

William Timberlake y Jean Allison (1974) probaron empíricamente esta formulación mediante experimentos de *privación de respuesta*. Si lo que importa no es el reforzador como evento discreto sino la restricción sobre el acceso a un comportamiento preferido, entonces no debería haber efecto de refuerzo cuando el organismo ya tiene libre acceso a más de su cantidad preferida de la consecuencia. Y así resultó: cuando la contingencia permite al organismo obtener su nivel preferido de consumo sin aumentar el trabajo, la tasa de trabajo no cambia. El efecto del refuerzo — el incremento de la respuesta instrumental — ocurre precisamente y solo cuando la restricción del programa *priva* al organismo de una parte de su consumo preferido, obligándolo a trabajar más para recuperarlo. Esta simetría del principio de refuerzo es algo que la ley del efecto de Thorndike no puede derivar sin supuestos adicionales.

---

## Los programas de refuerzo como restricciones

Con estas ideas en mano podemos reinterpretar los programas de refuerzo. Un programa de refuerzo no es simplemente una regla para entregar reforzadores: es una *restricción sobre el espacio de distribuciones de comportamiento alcanzables*.

Consideremos los tres comportamientos que compiten por el tiempo del organismo en un experimento típico: *trabajo* (la respuesta instrumental), *consumo* (el comportamiento de obtener y usar el refuerzo), y *ocio* (cualquier otra cosa). La primera restricción es universal: la suma de los tiempos asignados a los tres debe igualar el tiempo total disponible. La segunda restricción es la que impone el programa: la función de retroalimentación que determina cuánto consumo produce cada cantidad de trabajo.

En un programa de *razón variable*, la relación entre trabajo y consumo es lineal: por cada $n$ respuestas en promedio, el organismo obtiene un ciclo de consumo. Doblar el trabajo dobla el consumo. La restricción es una recta en el espacio (trabajo, consumo). En un programa de *intervalo variable*, la relación es de ganancias decrecientes: las primeras respuestas por minuto producen muchos refuerzos porque las oportunidades se han acumulado, pero más allá de cierta tasa el reloj se convierte en el cuello de botella, y la función se aplana. La restricción es una curva cóncava.

**[FIGURA 17.3: Funciones de retroalimentación como restricciones en el espacio (trabajo, consumo). Panel izquierdo: RV — restricción lineal. Panel derecho: IV — restricción cóncava. El punto B₀ es la distribución preferida, libre de restricciones. Paleta del libro.]**

Esta reinterpretación conecta directamente con las funciones de retroalimentación del capítulo 13. Lo que allí se describió como la relación entre tasa de respuesta y tasa de refuerzo — lineal para RV, cóncava para IV — es aquí la geometría de las restricciones que el entorno impone sobre las distribuciones posibles del organismo. El programa de refuerzo ya no fortalece respuestas: define el precio del consumo en unidades de trabajo, y ese precio tiene una geometría que determina la forma de las funciones de respuesta que queremos derivar.

---

## El modelo de distancia mínima (Staddon)

John Staddon formalizó la propuesta de Timberlake de la siguiente manera. Sea $B_0 = (R_0, r_0)$ la distribución preferida del organismo: el par (tasa de trabajo, tasa de consumo) que el organismo elegiría libremente. El programa de refuerzo define la función $r = f(R)$ que relaciona trabajo y consumo alcanzables. Si $B_0$ no está sobre esa función — y generalmente no lo está — el organismo debe alejarse de su preferencia. La pregunta es: ¿cuánto y en qué dirección?

La respuesta de Staddon: el organismo elige el punto sobre la restricción que minimiza el costo total de la desviación. El costo es la distancia euclidiana ponderada al punto preferido:

$$C(R) = a(R_0 - R)^2 + b(r_0 - f(R))^2$$

El primer término penaliza alejarse de la tasa de trabajo preferida; el segundo, alejarse de la tasa de consumo preferida. Los pesos $a$ y $b$ reflejan la importancia relativa de cada desviación — típicamente $b > a$, porque los organismos en condiciones libres dedican mucho más tiempo al consumo que al trabajo, y por tanto el costo de alejarse del consumo preferido es mayor. El organismo minimiza $C(R)$ encontrando el valor de $R$ que equilibra ambas pérdidas.

### Ejemplo numérico: la función bitónica del RV

Para hacer concreto el argumento, tomemos un organismo con distribución preferida $R_0 = 10$ resp/min y $r_0 = 5$ ref/min, con pesos iguales $a = b = 1$. Bajo distintos programas de razón variable, la restricción es $r = R/n$ donde $n$ es el valor del programa. La minimización de $C(R)$ para una restricción lineal tiene solución analítica: el punto predicho es la proyección perpendicular de $B_0$ sobre la línea de restricción.

| Programa | Pendiente $1/n$ | $R^*$ predicho | $r^*$ predicho |
|----------|-----------------|----------------|----------------|
| RV-1     | 1.00            | 7.5            | 7.5            |
| RV-2     | 0.50            | 9.0            | 4.5            |
| RV-5     | 0.20            | 10.4           | 2.1            |
| RV-10    | 0.10            | 10.9           | 1.1            |
| RV-20    | 0.05            | 11.0           | 0.55           |
| RV-50    | 0.02            | 10.4           | 0.21           |
| RV-100   | 0.01            | 8.9            | 0.09           |

La tasa de trabajo predicha sube de RV-1 a aproximadamente RV-20, alcanza un máximo, y luego desciende. Con RV-100, el programa es tan exigente que el costo de seguir aumentando el trabajo supera el beneficio marginal de consumo adicional, y el organismo reduce su tasa de respuesta. La función bitónica emerge de la geometría, no de ningún supuesto psicológico adicional.

**[FIGURA 17.4: Solución geométrica del modelo de distancia mínima para programas de razón variable. B₀ es la distribución preferida (10, 5). Cinco líneas de restricción con distintas pendientes (distintos valores del programa RV). La perpendicular desde B₀ a cada línea es el punto predicho — marcado con puntos llenos. La trayectoria de puntos predichos forma un semicírculo. Panel derecho: la misma información proyectada sobre el eje de la tasa de respuesta muestra la función bitónica. Paleta del libro.]**

Para el programa de intervalo variable, la restricción es cóncava. La perpendicular a una curva cóncava cae siempre del mismo lado — el de mayor trabajo y consumo — y se desplaza monótonamente sin revertir. La función predicha es de ganancias decrecientes, sin rama descendente.

---

## El modelo de maximización de utilidad (Rachlin)

Howard Rachlin llegó al mismo problema desde la microeconomía conductual. Su punto de partida, consistente con Premack, es que todos los comportamientos tienen valor. Ese valor puede representarse mediante una *función de utilidad*, y la distribución óptima de comportamiento es aquella que maximiza la utilidad total bajo las restricciones del programa.

### De la función psicofísica a la curva de indiferencia

Para entender la forma que adoptan las funciones de utilidad en este contexto, conviene empezar por la función psicofísica de valor. Sabemos desde los primeros capítulos del libro que la relación entre la magnitud física de un estímulo y su magnitud psicológica percibida es de ganancias decrecientes — la misma lógica de la ley de Weber-Fechner y de las funciones de potencia de Stevens. Lo mismo ocurre con el valor de los comportamientos: tener acceso a más de una actividad añade valor, pero cada unidad adicional añade menos que la anterior. La primera hora de descanso después de un día de trabajo vale mucho; la sexta hora, mucho menos.

Esta propiedad — ganancias decrecientes en el valor del comportamiento — tiene una consecuencia directa sobre la forma de las curvas de indiferencia. Una curva de indiferencia es el conjunto de todas las distribuciones (todos los paquetes de tiempo asignado a distintas actividades) que el organismo valora igualmente. Si el valor de cada comportamiento tiene ganancias decrecientes, entonces la relación de intercambio entre dos comportamientos no es constante sino que depende de los niveles actuales: cuando ya se tiene mucho de un comportamiento, hace falta sacrificar poco de él para compensar la pérdida de un poco del otro; cuando se tiene muy poco, hay que sacrificar mucho. Esa dependencia del nivel es exactamente lo que produce curvas de indiferencia *convexas*: curvas que se doblan hacia el origen, donde cada punto de la curva refleja una tasa de sustitución diferente.

**[FIGURA 17.5: Derivación de la convexidad de las curvas de indiferencia a partir de las ganancias decrecientes del valor. A niveles altos de consumo (izquierda del gráfico), un pequeño sacrificio de consumo requiere poca compensación en trabajo. A niveles bajos de consumo (derecha), el mismo sacrificio requiere mucha más compensación. La curva resultante es convexa. Paleta del libro.]**

### Funciones de potencia: sustitutos imperfectos con ganancias decrecientes

La forma funcional más natural para capturar las ganancias decrecientes es la función de potencia con exponente menor que uno:

$$U(x) = x^s, \quad 0 < s < 1$$

Estas funciones crecen monótonamente — siempre vale más — pero con ganancias decrecientes. Para un paquete de comportamientos (trabajo $R$, consumo $r$, ocio $L$), la utilidad total es la suma de las utilidades individuales:

$$U = R^{s_1} + r^{s_2} + L^{s_3}$$

Con esta forma funcional, las curvas de indiferencia en el espacio (trabajo, consumo) son hipérbolas convexas: a medida que el consumo disminuye, el trabajo necesario para compensar aumenta más que proporcionalmente. La forma de la hipérbola captura bien la sustitución imperfecta entre comportamientos que son distintos en naturaleza — trabajar no es lo mismo que comer, ni comer lo mismo que descansar — pero que compiten por el tiempo de la misma manera.

Las funciones de potencia son adecuadas para describir la relación entre trabajo y consumo en programas de intervalo variable, donde el punto de máxima utilidad está fuera del rango de restricciones relevante. Bajo un IV, el organismo nunca puede acercarse realmente a su tasa de consumo preferida porque el programa pone un techo sobre las oportunidades de refuerzo disponibles por unidad de tiempo; la restricción cóncava garantiza que más trabajo produce siempre más consumo, aunque con rendimientos decrecientes. En ese contexto, el máximo alcanzable está siempre en el extremo de mayor trabajo que la restricción permite, y la función de respuesta resulta monótonamente creciente.

### Funciones cuadráticas y el bliss point: la fuente de la bitonicidad

Para programas de razón variable, donde la función bitónica exige que la tasa de respuesta *disminuya* a valores altos del programa, las funciones de potencia no son suficientes. Una función que crece monótonamente no tiene un máximo interior — aumentar siempre el trabajo aumenta la utilidad del trabajo, aunque con ganancias decrecientes, y la tangencia óptima nunca retrocede. Para que el organismo prefiera trabajar *menos* cuando el programa es muy exigente hace falta que las funciones de utilidad tengan un *punto de saturación* más allá del cual más es peor.

Las funciones cuadráticas tienen exactamente esa propiedad:

$$u(R) = -a(R - R_0)^2, \quad u(r) = -b(r - r_0)^2$$

Estas funciones alcanzan su máximo en los valores preferidos $R_0$ y $r_0$, y *disminuyen* cuando el comportamiento se aleja de esos valores en cualquier dirección — ya sea por exceso o por defecto. El punto $(R_0, r_0) = B_0$ es el *bliss point*: la distribución que el organismo preferiría tener si pudiera elegir libremente. En torno a ese punto, las curvas de indiferencia son *elipses* centradas en $B_0$. Las elipses más cercanas al bliss point representan mayor utilidad; las más alejadas, menor.

**[FIGURA 17.6: Curvas de indiferencia elípticas centradas en el bliss point B₀. Eje horizontal: tasa de trabajo R. Eje vertical: tasa de consumo r. Las curvas más internas tienen mayor utilidad. La restricción lineal de un programa RV toca la elipse de mayor utilidad en el punto de tangencia, que es la distribución predicha. Conforme el valor del programa aumenta, la restricción rota y el punto de tangencia se desplaza formando una trayectoria bitónica. Paleta del libro.]**

**[SIMULADOR 17.1: Funciones cuadráticas y optimización bajo restricciones. El estudiante puede mover la posición del bliss point B₀, ajustar los pesos a y b de las funciones de costo, y seleccionar el valor del programa RV o IV. El simulador muestra las curvas de indiferencia elípticas, la restricción del programa, y el punto de tangencia predicho. Un panel secundario muestra la función de respuesta resultante (tasa de respuesta vs. valor del programa) a medida que se varía este parámetro. Permite verificar que la función es bitónica bajo RV y monótona bajo IV, y explorar cómo los parámetros del modelo afectan la forma y posición del máximo.]**

El modelo de Rachlin con funciones cuadráticas predice que, al aumentar el valor del programa de razón, el organismo primero aumenta su tasa de trabajo — la restricción lo aleja del consumo preferido y trabaja más para compensar — pero luego disminuye la tasa de trabajo cuando el costo de seguir alejándose del nivel de trabajo preferido supera el beneficio de recuperar algo de consumo. La tangencia óptima entre la restricción lineal y las elipses de indiferencia describe una trayectoria que sube y baja: exactamente la función bitónica de los datos.

Para el programa de intervalo variable, la restricción cóncava produce que la tangencia se desplace siempre en la misma dirección, sin revertir. La función de respuesta es monótonamente creciente, como predicen los datos de Catania y Reynolds.

---

## Minimización y maximización: regulación y teleología

La comparación entre los modelos de Staddon y de Rachlin revela algo más que una diferencia de formalismo: revela dos maneras diferentes de describir el mismo fenómeno, que corresponden a niveles de análisis distintos.

El modelo de Staddon tiene la misma estructura que todos los mecanismos regulatorios que hemos visto en este libro. Hay un punto de referencia, $B_0$, que representa el estado al que el organismo aspira. El programa de refuerzo produce una perturbación que aleja al organismo de ese estado. El organismo *reduce el error* — la distancia al punto de referencia — eligiendo la distribución que minimiza la función de costo. La métrica es cuadrática: $C = a(R_0 - R)^2 + b(r_0 - r)^2$. Esta es exactamente la misma arquitectura del termostato del capítulo 5, y de los modelos de aprendizaje de Bush-Mosteller y Rescorla-Wagner: en esos modelos la variable regulada es el valor predictivo de un estímulo y el error es la discrepancia entre lo esperado y lo obtenido; en el modelo de Staddon la variable regulada es la distribución del comportamiento y el error es la desviación respecto al punto preferido. Staddon es un modelo *regulatorio*: describe el organismo como un sistema que activamente corrige desviaciones de un estado de referencia. En el lenguaje de Marr, responde a una pregunta a caballo entre el nivel computacional y el algorítmico: especifica qué cantidad se minimiza y cómo se mide la desviación.

El modelo de Rachlin funciona de manera opuesta en su lógica, aunque idéntica en sus predicciones. No hay estado de referencia que el organismo proteja: hay una función de utilidad que el organismo maximiza. La dirección del argumento es hacia adelante — hacia el mayor valor posible — en lugar de hacia el origen. No se trata de corregir un error sino de alcanzar la mejor situación posible. Rachlin es un modelo *teleológico*: describe el organismo como un sistema que elige el mejor resultado disponible dado el conjunto de opciones. En el lenguaje de Marr, responde exclusivamente al nivel computacional: qué computa el organismo, sin comprometerse con el mecanismo que lo logra.

Los dos modelos producen exactamente las mismas predicciones sobre el comportamiento en equilibrio porque maximizar una función cuadrática con máximo en $B_0$ es matemáticamente idéntico a minimizar la distancia euclidiana ponderada a $B_0$. Esta equivalencia no es una coincidencia ni un truco algebraico: refleja el hecho de que cualquier función que tiene un máximo puede describirse igualmente como una función que tiene un mínimo de su negativo. La diferencia entre Staddon y Rachlin no está en las predicciones — está en el nivel de descripción que cada uno adopta y en las preguntas que cada uno deja abiertas.

Noten la implicación. Un termostato puede describirse como un sistema que minimiza el error respecto a la temperatura de referencia, o como un sistema que maximiza la cercanía a esa temperatura. Ambas descripciones son correctas, en niveles distintos, y ninguna es más "verdadera" que la otra. La elección entre ellas depende de qué preguntas queremos responder: si nos interesa el mecanismo de corrección, la descripción regulatoria es más fértil; si nos interesa la propiedad de equilibrio del sistema, la descripción de maximización es más natural. El trabajo de Staddon y el de Rachlin son, en este sentido, complementarios por construcción.

---

## De la optimización a la igualación

Los modelos que hemos presentado se desarrollaron para programas simples — una sola alternativa de trabajo con una sola función de retroalimentación. ¿Qué ocurre en los programas concurrentes, donde hay dos alternativas disponibles simultáneamente?

En ese caso, las restricciones son dos funciones de retroalimentación simultáneas, una por alternativa. El espacio de distribuciones alcanzables es el conjunto de pares (tiempo a alternativa 1, tiempo a alternativa 2) que satisfacen ambas restricciones y la restricción de tiempo total. El punto de máxima utilidad dentro de ese espacio — donde la curva de indiferencia toca la frontera factible — ocurre cuando las tasas relativas de respuesta igualan a las tasas relativas de refuerzo.

El argumento intuitivo es el siguiente. Si el organismo asignara más tiempo a la alternativa 1 del que el punto de igualación prescribe, la tasa de refuerzo local de la alternativa 1 caería y la de la alternativa 2 subiría — porque los programas de intervalo variable acumulan oportunidades durante la ausencia del organismo. Esa asimetría en la rentabilidad lleva a reasignar tiempo hacia la alternativa 2, lo que reequilibra los valores marginales de cada alternativa. El único equilibrio estable es aquel donde los valores marginales son iguales en ambas alternativas — y ese punto es exactamente la igualación. La derivación completa requiere cálculo, pero el resultado es el mismo que derivamos por el proceso dinámico de mejoramiento en el capítulo anterior: igualación como equilibrio estable.

La igualación, en este marco, no es un principio fundamental del cual se derivan los modelos de optimización. Es al revés: igualación es un *teorema* del principio de optimización bajo las restricciones específicas de los programas de intervalo variable concurrentes. Lo mismo vale para las funciones de respuesta de IV y RV: son predicciones del mismo principio, con restricciones de diferente geometría.

---

## Lo que los modelos explican y sus límites

Los modelos de optimización en equilibrio predicen correctamente las dos formas funcionales del problema: ganancias decrecientes para IV, bitonicidad para RV. Lo hacen con la misma arquitectura — un principio de optimización — simplemente porque las restricciones que los dos tipos de programa imponen tienen formas geométricas diferentes. Predicen también igualación en programas concurrentes como caso especial. El alcance explicativo de un principio único sobre tres fenómenos empíricos distintos es, por sí mismo, evidencia a su favor.

Sus límites son igualmente claros. Los modelos son de equilibrio: describen el estado estable al que converge el sistema después de suficiente exposición, pero no dicen nada sobre el proceso de convergencia ni sobre cuánto tiempo requiere. Ese es el territorio de los modelos del capítulo anterior. Los modelos de optimización responden una pregunta diferente: dado que el sistema llega al equilibrio, ¿cuál es ese equilibrio?

Requieren además conocer la distribución preferida $B_0$ del organismo, que se estima midiendo el comportamiento libre antes de instalar el programa de refuerzo. Cuando las condiciones motivacionales cambian — saciación, privación, cambios de contexto — $B_0$ puede cambiar, y el modelo debe actualizarse. Esta necesidad de datos de línea base distingue a los modelos de optimización de los modelos más parsimoniosos, como la ley del efecto relativa del capítulo siguiente, que ajustan directamente a los datos de respuesta sin requerir la medición previa de preferencias.

El límite conceptual más profundo, sin embargo, es el que la distinción entre Staddon y Rachlin pone en evidencia. Los modelos de optimización describen el equilibrio — qué distribución el organismo termina adoptando — sin especificar el mecanismo de aprendizaje que conduce allí. Tratan al organismo como si *calculara* la distribución óptima, lo que en el nivel computacional es una descripción legítima y poderosa. Pero el mecanismo que implementa ese cálculo es una pregunta abierta que los modelos de optimización, por su naturaleza, no responden. El capítulo siguiente muestra que existe un mecanismo simple de aprendizaje por refuerzo — la ley del efecto relativa de Herrnstein — que, aplicado repetidamente, conduce al mismo equilibrio que la optimización predice. Que el resultado de un cálculo de optimización y el resultado de una regla de aprendizaje local coincidan no es una casualidad: es una señal de que el organismo ha encontrado, por medios diferentes, la misma solución al mismo problema adaptativo.

---

## Conexiones

### Hacia atrás

**Comportamiento adaptable y optimización bajo restricciones (Introducción).** La Introducción identificó la optimización bajo restricciones como uno de los algoritmos fundamentales del comportamiento adaptable. Este capítulo es su desarrollo formal en el contexto del comportamiento operante.

**Sistemas de retroalimentación (capítulo 5).** El modelo de Staddon es una instancia del mismo mecanismo regulatorio que ese capítulo introdujo. El punto de referencia es $B_0$, el error es la distancia al punto preferido, y el sistema minimiza ese error encontrando la distribución alcanzable más cercana. Lo que cambió no es la arquitectura sino la variable regulada: ya no es la temperatura o el nivel de glucosa sino la distribución del comportamiento en el tiempo.

**Funciones psicofísicas de valor (capítulos anteriores).** Las ganancias decrecientes que determinan la convexidad de las curvas de indiferencia son la misma propiedad que aparece en la percepción de magnitudes y en la función psicofísica de Stevens. No es un supuesto importado de la economía: es el mismo principio aplicado a una nueva variable.

**Programas de refuerzo (capítulo 13).** Las funciones de retroalimentación de Rachlin ($r = dR^m$) son las restricciones del espacio de comportamiento. El exponente $m = 1$ da la restricción lineal del programa de razón; valores entre 0 y 1 dan las restricciones cóncavas del intervalo variable. La taxonomía de programas del capítulo 13 se convierte aquí en una taxonomía de geometrías de restricción.

**Igualación en programas concurrentes (capítulo 14).** La igualación es el equilibrio de optimización para programas concurrentes de intervalo variable. Lo que en el capítulo 14 se presentó como regularidad empírica emerge aquí como consecuencia del principio de optimización.

**Maximización local (capítulos 15-16).** Los modelos de mejoramiento y maximización momentánea describieron el proceso dinámico que lleva al organismo al equilibrio. Los modelos de este capítulo describen el equilibrio mismo. Los dos niveles son complementarios: uno responde cómo, el otro a qué.

### Hacia adelante

**La ley del efecto relativa (capítulo 18).** Los modelos de Staddon y Rachlin derivan igualación y las formas funcionales de $R(r)$ sin postular un mecanismo de refuerzo: solo necesitan restricciones y preferencias. El capítulo siguiente muestra que el mismo equilibrio puede derivarse a partir de una regla de aprendizaje por refuerzo. La ley del efecto relativa de Herrnstein puede interpretarse simultáneamente como una ecuación de actualización de valores — una regla de aprendizaje análoga a Bush-Mosteller — y como una regla de elección que implementa el axioma de Luce. La dualidad entre estas dos interpretaciones es el nudo conceptual del siguiente capítulo.

---

## Resumen

Las funciones de respuesta en programas simples — ganancias decrecientes para intervalo variable, bitónica para razón variable — y la igualación en programas concurrentes son los tres fenómenos empíricos que el bloque necesitaba unificar. Los modelos de optimización en equilibrio los derivan a partir de un principio único: el organismo distribuye su comportamiento de la manera que maximiza su bienestar total dentro del espacio de posibilidades que el programa de refuerzo define.

Ese espacio tiene dos componentes. La restricción de tiempo impone que la suma de los tiempos asignados a todos los comportamientos sea constante. La restricción del programa — la función de retroalimentación — impone que la relación entre trabajo y consumo siga la geometría del tipo de programa: lineal para RV, cóncava para IV. La diferente geometría de las restricciones es la razón por la que las mismas preferencias del organismo producen funciones de respuesta de formas tan distintas.

El modelo de distancia mínima de Staddon formaliza el principio como reducción del error respecto al punto preferido $B_0$ — la misma arquitectura regulatoria que los mecanismos de retroalimentación del capítulo 5. El modelo de maximización de utilidad de Rachlin lo formaliza como maximización de una función de preferencias sujeta a las restricciones del programa — una descripción teleológica del nivel computacional. Los dos son matemáticamente equivalentes: minimizar la distancia euclidiana ponderada a $B_0$ es idéntico a maximizar una función cuadrática centrada en $B_0$. Las curvas de indiferencia elípticas centradas en el bliss point conectan la geometría de Staddon con el formalismo de utilidad de Rachlin, y el simulador permite explorar directamente cómo los parámetros del modelo determinan la forma de las funciones de respuesta empíricas.

---

## Ejercicios

**1.** Un organismo tiene distribución preferida $R_0 = 8$ resp/min, $r_0 = 4$ ref/min, con pesos $a = b = 1$. Bajo un programa RV-$n$, la restricción es $r = R/n$. La minimización de la distancia euclidiana predice que el punto óptimo está en $R^* = (R_0 + r_0/n)/(1 + 1/n^2)$ (se puede verificar tomando la derivada de $C$ e igualándola a cero). Calcula $R^*$ para $n = 1, 2, 5, 10, 20, 50$. ¿A qué valor de $n$ se alcanza el máximo? ¿Qué ocurre cuando $n \to \infty$?

**2.** Dos programas producen la misma tasa promedio de refuerzo de 20 ref/hora: un RV-3 y un IV-3 min. Desde la perspectiva de los modelos de optimización, ¿por qué producen tasas de respuesta diferentes aun cuando la tasa de refuerzo es la misma? ¿Qué propiedad geométrica de las restricciones explica la diferencia?

**3.** El modelo de Rachlin con funciones de potencia predice que la función de respuesta bajo programas de razón variable es monotónica — siempre sube — mientras que el modelo con funciones cuadráticas predice que es bitónica. Explica, sin ecuaciones, por qué la diferencia en la forma funcional de la utilidad produce esta diferencia en la predicción. ¿Cuál es el supuesto psicológico que distingue a las dos formas?

**4.** El experimento de Timberlake y Allison predice que el refuerzo no tendrá efecto cuando el programa permite al organismo obtener su nivel preferido de consumo sin aumentar el trabajo. Diseña un experimento con ratas en una caja de Skinner que ponga a prueba esta predicción, especificando cómo medirías la distribución preferida de cada animal y cómo construirías el programa de refuerzo correspondiente.

**5. [Avanzado]** El capítulo argumenta que igualación es un teorema del principio de optimización bajo programas concurrentes IV-IV. Usando el concepto de bliss point y curvas de indiferencia elípticas, explica gráficamente por qué la distribución de igualación es el único equilibrio estable: muestra que cualquier desviación de ese punto reduce la utilidad del organismo dado que los programas IV acumulan oportunidades durante la ausencia.

---

## Lecturas Recomendadas

**Staddon, J. E. R. (1983).** *Adaptive Behavior and Learning.* Cambridge University Press. Capítulos 7 y 8. — La presentación original del modelo de distancia mínima, con derivaciones formales y ajustes a datos de varias especies. El capítulo 7 presenta los fundamentos conceptuales; el 8 desarrolla las predicciones cuantitativas y la extensión al modelo de tres comportamientos.

**Rachlin, H. (1978).** A molar theory of reinforcement schedules. *Journal of the Experimental Analysis of Behavior, 30*, 345–360. — El artículo fundacional del enfoque de maximización de utilidad. Corto, con buenas figuras y derivaciones accesibles de las predicciones para RV e IV.

**Premack, D. (1965).** Reinforcement theory. En D. Levine (Ed.), *Nebraska Symposium on Motivation.* University of Nebraska Press. — El artículo donde Premack propone que todos los comportamientos tienen valor ordenable y que el refuerzo es una relación de valor relativo. Lectura conceptualmente estimulante.

**Timberlake, W., & Allison, J. (1974).** Response deprivation: An empirical approach to instrumental performance. *Psychological Review, 81*, 146–164. — La formalización del papel de las restricciones y la distribución preferida, con los experimentos de privación de respuesta que distinguen empíricamente esta propuesta de la ley del efecto tradicional.

**Catania, A. C., & Reynolds, G. S. (1968).** A quantitative analysis of the responding maintained by interval schedules of reinforcement. *Journal of the Experimental Analysis of Behavior, 11*, 327–383. — El estudio original de la función de ganancias decrecientes para programas IV. Notable por la consistencia de los resultados entre sujetos y la claridad del diseño.

**Hursh, S. R., & Silberberg, A. (2008).** Economic demand and essential value. *Psychological Review, 115*, 186–198. — Una extensión contemporánea de los modelos de optimización al estudio de la demanda conductual, con aplicaciones al análisis del abuso de sustancias y al comportamiento de consumo en contextos clínicos y de políticas públicas.
