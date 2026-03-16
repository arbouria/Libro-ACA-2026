"""
estilo_libro_aca.py
===================
Estilo visual unificado para todas las figuras del libro
"Aprendizaje y Comportamiento Adaptable: Principios y Modelos"
Arturo Bouzas — Facultad de Psicología, UNAM

USO
---
Al inicio de cualquier script de figura del libro, agregar:

    import sys
    sys.path.insert(0, '.')          # o la ruta donde guardaste este archivo
    from estilo_libro_aca import aplicar_estilo, COLORES, nueva_figura, guardar_figura

    aplicar_estilo()                 # activa el estilo globalmente

    fig, ax = nueva_figura()         # figura estándar de un panel
    fig, axes = nueva_figura(2, 2)   # grilla de 2×2 paneles

PALETA DE COLORES
-----------------
Se usa una paleta en escala de grises con un acento de color neutro,
apropiada para impresión en blanco y negro y accesible para lectores
con deficiencia de visión al color.

    COLORES['principal']   → negro     (curva o dato central)
    COLORES['secundario']  → gris medio (curva comparativa)
    COLORES['terciario']   → gris claro (curva de referencia o fondo)
    COLORES['acento']      → azul pizarrón (énfasis puntual, si se imprime color)
    COLORES['referencia']  → línea punteada de referencia / azar

Para figuras con más de tres series, usar COLORES['secuencia'],
que es una lista de grises ordenada de oscuro a claro.
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# ── Paleta ────────────────────────────────────────────────────────────────────
COLORES = {
    'principal':   '#1a1a1a',   # negro suave
    'secundario':  '#555555',   # gris medio
    'terciario':   '#999999',   # gris claro
    'acento':      '#2c4a6e',   # azul pizarrón (para impresión a color)
    'referencia':  '#aaaaaa',   # líneas de referencia / azar
    'fondo':       '#ffffff',   # fondo blanco
    'secuencia':   [            # hasta 6 series distinguibles en b&n
        '#1a1a1a',
        '#444444',
        '#777777',
        '#999999',
        '#bbbbbb',
        '#dddddd',
    ],
}

# Marcadores estándar para series múltiples (distinguibles en b&n)
MARCADORES = ['o', 's', '^', 'D', 'v', 'x']

# Tipos de línea estándar
LINEAS = ['-', '--', '-.', ':', (0, (3, 1, 1, 1)), (0, (5, 2))]


# ── Función principal ─────────────────────────────────────────────────────────
def aplicar_estilo():
    """
    Aplica el estilo del libro a matplotlib globalmente.
    Llamar una sola vez al inicio de cada script.
    """
    mpl.rcParams.update({
        # Fuente
        'font.family':          'serif',
        'font.serif':           ['Palatino', 'Georgia', 'Times New Roman', 'DejaVu Serif'],
        'font.size':            11,
        'axes.titlesize':       11,
        'axes.labelsize':       11,
        'xtick.labelsize':      10,
        'ytick.labelsize':      10,
        'legend.fontsize':      9,
        'legend.title_fontsize':9,

        # Ejes
        'axes.spines.top':      False,
        'axes.spines.right':    False,
        'axes.linewidth':       0.8,
        'axes.grid':            True,
        'grid.alpha':           0.25,
        'grid.linewidth':       0.5,
        'grid.color':           '#cccccc',
        'axes.facecolor':       '#ffffff',
        'figure.facecolor':     '#ffffff',

        # Ticks
        'xtick.direction':      'out',
        'ytick.direction':      'out',
        'xtick.major.width':    0.8,
        'ytick.major.width':    0.8,
        'xtick.major.size':     4,
        'ytick.major.size':     4,
        'xtick.minor.visible':  False,
        'ytick.minor.visible':  False,

        # Líneas y marcadores
        'lines.linewidth':      2.0,
        'lines.markersize':     6,
        'lines.markeredgewidth':0.8,

        # Leyenda
        'legend.frameon':       True,
        'legend.framealpha':    0.9,
        'legend.edgecolor':     '#cccccc',
        'legend.borderpad':     0.5,

        # Figura
        'figure.dpi':           100,
        'savefig.dpi':          300,
        'savefig.bbox':         'tight',
        'savefig.facecolor':    '#ffffff',

        # Texto matemático
        'mathtext.fontset':     'dejavuserif',
    })


# ── Constructores de figuras ──────────────────────────────────────────────────
def nueva_figura(filas=1, columnas=1, ancho_panel=5.5, alto_panel=4.0):
    """
    Crea una figura con el número de paneles indicado.

    Parámetros
    ----------
    filas, columnas : int
        Disposición de paneles.
    ancho_panel, alto_panel : float
        Tamaño de cada panel en pulgadas.

    Devuelve
    --------
    fig, ax  (si filas==1 y columnas==1)
    fig, axes  (si hay más de un panel; axes es un array de matplotlib)
    """
    aplicar_estilo()
    ancho = columnas * ancho_panel
    alto  = filas * alto_panel
    fig, axes = plt.subplots(filas, columnas, figsize=(ancho, alto))
    if filas == 1 and columnas == 1:
        return fig, axes
    return fig, axes


def guardar_figura(fig, nombre_archivo, directorio='.'):
    """
    Guarda la figura en PNG y PDF con los parámetros del libro.

    Parámetros
    ----------
    fig : Figure de matplotlib
    nombre_archivo : str
        Nombre sin extensión, p. ej. 'figura_7_1_staddon_simmelhag'
    directorio : str
        Carpeta de destino (default: directorio actual)
    """
    import os
    base = os.path.join(directorio, nombre_archivo)
    fig.savefig(base + '.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig(base + '.pdf', bbox_inches='tight', facecolor='white')
    print(f"  → Guardado: {base}.png  /  {base}.pdf")


# ── Utilidades de anotación ───────────────────────────────────────────────────
def anotar_sbi(ax, x, etiqueta='SBI', color=None, orientacion='vertical'):
    """
    Añade una línea vertical punteada para marcar el momento del SBI.

    Parámetros
    ----------
    ax : Axes
    x : float  — posición en el eje x
    etiqueta : str
    color : str  — default: COLORES['referencia']
    orientacion : 'vertical' o 'horizontal'
    """
    c = color or COLORES['referencia']
    if orientacion == 'vertical':
        ax.axvline(x=x, color=c, linestyle=':', linewidth=1.2, alpha=0.8)
        ylim = ax.get_ylim()
        ax.text(x + 0.02 * (ax.get_xlim()[1] - ax.get_xlim()[0]),
                ylim[0] + 0.5 * (ylim[1] - ylim[0]),
                etiqueta, color=c, fontsize=9,
                rotation=90, va='center', ha='left')
    else:
        ax.axhline(y=x, color=c, linestyle=':', linewidth=1.2, alpha=0.8)


def anotar_azar(ax, orientacion='diagonal'):
    """
    Añade línea de azar para gráficas ROC u otras comparaciones.

    orientacion : 'diagonal' dibuja la diagonal [0,1]→[1,1]
                  'horizontal' dibuja una línea horizontal en y=0.5
    """
    if orientacion == 'diagonal':
        ax.plot([0, 1], [0, 1], color=COLORES['referencia'],
                linestyle='--', linewidth=1.2, label='Azar', zorder=0)
    else:
        ax.axhline(y=0.5, color=COLORES['referencia'],
                   linestyle='--', linewidth=1.2, label='Azar', zorder=0)


def pie_de_figura(ax, texto, fuente_datos=None):
    """
    Añade el pie de figura con la fuente de los datos debajo del panel.

    Parámetros
    ----------
    ax : Axes
    texto : str  — descripción de la figura (sin la cita)
    fuente_datos : str  — cita completa de los datos, p. ej.
                  'Datos: Staddon & Simmelhag (1971), Psychological Review, 78, 3–43'
    """
    titulo = texto
    if fuente_datos:
        titulo += f'\n{fuente_datos}'
    ax.set_title(titulo, fontsize=9, loc='left', pad=6,
                 color='#333333', style='italic')


# ── Función de demostración ───────────────────────────────────────────────────
def demo():
    """
    Genera una figura de demostración con los elementos visuales del libro.
    Ejecutar como: python estilo_libro_aca.py
    """
    aplicar_estilo()
    fig, axes = nueva_figura(1, 2)

    t = np.linspace(0, 15, 200)

    # Panel izquierdo: dos series con el estilo estándar
    ax = axes[0]
    serie_a = np.exp(-0.30 * t)
    serie_b = 1 - np.exp(-0.20 * t)
    ax.plot(t, serie_a, color=COLORES['principal'],
            linestyle=LINEAS[1], marker=MARCADORES[0],
            markevery=20, label='Respuestas interinas')
    ax.plot(t, serie_b, color=COLORES['secundario'],
            linestyle=LINEAS[0], marker=MARCADORES[1],
            markevery=20, label='Respuestas terminales')
    anotar_sbi(ax, 0)
    anotar_sbi(ax, 15)
    ax.set_xlabel('Tiempo en el intervalo (seg)')
    ax.set_ylabel('Probabilidad relativa')
    ax.legend()
    ax.set_ylim(0, 1.1)
    pie_de_figura(ax,
        'Distribución temporal de respuestas inducidas',
        'Datos: Staddon & Simmelhag (1971), Psychological Review, 78, 3–43')

    # Panel derecho: curva ROC con línea de azar
    ax2 = axes[1]
    fa   = np.array([0.05, 0.15, 0.35, 0.55, 0.75])
    hit  = np.array([0.55, 0.72, 0.85, 0.92, 0.97])
    anotar_azar(ax2, 'diagonal')
    ax2.plot(fa, hit, color=COLORES['acento'],
             linestyle=LINEAS[0], marker=MARCADORES[2],
             markersize=7, label='Sujeto S1')
    ax2.set_xlabel('P (falsa alarma)')
    ax2.set_ylabel('P (acierto)')
    ax2.set_xlim(0, 1); ax2.set_ylim(0, 1)
    ax2.set_aspect('equal')
    ax2.legend()
    pie_de_figura(ax2,
        'Curva ROC — discriminabilidad de causalidad',
        'Datos: Killeen (1978), Science, 199, 88–90')

    plt.tight_layout()
    guardar_figura(fig, 'demo_estilo_libro_aca')
    plt.show()


if __name__ == '__main__':
    demo()
