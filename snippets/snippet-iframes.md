# Snippets para Iframes

## Iframe Básico

```html
<!-- IFRAME: nombre-simulador.html -->
<div class="simulador-container">
  <iframe 
    src="simuladores/nombre-simulador.html"
    width="100%" 
    height="600px"
    frameborder="0"
    title="Descripción del Simulador">
  </iframe>
  <p class="caption">Figura X: Descripción del simulador interactivo</p>
</div>
<!-- FIN IFRAME -->
```

## Iframe Responsivo

```html
<!-- IFRAME: nombre-simulador.html -->
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe 
    src="simuladores/nombre-simulador.html"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    frameborder="0"
    title="Descripción del Simulador">
  </iframe>
</div>
<p class="caption">Figura X: Descripción del simulador interactivo</p>
<!-- FIN IFRAME -->
```

## Iframe con Fallback

```html
<!-- IFRAME: nombre-simulador.html -->
<div class="simulador-wrapper">
  <iframe 
    src="simuladores/nombre-simulador.html"
    width="100%" 
    height="600px"
    frameborder="0"
    title="Descripción del Simulador">
    <p>Tu navegador no soporta iframes. 
       <a href="simuladores/nombre-simulador.html">Ver simulador en nueva ventana</a>
    </p>
  </iframe>
</div>
<!-- FIN IFRAME -->
```

## Iframe de Observable

```html
<!-- IFRAME: Observable Plot -->
<iframe 
  width="100%" 
  height="584" 
  frameborder="0"
  src="https://observablehq.com/embed/@usuario/notebook?cells=chart">
</iframe>
<!-- FIN IFRAME -->
```

## Iframe de GeoGebra

```html
<!-- IFRAME: GeoGebra -->
<iframe 
  src="https://www.geogebra.org/material/iframe/id/ID_AQUI/width/800/height/600"
  width="800px" 
  height="600px" 
  style="border:0px;"
  scrolling="no">
</iframe>
<!-- FIN IFRAME -->
```

## Placeholder para MWeb

Usa este placeholder mientras trabajas en MWeb (antes de exportar a Quarto):

```markdown
::: {.callout-tip icon=false}
## 🎮 Simulador Interactivo

**[Nombre del Simulador]**

_Este simulador permite experimentar con [descripción breve]._

<!-- IFRAME: nombre-simulador.html -->
<!-- TODO: Agregar iframe en fase Quarto -->

**Instrucciones:**
1. Paso 1
2. Paso 2
3. Paso 3

:::
```
