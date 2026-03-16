# Preguntas de Estudio — Capítulo 2: Evolución y Adaptación

---

## Sección I: Comprensión conceptual

Estas preguntas verifican que los conceptos centrales del capítulo quedaron claros. Pueden responderse sin cálculos.

**1.** La selección natural requiere tres condiciones simultáneas. Describe cada una con tus propias palabras y explica por qué la ausencia de cualquiera de ellas detendría el proceso evolutivo. Da un ejemplo de una situación donde se cumplan las tres.

**2.** El capítulo afirma que la selección natural no "elige lo mejor" sino que "elimina lo que no funciona". ¿Cuál es la diferencia práctica entre estas dos descripciones? ¿Por qué importa esta distinción para entender los límites de la adaptación?

**3.** Explica en qué sentido la selección natural es un proceso "ciego" —sin intención ni dirección consciente. Usa el ejemplo de la resistencia a antibióticos en bacterias para ilustrar tu respuesta.

**4.** ¿Qué es un paisaje adaptativo? Describe qué representan los picos y los valles, y explica por qué una población no siempre llega al pico más alto.

**5.** El capítulo distingue entre "óptimo local" y "óptimo global". Define ambos términos y describe una situación evolutiva concreta donde una población pudiera quedar atrapada en un óptimo local.

**6.** ¿Por qué el paisaje adaptativo no es fijo? Describe dos razones por las que puede cambiar a lo largo del tiempo y explica cómo esto complica la idea de que la evolución "optimiza" a los organismos.

---

## Sección II: Restricciones y espacio fenotípico

**7.** El capítulo describe tres tipos de restricciones que limitan el espacio fenotípico accesible: físicas, genético-del desarrollo, y filogenéticas. Da un ejemplo de cada tipo y explica cómo cada una reduce el espacio de posibilidades disponibles para la selección.

**8.** ¿Por qué las restricciones filogenéticas son especialmente relevantes para entender la evolución comparada con un proceso de optimización desde cero? Usa el ejemplo del ojo humano mencionado en el texto o propón uno propio.

**9.** El capítulo conecta las restricciones evolutivas con los "sesgos inductivos" que veremos en aprendizaje. ¿Qué tienen en común? ¿En qué sentido las restricciones no son obstáculos al proceso sino parte de cómo funciona?

---

## Sección III: El modelo matemático

**10.** ¿Qué es una ecuación en diferencia? Explica el concepto con el ejemplo del modelo de COVID presentado en el capítulo, e identifica cuál es el "estado" del sistema y cuál es la función de actualización.

**11.** Define covarianza con tus propias palabras. Sin usar fórmulas, explica qué significa una covarianza positiva, negativa y cercana a cero en el contexto de la relación entre un rasgo fenotípico y el fitness.

**12.** Considera una población de pájaros donde medimos la longitud del pico y el número de crías por temporada. Describe dos escenarios: uno donde la covarianza entre longitud del pico y éxito reproductivo sea positiva, y otro donde sea negativa. ¿Qué predice la ecuación de Price para cada caso?

**13.** La ecuación de Price simplificada es:

$$\Delta \bar{z} = \frac{\text{Cov}(w, z)}{\bar{w}}$$

¿Qué ocurre con $\Delta \bar{z}$ cuando la covarianza es cero? ¿Qué significa biológicamente ese resultado? ¿Puede cambiar el rasgo de todas formas? ¿Cómo?

**14.** ¿Por qué la ecuación de Price es también una ecuación en diferencia? Escribe explícitamente cómo $\bar{z}(t+1)$ depende de $\bar{z}(t)$ y señala la analogía con el modelo de COVID.

---

## Sección IV: La equivalencia con el aprendizaje

**15.** El capítulo presenta esta comparación:

| Selección natural | Aprendizaje por refuerzo |
|---|---|
| $\Delta \bar{z} = \text{Cov}(w,z) / \bar{w}$ | $\Delta V = \alpha(R - V)$ |

Identifica el término en cada ecuación que cumple el papel de "señal de actualización" y explica en qué sentido ambos términos miden una *discrepancia*.

**16.** ¿En qué se diferencian la evolución y el aprendizaje por refuerzo en cuanto a escala temporal, sustrato y tipo de "sistema" que se actualiza? ¿Por qué el capítulo afirma que estas diferencias son "de implementación, no de lógica"?

**17.** Describe el problema de la asignación de crédito tal como se presenta en la evolución. Luego reformúlalo en términos de aprendizaje: ¿cuál sería el equivalente del problema cuando un animal aprende qué estímulos predicen comida?

---

## Sección V: Aplicación e integración

**18.** Un estudiante dice: "La selección natural es básicamente lo mismo que el aprendizaje —la naturaleza aprende qué rasgos funcionan". Evalúa esta afirmación: ¿en qué sentido es correcta? ¿En qué sentido es imprecisa o incompleta?

**19.** El dilema exploración-explotación aparece tanto en evolución (mutación vs. selección) como en aprendizaje. Describe concretamente en qué consiste este dilema en cada dominio y explica por qué no existe una solución óptima única.

**20.** Al inicio del capítulo se afirman dos observaciones sobre el mundo natural: la variabilidad y el ajuste al entorno. Al finalizar la lectura, ¿cómo explica la teoría de la selección natural cada una de estas observaciones? Construye una respuesta que integre los conceptos de variabilidad heredable, selección diferencial, herencia, paisaje adaptativo y restricciones.

---

## Preguntas de profundización (optativas)

Estas preguntas no tienen respuesta única y están diseñadas para discusión o reflexión adicional.

**P1.** Si la selección natural es análoga a un algoritmo de búsqueda, ¿qué ventajas y desventajas tendría frente a un algoritmo que diseña soluciones desde cero? ¿Podría la evolución producir soluciones que un diseñador racional nunca consideraría?

**P2.** El capítulo afirma que la adaptación "es siempre relativa al contexto". ¿Qué implicaciones tiene esto para el concepto de progreso evolutivo? ¿Tiene sentido decir que los humanos son "más evolucionados" que las bacterias?

**P3.** La ecuación de Price fue derivada en 1970. Antes de su existencia, ¿cómo creen que los biólogos describían el cambio evolutivo? ¿Qué ganó la teoría al tener esta formalización matemática?
