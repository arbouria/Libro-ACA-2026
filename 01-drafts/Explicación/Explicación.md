# Modelos y Explicación: El Mapa del Ingeniero
*"El mapa no es el territorio."* — Alfred Korzybski
Cuando observamos a un organismo comportarse —ya sea una rata presionando una palanca, un humano eligiendo pareja o nuestro robot **Wall-E** buscando baterías— nos enfrentamos a una complejidad abrumadora. Hay millones de neuronas disparando, hormonas fluyendo y una historia de vida única e irrepetible.
Si intentáramos describir *todo* lo que pasa, acabaríamos con un mapa tan grande y detallado como la realidad misma, lo cual sería inútil.
Para hacer ciencia del comportamiento, necesitamos simplificar. Necesitamos construir **Modelos**. En este capítulo, definiremos las "reglas del juego" de este curso: no vamos a memorizar listas de hechos, vamos a construir modelos para entender la maquinaria del comportamiento.
# 1\. ¿Qué es un Modelo? (Y por qué no buscamos "Leyes")
En la física clásica, Newton buscaba "Leyes Universales" (como $F=ma$). Durante mucho tiempo, la psicología intentó imitar esto, buscando la "Ley del Efecto" o la "Ley del Reflejo" como verdades absolutas escritas en piedra.
Hoy, nuestro enfoque es más pragmático, más cercano a la ingeniería.
Un **Modelo** no es la realidad; es una **representación simplificada** de la realidad que nos sirve para responder una pregunta específica.
* Un mapa del metro de la CDMX es un modelo. No muestra las tuberías de drenaje ni la profundidad del túnel. ¿Es falso? No. Es **útil** para saber cómo llegar de Copilco a Universidad.
* En este curso, nuestras ecuaciones (como la de Rescorla-Wagner) son mapas del metro. No capturan toda la complejidad de la neurobiología, pero nos dicen cómo llegar del estado "Ignorancia" al estado "Aprendizaje".

⠀La Estrategia del "Como Si"
A veces, los modelos suenan extraños: "Asumiremos que el organismo calcula la probabilidad futura...".
Un estudiante podría objetar: "¡Pero profe, mi perro no sabe cálculo!".
La respuesta es: El modelo funciona como si el perro supiera cálculo. Si el modelo predice correctamente que el perro correrá cuando suene la campana, el modelo es bueno, aunque el perro no sepa matemáticas.
# 2\. Los Tres Niveles de Marr: La Jerarquía de la Explicación
Para entender cualquier sistema complejo (un cerebro, una computadora o un termostato), el neurocientífico **David Marr** propuso que debemos responder tres preguntas distintas. Confundir estas preguntas es la causa principal de los debates estériles en psicología.
Imaginemos que queremos entender una **Caja Registradora** (o a Wall-E calculando su ruta).
### Nivel 1: Computacional (El "Qué" y el "Por Qué")
* **La Pregunta:** ¿Cuál es el problema que el sistema intenta resolver? ¿Cuál es su meta?
* **En la Caja Registradora:** El objetivo es sumar precios para cobrar la cantidad correcta (aritmética).
* **En el Comportamiento:** A esto le llamamos el **Nivel Racional o Adaptativo**.
  * *Ejemplo:* ¿Por qué la rata deja de palanquear cuando se llena? Porque su meta es mantener la homeostasis energética.
  * *Herramientas:* Aquí usamos la Teoría de la Evolución y la Economía.

⠀Nivel 2: Algorítmico (El "Cómo")
* **La Pregunta:** ¿Qué reglas, pasos o software utiliza el sistema para resolver ese problema?
* **En la Caja Registradora:** Es el código binario o el algoritmo de suma que lleva los acarreos.
* **En el Comportamiento:** Aquí es donde vive la mayor parte de este curso.
  * *Ejemplo:* ¿Cómo sabe la rata que ya comió suficiente? Quizás usa un algoritmo de **Retroalimentación Negativa** (comparar estado actual vs. estado ideal).
  * *Herramientas:* Modelos de Aprendizaje (Rescorla-Wagner, Q-Learning).

⠀Nivel 3: Implementación (El "Dónde")
* **La Pregunta:** ¿En qué hardware físico corre ese algoritmo?
* **En la Caja Registradora:** Son los chips de silicio, los cables y la pantalla LED.
* **En el Comportamiento:** Son las neuronas, las sinapsis y los neurotransmisores (Dopamina).
* *Nota:* Aunque amamos la neurociencia, en este curso nos centraremos en los Niveles 1 y 2. No necesitamos saber cómo funciona un transistor para programar en Python; de la misma forma, podemos entender la lógica del comportamiento sin perdernos en los detalles moleculares de la neurona.

⠀::: {.callout-tip}
# El Enfoque del Curso
La mayoría de los libros de texto tradicionales saltan del Nivel 1 (adaptación vaga) al Nivel 3 (cerebro) sin pasar por el medio.
Este curso es fundamentalmente sobre el Nivel 2: Los Algoritmos. Somos los ingenieros de software de la mente.
:::
# 3\. El Análisis Racional: Nuestra Receta de Cocina
¿Cómo construimos estos modelos? No adivinamos. Seguimos una receta científica llamada **Análisis Racional** (propuesta por John Anderson). En cada capítulo de este libro, verán que seguimos estos 5 pasos:
1. **Especificar la Meta:** ¿Qué quiere el robot? (Ej: Conseguir comida sin ser comido).
2. **Modelar el Entorno:** ¿Cómo es el mundo? (Ej: La comida aparece aleatoriamente o sigue un horario fijo).
3. **Asumir Restricciones:** ¿Qué limitaciones tiene el robot? (Ej: Tiene mala memoria, se mueve lento, tiene poca batería).
4. **Derivar la Conducta Óptima:** Dadas las metas, el entorno y las limitaciones... ¿qué es lo más inteligente que podría hacer? (Aquí usamos matemáticas para encontrar la solución ideal).
5. **Comparar con el Organismo Real:** Vamos al laboratorio. ¿Se comportan las ratas/humanos como predice nuestro modelo óptimo?
   * Si **SÍ**: ¡Bingo! Entendemos el mecanismo.
   * Si **NO**: Hemos descubierto una nueva restricción o nuestro modelo del entorno estaba mal. ¡A investigar más!

⠀4. Modelos Mínimos: La belleza de la simplicidad
A veces escucharán la crítica: *"Estudiar bacterias o ratas es reduccionista. Los humanos somos más complejos"*.
Aquí entra el concepto de Modelos Mínimos (Batterman & Rice).
Pensemos en un atasco de tráfico. El atasco se comporta igual (ondas de frenado) si los coches son Ferraris, Vochos o camiones. Los detalles del "individuo" no importan para la dinámica del "sistema".
En este curso buscamos esas dinámicas universales.
Un algoritmo de Ascenso de Colina funciona igual para:
* Una bacteria buscando azúcar.
* Un robot aspiradora buscando el enchufe.
* Un humano buscando un mejor salario.

⠀Al estudiar el "modelo de juguete" (la bacteria o el robot simple), estamos descubriendo las reglas universales que gobiernan la adaptación, aplicables a cualquier sistema complejo.
# Conclusión
La ciencia del comportamiento adaptable no es una colección de anécdotas sobre perros y campanas. Es la búsqueda de los algoritmos fundamentales que permiten a la vida sobrevivir en un mundo incierto.
A partir del próximo capítulo, dejaremos la filosofía y empezaremos a construir. Nuestro primer problema será simple: **Navegación**. Si nuestro robot tiene hambre y el mundo está oscuro... ¿cómo sabe hacia dónde moverse?

