# # Evolución Histórica: De la Máquina al Algoritmo {#sec-historia}

> *"La persecución de metas futuras y la elección de los medios para obtenerlas son la marca y el criterio de la presencia de mentalidad."* — William James

Para entender por qué este curso utiliza conceptos de ingeniería, economía e inteligencia artificial, primero debemos entender cómo llegamos aquí. La historia del estudio del comportamiento adaptable no es una simple sucesión de nombres y fechas; es la historia de cómo fuimos refinando nuestro modelo del "agente".

Hemos pasado de ver al organismo como una **máquina de reflejos** a entenderlo como un **sistema de optimización**. A continuación, trazaremos las tres grandes transformaciones que definieron este camino.

## 1. La Tradición Asociacionista: El Hardware Básico

Desde Descartes en el siglo XVII hasta mediados del siglo XIX, la visión dominante fue mecanicista.
* **El Modelo:** El organismo es una máquina reactiva.
* **El Mecanismo:** Un estímulo dispara una respuesta (Reflejo).
* **El Aprendizaje:** Ocurre por **contigüidad temporal**. Si dos eventos ocurren juntos, se conectan.

**Iván Pávlov** llevó esto al laboratorio. Demostró que un estímulo neutral (como un tono) podía "hackear" el sistema de reflejos si predecía un estímulo biológico (comida). Aunque revolucionario, este modelo tenía un límite severo: explicaba cómo el organismo *anticipa* el mundo, pero no cómo *actúa* para cambiarlo. El perro de Pavlov predice la comida, pero no hace nada para conseguirla.

## 2. Primera Transformación: Selección por Consecuencias (El Motor Darwiniano)

A finales del siglo XIX, **William James** y los funcionalistas cambiaron la pregunta. Dejaron de obsesionarse con la estructura del reflejo y se enfocaron en la **función**: ¿Para qué sirve el comportamiento? Para sobrevivir.

La publicación de *El Origen de las Especies* de Darwin (1859) ofreció la clave. La naturaleza crea diseño sin diseñador a través de un algoritmo simple: **Variación, Selección y Retención**.

**Edward Thorndike** tuvo la genialidad de aplicar este algoritmo evolutivo al aprendizaje individual:
* **Ensayo y Error:** El gato en la caja-problema prueba acciones al azar (Variación).
* **Ley del Efecto:** Las acciones seguidas de un estado "satisfactorio" se fortalecen; las que no, se debilitan (Selección).
* **Resultado:** El comportamiento inteligente emerge de las consecuencias, no de la intención.

## 3. Segunda Transformación: El Flujo Conductual (Skinner)

Hasta la década de 1930, se estudiaba el aprendizaje en ensayos discretos (el gato entra, sale, y se acabó el ensayo). **B.F. Skinner** liberó al comportamiento de esta restricción.

Skinner propuso que el comportamiento es un **flujo continuo**.
* **La Innovación:** Introdujo la **Tasa de Respuesta** como medida fundamental de probabilidad.
* **El Entorno:** Ya no era solo un estímulo disparador, sino un contexto estadístico. Los **Programas de Refuerzo** demostraron que la distribución temporal de las recompensas determina la estructura del comportamiento.
* **El Contexto:** Definió el **Estímulo Discriminativo**, no como algo que "empuja" la respuesta, sino como una señal que informa al agente sobre qué reglas de juego (contingencias) están vigentes en ese momento.

## 4. Tercera Transformación: Mapas y Representaciones (Tolman)

Mientras Skinner refinaba el control por consecuencias, **Edward Tolman** demostró que el asociacionismo E-R (Estímulo-Respuesta) era insuficiente.

En sus experimentos de **Aprendizaje Latente**, las ratas aprendían la estructura de un laberinto sin recibir comida. Solo demostraban ese conocimiento cuando aparecía el incentivo.
* **La Conclusión:** El organismo no es una central telefónica que conecta llamadas (E-R). Es un cartógrafo. Construye **Mapas Cognitivos** (representaciones internas) del entorno.
* **El Legado:** Tolman introdujo la idea de que el comportamiento es intrínsecamente **propositivo** (orientado a metas), anticipando los modelos modernos basados en modelos (*Model-Based RL*).

## 5. La Síntesis Contemporánea: Ingeniería, Economía e IA

A partir de 1960, las barreras entre disciplinas se rompieron. El estudio del comportamiento adaptable se fusionó con la teoría de la información, la microeconomía y la computación. Este es el marco teórico de nuestro curso:

### A. El Problema de la Información (Rescorla-Wagner)
Descubrimos que la contigüidad (tiempo) no basta. El fenómeno de **Bloqueo** (Kamin) mostró que el aprendizaje depende de la **Sorpresa**.
* **El Modelo:** Aprendemos para reducir el **Error de Predicción**. Si el mundo ya es predecible, dejamos de aprender. Esto conecta directamente con el aprendizaje supervisado en Inteligencia Artificial.

### B. El Problema de la Elección (Herrnstein y Economía)
**Richard Herrnstein** formuló la **Ley de Igualación**: los organismos distribuyen su conducta en proporción exacta a los refuerzos que reciben.
* **La Conexión:** Esto permitió modelar el comportamiento con herramientas de **Optimización**. Asumimos que el animal (o el humano) actúa como un agente económico racional que busca maximizar su utilidad bajo restricciones de tiempo y energía.

### C. El Problema de la Secuencia (Aprendizaje por Refuerzo)
Finalmente, algoritmos como **Diferencias Temporales (TD Learning)**, desarrollados por Sutton y Barto (inspirados en modelos psicológicos), resolvieron el problema de la **Asignación de Crédito Temporal**: ¿Cómo sé qué acción del pasado causó la recompensa de hoy?

---

**Conclusión del Capítulo**
Hoy, no vemos estas teorías como rivales.
* Usamos a **Thorndike/Skinner** para entender la selección de acciones (*Policy*).
* Usamos a **Tolman** para entender la estructura del entorno (*Model*).
* Usamos a **Rescorla/Wagner** para entender la actualización de expectativas (*Value Function*).

El "Robot" que construiremos en los siguientes capítulos integrará todas estas piezas. Empezaremos por lo más básico: ¿Cómo representamos teóricamente a este agente? Bienvenidos al capítulo de **Modelos**.