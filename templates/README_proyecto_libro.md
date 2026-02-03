# Aprendizaje y Comportamiento Adaptable: Principios y Modelos
## Proyecto de Libro - Documentación Interna

**Autor:** Arturo Bouzas  
**Institución:** Facultad de Psicología, UNAM  
**Versión del proyecto:** 1.0  
**Última actualización:** Enero 2026

---

## 📚 Propósito de Este Proyecto

Este proyecto de Claude contiene todos los materiales de referencia para el libro *Aprendizaje y Comportamiento Adaptable: Principios y Modelos*. Sirve como repositorio maestro para:

1. Mantener **coherencia conceptual** entre capítulos
2. Garantizar **consistencia terminológica** en todo el libro
3. Preservar el **tono y estilo** establecidos en Prefacio e Introducción
4. Facilitar **referencias cruzadas** entre capítulos
5. Documentar **decisiones editoriales** importantes

---

## 📂 Estructura del Proyecto

```
/proyecto/
├── README.md                          (este archivo)
├── PROMPT_TEMPLATE.md                 (plantilla para nuevas conversaciones)
├── GLOSARIO_TERMINOLOGIA.md          (términos técnicos y su uso)
│
├── 00_prefacio.md                     (versión final)
├── 00_introduccion.md                 (versión final)
│
├── Bloque_0_Fundamentos/
│   ├── 01_explicacion_aca.md
│   ├── 02_seleccion_natural.md
│   └── 03_psicofisica.md
│
├── Bloque_I_Mecanismos_Sin_Historia/
│   ├── 04_ascenso_colina.md
│   └── 05_retroalimentacion.md
│
├── Bloque_II_Asignacion_Credito/
│   ├── 06_deteccion_senales.md
│   ├── 07_condicionamiento_clasico.md
│   └── [futuros capítulos]
│
├── Bloque_III_Eleccion_Optimizacion/
│   └── [futuros capítulos]
│
├── Bloque_IV_Aprendizaje_Secuencial/
│   └── [futuros capítulos]
│
├── Bloque_V_Incertidumbre/
│   └── [futuros capítulos]
│
└── Bloque_VI_Estructura_Preferencias/
    └── [futuros capítulos]
```

---

## 🎯 Workflow para Revisión de Capítulos

### Antes de cada conversación:

1. **Verifica que el capítulo esté en el proyecto** (en su carpeta de bloque correspondiente)
2. **Revisa el PROMPT_TEMPLATE.md** para copiar el prompt optimizado
3. **Ten clara tu intención:**
   - ¿Revisión completa (gramática + estructura + contenido)?
   - ¿Solo verificación de consistencia terminológica?
   - ¿Integración de simuladores?
   - ¿Ejercicios y preguntas de comprensión?

### Durante la conversación:

4. **Usa el prompt template** (adaptándolo al capítulo específico)
5. Claude tendrá acceso a:
   - Prefacio e Introducción (para mantener tono)
   - Capítulos previos del mismo bloque (para referencias)
   - Glosario terminológico (para consistencia)

### Después de la conversación:

6. **Descarga la versión corregida** desde `/outputs/`
7. **Revisa los cambios** sugeridos
8. **Decide qué implementar**
9. **Opcionalmente:** Actualiza el archivo en el proyecto cuando tengas la versión final

### Actualización periódica del proyecto:

Después de revisar 3-4 capítulos, considera actualizar el proyecto con las versiones finales para que estén disponibles como referencia en futuras conversaciones.

---

## 📋 Convenciones del Libro

### Terminología Establecida

**USO CONSISTENTE (ver GLOSARIO_TERMINOLOGIA.md para detalles):**

| Concepto | Término preferido | Evitar | Contexto |
|----------|------------------|--------|----------|
| Eventos importantes | "sucesos biológicamente importantes" | "reforzadores" (hasta Bloque III) | Texto técnico |
| Recursos | "recursos" | "recompensas" | Ejemplos introductorios |
| Resultados de acciones | "consecuencias" | "outcomes" | Descripción de experimentos |
| Señales predictivas | "señales" o "estímulos predictivos" | "CSs" (hasta definirlo) | Antes de terminología técnica |
| Organismo adaptativo | "agente" | "organismo" o "animal" | Contexto formal/algorítmico |

### Formato de Ecuaciones

- **Primera mención:** Presentar intuitivamente antes de formalizar
- **Desarrollo paso a paso:** Mostrar derivaciones intermedias
- **Ejemplos numéricos:** Siempre incluir después de ecuación abstracta
- **Notación:** Definir todos los símbolos inmediatamente

**Ejemplo del formato preferido:**

```markdown
El cambio en la fuerza asociativa depende de cuán sorprendente fue el resultado. Si esperábamos un valor alto pero obtuvimos uno bajo, la predicción debe ajustarse:

$$\Delta V = \alpha(\lambda - V)$$

donde:
- $V$ es el valor predicho actual
- $\lambda$ es el valor real que apareció  
- $\alpha$ es la tasa de aprendizaje (0 < α < 1)
- $\Delta V$ es el cambio en la predicción

**Ejemplo concreto:** [incluir cálculo numérico aquí]
```

### Formato de Simuladores

**Ubicación estándar en capítulos:**

1. **Después de presentación intuitiva** del concepto (sin ecuaciones aún)
2. **Antes de derivaciones matemáticas** complejas
3. **Al final de sección principal** para consolidar

**Formato de inclusión:**

```markdown
## [Título de Sección]

[Explicación intuitiva del concepto: 2-3 párrafos]

### 🎮 Simulador Interactivo: [Nombre Descriptivo]

**Objetivo:** [Qué debe descubrir el estudiante al usar el simulador]

[AQUÍ VA SIMULADOR EMBEDDED - Indicación de ubicación]

**Parámetros manipulables:**
- **α (tasa de aprendizaje):** Controla qué tan rápido se aprende de cada experiencia
  - Valores sugeridos: Prueba α = 0.1, α = 0.5, α = 0.9
  - ¿Qué pasa con α = 1.0 (caso extremo)?

- **[Parámetro 2]:** [Descripción]
  - Valores sugeridos: [rango]
  - ¿Qué pasa cuando...?

**Ejercicios:**

1. **[Ejercicio básico]:** [Descripción de qué hacer y qué observar]
   - *Pregunta guía:* [Pregunta específica]
   - *Predicción:* Antes de cambiar el parámetro, predice qué sucederá

2. **[Ejercicio intermedio]:** [Requiere combinar dos parámetros]
   - *Pregunta guía:* [Pregunta que conecta con concepto teórico]

3. **[Ejercicio avanzado]:** [Exploración abierta o caso extremo]
   - *Desafío:* [Romper el modelo intencionalmente]

**Conexión con la teoría:** [1 párrafo explicando cómo lo observado en el simulador ilustra el principio matemático que viene a continuación]

---

[Continúa con formalización matemática]
```

### Formato de Figuras

```markdown
**Figura X.Y:** [Título descriptivo]

[IMAGEN O DIAGRAMA]

**Interpretación:** [2-3 líneas explicando qué muestra la figura y qué conclusión debe extraer el lector]
```

### Formato de Ejemplos

```markdown
**Ejemplo X.Y - [Título Descriptivo]**

**Situación:** [Descripción concreta del escenario]

**Análisis:** [Aplicación del concepto al ejemplo]

**Predicción del modelo:** [Qué predice la teoría]

**Conexión conceptual:** [Por qué este ejemplo ilustra el principio general]
```

### Tono y Voz

- **Segunda persona para instrucciones:** "Observa que...", "Nota cómo..."
- **Primera persona plural para razonamiento compartido:** "Asumiremos que...", "Podemos derivar..."
- **Evitar:** "El lector notará", construcciones pasivas excesivas
- **Preferir:** Voz activa, ejemplos concretos antes de abstracciones

### Estructura de Capítulos

**Estructura estándar:**

```markdown
# Capítulo X: [Título]

## Introducción
[2-3 párrafos estableciendo el problema adaptativo]

## El Problema [Descriptivo]
[Presentación intuitiva sin matemáticas]

## [Simulador 1 - Exploración inicial]

## Formalización: [Concepto Principal]
[Desarrollo matemático paso a paso]

## Aplicaciones y Ejemplos
[Casos concretos]

## [Simulador 2 - Consolidación - opcional]

## Extensiones y Limitaciones
[Qué NO resuelve este modelo]

## Conexiones
[Con capítulos anteriores y posteriores]

## Resumen
[Puntos clave en 3-5 bullets]

## Lecturas Complementarias
[Referencias actualizadas]
```

---

## 🔄 Estados de Capítulos

Mantén seguimiento del estado de cada capítulo:

### Estados posibles:
- **[BORRADOR]** - Primera versión, sin revisar
- **[EN REVISIÓN]** - Conversación activa con Claude
- **[REVISADO]** - Gramática y estructura verificadas
- **[SIMULADORES PENDIENTES]** - Esperando integración de simuladores
- **[FINAL]** - Listo para publicación

### Registro de Estado (actualizar según progreses):

| Capítulo | Estado | Última actualización | Notas |
|----------|--------|---------------------|-------|
| 00_prefacio | [FINAL] | 26-01-2026 | Versión corregida con tono suavizado |
| 00_introduccion | [FINAL] | 26-01-2026 | Estructura reorganizada, ejemplo Wall-E mejorado |
| 01_explicacion_aca | [REVISADO] | [fecha] | [notas] |
| 04_ascenso_colina | [BORRADOR] | [fecha] | Necesita simulador interactivo |
| ... | | | |

---

## 📖 Decisiones Editoriales Importantes

### Documentación de decisiones clave:

**1. Organización por problemas adaptativos vs. protocolos**
- **Decisión:** Estructura por bloques temáticos (problemas adaptativos)
- **Rationale:** Mayor coherencia conceptual, conecta con desarrollos contemporáneos
- **Fecha:** Enero 2026

**2. Tono en "Argumento Final"**
- **Decisión:** Versión suavizada que reconoce valor de enfoque tradicional
- **Rationale:** Facilitar adopción por instructores que usan textos tradicionales
- **Fecha:** 26-01-2026

**3. Uso de "sucesos biológicamente importantes" vs "reforzadores"**
- **Decisión:** "Sucesos biológicamente importantes" en capítulos iniciales
- **Rationale:** Neutral, no presupone mecanismo, introduce "reforzador" formalmente en Bloque III
- **Fecha:** Enero 2026

**4. Ubicación de simuladores**
- **Decisión:** Después de intuición, antes de formalización matemática compleja
- **Rationale:** Construir intuición empírica antes de abstracción
- **Fecha:** 26-01-2026

[Agregar nuevas decisiones importantes aquí]

---

## 🎓 Referencias de Estilo

### Libros que admiramos y de los que aprendemos:

1. **"Computational Cognitive Neuroscience"** (O'Reilly et al.)
   - Lo que nos gusta: Balance teoría-implementación
   - Lo que adaptamos: Estructura de ejercicios prácticos

2. **"Reinforcement Learning: An Introduction"** (Sutton & Barto)
   - Lo que nos gusta: Claridad matemática sin sacrificar intuición
   - Lo que adaptamos: Progresión de simple a complejo

3. **"Theoretical Neuroscience"** (Dayan & Abbott)
   - Lo que nos gusta: Rigor sin pedantería
   - Lo que evitamos: Densidad excesiva para audiencia introductoria

---

## 🛠️ Herramientas y Recursos

### Simuladores:
- **Plataforma principal:** Bouzas Lab (https://www.bouzaslab25.com)
- **Backup notebooks:** Google Colab
- **Formato preferido:** Widgets interactivos (sliders para parámetros)

### Tutoriales de matemáticas:
- Disponibles en Bouzas Lab
- Cubren: álgebra básica, ecuaciones diferenciales simples, probabilidad

### Repositorio:
- **GitHub:** https://github.com/bouzaslab25/libro-aca
- **Issues:** Para reporte de errores
- **Discusiones:** Para retroalimentación de lectores

---

## 📝 Notas para Futuras Conversaciones con Claude

### Información siempre relevante:

1. **Audiencia principal:** Estudiantes de licenciatura en psicología (con matemáticas de bachillerato)

2. **Filosofía pedagógica:** Construir intuición con simuladores ANTES de formalización matemática

3. **Nivel matemático objetivo:**
   - Álgebra básica: ✅ Siempre accesible
   - Cálculo simple: ✅ Con explicación cuidadosa
   - Probabilidad básica: ✅ Con recordatorios
   - Optimización: ✅ Intuitiva primero, formal después

4. **Tono establecido:**
   - Pedagógico pero riguroso
   - Respetuoso de enfoques tradicionales
   - Conectado con aplicaciones contemporáneas
   - Sin condescendencia ni pedantería

5. **Prohibiciones estilísticas:**
   - ❌ Listas extensas de fenómenos sin principio unificador
   - ❌ "Museo de curiosidades históricas"
   - ❌ Matemáticas sin intuición previa
   - ❌ Simuladores sin ejercicios específicos
   - ❌ Ecuaciones sin ejemplos numéricos

---

## 🔮 Próximos Pasos

### Prioridades inmediatas:

1. [ ] Crear GLOSARIO_TERMINOLOGIA.md
2. [ ] Revisar capítulos del Bloque 0 (Fundamentos)
3. [ ] Integrar simuladores en Bloque I
4. [ ] Desarrollar banco de ejercicios estándar

### Capítulos en pipeline:

- [ ] Capítulo 7: Condicionamiento Clásico
- [ ] Capítulo 8: Modelos de Error de Predicción
- [ ] Capítulo 9: Filtros Bayesianos
- [ ] [Agregar según progreses]

---

## 📧 Contacto y Soporte

**Autor:** Arturo Bouzas  
**Email:** arbouria@unam.mx  
**Laboratorio:** Lab 25, Facultad de Psicología, UNAM  
**Web:** www.bouzaslab25.com

---

## 📄 Licencia

Este proyecto de desarrollo (no el libro publicado) es material de trabajo interno.

El libro final se publicará bajo **Creative Commons BY-NC-SA 4.0**.

---

**Última actualización de este README:** 26 de enero de 2026
