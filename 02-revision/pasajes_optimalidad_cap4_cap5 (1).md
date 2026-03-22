# Pasajes de optimalidad — Capítulos 4 y 5
## Listos para insertar en los capítulos reescritos

---

## CAPÍTULO 4 — Ascenso de Colina

### Dónde va
Después de la sección "El Algoritmo" (el Ajusco vendado) y antes de "Formalización Matemática".
Título de sección sugerido: **¿Qué tan bueno es el algoritmo?**

---

### Texto

El algoritmo que describimos funciona, pero conviene preguntarse qué tan bien funciona y si puede hacerse mejor. Para eso, la competencia del Ajusco es útil más allá de ilustrar el mecanismo.

Imagina que ahora tienes información sobre la montaña: sabes que el Ajusco no es una colina perfectamente suave sino un terreno accidentado, con peñascos, cerros secundarios y mesetas que desde abajo parecen la cima. Tu compañero está vendado y usa el ascenso simple —da un paso, siente si subió o bajó, decide. Tú también estás vendado, pero usas el ascenso de mayor pendiente: antes de comprometerte con una dirección, tanteas varios pasos en distintas direcciones, memorizas los valores, y luego avanzas decididamente hacia donde la pendiente fue mayor. En una montaña suave, tu estrategia no te da ninguna ventaja y te cuesta tiempo extra. En una montaña con muchos cerros secundarios, tu estrategia reduce el riesgo de quedarte atascado en uno de ellos.

Pero hay algo que ambos hacen mal: el tamaño del paso. Lejos de la cima, cuando el terreno cambia rápidamente con cada movimiento, tiene sentido dar pasos grandes —la información de un paso pequeño es poco informativa respecto a si la dirección general es buena. Conforme te acercas a la cima, la pendiente se suaviza y la señal de cada paso se vuelve más pequeña y más ruidosa. En ese momento, un paso grande puede hacerte cruzar la cima sin notarlo. El paso óptimo no es constante: debe ir reduciéndose conforme se acerca al objetivo.

En la ecuación del mecanismo, el tamaño efectivo del paso está controlado por el parámetro *b*: cuánto peso le da el sistema a cada diferencia detectada. Un *b* grande actúa como un paso largo —sensible, rápido para reaccionar, pero propenso a sobrepasar el objetivo. Un *b* pequeño actúa como un paso corto —robusto ante el ruido, pero lento para reaccionar ante cambios reales. El valor óptimo de *b* no es fijo: depende de las características del terreno que está navegando el organismo.

Lo mismo aplica al parámetro *a*, que controla cuánto tiempo sigue el organismo en modo de explotación después de que la señal se estabiliza. En una montaña con pocos máximos locales, un *a* alto es bueno —el organismo explota con inercia y llega rápido a la cima. En una montaña con muchos cerros secundarios, un *a* alto es una trampa: el inercia del sistema lo mantiene escalando el primer cerro que encuentra aunque haya uno más alto a su izquierda. El valor óptimo de *a* también depende del terreno.

Esto no es un defecto del mecanismo sino una propiedad fundamental de cualquier algoritmo de búsqueda: no existe una estrategia universalmente óptima independiente del problema. Lo que existe son estrategias bien adaptadas a tipos particulares de entornos. Y si el entorno cambia, o si el organismo no sabe de antemano qué tipo de entorno enfrenta, el valor fijo de *a* y *b* con que parte puede ser bueno o puede ser desastroso.

La solución verdaderamente óptima al problema no es encontrar los mejores valores fijos de *a* y *b*, sino desarrollar la capacidad de *ajustar esos valores conforme se acumula experiencia con el entorno*. Un agente que empieza con pasos grandes cuando el terreno es desconocido y los va reduciendo sistemáticamente conforme aprende que está cerca de un óptimo —ese agente es mejor que cualquier agente con parámetros fijos, sin importar qué tan bien calibrados estén esos parámetros. Esa capacidad de ajustar adaptativamente la importancia del error es exactamente lo que veremos en los mecanismos de aprendizaje de los bloques siguientes.

---

## CAPÍTULO 5 — Sistemas de Retroalimentación

### Dónde va
Después de las cuatro preguntas (equilibrio, dinámica, perturbación) y antes de "Regulación y Servomecanismos". Si la sección de las cuatro preguntas tiene su propio título, este pasaje puede ir como subsección final de esa sección o como sección independiente.
Título de sección sugerido: **¿Qué tan buena es la función de control?**

---

### Texto

La función de control que describimos —girar a una tasa proporcional a la disparidad bilateral— funciona. La polilla llega a la fuente de luz, el organismo con un ojo cubierto gira indefinidamente, el sistema con demora oscila. Pero conviene preguntarse si esa función es la mejor posible.

Considera dos organismos con la misma arquitectura sensorial pero diferente ganancia *k*. El primero tiene *k* bajo: responde débilmente a cada unidad de disparidad, tarda más en corregir una desviación pero nunca sobrecompensa. El segundo tiene *k* alto: responde con fuerza a cada unidad de disparidad, corrige rápidamente pero puede pasarse de largo. En un ambiente tranquilo, sin viento, con la fuente de luz fija, el segundo organismo llega antes. En un ambiente con perturbaciones frecuentes —ráfagas de viento que desvían continuamente al organismo de su trayectoria— el organismo de *k* alto puede entrar en un ciclo de sobre-correcciones que lo hace menos eficiente que el de *k* bajo.

El valor óptimo de *k* no existe en abstracto: existe en relación a las características del entorno. En un entorno estable, alta ganancia es mejor. En un entorno turbulento, ganancia moderada produce mejor desempeño a largo plazo. La "solución" que vemos en cualquier especie particular es el resultado de que la selección natural ajustó *k* al entorno promedio que esa especie ha enfrentado a lo largo de su historia evolutiva. Una polilla que evolucionó en ambientes con poco viento tiene, probablemente, una ganancia más alta que una especie similar que evolucionó en zonas costeras con viento constante. No lo hemos medido, pero la predicción es directa.

Esto revela algo importante sobre qué significa "entender" un comportamiento. Si solo preguntamos cómo funciona el mecanismo —nivel algorítmico— la respuesta es la función de control y el valor de *k* que tiene esa especie. Pero si preguntamos por qué ese valor particular de *k* —por qué no más alto, por qué no más bajo— la respuesta requiere el nivel computacional: cuál es el problema adaptativo que ese organismo resuelve y en qué tipo de entorno lo resuelve. El valor de *k* es la respuesta al problema; el problema es lo que explica el valor de *k*.

La misma lógica aplica a la forma de la función de control. La función lineal ω = k·(S_der − S_izq) que usamos es la más simple posible. Podría imaginarse una función que no solo usa la disparidad actual sino la *tasa de cambio* de la disparidad —si la diferencia entre sensores está creciendo rápidamente, corrige más agresivamente que si está creciendo despacio, aunque en ambos casos el valor actual de la disparidad sea el mismo. Esa función sería más eficiente ante blancos móviles. Que organismos distintos tengan funciones de control distintas es esperable: la función es la solución y el entorno define el problema.

Lo que hace óptima a la solución más sofisticada no es solo tener la ganancia correcta, sino poder *cambiar adaptativamente qué tan importante es el error* dependiendo de la situación. Un organismo que en entornos tranquilos usa *k* alto para llegar rápido, y en entornos turbulentos reduce automáticamente su ganancia para no oscilar —ese organismo supera a cualquier competidor con ganancia fija, sin importar qué valor fijo tenga ese competidor. Esa capacidad de modificar la importancia del error basándose en la experiencia reciente con el entorno es, nuevamente, exactamente lo que los mecanismos de aprendizaje permiten. La diferencia entre un sistema de retroalimentación con *k* fijo y un sistema que aprende el valor de *k* adecuado no es de tipo sino de escala temporal: el primero es la solución filogenética al problema, el segundo es la solución ontogenética.

---

## Nota sobre la conexión forward en ambos capítulos

Los dos pasajes convergen en el mismo punto y lo hacen deliberadamente: el parámetro que controla la importancia del error (*b* en kinesis, *k* en taxias) tiene un valor óptimo que depende del entorno, y la solución verdaderamente óptima es aprender ese valor adaptativamente.

Eso es exactamente el parámetro α de los modelos de aprendizaje asociativo. En Rescorla-Wagner, α controla la velocidad del aprendizaje —qué tanto le importa al sistema la diferencia entre lo predicho y lo obtenido. En los modelos de atención de Mackintosh y Pearce-Hall, α se modifica ensayo a ensayo dependiendo de si el estímulo ha sido un buen o mal predictor. La línea de continuidad entre el *k* de la polilla y el α de Rescorla-Wagner es directa y vale la pena sembrarla aquí.

Una frase puente posible para el final de cada pasaje, si se quiere hacer explícita la conexión:

**Cap. 4:** *"Veremos esa capacidad —ajustar adaptativamente la importancia del cambio detectado— cuando lleguemos a los modelos de aprendizaje asociativo en el Bloque II."*

**Cap. 5:** *"Cuando en el Bloque II veamos el parámetro α de los modelos de aprendizaje, reconoceremos en él la misma pregunta que hemos planteado aquí: ¿qué tan importante debería ser el error para este organismo, en este entorno, en este momento?"*

Estas frases son opcionales. El argumento funciona sin ellas; con ellas hacen la conexión más explícita de lo que tu estilo habitual prefiere. Queda a tu criterio.
