# # Introducción al Curso {.unnumbered}

> *"Lo que no puedo crear, no lo entiendo."* — Richard Feynman

## Un Problema de Diseño

Imagina que te encargan diseñar un robot explorador para un planeta desconocido. La tarea del robot es localizar recursos dispersos en un terreno accidentado, evitar peligros, y encontrar fuentes de energía que le permitan recargar y gestionar su limitada energía. Para ello, cuentas con sensores imperfectos (cámaras con ruido, detectores químicos con umbrales de sensibilidad), un procesador con capacidad finita, y restricciones severas de tiempo y energía. ¿Qué capacidades mínimas debe tener este robot para sobrevivir?

Necesitará, al menos:
- **Sensores** que transformen energía física en señales procesables, distinguiendo información útil del ruido ambiental.
- **Navegación** que le permita moverse hacia concentraciones de recursos detectadas a distancia.
- **Aprendizaje predictivo** que le permita anticipar dónde aparecerán recursos basándose en señales previas (si cierta formación rocosa predice agua cercana).
- **Sistemas de elección** que le permitan decidir racionalmente entre opciones cuando los recursos son múltiples y los comportamientos compiten entre sí.

Este es exactamente el problema que enfrentan todos los organismos vivos. Una rata buscando alimento, una bacteria navegando gradientes químicos, un estudiante decidiendo cuánto tiempo dedicar a cada materia, un algoritmo de ajedrez evaluando jugadas—todos enfrentan variantes del mismo desafío fundamental: **cómo distribuir su comportamiento en el tiempo y en el espacio para maximizar la obtención de recursos necesarios para sobrevivir, reproducirse, o cumplir sus objetivos**.

Este curso estudia las soluciones biológicas y computacionales a este problema. Pero antes de construir ese robot—o de entender cómo funcionan los organismos—debemos confrontar un problema pedagógico previo.

## El Problema con la Enseñanza Tradicional

La estrategia pedagógica tradicional para enseñar aprendizaje y comportamiento adaptable, reflejada en la organización típica de los libros de texto, presenta casi exclusivamente las principales regularidades empíricas derivadas de más de 100 años de investigación, organizadas alrededor de protocolos experimentales específicos: condicionamiento clásico (Pavlov), condicionamiento operante (Skinner), programas de refuerzo, y quizás, si tuvo suerte, una clase sobre el modelo de Rescorla-Wagner y el principio de igualación de Herrnstein. Si bien este enfoque tiene valor histórico y permite apreciar la riqueza empírica del campo, puede dejar frecuentemente al estudiante con la impresión de que este es un área de conocimiento estática, fragmentada y predominantemente de interés histórico, llena de hallazgos aislados y con escasa coherencia conceptual.

Los estudiantes terminan ese curso sin una visión coherente de los principios que unifican estos fenómenos, ni una comprensión de por qué este campo sigue siendo relevante en el siglo XXI. Los hallazgos aparecen desconectados entre sí y, peor aún, desconectados de desarrollos contemporáneos en neurociencias, inteligencia artificial, economía conductual y teoría de la decisión.

Este curso adopta una estrategia diferente.

## Un Problema Adaptativo Fundamental

En el centro de este curso está el problema biológico fundamental que mencionamos al inicio: **cómo distribuir el comportamiento en el tiempo y en el espacio para maximizar la obtención de recursos necesarios para sobrevivir y reproducirse**. Los agentes biológicos y no biológicos deben Deben aprender qué aspectos de su entorno predicen recompensas y castigos, y deben usar ese conocimiento para elegir cursos de acción que maximicen su éxito.

### Dos Componentes Esenciales

El estudio del comportamiento adaptable busca los principios que permiten resolver este problema. Podemos descomponerlo en dos componentes fundamentales:

**1. El Problema del Conocimiento**: ¿Cómo detectar y aprender las propiedades estadísticas de la distribución de recursos relevantes desde el punto de vista biológico y psicológico? Es decir, ¿cómo aprender a predecir aquello fundamental para la supervivencia y reproducción? Este es el problema de la **asignación de crédito**: cuando un recurso aparece (o un peligro se presenta), ¿a cuál de los múltiples eventos, señales o acciones previas debe asignarse la responsabilidad? ¿Qué predice qué?

**2. El Problema de la Acción**: ¿Cómo usar eficientemente ese conocimiento para distribuir óptimamente el comportamiento en el tiempo y en el espacio? Dado que sabemos algo sobre dónde y cuándo aparecen los recursos, ¿cómo decidimos qué hacer? Este es el problema de la **elección** bajo restricciones: el tiempo es finito, los comportamientos compiten entre sí, y las decisiones tienen costos de oportunidad.

Estas dos preguntas—*¿qué predice qué?* y *¿qué hago ahora?*—organizan todo el curso.

### Dos Orígenes de Soluciones

Las soluciones a estos problemas adaptativos tienen dos orígenes temporales diferentes:

**1. Soluciones Filogenéticas (Selección Natural)**: En entornos relativamente constantes a lo largo de generaciones, la selección natural puede codificar directamente en el genoma las respuestas apropiadas. El resultado es lo que llamamos **comportamiento adaptado**: reflejos, instintos, sesgos perceptuales y atencionales que no requieren aprendizaje individual. Un ejemplo es la "impronta" en aves—los patitos siguen al primer objeto en movimiento que ven después de nacer, típicamente su madre.

**2. Soluciones Ontogenéticas (Aprendizaje)**: En entornos variables, volátiles e inciertos—la norma para la mayoría de los organismos—la selección natural no puede anticipar todas las contingencias. En estos casos, evoluciona algo diferente: mecanismos que permiten **comportamiento adaptable**, la capacidad de ajustar el comportamiento a la estructura estadística de los suceso biológicamente importantes, dentro de la vida del organismo. A esto le llamamos **aprendizaje**.

### Mecanismos Reutilizables: Las "Tuercas y Tornillos"

A lo largo del curso identificaremos un conjunto pequeño de mecanismos generales—verdaderas "tuercas y tornillos" en el cajón de herramientas de la adaptación—que aparecen una y otra vez en diferentes contextos. A estos mecanismos los llamaremos algoritmos:

- **Algoritmos de comparación** (sucesiva vs. simultánea): Detectar diferencias entre estados del mundo
- **Algoritmos de reducción de error**: Ajustar predicciones cuando difieren de resultados observados
- **Algoritmos para la Exploración vs. Explotación**: El dilema entre muestrear nuevas opciones y aprovechar lo conocido
- **Algoritmos de sistemas de retroalimentación**: Sistemas cerrados donde la acción modifica las condiciones que la provocan
- **Algoritmos para la optimización bajo restricciones**: Encontrar la mejor distribución posible de comportamiento dadas las limitaciones del entorno

Estos mecanismos/algoritmos son implementados tanto en agentes no biológicos (robots), como en agentes biológicos (sean unicelulares o humanos), y pueden estudiarse tanto a nivel conductual como neuronal.

## El Enfoque de Este Libro

### Una Perspectiva Ingenieril

Este curso adopta lo que podríamos llamar una **perspectiva ingenieril**: tratamos el comportamiento como una **solución a problemas adaptativos específicos**. Para cada fenómeno, preguntaremos no solo "¿qué hacen los organismos?" sino también:

- **¿Qué problema adaptativo están resolviendo?** (¿Por qué esto es importante para sobrevivir y reproducirse?)
- **¿Qué debería hacer un agente ideal?** (¿Cuál es la solución óptima dado el problema y las restricciones?)
- **¿Cómo lo logran?** (¿Qué algoritmos o mecanismos implementan esa solución o se aproximan a ella?)

## Mapa del Curso

El libro está organizado en bloques temáticos que siguen la lógica del problema adaptativo que planteamos al inicio. Cada bloque añade una capacidad funcional a nuestro "agente adaptativo", construyendo progresivamente desde mecanismos simples hasta sistemas complejos de toma de decisiones:

### **Bloque 0: Fundamentos Conceptuales** (Capítulos 0-3)
Establecemos el marco teórico general: niveles de explicación, el problema de la adaptabilidad, y la teoría de la selección natural como primera solución. Aquí definimos qué significa "adaptarse" y por qué necesitamos modelos mecanicistas en lugar de solo descripciones empíricas.

### **Bloque I: Mecanismos Sin Integración de Historia** (Capítulos 4-5)
Estudiamos dos mecanismos fundamentales que permiten adaptación en tiempo real sin requerir integración de experiencias pasadas: **ascenso de colina** (comparación sucesiva) y **sistemas de retroalimentación** (comparación simultánea). Estos son las "tuercas y tornillos" más básicas. Nuestro agente aprende a navegar y a mantener condiciones internas estables, pero vive completamente en el "ahora".

### **Bloque II: El Problema del Conocimiento - Asignación de Crédito** (Capítulos 6-10)
Abordamos el problema central: cuando un reforzador aparece, ¿a qué se le asigna el crédito?.  Primero revisamos modelos clásicos de aprendizaje asociativo (Rescorla-Wagner) y sus extensiones contemporáneas, incluyendo modelos basados en teoría de la información y filtros Bayesianos. Nuestro agente deja de ser puramente reactivo y aprende a predecir el futuro.

### **Bloque III: El Problema de la Acción - Elección y Optimización** (Capítulos 11-15)
Dado que hemos aprendido qué predice qué, ¿cómo distribuimos nuestro comportamiento? Estudiamos la ley del efecto, programas de refuerzo, la ley de igualación, y culminamos con modelos de optimización en equilibrio que integran economía conductual. Nuestro agente ahora conecta su conocimiento con la acción y aprende a elegir racionalmente.

### **Bloque IV: Aprendizaje Secuencial** 
Extendemos el análisis a secuencias de acciones donde el reforzador aparece al final (problema de asignación de crédito temporal). Introducimos algoritmos de aprendizaje por refuerzo: diferencias temporales, Q-learning, Actor-Crítico. Nuestro agente aprende a planificar secuencias de acciones hacia metas distantes.

### **Bloque V: Incertidumbre y Estados Ocultos** 
Finalmente, relajamos el supuesto de que el agente siempre sabe en qué estado del mundo se encuentra. Estudiamos entornos volátiles, y modelos Bayesianos avanzados. Nuestro agente aprende a razonar bajo incertidumbre profunda sobre el estado del mundo.

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

