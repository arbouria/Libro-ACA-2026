"""
Figuras para el Capítulo 12: Traducción del Conocimiento en Acción
Aprendizaje y Comportamiento Adaptable: Principios y Modelos
Paleta: azul #2C5282, naranja #C05621, verde #276749, gris #718096
Fondo blanco, tipografía serif, estilo académico limpio.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.gridspec import GridSpec
import matplotlib.ticker as ticker
import warnings
warnings.filterwarnings('ignore')

# ── Paleta ──────────────────────────────────────────────────────────────────
AZUL   = '#2C5282'
NARAN  = '#C05621'
VERDE  = '#276749'
GRIS   = '#718096'
GRIS_L = '#E2E8F0'
NEGRO  = '#1A202C'
BLANCO = '#FFFFFF'

def setup_fig(w, h):
    fig = plt.figure(figsize=(w, h), facecolor=BLANCO)
    fig.patch.set_facecolor(BLANCO)
    return fig

def top_bar(fig, color=AZUL, lw=4):
    """Línea delgada azul en el borde superior."""
    fig.add_artist(plt.Line2D([0, 1], [1, 1], transform=fig.transFigure,
                               color=color, linewidth=lw, solid_capstyle='butt'))

def caption(fig, num, texto, y=0.02):
    fig.text(0.5, y, f'Figura {num}. {texto}',
             ha='center', va='bottom', fontsize=8.5,
             fontfamily='serif', color=GRIS,
             wrap=True, transform=fig.transFigure)

def serif(size=10, weight='normal'):
    return {'fontfamily': 'serif', 'fontsize': size, 'fontweight': weight}

# ════════════════════════════════════════════════════════════════════════════
# FIGURA 12.1  Jenkins & Moore — forma de la respuesta condicionada
# ════════════════════════════════════════════════════════════════════════════
def fig_12_1():
    fig = setup_fig(9, 5)
    top_bar(fig)

    # Dos paneles: comida | agua
    ax1 = fig.add_axes([0.06, 0.18, 0.40, 0.68])
    ax2 = fig.add_axes([0.54, 0.18, 0.40, 0.68])

    for ax in [ax1, ax2]:
        ax.set_facecolor(BLANCO)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

    # ── Panel izquierdo: respuesta ante predictor de COMIDA ──
    # Silueta estilizada de cabeza de paloma + golpe seco en tecla
    # Cabeza
    head1 = plt.Circle((3, 6.5), 1.5, color=GRIS_L, zorder=2)
    ax1.add_patch(head1)
    # Pico: orientado horizontalmente, golpe rápido
    ax1.annotate('', xy=(5.2, 6.4), xytext=(4.5, 6.5),
                 arrowprops=dict(arrowstyle='->', color=AZUL, lw=2.2))
    # Tecla
    tecla1 = FancyBboxPatch((5.0, 5.8), 1.2, 1.4, boxstyle="round,pad=0.1",
                              facecolor=AZUL, edgecolor=AZUL, alpha=0.85, zorder=3)
    ax1.add_patch(tecla1)
    ax1.text(5.6, 6.5, '●', ha='center', va='center', fontsize=14,
             color=BLANCO, zorder=4)
    # Etiquetas
    ax1.text(5, 9.3, 'Predictor de comida', ha='center', va='center',
             **serif(11, 'bold'), color=NEGRO)
    ax1.text(5, 8.5, 'Golpe seco y rápido', ha='center', va='center',
             **serif(9), color=GRIS)
    ax1.text(5, 7.9, '(pico abierto, movimiento vertical)', ha='center',
             va='center', **serif(8), color=GRIS, style='italic')

    # Ojo
    ojo1 = plt.Circle((3.8, 7.1), 0.22, color=NEGRO, zorder=5)
    ax1.add_patch(ojo1)

    # Cuerpo esquemático
    cuerpo1 = mpatches.Ellipse((3, 4.5), 2.2, 3.5, angle=10,
                                facecolor=GRIS_L, edgecolor=GRIS, lw=1.2, zorder=1)
    ax1.add_patch(cuerpo1)

    # Flecha de movimiento rápido
    ax1.annotate('', xy=(4.9, 6.3), xytext=(3.5, 5.8),
                 arrowprops=dict(arrowstyle='->', color=NARAN, lw=1.8,
                                 connectionstyle='arc3,rad=-0.2'))
    ax1.text(4.1, 5.2, 'Rápido', ha='center', va='center',
             **serif(8), color=NARAN, style='italic')

    # ── Panel derecho: respuesta ante predictor de AGUA ──
    head2 = plt.Circle((3, 6.5), 1.5, color=GRIS_L, zorder=2)
    ax2.add_patch(head2)

    # Pico: inserción lenta, hacia abajo
    ax2.annotate('', xy=(5.0, 5.9), xytext=(4.4, 6.6),
                 arrowprops=dict(arrowstyle='->', color=AZUL, lw=2.2))

    tecla2 = FancyBboxPatch((5.0, 5.8), 1.2, 1.4, boxstyle="round,pad=0.1",
                              facecolor=AZUL, edgecolor=AZUL, alpha=0.85, zorder=3)
    ax2.add_patch(tecla2)
    ax2.text(5.6, 6.5, '●', ha='center', va='center', fontsize=14,
             color=BLANCO, zorder=4)

    ax2.text(5, 9.3, 'Predictor de agua', ha='center', va='center',
             **serif(11, 'bold'), color=NEGRO)
    ax2.text(5, 8.5, 'Inserción lenta, hacia abajo', ha='center', va='center',
             **serif(9), color=GRIS)
    ax2.text(5, 7.9, '(pico cerrado, movimientos de deglución)', ha='center',
             va='center', **serif(8), color=GRIS, style='italic')

    ojo2 = plt.Circle((3.8, 7.1), 0.22, color=NEGRO, zorder=5)
    ax2.add_patch(ojo2)

    cuerpo2 = mpatches.Ellipse((3, 4.5), 2.2, 3.5, angle=20,
                                facecolor=GRIS_L, edgecolor=GRIS, lw=1.2, zorder=1)
    ax2.add_patch(cuerpo2)

    # Movimientos de deglución (ondas pequeñas)
    x_deg = np.linspace(3.5, 5.0, 40)
    y_deg = 4.5 + 0.18 * np.sin(np.linspace(0, 3*np.pi, 40))
    ax2.plot(x_deg, y_deg, color=VERDE, lw=1.5, alpha=0.8)
    ax2.text(4.2, 4.0, 'Deglución', ha='center', va='center',
             **serif(8), color=VERDE, style='italic')

    # Línea divisoria central
    fig.add_artist(plt.Line2D([0.5, 0.5], [0.15, 0.95],
                               transform=fig.transFigure,
                               color=GRIS_L, linewidth=1.5, linestyle='--'))

    # Título general
    fig.text(0.5, 0.96, 'Forma de la respuesta condicionada según el SBI anticipado',
             ha='center', va='top', **serif(12, 'bold'), color=NEGRO)

    caption(fig, '12.1',
            'La forma de la respuesta condicionada refleja la naturaleza del SBI '
            'anticipado. Ante el predictor de comida, la paloma golpea la tecla '
            'con el pico abierto en movimientos secos y rápidos (izquierda); '
            'ante el predictor de agua, la inserta lentamente con movimientos '
            'de deglución (derecha). Adaptado de Jenkins y Moore (1973).')

    plt.savefig('/home/claude/fig_12_1_jenkins_moore.svg', format='svg',
                bbox_inches='tight', facecolor=BLANCO)
    plt.savefig('/home/claude/fig_12_1_jenkins_moore.png', dpi=180,
                bbox_inches='tight', facecolor=BLANCO)
    plt.close()
    print("✓ Fig 12.1 guardada")


# ════════════════════════════════════════════════════════════════════════════
# FIGURA 12.2  Holland (1977) — cuatro paneles de respuesta condicionada
# ════════════════════════════════════════════════════════════════════════════
def fig_12_2():
    np.random.seed(42)
    fig = setup_fig(10, 7.5)
    top_bar(fig)

    titles = ['Luz difusa', 'Luz localizada', 'Tono A', 'Tono B']
    positions = [(0.06, 0.54), (0.54, 0.54), (0.06, 0.10), (0.54, 0.10)]
    w, h = 0.40, 0.36

    # Sesiones: 5 sin refuerzo + 9 con refuerzo
    ses_pre  = np.arange(1, 6)
    ses_post = np.arange(1, 10)
    ses_all_pre  = ses_pre
    ses_all_post = ses_post + 5

    def smooth(base, noise=0.04):
        return base + np.random.normal(0, noise, len(base))

    # Patrones de respuesta para cada condición
    # [pararse, acercamiento comedero, sobresalto, sacudida]
    patterns = {
        'Luz difusa': {
            'pararse':    (smooth(np.array([0.38,0.35,0.36,0.34,0.37])),
                           smooth(np.array([0.35,0.33,0.30,0.28,0.28,0.27,0.26,0.25,0.24]))),
            'comedero':   (smooth(np.array([0.12,0.14,0.13,0.14,0.13])),
                           smooth(np.array([0.18,0.24,0.30,0.34,0.37,0.39,0.40,0.41,0.42]))),
            'sobresalto': (smooth(np.array([0.08,0.07,0.08,0.07,0.07])),
                           smooth(np.array([0.06,0.06,0.05,0.05,0.05,0.04,0.04,0.04,0.04]))),
            'sacudida':   (smooth(np.array([0.06,0.06,0.05,0.06,0.06])),
                           smooth(np.array([0.05,0.04,0.04,0.03,0.03,0.03,0.03,0.02,0.02]))),
        },
        'Luz localizada': {
            'pararse':    (smooth(np.array([0.42,0.40,0.41,0.39,0.40])),
                           smooth(np.array([0.40,0.44,0.50,0.53,0.55,0.56,0.57,0.57,0.58]))),
            'comedero':   (smooth(np.array([0.10,0.11,0.10,0.11,0.10])),
                           smooth(np.array([0.12,0.16,0.20,0.24,0.27,0.28,0.29,0.30,0.30]))),
            'sobresalto': (smooth(np.array([0.07,0.07,0.08,0.07,0.07])),
                           smooth(np.array([0.05,0.05,0.04,0.04,0.04,0.03,0.03,0.03,0.03]))),
            'sacudida':   (smooth(np.array([0.05,0.06,0.05,0.05,0.06])),
                           smooth(np.array([0.04,0.03,0.03,0.03,0.03,0.02,0.02,0.02,0.02]))),
        },
        'Tono A': {
            'pararse':    (smooth(np.array([0.36,0.35,0.34,0.33,0.35])),
                           smooth(np.array([0.20,0.15,0.10,0.07,0.06,0.05,0.05,0.05,0.04]))),
            'comedero':   (smooth(np.array([0.14,0.13,0.14,0.14,0.13])),
                           smooth(np.array([0.16,0.18,0.20,0.22,0.24,0.25,0.26,0.27,0.27]))),
            'sobresalto': (smooth(np.array([0.10,0.11,0.10,0.09,0.10])),
                           smooth(np.array([0.18,0.30,0.50,0.65,0.75,0.80,0.82,0.83,0.84]))),
            'sacudida':   (smooth(np.array([0.08,0.09,0.08,0.09,0.08])),
                           smooth(np.array([0.12,0.20,0.32,0.42,0.50,0.55,0.58,0.60,0.61]))),
        },
        'Tono B': {
            'pararse':    (smooth(np.array([0.37,0.36,0.35,0.36,0.35])),
                           smooth(np.array([0.18,0.13,0.09,0.06,0.05,0.05,0.04,0.04,0.04]))),
            'comedero':   (smooth(np.array([0.13,0.12,0.13,0.12,0.13])),
                           smooth(np.array([0.15,0.17,0.19,0.21,0.23,0.25,0.26,0.27,0.27]))),
            'sobresalto': (smooth(np.array([0.09,0.10,0.09,0.10,0.09])),
                           smooth(np.array([0.20,0.35,0.55,0.68,0.78,0.82,0.84,0.85,0.86]))),
            'sacudida':   (smooth(np.array([0.07,0.08,0.07,0.08,0.07])),
                           smooth(np.array([0.10,0.18,0.30,0.40,0.48,0.53,0.56,0.58,0.60]))),
        },
    }

    markers  = ['s', 'o', '*', 'o']
    colors   = [AZUL, VERDE, NARAN, GRIS]
    labels   = ['Pararse', 'Acercamiento\ncomedero', 'Sobresalto', 'Sacudida\ncabeza']
    lstyles  = ['-', '-', ':', '--']
    mksizes  = [5, 5, 7, 4]
    keys     = ['pararse', 'comedero', 'sobresalto', 'sacudida']

    for idx, (title, (lx, ly)) in enumerate(zip(titles, positions)):
        ax = fig.add_axes([lx, ly, w, h])
        ax.set_facecolor(BLANCO)
        pat = patterns[title]

        for ki, key in enumerate(keys):
            pre, post = pat[key]
            pre  = np.clip(pre, 0, 1)
            post = np.clip(post, 0, 1)
            ax.plot(ses_all_pre, pre,
                    color=colors[ki], ls=lstyles[ki],
                    marker=markers[ki], ms=mksizes[ki], lw=1.4, alpha=0.9)
            ax.plot(ses_all_post, post,
                    color=colors[ki], ls=lstyles[ki],
                    marker=markers[ki], ms=mksizes[ki], lw=1.4, alpha=0.9)

        # Línea divisoria pre/post
        ax.axvline(x=5.5, color=GRIS, lw=1, ls='--', alpha=0.6)
        ax.text(2.5, 0.92, 'Sin refuerzo', ha='center', va='top',
                **serif(7.5), color=GRIS, style='italic')
        ax.text(9.8, 0.92, 'Con refuerzo', ha='center', va='top',
                **serif(7.5), color=GRIS, style='italic')

        ax.set_xlim(0.5, 14.5)
        ax.set_ylim(0, 1.0)
        ax.set_title(title, **serif(10, 'bold'), color=NEGRO, pad=4)
        ax.set_xlabel('Sesiones', **serif(8.5), color=GRIS)
        ax.set_ylabel('% tiempo en cada respuesta', **serif(8.5), color=GRIS)
        ax.tick_params(labelsize=7.5, colors=GRIS)
        ax.spines[['top','right']].set_visible(False)
        ax.spines[['bottom','left']].set_color(GRIS_L)
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))

        # Xticks: 1-5 pre, luego 1-9 post → mostramos 1,3,5 | 2,4,6,8,9
        ax.set_xticks([1,3,5, 7,9,11,13,14])
        ax.set_xticklabels(['1','3','5','2','4','6','8','9'], fontsize=7)

    # Leyenda compartida abajo
    handles = [plt.Line2D([0],[0], color=colors[i], ls=lstyles[i],
                           marker=markers[i], ms=mksizes[i], lw=1.4,
                           label=labels[i])
               for i in range(4)]
    fig.legend(handles=handles, loc='lower center', ncol=4,
               frameon=False, fontsize=8.5,
               bbox_to_anchor=(0.5, 0.01),
               prop={'family': 'serif', 'size': 8.5})

    fig.text(0.5, 0.97,
             'Respuestas condicionadas ante cuatro tipos de estímulos predictores (Holland, 1977)',
             ha='center', va='top', **serif(11, 'bold'), color=NEGRO)

    caption(fig, '12.2',
            'Porcentaje de tiempo en cada tipo de respuesta ante cuatro estímulos '
            'predictores de comida. Los tonos (paneles inferiores) producen '
            'predominantemente sobresalto y sacudidas de cabeza; las luces (paneles '
            'superiores) producen pararse y acercamiento al comedero. '
            'La línea discontinua vertical separa las sesiones sin refuerzo de las '
            'sesiones con refuerzo. Basado en Holland (1977).')

    plt.savefig('/home/claude/fig_12_2_holland.svg', format='svg',
                bbox_inches='tight', facecolor=BLANCO)
    plt.savefig('/home/claude/fig_12_2_holland.png', dpi=180,
                bbox_inches='tight', facecolor=BLANCO)
    plt.close()
    print("✓ Fig 12.2 guardada")


# ════════════════════════════════════════════════════════════════════════════
# FIGURA 12.3  Automoldeamiento y procedimiento de omisión
# ════════════════════════════════════════════════════════════════════════════
def fig_12_3():
    np.random.seed(7)
    fig = setup_fig(10, 6.5)
    top_bar(fig)

    # ── Panel superior izquierdo: diagrama contingencia ESTÁNDAR ──
    ax_std = fig.add_axes([0.05, 0.55, 0.38, 0.36])
    ax_std.set_xlim(0, 10); ax_std.set_ylim(0, 10); ax_std.axis('off')

    # Título
    ax_std.text(5, 9.6, 'Procedimiento estándar',
                ha='center', va='center', **serif(10, 'bold'), color=NEGRO)

    # Tecla iluminada
    tecla = FancyBboxPatch((1, 6.5), 2, 2, boxstyle="round,pad=0.2",
                            facecolor=AZUL, edgecolor=AZUL, alpha=0.8)
    ax_std.add_patch(tecla)
    ax_std.text(2, 7.5, 'Tecla\niluminada', ha='center', va='center',
                **serif(9), color=BLANCO)

    # Flecha: tecla → comida (independiente de picar)
    ax_std.annotate('', xy=(8.2, 7.5), xytext=(3.2, 7.5),
                    arrowprops=dict(arrowstyle='->', color=VERDE, lw=2))
    ax_std.text(5.7, 8.0, 'independiente\nde la respuesta', ha='center',
                va='center', **serif(8), color=VERDE, style='italic')

    # Comida
    food = FancyBboxPatch((7, 6.5), 2, 2, boxstyle="round,pad=0.2",
                           facecolor=VERDE, edgecolor=VERDE, alpha=0.75)
    ax_std.add_patch(food)
    ax_std.text(8, 7.5, 'Comida', ha='center', va='center',
                **serif(9), color=BLANCO)

    # Respuesta de picar (aparece de todos modos)
    ax_std.text(5, 5.5, '→ la paloma pica la tecla', ha='center',
                va='center', **serif(9), color=AZUL)
    ax_std.text(5, 4.8, '(sin que nadie la entrene a hacerlo)', ha='center',
                va='center', **serif(8), color=GRIS, style='italic')

    # ── Panel superior derecho: diagrama contingencia OMISIÓN ──
    ax_om = fig.add_axes([0.55, 0.55, 0.38, 0.36])
    ax_om.set_xlim(0, 10); ax_om.set_ylim(0, 10); ax_om.axis('off')

    ax_om.text(5, 9.6, 'Procedimiento de omisión',
               ha='center', va='center', **serif(10, 'bold'), color=NEGRO)

    tecla2 = FancyBboxPatch((1, 6.5), 2, 2, boxstyle="round,pad=0.2",
                             facecolor=AZUL, edgecolor=AZUL, alpha=0.8)
    ax_om.add_patch(tecla2)
    ax_om.text(2, 7.5, 'Tecla\niluminada', ha='center', va='center',
               **serif(9), color=BLANCO)

    # Flecha: picar → no comida
    ax_om.annotate('', xy=(8.2, 8.3), xytext=(3.2, 7.8),
                   arrowprops=dict(arrowstyle='->', color=NARAN, lw=2))
    ax_om.text(5.8, 8.8, 'si pica → sin comida', ha='center',
               va='center', **serif(8), color=NARAN)

    # Flecha: no picar → comida
    ax_om.annotate('', xy=(8.2, 6.8), xytext=(3.2, 7.2),
                   arrowprops=dict(arrowstyle='->', color=VERDE, lw=2))
    ax_om.text(5.8, 6.2, 'si no pica → comida', ha='center',
               va='center', **serif(8), color=VERDE)

    food2 = FancyBboxPatch((7, 6.5), 2, 2, boxstyle="round,pad=0.2",
                            facecolor=VERDE, edgecolor=VERDE, alpha=0.75)
    ax_om.add_patch(food2)
    ax_om.text(8, 7.5, 'Comida', ha='center', va='center',
               **serif(9), color=BLANCO)

    ax_om.text(5, 5.5, '→ la paloma sigue picando', ha='center',
               va='center', **serif(9), color=AZUL)
    ax_om.text(5, 4.8, '(aunque eso le cuesta la comida)', ha='center',
               va='center', **serif(8), color=GRIS, style='italic')

    # ── Panel inferior: tasa de respuesta a lo largo de sesiones ──
    ax_data = fig.add_axes([0.12, 0.08, 0.76, 0.38])
    ax_data.set_facecolor(BLANCO)

    sesiones = np.arange(1, 21)

    # Estándar: adquisición normal
    tasa_std = 40 * (1 - np.exp(-0.28 * sesiones)) + np.random.normal(0, 1.5, 20)
    tasa_std = np.clip(tasa_std, 0, 50)

    # Omisión: adquisición parcial, persiste por encima de cero
    tasa_om  = 22 * (1 - np.exp(-0.20 * sesiones)) + np.random.normal(0, 1.5, 20)
    tasa_om  = np.clip(tasa_om, 0, 50)

    ax_data.plot(sesiones, tasa_std, color=AZUL, lw=2.2, marker='s', ms=5,
                 label='Procedimiento estándar')
    ax_data.plot(sesiones, tasa_om,  color=NARAN, lw=2.2, marker='o', ms=5,
                 ls='--', label='Procedimiento de omisión')
    ax_data.axhline(y=2, color=GRIS, lw=1.2, ls=':', alpha=0.7)
    ax_data.text(20.3, 2.5, 'línea base', ha='left', va='center',
                 **serif(8), color=GRIS, style='italic')

    ax_data.set_xlabel('Sesiones', **serif(9.5), color=GRIS)
    ax_data.set_ylabel('Picotazos / min', **serif(9.5), color=GRIS)
    ax_data.set_xlim(0.5, 21)
    ax_data.set_ylim(-1, 55)
    ax_data.spines[['top','right']].set_visible(False)
    ax_data.spines[['bottom','left']].set_color(GRIS_L)
    ax_data.tick_params(colors=GRIS, labelsize=8.5)
    ax_data.legend(frameon=False, prop={'family':'serif','size':8.5},
                   loc='upper left')

    fig.text(0.5, 0.98,
             'Automoldeamiento: procedimiento estándar y procedimiento de omisión',
             ha='center', va='top', **serif(11, 'bold'), color=NEGRO)

    caption(fig, '12.3',
            'Paneles superiores: contingencias en cada procedimiento. En el estándar, '
            'la comida se entrega independientemente de si la paloma pica o no. '
            'En el de omisión, picar la tecla cancela la entrega de comida. '
            'Panel inferior: tasa de picotazos a lo largo de sesiones en ambas condiciones. '
            'En el procedimiento de omisión la tasa es menor pero persiste muy '
            'por encima de la línea base, demostrando que la respuesta no está '
            'mantenida por sus consecuencias positivas. Basado en Williams y Williams (1969).')

    plt.savefig('/home/claude/fig_12_3_autoshaping.svg', format='svg',
                bbox_inches='tight', facecolor=BLANCO)
    plt.savefig('/home/claude/fig_12_3_autoshaping.png', dpi=180,
                bbox_inches='tight', facecolor=BLANCO)
    plt.close()
    print("✓ Fig 12.3 guardada")


# ════════════════════════════════════════════════════════════════════════════
# FIGURA 12.4  Timberlake — jerarquía de sistemas de comportamiento
# ════════════════════════════════════════════════════════════════════════════
def fig_12_4():
    fig = setup_fig(11, 7)
    top_bar(fig)
    ax = fig.add_axes([0.02, 0.08, 0.96, 0.84])
    ax.set_xlim(0, 22); ax.set_ylim(0, 12); ax.axis('off')
    ax.set_facecolor(BLANCO)

    def box(ax, x, y, w, h, label, sublabel=None,
            fc=AZUL, ec=AZUL, fontc=BLANCO, fs=9.5):
        rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                               boxstyle="round,pad=0.15",
                               facecolor=fc, edgecolor=ec, lw=1.5, zorder=3)
        ax.add_patch(rect)
        ax.text(x, y + (0.25 if sublabel else 0), label,
                ha='center', va='center', fontsize=fs,
                fontfamily='serif', fontweight='bold', color=fontc, zorder=4)
        if sublabel:
            ax.text(x, y - 0.4, sublabel, ha='center', va='center',
                    fontsize=fs-1.5, fontfamily='serif',
                    color=fontc, style='italic', zorder=4)

    def arrow(ax, x1, y1, x2, y2, color=GRIS, lw=1.5):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color,
                                    lw=lw, connectionstyle='arc3,rad=0.0'),
                    zorder=2)

    def col_header(ax, x, y, text):
        ax.text(x, y, text, ha='center', va='center',
                fontsize=10, fontfamily='serif', fontweight='bold',
                color=NEGRO, style='italic')
        ax.plot([x-1.5, x+1.5], [y-0.4, y-0.4], color=AZUL, lw=1.5)

    # ── Encabezados de columna ──
    col_header(ax,  2.0, 11.3, 'SUBSISTEMA')
    col_header(ax,  6.5, 11.3, 'MODO')
    col_header(ax, 12.0, 11.3, 'MÓDULO')
    col_header(ax, 18.5, 11.3, 'ACCIÓN')

    # ── Subsistema ──
    box(ax, 2.0, 6.0, 3.2, 1.8, 'Depredación',
        sublabel='(sistema de\nalimentación)',
        fc=AZUL, fontc=BLANCO, fs=10)

    # ── Modos ──
    modos = [
        (6.5, 9.5, 'Búsqueda\ngeneral'),
        (6.5, 6.0, 'Búsqueda\nfocalizada'),
        (6.5, 2.5, 'Manipulación\ny consumo'),
    ]
    for (mx, my, ml) in modos:
        box(ax, mx, my, 3.0, 1.5, ml,
            fc=VERDE, ec=VERDE, fontc=BLANCO, fs=9)
        arrow(ax, 3.6, 6.0, 5.0, my, color=AZUL, lw=1.8)

    # Flechas entre modos (transiciones)
    ax.annotate('', xy=(6.5, 7.5), xytext=(6.5, 8.75),
                arrowprops=dict(arrowstyle='<->', color=GRIS, lw=1.2), zorder=2)
    ax.annotate('', xy=(6.5, 4.0), xytext=(6.5, 5.25),
                arrowprops=dict(arrowstyle='<->', color=GRIS, lw=1.2), zorder=2)

    # ── Módulos ──
    modulos = [
        # modo búsqueda general
        (12.0, 10.4, 'Viajar',   NARAN, 9.5),
        (12.0,  8.8, 'Socializar', NARAN, 9.5),
        # modo búsqueda focalizada
        (12.0,  6.9, 'Perseguir', NARAN, 9.5),
        (12.0,  5.3, 'Capturar',  NARAN, 9.5),
        # modo manipulación
        (12.0,  3.5, 'Probar /\nSostener', NARAN, 9),
        (12.0,  1.8, 'Ingerir',  NARAN, 9.5),
    ]
    for (mx, my, ml, mc, mfs) in modulos:
        box(ax, mx, my, 2.8, 1.1, ml, fc=mc, ec=mc, fontc=BLANCO, fs=mfs)

    # Flechas modo → módulos
    arrow(ax, 8.0, 9.5,  10.6, 10.4, color=VERDE)
    arrow(ax, 8.0, 9.5,  10.6,  8.8, color=VERDE)
    arrow(ax, 8.0, 6.0,  10.6,  6.9, color=VERDE)
    arrow(ax, 8.0, 6.0,  10.6,  5.3, color=VERDE)
    arrow(ax, 8.0, 2.5,  10.6,  3.5, color=VERDE)
    arrow(ax, 8.0, 2.5,  10.6,  1.8, color=VERDE)

    # ── Acciones ──
    acciones = [
        (18.5, 10.4, 'Locomoción / Explorar'),
        (18.5,  8.8, 'Rastrear / Olfatear'),
        (18.5,  6.9, 'Perseguir / Cortar'),
        (18.5,  5.3, 'Atrapar / Morder'),
        (18.5,  3.5, 'Sostener / Masticar'),
        (18.5,  1.8, 'Tragar / Rechazar'),
    ]
    for (ax2x, ax2y, label) in acciones:
        box(ax, ax2x, ax2y, 4.2, 0.9, label,
            fc=GRIS_L, ec=GRIS, fontc=NEGRO, fs=8.5)

    # Flechas módulo → acción
    pairs = [(10.4+1.4, y_m, 16.4, y_a)
             for (_, y_m, _, _, _), (_, y_a, _)
             in zip(modulos, acciones)]
    for (x1,y1,x2,y2) in pairs:
        arrow(ax, x1, y1, x2, y2, color=NARAN, lw=1.4)

    # Líneas verticales separadoras
    for xv in [4.0, 8.5, 14.5]:
        ax.plot([xv, xv], [0.5, 11.0], color=GRIS_L, lw=1, ls='--', zorder=1)

    # Ejemplo temporal (anotación)
    ax.annotate('Intervalo largo\n→ modo focalizado\n(balín como presa)',
                xy=(8.5, 6.0), xytext=(9.6, 4.0),
                fontsize=7.5, fontfamily='serif', color=GRIS, style='italic',
                arrowprops=dict(arrowstyle='->', color=GRIS, lw=0.9))

    fig.text(0.5, 0.98,
             'Jerarquía de sistemas de comportamiento (Timberlake, 1994)',
             ha='center', va='top', **serif(11, 'bold'), color=NEGRO)

    caption(fig, '12.4',
            'Representación jerárquica del subsistema de depredación del sistema '
            'de alimentación de la rata. Los modos motivacionales (búsqueda general, '
            'focalizada, manipulación-consumo) organizan la conducta temporal y '
            'secuencialmente. Los módulos integran filtros perceptuales y programas '
            'motores que dan lugar a patrones de acción específicos. '
            'Un estímulo predictor activa el modo que corresponde a su posición '
            'temporal relativa al SBI. Adaptado de Timberlake (1994).')

    plt.savefig('/home/claude/fig_12_4_timberlake.svg', format='svg',
                bbox_inches='tight', facecolor=BLANCO)
    plt.savefig('/home/claude/fig_12_4_timberlake.png', dpi=180,
                bbox_inches='tight', facecolor=BLANCO)
    plt.close()
    print("✓ Fig 12.4 guardada")


# ── Ejecutar ─────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    fig_12_1()
    fig_12_2()
    fig_12_3()
    fig_12_4()
    print("\nTodas las figuras generadas.")
