# 📚 NotasQuarto - Sistema de Escritura y Publicación

Este es tu sistema organizado para escribir, revisar y publicar notas y capítulos de libro usando MWeb → Quarto → GitHub.

## 📁 Estructura de Carpetas

```
NotasQuarto/
├── 01-drafts/              # Borradores iniciales
├── 02-revision/            # Contenido en revisión
├── 03-listos-quarto/       # Listos para exportar a Quarto
├── 04-publicados/          # Archivos ya publicados (histórico)
├── templates/              # Plantillas para nuevos documentos
├── snippets/               # Fragmentos reutilizables (iframes, ecuaciones)
├── assets/
│   ├── imagenes/          # Imágenes y figuras
│   └── datos/             # Datasets, CSV, etc.
├── GUIA-CONFIGURACION-MWEB.md
├── checklist-workflow.md
└── README.md              # Este archivo
```

## 🚀 Inicio Rápido

### Crear Nuevo Capítulo

1. En MWeb, ve a `templates/`
2. Duplica `plantilla-capitulo.md`
3. Muévelo a `01-drafts/`
4. Renombra: `2025-01-XX-titulo-capitulo.md`
5. ¡Empieza a escribir!

### Workflow Resumido

```
01-drafts → 02-revision → 03-listos-quarto → Quarto → GitHub (draft) → GitHub (main)
```

Consulta `checklist-workflow.md` para detalles completos.

## 📝 Plantillas Disponibles

| Plantilla | Uso | Ubicación |
|-----------|-----|-----------|
| `plantilla-capitulo.md` | Capítulos del libro | `templates/` |
| `plantilla-nota-tecnica.md` | Notas técnicas cortas | `templates/` |
| `plantilla-idea.md` | Ideas/borradores rápidos | `templates/` |
| `plantilla-indice-proyecto.md` | Índice general del proyecto | Raíz |

## 🧩 Snippets Disponibles

| Snippet | Contenido | Ubicación |
|---------|-----------|-----------|
| `snippet-iframes.md` | Código para simuladores | `snippets/` |
| `snippet-ecuaciones.md` | Ecuaciones LaTeX comunes | `snippets/` |

## 🏷️ Sistema de Tags

Usa estos tags en el frontmatter YAML:

```yaml
categories: [estado, tema, prioridad]
```

**Estados:**
- `borrador`, `revision`, `listo-quarto`, `publicado`

**Temas:** (personaliza)
- `fisica`, `matematicas`, `programacion`, etc.

**Prioridad:**
- `urgente`, `alta-prioridad`, `baja-prioridad`

## 📏 Convención de Nombres

```
YYYY-MM-DD-titulo-descriptivo.md
```

O para capítulos numerados:
```
cap-XX-titulo.md
```

## 💾 Sistema de Respaldo

Este directorio está respaldado por:

1. **Time Machine** (automático) - Local
2. **iCloud Drive** (opcional) - Nube
3. **Git/GitHub** (para `03-listos-quarto/` y `04-publicados/`) - Versionado

## 🔧 Configuración Inicial

Si es tu primera vez aquí, sigue:

1. Lee `GUIA-CONFIGURACION-MWEB.md`
2. Configura MWeb con External Folder
3. Copia plantillas a `templates/`
4. Familiarízate con `checklist-workflow.md`

## 🎯 Workflow Visual

```
┌─────────────┐
│  01-drafts  │  ← Escribe aquí primero
└──────┬──────┘
       │ Contenido completo
       ▼
┌─────────────┐
│ 02-revision │  ← Revisa y mejora
└──────┬──────┘
       │ Listo para formato
       ▼
┌────────────────┐
│03-listos-quarto│  ← Prepara para export
└──────┬─────────┘
       │ Export desde MWeb
       ▼
┌─────────────┐
│   Quarto    │  ← Agrega iframes
│   (local)   │
└──────┬──────┘
       │ Build exitoso
       ▼
┌─────────────┐
│GitHub (draft)│  ← Prueba en línea
└──────┬──────┘
       │ Todo verificado
       ▼
┌─────────────┐
│GitHub (main) │  ← ¡Publicado! 🎉
└──────┬──────┘
       │ Copia para histórico
       ▼
┌──────────────┐
│04-publicados │
└──────────────┘
```

## 📊 Índice del Proyecto

Mantén actualizado `plantilla-indice-proyecto.md` con:
- Estado de cada capítulo
- Simuladores pendientes
- Timeline de publicación

## 🆘 Ayuda

- **Ecuaciones no renderizan?** → Ver `snippet-ecuaciones.md`
- **Problemas con iframes?** → Ver `snippet-iframes.md`
- **Dudas de workflow?** → Ver `checklist-workflow.md`
- **Configuración de MWeb?** → Ver `GUIA-CONFIGURACION-MWEB.md`

## 🎓 Recursos

- [Documentación de Quarto](https://quarto.org)
- [MWeb User Guide](https://www.mweb.im)
- [LaTeX Math](https://www.overleaf.com/learn/latex/Mathematical_expressions)
- [Markdown Guide](https://www.markdownguide.org)

---

**Versión:** 1.0  
**Creado:** Diciembre 2024  
**Última actualización:** [Fecha]  

**¡Feliz escritura! ✍️**
