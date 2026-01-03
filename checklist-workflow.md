# ✅ Checklist de Workflow

## Fase 1: Creación (Carpeta: `01-drafts/`)

- [ ] Crear archivo desde plantilla apropiada
- [ ] Escribir contenido principal
- [ ] Agregar ecuaciones necesarias
- [ ] Vista previa en MWeb
- [ ] Agregar placeholders para simuladores
- [ ] Primera auto-revisión rápida

**Criterio para pasar a Fase 2:** Contenido completo en borrador, estructura clara

---

## Fase 2: Revisión (Carpeta: `02-revision/`)

- [ ] Mover archivo a `02-revision/`
- [ ] Revisar estructura lógica
- [ ] Verificar ecuaciones (sintaxis LaTeX correcta)
- [ ] Revisar ortografía y gramática
- [ ] Agregar/mejorar ejemplos
- [ ] Completar referencias
- [ ] Verificar que imágenes estén en `assets/`
- [ ] Listar simuladores necesarios
- [ ] Segunda lectura crítica

**Criterio para pasar a Fase 3:** Contenido revisado, listo para formato Quarto

---

## Fase 3: Preparación Quarto (Carpeta: `03-listos-quarto/`)

- [ ] Mover archivo a `03-listos-quarto/`
- [ ] Verificar/ajustar frontmatter YAML
- [ ] Confirmar compatibilidad de ecuaciones
- [ ] Marcar ubicaciones exactas de iframes con comentarios
- [ ] Verificar que paths de imágenes sean correctos
- [ ] Agregar callouts de Quarto si aplica
- [ ] Probar exportación de MWeb
- [ ] Verificar categorías y tags

**Formato de comentario para iframes:**
```html
<!-- IFRAME: nombre-archivo.html -->
<!-- Descripción: [función del simulador] -->
<!-- Ubicación: simuladores/nombre-archivo.html -->
<!-- TODO: Insertar en Quarto -->
```

**Criterio para pasar a Fase 4:** Archivo exportable, simuladores identificados

---

## Fase 4: Integración Quarto (Carpeta Local de Quarto)

- [ ] Exportar desde MWeb como Markdown
- [ ] Copiar a proyecto Quarto local
- [ ] Insertar iframes según comentarios
- [ ] Crear/agregar simuladores faltantes
- [ ] Verificar renderización local (`quarto preview`)
- [ ] Revisar TOC (tabla de contenidos)
- [ ] Probar enlaces internos
- [ ] Verificar responsividad de iframes
- [ ] Build local exitoso (`quarto render`)

**Criterio para pasar a Fase 5:** Renderiza correctamente en local

---

## Fase 5: Draft en GitHub (Rama: `draft`)

- [ ] Commit a rama `draft`
- [ ] Push a GitHub
- [ ] Verificar GitHub Pages en draft (si aplicable)
- [ ] Revisar en diferentes dispositivos
- [ ] Probar simuladores en vivo
- [ ] Revisión final de contenido
- [ ] Solicitar feedback (opcional)
- [ ] Corregir issues encontrados

**Criterio para pasar a Fase 6:** Todo funciona correctamente en draft

---

## Fase 6: Publicación (Rama: `main`)

- [ ] Merge de `draft` a `main`
- [ ] Push a rama principal
- [ ] Verificar deployment automático
- [ ] Probar sitio en producción
- [ ] Compartir URL (si aplica)
- [ ] Actualizar índice del proyecto en MWeb
- [ ] Mover copia a `04-publicados/` en MWeb
- [ ] Cambiar tag a `#publicado`
- [ ] Celebrar 🎉

---

## Post-Publicación

- [ ] Documentar lecciones aprendidas
- [ ] Anotar mejoras para futuro
- [ ] Actualizar estadísticas en índice
- [ ] Planificar siguiente capítulo

---

## Checklist de Emergencia (Si algo falla)

### Ecuaciones no renderizan
- [ ] Verificar sintaxis LaTeX
- [ ] Verificar delimitadores `$$` o `$`
- [ ] Buscar caracteres especiales sin escapar

### Simulador no carga
- [ ] Verificar path del iframe
- [ ] Verificar archivo existe en carpeta
- [ ] Probar simulador standalone
- [ ] Revisar consola del navegador

### Imágenes no aparecen
- [ ] Verificar path relativo
- [ ] Confirmar imagen en `assets/`
- [ ] Revisar extensión del archivo
- [ ] Verificar nombres sin espacios

### Build falla en Quarto
- [ ] Revisar YAML frontmatter
- [ ] Verificar comillas en título
- [ ] Buscar caracteres especiales
- [ ] Revisar mensajes de error específicos

---

## Atajos de Teclado Útiles (MWeb Mac)

- `⌘ + N` - Nuevo documento
- `⌘ + E` - Exportar
- `⌘ + L` - Insertar enlace
- `⌘ + K` - Insertar código
- `⌘ + Shift + K` - Insertar bloque de código
- `⌘ + R` - Preview
- `⌘ + B` - Bold
- `⌘ + I` - Italic

---

**Versión del checklist:** 1.0  
**Última actualización:** [Fecha]
