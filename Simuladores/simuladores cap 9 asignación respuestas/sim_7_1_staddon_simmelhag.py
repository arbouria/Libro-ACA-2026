# ============================================================
# Simulador 7.1 — Inducción temporal: respuestas interinas y terminales
# Capítulo 7: El Problema de la Asignación de Crédito (II)
# Aprendizaje y Comportamiento Adaptable: Principios y Modelos
#
# Basado en: Staddon & Simmelhag (1971), Psychological Review
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
# Modelo de inducción temporal
# ─────────────────────────────────────────
#
# Staddon & Simmelhag (1971) documentaron dos clases de respuestas
# distribuidas a lo largo del intervalo entre entregas de comida:
#
# RESPUESTAS INTERINAS
#   Aparecen después del SBI y se disipan conforme el tiempo avanza.
#   Representan actividad inducida por la llegada del refuerzo:
#   explorar, desplazarse, vocalizar.
#   Modelo: P_int(t) = exp(−α × t)
#     α (DECAIMIENTO): velocidad con que se disipan estas respuestas.
#     A t=0 (inmediatamente después del SBI), P_int = 1.
#     A t=T (cuando llega el siguiente SBI), P_int = exp(−α×T).
#
# RESPUESTAS TERMINALES
#   Aparecen cerca del SBI siguiente y crecen hacia él.
#   Representan la activación anticipatoria del sistema de alimentación:
#   orientarse al comedero, picotear en esa dirección.
#   Modelo: P_term(t) = exp(−γ × (T − t))
#     γ (ANTICIPACION): velocidad de crecimiento anticipatorio.
#     A t=T (SBI siguiente), P_term = 1.
#     A t=0 (inmediatamente después del SBI previo), P_term = exp(−γ×T).
#
# PUNTO DE CRUCE
#   Las curvas se cruzan cuando P_int(t*) = P_term(t*):
#     exp(−α×t*) = exp(−γ×(T−t*))
#     t* = γ×T / (α + γ)
#   Nótese que t*/T = γ/(α+γ) es INDEPENDIENTE de T:
#   la posición relativa del cruce no cambia con la duración del intervalo.
#   Esto refleja la propiedad de "escala de tiempo relativa" documentada
#   en el comportamiento operante (Gibbon, 1977).

def probabilidades(T, alpha, gamma, n_puntos=300):
    """
    Calcula P(interina) y P(terminal) a lo largo del intervalo [0, T].

    Retorna t (vector de tiempo), p_int, p_term, t_cruce.
    """
    t      = np.linspace(0, T, n_puntos)
    p_int  = np.exp(-alpha * t)
    p_term = np.exp(-gamma * (T - t))
    t_cruce = gamma * T / (alpha + gamma) if (alpha + gamma) > 0 else None
    return t, p_int, p_term, t_cruce


def simular_raster(T, alpha, gamma, n_intervalos, rng=None):
    """
    Genera respuestas discretas segundo a segundo en n_intervalos.

    En cada segundo del intervalo, el organismo muestra:
      - respuesta interina  con probabilidad P_int(t)
      - respuesta terminal  con probabilidad P_term(t)
    Si ambas se "disparan" en el mismo segundo, prevalece la terminal
    (las respuestas terminales son dominantes cuando el SBI se acerca).

    Retorna: matriz (n_intervalos × n_seg), valores 0=ninguna, 1=interina, 2=terminal
    """
    if rng is None:
        rng = np.random.default_rng(42)
    n_seg = max(1, int(T))
    _, p_i, p_t, _ = probabilidades(T, alpha, gamma, n_puntos=n_seg)
    p_i = np.clip(p_i, 0, 1)
    p_t = np.clip(p_t, 0, 1)

    raster = np.zeros((n_intervalos, n_seg), dtype=int)
    for i in range(n_intervalos):
        r_i = rng.random(n_seg) < p_i
        r_t = rng.random(n_seg) < p_t
        raster[i] = np.where(r_t, 2, np.where(r_i, 1, 0))
    return raster


# ─────────────────────────────────────────
# Widgets
# ─────────────────────────────────────────
_style  = {'description_width': '240px'}
_layout = widgets.Layout(width='480px')

slider_T = widgets.FloatSlider(
    value=15, min=5, max=40, step=1,
    description='Duración del intervalo T (s):',
    continuous_update=True, readout_format='.0f',
    style=_style, layout=_layout,
)
slider_alpha = widgets.FloatSlider(
    value=0.25, min=0.02, max=1.5, step=0.02,
    description='Decaimiento de interinas (α):',
    continuous_update=True, readout_format='.2f',
    style=_style, layout=_layout,
)
slider_gamma = widgets.FloatSlider(
    value=0.35, min=0.02, max=1.5, step=0.02,
    description='Anticipación de terminales (γ):',
    continuous_update=True, readout_format='.2f',
    style=_style, layout=_layout,
)
slider_n_int = widgets.IntSlider(
    value=20, min=5, max=60, step=5,
    description='Intervalos a simular:',
    continuous_update=True,
    style=_style, layout=_layout,
)

out = widgets.Output()


# ─────────────────────────────────────────
# Función de actualización
# ─────────────────────────────────────────
def actualizar(change=None):
    T       = slider_T.value
    alpha   = slider_alpha.value
    gamma   = slider_gamma.value
    n_int   = slider_n_int.value
    n_seg   = max(1, int(T))

    t, p_int, p_term, t_cruce = probabilidades(T, alpha, gamma)
    raster = simular_raster(T, alpha, gamma, n_int)

    # Proporción de cada tipo por segundo (para Panel D)
    prop_int  = (raster == 1).mean(axis=0)
    prop_term = (raster == 2).mean(axis=0)
    t_seg     = np.arange(n_seg) + 0.5

    # Posición relativa del cruce para distintos T (Panel C)
    T_vals     = np.linspace(5, 40, 200)
    cruces_rel = gamma / (alpha + gamma) * np.ones_like(T_vals)  # constante!

    with out:
        clear_output(wait=True)

        fig = plt.figure(figsize=(15, 9))
        gs  = gridspec.GridSpec(2, 3, figure=fig, hspace=0.52, wspace=0.42)

        # ── Panel A: Curvas de probabilidad ──────────────────────────
        ax_prob = fig.add_subplot(gs[0, :2])

        ax_prob.fill_between(t, p_int, p_term,
                             where=(p_int > p_term),
                             alpha=0.10, color=NARANJA)
        ax_prob.fill_between(t, p_int, p_term,
                             where=(p_term >= p_int),
                             alpha=0.10, color=AZUL)

        ax_prob.plot(t, p_int,  color=NARANJA, lw=2.5,
                     label='Respuestas interinas\n(explorar, desplazarse)')
        ax_prob.plot(t, p_term, color=AZUL,    lw=2.5,
                     label='Respuestas terminales\n(orientarse, picotear comedero)')

        # SBIs
        for x, lbl in [(0, 'SBI anterior'), (T, 'SBI siguiente')]:
            ax_prob.axvline(x, color=VERDE, lw=2, linestyle=':', alpha=0.8)
            ax_prob.text(x + T*0.015, 0.97, lbl, color=VERDE, fontsize=9,
                         transform=ax_prob.get_xaxis_transform(), va='top')

        # Cruce
        if t_cruce is not None:
            p_c = float(np.exp(-alpha * t_cruce))
            ax_prob.axvline(t_cruce, color=GRIS, lw=1.8, linestyle='--', alpha=0.8)
            ax_prob.scatter([t_cruce], [p_c], color=GRIS, s=90, zorder=5,
                            label=f'Cruce en t* = {t_cruce:.1f} s ({t_cruce/T*100:.0f}% del intervalo)')

        ax_prob.set_xlabel('Tiempo en el intervalo (segundos)')
        ax_prob.set_ylabel('Probabilidad de ocurrencia')
        ax_prob.set_title('A.  Distribución temporal de respuestas inducidas',
                          fontweight='bold', loc='left')
        ax_prob.set_xlim(0, T); ax_prob.set_ylim(0, 1.08)
        ax_prob.legend(fontsize=9, loc='center', framealpha=0.9)

        # Caja de parámetros
        ax_prob.text(0.02, 0.06,
                     f'T = {T:.0f} s   α = {alpha:.2f}   γ = {gamma:.2f}\n'
                     f't* = {t_cruce:.1f} s = {t_cruce/T*100:.0f}% del intervalo   '
                     f't*/T = γ/(α+γ) = {gamma/(alpha+gamma):.2f}',
                     transform=ax_prob.transAxes, fontsize=9,
                     bbox=dict(boxstyle='round,pad=0.35', facecolor='#EBF4FF',
                               edgecolor=AZUL, alpha=0.85))

        # ── Panel B: Raster ──────────────────────────────────────────
        ax_raster = fig.add_subplot(gs[1, :2])

        img = np.zeros((*raster.shape, 3))
        img[raster == 0] = [0.97, 0.97, 0.97]
        img[raster == 1] = [0.75, 0.34, 0.13]   # naranja
        img[raster == 2] = [0.17, 0.32, 0.51]   # azul

        ax_raster.imshow(img, aspect='auto',
                         extent=[0, n_seg, n_int, 0], interpolation='nearest')

        for x, col in [(0, VERDE), (n_seg, VERDE)]:
            ax_raster.axvline(x, color=col, lw=2, linestyle=':', alpha=0.8)
        if t_cruce is not None:
            ax_raster.axvline(t_cruce, color=GRIS, lw=1.8, linestyle='--',
                              alpha=0.9, label=f't* = {t_cruce:.1f} s')
            ax_raster.legend(fontsize=8.5, loc='upper right', framealpha=0.9)

        ax_raster.set_xlabel('Tiempo en el intervalo (segundos)')
        ax_raster.set_ylabel('Número de intervalo')
        ax_raster.set_title(
            'B.  Respuestas simuladas intervalo a intervalo\n'
            '     ■ naranja = interina   ■ azul = terminal   □ gris = ninguna',
            fontweight='bold', loc='left'
        )
        ax_raster.set_xlim(0, n_seg)

        # ── Panel C: t*/T vs T ───────────────────────────────────────
        ax_cruce = fig.add_subplot(gs[0, 2])

        ax_cruce.plot(T_vals, cruces_rel, color=AZUL, lw=2.5,
                      label=f't*/T = γ/(α+γ) = {gamma/(alpha+gamma):.2f}')
        ax_cruce.axhline(0.5, color=GRIS, lw=1.2, linestyle='--',
                         label='Mitad del intervalo')
        ax_cruce.scatter([T], [gamma/(alpha+gamma)], color=NARANJA, s=120,
                         zorder=5, label=f'T actual = {T:.0f} s')

        ax_cruce.set_xlabel('Duración del intervalo T (s)')
        ax_cruce.set_ylabel('Posición del cruce (t*/T)')
        ax_cruce.set_title('C.  t*/T es constante:\nescala de tiempo relativa',
                            fontweight='bold', loc='left')
        ax_cruce.set_ylim(0, 1); ax_cruce.set_xlim(5, 40)
        ax_cruce.legend(fontsize=8.5, framealpha=0.9)
        ax_cruce.text(0.05, 0.08,
                      'El cruce ocurre en la misma\nfracción del intervalo\nindependientemente de T.',
                      transform=ax_cruce.transAxes, fontsize=8.5,
                      color=GRIS,
                      bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0FFF4',
                                edgecolor=VERDE, alpha=0.8))

        # ── Panel D: Proporción observada ────────────────────────────
        ax_prop = fig.add_subplot(gs[1, 2])

        ax_prop.bar(t_seg, prop_int,  color=NARANJA, alpha=0.80, width=0.85,
                    label='Interinas')
        ax_prop.bar(t_seg, prop_term, color=AZUL,    alpha=0.80, width=0.85,
                    bottom=prop_int, label='Terminales')

        for x in [0, n_seg]:
            ax_prop.axvline(x, color=VERDE, lw=1.5, linestyle=':', alpha=0.8)
        if t_cruce is not None:
            ax_prop.axvline(t_cruce, color=GRIS, lw=1.8, linestyle='--',
                            label=f't* = {t_cruce:.1f} s')

        ax_prop.set_xlabel('Tiempo en el intervalo (segundos)')
        ax_prop.set_ylabel('Fracción de intervalos\ncon esa respuesta')
        ax_prop.set_title('D.  Proporción de respuestas\n     en la simulación',
                           fontweight='bold', loc='left')
        ax_prop.set_xlim(0, n_seg); ax_prop.set_ylim(0, 1.05)
        ax_prop.legend(fontsize=8.5, framealpha=0.9)

        plt.suptitle(
            'Simulador 7.1 — Inducción temporal: respuestas interinas y terminales\n'
            '(Staddon & Simmelhag, 1971)',
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
    Simulador 7.1 — Inducción temporal de Staddon &amp; Simmelhag (1971)
  </div>
  <div style="font-size:13px; color:#2D3748; line-height:1.6;">
    La presentación periódica de un SBI alimenticio induce dos clases de respuestas
    cuya probabilidad varía a lo largo del intervalo entre entregas.<br>
    <b style="color:#C05621">Respuestas interinas</b> (naranja): explorar, desplazarse —
    aparecen después del SBI y decaen con tasa α.<br>
    <b style="color:#2C5282">Respuestas terminales</b> (azul): orientarse al comedero,
    picotear — crecen hacia el siguiente SBI con tasa γ.<br><br>
    <b>Panel A</b> — Curvas de probabilidad teóricas sobre el intervalo.<br>
    <b>Panel B</b> — Respuestas simuladas intervalo a intervalo (raster).<br>
    <b>Panel C</b> — La posición relativa del cruce (t*/T) no cambia con T.<br>
    <b>Panel D</b> — Proporción de cada tipo de respuesta observada en la simulación.
  </div>
</div>
""")

sep = widgets.HTML('<hr style="border:1px solid #CBD5E0; margin:6px 0;">')
lbl = widgets.HTML('<b style="font-family:Georgia,serif;font-size:13px;">Parámetros ajustables:</b>')

panel = widgets.VBox([cabecera, sep, lbl,
                      slider_T, slider_alpha, slider_gamma, slider_n_int, sep])

for sl in [slider_T, slider_alpha, slider_gamma, slider_n_int]:
    sl.observe(actualizar, names='value')

display(panel, out)
actualizar()
