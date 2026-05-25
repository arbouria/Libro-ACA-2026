"""
Figuras 12.2, 12.3 y 12.4 — Capítulo 12
Aprendizaje y Comportamiento Adaptable: Principios y Modelos
Estilo unificado:
  - Paleta: azul #2C5282, naranja #C05621, verde #276749, gris #718096
  - Fondo blanco; línea delgada azul en borde superior
  - Tipografía serif; fuente mínima 10pt en todo elemento del gráfico
  - Caption izquierda, fuente 9pt, "Figura X.X." en negrita
  - PNG 180 dpi + SVG
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
import warnings
warnings.filterwarnings('ignore')

matplotlib.rcParams.update({
    'font.family': 'serif',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.edgecolor': '#718096',
    'xtick.color': '#718096',
    'ytick.color': '#718096',
    'axes.labelcolor': '#718096',
    'text.color': '#1A202C',
})

AZUL  = '#2C5282'
NARAN = '#C05621'
VERDE = '#276749'
GRIS  = '#718096'
GRIS_L= '#E2E8F0'
NEGRO = '#1A202C'
BLANCO= '#FFFFFF'

AZUL_L = '#EBF4FF'
NARAN_L= '#FFF3E8'
VERDE_L= '#EBF7F0'

def top_rule(fig, lw=4):
    fig.add_artist(
        plt.Line2D([0, 1], [1, 1], transform=fig.transFigure,
                   color=AZUL, linewidth=lw, solid_capstyle='butt'))

def add_caption(fig, num, text, y=0.015):
    """Caption left-aligned; 'Figura X.X.' in bold."""
    fig.text(0.04, y,
             f'Figura {num}.\u2002{text}',
             ha='left', va='bottom', fontsize=9,
             fontstyle='normal', color=GRIS,
             transform=fig.transFigure,
             wrap=True)

def save(fig, stem):
    for ext, kw in [('.png', dict(dpi=180)), ('.svg', dict(format='svg'))]:
        fig.savefig(f'/home/claude/{stem}{ext}',
                    bbox_inches='tight', facecolor=BLANCO, **kw)
    plt.close(fig)
    print(f'✓ {stem}')


# ══════════════════════════════════════════════════════════════════════════════
# FIGURA 12.2 — Holland (1977)   4 paneles independientes
# ══════════════════════════════════════════════════════════════════════════════
def fig_12_2():
    np.random.seed(42)

    # --- datos simulados (misma lógica que antes) ---
    def sm(arr, sd=0.035):
        return np.clip(np.array(arr, float) + np.random.normal(0, sd, len(arr)), 0, 1)

    pre  = np.arange(1, 6)   # sesiones 1-5 sin refuerzo
    post = np.arange(1, 10)  # sesiones 1-9 con refuerzo

    patterns = {
        'Luz difusa': {
            'pararse':    (sm([.38,.35,.36,.34,.37]), sm([.35,.33,.30,.28,.28,.27,.26,.25,.24])),
            'comedero':   (sm([.12,.14,.13,.14,.13]), sm([.18,.24,.30,.34,.37,.39,.40,.41,.42])),
            'sobresalto': (sm([.08,.07,.08,.07,.07]), sm([.06,.06,.05,.05,.05,.04,.04,.04,.04])),
            'sacudida':   (sm([.06,.06,.05,.06,.06]), sm([.05,.04,.04,.03,.03,.03,.03,.02,.02])),
        },
        'Luz localizada': {
            'pararse':    (sm([.42,.40,.41,.39,.40]), sm([.40,.44,.50,.53,.55,.56,.57,.57,.58])),
            'comedero':   (sm([.10,.11,.10,.11,.10]), sm([.12,.16,.20,.24,.27,.28,.29,.30,.30])),
            'sobresalto': (sm([.07,.07,.08,.07,.07]), sm([.05,.05,.04,.04,.04,.03,.03,.03,.03])),
            'sacudida':   (sm([.05,.06,.05,.05,.06]), sm([.04,.03,.03,.03,.03,.02,.02,.02,.02])),
        },
        'Tono A': {
            'pararse':    (sm([.36,.35,.34,.33,.35]), sm([.20,.15,.10,.07,.06,.05,.05,.05,.04])),
            'comedero':   (sm([.14,.13,.14,.14,.13]), sm([.16,.18,.20,.22,.24,.25,.26,.27,.27])),
            'sobresalto': (sm([.10,.11,.10,.09,.10]), sm([.18,.30,.50,.65,.75,.80,.82,.83,.84])),
            'sacudida':   (sm([.08,.09,.08,.09,.08]), sm([.12,.20,.32,.42,.50,.55,.58,.60,.61])),
        },
        'Tono B': {
            'pararse':    (sm([.37,.36,.35,.36,.35]), sm([.18,.13,.09,.06,.05,.05,.04,.04,.04])),
            'comedero':   (sm([.13,.12,.13,.12,.13]), sm([.15,.17,.19,.21,.23,.25,.26,.27,.27])),
            'sobresalto': (sm([.09,.10,.09,.10,.09]), sm([.20,.35,.55,.68,.78,.82,.84,.85,.86])),
            'sacudida':   (sm([.07,.08,.07,.08,.07]), sm([.10,.18,.30,.40,.48,.53,.56,.58,.60])),
        },
    }

    colors  = [AZUL, VERDE, NARAN, GRIS]
    markers = ['s', 'o', '*', 'D']
    mksizes = [6, 6, 8, 5]
    lstyles = ['-', '-', ':', '--']
    labels  = ['Pararse', 'Acercamiento al comedero', 'Sobresalto', 'Sacudida de cabeza']
    keys    = ['pararse', 'comedero', 'sobresalto', 'sacudida']

    # Figure: 2×2 grid with generous size
    fig, axes = plt.subplots(2, 2, figsize=(13, 9),
                              facecolor=BLANCO,
                              gridspec_kw=dict(hspace=0.45, wspace=0.32))
    fig.patch.set_facecolor(BLANCO)
    top_rule(fig)

    titles = ['Luz difusa', 'Luz localizada', 'Tono A', 'Tono B']
    ax_flat = axes.flatten()

    for idx, (title, ax) in enumerate(zip(titles, ax_flat)):
        pat = patterns[title]
        ax.set_facecolor(BLANCO)

        for ki, key in enumerate(keys):
            yp, ypost = pat[key]
            # Pre: sesiones 1-5
            ax.plot(pre, yp,
                    color=colors[ki], ls=lstyles[ki],
                    marker=markers[ki], ms=mksizes[ki], lw=1.8, alpha=0.95,
                    clip_on=False)
            # Post: sesiones 7-15 (gap visual de 1 unidad = fase break)
            ax.plot(post + 6, ypost,
                    color=colors[ki], ls=lstyles[ki],
                    marker=markers[ki], ms=mksizes[ki], lw=1.8, alpha=0.95,
                    clip_on=False)

        # Línea de fase
        ax.axvline(x=5.8, color=GRIS, lw=1.2, ls='--', alpha=0.55, zorder=1)

        # Anotaciones de fase
        ax.text(3.0, 1.03, 'Sin refuerzo', ha='center', va='bottom',
                fontsize=9.5, color=GRIS, style='italic',
                transform=ax.get_xaxis_transform())
        ax.text(10.5, 1.03, 'Con refuerzo', ha='center', va='bottom',
                fontsize=9.5, color=GRIS, style='italic',
                transform=ax.get_xaxis_transform())

        ax.set_xlim(0.2, 15.8)
        ax.set_ylim(0, 1.0)
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
        ax.set_yticks([0, .25, .50, .75, 1.0])
        ax.tick_params(labelsize=10)

        # X ticks: 1 3 5 | 1 3 5 7 9
        xt_vals = [1, 3, 5, 7, 9, 11, 13, 15]
        xt_labs = ['1', '3', '5', '1', '3', '5', '7', '9']
        ax.set_xticks(xt_vals)
        ax.set_xticklabels(xt_labs, fontsize=10)

        ax.set_title(title, fontsize=12, fontweight='bold',
                     color=NEGRO, pad=8)
        ax.set_xlabel('Sesiones', fontsize=10.5, color=GRIS)
        ax.set_ylabel('% tiempo en cada respuesta', fontsize=10.5, color=GRIS)
        ax.spines['bottom'].set_color(GRIS_L)
        ax.spines['left'].set_color(GRIS_L)

    # Leyenda compartida bajo los paneles
    handles = [plt.Line2D([0], [0], color=colors[i], ls=lstyles[i],
                           marker=markers[i], ms=mksizes[i], lw=1.8,
                           label=labels[i])
               for i in range(4)]
    fig.legend(handles=handles, loc='lower center', ncol=4,
               frameon=False, fontsize=10.5,
               bbox_to_anchor=(0.5, 0.065),
               prop=dict(size=10.5))

    fig.suptitle(
        'Respuestas condicionadas ante cuatro estímulos predictores (Holland, 1977)',
        fontsize=13, fontweight='bold', color=NEGRO, y=0.97)

    fig.subplots_adjust(bottom=0.14)

    cap = ('Porcentaje de tiempo en cada categoría de respuesta durante ensayos con cuatro '
           'tipos de estímulos predictores de comida (Holland, 1977). Los tonos (paneles '
           'inferiores) producen predominantemente sobresalto y sacudidas de cabeza; las luces '
           '(paneles superiores), pararse y acercamiento al comedero. La línea discontinua '
           'vertical separa la fase sin refuerzo (sesiones 1–5) de la fase con refuerzo '
           '(sesiones 1–9 de la segunda fase). Basado en Holland (1977).')
    add_caption(fig, '12.2', cap, y=0.005)

    save(fig, 'fig_12_2_holland')


# ══════════════════════════════════════════════════════════════════════════════
# FIGURA 12.3 — Automoldeamiento y procedimiento de omisión
# ══════════════════════════════════════════════════════════════════════════════
def fig_12_3():
    np.random.seed(7)
    fig = plt.figure(figsize=(12, 9), facecolor=BLANCO)
    fig.patch.set_facecolor(BLANCO)
    top_rule(fig)

    # Layout: 2 paneles de diagrama arriba (izq/der), 1 panel de datos abajo
    ax_std = fig.add_axes([0.06, 0.56, 0.38, 0.34])
    ax_om  = fig.add_axes([0.56, 0.56, 0.38, 0.34])
    ax_dat = fig.add_axes([0.10, 0.16, 0.80, 0.33])

    for ax in [ax_std, ax_om]:
        ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
        ax.set_facecolor(BLANCO)

    def box(ax, cx, cy, w, h, txt, fc, ec, tc=BLANCO, fs=11):
        r = mpatches.FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                                     boxstyle='round,pad=0.18',
                                     facecolor=fc, edgecolor=ec, lw=1.8, zorder=3)
        ax.add_patch(r)
        ax.text(cx, cy, txt, ha='center', va='center',
                fontsize=fs, fontweight='bold', color=tc, zorder=4,
                multialignment='center')

    def arr(ax, x1, y1, x2, y2, col, label='', lside='top'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=col, lw=2.2), zorder=2)
        if label:
            mx, my = (x1+x2)/2, (y1+y2)/2
            dy = 0.45 if lside == 'top' else -0.45
            ax.text(mx, my+dy, label, ha='center', va='center',
                    fontsize=9.5, color=col, style='italic', zorder=5)

    # ── Panel estándar ──
    ax_std.text(5, 9.3, 'Procedimiento estándar',
                ha='center', va='center', fontsize=12, fontweight='bold', color=NEGRO)
    box(ax_std, 2, 6.5, 3.0, 1.8, 'Tecla\niluminada', AZUL, AZUL)
    box(ax_std, 8, 6.5, 2.8, 1.8, 'Comida', VERDE, VERDE)
    arr(ax_std, 3.5, 6.5, 6.6, 6.5, VERDE, 'independiente\nde la respuesta')
    ax_std.text(5, 4.4, '→ la paloma pica la tecla',
                ha='center', va='center', fontsize=11, color=AZUL, fontweight='bold')
    ax_std.text(5, 3.5, '(sin entrenamiento explícito)',
                ha='center', va='center', fontsize=10, color=GRIS, style='italic')

    # ── Panel omisión ──
    ax_om.text(5, 9.3, 'Procedimiento de omisión',
               ha='center', va='center', fontsize=12, fontweight='bold', color=NEGRO)
    box(ax_om, 2, 6.5, 3.0, 1.8, 'Tecla\niluminada', AZUL, AZUL)
    box(ax_om, 8, 6.5, 2.8, 1.8, 'Comida', VERDE, VERDE)
    # Flecha superior: picar → sin comida
    arr(ax_om, 3.5, 7.2, 6.6, 7.6, NARAN, 'pica → sin comida', 'top')
    # Flecha inferior: no picar → comida
    arr(ax_om, 3.5, 5.8, 6.6, 5.4, VERDE, 'no pica → comida', 'top')
    ax_om.text(5, 4.4, '→ la paloma sigue picando',
               ha='center', va='center', fontsize=11, color=AZUL, fontweight='bold')
    ax_om.text(5, 3.5, '(aunque eso le cuesta la comida)',
               ha='center', va='center', fontsize=10, color=GRIS, style='italic')

    # ── Panel de datos ──
    sesiones = np.arange(1, 21)
    tasa_std = np.clip(40*(1-np.exp(-0.28*sesiones)) + np.random.normal(0, 1.5, 20), 0, 55)
    tasa_om  = np.clip(22*(1-np.exp(-0.20*sesiones)) + np.random.normal(0, 1.5, 20), 0, 55)

    ax_dat.set_facecolor(BLANCO)
    ax_dat.plot(sesiones, tasa_std, color=AZUL, lw=2.2,
                marker='s', ms=6, label='Procedimiento estándar')
    ax_dat.plot(sesiones, tasa_om,  color=NARAN, lw=2.2, ls='--',
                marker='o', ms=6, label='Procedimiento de omisión')
    ax_dat.axhline(y=2, color=GRIS, lw=1.2, ls=':', alpha=0.7)
    ax_dat.text(20.4, 2.8, 'línea base', ha='left', va='center',
                fontsize=9.5, color=GRIS, style='italic')

    ax_dat.set_xlim(0.5, 21)
    ax_dat.set_ylim(-1, 57)
    ax_dat.set_xlabel('Sesiones', fontsize=11, color=GRIS)
    ax_dat.set_ylabel('Picotazos / min', fontsize=11, color=GRIS)
    ax_dat.tick_params(labelsize=10.5)
    ax_dat.spines['bottom'].set_color(GRIS_L)
    ax_dat.spines['left'].set_color(GRIS_L)
    ax_dat.legend(frameon=False, fontsize=11, loc='upper left',
                  prop=dict(size=11))

    fig.suptitle('Automoldeamiento: procedimiento estándar y procedimiento de omisión',
                 fontsize=13, fontweight='bold', color=NEGRO, y=0.97)

    cap = ('Paneles superiores: contingencias en cada procedimiento. En el estándar la comida se '
           'entrega al apagarse la tecla independientemente de si la paloma pica. En el de omisión '
           'picar la tecla cancela la entrega de comida en ese ensayo. Panel inferior: tasa de '
           'picotazos a lo largo de sesiones en ambos procedimientos. En el de omisión la tasa '
           'es menor pero persiste muy por encima de la línea base, demostrando que la respuesta '
           'no está mantenida por sus consecuencias positivas. Basado en Williams y Williams (1969).')
    add_caption(fig, '12.3', cap, y=0.005)

    save(fig, 'fig_12_3_autoshaping')


# ══════════════════════════════════════════════════════════════════════════════
# FIGURA 12.4 — Timberlake: jerarquía de sistemas de comportamiento
# ══════════════════════════════════════════════════════════════════════════════
def fig_12_4():
    fig = plt.figure(figsize=(14, 8.5), facecolor=BLANCO)
    fig.patch.set_facecolor(BLANCO)
    top_rule(fig)

    ax = fig.add_axes([0.01, 0.12, 0.97, 0.80])
    ax.set_xlim(0, 24); ax.set_ylim(0, 13); ax.axis('off')
    ax.set_facecolor(BLANCO)

    # ── Helpers ──
    def rect(cx, cy, w, h, label, fc, ec, tc=BLANCO, fs=10.5, bold=True):
        r = mpatches.FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                                     boxstyle='round,pad=0.2',
                                     facecolor=fc, edgecolor=ec, lw=1.8, zorder=3)
        ax.add_patch(r)
        ax.text(cx, cy, label, ha='center', va='center',
                fontsize=fs, fontweight='bold' if bold else 'normal',
                color=tc, zorder=4, multialignment='center')

    def arrow(x1, y1, x2, y2, col=GRIS, lw=1.6):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=col, lw=lw), zorder=2)

    def col_header(cx, cy, txt):
        ax.text(cx, cy, txt, ha='center', va='center',
                fontsize=11.5, fontweight='bold', color=NEGRO, style='italic')
        ax.plot([cx-2.0, cx+2.0], [cy-0.42, cy-0.42], color=AZUL, lw=1.8)

    # ── Encabezados ──
    col_header(2.5,  12.3, 'SUBSISTEMA')
    col_header(7.2,  12.3, 'MODO')
    col_header(13.5, 12.3, 'MÓDULO')
    col_header(20.5, 12.3, 'ACCIÓN')

    # Separadores verticales
    for xv in [4.8, 9.8, 17.0]:
        ax.plot([xv, xv], [0.6, 11.8], color=GRIS_L, lw=1.2, ls='--', zorder=1)

    # ── Subsistema ──
    rect(2.5, 6.3, 4.2, 2.2, 'Depredación\n(subsistema\nde alimentación)',
         AZUL, AZUL, fs=10.5)

    # ── Modos ──
    modos = [(7.2, 10.2, 'Búsqueda\ngeneral'),
             (7.2,  6.3, 'Búsqueda\nfocalizada'),
             (7.2,  2.4, 'Manipulación\ny consumo')]
    for mx, my, ml in modos:
        rect(mx, my, 4.0, 1.6, ml, VERDE, VERDE, fs=10.5)
        arrow(4.6, 6.3, 5.2, my, AZUL, 1.8)

    # Doble flecha entre modos
    for y1, y2 in [(8.4, 7.1), (5.1, 3.2)]:
        ax.annotate('', xy=(7.2, y2), xytext=(7.2, y1),
                    arrowprops=dict(arrowstyle='<->', color=GRIS, lw=1.2), zorder=2)

    # ── Módulos ──
    modulos = [
        # Búsqueda general
        (13.5, 11.1, 'Viajar'),
        (13.5,  9.4, 'Socializar'),
        # Búsqueda focalizada
        (13.5,  7.2, 'Perseguir'),
        (13.5,  5.5, 'Capturar'),
        # Manipulación
        (13.5,  3.5, 'Probar /\nSostener'),
        (13.5,  1.7, 'Ingerir'),
    ]
    for mx, my, ml in modulos:
        rect(mx, my, 4.0, 1.3, ml, NARAN, NARAN, fs=10.5)

    # Flechas modo → módulos
    for mod_y, (m1x, m1y, _), (m2x, m2y, _) in [
            (10.2, modulos[0], modulos[1]),
            ( 6.3, modulos[2], modulos[3]),
            ( 2.4, modulos[4], modulos[5])]:
        arrow(9.2, mod_y, 11.5, m1y, VERDE)
        arrow(9.2, mod_y, 11.5, m2y, VERDE)

    # ── Acciones ──
    acciones = [
        (20.5, 11.1, 'Locomoción / Explorar'),
        (20.5,  9.4, 'Rastrear / Olfatear'),
        (20.5,  7.2, 'Perseguir / Cortar'),
        (20.5,  5.5, 'Atrapar / Morder'),
        (20.5,  3.5, 'Sostener / Masticar'),
        (20.5,  1.7, 'Tragar / Rechazar'),
    ]
    for ax2x, ay, al in acciones:
        rect(ax2x, ay, 5.0, 1.0, al, GRIS_L, GRIS, NEGRO, fs=10, bold=False)

    # Flechas módulo → acción
    for (_, my, _), (_, ay, _) in zip(modulos, acciones):
        arrow(15.5, my, 18.0, ay, NARAN, 1.5)

    # ── Anotación del experimento del balín — DEBAJO del diagrama ──
    ax.text(12.0, 0.30,
            'Experimento del balín: intervalo largo (7.6 s) → modo búsqueda focalizada  '
            '|  intervalo corto (2.6 s) → modo manipulación-consumo',
            ha='center', va='center', fontsize=9.5, color=GRIS,
            style='italic', zorder=5)

    fig.suptitle('Jerarquía de sistemas de comportamiento — subsistema de depredación '
                 '(Timberlake, 1994)',
                 fontsize=13, fontweight='bold', color=NEGRO, y=0.97)

    cap = ('Representación jerárquica del subsistema de depredación del sistema de alimentación '
           'de la rata. Los modos motivacionales organizan temporalmente la conducta; los módulos '
           'integran filtros perceptuales y programas motores que se expresan como patrones de '
           'acción específicos. Un estímulo predictor activa el modo que corresponde a su '
           'posición temporal relativa al SBI. Adaptado de Timberlake (1994).')
    add_caption(fig, '12.4', cap, y=0.005)

    save(fig, 'fig_12_4_timberlake')


# ── Ejecutar ─────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    fig_12_2()
    fig_12_3()
    fig_12_4()
    print('\nTodas las figuras generadas.')
