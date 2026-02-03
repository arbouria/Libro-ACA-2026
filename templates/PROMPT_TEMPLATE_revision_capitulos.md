# PLANTILLA DE PROMPT PARA REVISIÓN DE CAPÍTULOS
## Para usar en nuevas conversaciones en el proyecto

---

## 🎯 PROMPT COMPLETO (Copiar y adaptar)

```
Estoy escribiendo el libro "Aprendizaje y Comportamiento Adaptable: Principios y Modelos" para estudiantes de licenciatura en psicología. Este libro está organizado por problemas adaptativos (no por protocolos experimentales tradicionales) y enfatiza modelos formales con simuladores interactivos.

Necesito tu ayuda revisando el [CAPÍTULO X: TÍTULO].

## Contexto del capítulo:

**Bloque:** [Nombre del bloque, ej: "Bloque II - Asignación de Crédito"]
**Ubicación en progresión:** [ej: "Tercer capítulo del bloque, después de Detección de Señales"]
**Problema adaptativo central:** [ej: "¿Cómo asignar crédito a señales que predicen sucesos importantes?"]
**Conceptos clave:** [ej: "Condicionamiento clásico, valor asociativo, aprendizaje predictivo"]

## Tipo de revisión solicitada:

[Marca con X las que apliquen]

- [ ] **Revisión completa:** Gramática, estructura, coherencia conceptual, flujo pedagógico
- [ ] **Consistencia terminológica:** Verificar uso correcto de términos según glosario del proyecto
- [ ] **Integración de simulador:** Sugerir ubicación, parámetros, y ejercicios
- [ ] **Matemáticas:** Verificar claridad de ecuaciones, agregar ejemplos numéricos
- [ ] **Conexiones:** Referencias cruzadas con capítulos previos/posteriores
- [ ] **Ejercicios:** Diseñar preguntas de comprensión y problemas
- [ ] **Otro:** [Especificar]

## Elementos específicos que requieren atención:

1. [ej: "La sección sobre bloqueo necesita un ejemplo más claro"]
2. [ej: "Falta simulador interactivo para explorar parámetro α"]
3. [ej: "Necesito ayuda formulando ejercicios que conecten con capítulo anterior"]

## Simuladores requeridos (si aplica):

**Simulador [Número/Nombre]:**
- **Ubicación sugerida:** [Después de qué sección]
- **Objetivo pedagógico:** [Qué debe aprender el estudiante]
- **Parámetros a manipular:** [ej: "α (tasa de aprendizaje), λ (valor asintótico)"]
- **Tipo de visualización:** [ej: "Gráfica de fuerza asociativa en función de ensayos"]
- **Ejercicios necesarios:** [Número aproximado: básicos, intermedios, avanzados]

## Instrucciones adicionales:

- Mantén consistencia con el tono establecido en Prefacio e Introducción (disponibles en el proyecto)
- Usa terminología según GLOSARIO_TERMINOLOGIA.md
- Sigue formato de ecuaciones y ejemplos establecido en README
- Sugiere ubicaciones específicas para simuladores con este formato: [SIMULADOR AQUÍ: Nombre]
- Todos los ejercicios deben incluir: (1) pregunta guía, (2) instrucción de predicción previa, (3) conexión conceptual

## Preguntas específicas (opcional):

1. [ej: "¿El ejemplo del perro de Pavlov es suficientemente claro?"]
2. [ej: "¿La derivación de la ecuación de Rescorla-Wagner necesita más pasos intermedios?"]
3. [ej: "¿Los ejercicios son apropiados para el nivel de licenciatura?"]

---

Por favor:
1. Lee el capítulo completo
2. Proporciona retroalimentación estructurada
3. Genera una versión corregida si aplica
4. Documenta todas las decisiones importantes tomadas

Gracias.
```

---

## 📋 VARIANTES DEL PROMPT PARA CASOS ESPECÍFICOS

### VARIANTE A: Solo Integración de Simulador

```
Estoy escribiendo el libro "Aprendizaje y Comportamiento Adaptable: Principios y Modelos". 

Necesito integrar un simulador interactivo en el [CAPÍTULO X: TÍTULO].

**Contexto:**
- **Concepto a ilustrar:** [ej: "Regla delta de Rescorla-Wagner"]
- **Ecuación principal:** [copiar ecuación aquí]
- **Ubicación en capítulo:** [ej: "Después de presentación intuitiva, antes de derivación matemática"]

**Requisitos del simulador:**

1. **Parámetros manipulables:**
   - [Parámetro 1]: [rango sugerido]
   - [Parámetro 2]: [rango sugerido]
   - [etc.]

2. **Visualización:**
   - Tipo: [gráfica, animación, tabla interactiva]
   - Ejes: [especificar qué graficar]

3. **Ejercicios:** Necesito diseñar 3 ejercicios:
   - 1 básico (exploración guiada de un parámetro)
   - 1 intermedio (relación entre dos parámetros)
   - 1 avanzado (casos extremos o contraintuitivos)

Por favor:
- Sugiere formato completo de sección de simulador siguiendo el template del README
- Diseña ejercicios específicos con preguntas guía
- Incluye "Conexión con la teoría" para cerrar la sección

El simulador debe permitir que estudiantes de licenciatura descubran intuitivamente el principio antes de ver las matemáticas formales.
```

---

### VARIANTE B: Solo Revisión de Matemáticas

```
Estoy escribiendo el libro "Aprendizaje y Comportamiento Adaptable: Principios y Modelos" para estudiantes de licenciatura en psicología (nivel matemático: álgebra y cálculo básico del bachillerato).

Necesito revisar la claridad matemática del [CAPÍTULO X, SECCIÓN Y].

**Ecuaciones a revisar:**
[Copiar ecuaciones aquí]

**Preocupaciones específicas:**
1. [ej: "¿Los pasos de la derivación son suficientemente explícitos?"]
2. [ej: "¿Necesito más ejemplos numéricos?"]
3. [ej: "¿La notación es consistente con capítulos previos?"]

Por favor:
- Verifica que cada ecuación esté introducida intuitivamente antes de formalizarla
- Asegura que todos los símbolos estén definidos inmediatamente
- Sugiere ejemplos numéricos concretos donde falten
- Identifica saltos lógicos que puedan confundir a estudiantes
- Mantén formato establecido en README (intuición → formalización → ejemplo)
```

---

### VARIANTE C: Solo Ejercicios y Evaluación

```
Estoy escribiendo el libro "Aprendizaje y Comportamiento Adaptable: Principios y Modelos".

Necesito diseñar ejercicios de comprensión para el [CAPÍTULO X: TÍTULO].

**Conceptos clave del capítulo:**
1. [Concepto 1]
2. [Concepto 2]
3. [etc.]

**Niveles de ejercicios necesarios:**

1. **Básicos** (3-4 ejercicios):
   - Aplicación directa de fórmulas con valores dados
   - Interpretación de gráficas simples
   - Identificación de conceptos en ejemplos

2. **Intermedios** (2-3 ejercicios):
   - Integración de dos conceptos del capítulo
   - Predicción de resultados antes de calcular
   - Análisis de casos ambiguos

3. **Avanzados** (1-2 ejercicios):
   - Conexión con capítulos previos
   - Casos que revelan limitaciones del modelo
   - Extensiones creativas

Por favor diseña ejercicios específicos siguiendo este formato:

**Ejercicio X.Y - [Título]**

**Nivel:** [Básico/Intermedio/Avanzado]

**Enunciado:** [Descripción del problema]

**Preguntas:**
a) [Pregunta específica]
b) [Pregunta de profundización]

**Conexión conceptual:** [Qué principio ilustra este ejercicio]

**Solución sugerida:** [Pasos clave, no solución completa]
```

---

### VARIANTE D: Revisión de Coherencia con Capítulos Previos

```
Estoy escribiendo el libro "Aprendizaje y Comportamiento Adaptable: Principios y Modelos".

Necesito verificar coherencia del [CAPÍTULO X: TÍTULO] con capítulos previos del mismo bloque.

**Capítulos previos relevantes:**
- [Capítulo Y]: [Conceptos clave introducidos]
- [Capítulo Z]: [Conceptos clave introducidos]

**Verificaciones necesarias:**

1. **Terminología:** ¿Uso términos consistentemente con definiciones previas?
2. **Referencias cruzadas:** ¿Dónde debería referenciar explícitamente capítulos anteriores?
3. **Progresión conceptual:** ¿El nivel de complejidad es apropiado dada la secuencia?
4. **Redundancia:** ¿Estoy repitiendo innecesariamente algo ya cubierto?
5. **Lagunas:** ¿Asumo conocimiento que no fue establecido previamente?

Por favor:
- Lee los capítulos previos disponibles en el proyecto
- Identifica problemas de coherencia específicos
- Sugiere dónde agregar referencias cruzadas
- Señala conceptos que necesitan ser re-introducidos brevemente
```

---

## 🎯 CONSEJOS PARA USAR ESTOS PROMPTS

### 1. Personaliza según necesidad
- Combina variantes si necesitas múltiples tipos de revisión
- Sé específico sobre tus preocupaciones
- Incluye ejemplos concretos de lo que buscas

### 2. Proporciona contexto suficiente
- Menciona siempre el bloque temático
- Indica relación con capítulos previos/posteriores
- Especifica la audiencia (licenciatura en psicología)

### 3. Sé claro sobre el tipo de ayuda
- ¿Quieres solo retroalimentación o también versión corregida?
- ¿Necesitas explicación de decisiones o solo implementación?
- ¿Prefieres múltiples opciones o una sola recomendación?

### 4. Utiliza el proyecto efectivamente
- Menciona que hay otros capítulos disponibles para referencia
- Pide verificación de consistencia con materiales del proyecto
- Solicita que se consulte el glosario terminológico si existe

---

## 📝 EJEMPLO DE USO REAL

### Situación: Necesitas revisar Capítulo 7 sobre Condicionamiento Clásico

```
Estoy escribiendo el libro "Aprendizaje y Comportamiento Adaptable: Principios y Modelos" para estudiantes de licenciatura en psicología. Este libro está organizado por problemas adaptativos y enfatiza modelos formales con simuladores interactivos.

Necesito tu ayuda revisando el Capítulo 7: Condicionamiento Clásico y el Modelo de Rescorla-Wagner.

## Contexto del capítulo:

**Bloque:** Bloque II - El Problema del Conocimiento (Asignación de Crédito)
**Ubicación en progresión:** Segundo capítulo del bloque, después de "Detección de Señales"
**Problema adaptativo central:** ¿Cómo aprenden los organismos qué señales predicen sucesos importantes? ¿Por qué algunas asociaciones se aprenden y otras no?
**Conceptos clave:** Condicionamiento clásico, valor asociativo, aprendizaje predictivo, bloqueo, regla delta

## Tipo de revisión solicitada:

- [X] **Revisión completa:** Gramática, estructura, coherencia conceptual, flujo pedagógico
- [X] **Consistencia terminológica:** Verificar uso correcto de términos según glosario del proyecto
- [X] **Integración de simulador:** Sugerir ubicación, parámetros, y ejercicios
- [ ] **Matemáticas:** Verificar claridad de ecuaciones (ya está bien)
- [X] **Conexiones:** Referencias cruzadas con Capítulo 6 (Detección de Señales)
- [X] **Ejercicios:** Diseñar preguntas de comprensión y problemas

## Elementos específicos que requieren atención:

1. La sección sobre "bloqueo" necesita un ejemplo más intuitivo antes de explicar por qué el modelo RW lo predice
2. Falta simulador interactivo para explorar efectos de α y λ en diferentes protocolos
3. La transición entre condicionamiento clásico (descripción fenomenológica) y modelo RW (formalización) es muy abrupta
4. Necesito conectar mejor con Capítulo 6 donde introduje el concepto de "señal" y "ruido"

## Simuladores requeridos:

**Simulador 7.1: Explorador Rescorla-Wagner**
- **Ubicación sugerida:** Después de presentar intuitivamente el problema del bloqueo, antes de mostrar las ecuaciones
- **Objetivo pedagógico:** Que el estudiante descubra que lo que importa es el error de predicción, no solo la contigüidad temporal
- **Parámetros a manipular:**
  - α (tasa de aprendizaje del EC): 0.0 a 1.0
  - λ (valor del EI): 0 a 100
  - Tipo de protocolo: Adquisición simple, Bloqueo, Inhibición condicionada
- **Tipo de visualización:** Gráfica de V (fuerza asociativa) vs. ensayos, con opción de mostrar error de predicción
- **Ejercicios necesarios:** 3 básicos, 2 intermedios, 1 avanzado

## Instrucciones adicionales:

- El capítulo debe sentirse como resolución natural del problema planteado en Cap. 6
- Usa "sucesos biológicamente importantes" en lugar de "reforzadores" (ese término lo introduzco formalmente en Bloque III)
- El ejemplo de Pavlov debe servir solo como motivación histórica breve, no como eje del capítulo
- Enfatiza más el problema computacional (asignación de crédito) que el protocolo experimental

## Preguntas específicas:

1. ¿La progresión de: fenómeno del bloqueo → intuición del error de predicción → formalización RW es clara?
2. ¿Los ejercicios del simulador permiten descubrir el principio sin que yo lo diga explícitamente primero?
3. ¿Necesito una sección aparte sobre "Limitaciones del modelo RW" o la integro en cada subsección?

---

Por favor:
1. Lee el capítulo completo y también el Capítulo 6 (Detección de Señales) disponible en el proyecto
2. Proporciona retroalimentación estructurada sobre cada elemento
3. Genera una versión corregida del capítulo
4. Diseña completamente la sección del simulador con ejercicios específicos
5. Sugiere 2-3 ejercicios finales de comprensión para cerrar el capítulo

Gracias.
```

---

## 🔄 DESPUÉS DE LA CONVERSACIÓN

### Checklist post-revisión:

- [ ] Descargué la versión corregida
- [ ] Revisé todos los cambios sugeridos
- [ ] Implementé los cambios que acepto
- [ ] Documenté decisiones importantes en README (si aplica)
- [ ] Actualicé estado del capítulo en tabla de seguimiento
- [ ] Agregué términos nuevos a GLOSARIO_TERMINOLOGIA.md (si aplica)
- [ ] Marqué simulador como "diseñado, pendiente implementación" (si aplica)

---

## 📌 RECORDATORIOS FINALES

1. **Siempre menciona que tienes un proyecto** con materiales de referencia (Prefacio, Introducción, otros capítulos)

2. **Pide que Claude consulte esos materiales** para mantener consistencia

3. **Sé específico sobre lo que necesitas** - no uses el prompt genérico si solo necesitas una cosa específica

4. **Incluye contexto pedagógico** - recuerda que es para estudiantes de licenciatura en psicología

5. **Documenta decisiones importantes** - si Claude sugiere algo que cambias, anótalo en el README para futuras referencias

---

**Versión de esta plantilla:** 1.0  
**Última actualización:** 26 de enero de 2026
