# Introducción al Curso

> "Lo que no puedo crear, no lo entiendo." — Richard Feynman

## Un Problema de Diseño

Cada mañana, antes de comenzar su día, Wall-E hace lo mismo: conecta su panel solar y recarga su batería. Inmediatamente, inicia una rutina de búsqueda: navega por un terreno accidentado, identifica objetos de interés entre la basura y regresa a su base antes de que se agote su energía. después se da tiempo de ver una película musical.  Este ritual aparentemente simple revela algo profundo. Wall-E enfrenta el problema fundamental que comparten todos los agentes adaptativos, desde bacterias hasta algoritmos de inteligencia artificial: cómo distribuir el comportamiento en el tiempo y en el espacio para maximizar la obtención de recursos necesarios para sobrevivir, funcionar o cumplir sus objetivos.

Ahora, imagina que te encargan diseñar un robot explorador similar a Wall-E para un planeta desconocido. Tu misión es construir un agente autónomo capaz de  localizar recursos dispersos en un terreno accidentado, evitar peligros y encontrar fuentes de energía que le permitan recargar y gestionar su limitada reserva energética. Tienes un presupuesto limitado: sensores imperfectos que confunden el ruido con señales, un procesador con memoria finita y una batería que se agota con cada movimiento. 

Para que el robot sobreviva, debes programar soluciones a cuatro problemas fundamentales:

1. **Sensores** que transformen energía física en señales que permitan identificar los recursos buscados en medio del ruido ambiental.  Wall-E usa sus cámaras para distinguir objetos compactables de obstáculos peligrosos.

2. **Navegación** que le permita moverse hacia concentraciones de recursos detectados a distancia. Cuando Wall-E detecta un objeto de interés, no se mueve aleatoriamente sino que se dirige directamente hacia él.

3. **Aprendizaje predictivo** que le permita anticipar dónde aparecerán recursos basándose en señales previas. Si cierta formación rocosa predice agua cercana, o si cierto tipo de escombros suele contener objetos valiosos, el robot debe aprender estas regularidades. Wall-E aprende que ciertos contenedores suelen tener objetos brillantes que le interesan.

4. **Sistemas de elección** que le permitan decidir racionalmente entre opciones cuando los recursos son múltiples y los comportamientos compiten entre sí. Wall-E debe decidir constantemente: ¿sigo compactando basura o busco un lugar seguro antes del anochecer? ¿Persigo ese objeto brillante interesante o regreso a cargar energía?

Este es exactamente el problema que enfrentan todos los organismos vivos y que la evolución ha resuelto. Una rata buscando alimento, una bacteria navegando hacia glucosa, un estudiante decidiendo cuánto tiempo dedicar a cada materia: **cómo distribuir su comportamiento en el tiempo y en el espacio para maximizar la obtención de recursos necesarios para sobrevivir, reproducirse o cumplir sus objetivos**. Este curso estudia las soluciones biológicas y computacionales a este problema.

## El Enfoque de la Ingeniería Inversa

La estrategia pedagógica tradicional para enseñar aprendizaje y comportamiento adaptable, reflejada en la organización típica de los libros de texto, presenta casi exclusivamente las principales regularidades empíricas derivadas de más de 100 años de investigación, organizadas alrededor de protocolos experimentales específicos: condicionamiento clásico (Pavlov), condicionamiento operante (Skinner), programas de refuerzo, y quizás, si tuvo suerte, una clase sobre el modelo de Rescorla-Wagner y el principio de igualación de Herrnstein. Si bien este enfoque tiene valor histórico y permite apreciar la riqueza empírica del campo, puede dejar frecuentemente al estudiante con la impresión de que este es un área de conocimiento estática, fragmentada y predominantemente de interés histórico, llena de hallazgos aislados y con escasa coherencia conceptual.

Los estudiantes terminan ese curso sin una visión coherente de los principios que unifican estos fenómenos, ni una comprensión de por qué este campo sigue siendo relevante en el siglo XXI. Los hallazgos aparecen desconectados entre sí y, peor aún, desconectados de desarrollos contemporáneos en neurociencia computacional, inteligencia artificial, economía conductual y teoría de la decisión.

En este curso adoptaremos una estrategia diferente de **ingeniería inversa**. Asumiremos que el comportamiento observado es la solución a un problema de adaptación, y nuestro trabajo es descubrir el algoritmo que lo genera. Para cada fenómeno, preguntaremos no solo "¿qué hacen los organismos?" sino también:

¿Qué problema adaptativo están resolviendo? (¿Por qué esto es importante para sobrevivir y reproducirse?)

¿Qué debería hacer un agente ideal? (¿Cuál es la solución óptima dado el problema y las restricciones?)

¿Cómo lo logran? (¿Qué algoritmos o mecanismos implementan esa solución o se aproximan a ella?) 

## El Enfoque de Este Libro

### Una Perspectiva Ingenieril

Este curso adopta lo que podríamos llamar una perspectiva ingenieril: tratamos el comportamiento como una solución a problemas adaptativos específicos. Para cada fenómeno, preguntaremos no solo "¿qué hacen los organismos?" sino también:

¿Qué problema adaptativo están resolviendo? (¿Por qué esto es importante para sobrevivir y reproducirse?)

¿Qué debería hacer un agente ideal? (¿Cuál es la solución óptima dado el problema y las restricciones?)

¿Cómo lo logran? (¿Qué algoritmos o mecanismos implementan esa solución o se aproximan a ella?)

## Mapa del Libro

El libro está organizado en bloques temáticos que siguen la lógica del problema adaptativo que planteamos al inicio. Cada bloque añade una capacidad funcional a nuestro "agente adaptativo", construyendo progresivamente desde mecanismos simples hasta sistemas complejos de toma de decisiones:

### Bloque 0: Fundamentos Conceptuales (Capítulos 0-3)

Establecemos el marco teórico general: niveles de explicación, el problema de la adaptabilidad, y la teoría de la selección natural como primera solución. Aquí definimos qué significa "adaptarse" y por qué necesitamos modelos mecanicistas en lugar de solo descripciones empíricas.

### Bloque I: Mecanismos Sin Integración de Historia (Capítulos 4-5)

Estudiamos dos mecanismos fundamentales que permiten adaptación en tiempo real sin requerir integración de experiencias pasadas: ascenso de colina (comparación sucesiva) y sistemas de retroalimentación (comparación simultánea). Estos son las "tuercas y tornillos" más básicas. Nuestro agente aprende a navegar y a mantener condiciones internas estables, pero vive completamente en el "ahora".

### Bloque II: El Problema del Conocimiento - Asignación de Crédito (Capítulos 6-10)

Abordamos el problema central: cuando un reforzador aparece, ¿Que lo causo?, ¿a qué se le asigna el crédito? Primero revisamos modelos clásicos de aprendizaje asociativo y sus extensiones contemporáneas, incluyendo modelos basados en teoría de la información y filtros Bayesianos. Nuestro agente deja de ser puramente reactivo y aprende a predecir el futuro.

### Bloque III: El Problema de la Acción - Elección y Optimización (Capítulos 11-15)

Dado que hemos aprendido qué predice qué, ¿cómo distribuimos nuestro comportamiento? Estudiamos la ley del efecto, programas de refuerzo, la ley de igualación, y culminamos con modelos de optimización en equilibrio que integran economía conductual. Nuestro agente ahora conecta su conocimiento con la acción y aprende a elegir racionalmente.

### Bloque IV: Aprendizaje Secuencial

Extendemos el análisis a secuencias de acciones donde el reforzador aparece al final (problema de asignación de crédito temporal). Introducimos algoritmos de aprendizaje por refuerzo: diferencias temporales, Q-learning, Actor-Crítico. Nuestro agente aprende a planificar secuencias de acciones hacia metas distantes.

### Bloque V: Incertidumbre y Estados Ocultos

Relajamos el supuesto de que el agente siempre sabe en qué estado del mundo se encuentra. Estudiamos entornos volátiles y modelos Bayesianos avanzados. Nuestro agente aprende a razonar bajo incertidumbre profunda sobre el estado del mundo.

### Bloque VI: Estructura de Preferencias

Finalmente, toda la maquinaria estudiada en los bloques anteriores tiene sentido solo si, en el entorno del agente (biológico o artificial), se encuentran sucesos con un valor que hace adpatativo predecirlos y organizar el comportamiento para maximizar su ocurrencia. Estudiaremos los determinantes de la asignación de valor,entre otros su probabilidad y demora, 

**1. El Problema del Conocimiento (Predicción):** ¿Cómo detectar y aprender las propiedades estadísticas de la distribución de recursos relevantes desde el punto de vista biológico y psicológico? Es decir, ¿cómo aprender a predecir aquello fundamental para la supervivencia y reproducción? Este es el problema de la **asignación de crédito**: cuando se encuentra un suceso biológicamente importante, positivo o negativo, ¿a cuál de los múltiples eventos, señales o acciones previas debe asignarse la responsabilidad de su presencia? ¿Qué predice qué?

**2. El Problema de la Acción:** ¿Cómo usar eficientemente ese conocimiento para distribuir óptimamente el comportamiento en el tiempo y en el espacio? Dado que sabemos algo sobre dónde y cuándo aparecen los sucesos biológicamente importantes, ¿cómo decidimos qué hacer? Este es el problema de la elección bajo restricciones: el tiempo es finito, los comportamientos compiten entre sí, y las decisiones tienen costos de oportunidad.

Estas dos preguntas (¿qué predice qué? y ¿qué hago ahora?) organizan todo el curso.

## Dos Orígenes de Soluciones

Las soluciones a estos problemas adaptativos tienen dos orígenes temporales diferentes:

**1. Soluciones Filogenéticas (Selección Natural):** En entornos relativamente constantes a lo largo de generaciones, la selección natural puede codificar directamente en el genoma las respuestas apropiadas. El resultado es lo que llamamos comportamiento adaptado: reflejos, instintos, sesgos perceptuales y atencionales que no requieren aprendizaje individual. Un ejemplo es la impronta en aves: los patitos siguen al primer objeto en movimiento que ven después de nacer, típicamente su madre.

**2. Soluciones Ontogenéticas (Aprendizaje):** En entornos variables, volátiles e inciertos (la norma para la mayoría de los organismos), la selección natural no puede anticipar todas las contingencias. En estos casos, evoluciona algo diferente: mecanismos que permiten comportamiento adaptable, la capacidad de ajustar el comportamiento a la estructura estadística de los sucesos biológicamente importantes, dentro de la vida del organismo. A esto le llamamos aprendizaje.

## Mecanismos Reutilizables: Las "Tuercas y Tornillos"

A lo largo del libro identificaremos un conjunto pequeño de mecanismos generales (verdaderas "tuercas y tornillos" en el cajón de herramientas de la adaptación) que aparecen una y otra vez en diferentes contextos. A estos mecanismos los llamaremos algoritmos:

**Algoritmos de comparación** (sucesiva vs. simultánea): Detectar diferencias entre estados del mundo.

**Algoritmos de reducción de error:** Ajustar predicciones cuando difieren de resultados observados.

**Algoritmos para la exploración vs. explotación:** Soluciones al dilema entre muestrear nuevas opciones y aprovechar lo conocido.

**Algoritmos de sistemas de retroalimentación:** Sistemas cerrados donde la acción modifica las condiciones que la provocan.

**Algoritmos para la optimización bajo restricciones:** Encontrar la mejor distribución posible de comportamiento dadas las limitaciones del entorno.

## Cómo Usar Estas Notas

### Para el Estudiante: Estrategias de Lectura Activa

Este material exige una lectura activa. Para maximizar el aprendizaje del material del libro, te sugerimos la siguiente estrategia: 

**Antes de cada capítulo:** Lee el título y el primer párrafo. Formula una pregunta concreta que esperas que el capítulo responda. Por ejemplo, antes del capítulo sobre Rescorla-Wagner, pregúntate: "¿Cómo aprende un organismo qué señales predicen recompensas y cuáles son irrelevantes?" Esta pregunta explícita activará tu atención selectiva durante la lectura.

**Durante la lectura:** Lee con lápiz y papel a la mano. Cuando aparece una ecuación, desarróllala. Verifica las derivaciones. Sustituye números concretos y calcula resultados. Por ejemplo, si el texto presenta la ecuación de Rescorla-Wagner, calcula manualmente los primeros cinco ensayos de un protocolo de condicionamiento antes de ver el resultado en el simulador. Esta aparente "pérdida de tiempo" es en realidad la forma más eficiente de aprendizaje profundo. La mayoría de las confusiones matemáticas se disuelven cuando calculas casos específicos con números reales.

**Usa los simuladores inmediatamente y sin restricciones.** Cuando un capítulo menciona un simulador, ve a explorarlo antes de seguir leyendo. No esperes a "terminar de leer" para experimentar. La secuencia óptima es: lee la presentación del problema adaptativo, explora el simulador libremente durante 10-15 minutos, regresa al texto para la formalización matemática, vuelve al simulador para validar tu comprensión con casos extremos.

En el simulador, prueba valores extremos intencionalmente. Si hay un parámetro α (tasa de aprendizaje), no solo uses α=0.3. Prueba α=0.01 (aprendizaje extremadamente lento), α=0.99 (aprendizaje casi instantáneo), α=1.0 (caso límite). Rompe el modelo intencionalmente para entender sus límites. ¿Qué pasa si todos los parámetros son cero? ¿Y si todos son máximos? Solo después de romperlo y ver qué falla, regresa al texto para consolidar por qué esas condiciones son problemáticas.

**Sé paciente con las matemáticas.** Algunas ecuaciones parecerán opacas al inicio. Esta incomodidad es normal y esperada. Regresa a ellas después de explorar el simulador. La intuición precede a la formalización. Si una ecuación no tiene sentido la primera vez, marca la página y continúa. Frecuentemente, un ejemplo posterior o un simulador específico iluminará retrospectivamente lo que parecía oscuro. Si después de ver el simulador y regresar al texto una ecuación sigue siendo opaca, ese es el momento de pedir ayuda, no antes.

**Conecta con tus experiencias.** Cada mecanismo que estudiamos opera también en tu comportamiento cotidiano. Esta no es una sugerencia decorativa sino una estrategia pedagógica fundamental.  Cuando estudies ascenso de colina, observa durante tu próxima ducha cómo buscas el punto óptimo al ajustar la temperatura del agua: ¿haces cambios grandes o pequeños? ¿Cómo decides cuándo has encontrado el óptimo? Estas conexiones personales anclan la teoría abstracta en la experiencia vivida, transformándola de "contenido para memorizar" a "herramienta para comprender tu propio comportamiento".

**Organiza revisiones activas periódicas.** Después de completar tres capítulos, antes de continuar, dedica una sesión a responder: ¿Qué problema adaptativo resuelve cada mecanismo? ¿Qué tienen en común los tres algoritmos? ¿En qué se diferencian? Si tuvieras que diseñar un robot con esas capacidades, ¿en qué orden las implementarías y por qué? Esta metacognición consolida el aprendizaje más efectivamente que releer pasivamente.

### Para el Instructor

Estas notas permiten múltiples configuraciones pedagógicas. Una que puede ser experimentada es el modelo de clase invertida. Asigna la lectura de un capítulo más la exploración libre del simulador correspondiente como tarea previa a clase. Usa el tiempo presencial para resolver dudas sobre sobre la formulación matemática, discutir las implicaciones teóricas de lo observada en el simulador, conectar el mecanismo con fenómenos reales o aplicaciones.

Los simuladores y notebooks de Google Colab permiten extender el análisis más allá del libro. Asigna proyectos donde los estudiantes modifiquen el código para responder preguntas originales.

Cada bloque temático es relativamente autocontenido, aunque se beneficia de la lectura secuencial. Si usas este libro como complemento a un texto tradicional organizado por protocolos, puedes asignar capítulos específicos como lecturas paralelas que proporcionan la formalización matemática que el texto principal omite.

## Un Argumento Final

Muchos colegas me han dicho que los modelos formales como -aprendizaje por refuerzo, modelos Bayesianos, teoría de la información) son demasiado complejos para un curso de licenciatura de Psicología. Se argumenta que es preferible mantenerse en el terreno descriptivo.  

Este libro parte de una premisa distinta.

Los estudiantes de hoy crecieron con algoritmos de recomendación, navegación GPS y juegos con IA. Tienen una intuición operativa sobre aprendizaje de máquinas que generaciones previas no tenían. Lo que les falta no es capacidad, es un puente entre esa intuición informal y los principios formales.

Los simuladores interactivos, los ejemplos concretos y una narrativa de diseño construyen ese puente. Las matemáticas dejan de ser un obstáculo y se convierten en lenguaje natural para expresar regularidades empíricas, que abre nuevas puertas de comprensión.
Más importante, privar a los estudiantes de esta perspectiva integradora (mantenerlos en el mundo de fenómenos desconectados del siglo XX) es hacerles un flaco favor. El comportamiento adaptable no es un museo de curiosidades históricas. Es un campo vivo con aplicaciones en robótica, neurociencias computacionales, economía conductual y políticas públicas. Los mismos principios que explicamos aquí operan en algoritmos que determinan qué videos te recomienda YouTube, en modelos de neurociencias que estudian adicción, en políticas de salud pública que buscan modificar comportamientos de riesgo.

Estas notas son un experimento pedagógico. No tienen el pulido de un libro de editorial, ni las restricciones de extensión o contenido que imponen los mercados académicos. Son un recurso abierto, en evolución, diseñado para estudiantes que no le temen a los formalismos matemáticos y que merecen algo mejor que listas de fenómenos inconexos.

Si funcionan para ti (como estudiante o instructor) compártelas. Si encuentras errores, omisiones o secciones poco claras, comunícamelo. Este es un proyecto colaborativo en el mejor espíritu de la ciencia abierta.
