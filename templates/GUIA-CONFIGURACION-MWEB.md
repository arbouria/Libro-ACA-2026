# 📘 Guía de Configuración de MWeb

## Paso 1: Crear Estructura de Carpetas

Abre Terminal y ejecuta:

```bash
# Crear carpeta principal
mkdir -p ~/Documents/NotasQuarto

# Crear subcarpetas
cd ~/Documents/NotasQuarto
mkdir -p 01-drafts
mkdir -p 02-revision
mkdir -p 03-listos-quarto
mkdir -p 04-publicados
mkdir -p templates
mkdir -p snippets
mkdir -p assets/imagenes
mkdir -p assets/datos
```

## Paso 2: Copiar Plantillas

Copia las plantillas que creamos a la carpeta correspondiente:

```bash
# Mueve las plantillas a la carpeta templates
mv plantilla-*.md ~/Documents/NotasQuarto/templates/
mv snippet-*.md ~/Documents/NotasQuarto/snippets/
mv checklist-workflow.md ~/Documents/NotasQuarto/
mv plantilla-indice-proyecto.md ~/Documents/NotasQuarto/
```

## Paso 3: Configurar MWeb

### 3.1 Agregar External Folder

1. Abre **MWeb**
2. Ve a **Preferences** (`⌘ + ,`)
3. Selecciona **Library & Folders** en la barra lateral
4. Click en **"+"** (abajo a la izquierda)
5. Selecciona **"Add External Folder"**
6. Navega a: `~/Documents/NotasQuarto/`
7. Click **"Select"**

### 3.2 Configurar la Carpeta

1. Selecciona la carpeta `NotasQuarto` que acabas de agregar
2. En el panel derecho, configura:

**General Settings:**
- ✅ **Use as Document Library folder**
- Nombre: "NotasQuarto" (o el que prefieras)

**Media Settings:**
- Media Folder: `assets/imagenes`
- ✅ Copy media files to Media Folder

**External Mode:**
- ✅ **Enable External Mode**
  (Esto permite edición directa de archivos)

### 3.3 Configurar Markdown y Metadata

1. En Preferences, ve a **Publishing**
2. Selecciona **Markdown**
3. Configura:

**Metadata (Front Matter):**
```yaml
Insert document info: ✅
Format: YAML

Template:
---
title: "{title}"
date: {date:yyyy-MM-dd}
draft: true
---
```

**Markdown Extensions:**
- ✅ Tables
- ✅ Fenced Code Blocks
- ✅ Footnotes
- ✅ Task Lists
- ✅ Strikethrough
- ✅ LaTeX Math

### 3.4 Configurar Editor

En Preferences → **Editor**:

- Font: Monaco 14 (o tu preferencia)
- ✅ Show line numbers
- ✅ Typewriter mode (opcional)
- ✅ Focus mode (opcional)
- Tab width: 2 spaces
- ✅ Auto pair brackets/quotes

### 3.5 Configurar Preview

En Preferences → **Preview**:

- Theme: GitHub (o tu preferencia)
- ✅ Math support (MathJax/KaTeX)
- ✅ Mermaid diagrams
- ✅ Task lists

## Paso 4: Crear Atajos para Plantillas

### Método 1: Snippets de MWeb

1. Ve a **Preferences → Snippets**
2. Click **"+"** para agregar nuevo snippet
3. Configura:

**Snippet 1: Capítulo**
- Nombre: `cap`
- Contenido: (copia el contenido de `plantilla-capitulo.md`)
- Shortcut: `cap` + `Tab`

**Snippet 2: Nota Técnica**
- Nombre: `nota`
- Contenido: (copia el contenido de `plantilla-nota-tecnica.md`)
- Shortcut: `nota` + `Tab`

**Snippet 3: Idea**
- Nombre: `idea`
- Contenido: (copia el contenido de `plantilla-idea.md`)
- Shortcut: `idea` + `Tab`

### Método 2: Usar Plantillas Directamente

Alternativamente, simplemente duplica los archivos de la carpeta `templates/` cuando necesites uno nuevo:

1. En MWeb, navega a `templates/`
2. Click derecho en `plantilla-capitulo.md`
3. Selecciona **Duplicate**
4. Mueve la copia a `01-drafts/`
5. Renombra según tu convención

## Paso 5: Configurar Sistema de Tags

MWeb permite tags en el frontmatter. Usa estos tags estándar:

```yaml
categories: [estado, tema]
```

**Tags de Estado:**
- `borrador`
- `revision`
- `listo-quarto`
- `publicado`

**Tags de Tema:** (personaliza según tu libro)
- `fisica`
- `matematicas`
- `programacion`
- `capitulo`
- `nota-tecnica`
- `idea`

**Tags de Prioridad:**
- `urgente`
- `alta-prioridad`
- `baja-prioridad`

## Paso 6: Configurar Exportación

En Preferences → **Publishing → Export**:

**Markdown:**
- ✅ Preserve YAML front matter
- ✅ Convert relative image paths
- Format: CommonMark

**Export location:**
- Default: Ask each time (o configura una carpeta específica)

## Paso 7: Naming Convention para Archivos

Usa este formato consistente:

```
YYYY-MM-DD-titulo-descriptivo.md
```

Ejemplos:
```
2025-01-15-ecuaciones-maxwell.md
2025-01-20-simulador-ondas.md
2025-02-01-mecanica-cuantica-intro.md
```

O para capítulos numerados:
```
cap-01-introduccion.md
cap-02-fundamentos.md
cap-03-aplicaciones.md
```

## Paso 8: Workflow Diario Recomendado

### Crear Nuevo Documento

1. `⌘ + N` para nuevo documento
2. Escribe `cap` + `Tab` para plantilla de capítulo
3. O duplica plantilla desde `templates/`
4. Guarda en `01-drafts/` con nombre apropiado
5. Empieza a escribir

### Usar Ecuaciones

```latex
Ecuación en línea: $E = mc^2$

Ecuación destacada:
$$
\int_{a}^{b} f(x) \, dx
$$
```

### Insertar Imágenes

```markdown
![Descripción de la imagen](assets/imagenes/nombre.png)
```

MWeb copiará automáticamente la imagen a `assets/imagenes/` si arrastras y sueltas.

### Agregar Placeholder de Simulador

```html
<!-- IFRAME: ondas-mecanicas.html -->
<!-- TODO: Agregar en fase Quarto -->
```

## Paso 9: Backup y Sincronización

### Opción 1: iCloud Drive (Automático)

1. Mueve `~/Documents/NotasQuarto/` a `~/Library/Mobile Documents/com~apple~CloudDocs/NotasQuarto/`
2. Actualiza la referencia en MWeb
3. iCloud sincronizará automáticamente

### Opción 2: Git + GitHub (Manual pero versionado)

```bash
cd ~/Documents/NotasQuarto
git init
git add .
git commit -m "Initial commit"
git remote add origin [tu-repo-url]
git push -u origin main
```

### Opción 3: Time Machine (Local)

- Time Machine ya respalda `~/Documents/` automáticamente
- Asegúrate de tener Time Machine activado

## Paso 10: Verificación Final

Checklist de verificación:

- [ ] External folder agregado correctamente
- [ ] Plantillas copiadas a `templates/`
- [ ] Snippets configurados (opcional)
- [ ] LaTeX math habilitado en preview
- [ ] Media folder configurado
- [ ] External mode habilitado
- [ ] Sistema de tags definido
- [ ] Naming convention decidida
- [ ] Backup configurado

---

## Solución de Problemas Comunes

### Las ecuaciones no se ven en preview
- Verifica que Math support esté habilitado en Preferences → Preview
- Asegúrate de usar delimitadores correctos: `$...$` o `$$...$$`

### Las imágenes no se copian a assets/
- Verifica la configuración de Media Folder
- Asegúrate de que "Copy media files" esté marcado

### No puedo editar archivos en External Folder
- Verifica que "Enable External Mode" esté marcado
- Intenta cerrar y reabrir MWeb

### Los cambios no se sincronizan con iCloud
- iCloud puede tardar unos minutos
- Verifica que iCloud Drive esté funcionando
- Revisa espacio disponible en iCloud

---

## Próximos Pasos

Ahora estás listo para:

1. ✅ Crear tu primer borrador usando las plantillas
2. ✅ Seguir el workflow definido en `checklist-workflow.md`
3. ✅ Mantener actualizado tu `índice-proyecto.md`

**¡Buena suerte con tu proyecto! 🚀**
