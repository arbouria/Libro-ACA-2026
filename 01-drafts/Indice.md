# ---
title: "Aprendizaje y Comportamiento Adaptable"
subtitle: "Principios y Modelos"
author: "Arturo Bouzas"
---

::: {.hero-banner}
![](images/cover.png){.cover-image}
:::

## Bienvenida {.unnumbered}

Este libro es una edición revisada y extendida del libro de notas [Aprendizage y Comportamiento Adaptable](https://arbouria.github.io/Notas-Aprendizaje-y-Comportamiento-Adaptable-I/). Ofrece una introducción rigurosa pero accesible a los **principios y modelos del aprendizaje y comportamiento adaptable**. A diferencia de textos tradicionales organizados por paradigmas experimentales (condicionamiento clásico, instrumental, etc.), este libro se estructura alrededor de **problemas adaptativos** que los organismos deben resolver y las **soluciones algorítmicas** que han evolucionado para enfrentarlos.

### ¿Para Quién es Este Libro? {.unnumbered}

Este libro está diseñado para:

- **Estudiantes de licenciatura** en psicología, neurociencia o ciencia cognitiva con preparación en cálculo y probabilidad básicos
- **Estudiantes de posgrado** que desean conectar psicología del aprendizaje con neurociencia computacional y machine learning
- **Profesionales en transición** de física, matemáticas, ingeniería o ciencias de la computación hacia neurociencia o ciencia cognitiva
- **Investigadores** buscando introducción formal a modelos computacionales del comportamiento

::: {.callout-important}
## Pre-requisitos

Este libro asume familiaridad con:

- **Cálculo básico**: Derivadas, gradientes, integrales simples
- **Probabilidad y estadística**: Distribuciones, probabilidad condicional, esperanza
- **Programación** (preferentemente Python): Capacidad de implementar algoritmos simples

Si necesitas refrescar estos temas, consulta los **Apéndices A, B y C**.
:::

### Filosofía del Libro {.unnumbered}

#### Marco Conceptual Unificado

El **Capítulo 1** establece un marco de explicación multinivel (Marr, Tinbergen, Killeen) que guía todo el libro. Aprenderás a distinguir entre:

- **Nivel computacional**: ¿Qué problema adaptativo se resuelve?
- **Nivel algorítmico**: ¿Qué procedimientos generan el comportamiento?
- **Nivel de implementación**: ¿Qué circuitos neuronales lo realizan?

Este marco evita confusiones comunes y te permite entender por qué diferentes tipos de modelos coexisten sin competir.

#### Énfasis en Principios Generales

En lugar de memorizar fenómenos específicos de protocolos particulares, aprenderás **principios que cruzan dominios**:

- El **ascenso de colina** (Cap 4) aplica a bacterias navegando gradientes químicos, plantas buscando luz, y algoritmos de optimización en machine learning
- La **teoría de detección de señales** (Cap 6) explica decisiones perceptuales, diagnóstico médico, y asignación de crédito en aprendizaje asociativo
- El **aprendizaje por refuerzo** (Caps 18-21) conecta comportamiento animal, neurociencia (dopamina), y robótica

#### Implementación Computacional

**Todos los modelos en este libro son implementables**. No son solo ecuaciones abstractas - puedes programarlos, simularlos, y experimentar con ellos.

::: {.callout-tip}
## 🤖 Simuladores Interactivos

Este libro incluye **simuladores embebidos** y enlaces a **notebooks interactivos** (Google Colab) donde puedes:

- Manipular parámetros y observar resultados inmediatos
- Implementar algoritmos desde cero
- Replicar experimentos clásicos
- Explorar extensiones creativas

Accede a todos los simuladores y tutoriales de matemáticas en:[Bouzas Lab](https://www.bouzaslab25.com/content/lab25.html)
:::

### Estructura del Libro {.unnumbered}

El libro está organizado en **dos semestres** con **seis bloques temáticos**:

#### Semestre I: Fundamentos y Asignación de Crédito

**Bloque 0: Marco Conceptual**  
Establece fundamentos teóricos y evolutivos

**Bloque I: Mecanismos Sin Historia**  
Algoritmos de adaptación que no requieren memoria (ascenso de colina, taxias)

**Bloque II: Decisión Bajo Incertidumbre**  
Marcos formales para decisiones óptimas (teoría de detección de señales, inferencia bayesiana)

**Bloque III: Asignación de Crédito**  
Cómo aprender qué causa qué (Rescorla-Wagner, modelos bayesianos, teoría de información)

**Bloque IV: El Problema de la Acción**  
Cómo traducir conocimiento en comportamiento (ley del efecto, elección, igualación)

#### Semestre II: Aprendizaje Secuencial y Estados Ocultos

**Bloque V: Aprendizaje Secuencial**  
Asignación de crédito temporal (diferencias temporales, Q-learning, actor-crítico)

**Bloque VI: Incertidumbre y Estados Ocultos**  
Entornos volátiles, POMDPs, modelos bayesianos avanzados

### Cómo Usar Este Libro {.unnumbered}

#### Para Estudiantes

1. **Lee el Capítulo 1** completo antes de continuar - establece el marco conceptual necesario
2. **Sigue la secuencia** - los capítulos construyen progresivamente
3. **Implementa los modelos** - usa los simuladores y crea tus propias versiones
4. **Haz los ejercicios** al final de cada capítulo
5. **Experimenta** - modifica parámetros, prueba casos límite, explora extensiones

#### Para Instructores

Este libro puede usarse para:

- **Curso de un semestre**: Bloques 0-III (fundamentos y asignación de crédito)
- **Secuencia de dos semestres**: Todo el material
- **Curso de posgrado**: Ritmo acelerado con proyectos de investigación

**Recursos disponibles:**

- Simuladores interactivos para cada tema
- Código en Google Colab (sin necesidad de instalación local)
- [Próximamente] Guía del instructor con exámenes, proyectos y rúbricas

#### Para Autodidactas

Si estudias por tu cuenta:

1. Revisa pre-requisitos en apéndices si es necesario
2. Implementa todos los modelos - el debugging fuerza comprensión profunda
3. Únete a discusiones en el [repositorio GitHub](https://github.com/bouzaslab25/libro-aca)
4. Comparte tus implementaciones y extensiones

### Recursos Adicionales {.unnumbered}

::: {.callout-note}
## Enlaces Importantes

- **Simuladores**: [Material de Apoyo Lab25](https://bouzaslab25.github.io/Material_Apoyo_ACA_I_II_III/)
- **Código fuente**: [GitHub](https://github.com/bouzaslab25/libro-aca)
- **Reportar errores**: [GitHub Issues](https://github.com/bouzaslab25/libro-aca/issues)
- **Laboratorio 25**: [www.bouzaslab25.com](https://www.bouzaslab25.com/)
:::

### Licencia y Uso {.unnumbered}

Este libro se distribuye bajo licencia **Creative Commons BY-NC-SA 4.0**. Esto significa que puedes:

✅ Compartir - copiar y redistribuir el material  
✅ Adaptar - remezclar, transformar y construir sobre el material  

Bajo las siguientes condiciones:

- **Atribución**: Debes dar crédito apropiado
- **No Comercial**: No puedes usar el material con fines comerciales
- **Compartir Igual**: Si remezclas, debes distribuir bajo la misma licencia

### Agradecimientos {.unnumbered}

Este proyecto fue financiado por **PAPIME PE309624** (UNAM).

Agradezco profundamente a:

- Todos los miembros del **Laboratorio 25** por desarrollar los simuladores interactivos
- Mis estudiantes, cuyo feedback ha sido invaluable para mejorar el material
- La comunidad open source de Python científico (NumPy, SciPy, Matplotlib, Plotly)
- Los desarrolladores de Quarto por esta plataforma excepcional

### Cómo Citar Este Libro {.unnumbered}

```bibtex
@book{bouzas2025aca,
  title = {Aprendizaje y Comportamiento Adaptable: Fundamentos Computacionales y Modelos Formales},
  author = {Bouzas, Arturo},
  year = {2025},
  publisher = {Lab25, UNAM},
  url = {https://github.com/bouzaslab25/libro-aca},
  note = {Licencia CC BY-NC-SA 4.0}
}
```

### Contacto {.unnumbered}

**Arturo Bouzas**  
Facultad de Psicología  
Universidad Nacional Autónoma de México  
📧 bouzas@unam.mx  
🌐 [www.bouzaslab25.com](https://www.bouzaslab25.com/)

---

::: {.callout-important}
## Aviso: Libro en Desarrollo

Este es un **proyecto vivo**. El contenido se actualiza regularmente basándose en:

- Feedback de estudiantes e instructores
- Nuevos desarrollos en el campo
- Mejoras en simuladores y código

Verifica el [repositorio GitHub](https://github.com/bouzaslab25/libro-aca) para la versión más reciente.

**Versión actual**: v1.0 (Enero 2025)
:::

---

¿Listo para comenzar? Pasa al **[Capítulo 0: Introducción](chapters/cap0_introduccion.qmd)** 🚀
