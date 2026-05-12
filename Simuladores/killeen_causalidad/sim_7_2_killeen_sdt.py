# ============================================================
# Simulador 7.2 — Detección de causalidad (Killeen, 1978)
# Capítulo 7: El Problema de la Asignación de Crédito (II)
# Aprendizaje y Comportamiento Adaptable: Principios y Modelos
#
# Para ejecutar en Google Colab:
#   !pip install ipywidgets --quiet
#   from google.colab import output
#   output.enable_custom_widget_manager()
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from scipy import stats
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
# Funciones del modelo (Teoría de Detección de Señales)
# ─────────────────────────────────────────

def tasa_aciertos_y_fa(criterio, dprime):
    """
    Calcula P(acierto) y P(falsa alarma) dado un criterio c y una
    discriminabilidad d'.
    
    Distribución ruido   ~ N(0, 1)       → evento NO causado por el agente
    Distribución señal   ~ N(d', 1)      → evento SÍ causado por el agente
    
    El agente dice "fui yo" cuando la evidencia interna supera c.
    """
    p_acierto = 1 - stats.norm.cdf(criterio, loc=dprime, scale=1)
    p_fa      = 1 - stats.norm.cdf(criterio, loc=0,      scale=1)
    return p_acierto, p_fa


def criterio_optimo(dprime, valor_acierto, costo_fa=1.0, p_senal=0.5):
    """
    Criterio de decisión que maximiza la ganancia esperada.
    
    Un observador racional elige c* de manera que:
        β* = (p_ruido / p_señal) × (costo_FA / valor_acierto)
    donde β = f_ruido(c) / f_señal(c) es la razón de verosimilitudes.
    
    En términos de z-scores:
        c* = (d'/2) + (1/d') × ln(β*)
    
    Cuando valor_acierto sube, β* baja → c* baja → criterio más liberal
    (más aciertos y más falsas alarmas).
    """
    p_ruido  = 1 - p_senal
    beta_star = (p_ruido / p_senal) * (costo_fa / valor_acierto)
    beta_star = max(beta_star, 1e-6)          # evitar log(0)
    c_opt = (dprime / 2) + (1 / dprime) * np.log(beta_star)
    return c_opt


def curva_roc(dprime, n=300):
    """Genera la curva ROC para una d' dada."""
    fa_vals   = np.linspace(0.001, 0.999, n)
    hit_vals  = stats.norm.cdf(stats.norm.ppf(fa_vals) + dprime)
    return fa_vals, hit_vals


def auc_roc(dprime):
    """Área bajo la curva ROC (índice Az). Az = Φ(d'/√2)."""
    return stats.norm.cdf(dprime / np.sqrt(2))


def gradiente_temporal(demoras, fa_base, tau):
    """
    Probabilidad de falsa alarma como función de la demora entre
    la respuesta del agente y el evento no contingente.
    
    Decaimiento exponencial: P(FA | demora) = fa_base × exp(-τ × demora)
    
    Refleja que la contigüidad temporal opera como señal de causalidad:
    a mayor distancia temporal, menor es la "evidencia interna" de
    haber causado el evento.
    """
    return fa_base * np.exp(-tau * (demoras - demoras[0]))


# ─────────────────────────────────────────
# Parámetros fijos del experimento
# ─────────────────────────────────────────
DPRIME   = 1.5      # discriminabilidad ≈80% accuracy (Killeen, 1978)
COSTO_FA = 1.0      # costo de una falsa alarma (normalizado)
P_SENAL  = 0.5      # P(evento causado) = P(evento no causado) = 0.5
DEMORAS  = np.linspace(0.2, 1.0, 80)   # demoras en segundos

# Condiciones de pago reportadas por Killeen (1978):
# 1.8, 2.3, 2.8, 3.8 segundos de acceso a comida por acierto
CONDICIONES_PAGO = [
    (1.8, AZUL,    '1.8 s'),
    (2.3, VERDE,   '2.3 s'),
    (2.8, NARANJA, '2.8 s'),
    (3.8, ROJO,    '3.8 s'),
]

# ─────────────────────────────────────────
# Widgets
# ─────────────────────────────────────────
_style  = {'description_width': '230px'}
_layout = widgets.Layout(width='480px')

slider_criterio = widgets.FloatSlider(
    value=0.75,
    min=-2.5, max=3.5, step=0.05,
    description='Criterio del agente (c):',
    continuous_update=True,
    readout_format='.2f',
    style=_style, layout=_layout,
)

slider_valor = widgets.FloatSlider(
    value=2.3,
    min=1.0, max=4.5, step=0.1,
    description='Valor del acierto (segundos de comida):',
    continuous_update=True,
    readout_format='.1f',
    style=_style, layout=_layout,
)

slider_tau = widgets.FloatSlider(
    value=2.5,
    min=0.3, max=8.0, step=0.1,
    description='Pendiente del gradiente temporal (τ):',
    continuous_update=True,
    readout_format='.1f',
    style=_style, layout=_layout,
)

checkbox_optimo = widgets.Checkbox(
    value=True,
    description='Mostrar criterio óptimo para el valor actual',
    indent=False,
    style={'description_width': 'initial'},
)

out = widgets.Output()


# ─────────────────────────────────────────
# Función de actualización
# ─────────────────────────────────────────
def actualizar(change=None):
    c      = slider_criterio.value
    valor  = slider_valor.value
    tau    = slider_tau.value
    mostrar_opt = checkbox_optimo.value

    # Calcular estadísticos del criterio actual
    hit, fa = tasa_aciertos_y_fa(c, DPRIME)

    # Criterio óptimo para el valor actual
    c_opt         = criterio_optimo(DPRIME, valor, COSTO_FA, P_SENAL)
    hit_opt, fa_opt = tasa_aciertos_y_fa(c_opt, DPRIME)

    # Distribuciones
    x            = np.linspace(-4.5, 6.0, 400)
    dist_ruido   = stats.norm.pdf(x, 0,      1)
    dist_senal   = stats.norm.pdf(x, DPRIME, 1)

    # Curva ROC
    fa_roc, hit_roc = curva_roc(DPRIME)
    az              = auc_roc(DPRIME)

    # Curva de criterio óptimo vs valor del acierto
    valores_eje = np.linspace(1.0, 4.5, 200)
    c_opts      = [criterio_optimo(DPRIME, v, COSTO_FA, P_SENAL) for v in valores_eje]
    hits_opt    = [tasa_aciertos_y_fa(co, DPRIME)[0] for co in c_opts]
    fas_opt     = [tasa_aciertos_y_fa(co, DPRIME)[1] for co in c_opts]

    with out:
        clear_output(wait=True)

        fig = plt.figure(figsize=(15, 9.5))
        gs  = GridSpec(2, 3, figure=fig, hspace=0.50, wspace=0.42)

        # ══════════════════════════════════════════
        # Panel A: Distribuciones señal y ruido
        # ══════════════════════════════════════════
        ax_dist = fig.add_subplot(gs[0, :2])

        # Sombras de aciertos y falsas alarmas
        ax_dist.fill_between(
            x, dist_senal,
            where=(x >= c),
            alpha=0.30, color=VERDE,
            label=f'Aciertos: P(acierto) = {hit:.2f}'
        )
        ax_dist.fill_between(
            x, dist_ruido,
            where=(x >= c),
            alpha=0.35, color=NARANJA,
            label=f'Falsas alarmas: P(FA) = {fa:.2f}'
        )

        # Curvas de densidad
        ax_dist.plot(x, dist_ruido, color=NARANJA, lw=2.2,
                     label='Ruido: evento NO causado por el agente')
        ax_dist.plot(x, dist_senal, color=AZUL,    lw=2.2,
                     label='Señal: evento SÍ causado por el agente')

        # Criterio actual
        y_max = max(dist_ruido.max(), dist_senal.max())
        ax_dist.axvline(c, color=GRIS, lw=2, linestyle='--',
                        label=f'Criterio actual  c = {c:.2f}')

        # Criterio óptimo (opcional)
        if mostrar_opt:
            ax_dist.axvline(c_opt, color=ROJO, lw=1.8, linestyle=':',
                            label=f'Criterio óptimo c* = {c_opt:.2f}')

        # Flechas de d'
        ax_dist.annotate(
            '', xy=(DPRIME, y_max * 0.82), xytext=(0, y_max * 0.82),
            arrowprops=dict(arrowstyle='<->', color=GRIS, lw=1.5)
        )
        ax_dist.text(DPRIME / 2, y_max * 0.86, f"d' = {DPRIME}",
                     ha='center', color=GRIS, fontsize=10)

        ax_dist.set_xlabel("Evidencia interna de «fui yo la causa»")
        ax_dist.set_ylabel("Densidad de probabilidad")
        ax_dist.set_title(
            "A.  Distribuciones señal y ruido",
            fontweight='bold', loc='left'
        )
        ax_dist.set_xlim(-4.5, 6.0)
        ax_dist.set_ylim(0, y_max * 1.15)

        # Caja de resultados
        ax_dist.text(
            0.02, 0.97,
            f"P(acierto) = {hit:.2f}    P(falsa alarma) = {fa:.2f}    "
            f"Ganancia esperada = {hit * valor - fa * COSTO_FA:.2f}",
            transform=ax_dist.transAxes, fontsize=10,
            va='top',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#EBF4FF',
                      edgecolor=AZUL, alpha=0.85)
        )
        ax_dist.legend(fontsize=8.5, loc='upper right', framealpha=0.9)

        # ══════════════════════════════════════════
        # Panel B: Curva ROC
        # ══════════════════════════════════════════
        ax_roc = fig.add_subplot(gs[0, 2])

        ax_roc.plot(fa_roc, hit_roc, color=AZUL, lw=2.5,
                    label=f"d' = {DPRIME}  (Az = {az:.2f})")
        ax_roc.plot([0, 1], [0, 1], color=GRIS, lw=1.2, linestyle='--',
                    label='Azar (Az = 0.50)')

        # Punto del criterio actual
        ax_roc.scatter([fa], [hit], color=GRIS, s=110, zorder=5,
                       label=f'Criterio actual\n({fa:.2f}, {hit:.2f})')

        # Punto óptimo
        if mostrar_opt:
            ax_roc.scatter([fa_opt], [hit_opt], color=ROJO, marker='*',
                           s=200, zorder=6,
                           label=f'Criterio óptimo\n({fa_opt:.2f}, {hit_opt:.2f})')

        ax_roc.set_xlabel("P(falsa alarma)")
        ax_roc.set_ylabel("P(acierto)")
        ax_roc.set_title("B.  Curva ROC", fontweight='bold', loc='left')
        ax_roc.set_xlim(0, 1); ax_roc.set_ylim(0, 1)
        ax_roc.set_aspect('equal')
        ax_roc.legend(fontsize=7.5, loc='lower right', framealpha=0.9)

        # Nota de área
        ax_roc.text(0.05, 0.92,
                    f'Az = {az:.2f}\n≈ {az*100:.0f}% discriminación',
                    transform=ax_roc.transAxes, fontsize=9,
                    color=AZUL,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#EBF4FF',
                              edgecolor=AZUL, alpha=0.7))

        # ══════════════════════════════════════════
        # Panel C: Efecto del valor del acierto sobre criterio óptimo
        # ══════════════════════════════════════════
        ax_pago = fig.add_subplot(gs[1, :2])

        ax_pago.plot(valores_eje, hits_opt, color=VERDE,   lw=2.2,
                     label='P(acierto) óptimo')
        ax_pago.plot(valores_eje, fas_opt,  color=NARANJA, lw=2.2,
                     label='P(falsa alarma) óptima')

        # Línea vertical en valor actual
        ax_pago.axvline(valor, color=GRIS, lw=1.8, linestyle='--',
                        label=f'Valor actual = {valor:.1f} s')

        # Puntos del valor actual
        ax_pago.scatter([valor], [hit_opt], color=VERDE,   s=90, zorder=5)
        ax_pago.scatter([valor], [fa_opt],  color=NARANJA, s=90, zorder=5)

        # Marcas de las condiciones de Killeen
        for v_val, v_color, v_label in CONDICIONES_PAGO:
            h_k, f_k = tasa_aciertos_y_fa(
                criterio_optimo(DPRIME, v_val, COSTO_FA, P_SENAL), DPRIME
            )
            ax_pago.axvline(v_val, color=v_color, lw=0.8,
                            linestyle=':', alpha=0.6)

        ax_pago.set_xlabel("Valor del acierto (segundos de acceso a comida)")
        ax_pago.set_ylabel("Probabilidad")
        ax_pago.set_title(
            "C.  Efecto del valor del acierto sobre el criterio óptimo\n"
            "     (Resultado 2 de Killeen, 1978)",
            fontweight='bold', loc='left'
        )
        ax_pago.legend(fontsize=9, framealpha=0.9)
        ax_pago.set_ylim(0, 1)

        # Anotación pedagógica
        ax_pago.text(
            1.15, 0.5,
            "↑ Valor\n→ criterio\n  más liberal\n→ más aciertos\n  y más FA",
            transform=ax_pago.transAxes, fontsize=9,
            va='center', color=GRIS,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF5EB',
                      edgecolor=NARANJA, alpha=0.85)
        )

        # ══════════════════════════════════════════
        # Panel D: Gradiente temporal de falsas alarmas
        # ══════════════════════════════════════════
        ax_grad = fig.add_subplot(gs[1, 2])

        for v_val, v_color, v_label in CONDICIONES_PAGO:
            c_v   = criterio_optimo(DPRIME, v_val, COSTO_FA, P_SENAL)
            fa_v  = tasa_aciertos_y_fa(c_v, DPRIME)[1]
            fa_t  = gradiente_temporal(DEMORAS, fa_v, tau)
            ax_grad.plot(DEMORAS, fa_t, color=v_color, lw=1.9,
                         label=f'{v_label}')

        ax_grad.set_xlabel("Demora entre respuesta y evento\nno contingente (segundos)")
        ax_grad.set_ylabel("P(falsa alarma)")
        ax_grad.set_title(
            "D.  Gradiente temporal de\n     falsas alarmas\n"
            "     (Resultado 3 de Killeen, 1978)",
            fontweight='bold', loc='left'
        )
        ax_grad.legend(title='Valor del acierto', fontsize=8,
                       framealpha=0.9)
        ax_grad.set_ylim(0, 1)
        ax_grad.set_xlim(DEMORAS[0], DEMORAS[-1])

        # Anotación pedagógica
        ax_grad.text(
            0.50, 0.35,
            "La contigüidad opera\ncomo señal de causalidad:\na mayor demora,\nmenos falsas alarmas",
            transform=ax_grad.transAxes, fontsize=8.5,
            va='center', ha='center', color=GRIS,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#F0FFF4',
                      edgecolor=VERDE, alpha=0.85)
        )

        plt.suptitle(
            "Simulador 7.2 — Detección de causalidad: experimento de Killeen (1978)",
            fontsize=14, fontweight='bold', y=1.01
        )
        plt.show()


# ─────────────────────────────────────────
# Encabezado descriptivo
# ─────────────────────────────────────────
cabecera = widgets.HTML(value="""
<div style="background:#EBF4FF; border-left:5px solid #2C5282;
            padding:14px 18px; margin-bottom:10px; font-family:Georgia,serif;">
  <div style="font-size:16px; font-weight:bold; color:#2C5282; margin-bottom:6px;">
    Simulador 7.2 — Detección de causalidad
  </div>
  <div style="font-size:13px; color:#2D3748; line-height:1.6;">
    Una paloma (o tú) debe decidir: <em>«¿Fui yo la causa de que la tecla se apagara?»</em><br>
    El evento puede haber ocurrido porque el agente picó la tecla, o por un pseudo-picotazo
    generado por la computadora. Las dos posibilidades producen <em>distribuciones internas</em>
    que se superponen.<br><br>
    <b>Panel A</b> — Ajusta el criterio de decisión y observa cómo cambian los aciertos y las falsas alarmas.<br>
    <b>Panel B</b> — Sigue el punto correspondiente en la curva ROC.<br>
    <b>Panel C</b> — Cambia el valor del acierto y observa cómo el observador racional desplaza su criterio.<br>
    <b>Panel D</b> — Observa cómo la probabilidad de falsa alarma disminuye con la demora temporal.
  </div>
</div>
""")

separador = widgets.HTML(
    value='<hr style="border:1px solid #CBD5E0; margin:6px 0;">'
)

etiqueta_controles = widgets.HTML(
    value='<b style="font-family:Georgia,serif; font-size:13px;">Parámetros ajustables:</b>'
)

panel_controles = widgets.VBox([
    cabecera,
    separador,
    etiqueta_controles,
    slider_criterio,
    slider_valor,
    slider_tau,
    checkbox_optimo,
    separador,
])

# Vincular widgets
slider_criterio.observe(actualizar, names='value')
slider_valor.observe(actualizar,    names='value')
slider_tau.observe(actualizar,      names='value')
checkbox_optimo.observe(actualizar, names='value')

# Mostrar
display(panel_controles, out)
actualizar()
