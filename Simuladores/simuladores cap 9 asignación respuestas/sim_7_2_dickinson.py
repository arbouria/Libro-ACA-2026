# ============================================================
# Simulador 7.2 — Detección de contingencia con gradiente de demora
# Capítulo 7: El Problema de la Asignación de Crédito (II)
# Aprendizaje y Comportamiento Adaptable: Principios y Modelos
#
# Basado en: Dickinson, Watt & Griffiths (1992), QJEP
#            Lattal (1987)
#
# Para ejecutar en Google Colab:
#   !pip install ipywidgets --quiet
#   from google.colab import output
#   output.enable_custom_widget_manager()
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import ipywidgets as widgets
from IPython.display import display, clear_output

# ─────────────────────────────────────────
# Paleta del libro
# ─────────────────────────────────────────
AZUL    = '#2C5282'
NARANJA = '#C05621'
VERDE   = '#276749'
GRIS    = '#718096'
ROJO    = '#9B2335'
FONDO   = 'white'

plt.rcParams.update({
    'font.family': 'serif',
    'axes.spines.top':   False,
    'axes.spines.right': False,
    'figure.facecolor':  FONDO,
    'axes.facecolor':    FONDO,
    'axes.labelsize':    11,
    'axes.titlesize':    12,
})

# ─────────────────────────────────────────
# Modelo de aprendizaje por contingencia con demora
# ─────────────────────────────────────────
#
# El simulador compara dos grupos:
#
# GRUPO EXPERIMENTAL (contingente)
#   La respuesta del agente causa los SBIs (con demora programada).
#   La tasa de SBIs cuando el agente responde es p_r > p_nor.
#   La señal de aprendizaje llega con una demora dem, que atenúa
#   su efectividad según el gradiente: efectividad = exp(−λ × dem).
#
# GRUPO YOKED (no contingente)
#   Recibe exactamente la misma secuencia de SBIs que el experimental,
#   pero en momentos no relacionados con SUS propias respuestas.
#   Desde la perspectiva del yoked, el SBI ocurre a una distancia
#   temporal aleatoria de su última respuesta, no al lapso programado.
#   Por eso no puede aprender la contingencia: el valor de sus
#   respuestas converge a la tasa de línea base, no a p_r.
#
# LA DISOCIACIÓN CLAVE
#   Si el aprendizaje dependiera solo de contigüidades accidentales,
#   ambos grupos aprenderían igual: el yoked experimenta las mismas
#   contigüidades accidentales que el experimental durante la demora.
#   Si el experimental aprende más, la diferencia se debe a la
#   relación de dependencia real — el resultado de Dickinson.
#
# MODELO FORMAL
#   La tasa de respuesta de cada grupo sigue una dinámica B&M
#   hacia su asíntota correspondiente:
#
#     rate_{n+1} = rate_n + α × (asíntota − rate_n) + ε_n
#
#   Asíntota experimental:
#     asint_exp(dem) = base + escala × (p_r − p_nor) × exp(−λ × dem)
#
#   Asíntota yoked:
#     asint_yoke = base
#     (no hay contingencia aprendible: las respuestas no producen SBIs)
#
#   Con dem → 0:  asint_exp → base + escala × ΔP   (máximo aprendizaje)
#   Con dem → ∞:  asint_exp → base                  (igual que yoked)
#
# PARÁMETROS:
#   p_r    = P(SBI | respuesta)     — prob. condicional real
#   p_nor  = P(SBI | sin respuesta) — línea base de SBIs
#   dem    = demora en segundos
#   α      = tasa de aprendizaje (velocidad hacia la asíntota)
#   λ      = pendiente del gradiente de demora

TASA_BASE = 1.0     # tasa de respuesta en línea base (resp/min)
TASA_MAX  = 20.0    # tasa máxima posible
ESCALA    = TASA_MAX - TASA_BASE
N_SESIONES    = 20
N_ENSAYOS_SES = 60

# Demoras del experimento de Dickinson et al. (1992): 0, 4, 8, 16, 32, 64 s
DEMORAS_DICKINSON = [0, 4, 8, 16, 32, 64]
COLORES_DEMORA    = {0: VERDE, 4: '#1A6B4A', 8: '#155724',
                     16: AZUL, 32: NARANJA, 64: ROJO}


def simular_par(p_r, p_nor, demora, alpha, lam, n_ses, seed=42):
    """
    Simula ambos grupos (experimental y yoked) con la dinámica B&M
    hacia sus asíntotas respectivas.

    Retorna
    -------
    tasas_exp, tasas_yoke : arrays (n_ses,) con tasa de respuesta por sesión
    """
    rng = np.random.default_rng(seed)
    efectividad = np.exp(-lam * demora)

    asint_exp  = TASA_BASE + ESCALA * np.clip((p_r - p_nor) * efectividad, 0, 1)
    asint_yoke = TASA_BASE   # sin contingencia aprendible

    rate_e = TASA_BASE
    rate_y = TASA_BASE
    te = np.zeros(n_ses)
    ty = np.zeros(n_ses)

    for ses in range(n_ses):
        noise = rng.normal(0, 0.5, 2)
        rate_e = rate_e + alpha * (asint_exp  - rate_e)
        rate_y = rate_y + alpha * (asint_yoke - rate_y)
        te[ses] = np.clip(rate_e + noise[0], 0, TASA_MAX)
        ty[ses] = np.clip(rate_y + noise[1], 0, TASA_MAX)

    return te, ty


def tasa_final_vs_demora(p_r, p_nor, alpha, lam, n_ses,
                         dem_array, seed=42):
    """
    Calcula la tasa en la sesión final para cada valor de demora,
    en ambos grupos.
    """
    te_f = np.zeros(len(dem_array))
    ty_f = np.zeros(len(dem_array))
    for i, d in enumerate(dem_array):
        te, ty = simular_par(p_r, p_nor, d, alpha, lam, n_ses, seed=seed+i)
        te_f[i] = te[-1]
        ty_f[i] = ty[-1]
    return te_f, ty_f


# ─────────────────────────────────────────
# Widgets
# ─────────────────────────────────────────
_style  = {'description_width': '250px'}
_layout = widgets.Layout(width='490px')

slider_pr = widgets.FloatSlider(
    value=0.50, min=0.05, max=0.95, step=0.05,
    description='P(SBI | respuesta):',
    continuous_update=True, readout_format='.2f',
    style=_style, layout=_layout,
)
slider_pnor = widgets.FloatSlider(
    value=0.05, min=0.00, max=0.50, step=0.05,
    description='P(SBI | sin respuesta):',
    continuous_update=True, readout_format='.2f',
    style=_style, layout=_layout,
)
slider_dem = widgets.FloatSlider(
    value=0.0, min=0.0, max=64.0, step=2.0,
    description='Demora respuesta → SBI (s):',
    continuous_update=True, readout_format='.0f',
    style=_style, layout=_layout,
)
slider_alpha = widgets.FloatSlider(
    value=0.25, min=0.02, max=0.70, step=0.02,
    description='Tasa de aprendizaje (α):',
    continuous_update=True, readout_format='.2f',
    style=_style, layout=_layout,
)
slider_lam = widgets.FloatSlider(
    value=0.06, min=0.005, max=0.20, step=0.005,
    description='Gradiente de demora (λ):',
    continuous_update=True, readout_format='.3f',
    style=_style, layout=_layout,
)

out = widgets.Output()


# ─────────────────────────────────────────
# Función de actualización
# ─────────────────────────────────────────
def actualizar(change=None):
    p_r   = slider_pr.value
    p_nor = slider_pnor.value
    dem   = slider_dem.value
    alpha = slider_alpha.value
    lam   = slider_lam.value

    delta_p     = p_r - p_nor
    efectividad = np.exp(-lam * dem)
    sesiones    = np.arange(1, N_SESIONES + 1)

    # Curvas de adquisición para la demora actual
    te, ty = simular_par(p_r, p_nor, dem, alpha, lam, N_SESIONES, seed=7)

    # Tasa final vs demora (continua)
    dem_cont = np.linspace(0, 64, 80)
    te_d, ty_d = tasa_final_vs_demora(p_r, p_nor, alpha, lam,
                                       N_SESIONES, dem_cont, seed=11)

    # Curvas fijas de Dickinson
    curvas = {}
    for d in DEMORAS_DICKINSON:
        te_d2, ty_d2 = simular_par(p_r, p_nor, d, alpha, lam, N_SESIONES, seed=42)
        curvas[d] = (te_d2, ty_d2)

    # Gradiente teórico
    dem_g = np.linspace(0, 64, 200)
    grad  = np.exp(-lam * dem_g)

    with out:
        clear_output(wait=True)

        fig = plt.figure(figsize=(15, 9.5))
        gs  = gridspec.GridSpec(2, 3, figure=fig, hspace=0.52, wspace=0.42)

        # ── Panel A: Curvas de adquisición ────────────────────────────
        ax_adq = fig.add_subplot(gs[0, :2])

        ax_adq.plot(sesiones, te, color=AZUL,    lw=2.5,
                    label=f'Grupo experimental (contingente)\ndemora = {dem:.0f} s')
        ax_adq.plot(sesiones, ty, color=NARANJA, lw=2.5, linestyle='--',
                    label='Grupo yoked (no contingente)')
        ax_adq.axhline(TASA_BASE, color=GRIS, lw=1.2, linestyle=':',
                       label=f'Línea base = {TASA_BASE:.0f} resp/min')

        # Flecha de disociación
        dif = te[-1] - ty[-1]
        mid = (te[-1] + ty[-1]) / 2
        if abs(dif) > 0.3:
            ax_adq.annotate(
                f'Δ = {dif:.1f}\nresp/min',
                xy=(N_SESIONES, mid),
                xytext=(N_SESIONES - 5.5, mid + 1.8),
                fontsize=9, color=GRIS,
                arrowprops=dict(arrowstyle='->', color=GRIS, lw=1.2),
            )

        ax_adq.set_xlabel('Sesión')
        ax_adq.set_ylabel('Tasa de respuesta (resp/min)')
        ax_adq.set_title(
            f'A.  Curvas de adquisición — demora = {dem:.0f} s\n'
            f'     ΔP = P(SBI|R) − P(SBI|¬R) = {delta_p:.2f}     '
            f'efectividad = exp(−λ×dem) = {efectividad:.2f}',
            fontweight='bold', loc='left'
        )
        ax_adq.set_xlim(1, N_SESIONES)
        ax_adq.set_ylim(0, TASA_MAX * 1.05)
        ax_adq.legend(fontsize=8.5, loc='upper left', framealpha=0.9)

        ax_adq.text(
            0.01, 0.97,
            f'P(SBI|R) = {p_r:.2f}   P(SBI|¬R) = {p_nor:.2f}   '
            f'α = {alpha:.2f}   λ = {lam:.3f}',
            transform=ax_adq.transAxes, fontsize=9, va='top',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#EBF4FF',
                      edgecolor=AZUL, alpha=0.85)
        )

        # ── Panel B: Tasa final vs demora ─────────────────────────────
        ax_dem = fig.add_subplot(gs[0, 2])

        ax_dem.plot(dem_cont, te_d, color=AZUL,    lw=2.2, label='Experimental')
        ax_dem.plot(dem_cont, ty_d, color=NARANJA, lw=2.2, linestyle='--',
                    label='Yoked')
        ax_dem.axvline(dem, color=GRIS, lw=1.5, linestyle='--',
                       label=f'Demora actual = {dem:.0f}s')
        ax_dem.scatter([dem], [te[-1]], color=AZUL,    s=90, zorder=5)
        ax_dem.scatter([dem], [ty[-1]], color=NARANJA, s=90, zorder=5)

        for d_f in DEMORAS_DICKINSON:
            ax_dem.axvline(d_f, color=GRIS, lw=0.5, linestyle=':', alpha=0.4)

        ax_dem.set_xlabel('Demora (segundos)')
        ax_dem.set_ylabel('Tasa final (resp/min)')
        ax_dem.set_title('B.  Tasa de respuesta al final\n     del entrenamiento vs demora',
                          fontweight='bold', loc='left')
        ax_dem.set_xlim(0, 64); ax_dem.set_ylim(0, TASA_MAX * 1.05)
        ax_dem.legend(fontsize=8, framealpha=0.9)
        ax_dem.text(0.50, 0.88, 'Dickinson:\n0, 4, 8, 16, 32, 64 s',
                    transform=ax_dem.transAxes, fontsize=8, color=GRIS, ha='center')

        # ── Panel C: Curvas de adquisición a demoras de Dickinson ─────
        ax_fij = fig.add_subplot(gs[1, :2])

        for d_f, (te_f, ty_f) in curvas.items():
            col = COLORES_DEMORA[d_f]
            ax_fij.plot(sesiones, te_f, color=col, lw=2.0, label=f'Exp. {d_f}s')
            ax_fij.plot(sesiones, ty_f, color=col, lw=1.5, linestyle='--', alpha=0.55)

        ax_fij.axhline(TASA_BASE, color=GRIS, lw=1, linestyle=':', alpha=0.7)
        ax_fij.set_xlabel('Sesión')
        ax_fij.set_ylabel('Tasa de respuesta (resp/min)')
        ax_fij.set_title(
            'C.  Curvas de adquisición a demoras de Dickinson et al. (1992)\n'
            '     Líneas sólidas = experimental   Punteadas = yoked',
            fontweight='bold', loc='left'
        )
        ax_fij.set_xlim(1, N_SESIONES); ax_fij.set_ylim(0, TASA_MAX * 1.05)
        ax_fij.legend(fontsize=8, ncol=2, framealpha=0.9, loc='upper left',
                      title='Demora')

        ax_fij.text(
            0.98, 0.06,
            'Dickinson et al. (1992):\n'
            '≤32 s → exp > yoked (contingencia aprendible)\n'
            '64 s → ambos ≈ línea base (señal extinguida)',
            transform=ax_fij.transAxes, fontsize=8.5,
            va='bottom', ha='right', color=GRIS,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#F0FFF4',
                      edgecolor=VERDE, alpha=0.85)
        )

        # ── Panel D: Gradiente de demora teórico ─────────────────────
        ax_grad = fig.add_subplot(gs[1, 2])

        ax_grad.plot(dem_g, grad, color=AZUL, lw=2.5,
                     label=f'exp(−λ × dem)   λ={lam:.3f}')
        ax_grad.axvline(dem, color=GRIS, lw=1.5, linestyle='--',
                        label=f'Demora actual = {dem:.0f}s\nEfect. = {efectividad:.2f}')
        ax_grad.scatter([dem], [efectividad], color=NARANJA, s=120, zorder=5)

        # Puntos de Dickinson
        for d_f in DEMORAS_DICKINSON:
            ax_grad.scatter([d_f], [np.exp(-lam*d_f)],
                            color=COLORES_DEMORA[d_f], s=65, zorder=4, alpha=0.9)
        ax_grad.text(0.56, 0.82,
                     'Puntos = demoras\nde Dickinson',
                     transform=ax_grad.transAxes, fontsize=8.5, color=GRIS,
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='#EBF4FF',
                               edgecolor=AZUL, alpha=0.7))

        ax_grad.set_xlabel('Demora (segundos)')
        ax_grad.set_ylabel('Efectividad del SBI\npara producir aprendizaje')
        ax_grad.set_title('D.  Gradiente de demora exponencial',
                           fontweight='bold', loc='left')
        ax_grad.set_xlim(0, 64); ax_grad.set_ylim(0, 1.05)
        ax_grad.legend(fontsize=8.5, framealpha=0.9)

        plt.suptitle(
            'Simulador 7.2 — Detección de contingencia con gradiente de demora\n'
            '(Dickinson, Watt & Griffiths, 1992)',
            fontsize=13, fontweight='bold', y=1.01
        )
        plt.show()


# ─────────────────────────────────────────
# Interfaz
# ─────────────────────────────────────────
cabecera = widgets.HTML(value="""
<div style="background:#EBF4FF; border-left:5px solid #2C5282;
            padding:14px 18px; margin-bottom:10px; font-family:Georgia,serif;">
  <div style="font-size:16px; font-weight:bold; color:#2C5282; margin-bottom:6px;">
    Simulador 7.2 — Detección de contingencia con gradiente de demora
  </div>
  <div style="font-size:13px; color:#2D3748; line-height:1.6;">
    Un agente aprende que sus respuestas producen SBIs aunque haya una demora entre ambos.<br>
    El <b style="color:#2C5282">grupo experimental</b> tiene una relación real de dependencia
    respuesta → SBI; el <b style="color:#C05621">grupo yoked</b> (punteado) recibe los mismos
    SBIs en los mismos momentos, pero sin dependencia con sus propias respuestas.<br><br>
    Si el aprendizaje dependiera solo de contigüidades accidentales, ambos grupos aprenderían
    igual — porque el yoked experimenta las mismas contigüidades accidentales durante la demora.
    Si el experimental aprende más, la diferencia se debe a la relación de dependencia real.
    Ese es el resultado de Dickinson.<br><br>
    <b>Panel A</b> — Curvas de adquisición para la demora seleccionada.<br>
    <b>Panel B</b> — Tasa de respuesta final como función de la demora.<br>
    <b>Panel C</b> — Curvas de adquisición a las seis demoras del experimento de Dickinson.<br>
    <b>Panel D</b> — Gradiente de demora exponencial y su parámetro λ.
  </div>
</div>
""")

sep = widgets.HTML('<hr style="border:1px solid #CBD5E0; margin:6px 0;">')
lbl = widgets.HTML('<b style="font-family:Georgia,serif;font-size:13px;">Parámetros ajustables:</b>')

panel = widgets.VBox([cabecera, sep, lbl,
                      slider_pr, slider_pnor, slider_dem,
                      slider_alpha, slider_lam, sep])

for sl in [slider_pr, slider_pnor, slider_dem, slider_alpha, slider_lam]:
    sl.observe(actualizar, names='value')

display(panel, out)
actualizar()
