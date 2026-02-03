# Introducción al Curso {.unnumbered}

> *"Lo que no puedo crear, no lo entiendo."* — Richard Feynman

## Un Problema de Diseño

Imagina que te encargan diseñar un robot explorador para un planeta desconocido. El robot debe localizar recursos dispersos en un terreno accidentado, evitar peligros, y gestionar su limitada energía. Para ello, cuentas con sensores imperfectos (cámaras con ruido, detectores químicos con umbrales de sensibilidad), un procesador con capacidad finita, y restricciones severas de tiempo y energía. ¿Qué capacidades mínimas debe tener este robot para sobrevivir?

Necesitará, al menos:
- **Sensores** que transformen energía física en señales procesables, distinguiendo información útil del ruido ambiental.
- **Navegación** que le permita moverse hacia concentraciones de recursos detectadas a distancia.
- **Aprendizaje predictivo** que le permita anticipar dónde aparecerán recursos basándose en señales previas (si cierta formación rocosa predice agua cercana).
- **Sistemas de elección** que le permitan decidir racionalmente entre opciones cuando los recursos son múltiples y los comportamientos compiten entre sí.

Este no es un ejercicio de ciencia ficción. Es exactamente el problema que enfrentan todos los organismos vivos. Un ratón buscando alimento, una bacteria navegando gradientes químicos, un estudiante decidiendo cuánto tiempo dedicar a cada materia, un algoritmo de ajedrez evaluando jugadas—todos enfrentan variantes del mismo desafío fundamental: **cómo distribuir su comportamiento en el tiempo y en el espacio para maximizar la obtención de recursos necesarios para sobrevivir, reproducirse, o cumplir sus objetivos**.

Este curso estudia las soluciones biológicas y computacionales a este problema. Pero antes de construir ese robot—o de entender cómo funcionan los organismos—debemos confrontar un problema pedagógico previo.

## El Problema con la Enseñanza Tradicional

Imagina a un estudiante que acaba de terminar un curso introductorio de "Psicología del Aprendizaje". Ha dedicado un semestre a estudiar condicionamiento clásico (Pavlov y sus perros), condicionamiento operante (Skinner y sus palomas), programas de refuerzo (razón fija, intervalo variable), y quizás, si tuvo suerte, un capítulo final sobre "temas avanzados" donde aparece brevemente la igualación de Herrnstein. Al final del curso, ¿qué tiene en su cabeza? Un catálogo de fenómenos: bloqueo, ensombrecimiento, moldeamiento, extinción, recuperación espontánea, efecto de contraste. Una lista de nombres: Pavlov, Thorndike, Watson, Skinner, Tolman. Una colección de protocolos experimentales: cajas de condicionamiento, laberintos en T, programas de refuerzo.

La estrategia pedagógica tradicional para enseñar aprendizaje y comportamiento adaptable, reflejada en la organización típica de los libros de texto, presenta casi exclusivamente las principales regularidades empíricas derivadas de más de 100 años de investigación, organizadas alrededor de protocolos experimentales específicos: condicionamiento clásico (Pavlov), condicionamiento operante (Skinner), programas de refuerzo, y quizás, si tuvo suerte, una clase sobre el modelo de Rescorla-Wagner y el principio de igualación de Herrnstein. Si bien este enfoque tiene valor histórico y permite apreciar la riqueza empírica del campo, puede dejar frecuentemente al estudiante con la impresión de que este es un área de conocimiento estática, fragmentada y predominantemente de interés histórico, llena de hallazgos aislados y con escasa coherencia conceptual.

Los estudiantes terminan ese curso sin una visión coherente de los principios que unifican estos fenómenos, ni una comprensión de por qué este campo sigue siendo relevante en el siglo XXI. Los hallazgos aparecen desconectados entre sí y, peor aún, desconectados de desarrollos contemporáneos en neurociencias, inteligencia artificial, economía conductual y teoría de la decisión.

Este curso adopta una estrategia diferente.

## La Promesa de Este Curso

### Un Problema Adaptativo Fundamental

En el centro de este curso está el problema biológico fundamental que mencionamos al inicio: **cómo distribuir el comportamiento en el tiempo y en el espacio para maximizar la obtención de recursos necesarios para sobrevivir y reproducirse**.

Este problema unifica fenómenos aparentemente dispares. Un ratón buscando alimento, un estudiante decidiendo cuánto tiempo dedicar a cada materia, un algoritmo de ajedrez evaluando jugadas, una bacteria moviéndose hacia nutrientes—todos enfrentan variantes del mismo desafío. Deben aprender qué aspectos de su entorno predicen recompensas y castigos, y deben usar ese conocimiento para elegir cursos de acción que maximicen su éxito.

### Dos Componentes Esenciales

El estudio del comportamiento adaptable busca los principios que permiten resolver este problema. Podemos descomponerlo en dos componentes fundamentales:

**1. El Problema del Conocimiento**: ¿Cómo detectar y aprender las propiedades estadísticas de la distribución de recursos relevantes desde el punto de vista biológico y psicológico? Es decir, ¿cómo aprender a predecir aquello fundamental para la supervivencia y reproducción? Este es el problema de la **asignación de crédito**: cuando un recurso aparece (o un peligro se presenta), ¿a cuál de los múltiples eventos, señales o acciones previas debe asignarse la responsabilidad? ¿Qué predice qué?

**2. El Problema de la Acción**: ¿Cómo usar eficientemente ese conocimiento para distribuir óptimamente el comportamiento en el tiempo y en el espacio? Dado que sabemos algo sobre dónde y cuándo aparecen los recursos, ¿cómo decidimos qué hacer? Este es el problema de la **elección** bajo restricciones: el tiempo es finito, los comportamientos compiten entre sí, y las decisiones tienen costos de oportunidad.

Estas dos preguntas—*¿qué predice qué?* y *¿qué hago ahora?*—organizan todo el curso.

### Dos Orígenes de Soluciones

Las soluciones a estos problemas adaptativos tienen dos orígenes temporales diferentes:

**1. Soluciones Filogenéticas (Selección Natural)**: En entornos relativamente constantes a lo largo de generaciones, la selección natural puede codificar directamente en el genoma las respuestas apropiadas. El resultado es lo que llamamos **comportamiento adaptado**: reflejos, instintos, sesgos perceptuales y atencionales que no requieren aprendizaje individual. Un ejemplo es la "impronta" en aves—los polluelos siguen al primer objeto en movimiento que ven después de nacer, típicamente su madre.

**2. Soluciones Ontogenéticas (Aprendizaje)**: En entornos variables, volátiles e inciertos—la norma para la mayoría de los organismos—la selección natural no puede anticipar todas las contingencias. En estos casos, evoluciona algo diferente: mecanismos que permiten **comportamiento adaptable**, la capacidad de ajustar el comportamiento dentro de la vida del organismo en respuesta a la experiencia. A esto le llamamos **aprendizaje**.

La teoría de la selección natural de Darwin resolvió el enigma de cómo los rasgos pueden parecer diseñados sin necesidad de un diseñador: variación, selección por consecuencias, y retención de lo exitoso. Veremos que los mecanismos del aprendizaje operan según el mismo principio abstracto—ensayo, error y selección—pero a una escala temporal ontogenética en lugar de filogenética.

### Mecanismos Reutilizables: Las "Tuercas y Tornillos"

A lo largo del curso identificaremos un conjunto pequeño de mecanismos generales—verdaderas "tuercas y tornillos" en el cajón de herramientas de la adaptación—que aparecen una y otra vez en diferentes contextos:

- **Comparación** (sucesiva vs. simultánea): Detectar diferencias entre estados del mundo
- **Reducción de error**: Ajustar predicciones cuando difieren de resultados observados
- **Exploración vs. Explotación**: El dilema entre muestrear nuevas opciones y aprovechar lo conocido
- **Sistemas de retroalimentación**: Sistemas cerrados donde la acción modifica las condiciones que la provocan
- **Descuento temporal**: Valorar más las consecuencias cercanas que las lejanas
- **Optimización bajo restricciones**: Encontrar la mejor distribución posible de comportamiento dadas las limitaciones del entorno

Estos mecanismos no son curiosidades teóricas. Son implementables, operan en robots y algoritmos de inteligencia artificial, y pueden estudiarse tanto a nivel conductual como neural.

## El Enfoque de Este Curso

### Una Perspectiva Ingenieril

Este curso adopta lo que podríamos llamar una **perspectiva ingenieril**: tratamos el comportamiento como una **solución a problemas adaptativos específicos**. Para cada fenómeno, preguntaremos no solo "¿qué hacen los organismos?" sino también:

- **¿Qué problema adaptativo están resolviendo?** (¿Por qué esto es importante para sobrevivir y reproducirse?)
- **¿Qué debería hacer un agente ideal?** (¿Cuál es la solución óptima dado el problema y las restricciones?)
- **¿Cómo lo logran?** (¿Qué algoritmos o mecanismos implementan esa solución o se aproximan a ella?)

Esta perspectiva conecta naturalmente con la distinción de niveles de análisis propuesta por David Marr (1982) y relacionada con las cuatro preguntas de Tinbergen (1963):

**Nivel Computacional (¿Por Qué?)**: ¿Qué problema está resolviendo el sistema? ¿Cuál es la lógica de la tarea? Ejemplos: maximizar la tasa de obtención de energía, minimizar incertidumbre sobre la ocurrencia de recursos, encontrar el camino más corto en un laberinto.

**Nivel Algorítmico (¿Cómo?)**: ¿Qué representaciones y procesos implementan la solución? Ejemplos: comparación sucesiva de estados ambientales, actualización de valores mediante error de predicción, elección probabilística proporcional a valores estimados.

**Nivel de Implementación (¿Con Qué?)**: ¿Qué estructuras físicas (neurales, genéticas) realizan el algoritmo? Ejemplos: neuronas dopaminérgicas, circuitos cortico-estriatales, expresión génica inducida por experiencia.

Estos niveles no compiten entre sí—son **complementarios**. Una explicación completa requiere los tres. En este curso nos enfocaremos principalmente en los niveles computacional y algorítmico, aunque haremos referencias al nivel de implementación cuando sea relevante.

### Modelos Formales como Lenguaje Natural

Los modelos matemáticos que emplearemos—ecuaciones en diferencia, funciones de probabilidad, algoritmos de optimización—no son ornamentos técnicos para impresionar. Son el **lenguaje natural** para expresar con precisión los principios del comportamiento adaptable.

Considera el **principio de refuerzo** de Skinner. La afirmación de que "el comportamiento seguido por un refuerzo incrementa su tasa de ocurrencia" no es suficientemente precisa, ni como explicación ni como guía para una intervención terapéutica. Queremos encontrar una función matemática que transforme diferentes parámetros del refuerzo—su frecuencia, probabilidad, demora—en valores de tasas de ocurrencia de la respuesta. Veremos que un modelo de refuerzo que promedia los refuerzos obtenidos proporciona una **descripción** correcta de lo observado y simultáneamente proporciona un **algoritmo/mecanismo** que explica y predice el comportamiento observado.

### Los Simuladores como Herramientas de Descubrimiento

Los modelos formales que revisaremos pueden parecer abstractos cuando se presentan solo como ecuaciones en papel. Los **simuladores interactivos** que acompañan estas notas están diseñados para transformar símbolos abstractos en comportamiento observable.

Cada simulador te permite:
- **Manipular parámetros** y observar efectos inmediatos sobre el comportamiento del sistema
- **Reproducir experimentos clásicos** con diferentes condiciones para ver qué cambia y qué permanece constante
- **Desarrollar intuición** sobre el comportamiento de sistemas complejos antes de formalizar esa intuición matemáticamente
- **Descubrir por ti mismo** relaciones que el texto describe, convirtiendo la lectura pasiva en exploración activa

Por ejemplo, en el capítulo sobre el modelo de Rescorla-Wagner, en lugar de simplemente leer sobre el fenómeno de bloqueo, podrás manipular directamente los parámetros del modelo ($\alpha$, $\beta$, intensidad de los estímulos) y observar cómo emerge el bloqueo como una consecuencia natural de la regla de aprendizaje. Esta experiencia interactiva transforma una ecuación abstracta en una intuición operativa sobre el proceso de asignación de crédito.

Los simuladores no son "extras" opcionales o meras ilustraciones—son parte integral de la estrategia pedagógica de este curso. Están organizados por tema y disponibles en:

**🔗 https://www.bouzaslab25.com/**

A lo largo de las notas encontrarás secciones claramente marcadas que te dirigen a simuladores específicos, con sugerencias sobre qué explorar y qué preguntas hacerte. Usa estas herramientas. Experimenta. El aprendizaje más profundo ocurre cuando descubres, no solo cuando lees.

## Mapa del Curso

El curso está organizado en bloques temáticos que siguen la lógica del problema adaptativo que planteamos al inicio. Cada bloque añade una capacidad funcional a nuestro "agente adaptativo", construyendo progresivamente desde mecanismos simples hasta sistemas complejos de toma de decisiones:

### **Bloque 0: Fundamentos Conceptuales** (Capítulos 0-3)
Establecemos el marco teórico general: niveles de explicación, el problema de la adaptabilidad, y la teoría de la selección natural como primera solución. Aquí definimos qué significa "adaptarse" y por qué necesitamos modelos mecanicistas en lugar de solo descripciones empíricas.

### **Bloque I: Mecanismos Sin Integración de Historia** (Capítulos 4-5)
Estudiamos dos mecanismos fundamentales que permiten adaptación en tiempo real sin requerir integración de experiencias pasadas: **ascenso de colina** (comparación sucesiva) y **sistemas de retroalimentación** (comparación simultánea). Estos son los "nuts and bolts" más básicos. Nuestro agente aprende a navegar y a mantener condiciones internas estables, pero vive completamente en el "ahora".

### **Bloque II: El Problema del Conocimiento - Asignación de Crédito** (Capítulos 6-10)
Abordamos el problema central: cuanestudiamosdo un reforzador aparece, ¿a qué se le asigna el crédito? Primero los límites sensoriales (psicofísica y teoría de detección de señales) que determinan qué puede detectar el agente. Luego revisamos modelos clásicos de aprendizaje asociativo (Rescorla-Wagner) y sus extensiones contemporáneas, incluyendo modelos basados en teoría de la información y filtros bayesianos. Nuestro agente deja de ser puramente reactivo y aprende a predecir el futuro.

### **Bloque III: El Problema de la Acción - Elección y Optimización** (Capítulos 11-15)
Dado que hemos aprendido qué predice qué, ¿cómo distribuimos nuestro comportamiento? Estudiamos la ley del efecto, programas de refuerzo, la ley de igualación, y culminamos con modelos de optimización en equilibrio que integran economía conductual. Nuestro agente ahora conecta su conocimiento con la acción y aprende a elegir racionalmente.

### **Bloque IV: Aprendizaje Secuencial** (Segundo Semestre)
Extendemos el análisis a secuencias de acciones donde el reforzador aparece al final (problema de asignación de crédito temporal). Introducimos algoritmos de aprendizaje por refuerzo: diferencias temporales, Q-learning, Actor-Crítico. Nuestro agente aprende a planificar secuencias de acciones hacia metas distantes.

### **Bloque V: Incertidumbre y Estados Ocultos** (Segundo Semestre)
Finalmente, relajamos el supuesto de que el agente siempre sabe en qué estado del mundo se encuentra. Estudiamos entornos volátiles, POMDPs, y modelos bayesianos avanzados. Nuestro agente aprende a razonar bajo incertidumbre profunda sobre el estado del mundo.

## Cómo Usar Estas Notas

### Para el Estudiante

Estas notas están diseñadas para **lectura activa**, no pasiva. Algunas sugerencias:

1. **Lee con lápiz y papel a la mano**. Cuando aparece una ecuación, no la saltes—desarróllala. Verifica las derivaciones. Sustituye números concretos y calcula resultados. Por ejemplo, si el texto presenta la ecuación de Rescorla-Wagner, calcula manualmente los primeros cinco ensayos de un protocolo de condicionamiento antes de ver el resultado en el simulador.

2. **Usa los simuladores inmediatamente**. Cuando un capítulo menciona un simulador, ve a explorarlo *antes* de seguir leyendo. Primero juega, luego formaliza. Manipula los parámetros sin restricciones. Prueba valores extremos. Rompe el modelo intencionalmente para entender sus límites. Solo después regresa al texto para consolidar la formalización matemática de lo que descubriste experimentalmente.

3. **Sé paciente con las matemáticas**. Algunas ecuaciones parecerán opacas al inicio. Regresa a ellas después de explorar el simulador. La intuición precede a la formalización. Si una ecuación no tiene sentido la primera vez, márca la página y continúa. Frecuentemente, un ejemplo posterior o un simulador específico iluminará retrospectivamente lo que parecía oscuro.

4. **Conecta con tus experiencias**. Cada mecanismo que estudiamos opera también en tu comportamiento cotidiano. Cuando leas sobre descuento temporal, piensa en tu última procrastinación. Cuando estudies ascenso de colina, observa cómo buscas el punto óptimo al ajustar la temperatura del agua en la ducha. Estas conexiones personales anclan la teoría abstracta en la experiencia vivida.

### Para el Instructor

Estas notas pueden usarse de múltiples formas:

- **Como texto principal** en un curso de dos semestres sobre aprendizaje y comportamiento adaptable. Los primeros tres bloques cubren típicamente el primer semestre; los bloques IV y V, el segundo.

- **Como complemento** a un texto tradicional, añadiendo la perspectiva formal y de optimización que esos textos omiten. Por ejemplo, si usa un texto clásico organizado por protocolos (condicionamiento clásico, operante, etc.), puede asignar los capítulos correspondientes de estas notas como lecturas complementarias que proporcionan la formalización matemática y la perspectiva integradora.

- **Como recurso para temas específicos** (por ejemplo, solo los capítulos sobre aprendizaje por refuerzo, o solo los de modelos de optimización). Cada bloque es relativamente autocontenido, aunque se beneficia de la lectura secuencial.

Los simuladores permiten clases invertidas: los estudiantes exploran antes de clase, y el tiempo presencial se dedica a discusión, resolución de problemas, y profundización conceptual. Una estrategia efectiva es asignar la lectura de un capítulo más la exploración libre del simulador correspondiente *antes* de clase, y usar el tiempo presencial para: (1) resolver dudas sobre la formalización matemática, (2) discutir las implicaciones teóricas de lo observado en el simulador, y (3) conectar el mecanismo con fenómenos reales en neurociencias o aplicaciones.

## Un Argumento Final

Muchos colegas me han dicho que es imposible enseñar estos temas—aprendizaje por refuerzo, modelos bayesianos, teoría de la información—a nivel introductorio. Que los estudiantes de licenciatura no tienen las herramientas matemáticas. Que es mejor mantener el enfoque tradicional, descriptivo, organizado por protocolos.

Discrepo respetuosamente.

Los estudiantes de hoy crecieron con algoritmos de recomendación, navegación GPS, y juegos con IA. Tienen una intuición operativa sobre aprendizaje de máquinas que generaciones previas no tenían. Lo que les falta no es capacidad—es un puente entre esa intuición informal y los principios formales.

Los simuladores interactivos, los ejemplos concretos, y la conexión explícita con aplicaciones contemporáneas construyen ese puente. Las matemáticas no necesitan ser una barrera; pueden ser una revelación. Cuando un estudiante manipula los parámetros del modelo de Rescorla-Wagner y observa cómo emerge el bloqueo, la ecuación deja de ser un símbolo opaco y se convierte en una descripción precisa de un proceso observable. Cuando experimenta con diferentes programas de refuerzo en el simulador y luego ve cómo la ley de igualación predice cuantitativamente la distribución de respuestas, las matemáticas se revelan como el lenguaje natural para expresar regularidades empíricas.

Más importante, privar a los estudiantes de esta perspectiva integradora—mantenerlos en el mundo de fenómenos desconectados del siglo XX—es hacerles un flaco favor. El comportamiento adaptable no es un museo de curiosidades históricas. Es un campo vivo con aplicaciones en robótica, neurociencias computacionales, economía conductual, y políticas públicas. Los mismos principios que explicamos aquí operan en algoritmos que determinan qué videos te recomienda YouTube, en modelos de neurociencias que estudian adicción, en políticas de salud pública que buscan modificar comportamientos de riesgo.

Estas notas son un experimento pedagógico. No tienen el pulido de un libro de editorial, ni las restricciones de extensión o contenido que imponen los mercados académicos. Son un recurso abierto, en evolución, diseñado para estudiantes que no le temen a los formalismos matemáticos y que merecen algo mejor que listas de fenómenos inconexos.

Si funcionan para ti—como estudiante o instructor—compártelas. Si encuentras errores, omisiones, o secciones poco claras, comunícamelo. Este es un proyecto colaborativo en el mejor espíritu de la ciencia abierta.

---

**Bienvenidos al taller. Empecemos a construir.**
