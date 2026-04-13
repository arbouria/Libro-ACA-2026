# ============================================================
# Simulador 8.1 — El Integrador con Fuga
# Capítulo 8: El Modelo de Bush y Mosteller
# Aprendizaje y Comportamiento Adaptable: Principios y Modelos
# Arturo Bouzas
# ============================================================
# Para correr en Google Colab: File → Open notebook → GitHub
# e.g. https://github.com/[usuario]/[repo]/blob/main/sim_8_1_integrador.py
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# --- Paleta del libro ---
AZUL    = '#2C5282'
NARANJA = '#C05621'
VERDE   = '#276749'
GRIS    = '#718096'

plt.rcParams.update({
    'font.family'        : 'serif',
    'figure.facecolor'   : 'white',
    'axes.facecolor'     : 'white',
    'axes.spines.top'    : False,
    'axes.spines.right'  : False,
    'axes.grid'          : True,
    'grid.alpha'         : 0.25,
    'grid.color'         : GRIS,
    'axes.labelcolor'    : GRIS,
    'xtick.color'        : GRIS,
    'ytick.color'        : GRIS,
    'axes.labelsize'     : 11,
    'xtick.labelsize'    : 10,
    'ytick.labelsize'    : 10,
})


def simular(alpha, V0, n_adq, n_ext, prob):
    """Simula el integrador con fuga y devuelve las trayectorias."""
    total = n_adq + n_ext
    V = V0
    Vs, deltas, Rs = [], [], []

    for t in range(total):
        es_ext = t >= n_adq
        R = 0 if es_ext else (1 if np.random.random() < prob else 0)
        delta = R - V
        V += alpha * delta
        Vs.append(V)
        deltas.append(delta)
        Rs.append(R)

    return np.array(Vs), np.array(deltas), np.array(Rs)


def graficar(alpha=0.30, V0=0.0, n_adq=10, n_ext=8, prob=1.0):
    Vs, deltas, Rs = simular(alpha, V0, n_adq, n_ext, prob)
    total = n_adq + n_ext
    ensayos = np.arange(1, total + 1)

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(9, 6), sharex=True,
        gridspec_kw={'height_ratios': [3, 1.6], 'hspace': 0.06}
    )

    # ── Panel superior: V ──────────────────────────────────────
    mk = 'o' if total <= 25 else None
    ax1.plot(ensayos, Vs, color=AZUL, linewidth=2.5,
             marker=mk, markersize=4, markerfacecolor=AZUL,
             label='V (valor predictivo)')
    ax1.axhline(prob, color=VERDE, linewidth=1.2, linestyle='--', alpha=0.85,
                label=f'equilibrio teórico = {prob:.2f}')
    ax1.set_ylim(-0.05, 1.18)
    ax1.set_ylabel('Valor predictivo V')
    ax1.legend(fontsize=9, loc='lower right', framealpha=0.9)

    # ── Panel inferior: δ ──────────────────────────────────────
    ax2.plot(ensayos, deltas, color=NARANJA, linewidth=1.8,
             linestyle='--', label='δ = R − V  (error de predicción)')
    ax2.axhline(0, color=GRIS, linewidth=0.8, alpha=0.6)
    ax2.set_ylim(-1.15, 1.15)
    ax2.set_ylabel('Error de predicción δ')
    ax2.set_xlabel('Ensayo')
    ax2.legend(fontsize=9, loc='upper right', framealpha=0.9)

    # ── Línea de fase ──────────────────────────────────────────
    if n_ext > 0:
        xdiv = n_adq + 0.5          # en matplotlib esto es preciso y directo
        for ax in (ax1, ax2):
            ax.axvline(xdiv, color=GRIS, linewidth=1.2,
                       linestyle=':', alpha=0.9)
        ax1.text(xdiv + 0.15, 1.10, 'extinción →',
                 color=GRIS, fontsize=9, va='top')

    # ── Título con métricas ────────────────────────────────────
    V_adq = Vs[n_adq - 1]
    titulo = (f'α = {alpha:.2f}   |   V₀ = {V0:.1f}   |   '
              f'P(refuerzo) = {prob:.1f}   |   '
              f'V final adq. = {V_adq:.3f}')
    if n_ext > 0:
        titulo += f'   |   V final ext. = {Vs[-1]:.3f}'
    fig.suptitle(titulo, fontsize=9.5, color=GRIS, y=0.99)

    plt.tight_layout()
    plt.show()
    print(f'\nEcuación — Adquisición: V_{{t+1}} = (1−{alpha:.2f})·V_t + {alpha:.2f}·R_t')
    if n_ext > 0:
        print(f'           Extinción:   V_{{t+1}} = (1−{alpha:.2f})·V_t')


# ── Controles ──────────────────────────────────────────────────
estilo   = {'description_width': '110px'}
layout_s = widgets.Layout(width='420px')
layout_l = widgets.Layout(width='500px')

w_alpha = widgets.FloatSlider(
    value=0.30, min=0.05, max=0.95, step=0.05,
    description='α:', style=estilo, layout=layout_s,
    readout_format='.2f')

w_V0 = widgets.FloatSlider(
    value=0.0, min=0.0, max=1.0, step=0.1,
    description='V₀:', style=estilo, layout=layout_s,
    readout_format='.1f')

w_nadq = widgets.IntSlider(
    value=10, min=2, max=20, step=1,
    description='Adquisición:', style=estilo, layout=layout_s)

w_next = widgets.IntSlider(
    value=8, min=0, max=20, step=1,
    description='Extinción:', style=estilo, layout=layout_s)

w_prob = widgets.FloatSlider(
    value=1.0, min=0.1, max=1.0, step=0.1,
    description='P(refuerzo):', style=estilo, layout=layout_l,
    readout_format='.1f')

ui = widgets.VBox([
    widgets.HTML('<b style="color:#2C5282; font-family:serif;">Simulador 8.1 — Integrador con Fuga</b>'),
    widgets.HBox([w_alpha, w_V0]),
    widgets.HBox([w_nadq, w_next]),
    w_prob,
])

out = widgets.interactive_output(
    graficar,
    {'alpha': w_alpha, 'V0': w_V0,
     'n_adq': w_nadq, 'n_ext': w_next, 'prob': w_prob}
)

display(ui, out)
