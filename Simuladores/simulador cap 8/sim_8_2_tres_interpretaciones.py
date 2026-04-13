# ============================================================
# Simulador 8.2 — Las Tres Interpretaciones del Modelo de B&M
# Capítulo 8: El Modelo de Bush y Mosteller
# Aprendizaje y Comportamiento Adaptable: Principios y Modelos
# Arturo Bouzas
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

AZUL    = '#2C5282'
NARANJA = '#C05621'
VERDE   = '#276749'
GRIS    = '#718096'

plt.rcParams.update({
    'font.family'      : 'serif',
    'figure.facecolor' : 'white',
    'axes.facecolor'   : 'white',
    'axes.spines.top'  : False,
    'axes.spines.right': False,
    'axes.grid'        : True,
    'grid.alpha'       : 0.25,
    'grid.color'       : GRIS,
    'axes.labelcolor'  : GRIS,
    'xtick.color'      : GRIS,
    'ytick.color'      : GRIS,
    'axes.labelsize'   : 10,
    'xtick.labelsize'  : 9,
    'ytick.labelsize'  : 9,
})


def graficar_tres(alpha=0.30, n_adq=15, prob=1.0):
    # ── Simular ────────────────────────────────────────────────
    V = 0.0
    Vs, deltas = [], []
    for t in range(n_adq):
        R = 1 if np.random.random() < prob else 0
        delta = R - V
        V += alpha * delta
        Vs.append(V)
        deltas.append(delta)

    ensayos = np.arange(1, n_adq + 1)

    # Pesos exponenciales para el panel 3
    k_max   = min(20, n_adq)
    ks      = np.arange(k_max)
    pesos   = alpha * (1 - alpha) ** ks

    # ── Figura ─────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))
    fig.suptitle(
        f'α = {alpha:.2f}   |   P(refuerzo) = {prob:.1f}   |   ensayos = {n_adq}',
        fontsize=10, color=GRIS, y=1.01
    )

    # Panel 1 — Integrador con fuga: trayectoria de V
    ax1 = axes[0]
    mk = 'o' if n_adq <= 25 else None
    ax1.plot(ensayos, Vs, color=AZUL, linewidth=2.5,
             marker=mk, markersize=4, markerfacecolor=AZUL)
    ax1.axhline(prob, color=VERDE, linewidth=1.2, linestyle='--', alpha=0.8,
                label=f'equilibrio = {prob:.2f}')
    ax1.set_ylim(-0.05, 1.15)
    ax1.set_xlabel('Ensayo')
    ax1.set_ylabel('V (cantidad de carga)')
    ax1.set_title('Panel 1\nIntegrador: trayectoria de V', fontsize=9, color=GRIS)
    ax1.legend(fontsize=8)

    # Panel 2 — Error de predicción: trayectoria de δ
    ax2 = axes[1]
    ax2.plot(ensayos, deltas, color=NARANJA, linewidth=2,
             linestyle='--')
    ax2.axhline(0, color=GRIS, linewidth=0.8, alpha=0.6)
    ax2.fill_between(ensayos, deltas, 0,
                     where=np.array(deltas) > 0,
                     color=NARANJA, alpha=0.12)
    ax2.fill_between(ensayos, deltas, 0,
                     where=np.array(deltas) < 0,
                     color=GRIS, alpha=0.12)
    ax2.set_ylim(-1.15, 1.15)
    ax2.set_xlabel('Ensayo')
    ax2.set_ylabel('δ = R − V')
    ax2.set_title('Panel 2\nError de predicción δ', fontsize=9, color=GRIS)
    nota_delta = ('δ decrece conforme V → equilibrio.\n'
                  'Cuando δ = 0, el aprendizaje se detiene.')
    ax2.text(0.97, 0.97, nota_delta, transform=ax2.transAxes,
             fontsize=7.5, color=GRIS, ha='right', va='top',
             bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

    # Panel 3 — Filtro exponencial: pesos de ensayos pasados
    ax3 = axes[2]
    ax3.bar(ks, pesos, color=AZUL, alpha=0.75, width=0.7,
            edgecolor=AZUL, linewidth=0.8)
    ax3.set_xlabel('k  (ensayos atrás)')
    ax3.set_ylabel(r'peso  α·(1−α)$^k$')
    ax3.set_title('Panel 3\nFiltro: pesos exponenciales', fontsize=9, color=GRIS)

    # Anotación del peso del ensayo más reciente
    ax3.annotate(f'α = {alpha:.2f}',
                 xy=(0, pesos[0]), xytext=(2, pesos[0] * 0.85),
                 fontsize=8, color=AZUL,
                 arrowprops=dict(arrowstyle='->', color=AZUL, lw=1))

    suma = pesos.sum()
    ax3.text(0.97, 0.97,
             f'suma de {k_max} pesos = {suma:.3f}',
             transform=ax3.transAxes,
             fontsize=7.5, color=GRIS, ha='right', va='top')

    plt.tight_layout()
    plt.show()

    # ── Tabla de pesos ──────────────────────────────────────────
    print(f'\nPesos para α = {alpha:.2f}:')
    print(f"{'k (ensayos atrás)':<22} {'peso α(1−α)^k':<18} {'%'}")
    print('─' * 48)
    for k in range(min(8, k_max)):
        p = pesos[k]
        print(f"  {k:<21} {p:<18.4f} {p*100:.1f}%")
    if k_max > 8:
        print(f"  ... (hasta k = {k_max - 1})")
    print(f"\n  Suma de todos los pesos mostrados: {pesos[:8].sum():.4f}")


# ── Controles ──────────────────────────────────────────────────
estilo = {'description_width': '110px'}

w_alpha = widgets.FloatSlider(
    value=0.30, min=0.05, max=0.95, step=0.05,
    description='α:', style=estilo,
    layout=widgets.Layout(width='420px'),
    readout_format='.2f')

w_nadq = widgets.IntSlider(
    value=15, min=5, max=30, step=1,
    description='Ensayos de adq.:', style=estilo,
    layout=widgets.Layout(width='420px'))

w_prob = widgets.FloatSlider(
    value=1.0, min=0.1, max=1.0, step=0.1,
    description='P(refuerzo):', style=estilo,
    layout=widgets.Layout(width='420px'),
    readout_format='.1f')

ui = widgets.VBox([
    widgets.HTML('<b style="color:#2C5282; font-family:serif;">'
                 'Simulador 8.2 — Las Tres Interpretaciones del Modelo de B&M</b>'),
    widgets.HBox([w_alpha, w_nadq]),
    w_prob,
])

out = widgets.interactive_output(
    graficar_tres,
    {'alpha': w_alpha, 'n_adq': w_nadq, 'prob': w_prob}
)

display(ui, out)
