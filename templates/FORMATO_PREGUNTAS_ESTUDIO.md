# FORMATO ESTÁNDAR: PREGUNTAS DE ESTUDIO
## Guía para Capítulos del Libro

**Propósito:** Este documento establece el formato estándar para las preguntas de estudio que aparecen al final de cada capítulo del libro.

**Última actualización:** 26 de enero de 2026

---

## 📋 ESTRUCTURA ESTÁNDAR

Cada capítulo debe terminar con **3-4 secciones de preguntas** organizadas por tipo:

```markdown
---

## Preguntas de Estudio

### 1. Preguntas Conceptuales

[Preguntas que evalúan comprensión de conceptos sin cálculo]

### 2. Problemas Cuantitativos

[Ejercicios que requieren cálculo o manipulación de ecuaciones]

### 3. Análisis de Casos

[Preguntas que piden aplicar conceptos a situaciones complejas]

### 4. Conexiones Integradoras

[Preguntas que conectan con otros capítulos o bloques]

---

## Lecturas Complementarias

[Referencias actualizadas y anotadas]
```

---

## 🎯 TIPOS DE PREGUNTAS

### 1. PREGUNTAS CONCEPTUALES

**Propósito:** Evaluar comprensión profunda sin requerir cálculo

**Características:**
- Formuladas en lenguaje claro
- Requieren explicación en 2-4 oraciones
- Enfocan en "por qué" y "cómo" más que "qué"
- Sin números ni ecuaciones

**Formatos efectivos:**

#### A) Explicación de conceptos
```markdown
**1.1** Explica con tus propias palabras por qué el bloqueo ocurre según el modelo de Rescorla-Wagner. ¿Qué tiene que ver el error de predicción con este fenómeno?
```

#### B) Comparación de conceptos
```markdown
**1.2** ¿En qué se diferencia "comportamiento adaptado" de "comportamiento adaptable"? Proporciona un ejemplo de cada uno.
```

#### C) Predicción de resultados
```markdown
**1.3** Un agente con α = 0.9 y otro con α = 0.1 experimentan el mismo protocolo de adquisición. ¿Cuál aprenderá más rápido? ¿Cuál será más sensible a cambios si el EI cambia de valor súbitamente? Justifica tu respuesta.
```

#### D) Análisis de relaciones
```markdown
**1.4** ¿Por qué es adaptativo tener mecanismos de aprendizaje predictivo en entornos variables? ¿Cuáles serían las desventajas de respuestas completamente programadas genéticamente?
```

**Cantidad recomendada:** 4-6 preguntas conceptuales por capítulo

---

### 2. PROBLEMAS CUANTITATIVOS

**Propósito:** Evaluar habilidad de aplicar ecuaciones y realizar cálculos

**Características:**
- Requieren manipulación de fórmulas
- Incluyen datos numéricos específicos
- Pueden tener múltiples pasos
- Resultados verificables

**Niveles de dificultad:**

#### Nivel Básico: Aplicación directa
```markdown
**2.1** Un EC tiene valor inicial V = 0. Después del primer ensayo con λ = 100 y α = 0.3, ¿cuál será el nuevo valor V?

*Usa:* ΔV = α(λ - V)
```

#### Nivel Intermedio: Serie de ensayos
```markdown
**2.2** Calcula los valores de V para los primeros 5 ensayos de un protocolo de adquisición con:
- V₀ = 0
- λ = 80
- α = 0.4

Presenta tus cálculos en una tabla con columnas: Ensayo, V_anterior, Error, ΔV, V_nuevo
```

#### Nivel Avanzado: Análisis paramétrico
```markdown
**2.3** En un protocolo de extinción, V comienza en 100 y λ = 0.

a) Calcula cuántos ensayos se necesitan para que V < 10 si α = 0.5
b) ¿Cuántos ensayos se necesitarían con α = 0.2?
c) ¿Qué relación general observas entre α y la velocidad de extinción?
```

**Formato de presentación:**
- Siempre especifica valores de todos los parámetros
- Indica fórmulas relevantes cuando sea útil
- Para problemas largos, divide en incisos (a, b, c)
- Incluye pregunta de interpretación al final de cálculos

**Cantidad recomendada:** 3-5 problemas cuantitativos por capítulo

---

### 3. ANÁLISIS DE CASOS

**Propósito:** Evaluar capacidad de aplicar teoría a situaciones complejas y realistas

**Características:**
- Presentan escenarios detallados
- Requieren integrar múltiples conceptos
- Tienen componentes ambiguos o realistas
- Permiten respuestas diversas

**Formato estándar:**

```markdown
**3.1 - Caso: [Título Descriptivo]**

**Escenario:**
[Descripción detallada de 3-5 oraciones presentando situación]

**Preguntas:**
a) [Pregunta de análisis]
b) [Pregunta de predicción]
c) [Pregunta de diseño o intervención]

**Conexión conceptual:**
[1 oración indicando qué conceptos del capítulo son relevantes]
```

**Ejemplos por tipo de capítulo:**

#### Para capítulo de Rescorla-Wagner:
```markdown
**3.1 - Caso: El Perro que No Come**

**Escenario:**
Un perro fue entrenado durante 50 ensayos en los que un tono (A) predecía comida. Ahora, cuando se presenta un compuesto de tono (A) + luz (B) seguido de comida, el perro saliva vigorosamente ante A pero no muestra respuesta alguna ante B cuando se presenta sola. El entrenador está confundido: "¿Por qué el perro no aprendió sobre la luz si también predecía la comida?"

**Preguntas:**
a) Usa el modelo de Rescorla-Wagner para explicar por qué B no adquirió valor asociativo.
b) ¿Qué habría pasado si B se hubiera presentado primero, sin entrenar A previamente?
c) Diseña un protocolo que sí permitiría que B adquiriera valor asociativo.

**Conexión conceptual:**
Este caso ilustra el fenómeno de bloqueo y la importancia del error de predicción en el aprendizaje asociativo.
```

#### Para capítulo de Ascenso de Colina:
```markdown
**3.2 - Caso: Robot Explorador Atascado**

**Escenario:**
Un robot programado con ascenso de colina simple (siempre moverse hacia mayor intensidad de señal) está buscando la fuente de radio más fuerte en un terreno montañoso. El robot detecta señal de intensidad 50 en su ubicación actual. Encuentra que al norte la intensidad es 60, al sur es 40, al este es 55 y al oeste es 45. Se mueve al norte. Después de 20 movimientos similares, se detiene en una ubicación con intensidad 75, rodeado de posiciones con intensidades menores.

Sin embargo, los operadores saben que existe una fuente mucho más fuerte (intensidad 200) a 500 metros al sur de la posición inicial del robot.

**Preguntas:**
a) ¿Por qué el robot no encontró la fuente más fuerte?
b) ¿Qué concepto de este capítulo explica el problema del robot?
c) Propón dos modificaciones al algoritmo que permitirían al robot encontrar la fuente global.

**Conexión conceptual:**
Este caso ilustra el problema de máximos locales vs. globales y las limitaciones del ascenso de colina puro.
```

**Cantidad recomendada:** 2-3 casos por capítulo

---

### 4. CONEXIONES INTEGRADORAS

**Propósito:** Promover síntesis entre capítulos y bloques del libro

**Características:**
- Requieren conocimiento de múltiples capítulos
- Enfocan en principios generales
- Preparan para contenido futuro
- Promueven pensamiento de alto nivel

**Formatos efectivos:**

#### A) Conexión con capítulos previos
```markdown
**4.1** En el Capítulo 4 estudiamos ascenso de colina, un mecanismo que usa comparación sucesiva. En este capítulo vimos el modelo de Rescorla-Wagner, que usa reducción de error. ¿Qué tienen en común estos dos algoritmos? ¿En qué se diferencian fundamentalmente?
```

#### B) Anticipación de contenido futuro
```markdown
**4.2** El modelo de Rescorla-Wagner explica aprendizaje predictivo (EC predice EI), pero no explica cómo las acciones del organismo afectan los resultados. ¿Qué tipo de aprendizaje adicional necesitaríamos para explicar comportamiento instrumental? [Pista: Lo veremos en Bloque III]
```

#### C) Aplicación a múltiples dominios
```markdown
**4.3** Los principios de asignación de crédito que viste en este capítulo aplican no solo a ratas en laboratorios, sino también a:
- Algoritmos de recomendación (YouTube, Netflix)
- Diagnóstico médico
- Inversión financiera

Elige uno de estos dominios y explica cómo se aplica el concepto de "error de predicción" en ese contexto.
```

#### D) Niveles de explicación
```markdown
**4.4** Este capítulo se enfocó en el nivel algorítmico del aprendizaje predictivo. ¿Cuál sería la pregunta correspondiente a nivel:
a) Computacional: [¿Qué problema...]
b) De implementación: [¿Qué circuitos...]
```

**Cantidad recomendada:** 2-3 preguntas integradoras por capítulo

---

## 🎨 FORMATO DE PRESENTACIÓN

### Estructura visual clara:

```markdown
---

## Preguntas de Estudio

Estas preguntas están diseñadas para consolidar tu comprensión del capítulo. Se recomienda intentar responderlas sin consultar el texto primero, y luego verificar o complementar tus respuestas.

### 1. Preguntas Conceptuales

**1.1** [Pregunta aquí]

**1.2** [Pregunta aquí]

[...]

### 2. Problemas Cuantitativos

**2.1** [Problema aquí]

*Datos:* [Lista de valores]
*Usa:* [Fórmula relevante]

**2.2** [Problema aquí]

[...]

### 3. Análisis de Casos

**3.1 - Caso: [Título]**

**Escenario:** [Descripción]

**Preguntas:**
a) [Pregunta]
b) [Pregunta]
c) [Pregunta]

**Conexión conceptual:** [Explicación]

[...]

### 4. Conexiones Integradoras

**4.1** [Pregunta aquí]

**4.2** [Pregunta aquí]

[...]

---

## Lecturas Complementarias

[Ver sección siguiente]
```

---

## 📚 LECTURAS COMPLEMENTARIAS

### Formato estándar:

```markdown
## Lecturas Complementarias

### Fundamentales

**Autor, A. (Año).** *Título del artículo o libro.* Journal/Editorial.

**Qué aporta:** [1-2 oraciones sobre por qué esta lectura es valiosa]

**Nivel:** [Introductorio/Intermedio/Avanzado]

**Disponibilidad:** [DOI, URL, o "Biblioteca"]

---

### Clásicos

[Artículos históricos importantes, con contexto]

---

### Contemporáneos

[Artículos recientes, aplicaciones modernas]

---

### Extensiones

[Para estudiantes que quieren profundizar]
```

### Ejemplo concreto:

```markdown
## Lecturas Complementarias

### Fundamentales

**Rescorla, R. A., & Wagner, A. R. (1972).** *A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement.* In Classical Conditioning II: Current Research and Theory.

**Qué aporta:** El artículo original que presenta el modelo de Rescorla-Wagner. Aunque usa notación ligeramente diferente, introduce los conceptos centrales de error de predicción y asignación de crédito que discutimos en este capítulo.

**Nivel:** Intermedio

**Disponibilidad:** Biblioteca, Google Scholar

---

**Schultz, W. (1998).** *Predictive reward signal of dopamine neurons.* Journal of Neurophysiology, 80(1), 1-27.

**Qué aporta:** Demuestra que las neuronas dopaminérgicas implementan exactamente un error de predicción tipo Rescorla-Wagner. Conecta el nivel algorítmico (que vimos en el capítulo) con el nivel de implementación neuronal.

**Nivel:** Intermedio-Avanzado

**Disponibilidad:** DOI: 10.1152/jn.1998.80.1.1

---

### Clásicos

**Kamin, L. J. (1969).** *Predictability, surprise, attention, and conditioning.* In Campbell, B. A. & Church, R. M. (Eds.), Punishment and aversive behavior.

**Qué aporta:** Presenta el fenómeno de bloqueo que motivó el desarrollo del modelo de Rescorla-Wagner.

**Nivel:** Introductorio

---

### Contemporáneos

**Gershman, S. J. (2015).** *A unifying probabilistic view of associative learning.* PLOS Computational Biology, 11(11), e1004567.

**Qué aporta:** Muestra cómo el modelo de Rescorla-Wagner puede derivarse de principios Bayesianos. Conecta con material que veremos en Bloque V.

**Nivel:** Avanzado

**Disponibilidad:** Open access: doi.org/10.1371/journal.pcbi.1004567

---

### Extensiones

Para estudiantes interesados en implementación computacional:

**Sutton, R. S., & Barto, A. G. (2018).** *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. [Capítulo 6: Temporal-Difference Learning]

**Qué aporta:** Extiende las ideas de Rescorla-Wagner a aprendizaje secuencial. Prepara para material del Bloque IV.

**Nivel:** Intermedio

**Disponibilidad:** Gratis en: incompleteideas.net/book/the-book.html
```

---

## ✅ CHECKLIST PARA AUTORES

Al terminar cada capítulo, verifica:

- [ ] ¿Hay 4-6 preguntas conceptuales?
- [ ] ¿Las preguntas conceptuales cubren los conceptos clave del capítulo?
- [ ] ¿Hay 3-5 problemas cuantitativos con niveles variados de dificultad?
- [ ] ¿Los problemas cuantitativos especifican todos los parámetros necesarios?
- [ ] ¿Hay 2-3 casos de análisis con escenarios realistas?
- [ ] ¿Los casos están bien estructurados (escenario + preguntas + conexión)?
- [ ] ¿Hay 2-3 preguntas integradoras que conectan con otros capítulos?
- [ ] ¿Al menos una pregunta anticipa contenido de bloques futuros?
- [ ] ¿Las lecturas complementarias están anotadas (qué aportan + nivel)?
- [ ] ¿Hay mix de lecturas clásicas y contemporáneas?
- [ ] ¿Al menos una lectura es de acceso abierto?

---

## 🎯 PRINCIPIOS PEDAGÓGICOS

### Las preguntas deben:

1. **Promover pensamiento activo**, no solo recuerdo
   - ❌ "¿Qué es α?" (memorización)
   - ✅ "¿Por qué α alto produce aprendizaje rápido pero también hace al sistema sensible a ruido?" (comprensión)

2. **Conectar con intuiciones**, no solo fórmulas
   - ❌ "Calcula V después de 10 ensayos"
   - ✅ "Calcula V después de 10 ensayos. ¿El resultado coincide con tu intuición? ¿Por qué?"

3. **Fomentar experimentación** con simuladores
   - Incluir al menos 1-2 preguntas que sugieran explorar el simulador del capítulo

4. **Escalabilidad de dificultad**
   - Comenzar con preguntas que todos puedan responder
   - Terminar con preguntas que desafíen incluso a estudiantes destacados

5. **Preparar para evaluación**
   - Las preguntas deben ser similares a las que aparecerían en un examen
   - Balance entre conceptual y cuantitativo

---

## 📊 DISTRIBUCIÓN TÍPICA

Para un capítulo estándar de 20-30 páginas:

| Tipo de pregunta | Cantidad | Tiempo estimado |
|------------------|----------|-----------------|
| Conceptuales | 4-6 | 15-20 min |
| Cuantitativas | 3-5 | 30-40 min |
| Análisis de casos | 2-3 | 20-30 min |
| Integradoras | 2-3 | 15-20 min |
| **Total** | **12-17** | **80-110 min** |

**Tiempo total:** Aproximadamente 1.5-2 horas para completar todas las preguntas de estudio de un capítulo.

---

## 🔄 ADAPTACIONES POR BLOQUE

### Bloque 0 (Fundamentos):
- Más preguntas conceptuales
- Menos cuantitativas (aún no hay modelos formales)
- Casos más filosóficos sobre niveles de explicación

### Bloques I-II:
- Balance entre conceptual y cuantitativo
- Casos aplicados a ejemplos biológicos
- Conexiones con capítulos previos

### Bloques III-IV:
- Más problemas cuantitativos (modelos más complejos)
- Casos con múltiples pasos de decisión
- Preguntas que requieren comparar modelos

### Bloques V-VI:
- Integración de múltiples modelos
- Casos con incertidumbre o información incompleta
- Conexiones con aplicaciones reales (economía, IA)

---

## EJEMPLOS COMPLETOS

### Ejemplo 1: Final de capítulo sobre Rescorla-Wagner

```markdown
---

## Preguntas de Estudio

Estas preguntas están diseñadas para consolidar tu comprensión del capítulo. Se recomienda intentar responderlas sin consultar el texto primero, y luego verificar o complementar tus respuestas.

### 1. Preguntas Conceptuales

**1.1** Explica con tus propias palabras por qué el bloqueo ocurre según el modelo de Rescorla-Wagner. ¿Qué tiene que ver el error de predicción con este fenómeno?

**1.2** Un organismo con α = 0.9 aprende más rápido que uno con α = 0.1, pero también es más sensible a cambios en el ambiente. ¿Por qué existe este trade-off? ¿En qué tipo de ambientes sería ventajoso cada valor de α?

**1.3** El modelo de Rescorla-Wagner predice que la extinción no es "desaprendizaje" sino nueva asociación (EC-nada). ¿Qué evidencia experimental apoya esta interpretación? [Pista: piensa en recuperación espontánea]

**1.4** ¿Por qué el modelo usa la suma de valores (ΣV) en lugar de solo el valor del EC individual para calcular el error de predicción? ¿Qué fenómeno permite explicar esto?

**1.5** En condicionamiento clásico, el EC precede al EI temporalmente, pero el modelo calcula el cambio en V basándose en el resultado (λ). ¿Cómo resuelve el organismo esta paradoja temporal en la realidad?

### 2. Problemas Cuantitativos

**2.1** [Básico] Un EC tiene valor inicial V = 0. En cada ensayo, α = 0.3 y λ = 100. Calcula los valores de V después de los primeros 3 ensayos.

*Usa:* ΔV = α(λ - V)

**2.2** [Intermedio] Protocolo de bloqueo:
- Fase 1: EC_A solo, 5 ensayos, α = 0.4, λ = 80
- Fase 2: Compuesto AB, 3 ensayos, α_A = α_B = 0.4, λ = 80

Calcula:
a) V_A al final de Fase 1
b) Error de predicción en primer ensayo de Fase 2
c) V_B al final del entrenamiento

**2.3** [Intermedio-Avanzado] Extinción:
- Inicio: V = 90
- Protocolo: λ = 0, α = 0.3

a) Calcula V después de 5 ensayos de extinción
b) ¿Cuántos ensayos se necesitan para que V < 10?
c) ¿Cómo cambiaría tu respuesta en (b) si α = 0.6?

**2.4** [Avanzado] Inhibición condicionada:
- Fase 1: EC_A solo → EI (5 ensayos, α = 0.3, λ = 100)
- Fase 2: Compuesto AB → nada (5 ensayos, α = 0.3, λ = 0)

Calcula V_A y V_B al final del entrenamiento. ¿Por qué V_B es negativo?

### 3. Análisis de Casos

**3.1 - Caso: La Rata que Sabe Demasiado**

**Escenario:**
Una rata fue entrenada durante 20 ensayos en los que un tono (A) predecía descarga eléctrica. Desarrolló fuerte respuesta de congelamiento ante A. Después, el experimentador presentó un compuesto de tono (A) más luz (B), seguido de la misma descarga. Finalmente, cuando se probó B sola, la rata mostró congelamiento mínimo.

El experimentador está confundido: "La luz también predijo perfectamente la descarga. ¿Por qué la rata no le tiene miedo?"

**Preguntas:**
a) Usa el modelo de Rescorla-Wagner para calcular aproximadamente V_B después del entrenamiento en compuesto (asume α = 0.4, λ = 100, y que V_A al inicio de la fase de compuesto era ~85).

b) ¿Qué habría pasado si B se hubiera presentado sola con la descarga, sin estar acompañada de A?

c) Este fenómeno se llama "bloqueo". ¿Qué nos dice sobre lo que realmente aprenden los organismos? (Pista: ¿aprenden todas las correlaciones o solo las predictivamente útiles?)

**Conexión conceptual:**
Este caso ilustra el fenómeno de bloqueo y demuestra que el aprendizaje está guiado por error de predicción, no por simple contigüidad temporal.

**3.2 - Caso: Diseño Experimental**

**Escenario:**
Eres investigador y quieres demostrar que un animal aprende sobre asociaciones predictivas, no solo sobre correlaciones temporales. Tienes disponibles:
- 3 estímulos condicionados diferentes (tono, luz, textura)
- 1 estímulo incondicionado (comida)
- Capacidad de presentarlos en cualquier orden y combinación

**Preguntas:**
a) Diseña un experimento que demuestre el fenómeno de bloqueo. Especifica qué estímulos usarías en cada fase y qué predice el modelo de Rescorla-Wagner vs. una teoría de simple contigüidad.

b) ¿Qué controles experimentales necesitarías para asegurar que tus resultados se deben a bloqueo y no a otros factores (ej: B simplemente es menos saliente)?

c) Si obtuvieras los resultados que predice Rescorla-Wagner, ¿qué puedes concluir sobre cómo los animales asignan crédito causal?

**Conexión conceptual:**
Este caso requiere integrar comprensión del modelo con diseño experimental riguroso.

### 4. Conexiones Integradoras

**4.1** En el Capítulo 6 (Detección de Señales) vimos cómo organismos distinguen señales de ruido. En este capítulo vimos cómo aprenden qué señales predicen qué resultados. ¿Cómo se relacionan estos dos problemas? ¿Podría un EC con baja saliencia (difícil de detectar) ser bloqueado más fácilmente? Justifica.

**4.2** El modelo de Rescorla-Wagner explica aprendizaje sobre relaciones EC→EI, pero no explica qué pasa cuando el organismo puede controlar si el EI aparece o no. ¿Qué extensión del modelo necesitaríamos para explicar aprendizaje instrumental? [Pista: Esto es tema del Bloque III]

**4.3** Las neuronas dopaminérgicas en el cerebro de mamíferos codifican exactamente un error de predicción: disparan cuando el resultado es mejor de lo esperado, disminuyen actividad cuando es peor, y no cambian cuando es igual a lo esperado. ¿Qué sugiere esto sobre la relación entre el nivel algorítmico (modelo RW) y el nivel de implementación (neuronas)? [Referencia: Schultz, 1998 en lecturas complementarias]

**4.4** Reflexiona sobre cómo el concepto de "error de predicción" aparece en tu vida cotidiana:
- Cuando aprendes la ruta más rápida al trabajo
- Cuando Netflix te recomienda películas
- Cuando un médico actualiza un diagnóstico

Elige uno y explica cómo opera el principio de reducción de error en ese contexto.

---

## Lecturas Complementarias

### Fundamentales

**Rescorla, R. A., & Wagner, A. R. (1972).** *A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement.* In Classical Conditioning II: Current Research and Theory.

**Qué aporta:** El artículo original que presenta el modelo. Aunque usa notación ligeramente diferente, introduce los conceptos centrales de error de predicción y asignación de crédito.

**Nivel:** Intermedio | **Disponibilidad:** Biblioteca, Google Scholar

---

**Schultz, W. (1998).** *Predictive reward signal of dopamine neurons.* Journal of Neurophysiology, 80(1), 1-27.

**Qué aporta:** Evidencia neuronal de que neuronas dopaminérgicas implementan error de predicción. Conecta nivel algorítmico con implementación.

**Nivel:** Intermedio-Avanzado | **DOI:** 10.1152/jn.1998.80.1.1

---

### Clásicos

**Kamin, L. J. (1969).** *Predictability, surprise, attention, and conditioning.* En Campbell & Church (Eds.), Punishment and aversive behavior.

**Qué aporta:** Presenta el fenómeno de bloqueo que motivó el modelo RW.

**Nivel:** Introductorio

---

### Contemporáneos

**Gershman, S. J. (2015).** *A unifying probabilistic view of associative learning.* PLOS Computational Biology, 11(11), e1004567.

**Qué aporta:** Derivación Bayesiana del modelo RW. Conecta con Bloque V.

**Nivel:** Avanzado | **Open access:** doi.org/10.1371/journal.pcbi.1004567

---

### Extensiones

**Sutton, R. S., & Barto, A. G. (2018).** *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. [Capítulo 6]

**Qué aporta:** Extiende RW a aprendizaje secuencial (Bloque IV).

**Nivel:** Intermedio | **Gratis:** incompleteideas.net/book/the-book.html
```

---

## 📝 PLANTILLA VACÍA PARA COPIAR

```markdown
---

## Preguntas de Estudio

Estas preguntas están diseñadas para consolidar tu comprensión del capítulo. Se recomienda intentar responderlas sin consultar el texto primero, y luego verificar o complementar tus respuestas.

### 1. Preguntas Conceptuales

**1.1** [Pregunta]

**1.2** [Pregunta]

**1.3** [Pregunta]

**1.4** [Pregunta]

### 2. Problemas Cuantitativos

**2.1** [Básico] [Problema]

*Datos:* 
*Usa:*

**2.2** [Intermedio] [Problema]

**2.3** [Avanzado] [Problema]

### 3. Análisis de Casos

**3.1 - Caso: [Título]**

**Escenario:**
[Descripción de 3-5 oraciones]

**Preguntas:**
a) [Pregunta]
b) [Pregunta]
c) [Pregunta]

**Conexión conceptual:**
[Explicación]

**3.2 - Caso: [Título]**

[...]

### 4. Conexiones Integradoras

**4.1** [Pregunta que conecta con capítulo previo]

**4.2** [Pregunta que anticipa contenido futuro]

**4.3** [Pregunta sobre niveles de explicación o aplicación]

---

## Lecturas Complementarias

### Fundamentales

**Autor, A. (Año).** *Título.* Journal/Editorial.

**Qué aporta:** [Explicación]

**Nivel:** [Introductorio/Intermedio/Avanzado] | **Disponibilidad:** [Info]

---

### Clásicos

[...]

---

### Contemporáneos

[...]

---

### Extensiones

[...]
```

---

**Versión:** 1.0  
**Última actualización:** 26 de enero de 2026  
**Mantenedor:** Arturo Bouzas
