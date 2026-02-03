 ---
title: "Selección natural y adaptabilidad"
subtitle: "Principios, evidencia moderna y el paralelo con aprendizaje"
author: "Arturo Bouzas & Lab25"
date: last-modified
format:
  html:
    toc: true
    toc-depth: 3
    number-sections: true
  pdf:
    toc: true
    number-sections: true
    geometry: margin=1in
execute:
  echo: false
  warning: false
  message: false
---

## 1. Propósito del capítulo

Este capítulo cumple dos funciones dentro del libro. La primera es presentar la teoría de la selección natural como explicación general del origen de la adaptación biológica, en un nivel adecuado para estudiantes de psicología. La segunda es usar esa teoría como ejemplo paradigmático de un **modelo de adaptabilidad**: un mecanismo que produce ajuste a restricciones ambientales, pero operando a una escala temporal distinta de los mecanismos de aprendizaje.

En el resto del libro estudiaremos sistemas adaptativos que cambian dentro del individuo: aprendizaje por refuerzo, exploración–explotación, formación de hábitos y ajuste a entornos no estacionarios. La selección natural ofrece un contraste: también resuelve problemas de adaptación, pero a nivel de poblaciones, mediante cambios en frecuencias a través de generaciones.

Este contraste será útil si mantenemos una regla metodológica: evitaremos teleología. El proceso no “busca” soluciones; cambia distribuciones. En términos simples: no se selecciona “al mejor”; se eliminan los que no pasan por el filtro.

---

## 2. Dos observaciones que requieren explicación: variabilidad y adaptación

Dos hechos generales motivan la teoría. Primero, existe una inmensa variabilidad entre organismos: variabilidad morfológica, fisiológica y conductual. En segundo lugar, esa variabilidad no se distribuye al azar: con frecuencia está correlacionada con propiedades del entorno donde vive la especie. El ejemplo clásico es la correlación entre forma del pico y tipo de alimento en aves relacionadas.

La propuesta de Darwin es que el ajuste (adaptación) no requiere un diseñador; puede emerger de un proceso simple repetido durante muchas generaciones.

---

## 3. Tres principios de la teoría de la selección natural

La teoría de Darwin puede organizarse en tres principios:

1. **Variabilidad.** Existe variabilidad en rasgos entre miembros de una especie.  
2. **Heredabilidad.** Parte de esa variabilidad se transmite de una generación a otra.  
3. **Éxito reproductivo diferencial.** Existe covarianza entre rasgos y número de descendientes; parte de esa covarianza es atribuible al papel causal de los rasgos en supervivencia y reproducción.

Si se satisfacen estos tres principios, entonces, de generación a generación, los rasgos asociados con mayor éxito reproductivo incrementarán su frecuencia en la población.

---

## 4. Éxito reproductivo diferencial y filtros

El éxito reproductivo diferencial puede entenderse como el número de “copias” que se dejan de una generación a otra. Son las propiedades estadísticas del entorno las que determinan el éxito reproductivo diferencial de los rasgos.

Una analogía útil es considerar a los entornos como **filtros** sobre la variabilidad. Los filtros cambian la frecuencia relativa de un rasgo en una población. Es crucial no confundir el resultado con una intención: el filtro no “elige al mejor”; elimina diferencialmente.

### 4.1 Analogía: la caja de inserción de formas

La cubierta de una caja infantil tiene orificios de diferentes formas; objetos con formas compatibles pasan, otros no. Si vaciamos un saco con objetos (rasgos) sobre una cubierta (entorno), la distribución final de objetos que pasa es la “siguiente generación”. El filtro no necesita inteligencia para producir cambios sistemáticos.

### 4.2 El límite de la analogía: la necesidad de variación nueva

La analogía anterior no contempla la creación de objetos nuevos. La selección natural requiere un proceso que produzca variabilidad de generación a generación: mutación, recombinación, migración, etc.

---

## 5. Un modelo mínimo (numérico): resistencia antibiótica como ejemplo conductor

Este capítulo usará resistencia a antibióticos como ejemplo por su claridad y porque prepara la lectura de evolución experimental.

### 5.1 Dos tipos: R (resistente) y S (sensible)

Sea \(p\) la proporción de resistentes (R) antes de reproducirse, y \(1-p\) la de sensibles (S). Asignamos **fitness** (éxito reproductivo esperado):

- \(w_R\): descendencia media de R  
- \(w_S\): descendencia media de S  

Fitness promedio:
\[
\bar w = p w_R + (1-p) w_S
\]

Actualización de frecuencia (una generación):
\[
p' = \frac{p w_R}{\bar w}
\]

### 5.2 Ejemplo trabajado 1: con antibiótico

Supón que se introduce un antibiótico y ahora:

- \(w_R = 1.5\)  
- \(w_S = 0.5\)  
- \(p = 0.10\)

1) \(\bar w = 0.10(1.5) + 0.90(0.5) = 0.15 + 0.45 = 0.60\)  
2) \(p' = \frac{0.10(1.5)}{0.60} = \frac{0.15}{0.60} = 0.25\)

Interpretación: en una generación, R sube de 10% a 25% porque deja más “copias” bajo ese filtro.

### 5.3 Ejercicio 1: costo sin antibiótico (con respuesta)

Sin antibiótico, supón costos de resistencia:

- \(w_R = 0.95\), \(w_S = 1.00\), \(p = 0.10\)

**Ejercicio 1.** Calcula \(p'\). ¿Sube o baja R?

**Respuesta.**
\[
\bar w = 0.10(0.95) + 0.90(1.00) = 0.095 + 0.90 = 0.995
\]
\[
p'=\frac{0.10(0.95)}{0.995}\approx 0.0955
\]
R baja ligeramente: hay costo.

**Discusión.** ¿Qué “tendencia” esperas si el costo \(c\) aumenta (todo lo demás constante)?

---

## 6. Mutación y selección: una división del trabajo (con números)

Una intuición moderna clave es la división del trabajo:

- **Mutación** (y procesos similares) introduce variantes.  
- **Selección** cambia frecuencias según el entorno.

### 6.1 Mutación mínima en el modelo R/S

Ahora añade una tasa \(\mu\) de mutación S→R (modelo mínimo):

1) Selección:
\[
p_{\text{sel}} = \frac{p w_R}{\bar w}
\]
2) Mutación:
\[
p' = p_{\text{sel}} + \mu(1 - p_{\text{sel}})
\]

### 6.2 Ejercicio 2: dos frases, dos fuerzas (con respuesta)

**Ejercicio 2.** En ambiente con antibiótico fuerte, explica en 2 líneas qué hace mutación y qué hace selección.

**Respuesta.** Mutación introduce (o reintroduce) variantes resistentes; selección amplifica resistentes porque dejan más descendencia bajo antibiótico.

**Discusión.** ¿Cómo cambia tu respuesta si el ambiente alterna ON/OFF?

---

## 7. Deriva y neutralidad: por qué “favorable” no es “inevitable”

Cuando una mutación favorable aparece en pocos individuos, puede perderse por azar (muestreo) antes de ser amplificada. Por eso, selección empuja direccionalmente en promedio, pero deriva introduce fluctuaciones y puede borrar variantes raras.

### 7.1 Ejercicio 3: rareza y azar (con respuesta)

**Ejercicio 3.**
1) Una mutación resistente aparece en un solo individuo. ¿Por qué podría perderse aunque sea favorable?  
2) ¿Qué cambia si aparecen 50 resistentes en la misma generación?

**Respuesta.**  
1) Por azar de reproducción/mortalidad cuando es rara: puede extinguirse antes de multiplicarse.  
2) Con 50 copias, la pérdida accidental es menos probable y la selección tiene más material para amplificar.

**Discusión.** ¿Cómo se relaciona esto con el hecho de que “mutaciones favorables” pueden ser raras?

---

## 8. Adaptación: perspectiva actual y perspectiva histórica

Conviene distinguir dos sentidos de “adaptación”.

1) **Ventaja actual.** Un rasgo puede ser útil hoy sin ser producto directo de selección para ese contexto.  
2) **Adaptación histórica.** Reservamos “adaptación” para rasgos cuya existencia es resultado de un proceso de selección natural en el pasado.

Esta distinción es crucial para evitar explicaciones ad hoc: una historia plausible no basta; necesitamos predicciones y evidencia comparativa o mecanicista.

---

## 9. Paisaje adaptativo y optimización (con matices)

Es útil representar el problema como un paisaje: un espacio multidimensional donde el eje vertical representa éxito reproductivo asociado a combinaciones fenotípicas.

En este marco, selección puede describirse como ascenso de colina. Pero hay tres matices: (a) el entorno puede cambiar y desplazar el óptimo; (b) moverse requiere variación; (c) la imagen de “colina lisa” falla cuando el paisaje es rugoso.

---

## 10. Paisajes rugosos y dependencia histórica (modelo mínimo con valle)

Considere dos cambios A y B y cuatro genotipos: 00, 10, 01, 11. Suponga fitness relativo:

| Genotipo | 00 | 10 | 01 | 11 |
|---|---:|---:|---:|---:|
| Fitness \(w\) | 1.00 | 0.95 | 0.95 | 1.20 |

Aquí 11 es superior, pero 10 y 01 son inferiores a 00: hay un “valle”.

### 10.1 Ejercicio 4: la selección local es miope (con respuesta)

**Ejercicio 4.**
1) Desde 00, ¿qué mutación sería favorecida localmente?  
2) ¿Qué implica para llegar a 11?  
3) Menciona dos mecanismos que podrían permitir llegar a 11.

**Respuesta.**
1) Ninguna: 10 y 01 son peores que 00.  
2) La selección local se queda atrapada: no hay gradiente favorable “paso a paso”.  
3) Deriva/azar (especialmente con cuellos de botella), cambios de ambiente que modifiquen el paisaje, recombinación, rutas alternativas por mutaciones adicionales.

**Discusión.** ¿Cuál es el análogo conductual de “quedarse atrapado” en 00?

---

## 11. Selección dependiente de frecuencia: equilibrio 50/50 de sexos (ejemplo central)

Antes de pasar a evidencia y casos empíricos, conviene introducir un tipo de explicación que reaparecerá en varios capítulos del libro: las explicaciones por **equilibrio**. 

En psicología estamos acostumbrados a contar historias causales en secuencia: ocurrió A, luego B, y por tanto C. En cambio, muchos modelos evolutivos (y muchos modelos de conducta) se formulan como problemas de estabilidad: dadas ciertas reglas de interacción, ¿cuál es el estado al que el sistema regresa después de una perturbación?

La selección dependiente de frecuencia es una buena entrada porque obliga a abandonar dos intuiciones. La primera es que el éxito reproductivo de un rasgo es una constante; aquí depende del estado de la población. La segunda es que una explicación científica debe reconstruir “paso a paso” una historia particular; en muchos casos, el objetivo es derivar por qué existe un punto fijo y por qué ese punto fijo es estable. Este tipo de razonamiento será útil más adelante cuando estudiemos modelos de decisión y aprendizaje que también se entienden mejor como dinámicas que convergen (o no) a políticas estables.


Este ejemplo es ideal para mostrar explicaciones de equilibrio (modelos de estado estable más que historias detalladas).

Sea \(p\) la proporción de machos (y \(1-p\) la de hembras). Un modelo mínimo captura que el valor reproductivo de producir un sexo depende de su frecuencia:

\[
w_{\text{macho}}(p)\ \propto\ \frac{1-p}{p}
\qquad\qquad
w_{\text{hembra}}(p)\ \propto\ \frac{p}{1-p}
\]

El cociente:
\[
\frac{w_{\text{macho}}(p)}{w_{\text{hembra}}(p)}=\left(\frac{1-p}{p}\right)^2
\]

- Si \(p<0.5\), el cociente \(>1\): conviene producir más machos → \(p\) sube.  
- Si \(p>0.5\), el cociente \(<1\): conviene producir más hembras → \(p\) baja.  
- \(p=0.5\) es equilibrio estable (retroalimentación negativa).

### 11.1 Ejercicio 5: verifica el empuje (con respuesta)

**Ejercicio 5.**
1) Para \(p=0.40\), ¿el cociente es >1 o <1?  
2) Para \(p=0.60\), ¿qué ocurre?  
3) En una frase: ¿por qué esto es dependiente de frecuencia?

**Respuesta.**  
1) \(((0.60/0.40)^2)=(1.5)^2=2.25>1\): conviene producir machos → \(p\) sube.  
2) \(((0.40/0.60)^2)\approx(0.666)^2\approx0.444<1\): conviene producir hembras → \(p\) baja.  
3) Porque el fitness depende del estado poblacional \(p\), no es constante.

**Discusión.** ¿Qué ganamos al explicar 50/50 como equilibrio, en lugar de contar una historia “paso a paso” de cómo se llegó ahí?

En resumen, el ejemplo 50/50 muestra que una explicación evolutiva no siempre consiste en narrar una secuencia histórica; a veces consiste en derivar un estado estable y mostrar por qué el sistema regresa a él cuando se lo perturba. Esta forma de explicación será útil más adelante: en aprendizaje y decisión también encontraremos dinámicas donde el “resultado” relevante no es una trayectoria particular, sino el tipo de política o patrón estable que emerge bajo ciertas reglas de interacción.


---

## 12. Evolución experimental: el LTEE como “película” de la adaptación

La evolución experimental permite observar procesos que en condiciones naturales serían difíciles de reconstruir. El experimento de Lenski con E. coli es ejemplar por dos rasgos metodológicos: (a) múltiples poblaciones fundadas a partir de un ancestro común y (b) archivo de muestras congeladas que permite comparar presente y pasado e incluso reiniciar líneas.

Didácticamente, el LTEE permite introducir tres ideas: (1) mejora sistemática con rendimientos decrecientes, (2) paralelismo parcial y divergencia, y (3) episodios raros de innovación cuya interpretación depende de la historia previa.

### 12.1 Ejercicio 6: tres predicciones cualitativas (con respuesta)

**Ejercicio 6.**
1) ¿Qué esperas del fitness en las primeras ~2,000 generaciones?  
2) ¿Todas las poblaciones terminarán idénticas? ¿por qué?  
3) ¿Qué papel tiene la mutación: “motor” o “ruido”?

**Respuesta guía.**
1) Subida relativamente rápida seguida de desaceleración.  
2) No necesariamente: azar histórico y rutas accesibles pueden diferenciar líneas.  
3) Motor porque aporta variación; ruido porque muchas mutaciones serán neutrales o de efecto pequeño.

**Discusión.** ¿Qué observación empírica del LTEE te parecería más “anti-teleológica”?

---

## 13. Resistencia antibiótica en versión completa: equilibrio mutación–selección

En ausencia de antibiótico, la resistencia puede tener costo. Sin embargo, si existe una fuente constante de resistencia (mutación/adquisición), puede existir un equilibrio.

### 13.1 Modelo mínimo

- \(w_S = 1\)  
- \(w_R = 1-c\) (costo \(c>0\))  
- mutación S→R con tasa \(\mu\)

Aproximación didáctica útil (para \(\mu\) pequeña):
\[
p^\* \approx \frac{\mu}{c}
\]

### 13.2 Ejemplo trabajado 2: piso de resistencia

Supón \(c=0.05\) y \(\mu=10^{-5}\).
\[
p^\*\approx \frac{10^{-5}}{0.05} = 2\times 10^{-4} = 0.02\%
\]

Interpretación: no llega a cero; hay un “piso” de resistencia por variación nueva constante.

**Discusión.** ¿En qué sentido este “piso” es análogo a mantener exploración en un bandit?

---

## 14. Antibióticos intermitentes: paisajes que se mueven (con cálculo de 4 días)

Alternar ambiente con antibiótico (ON) y sin antibiótico (OFF) desplaza el “óptimo” y puede producir ciclos.

Usa:
\[
p'=\frac{p w_R}{p w_R+(1-p)w_S}
\]

### 14.1 Ejercicio 7: cuatro días (con respuesta completa)

Valores:

- OFF: \(w_R=0.9\), \(w_S=1.0\)  
- ON: \(w_R=1.0\), \(w_S=0.2\)  
- Inicio: \(p_0=0.01\)  
- Secuencia: ON, ON, OFF, OFF

**Respuesta paso a paso**

Paso 1 (ON):
\[
\bar w = 0.01(1.0)+0.99(0.2)=0.208
\Rightarrow
p_1=\frac{0.01}{0.208}\approx 0.0481
\]

Paso 2 (ON):
\[
\bar w = 0.0481(1.0)+0.9519(0.2)=0.2385
\Rightarrow
p_2=\frac{0.0481}{0.2385}\approx 0.2017
\]

Paso 3 (OFF):
\[
\bar w = 0.2017(0.9)+0.7983(1.0)=0.9798
\Rightarrow
p_3=\frac{0.2017(0.9)}{0.9798}\approx 0.1852
\]

Paso 4 (OFF):
\[
\bar w = 0.1852(0.9)+0.8148(1.0)=0.9815
\Rightarrow
p_4=\frac{0.1852(0.9)}{0.9815}\approx 0.1698
\]

Patrón: ON sube \(p\) rápido; OFF lo baja lento si el costo es moderado.

**Discusión.** ¿Qué condición cualitativa haría que OFF “revirtiera” casi por completo lo ganado en ON?

---

## 15. Un paralelo conductual explícito: exploración–explotación en bandits (con números)

Hasta aquí hemos usado resistencia antibiótica y paisajes adaptativos para ilustrar cómo cambia una distribución de variantes bajo filtros ambientales. Ahora conviene hacer explícita la razón por la que este capítulo aparece en un libro de psicología del aprendizaje y la adaptabilidad: muchas preguntas que hacemos sobre conducta pueden leerse como preguntas análogas sobre adaptación, solo que a una escala temporal distinta.

En los capítulos de aprendizaje por refuerzo veremos al individuo como un sistema que debe ajustarse a un entorno incierto y, con frecuencia, cambiante. El dilema central es exploración–explotación: explorar para obtener información y descubrir alternativas, o explotar lo que ya parece funcionar. Ese dilema no es exclusivo del aprendizaje. En evolución, aunque no exista un “agente” que decida, el sistema también enfrenta una versión estructural del mismo problema: sin variación no hay innovación, pero sin selección no hay acumulación. Un ejemplo numérico mínimo de bandits ayuda a fijar la intuición antes de volver a Price.


En aprendizaje, el individuo resuelve un problema de adaptación rápido: elegir bajo incertidumbre. El dilema exploración–explotación evita dos errores simétricos: (a) explotar demasiado pronto (quedarse en un “pico local” por muestras escasas) o (b) explorar sin consolidar.

### 15.1 Ejercicio 8: mini-bandit (con respuesta)

Opciones A–D con recompensas observadas:

- A: 3, 2, 4  
- B: 1, 1, 0, 2  
- C: 5  
- D: 2, 2

**Ejercicio 8.**
1) Calcula promedios observados.  
2) Si explotas, ¿cuál eliges en la siguiente prueba?  
3) Si exploras razonablemente, ¿cuál exploras y por qué?  
4) ¿Qué sería un “pico local” aquí?

**Respuesta.**
1) \(\bar A=3.0\), \(\bar B=1.0\), \(\bar C=5.0\), \(\bar D=2.0\).  
2) Explotar: C.  
3) Explorar razonable: A (tiene evidencia moderada y buen promedio; C tiene n=1).  
4) Pico local: quedar “encandilado” con C por una sola muestra; explorar reduce el riesgo de confundir ruido con estructura.

**Discusión.** ¿Qué parámetro “psicológico” podría regular exploración: aversión al riesgo, curiosidad, o ambos?

En resumen, el mini-bandit sirve como versión comprimida de un problema general de adaptabilidad: decidir bajo incertidumbre y con información incompleta. En el individuo, la exploración puede ser una estrategia; en evolución, la variación aparece sin intención. Sin embargo, en ambos casos la pregunta estructural es la misma: cómo evitar quedar atrapados en soluciones aparentes por evidencia escasa y cómo acumular mejoras sin perder la capacidad de responder a cambios del entorno. Esta idea prepara el terreno para introducir una “contabilidad” formal del cambio: la ecuación de Price.


---

## 16. Ecuación de Price: una gramática común para selección, mutación y el puente con aprendizaje

En el resto del libro aparecerá con frecuencia un patrón explicativo: describir un cambio observado como la suma de componentes distinguibles. En psicología, un ejemplo familiar es separar desempeño en sesgo y sensibilidad, o separar respuesta en señal y ruido. En teoría evolutiva existe una herramienta sorprendentemente general para hacer una separación análoga: la ecuación de Price.

Su valor, para este capítulo, no es solo formal. Price nos obliga a escribir con precisión una idea que hemos repetido de forma intuitiva: el cambio poblacional no ocurre por una sola “fuerza”. Una parte del cambio es selección (asociación entre rasgo y éxito reproductivo) y otra parte es transmisión (cambios dentro del linaje: mutación y otros sesgos). Esta descomposición será el puente natural con aprendizaje: más adelante, la parte “dentro del linaje” tendrá análogos en la actualización interna del individuo, mientras que la parte “selección” será análoga al papel de la consecuencia en seleccionar acciones o políticas.


La ecuación de Price separa el cambio total en dos componentes: selección y transmisión.

Para un rasgo \(z\):
\[
\Delta \bar z \;=\; \frac{1}{\bar w}\,\mathrm{Cov}(w_i,z_i)\;+\;\frac{1}{\bar w}\,\mathrm{E}(w_i\,\Delta z_i)
\]

El primer término captura selección (asociación entre rasgo y reproducción). El segundo término captura cambios “dentro del linaje” (mutación u otros sesgos de transmisión).

### 16.1 Ejercicio 9: Price paso a paso (con tabla y respuesta)

Definimos \(z\): resistente=1, sensible=0.

| i | \(z_i\) | \(w_i\) | \(\Delta z_i\) |
|---|---:|---:|---:|
| 1 | 1 | 2 | -0.10 |
| 2 | 1 | 1 | 0 |
| 3 | 0 | 1 | +0.05 |
| 4 | 0 | 2 | +0.05 |
| 5 | 0 | 0 | 0 |

**Respuesta.**
1) \(\bar w = (2+1+1+2+0)/5 = 1.2\)  
2) \(\bar z = (1+1+0+0+0)/5 = 0.4\)  
3) \(E(wz) = (2\cdot1 + 1\cdot1 + 1\cdot0 + 2\cdot0 + 0)/5 = 0.6\)  
4) \(\mathrm{Cov}(w,z)=E(wz)-E(w)E(z)=0.6-(1.2)(0.4)=0.12\)  
5) Selección: \(0.12/1.2=0.10\)

Transmisión:
\[
E(w\Delta z) = [2(-0.1)+1(0)+1(0.05)+2(0.05)+0]/5 = -0.01
\]
\[
(1/\bar w)E(w\Delta z)=-0.01/1.2\approx -0.0083
\]

Total:
\[
\Delta \bar z \approx 0.10 - 0.0083 = 0.0917
\]

**Discusión.** ¿Qué componente (selección o transmisión) sería análogo a “actualización” interna en aprendizaje?

En resumen, Price permite decir con precisión algo que, de otro modo, queda como intuición: el cambio total puede descomponerse en un componente atribuible a selección y otro atribuible a transmisión. Esta separación es útil porque evita confundir el papel del filtro con el origen de la variación y porque, además, prepara un puente natural con aprendizaje: cuando pasemos a modelos de actualización en el individuo, volveremos a encontrar una distinción análoga entre cambios debidos a “retroalimentación” y cambios debidos a procesos internos de actualización, ruido u olvido.


---

## 17. Evolución como aprendizaje: un paralelo formal (no psicológico)

El hilo del capítulo puede cerrarse sin metáforas engañosas. Selección natural y aprendizaje son dos solucionadores de adaptación, pero en escalas temporales distintas y con unidades distintas.

- En evolución, el estado relevante es la distribución de variantes en una población; lo que cambia es la frecuencia de esas variantes.  
- En aprendizaje, el estado relevante es interno al individuo (valores, hábitos, políticas); lo que cambia es una regla de elección o una función de valor.

La analogía útil es formal: ambos procesos pueden describirse como variación + filtrado + retención. El error sería confundir esto con intención o con metas en la evolución.

### 17.1 Ejercicio 10: identifica la unidad (con respuesta)

**Ejercicio 10.**
1) En resistencia antibiótica, ¿qué “cambia” realmente?  
2) En bandits, ¿qué se actualiza?  
3) ¿Qué error cometes si confundes ambos?

**Respuesta.**
1) Cambian frecuencias en la población.  
2) Se actualiza valor o política dentro del individuo.  
3) Atribuyes intención a la evolución o reduces aprendizaje a un proceso poblacional.

**Discusión.** ¿En qué sentido el vocabulario “como si maximizara” es útil, y en qué sentido es peligroso?

---

## 18. Controversia contemporánea: “teoría extendida” (EES) como mapa de debate

Una discusión contemporánea gira en torno a si la teoría evolutiva requiere un marco extendido que ponga en primer plano desarrollo, plasticidad, construcción de nicho y herencias ampliadas. Para este curso, el valor pedagógico del debate es metodológico: muestra cómo cambian los modelos cuando cambian las variables que se consideran fundamentales y las predicciones que se exigen.

En psicología, el paralelo es inmediato: debates sobre “qué es fundamental” (cognición, aprendizaje, cultura) alteran qué se modela explícitamente y qué se trata como ruido.

---

## 19. Cuidado con historias ad hoc (“just-so stories”)

Las explicaciones adaptativas pueden degenerar en historias plausibles que no arriesgan predicciones. Para mantener estándar científico conviene seguir tres reglas: (1) distinguir ventaja actual de origen histórico; (2) exigir predicciones contrastables (comparativas, trade-offs, mecanismos plausibles); (3) competir contra alternativas (neutralidad/deriva, subproducto, restricciones, mismatch).

### 19.1 Ejercicio 11: arregla un “cuento” (con respuesta)

Frase: “La gente prefiere azúcar porque fue adaptativo en el pasado”.

**Ejercicio 11.**
1) ¿Qué parte es utilidad presente y cuál es origen histórico?  
2) Da dos predicciones contrastables.  
3) Da una alternativa no-adaptativa o parcialmente adaptativa.

**Respuesta guía.**
1) La frase mezcla ambos sentidos; utilidad presente no prueba origen histórico.  
2) Predicciones comparativas y trade-offs: variación sistemática con condiciones ecológicas/históricas; costos o correlatos fisiológicos específicos.  
3) Subproducto de sistemas generales de recompensa + cambio cultural/industrial reciente (mismatch).

**Discusión.** ¿Qué parte del problema es empírico (datos) y qué parte es conceptual (definiciones)?

---

## 20. En resumen: selección natural y aprendizaje como dos solucionadores de adaptación

1) Selección natural cambia frecuencias por éxito reproductivo diferencial bajo filtros ambientales.  
2) Mutación y recombinación sostienen exploración de variantes; selección acumula explotación.  
3) La imagen de ascenso de colina es útil, pero requiere matices: rugosidad, neutralidad, restricciones e historia.  
4) La selección dependiente de frecuencia (50/50 sexos) muestra equilibrios y modelos de estado estable.  
5) Resistencia antibiótica y ambientes intermitentes ejemplifican paisajes que se mueven y equilibrios mutación–selección.  
6) Price separa selección y transmisión y ofrece una gramática común para conectar con aprendizaje.  
7) Selección natural y aprendizaje son dos solucionadores de adaptación a escalas distintas: población e individuo.

---

## 21. Autoevaluación breve (5 preguntas)

1) ¿Qué significa “filtro” y por qué no implica intención?  
2) ¿Qué condición hace que el 50/50 sexos sea equilibrio estable?  
3) ¿Por qué puede haber un “piso” de resistencia sin antibiótico?  
4) ¿Qué muestra el ejemplo del valle epistático sobre historia?  
5) ¿Qué separa Price y por qué eso ayuda a tender puentes con aprendizaje?
# 