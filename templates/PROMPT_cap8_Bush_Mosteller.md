# PROMPT — Capítulo 8: El Modelo de Bush y Mosteller
## Aprendizaje y Comportamiento Adaptable: Principios y Modelos

---

## CONTEXTO DEL PROYECTO

Estoy escribiendo el libro *Aprendizaje y Comportamiento Adaptable: Principios y Modelos* para estudiantes de licenciatura en psicología (matemáticas nivel bachillerato). El libro está organizado por problemas adaptativos, no por protocolos experimentales, y enfatiza modelos formales con simuladores interactivos en Python/Google Colab.

**Archivos de referencia disponibles en el proyecto:**
- `cap4_REESCRITO.md` y `cap5_FINAL_v3.md` — estilo de referencia (Bloque I)
- `cap6_REESCRITO.md` — capítulo precedente inmediato (asignación de crédito a estímulos)
- `cap7_REESCRITO_v3.md` — capítulo precedente directo (asignación de crédito a respuestas) ← **leer obligatoriamente**
- `GLOSARIO_TERMINOLOGIA.md` — terminología oficial
- `Aprendizaje_por_refuerzo.md` — borrador viejo del capítulo ← **leer obligatoriamente**
- `estilo_libro_aca.py` — módulo Python de estilo visual para todas las figuras del libro

---

## POSICIÓN DEL CAPÍTULO EN EL LIBRO

**Bloque II — El Problema del Conocimiento: Asignación de Crédito**

- Cap. 6: Asignación de crédito a estímulos (contigüidad, sesgos inductivos, Rescorla-Wagner introducido al final)
- Cap. 7: Asignación de crédito a respuestas (inducción, Staddon-Simmelhag, Dickinson, Lattal, Killeen) ← capítulo anterior
- **Cap. 8: El modelo de Bush y Mosteller** ← este capítulo
- Cap. 9+: Rescorla-Wagner (estímulos compuestos como elementos separables que compiten)

El capítulo 8 es el puente formal entre los dos capítulos de evidencia empírica (6 y 7) y los modelos más complejos que vienen después.

---

## LO QUE EL ESTUDIANTE YA SABE AL LLEGAR A ESTE CAPÍTULO

- El problema de la asignación de crédito: ¿qué estímulos/respuestas merecen ser identificados como predictores o productores de SBIs?
- Que la contigüidad no es ni necesaria ni suficiente (evidencia de caps. 6 y 7)
- Que los organismos son detectores de contingencia estadística, no registradores de contigüidad
- Curvas de aprendizaje empíricas: adquisición y extinción tienen forma negativa y positivamente acelerada, respectivamente
- Que Bush y Mosteller propusieron el modelo de actualización de valor (mencionado al cierre del cap. 7, sin desarrollar)
- **No conoce aún Rescorla-Wagner**: ese modelo aparece en el capítulo siguiente, cuando se introduce la idea de que los estímulos compuestos son separables en elementos que compiten entre sí

---

## DECISIONES EDITORIALES CRÍTICAS PARA ESTE CAPÍTULO

### 1. Bush-Mosteller es anterior e independiente de Rescorla-Wagner
Bush y Mosteller (1951) propusieron la ecuación de actualización **antes** que Rescorla y Wagner (1972). La contribución conceptual de R&W no está en la ecuación de actualización —que ya existía— sino en suponer que los estímulos en un compuesto son separables en elementos que compiten entre sí por el crédito predictivo. Eso produce el bloqueo y los fenómenos de interacción entre estímulos, y es el tema del capítulo siguiente. **No mezclar los dos modelos en este capítulo.**

### 2. La ley del efecto de Thorndike/Skinner como principio de acción, no de aprendizaje
El autor distingue explícitamente entre:
- **Principios de conocimiento/aprendizaje**: cómo el organismo detecta la estructura causal del entorno y actualiza el valor de estímulos y respuestas (tema de este capítulo)
- **Principios de acción**: cómo el organismo usa ese conocimiento para decidir qué hacer (tema del Bloque III: programas de refuerzo, igualación, elección óptima)

La ley del efecto de Skinner —"el reforzador fortalece la respuesta que lo precede"— es un principio de acción, no de aprendizaje. **No presentar B&M como formalización de la ley del efecto.** B&M formaliza el proceso de actualización del valor predictivo de estímulos y respuestas, que es una cuestión de conocimiento.

### 3. Las tres interpretaciones de la ecuación son el argumento central del capítulo
La ecuación de Bush y Mosteller admite tres lecturas que son matemáticamente equivalentes pero conceptualmente distintas. El capítulo debe desarrollarlas todas, mostrando que ninguna es "la correcta":

  a) **Integrador con fuga (carga-descarga)**: lectura literal. El refuerzo carga el valor; la presentación del estímulo sin refuerzo lo descarga. El parámetro *a* balancea experiencia acumulada vs. experiencia presente.

  b) **Reducción del error de predicción (regla delta)**: misma ecuación reordenada. El cambio en V es proporcional a la diferencia entre lo que ocurrió (R) y lo que se esperaba (V). Cuando esa diferencia es cero, no hay aprendizaje. Es la lectura dominante en psicología del aprendizaje y neurociencia.

  c) **Media exponencial corrida**: misma ecuación leída estadísticamente. V es el promedio ponderado de todos los refuerzos pasados, donde las experiencias recientes pesan más que las lejanas. Es la lectura estándar en machine learning.

  **El orden pedagógico preferido**: primero la de carga-descarga (más intuitiva para el estudiante), luego la derivación algebraica que muestra que es equivalente a la de reducción de error, luego la interpretación como media exponencial corrida. El borrador viejo ya tiene el esquema de esa derivación —usarlo.

### 4. El capítulo arranca desde las curvas de aprendizaje empíricas
El borrador viejo comienza con curvas de adquisición y extinción (Parssey 1948 para condicionamiento clásico; Ramond 1954 para instrumental). Esa es la estrategia correcta: el modelo formal se presenta como respuesta a la pregunta "¿qué función matemática describe esas curvas?", no como axioma. Mantener esa estructura.

### 5. Figuras con código Python usando el módulo de estilo unificado
Todas las figuras deben generarse con el módulo `estilo_libro_aca.py` (disponible en outputs). La cabecera estándar para cada bloque de figura es:

```python
import sys
sys.path.insert(0, '.')
from estilo_libro_aca import aplicar_estilo, COLORES, MARCADORES, LINEAS, nueva_figura, guardar_figura
aplicar_estilo()
```

---

## ESTRUCTURA SUGERIDA PARA EL CAPÍTULO

1. **Apertura** — retomar del cap. 7: tenemos evidencia de que los organismos detectan contingencias estadísticas. ¿Qué algoritmo podría producir ese resultado? La pregunta no es nueva: las curvas de aprendizaje llevan más de un siglo documentándola.

2. **Curvas de aprendizaje** — presentar los dos ejemplos empíricos del borrador viejo (Parssey 1948, Ramond 1954). Preguntar: ¿qué tienen en común? ¿Qué función matemática tiene esta forma? Anticipar que el modelo debe reproducirla.

3. **Simulador de sistemas dinámicos discretos** — antes de la ecuación formal, el estudiante debe tener intuición sobre ecuaciones recurrentes. El borrador viejo remite a un simulador externo; aquí debe estar integrado como bloque de código en el capítulo.

4. **Primera lectura: integrador con fuga (carga-descarga)** — presentar la ecuación V(t+1) = (1-a)·V(t) + a·R(t). Mostrar que produce curvas negativa y positivamente aceleradas. Interpretar *a*. Ejemplo numérico paso a paso.

5. **Segunda lectura: reducción del error de predicción** — derivación algebraica completa desde la ecuación de carga-descarga. Mostrar que ΔV = a·(R - V) es la misma ecuación vista desde otro ángulo. Interpretar (R - V) como error de predicción. Conexión con el concepto de error de predicción del cap. 6.

6. **Tercera lectura: media exponencial corrida** — mostrar que V es el promedio ponderado exponencialmente de todos los R pasados. Ejemplo con datos COVID o similares (el borrador de diapositivas del cap. 8 usa ese ejemplo — ver transcripción). Conexión con machine learning.

7. **Las tres lecturas son la misma ecuación** — sección de síntesis que hace explícita la equivalencia matemática y el valor pedagógico de cada interpretación.

8. **Simulador de la ecuación B&M** — parámetros: *a* (tasa de aprendizaje), secuencia de refuerzos, condiciones de adquisición y extinción.

9. **Extensiones y límites del modelo** — qué explica (forma de las curvas, velocidad de aprendizaje, extinción) y qué no (competencia entre estímulos → eso requiere el modelo del capítulo siguiente).

10. **Conexiones** — hacia atrás: error de predicción como puente con caps. 6-7; hacia adelante: R&W extiende B&M suponiendo que los estímulos en un compuesto son separables.

---

## PRINCIPIOS DE ESCRITURA (NO NEGOCIABLES)

- **Prosa continua**, no listas de bullets en el cuerpo del texto
- **Segunda persona** para instrucciones: "Observa que...", "Nota cómo..."
- **Primera persona plural** para razonamiento compartido: "Podemos derivar...", "Asumiremos que..."
- **Ejemplos cotidianos** antes de los ejemplos de laboratorio
- **Cada ecuación**: (1) presentación intuitiva en palabras, (2) derivación paso a paso, (3) ejemplo numérico concreto con tabla
- **Sin "museografía"**: no listar fenómenos sin principio unificador
- **Matemáticas graduales**: el estudiante tiene álgebra bachillerato; el cálculo diferencial se evita o se explica desde cero si aparece

---

## TAREA ESPECÍFICA

Usando como base el borrador en `Aprendizaje_por_refuerzo.md` y el estilo de referencia de `cap4_REESCRITO.md` y `cap6_REESCRITO.md`, generar una versión reescrita del capítulo 8 que:

1. Mantenga la estructura del borrador pero lo convierta a prosa continua en el estilo establecido del libro
2. Desarrolle las tres interpretaciones de la ecuación con la derivación algebraica completa (que el borrador tiene parcialmente)
3. Incluya ejemplos numéricos con tablas para cada interpretación
4. Integre los simuladores como bloques de código Python con el módulo `estilo_libro_aca.py`
5. Genere las figuras de curvas de aprendizaje (Parssey/Ramond) como código Python con datos digitalizados, usando el módulo de estilo
6. Establezca con claridad que B&M es un modelo de actualización del **valor predictivo** (conocimiento), no un principio de acción
7. Cierre anticipando que la siguiente extensión —R&W— modifica el modelo para manejar estímulos compuestos con elementos que compiten

**Nota sobre el borrador viejo**: el borrador usa "refuerzo" y "reforzador" donde el libro dice "suceso biológicamente importante" (SBI). Verificar consistencia con el GLOSARIO_TERMINOLOGIA.md.

---

## RECORDATORIO FINAL

El estudiante que llega a este capítulo ya entiende *por qué* los organismos necesitan un mecanismo de actualización de valor. Lo que no tiene todavía es la ecuación. El capítulo debe sentirse como: "Aquí está la solución formal al problema que llevamos dos capítulos describiendo" —no como un capítulo de matemáticas desconectado de la evidencia empírica.
