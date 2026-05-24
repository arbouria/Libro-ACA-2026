# Capítulo 15: El Control Local del Comportamiento de Elección
## A. Bouzas
---

##  Borrador

El capítulo anterior documentó uno de los fenómenos más replicados de la psicología experimental: en equilibrio, los organismos distribuyen sus respuestas entre dos opciones de modo que la proporción de respuestas a cada alternativa iguala a la proporción de reforzadores que obtienen de ella. Mostramos que este resultado es compatible con dos tipos de explicación: que los organismos igualan la rentabilidad de cada opción, o que maximizan la tasa global de refuerzo a lo largo de la sesión. Ambas explicaciones operan sobre medidas agregadas — promedios calculados sobre sesiones completas — y ambas describen correctamente el estado de equilibrio. Lo que ninguna de las dos describe es el proceso que produce ese equilibrio.

Consideremos una situación cotidiana. Una persona trabaja frente a su computadora con dos fuentes de mensajes abiertas: el correo electrónico y la mensajería instantánea. Ambas llegan de manera intermitente e impredecible. La persona debe decidir, en cada momento, a cuál de las dos prestar atención. Mientras revisa los mensajes instantáneos, los correos se acumulan; mientras atiende el correo, los mensajes instantáneos se acumulan. En ninguno de los dos casos la atención continua a una sola fuente es sostenible: eventualmente la acumulación en la opción ignorada se vuelve suficientemente grande para atraer la atención de vuelta.

¿Qué regla sigue esta persona para decidir cuándo cambiar de una fuente a otra? Una posibilidad es que cambie cuando la probabilidad de que haya un mensaje nuevo en la opción alternativa supera a la probabilidad de que haya uno en la opción actual — es decir, que en cada instante vaya a donde la probabilidad de encontrar algo es mayor. Otra posibilidad es que estime, sobre los últimos minutos de experiencia, la tasa a la que llegan mensajes de cada fuente, y redistribuya su atención para igualar esas tasas locales. Las dos reglas producen el mismo resultado agregado — en equilibrio, el tiempo dedicado a cada fuente refleja la frecuencia relativa de mensajes de cada una — pero lo hacen mediante mecanismos diferentes y generan predicciones distintas sobre el patrón momento a momento de cambios de atención.

Esta es exactamente la pregunta de este capítulo. Sabemos qué distribuye el organismo en equilibrio; la pregunta es qué proceso momento a momento genera esa distribución. Los dos modelos que examinaremos comparten la premisa de que igualación no es una meta que el organismo persigue deliberadamente, sino el resultado de una regla de decisión local. Difieren en la variable que esa regla evalúa: el modelo de maximización momentánea propone que el organismo computa la probabilidad de refuerzo en el instante presente y elige la opción con probabilidad más alta; el modelo de mejoramiento propone que el organismo estima la tasa de refuerzo local de cada opción sobre el tiempo reciente que le ha dedicado, y se mueve hacia la opción más rentable. En ambos casos, la regla es simple y local; lo que resulta no trivial es que esa regla simple produzca igualación globalmente.

---

## Maximización Momentánea

El modelo de maximización momentánea, propuesto por Shimp en 1966, parte de una observación sobre la naturaleza de los programas de intervalo variable. En un programa concurrente IV-IV, la probabilidad de que una respuesta a cualquiera de las dos opciones sea reforzada no es constante: depende de cuánto tiempo ha transcurrido desde la última respuesta a cada opción. Un reforzador en los programas de intervalo variable se "arma" después de que transcurre el intervalo programado, y permanece disponible hasta que el organismo responde. Por tanto, conforme el organismo acumula respuestas consecutivas a una opción, el intervalo de la opción alterna sigue transcurriendo: la probabilidad de que un reforzador esté esperando en la alternativa crece con cada respuesta adicional a la opción actual.

Shimp argumentó que los organismos siguen esta lógica de manera precisa. Su propuesta es que en cada oportunidad de respuesta el organismo computa las probabilidades de refuerzo asociadas con cada opción en ese momento específico, y responde a la alternativa cuya probabilidad es más alta. La igualación global sería entonces un resultado emergente de esta regla local: si el organismo siempre va hacia donde la probabilidad de refuerzo es máxima, la distribución de su tiempo entre las opciones refleja, en promedio, la proporción relativa de reforzadores que cada una proporciona. Shimp verificó este resultado mediante simulación: el algoritmo de maximización momentánea produce igualación a nivel agregado.

La pregunta empírica es si los organismos reales siguen este algoritmo.

### Evaluación experimental: programas de ensayos discretos IV-IV

Para estudiar la predicción del modelo, el protocolo de *programas libres* — donde el organismo puede cambiar de opción en cualquier momento — presenta una dificultad: es difícil definir y contar "secuencias de *n* respuestas consecutivas a una misma opción" cuando el animal puede migrar entre teclas en cualquier instante. Los *programas concurrentes de ensayos discretos* resuelven este problema forzando una sola respuesta por oportunidad. El procedimiento es el siguiente: se presenta al organismo una oportunidad de respuesta breve — típicamente unas pocas segundos — durante la cual puede elegir una de las dos alternativas con una sola respuesta. Después de la respuesta, un intervalo entre ensayos de varios segundos cierra la oportunidad de elección. Al finalizar ese intervalo, se presenta una nueva oportunidad. Lo que es crítico para interpretar los resultados es que los programas de intervalo siguen corriendo durante el intervalo entre ensayos como si no hubiera discontinuidades: cuando un reforzador se acumula en una de las opciones, permanece disponible hasta que el organismo responda a ella. Así, cada respuesta adicional a la misma tecla aumenta la probabilidad de que un reforzador esté esperando en la alternativa.

La predicción del modelo es entonces perfectamente operacionalizable: la probabilidad de que el organismo cambie de opción debe aumentar con el número de elecciones consecutivas de una misma alternativa, siguiendo exactamente el ritmo al que crece la probabilidad de refuerzo en la opción no elegida.

En el experimento más influyente con este protocolo, Nevin (1969) empleó un programa concurrente IV-IV con palomas y midió la secuencia de elecciones durante sesiones extensas. Los resultados produjeron dos hallazgos que conviene mantener separados porque responden preguntas distintas.

El primer hallazgo concierne directamente a la predicción del modelo. La probabilidad de que un reforzador esté disponible en la opción alterna crece sistemáticamente con el número de elecciones consecutivas de la opción actual — esto es exactamente lo que los programas de intervalo garantizan por construcción. Sin embargo, la probabilidad de que el organismo *cambie* de opción no crece en función de ese número de elecciones consecutivas. Los animales no respondían a la tecla roja con mayor frecuencia a medida que acumulaban más respuestas en la tecla verde, aunque la probabilidad de refuerzo para rojo aumentara de manera regular. Este resultado es contrario a la predicción central del modelo.

**[FIGURA 15.1: Dos paneles. Panel superior: probabilidad de refuerzo para la opción alterna (eje vertical) en función del número de elecciones consecutivas de la opción actual (eje horizontal). La curva es creciente, mostrando que los programas IV acumulan disponibilidad de refuerzo. Panel inferior: probabilidad observada de cambiar de opción (eje vertical) en función del número de elecciones consecutivas. La curva es plana o decreciente — contraria a la predicción del modelo. Paleta del libro; el panel inferior debe destacarse porque es el resultado crítico.]**

El segundo hallazgo emerge de un reanálisis que Nevin realizó sobre sus datos originales y sobre los datos de un experimento de Silberberg et al. (1978). Al examinar la probabilidad de cambiar de opción no como función de la probabilidad de refuerzo en la alternativa, sino en términos de la historia de respuestas del propio organismo, ambos experimentos mostraron el mismo patrón: la probabilidad de repetir una elección era alta e independiente de si esa respuesta había sido reforzada en el ensayo anterior. Los organismos tendían a *permanecer* en la opción que habían elegido, no a cambiar según el cálculo de probabilidades. Este efecto de perseverancia no estaba previsto por el modelo y sugiere que el control local del comportamiento incorpora una inercia que el modelo de maximización momentánea ignora.

**[FIGURA 15.2: Probabilidad de cambiar de tecla en función del número de respuestas consecutivas previas, para los datos de Nevin (1969) y Silberberg et al. (1978). Ambas curvas son planas o decrecientes. La figura muestra dos experimentos distintos convergiendo en el mismo patrón, lo que refuerza la robustez del resultado.]**

### Evaluación experimental: programas de ensayos discretos RV-IV

Un segundo protocolo permite una prueba más limpia de la maximización momentánea porque la asimetría entre los dos programas hace la predicción todavía más específica. En un programa concurrente RV-IV de ensayos discretos, la probabilidad de refuerzo para la opción asociada al programa de razón variable es constante en todos los ensayos — no depende del tiempo transcurrido ni de la historia reciente. En cambio, la probabilidad de refuerzo para la opción IV sí depende del tiempo: crece con cada ensayo adicional desde la última respuesta a esa opción. 

Una estrategia consistente con maximización momentánea sería clara: inmediatamente después de recibir un reforzador en la opción IV — momento en el que la probabilidad de un nuevo reforzador IV es mínima — el organismo debería responder al RV, cuya probabilidad de refuerzo no cambia. Conforme pasan más ensayos en el RV, la probabilidad de refuerzo para el IV crece; en algún punto, la probabilidad IV supera a la del RV y el organismo debería cambiar. La predicción es una función creciente: la probabilidad de responder al IV debe aumentar monotónicamente con el número de ensayos desde la última respuesta IV.

Williams (1985) puso a prueba esta predicción con palomas en programas concurrentes RV-IV con distintas combinaciones de valores. Los resultados fueron inequívocos en dos sentidos. Primero, los organismos sí igualaron a nivel molar — la frecuencia relativa de respuestas al IV igualó a la frecuencia relativa de reforzadores del IV — lo que confirma una vez más la robustez de la ley de igualación. Segundo, y esto es lo crítico, la probabilidad de responder al IV no creció como función del número de ensayos desde la última respuesta IV, a pesar de que la probabilidad de que un reforzador estuviera disponible en esa opción sí crecía de manera ordenada. La función observada era plana o ligeramente decreciente — opuesta en su forma a la predicción del modelo.

**[FIGURA 15.3: Dos paneles. Panel izquierdo: probabilidad de que un reforzador esté disponible en la opción IV como función del número de ensayos desde la última respuesta IV. La curva es creciente. Panel derecho: probabilidad observada de responder al IV como función del número de ensayos desde la última respuesta IV. La curva es plana o decreciente para sujetos individuales, contraria a la predicción. Reproduce el estilo de la figura original de Williams.]**

### Conclusiones sobre el modelo de maximización momentánea

Los experimentos con programas de ensayos discretos — tanto IV-IV como RV-IV — convergen en un diagnóstico claro: la maximización momentánea no describe el proceso que genera igualación. Los organismos no computan la probabilidad de refuerzo en el instante presente y responden en consecuencia. Tres regularidades destacan en su lugar. La primera es que la ocurrencia de un reforzador sí aumenta la probabilidad de repetir la misma respuesta — este efecto del refuerzo reciente es consistente con la ley del efecto y con los modelos de aprendizaje que ya conocemos. La segunda es la perseverancia: los organismos repiten una elección con mayor probabilidad por el simple hecho de haberla emitido recientemente, independientemente de si fue reforzada. La tercera es que la sensibilidad a la secuencia de ensayos puede verse afectada por el intervalo entre elecciones y por otros factores que influyen en la memoria sobre las respuestas recientes.

La implicación más importante, sin embargo, es conceptual: igualación puede ocurrir sin que el organismo esté maximizando la probabilidad de refuerzo en cada elección individual. El patrón global emerge sin que el mecanismo local lo "apunte" directamente. Esto deja abierta la pregunta de qué sí hace el organismo en cada momento — y esa es exactamente la pregunta que los dos modelos siguientes intentan responder.

---

## Modelo de Mejoramiento

El modelo de mejoramiento (*melioration*) fue propuesto por Herrnstein y Vaughan (1980) como una descripción del proceso momento-a-momento que produce igualación en programas concurrentes. Como todos los modelos de esta familia, el mejoramiento tiene dos componentes: una *variable de decisión* — la cantidad que el organismo evalúa en cada oportunidad de respuesta — y una *regla de respuesta* — el criterio con el que elige.

La variable de decisión en el modelo de mejoramiento son las *tasas locales de refuerzo* de cada alternativa, que corresponden a lo que en el capítulo anterior llamamos rentabilidad de las opciones. La tasa local de refuerzo de una opción es el cociente entre el número de reforzadores obtenidos en esa opción y el tiempo que el organismo le dedica:

$$\frac{r_i}{T_i}$$

A diferencia de la tasa global — que divide el número de reforzadores entre el tiempo total de la sesión — la tasa local divide entre el tiempo asignado específicamente a esa opción. Esta distinción es fundamental: el tiempo que el organismo pasa en la opción 1 no contribuye al denominador de la tasa local de la opción 2, y viceversa.

La regla de respuesta del modelo de mejoramiento es una variante de maximización: en cada momento, el organismo asigna más tiempo a la opción cuya tasa de refuerzo local es más alta. Esta regla genera un sistema dinámico de retroalimentación. Al aumentar el tiempo asignado a la opción más rentable, el denominador de su tasa local crece — su rentabilidad disminuye. Simultáneamente, el tiempo asignado a la opción alternativa decrece, reduciendo el denominador de su tasa local — su rentabilidad aumenta. El sistema se auto-corrige hasta que las dos tasas locales son iguales, punto en el que el organismo ya no tiene incentivo para redistribuir su tiempo.

### El ejemplo numérico

Consideren un programa concurrente IV 1 min – IV 2 min en una sesión de una hora. Un supuesto importante: asumiremos que el organismo responde a una tasa suficientemente alta como para obtener prácticamente todos los reforzadores disponibles cada vez que visita una opción. Esto es posible en los programas de intervalo variable porque los reforzadores que se arman mientras el organismo está en la otra opción *se acumulan y esperan*: cuando el organismo regresa, los recoge con su siguiente respuesta. La cantidad de reforzadores que el organismo obtiene de cada opción depende, por tanto, del número total de reforzadores que el programa puede generar en la sesión — no de cuánto tiempo pasa activamente en esa opción.

Con este supuesto, la tasa máxima posible de reforzadores para el IV 1' es de 60 por hora; para el IV 2', es de 30 por hora. Supongamos que al inicio de una sesión el organismo asigna la mitad de su tiempo a cada opción (0.5 hr cada una). Las tasas locales de refuerzo serían:

$$\frac{60}{0.5\text{ hr}} = 120 \text{ ref/hr} \qquad \text{(IV 1')}$$
$$\frac{30}{0.5\text{ hr}} = 60 \text{ ref/hr} \qquad \text{(IV 2')}$$

La opción IV 1' es más rentable. El modelo predice que el organismo asignará más tiempo a esa alternativa. Supongamos que lo lleva al 90% de su tiempo:

$$\frac{60}{0.9\text{ hr}} = 66.7 \text{ ref/hr} \qquad \text{(IV 1')}$$
$$\frac{30}{0.1\text{ hr}} = 300 \text{ ref/hr} \qquad \text{(IV 2')}$$

Al invertir tanto tiempo en el IV 1', su rentabilidad colapsó a 66.7; mientras tanto, el IV 2', que recibió solo el 10% del tiempo, tiene ahora una tasa local de 300 ref/hr — cinco veces mayor. El organismo ahora reasignará tiempo al IV 2'. El sistema oscila así alrededor del punto donde las dos tasas locales son iguales.

Para encontrar ese punto de equilibrio formalmente, llamamos $T_1$ y $T_2$ a las proporciones de tiempo asignadas a cada opción ($T_1 + T_2 = 1$). En el equilibrio, la tasa local de refuerzo de ambas opciones debe ser idéntica:

$$\frac{r_1}{T_1} = \frac{r_2}{T_2}$$

Reorganizando:

$$\frac{T_1}{T_2} = \frac{r_1}{r_2}$$

Esta es exactamente la ley de igualación. La conclusión es notable: el organismo no necesita "conocer" la ley de igualación ni computar proporciones relativas. Basta con que siga la regla local de elegir la opción más rentable en cada momento; la igualación global es el estado de equilibrio de ese proceso de retroalimentación.

Para el ejemplo numérico, el equilibrio se alcanza cuando $T_1/T_2 = 60/30 = 2$, es decir, cuando el organismo dedica dos tercios de su tiempo al IV 1' y un tercio al IV 2':

$$\frac{60}{2/3} = 90 \text{ ref/hr} = \frac{30}{1/3} \quad \checkmark$$

En ese punto, ambas opciones ofrecen exactamente la misma tasa local de 90 ref/hr, y la distribución de tiempo cumple:

$$\frac{2/3}{2/3 + 1/3} = \frac{60}{60 + 30} = \frac{2}{3}$$

En el simulador correspondiente pueden explorar la dinámica del sistema para distintas combinaciones de programas concurrentes IV-IV, observando cómo el organismo oscila alrededor del punto de igualación desde diferentes puntos de partida.

**[FIGURA 15.4: Dinámica del modelo de mejoramiento. Eje horizontal: proporción de tiempo asignada a la opción 1. Eje vertical: tasa local de refuerzo. Dos curvas: tasa local de opción 1 (decreciente) y tasa local de opción 2 (creciente). La intersección marca el punto de equilibrio. Flechas horizontales muestran la dirección de movimiento del sistema a ambos lados del equilibrio.]**

### Una limitación importante

El modelo de mejoramiento deja sin especificar la ventana temporal sobre la que el organismo estima las tasas locales. ¿Las estima a lo largo de la sesión completa? ¿Sobre los últimos diez minutos? ¿Reinicia el cómputo después de cada reforzador? Esta indeterminación no es un detalle menor: la respuesta tiene consecuencias profundas cuando las condiciones del entorno cambian a lo largo del tiempo. En entornos donde la disponibilidad de reforzadores fluctúa — que es la norma en el mundo natural, no la excepción — el tamaño de la ventana temporal determina qué tan rápido puede el organismo adaptarse a los cambios. Un organismo que promedia sobre ventanas muy largas será lento para detectar cambios; uno que usa ventanas cortas será veloz pero susceptible al ruido. Este problema — la elección adaptativa de la escala temporal de estimación — es uno de los temas centrales del módulo de incertidumbre, más adelante en el libro.

---

## Conclusión

Los dos modelos revisados en este capítulo comparten la premisa de que igualación es un fenómeno emergente — el resultado de un proceso, no su causa — y que ese proceso opera en una escala temporal mucho más fina que las sesiones completas sobre las que se calcula la igualación. Donde difieren es en la variable que gobierna la decisión local.

El modelo de maximización momentánea falla en su predicción más específica: los organismos no responden a la opción con mayor probabilidad instantánea de refuerzo. Lo que sí se observa — el efecto de perseverancia documentado por Nevin y Silberberg — no estaba previsto por el modelo y sugiere que el control local del comportamiento incorpora inercia, no solo sensibilidad probabilística. La maximización momentánea resulta demasiado reactiva al estado del entorno instante a instante.

El modelo de mejoramiento resuelve esto apelando a una escala temporal intermedia: el organismo estima la tasa de refuerzo sobre el tiempo que ha dedicado recientemente a cada opción, y redistribuye su comportamiento para reducir la diferencia entre esas tasas. Este proceso de retroalimentación negativa converge exactamente al punto de igualación — no como una meta programada, sino como el estado en el que ya no existe diferencia entre las tasas locales y, por tanto, ya no existe incentivo para redistribuir. La condición formal de equilibrio resulta ser algebraicamente idéntica a la ley de igualación, lo que convierte al mejoramiento en la explicación mecanística más completa del fenómeno que documentamos en el capítulo anterior.

La limitación principal del modelo no es empírica sino de especificación: no determina la ventana temporal sobre la que se estiman las tasas locales. En entornos estables esa omisión es tolerable; en entornos que cambian — la norma fuera del laboratorio — la elección de esa ventana determina qué tan rápido puede adaptarse el organismo, y ese problema requiere herramientas que desarrollaremos en módulos posteriores.

Volviendo al ejemplo con el que abrimos: la persona que alterna entre correos y mensajes instantáneos no computa probabilidades de llegada en cada instante ni maximiza globalmente sobre toda la jornada. Estima, de manera implícita, la tasa reciente de mensajes en cada canal, y redistribuye su atención cuando la diferencia entre esas tasas se vuelve suficientemente grande. Igualación emerge de esa regla simple, sin que la persona la conozca ni la aplique deliberadamente.

---

## Resumen

La igualación global que documentamos en el capítulo anterior puede ser el resultado de mecanismos muy distintos que operen a nivel local. El modelo de maximización momentánea propone que el organismo elige en cada instante la opción con mayor probabilidad de refuerzo; la evidencia de experimentos de ensayos discretos — tanto IV-IV como RV-IV — no apoya esta predicción. El efecto de perseverancia observado en ambos protocolos indica que el comportamiento de elección incorpora inercia que el modelo no contempla. El modelo de mejoramiento propone que el organismo estima las tasas de refuerzo locales de cada opción y se mueve para reducir la diferencia entre ellas; este proceso de retroalimentación negativa converge al punto de igualación como su equilibrio natural, y la condición formal de ese equilibrio es algebraicamente idéntica a la ley de igualación.

---

## Conexiones

### Hacia atrás

**Sistemas de retroalimentación (capítulo 5).** El modelo de mejoramiento es un sistema de retroalimentación negativa en el sentido más preciso del capítulo 5: el organismo mide la discrepancia entre las tasas locales de las dos opciones y se mueve para reducirla. El punto de equilibrio — donde la discrepancia es cero y el organismo deja de redistribuir su comportamiento — corresponde exactamente al punto de igualación. La novedad respecto al capítulo 5 es que la variable comparada no es una magnitud física sino una tasa de reforzamiento que el propio comportamiento del organismo contribuye a determinar.

**Igualación en programas concurrentes (capítulo 14).** Los dos modelos de este capítulo buscan explicar el mismo fenómeno que documentamos en el capítulo anterior, pero desde la escala temporal del proceso que lo genera. La contribución central de los experimentos de ensayos discretos es demostrar que el equilibrio molar puede coexistir con mecanismos moleculares que no lo apuntan directamente: igualación emerge sin que el organismo la calcule.

**Programas de refuerzo (capítulo 13).** La razón por la que el mejoramiento funciona donde la maximización momentánea falla tiene que ver con una propiedad específica de los programas de intervalo variable: los reforzadores se acumulan mientras el organismo atiende la otra opción. Esta propiedad — descrita formalmente cuando analizamos las funciones de retroalimentación de los programas IV — es la que da al mejoramiento su dinámica característica y la que hace inteligible el ejemplo numérico del equilibrio.

### Hacia adelante

**Maximización global: Premack, Staddon y Rachlin (capítulos siguientes).** El mejoramiento es un modelo local: opera sobre la diferencia entre tasas estimadas en ventanas recientes. La familia de modelos de maximización global propone una perspectiva complementaria: los organismos distribuyen su comportamiento de modo que maximizan alguna cantidad definida sobre la sesión completa o sobre períodos aún más largos. Entender qué predicciones distinguen estas dos familias — y en qué condiciones cada una se aproxima mejor a los datos — es el problema de los capítulos siguientes.

**La ley del efecto relativa (capítulo posterior).** El modelo de mejoramiento describe cómo el organismo redistribuye su comportamiento entre opciones, pero no especifica cómo se determina el valor de cada opción a partir de su historia de reforzamiento. La ley del efecto relativa de Herrnstein completa ese cuadro: propone que el valor de una respuesta depende de su tasa de reforzamiento en relación al reforzamiento total disponible en el contexto. Esa dependencia contextual del valor, que el mejoramiento asume implícitamente, es la pieza que conecta los modelos moleculares de elección con los modelos de aprendizaje de valor que construimos en los bloques anteriores del libro.

**Incertidumbre y volatilidad ambiental (módulo posterior).** La limitación más seria del mejoramiento — la indeterminación de la ventana temporal para estimar tasas locales — se convierte en el problema central cuando el entorno cambia. La investigación contemporánea con protocolos de entornos volátiles estudia cómo los organismos ajustan esa escala temporal en función de la incertidumbre sobre el estado actual del entorno. En esos contextos, la exploración de opciones cuyo valor es incierto reemplaza al mejoramiento como principio explicativo.

---

## Ejercicios

**1.** Un programa concurrente IV 1' – IV 4' opera durante una sesión de una hora. Asumiendo que el organismo responde lo suficientemente rápido para recolectar todos los reforzadores disponibles, calcula las tasas locales de refuerzo si el organismo asigna el 50%, el 80% y el 20% de su tiempo a la opción IV 1'. ¿En cuál de los tres casos las tasas locales son iguales? Verifica que ese punto coincide con la predicción de igualación.

**2.** El modelo de maximización momentánea y el modelo de mejoramiento producen ambos igualación en equilibrio, pero mediante procesos diferentes. Explica qué observación empírica permite distinguirlos experimentalmente. ¿Qué patrón de resultados esperarías de cada modelo en un experimento de ensayos discretos que mida la probabilidad de cambiar de opción como función del número de respuestas consecutivas a la opción actual?

**3.** En el experimento de Nevin (1969), los animales mostraron perseverancia: la probabilidad de repetir la elección anterior era alta independientemente de si esa elección había sido reforzada. ¿Qué implicaciones tiene este resultado para la ley del efecto? ¿Es compatible con el modelo de Bush y Mosteller que estudiamos en el capítulo 8? Explica tu razonamiento.

**4.** El modelo de mejoramiento predice que el sistema converge al punto de igualación desde cualquier punto de partida. Usa el ejemplo numérico del capítulo (IV 1' – IV 2', sesión de una hora) y calcula las tasas locales si el organismo comienza asignando el 10% de su tiempo al IV 1'. ¿En qué dirección se moverá el sistema? ¿Hacia dónde se movería si comenzara con el 90%? ¿Cuántos pasos de ajuste imaginás que tomaría converger al equilibrio?

**5.** El modelo de mejoramiento deja sin especificar la ventana temporal sobre la que el organismo estima las tasas locales de refuerzo. Describe dos contextos naturales —uno donde una ventana corta sería adaptativa y uno donde una ventana larga lo sería— y explica por qué en cada caso. ¿Qué propiedad del entorno determinaría cuál ventana es más apropiada?

**6.** *(Reflexión)* Este capítulo mostró que igualación puede producirse sin que el organismo tenga representación del patrón global que está produciendo. ¿Cómo se relaciona esto con la distinción entre el nivel computacional y el nivel algorítmico de explicación que introdujimos al inicio del libro? ¿Qué dice sobre la relación entre las metas funcionales de un sistema y los mecanismos que las implementan?

---

## Lecturas Recomendadas

**Shimp, C. P. (1966).** Probabilistically reinforced choice behavior in pigeons. *Journal of the Experimental Analysis of Behavior, 9*, 443–455. — La propuesta original del modelo de maximización momentánea y su derivación de igualación por simulación. Vale la pena leer la sección de simulación, que es inusualmente clara para la época.

**Nevin, J. A. (1969).** Interval reinforcement of choice behavior in discrete trials. *Journal of the Experimental Analysis of Behavior, 12*, 875–885. — El experimento de ensayos discretos IV-IV que puso a prueba y refutó la maximización momentánea. La figura de los dos paneles — probabilidad de refuerzo creciente versus probabilidad de cambio plana — es uno de los resultados más limpios del área.

**Williams, B. A. (1985).** Choice behavior in a discrete-trial concurrent schedule: A test of maximizing theories. *Learning and Motivation, 16*, 423–443. — El experimento RV-IV de ensayos discretos. Diseño especialmente limpio porque la asimetría entre los dos programas hace la predicción del modelo perfectamente específica. Los datos de probabilidad de respuesta al IV plana o decreciente son concluyentes.

**Herrnstein, R. J., & Vaughan, W. (1980).** Melioration and behavioral allocation. En J. E. R. Staddon (Ed.), *Limits to Action: The Allocation of Individual Behavior* (pp. 143–176). Academic Press. — La propuesta original del mejoramiento. El capítulo incluye la derivación formal del equilibrio y varios experimentos de evaluación. Herrnstein escribe con una claridad inhabitual para escritura técnica.

**Silberberg, A., Hamilton, B., Ziriax, J. M., & Casey, J. (1978).** The structure of choice. *Journal of Experimental Psychology: Animal Behavior Processes, 4*, 368–398. — El reanálisis de los datos de Nevin y nuevos datos propios que documentan el efecto de perseverancia. La combinación de los dos conjuntos de datos — con diseños ligeramente distintos — fortalece la conclusión sobre igualación sin maximización momentánea.

**Staddon, J. E. R. (2001).** *Adaptive Dynamics: The Theoretical Analysis of Behavior.* MIT Press. — Los capítulos sobre elección presentan el mejoramiento como un caso especial de dinámica adaptativa en lazo cerrado, con análisis de estabilidad y extensiones a entornos cambiantes. El tratamiento formal complementa la presentación intuitiva de este capítulo.
