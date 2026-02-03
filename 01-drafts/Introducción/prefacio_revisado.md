# Prefacio
## Principios y Modelos

Este libro es una edición revisada y extendida del libro de notas *Aprendizaje y Comportamiento Adaptable*. Su origen se encuentra en las presentaciones que desarrollé a lo largo de los años para los tres cursos de Aprendizaje y Comportamiento Adaptable que imparto en la Facultad de Psicología de la UNAM. El libro ofrece una introducción rigurosa pero accesible a los principios y modelos del aprendizaje y comportamiento adaptable. A diferencia de textos tradicionales organizados por paradigmas experimentales (condicionamiento clásico, instrumental, etc.), este libro se estructura alrededor de problemas adaptativos que los organismos deben resolver y las soluciones algorítmicas que han evolucionado para enfrentarlos.

## ¿Para Quién es Este Libro?

Este libro está diseñado para estudiantes de licenciatura en psicología, neurociencia o ciencia cognitiva con el conocimiento básico de matemáticas enseñado en el bachillerato. Si necesitas refrescar estos temas, consulta los tutoriales en Bouzas Lab. También es apropiado para estudiantes de posgrado que desean conectar psicología del aprendizaje con neurociencia computacional y machine learning, así como para profesionales en transición de física, matemáticas, ingeniería o ciencias de la computación hacia neurociencia o ciencia cognitiva.

## Filosofía del Libro

### Marco Conceptual Unificado

El Capítulo 0 presenta el marco general que guía al libro. Aprenderás a distinguir entre nivel computacional (¿qué problema adaptativo se resuelve?), nivel algorítmico (¿qué procedimientos generan el comportamiento?), y nivel de implementación (¿qué circuitos neuronales lo realizan?). Este marco evita confusiones comunes y te permite entender por qué diferentes tipos de modelos coexisten sin competir.

### Énfasis en Principios Generales

En lugar de memorizar fenómenos específicos de protocolos particulares, aprenderás principios que cruzan dominios.

### Implementación Computacional

Todos los modelos en este libro son implementables. No son solo ecuaciones abstractas: puedes programarlos, simularlos y experimentar con ellos.

### Simuladores Interactivos

Este libro incluye simuladores embebidos y enlaces a notebooks interactivos (Google Colab) donde puedes manipular parámetros y observar resultados inmediatos, implementar algoritmos desde cero, replicar experimentos clásicos y explorar extensiones creativas. Accede a todos los simuladores y tutoriales de matemáticas en Bouzas Lab.

## Cómo Usar Este Libro

### Para Estudiantes

Estas notas están diseñadas para lectura activa, no pasiva. Lee el Capítulo 0 completo antes de continuar, ya que establece el marco conceptual necesario. Cuando un capítulo menciona un simulador, explóralo antes de seguir leyendo. La Introducción contiene estrategias detalladas de lectura activa que maximizarán tu aprendizaje.

### Para Instructores

Este libro puede usarse como texto principal en un curso de dos semestres sobre aprendizaje y comportamiento adaptable, como complemento a un texto tradicional añadiendo la perspectiva formal y de optimización que esos textos omiten, o como recurso para temas específicos. Los simuladores permiten clases invertidas donde los estudiantes exploran antes de clase, y el tiempo presencial se dedica a discusión, resolución de problemas y profundización conceptual. La Introducción incluye sugerencias específicas para implementar este modelo pedagógico.

## Recursos Adicionales

### Enlaces Importantes

- **Simuladores:** Material de Apoyo Lab25
- **Código fuente:** GitHub
- **Reportar errores:** GitHub Issues
- **Laboratorio 25:** www.bouzaslab25.com

## Un Argumento Final

Muchos colegas me han dicho que es imposible enseñar estos temas (aprendizaje por refuerzo, modelos bayesianos, teoría de la información) a nivel introductorio. Que los estudiantes de licenciatura no tienen las herramientas matemáticas. Que es mejor mantener el enfoque tradicional, descriptivo, organizado por protocolos.

Discrepo respetuosamente.

Los estudiantes de hoy crecieron con algoritmos de recomendación, navegación GPS y juegos con IA. Tienen una intuición operativa sobre aprendizaje de máquinas que generaciones previas no tenían. Lo que les falta no es capacidad, es un puente entre esa intuición informal y los principios formales.

Los simuladores interactivos, ejemplos concretos y la conexión explícita con aplicaciones contemporáneas construyen ese puente. Las matemáticas no necesitan ser una barrera; pueden ser una revelación.

Más importante, privar a los estudiantes de esta perspectiva integradora (mantenerlos en el mundo de fenómenos desconectados del siglo XX) es hacerles un flaco favor. El comportamiento adaptable no es un museo de curiosidades históricas. Es un campo vivo con aplicaciones en robótica, neurociencias computacionales, economía conductual, psicología clínica, psiquiatría computacional y políticas públicas.

Estas notas son un experimento pedagógico. No tienen el pulido de un libro de editorial, ni las restricciones de extensión o contenido que imponen los mercados académicos. Son un recurso abierto, en evolución, diseñado para estudiantes que no le temen a los formalismos matemáticos y que merecen algo mejor que listas de fenómenos inconexos.

Si funcionan para ti (como estudiante o instructor) compártelas. Si encuentras errores, omisiones o secciones poco claras, comunícamelo. Este es un proyecto colaborativo en el mejor espíritu de la ciencia abierta.

## Licencia y Uso

Este libro se distribuye bajo licencia Creative Commons BY-NC-SA 4.0. Esto significa que puedes compartir (copiar y redistribuir el material) y adaptar (remezclar, transformar y construir sobre el material) bajo las siguientes condiciones: debes dar crédito apropiado (Atribución), no puedes usar el material con fines comerciales (No Comercial), y si remezclas debes distribuir bajo la misma licencia (Compartir Igual).

## Agradecimientos

La primera edición del libro mejoró significativamente gracias al excelente trabajo editorial de Rodrigo Álvarez. La estructura de esta página web fue adaptada del diseño original de Christian Badillo, quien siempre apoyó que este proyecto se concretara.

Mi agradecimiento a varias generaciones del Laboratorio 25 por desarrollar los simuladores interactivos que se encuentran en la página del Laboratorio.

Finalmente, extiendo un agradecimiento especial a los cientos de estudiantes que en mis cursos han sufrido pacientemente mis intentos por enseñar los principios fundamentales del estudio del comportamiento adaptable.

La elaboración de esta página web fue financiado por los proyectos PAPIME PE309624 y PAPIME PE302221.

## Cómo Citar Este Libro

```
@book{bouzas2025aca,
  title = {Aprendizaje y Comportamiento Adaptable: Fundamentos Computacionales y Modelos Formales},
  author = {Bouzas, Arturo},
  year = {2026},
  publisher = {Lab25, UNAM},
  url = {https://github.com/bouzaslab25/libro-aca},
  note = {Licencia CC BY-NC-SA 4.0}
}
```

## Contacto

**Arturo Bouzas**  
Facultad de Psicología  
Universidad Nacional Autónoma de México  
arbouria@unam.mx  
www.bouzaslab25.com

## Aviso: Libro en Desarrollo

Este es un proyecto vivo. El contenido se actualiza regularmente basándose en feedback de estudiantes e instructores, nuevos desarrollos en el campo, y mejoras en simuladores y código. Verifica el repositorio GitHub para la versión más reciente.

**Versión actual:** v1.0 (Enero 2026)

---

**¿Listo para comenzar?** Pasa al Capítulo 0: Introducción
