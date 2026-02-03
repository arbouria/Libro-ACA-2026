# GLOSARIO TERMINOLÓGICO
## Aprendizaje y Comportamiento Adaptable: Principios y Modelos

**Propósito:** Este glosario documenta el uso correcto y consistente de términos técnicos a lo largo del libro. Es una guía de referencia para mantener coherencia terminológica entre capítulos.

**Última actualización:** 26 de enero de 2026

---

## 📋 ÍNDICE POR CATEGORÍAS

1. [Conceptos Fundamentales](#conceptos-fundamentales)
2. [Tipos de Comportamiento](#tipos-de-comportamiento)
3. [Mecanismos y Algoritmos](#mecanismos-y-algoritmos)
4. [Sucesos y Consecuencias](#sucesos-y-consecuencias)
5. [Señales y Estímulos](#señales-y-estímulos)
6. [Parámetros y Variables](#parámetros-y-variables)
7. [Procedimientos y Protocolos](#procedimientos-y-protocolos)
8. [Niveles de Análisis](#niveles-de-análisis)

---

## CONCEPTOS FUNDAMENTALES

### Adaptación vs. Adaptabilidad

**Adaptación (sustantivo)**
- **Definición:** Proceso por el cual un organismo o mecanismo se ajusta a su entorno para maximizar supervivencia/reproducción
- **Usar en:** Contextos generales sobre evolución y función
- **Ejemplo:** "La migración es una adaptación a cambios estacionales en disponibilidad de recursos"
- **Evitar confusión con:** Adaptabilidad (capacidad), habituación (proceso específico)

**Adaptabilidad (sustantivo)**
- **Definición:** Capacidad de un sistema para ajustarse a cambios en el entorno
- **Usar en:** Cuando se discute la capacidad general de ajuste
- **Ejemplo:** "La adaptabilidad requiere mecanismos que detecten cambios y ajusten el comportamiento"
- **Relacionado:** Flexibilidad conductual, plasticidad

**Adaptable (adjetivo)**
- **Definición:** Que puede adaptarse; que posee adaptabilidad
- **Usar en:** "comportamiento adaptable" (título del libro)
- **Ejemplo:** "Un agente adaptable modifica sus respuestas según la experiencia"

**Adaptativo (adjetivo)**
- **Definición:** Que contribuye a la adaptación; que es funcionalmente apropiado
- **Usar en:** "problema adaptativo", "función adaptativa", "valor adaptativo"
- **Ejemplo:** "La capacidad de predecir es adaptativa porque mejora las decisiones"

---

### Agente

**Agente**
- **Definición:** Término neutral para cualquier sistema (biológico o artificial) que percibe y actúa en un entorno
- **Usar en:** Contextos formales/algorítmicos donde queremos generalizar sobre organismos y máquinas
- **Ejemplo:** "El agente debe decidir cómo distribuir su comportamiento"
- **Términos relacionados:** Organismo (solo biológico), robot (solo artificial), sistema

**Cuándo usar cada término:**
- **"Agente"** → Discusión formal de algoritmos, principios generales
- **"Organismo"** → Ejemplos biológicos, evolución, contexto ecológico
- **"Animal"** → Ejemplos experimentales específicos (rata, paloma)
- **"Robot"** → Ejemplos de implementación artificial

---

### Aprendizaje

**Aprendizaje**
- **Definición estándar en el libro:** Cambio relativamente permanente en el comportamiento resultado de la experiencia
- **Definición funcional (preferida):** Mecanismo que permite comportamiento adaptable ajustando el comportamiento a la estructura estadística del entorno
- **Usar en:** Cuando el cambio es resultado de experiencia individual (ontogenético)
- **Distinguir de:** Instinto (filogenético), maduración (desarrollo), fatiga (temporal)

**Aprendizaje predictivo**
- **Definición:** Aprendizaje sobre relaciones predictivas entre eventos
- **Usar en:** Condicionamiento clásico, formación de expectativas
- **Ejemplo:** "El aprendizaje predictivo permite anticipar cuándo aparecerán recursos"

**Aprendizaje instrumental / operante**
- **Definición:** Aprendizaje sobre consecuencias de acciones
- **Cuándo introducir formalmente:** Bloque III
- **Usar en:** Contextos donde las acciones producen consecuencias
- **Nota:** Introducimos el concepto intuitivamente antes, pero el término técnico en Bloque III

---

## TIPOS DE COMPORTAMIENTO

### Comportamiento adaptado vs. Comportamiento adaptable

**Comportamiento adaptado**
- **Definición:** Respuestas apropiadas codificadas genéticamente (filogenéticas)
- **Usar en:** Instintos, reflejos, respuestas innatas
- **Ejemplo:** "La impronta en patitos es comportamiento adaptado"
- **Origen:** Selección natural

**Comportamiento adaptable**
- **Definición:** Capacidad de ajustar respuestas según experiencia (ontogenéticas)
- **Usar en:** Aprendizaje, plasticidad conductual
- **Ejemplo:** "El condicionamiento es un mecanismo de comportamiento adaptable"
- **Origen:** Aprendizaje individual

---

## MECANISMOS Y ALGORITMOS

### Algoritmo

**Algoritmo**
- **Definición:** Procedimiento paso a paso que transforma inputs en outputs
- **Usar en:** Nivel algorítmico de explicación, mecanismos computacionales
- **Ejemplo:** "El algoritmo de reducción de error ajusta predicciones"
- **Nota importante:** En este libro, "algoritmo" es sinónimo de "mecanismo" cuando hablamos del nivel procedimental

**Mecanismo**
- **Definición:** Sistema o proceso que produce un efecto
- **Usar en:** Cuando discutimos el "cómo" funciona algo
- **Ejemplo:** "El mecanismo de retroalimentación mantiene la homeostasis"
- **Niveles:** Puede referirse a nivel algorítmico o de implementación según contexto

---

### Tipos de algoritmos (las "tuercas y tornillos")

**Algoritmo de comparación**
- **Tipos:** Sucesiva (en el tiempo) vs. Simultánea (en el espacio)
- **Función:** Detectar diferencias entre estados
- **Ejemplos:** Ascenso de colina (sucesiva), retroalimentación (simultánea)

**Algoritmo de reducción de error**
- **Función:** Ajustar predicciones cuando difieren de resultados
- **Ejemplo:** Regla delta de Rescorla-Wagner
- **Término clave:** Error de predicción

**Algoritmo de exploración vs. explotación**
- **Función:** Balancear muestreo de opciones nuevas vs. uso de conocidas
- **Usar en:** Bloque III y IV principalmente
- **Dilema central:** Trade-off entre conocimiento y ganancia

---

## SUCESOS Y CONSECUENCIAS

### Términos para eventos importantes

**Suceso biológicamente importante** (PREFERIDO en bloques iniciales)
- **Definición:** Cualquier evento relevante para supervivencia/reproducción
- **Usar en:** Bloques 0, I, II (antes de introducir terminología técnica)
- **Ejemplo:** "Cuando aparece un suceso biológicamente importante, el agente debe asignar crédito"
- **Ventaja:** Neutral, no presupone mecanismo
- **Incluye:** Comida, agua, peligro, dolor, pareja potencial

**Reforzador** (introducir formalmente en Bloque III)
- **Definición:** Consecuencia que incrementa o disminuye probabilidad de respuesta
- **Cuándo introducir:** Al hablar de condicionamiento operante
- **Tipos:** Positivo (incrementa), negativo (decrementa)
- **Nota:** Evitar en bloques iniciales; usar "suceso biológicamente importante"

**Recurso**
- **Definición:** Elemento necesario para supervivencia/funcionamiento
- **Usar en:** Ejemplos concretos, explicaciones introductorias
- **Ejemplo:** "El robot debe localizar recursos dispersos"
- **Contextos apropiados:** Sección de Wall-E, ejemplos de forrajeo

**Consecuencia**
- **Definición:** Resultado que sigue a una acción
- **Usar en:** Contexto general de relaciones causa-efecto
- **Ejemplo:** "Las consecuencias de una acción determinan si se repetirá"

**Resultado**
- **Definición:** Valor observado de un evento (término más neutral que "consecuencia")
- **Usar en:** Ecuaciones, contextos formales
- **Ejemplo:** "El resultado observado fue λ = 10"

---

### Valor y Magnitud

**Valor**
- **Definición:** Medida de importancia biológica o utilidad de un suceso
- **Usar en:** Contextos formales, modelos de elección
- **Ejemplo:** "El valor de la comida depende de su magnitud y demora"
- **Símbolo común:** V (valor asociativo), λ (valor del resultado)

**Magnitud**
- **Definición:** Cantidad física de un recurso o intensidad de un estímulo
- **Usar en:** Cuando discutimos cantidad concreta
- **Ejemplo:** "La magnitud del reforzador fue 10 pellets de comida"

**Utilidad**
- **Definición:** Valor subjetivo de un resultado
- **Usar en:** Economía conductual, teoría de la decisión (Bloque III+)
- **Ejemplo:** "La utilidad de $100 no es el doble que $50"

---

## SEÑALES Y ESTÍMULOS

### Terminología de estímulos

**Señal**
- **Definición:** Estímulo que porta información sobre otro evento
- **Usar en:** Contexto de predicción, detección de señales
- **Ejemplo:** "Una señal confiable predice la aparición del recurso"
- **Distinguir de:** Ruido (sin información)

**Estímulo**
- **Definición:** Cualquier evento detectable del entorno
- **Usar en:** Término general neutral
- **Ejemplo:** "El estímulo auditivo fue un tono de 1000 Hz"
- **Nota:** Más general que "señal"

**Estímulo condicionado (EC)**
- **Definición:** Señal inicialmente neutral que adquiere valor predictivo
- **Cuándo introducir:** Al formalizar condicionamiento clásico (Bloque II)
- **Usar antes de introducir:** "señal predictiva" o simplemente "señal"
- **Ejemplo:** "El EC (campana) predice el EI (comida)"

**Estímulo incondicionado (EI)**
- **Definición:** Estímulo con valor biológico intrínseco
- **Cuándo introducir:** Con EC (Bloque II)
- **Usar antes de introducir:** "suceso biológicamente importante"
- **Ejemplo:** "El EI (comida) tiene valor λ = 100"

**Estímulo discriminativo**
- **Definición:** Señal que indica disponibilidad de contingencia
- **Cuándo introducir:** Condicionamiento operante (Bloque III)
- **Ejemplo:** "La luz verde es estímulo discriminativo para presionar la palanca"

---

### Propiedades de señales

**Confiabilidad**
- **Definición:** Grado en que una señal predice consistentemente un suceso
- **Medida:** P(suceso|señal)
- **Usar en:** Detección de señales, teoría de la información
- **Relacionado:** Validez predictiva

**Saliencia**
- **Definición:** Grado en que un estímulo captura atención
- **Parámetro común:** α (alfa)
- **Usar en:** Modelos de aprendizaje asociativo
- **Ejemplo:** "La saliencia del tono (α = 0.8) era alta"

**Validez predictiva**
- **Definición:** En qué medida una señal predice un suceso
- **Usar en:** Contexto de condicionamiento, modelos predictivos
- **Relacionado:** Confiabilidad, correlación

---

## PARÁMETROS Y VARIABLES

### Parámetros de aprendizaje

**α (alfa) - Tasa de aprendizaje**
- **Definición:** Parámetro que controla la velocidad del aprendizaje
- **Rango:** 0 < α ≤ 1
- **Interpretación:** α alto = aprendizaje rápido, α bajo = aprendizaje lento
- **Usar en:** Modelo de Rescorla-Wagner, reglas delta
- **Relacionado:** Saliencia del EC

**β (beta) - Tasa de aprendizaje del EI**
- **Definición:** Parámetro de aprendizaje específico del estímulo incondicionado
- **Rango:** 0 < β ≤ 1
- **Usar en:** Modelos con múltiples tasas de aprendizaje
- **Distinguir de:** α (del EC)

**λ (lambda) - Valor asintótico**
- **Definición:** Valor máximo que puede alcanzar la asociación
- **Usar en:** Modelos de aprendizaje asociativo
- **Interpretación:** Representa la magnitud o valor del EI
- **Ejemplo:** "Con λ = 100, la fuerza máxima es 100"

**V - Valor asociativo**
- **Definición:** Fuerza de la asociación aprendida
- **Usar en:** Modelos predictivos, condicionamiento
- **Notación:** V_EC (valor del EC), ΣV (suma de valores)
- **Ejemplo:** "Después de 10 ensayos, V = 85"

---

### Variables temporales

**Demora**
- **Definición:** Tiempo entre respuesta y consecuencia (o entre EC y EI)
- **Usar en:** Descuento temporal, condicionamiento
- **Símbolo común:** D o t
- **Ejemplo:** "Con demora de 5 segundos, el aprendizaje es más lento"

**Intervalo entre ensayos (IEE)**
- **Definición:** Tiempo entre presentaciones sucesivas
- **Usar en:** Protocolos experimentales
- **Importancia:** Afecta tasa de aprendizaje
- **Ejemplo:** "Con IEE = 60s, el condicionamiento fue más efectivo"

**Descuento temporal**
- **Definición:** Reducción del valor de consecuencias demoradas
- **Usar en:** Bloque VI (Estructura de Preferencias)
- **Fórmula común:** V = A/(1 + kD)
- **Parámetro:** k (tasa de descuento)

---

## PROCEDIMIENTOS Y PROTOCOLOS

### Protocolos de condicionamiento clásico

**Adquisición**
- **Definición:** Fase donde se establece la asociación EC-EI
- **Procedimiento:** EC seguido de EI repetidamente
- **Resultado esperado:** V incrementa hacia λ

**Extinción**
- **Definición:** Presentación del EC sin EI
- **Procedimiento:** EC solo
- **Resultado esperado:** V decrementa hacia 0
- **Nota importante:** No es "desaprendizaje", es nueva asociación EC-nada

**Bloqueo**
- **Definición:** Fenómeno donde EC preentrenado impide aprendizaje de EC nuevo
- **Procedimiento:** Fase 1: A → EI, Fase 2: AB → EI
- **Resultado:** B no adquiere valor asociativo
- **Explicación:** Error de predicción es cero en Fase 2

**Inhibición condicionada**
- **Definición:** EC adquiere valor negativo (predice ausencia)
- **Procedimiento:** A → EI, AB → nada
- **Resultado:** V_B < 0
- **Ejemplo:** "B señala que NO habrá comida"

---

### Programas de refuerzo (introducir en Bloque III)

**Razón fija (RF)**
- **Definición:** Reforzador después de N respuestas
- **Ejemplo:** RF-5 = reforzador cada 5 respuestas
- **Patrón típico:** Tasa alta, pausa post-reforzador

**Intervalo fijo (IF)**
- **Definición:** Reforzador disponible después de tiempo fijo
- **Ejemplo:** IF-60s = reforzador cada 60 segundos
- **Patrón típico:** Aceleración ("festón")

**Razón variable (RV)**
- **Definición:** Reforzador después de promedio de N respuestas
- **Ejemplo:** RV-10 = promedio de 10 respuestas
- **Patrón típico:** Tasa alta y estable

**Intervalo variable (IV)**
- **Definición:** Reforzador disponible después de tiempo promedio
- **Ejemplo:** IV-30s = promedio de 30 segundos
- **Patrón típico:** Tasa moderada y estable

---

## NIVELES DE ANÁLISIS

### Marco de Marr / Tinbergen

**Nivel computacional**
- **Pregunta:** ¿Qué problema adaptativo se resuelve?
- **Usar en:** Al introducir cada mecanismo
- **Ejemplo:** "A nivel computacional, el problema es asignar crédito"
- **También llamado:** Nivel funcional, nivel de la tarea

**Nivel algorítmico**
- **Pregunta:** ¿Qué procedimiento implementa la solución?
- **Usar en:** Al describir mecanismos y reglas
- **Ejemplo:** "A nivel algorítmico, usa reducción de error"
- **También llamado:** Nivel representacional, nivel de procesamiento

**Nivel de implementación**
- **Pregunta:** ¿Qué circuitos físicos lo realizan?
- **Usar en:** Cuando discutimos sustratos neurales
- **Ejemplo:** "A nivel de implementación, neuronas dopaminérgicas..."
- **También llamado:** Nivel físico, nivel neuronal

---

### Preguntas de Tinbergen (complementarias)

**Causación proximal (Mecanismo)**
- **Pregunta:** ¿Qué causa inmediata produce el comportamiento?
- **Equivalente aproximado:** Nivel algorítmico + implementación

**Ontogenia (Desarrollo)**
- **Pregunta:** ¿Cómo se desarrolla en la vida del individuo?
- **Usar en:** Cuando discutimos aprendizaje y experiencia

**Función adaptativa (Supervivencia)**
- **Pregunta:** ¿Cómo contribuye a supervivencia/reproducción?
- **Equivalente aproximado:** Nivel computacional

**Filogenia (Evolución)**
- **Pregunta:** ¿Cómo evolucionó en la especie?
- **Usar en:** Selección natural, orígenes evolutivos

---

## TÉRMINOS A EVITAR O USAR CON CUIDADO

### Términos ambiguos

**"Recompensa"**
- **Problema:** Ambiguo (¿valor subjetivo o estímulo objetivo?)
- **Preferir:** "Suceso biológicamente importante" o "resultado positivo"
- **Excepción:** En economía conductual (Bloque VI) donde es estándar

**"Castigo"**
- **Problema:** Connotaciones, además término técnico con definición precisa
- **Preferir:** "Resultado aversivo" o "suceso negativo"
- **Usar formalmente:** Solo al introducir condicionamiento operante

**"Estímulo-respuesta"**
- **Problema:** Implica visión conductista mecanicista que queremos evitar
- **Preferir:** Describir relaciones funcionales específicas
- **Excepción:** Contexto histórico de behaviorismo

**"Refuerzo"**
- **Problema:** A veces usado incorrectamente como sinónimo de "reforzador"
- **Distinguir:** 
  - Refuerzo (proceso): incremento en probabilidad de respuesta
  - Reforzador (evento): consecuencia que produce refuerzo

---

### Términos que requieren definición previa

Estos términos NO deben usarse antes de introducirse formalmente:

**Antes de Bloque II:**
- ❌ EC, EI (estímulo condicionado/incondicionado)
- ❌ Valor asociativo
- ❌ Error de predicción
- ✅ Usar: "señal", "suceso importante", "predicción", "diferencia"

**Antes de Bloque III:**
- ❌ Reforzador, refuerzo
- ❌ Respuesta operante
- ❌ Contingencia
- ✅ Usar: "consecuencia", "resultado de acción", "relación entre acción y resultado"

**Antes de Bloque IV:**
- ❌ Error de predicción temporal
- ❌ Q-learning
- ❌ Valor de estado
- ✅ Usar: Describir intuitivamente conceptos cuando sea necesario

---

## CONVENCIONES DE TRADUCCIÓN

### Términos en inglés que aparecen frecuentemente

| Inglés | Español (preferido) | Notas |
|--------|---------------------|-------|
| Learning | Aprendizaje | Nunca "enseñanza" |
| Reward | Recompensa (evitar), Resultado positivo | Ver arriba |
| Punishment | Castigo (definir), Resultado aversivo | Definir formalmente |
| Cue | Señal | Nunca "clave" |
| Outcome | Resultado, Consecuencia | Contexto dependiente |
| Schedule | Programa (de refuerzo) | No "calendario" |
| Rate | Tasa | Nunca "velocidad" para tasa de respuesta |
| Trial | Ensayo | No "prueba" |
| Block | Bloque (de ensayos) | Contexto claro |
| Extinction | Extinción | OK |
| Acquisition | Adquisición | OK |
| Contingency | Contingencia | Definir antes de usar |
| Habit | Hábito | Definir formalmente |
| Goal | Meta, Objetivo | Contexto dependiente |

---

## NOTAS DE USO POR BLOQUE

### Bloque 0 (Fundamentos):
- Establecer niveles de explicación
- Introducir "agente", "problema adaptativo", "algoritmo"
- Evitar terminología técnica de condicionamiento

### Bloque I (Sin Historia):
- "Comparación sucesiva" vs. "simultánea"
- "Retroalimentación", "homeostasis"
- Evitar "aprendizaje" (estos no integran historia)

### Bloque II (Asignación de Crédito):
- Introducir "EC", "EI", "valor asociativo"
- "Error de predicción" es concepto central
- "Suceso biológicamente importante" → formalizar terminología

### Bloque III (Elección):
- Introducir "reforzador", "contingencia"
- "Programa de refuerzo" con tipos
- "Optimización bajo restricciones"

### Bloque IV (Secuencial):
- "Error de predicción temporal"
- "Valor de estado", "valor de acción"
- Terminología de aprendizaje por refuerzo (Q, π, etc.)

### Bloque V (Incertidumbre):
- "Volatilidad", "incertidumbre"
- "Estado oculto", "inferencia"
- Bayesiano, posterior, prior

### Bloque VI (Preferencias):
- "Utilidad", "descuento"
- "Impulsividad", "autocontrol"
- Economía conductual estándar

---

## SÍMBOLOS MATEMÁTICOS COMUNES

| Símbolo | Significado | Introducción |
|---------|-------------|--------------|
| α (alfa) | Tasa de aprendizaje (EC) | Bloque II |
| β (beta) | Tasa de aprendizaje (EI) | Bloque II |
| λ (lambda) | Valor asintótico | Bloque II |
| V | Valor asociativo | Bloque II |
| Δ (delta) | Cambio en | Bloque II |
| δ (delta minúscula) | Error de predicción temporal | Bloque IV |
| γ (gamma) | Factor de descuento | Bloque IV |
| π (pi) | Política | Bloque IV |
| Q | Valor de acción | Bloque IV |
| k | Tasa de descuento temporal | Bloque VI |

---

## CÓMO USAR ESTE GLOSARIO

### Durante escritura:
1. Busca el término antes de usarlo
2. Verifica que estés en el bloque correcto para introducirlo
3. Usa la definición y ejemplos como guía
4. Sigue convenciones de cuándo usar qué variante

### Durante revisión:
1. Ctrl+F términos clave en tu capítulo
2. Verifica consistencia con definiciones del glosario
3. Confirma que introduces términos en el momento apropiado
4. Asegura que usas la variante preferida del término

### Para actualizaciones:
1. Documenta nuevos términos técnicos aquí
2. Nota si un término requiere definición formal antes de uso
3. Agrega ejemplos de uso correcto
4. Marca términos ambiguos a evitar

---

## REGISTRO DE CAMBIOS

| Fecha | Término | Cambio | Rationale |
|-------|---------|--------|-----------|
| 26-01-2026 | "suceso biológicamente importante" | Preferido sobre "reforzador" en bloques iniciales | Neutral, no presupone mecanismo |
| 26-01-2026 | "agente" | Adoptar para contextos formales | Generaliza sobre biológico/artificial |
| [Agregar cambios futuros aquí] | | | |

---

**Versión:** 1.0  
**Mantenedor:** Arturo Bouzas  
**Última revisión:** 26 de enero de 2026
