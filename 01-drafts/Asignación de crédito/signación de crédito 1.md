# # Capítulo 8: Asignación de Crédito para Estímulos

**Objetivos del capítulo:**
- Comprender el problema de asignación de crédito y su importancia adaptativa
- Identificar los sesgos inductivos que reducen el espacio de candidatos
- Distinguir entre condiciones necesarias y suficientes para el aprendizaje
- Reconocer evidencia de competencia entre elementos por asignación de crédito

---

## Introducción: El Problema Fundamental

Imagina que regresas a casa después de comer en un restaurante nuevo y experimentas un fuerte malestar estomacal. ¿Qué causó tu enfermedad? Las posibilidades son abrumadoras:

- El sabor del platillo que ordenaste
- El olor del restaurante
- La música que sonaba
- El color de las paredes
- La hora del día
- Tu compañero de mesa
- Algo que comiste ayer
- Algo que tocaste en el transporte público
- El estrés de tu día

Esta lista podría extenderse indefinidamente hacia el pasado. Cada segundo de tu vida antes del malestar contiene miles de eventos que, en principio, podrían ser la causa. **¿Cómo determinas cuál fue realmente responsable?**

Este es el **problema de asignación de crédito**: dado un resultado importante (en este caso, enfermedad), ¿a cuál de los incontables eventos que lo precedieron debemos atribuirle la responsabilidad?

### Por Qué Este Problema es Crucial

En el Capítulo 2 establecimos que la tarea fundamental de un organismo es **reducir la incertidumbre** acerca de la ocurrencia de sucesos biológicamente importantes (SBI). Para lograrlo, debe identificar las **señales predictivas** en su entorno. Pero el entorno es un flujo constante de estimulación: en cualquier momento, cientos de estímulos están presentes simultáneamente. Sin algún mecanismo para filtrar este vasto espacio de posibilidades, el aprendizaje sería imposible.

La selección natural resolvió este problema desarrollando **sesgos inductivos**: mecanismos que sistemáticamente reducen el espacio de candidatos a la asignación de crédito y establecen un orden de prioridad para evaluarlos.

En este capítulo exploraremos:
1. ¿Cuáles son estos sesgos?
2. ¿Qué tan efectivos son?
3. ¿Cuáles son sus límites?

Nos concentraremos en el **aprendizaje asociativo**: cómo los organismos aprenden que ciertos **estímulos** (eventos en el mundo) predicen ciertos **resultados** (SBI). En el próximo capítulo (Cap 9) abordaremos el problema paralelo de cómo los organismos aprenden que ciertas **acciones** producen ciertos resultados.

---

## Parte I: El Paradigma de Pavlov y el Sesgo de Contigüidad

### El Punto de Partida Histórico

A principios del siglo XX, Ivan Pavlov diseñó una serie de experimentos que se convertirían en la base del estudio del aprendizaje asociativo. Su protocolo, aunque simple, fue revolucionario:

**Procedimiento básico:**
1. Presentar un estímulo inicialmente neutral (ej: un tono)
2. Seguirlo por un estímulo biológicamente importante (ej: comida)
3. Repetir este apareamiento múltiples veces
4. Evaluar: ¿El tono ahora provoca respuestas similares a las que provoca la comida?

**Terminología:**
- **Estímulo Condicionado (EC)**: El estímulo inicialmente neutral (tono)
- **Estímulo Incondicionado (EI/SBI)**: El estímulo biológicamente importante (comida)
- **Respuesta Condicionada (RC)**: La respuesta que emerge al EC después del entrenamiento
- **Respuesta Incondicionada (RI)**: La respuesta natural al EI

**Resultado**: Después de múltiples apareamientos EC→EI, los perros comenzaban a **salivar al tono**, aunque el tono nunca había tenido valor nutritivo.

[**FIGURA 8.1**: Diagrama del procedimiento de condicionamiento clásico de Pavlov]

### Contigüidad como Primer Sesgo Inductivo

El hallazgo de Pavlov sugirió que la **contigüidad temporal** entre eventos podría ser el principio fundamental del aprendizaje. La contigüidad reduce drásticamente el espacio de candidatos:

**Regla de contigüidad:**
> "Solo considera como candidatos a predecir el SBI a aquellos eventos que ocurren temporalmente cerca de él"

En nuestro ejemplo del restaurante, este sesgo te llevaría a considerar solo lo que comiste en esa comida, no lo que comiste ayer ni la música que escuchaste.

### Variaciones Temporales: El Gradiente de la Demora

Pavlov y sus sucesores exploraron sistemáticamente diferentes **relaciones temporales** entre EC y EI:

**1. Condicionamiento Simultáneo**
- EC y EI inician y terminan juntos
- Aprendizaje: Pobre

**2. Condicionamiento de Demora Corta**
- EC inicia, luego EI se presenta (mientras EC continúa)
- Demora: 0.5 - 2 segundos
- Aprendizaje: Excelente

**3. Condicionamiento de Demora Larga**
- EC inicia, demora extensa, luego EI
- Demora: varios segundos a minutos
- Aprendizaje: Disminuye con la demora

**4. Condicionamiento de Huella**
- EC termina, demora, luego EI inicia
- Aprendizaje: Disminuye con la demora

**5. Condicionamiento Hacia Atrás**
- EI se presenta primero, luego EC
- Aprendizaje: Mínimo o nulo

[**FIGURA 8.2**: Diagramas temporales de diferentes procedimientos de condicionamiento]

**Patrón general - Gradiente de la demora:**
La fuerza del condicionamiento disminuye conforme aumenta el intervalo temporal entre EC y EI. Dependiendo del sistema (visual, gustativo, etc.), después de menos de un minuto de intervalo, el aprendizaje puede ser nulo.

**Implicación:** La contigüidad no es binaria (presente/ausente) sino **gradual**. Mientras más cercanos en el tiempo, mayor es el crédito asignado.

---

## Parte II: ¿Es la Contigüidad Necesaria?

Si la contigüidad es el principio fundamental, entonces debería ser una **condición necesaria**: sin contigüidad, no debería haber aprendizaje.

Pero un experimento casual de John García cambió radicalmente esta perspectiva.

### El Experimento Accidental de García

**Contexto:** García estudiaba los efectos de la radiación en ratas. Accidentalmente notó que las ratas desarrollaban aversión a su comida habitual después de ser irradiadas, a pesar de que el malestar ocurría **horas** después de comer.

**Experimento sistemático (García & Koelling, 1966):**

**Fase 1: Entrenamiento**
- Todas las ratas beben agua azucarada ("dulce")
- Cada lengüetazo activa un click y luz ("brillante-ruidosa")
- Compuesto: Sabor DULCE + Estímulo audiovisual BRILLANTE-RUIDOSO

**Fase 2: Consecuencias (dividido en dos grupos)**
- Grupo A: Descarga eléctrica inmediata en las patas
- Grupo B: Inyección que causa malestar estomacal (con demora de horas)

**Fase 3: Prueba**
- Opción 1: Agua dulce (sin audiovisual)
- Opción 2: Agua normal con brillante-ruidoso

**Resultados (ver Fig 8.3):**
- Grupo A (descarga): Evita BRILLANTE-RUIDOSO, no evita DULCE
- Grupo B (enfermedad): Evita DULCE, no evita BRILLANTE-RUIDOSO

[**FIGURA 8.3**: Resultados del experimento de García & Koelling mostrando selectividad de asociación]

### Implicaciones Profundas

**1. La contigüidad NO es necesaria:**
Las ratas aprenden aversión a sabores con demoras de **horas** entre consumo y enfermedad. Esto viola el gradiente de demora establecido por Pavlov.

**2. Existe un sesgo de RELEVANCIA BIOLÓGICA:**
No todos los estímulos contiguos con el SBI son candidatos iguales. El **tipo de SBI** determina qué dimensiones de estimulación son consideradas:

- Enfermedad estomacal → Considerar SABORES (no visuales/auditivos)
- Dolor externo → Considerar estímulos AUDIOVISUALES (no sabores)

**¿Por qué este sesgo evolucionó?**

Para especies omnívoras como ratas (y humanos):
- **Problema adaptativo**: Identificar alimentos tóxicos
- **Información relevante**: El sabor es la señal confiable de toxinas
- **Demora inevitable**: Los efectos tóxicos toman tiempo en manifestarse

La selección natural favoreció un sistema que:
- Tolera demoras largas para asociaciones sabor→enfermedad
- Restringe estas asociaciones a la dimensión relevante (sabor)

**Contraste con otras especies:**

**Palomas (aves):**
- Forrajean visualmente (buscan semillas/insectos por color/forma)
- **No** aprenden aversiones a sabores fácilmente
- **Sí** aprenden aversiones a estímulos visuales asociados con toxicidad

**Ejemplo en coevolución:**
- Polillas tóxicas → Patrones visuales llamativos (aposematismo)
- Aves depredadoras → Aprenden evitar esos patrones visuales
- Polillas no-tóxicas → Evoluciona mimetismo (parecerse a las tóxicas)

[**FIGURA 8.4**: Ilustración de aposematismo y mimetismo en polillas y aves]

### Otros Sesgos Revelados por García

**Experimento de novedad:**
- Presentar dos sabores: uno familiar, uno novedoso
- Ambos igualmente contiguos con enfermedad
- Resultado: Aversión se desarrolla solo al sabor **novedoso**

**Sesgo de NOVEDAD:**
> "Prioriza estímulos novedosos sobre familiares al asignar crédito"

**Racionalidad adaptativa:** Si un alimento familiar nunca te ha enfermado antes, es poco probable que sea el culpable ahora. El nuevo alimento es el candidato más probable.

**Evidencia adicional del gradiente temporal (incluso con relevancia biológica):**
Aunque las demoras largas son toleradas, el aprendizaje sigue siendo más fuerte cuando la demora es menor. En experimentos donde se presentan dos sabores antes de la enfermedad, la aversión es mayor al sabor **temporalmente más cercano** al malestar.

---

## Parte III: ¿Es la Contigüidad Suficiente?

Hasta ahora hemos visto que la contigüidad no es necesaria (García). Ahora preguntamos: ¿es **suficiente**? Es decir, ¿basta con que un estímulo esté contiguo con un SBI para que se le asigne crédito?

Si la respuesta fuera "sí", entonces todos los estímulos igualmente contiguos con un SBI deberían adquirir el mismo valor predictivo. Pero varios experimentos demuestran que esto no es así.

### Ensombrecimiento (Overshadowing)

**Experimento de Reynolds (1961):**

**Diseño:**
Dos palomas entrenad as a discriminar entre dos teclas:
- Tecla + (reforzada): Triángulo blanco sobre fondo rojo
- Tecla - (no reforzada): Círculo blanco sobre fondo verde

Ambas palomas aprenden a picotear solo la tecla +.

**Prueba crítica:**
Presentar los cuatro estímulos **por separado**:
- Triángulo (sin color)
- Rojo (sin forma)
- Círculo (sin color)
- Verde (sin forma)

**Resultado:**
- Paloma 1: Responde solo a TRIÁNGULO (ignora rojo)
- Paloma 2: Responde solo a ROJO (ignora triángulo)

[**FIGURA 8.5**: Diseño y resultados del experimento de Reynolds mostrando ensombrecimiento]

**Implicación:**
Aunque tanto forma como color estaban **igualmente contiguos** con el refuerzo, **solo uno** de ellos adquirió control sobre el comportamiento. Los elementos del compuesto **compitieron** por la asignación de crédito.

**Factores que determinan qué elemento "gana":**
1. **Saliencia (intensidad)**: Estímulos más intensos/conspicuos dominan
2. **Relevancia biológica**: Dimensiones relevantes para el SBI dominan
3. **Novedad**: Estímulos novedosos dominan sobre familiares
4. **Historia previa**: Como veremos en bloqueo...

### Bloqueo (Blocking) - El Hallazgo Crucial

El experimento de bloqueo de Leon Kamin (1969) es uno de los hallazgos más importantes en la historia del estudio del aprendizaje.

**Diseño de dos grupos:**

**GRUPO EXPERIMENTAL:**
- Fase 1: Luz → Descarga eléctrica (múltiples ensayos)
- Fase 2: [Luz + Tono] → Descarga eléctrica
- Prueba: ¿Cuánto miedo provoca el Tono solo?

**GRUPO CONTROL:**
- Fase 1: (Nada - no recibe entrenamiento previo)
- Fase 2: [Luz + Tono] → Descarga eléctrica  
- Prueba: ¿Cuánto miedo provoca el Tono solo?

**Predicción de contigüidad:**
En Fase 2, ambos grupos reciben exactamente la misma experiencia: [Luz+Tono] contiguo con descarga. Por tanto, ambos grupos deberían aprender igual sobre el Tono.

**Resultado empírico:**
- Grupo Control: Tono provoca **miedo fuerte**
- Grupo Experimental: Tono provoca **poco o ningún miedo**

[**FIGURA 8.6**: Diseño del experimento de bloqueo de Kamin y resultados]

**Conclusión devastadora:**
La contigüidad entre Tono y descarga es **insuficiente** para generar aprendizaje. Lo que importa es si el SBI es **sorprendente o predecible**. En el grupo experimental, la Luz ya predecía perfectamente la descarga, por lo que esta no era sorprendente. El Tono es "redundante" - no agrega información nueva.

**Principio de competencia:**
> "El aprendizaje sobre un elemento de un compuesto depende del aprendizaje previo sobre otros elementos. Los elementos compiten por un 'pool' limitado de asociabilidad."

Este hallazgo cambió radicalmente la teorización sobre aprendizaje. Ya no se podía ver como una simple asociación automática basada en contigüidad. El sistema tiene que estar **computando algo** sobre predictibilidad, sorpresa, redundancia de información.

---

## Parte IV: Resumen de Sesgos Inductivos

Con base en los experimentos revisados, podemos caracterizar los sesgos inductivos que evolucionaron para resolver el problema de asignación de crédito:

### Sesgos que Reducen el Espacio de Candidatos

**1. Contigüidad Temporal**
- **Regla**: Considera principalmente eventos temporalmente cercanos al SBI
- **Efecto**: Reduce espacio de infinitos eventos pasados a ventana de segundos/minutos
- **Limitación**: No es necesaria (García) ni suficiente (Kamin)

**2. Relevancia Biológica**
- **Regla**: Considera solo dimensiones de estimulación relevantes al tipo de SBI
- **Ejemplos**:
  - Enfermedad → Sabores
  - Dolor externo → Audiovisuales
  - (Varía entre especies según nicho ecológico)
- **Función adaptativa**: Evita asociaciones espurias, enfoca en información confiable

**3. Novedad**
- **Regla**: Prioriza estímulos novedosos sobre familiares
- **Racionalidad**: Estímulos familiares ya demostraron no predecir el SBI
- **Aplicación**: En compuestos con elementos nuevos y viejos, aprendizaje se dirige al nuevo

### Sesgos que Ordenan la Evaluación de Candidatos

**4. Saliencia (Intensidad)**
- Estímulos más intensos/conspicuos reciben prioridad
- Ejemplo: Luz brillante vs luz tenue; sabor fuerte vs suave

**5. Competencia por Asociabilidad Limitada**
- Cuando múltiples estímulos están presentes, compiten
- El crédito asignado a uno reduce el disponible para otros
- Mecanismo: Predicción agregada (como veremos en modelo de Rescorla-Wagner, Cap 9)

**6. Historia Previa (Bloqueo)**
- Si un estímulo ya predice el SBI, bloquea el aprendizaje sobre estímulos adicionales
- Principio: Solo eventos que reducen incertidumbre reciben crédito

[**FIGURA 8.7**: Diagrama conceptual de cómo los sesgos filtran el espacio de candidatos]

---

## Parte V: Conexiones Conceptuales

### Vínculo con Capítulo 2: Propiedades Estadísticas del Entorno

En el Cap 2 establecimos que el aprendizaje evolucionó para detectar **covarianzas** entre eventos. Los sesgos inductivos que hemos estudiado implementan esta detección de forma computacionalmente tratable:

**Sin sesgos:**
- Espacio de candidatos: Infinito (todos los eventos pasados)
- Computación requerida: Imposible

**Con sesgos:**
- Espacio de candidatos: Reducido a ~10-100 eventos contiguos y relevantes
- Computación requerida: Tratable

**Los sesgos son restricciones evolutivas** (Cap 2) que hacen posible el aprendizaje.

### Vínculo con Capítulo 3: Selección Natural como Proceso Análogo

Los sesgos inductivos operan de forma análoga a las restricciones en evolución:

| Selección Natural | Asignación de Crédito |
|-------------------|----------------------|
| Mutación genera variabilidad genética | Entorno presenta variabilidad en estímulos |
| Restricciones físicas/genéticas reducen espacio | Sesgos inductivos reducen candidatos |
| Filtros ambientales seleccionan genotipos | Error de predicción selecciona estímulos |
| Deriva genética (ruido aleatorio) | Variabilidad individual en saliencia |

En ambos casos, el problema es navegar un espacio gigantesco de posibilidades. Las restricciones/sesgos no son "limitaciones" sino **soluciones** que hacen el problema tratable.

### Preparando el Terreno para Modelos Formales

Los experimentos de este capítulo plantearon una pregunta urgente: Si la contigüidad no es suficiente, ¿qué principio determina la asignación de crédito?

**Las pistas:**
1. **Sorpresa/Predictibilidad** importa (bloqueo)
2. **Competencia** entre elementos (ensombrecimiento)
3. **Información agregada** del compuesto importa

Rescorla y Wagner (1972) formalizaron estas intuiciones en un modelo matemático que estudiaremos en el Capítulo 9. Su ecuación captura la idea de que:
> "El aprendizaje es proporcional a la discrepancia entre lo obtenido y lo esperado"

Este principio de **reducción de error de predicción** se convertirá en el motor conceptual de prácticamente todos los modelos modernos de aprendizaje.

---

## Conclusiones y Conceptos Clave

**El problema de asignación de crédito:**
- Dado un SBI, ¿cuál de los incontables eventos previos fue responsable?
- Sin mecanismos de filtrado, el problema es intratable
- Evolución desarrolló sesgos inductivos como solución

**Sesgos inductivos identificados:**
1. Contigüidad temporal (gradiente de demora)
2. Relevancia biológica (dependiente de especie y SBI)
3. Novedad vs familiaridad
4. Saliencia (intensidad del estímulo)
5. Competencia entre elementos
6. Bloqueo por aprendizaje previo

**Límites de la contigüidad:**
- **No es necesaria**: Aversiones a sabores con demoras de horas (García)
- **No es suficiente**: Bloqueo muestra que contigüidad sin sorpresa no genera aprendizaje (Kamin)

**Principio emergente - Predictibilidad:**
El sistema no solo detecta contigüidad sino **cambios en predictibilidad**. Solo eventos que reducen incertidumbre sobre el SBI reciben crédito.

**Hacia adelante:**
- Cap 9: Modelo de Rescorla-Wagner formaliza estos principios
- Cap 10: Extensiones que incorporan atención, tiempo, etc.

---

## Lecturas Recomendadas

**Textos Clásicos:**
- Pavlov, I. P. (1927). *Conditioned Reflexes*
- García, J., & Koelling, R. A. (1966). "Relation of cue to consequence in avoidance learning"
- Kamin, L. J. (1969). "Predictability, surprise, attention and conditioning"

**Revisiones Modernas:**
- Pearce, J. M., & Bouton, M. E. (2001). "Theories of associative learning in animals"
- Miller, R. R., & Matzel, L. D. (1988). "The comparator hypothesis"
- Gallistel, C. R., & Gibbon, J. (2000). "Time, rate, and conditioning"

**Perspectiva Evolutiva:**
- Domjan, M. (2005). "Pavlovian conditioning: A functional perspective"
- Shettleworth, S. J. (2010). *Cognition, Evolution, and Behavior* (2nd ed.)

---

## Ejercicios

### Conceptuales

1. **Análisis de Caso Personal:**
Piensa en la última vez que desarrollaste una aversión a algún alimento. 
- ¿Cuánto tiempo pasó entre comer y sentirte mal?
- ¿Consideraste otros posibles causantes (lugar, personas, actividades)?
- ¿Qué sesgos inductivos observas en tu propia asignación de crédito?

2. **Predicciones de Sesgos:**
Un restaurante sirve comida en platos rojos. Una persona come ahí, se enferma, y desarrolla aversión. ¿A qué es más probable que desarrolle aversión: al color del plato o al sabor de la comida? ¿Por qué? ¿Cambiaría tu respuesta si la persona fuera un pájaro en lugar de un humano?

3. **Bloqueo en Humanos:**
Diseña un experimento para demostrar bloqueo en humanos usando estímulos visuales y un resultado emocional (ej: sobresalto por ruido fuerte). Especifica:
- Fase 1 del grupo experimental
- Fase 2 (ambos grupos)
- Grupo control
- Predicción y medida

### Cuantitativos

4. **Gradiente de Demora:**
Supón que la fuerza del condicionamiento (V) decrece exponencialmente con la demora (d en segundos):
$$V = V_{max} \cdot e^{-\lambda d}$$

Si $V_{max} = 1$ y $\lambda = 0.1$:
- a) ¿Cuál es V cuando d = 0 seg? ¿d = 5 seg? ¿d = 10 seg?
- b) ¿A qué demora V cae a 0.5?
- c) Grafica V vs d para d = 0 a 60 seg

5. **Competencia en Ensombrecimiento:**
En un compuesto AB, supón que el crédito total disponible es 1.0. Si A es más saliente que B (saliencia_A = 0.7, saliencia_B = 0.3), y el crédito se distribuye proporcionalmente a saliencia:
- a) ¿Cuánto crédito recibe A? ¿B?
- b) Si saliencia_A aumenta a 0.9, ¿cómo cambia la distribución?
- c) ¿Qué pasaría si ambos tuvieran saliencia = 0.5?

### Aplicados

6. **Diseño Experimental - Relevancia Biológica:**
Quieres demostrar que los humanos muestran sesgo de relevancia biológica similar al de García. Diseña un experimento donde:
- SBI A: Malestar estomacal leve (inducido por rotación)
- SBI B: Sobresalto (ruido fuerte)
- EC1: Sabor de bebida
- EC2: Color de luz en habitación

Especifica grupos, fases, predicciones.

7. **Análisis de Fenómeno Real - Quimioterapia:**
Pacientes de quimioterapia frecuentemente desarrollan aversiones a alimentos consumidos antes del tratamiento, incluso sabiendo que la comida no causó la náusea.
- ¿Qué sesgos inductivos explican esto?
- ¿Por qué el conocimiento consciente no previene la aversión?
- ¿Qué estrategias podrían minimizar el problema?

8. **Evolución de Sesgos:**
¿Por qué crees que evolucionó el sesgo de novedad? Considera:
- Costos de asociaciones falsas positivas
- Costos de asociaciones falsas negativas  
- Entornos ancestrales vs modernos
- ¿Cuándo sería desadaptativo?

---

## Figuras Requeridas

**FIGURA 8.1**: Procedimiento de Condicionamiento Clásico de Pavlov
- Diagrama temporal EC (tono) → EI (comida)
- Respuesta incondicionada (salivación a comida)
- Respuesta condicionada (salivación a tono)
- Gráfica de adquisición (ensayos vs fuerza de RC)

**FIGURA 8.2**: Diferentes Relaciones Temporales EC-EI
- 5 paneles mostrando: simultáneo, demora corta, demora larga, huella, hacia atrás
- Barras indicando duración de EC y tiempo de presentación de EI
- Fuerza de condicionamiento para cada tipo

**FIGURA 8.3**: Experimento de García & Koelling
- Diseño experimental (3 fases)
- Gráfica de resultados: consumo de agua dulce vs brillante-ruidosa
- Separado por grupo (descarga vs enfermedad)

**FIGURA 8.4**: Aposematismo y Mimetismo
- Polilla tóxica con patrón llamativo
- Polilla no-tóxica mimética
- Ave aprendiendo a evitar patrón

**FIGURA 8.5**: Ensombrecimiento (Reynolds)
- Diseño: triángulo-rojo vs círculo-verde
- Resultados de prueba: respuestas a forma vs color (separado por paloma)

**FIGURA 8.6**: Bloqueo (Kamin)
- Diagrama de fases para grupo experimental vs control
- Gráfica: nivel de miedo al tono en prueba (comparando grupos)

**FIGURA 8.7**: Diagrama de Sesgos Inductivos
- Espacio inicial de candidatos (muy grande)
- Flechas de filtrado secuencial por cada sesgo
- Espacio final reducido

---

## Notas para Simuladores

**Simulador 1: Gradiente de Demora**
- Slider: Demora entre EC y EI (0-60 seg)
- Output: Fuerza de condicionamiento adquirida
- Visualización: Curva de demora vs V

**Simulador 2: Ensombrecimiento**
- Ajustar saliencia de elemento A y B (sliders)
- Simular ensayos de entrenamiento compuesto AB → Refuerzo
- Mostrar evolución de V_A y V_B
- Prueba: Respuesta a A vs B separados

**Simulador 3: Bloqueo**
- Dos condiciones: con/sin Fase 1
- Simular entrenamiento
- Comparar aprendizaje sobre elemento "bloqueado"

---

**Fin del Capítulo 8**
