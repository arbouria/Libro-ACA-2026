"""
╔══════════════════════════════════════════════════════════════════════╗
║  Simulador 15.1 – Maximización Momentánea y Mejoramiento            ║
║  Capítulo 15: El Control Local del Comportamiento de Elección        ║
║  Aprendizaje y Comportamiento Adaptable: Principios y Modelos        ║
║  Arturo Bouzas · UNAM                                                ║
╚══════════════════════════════════════════════════════════════════════╝

Instalación (solo la primera vez en Colab):
    !pip install ipywidgets --quiet

Uso:
    Ejecuta todas las celdas en orden. Los controles permiten explorar
    dos modelos de elección local: maximización momentánea y mejoramiento.
"""

# ─────────────────────────────────────────────────────────────────────────────
# CELDA 1 — Dependencias
# ─────────────────────────────────────────────────────────────────────────────
import sys

try:
    import ipywidgets as widgets
    from IPython.display import display, HTML, clear_output
    print("✓ ipywidgets disponible")
except ImportError:
    print("Instalando ipywidgets...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "ipywidgets", "-q"])
    import ipywidgets as widgets
    from IPython.display import display, HTML, clear_output

import numpy as np
import matplotlib
matplotlib.use("module://ipympl.backend_nbagg") if "google.colab" not in sys.modules else None
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────────────────
# CELDA 2 — Paleta y estilo
# ─────────────────────────────────────────────────────────────────────────────

AZUL    = "#2C5282"
NARANJA = "#C05621"
VERDE   = "#276749"
GRIS    = "#718096"
GRIS_L  = "#EBF4FF"

def estilo(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRIS)
    ax.spines["bottom"].set_color(GRIS)
    ax.tick_params(colors=GRIS, labelsize=9)
    ax.xaxis.label.set_color(GRIS)
    ax.yaxis.label.set_color(GRIS)

CABECERA = """
<div style="background:#2C5282;color:white;padding:16px 20px;border-radius:8px;
            margin-bottom:14px;font-family:Georgia,serif;">
  <div style="font-size:13px;opacity:0.8;margin-bottom:4px;">
    Capítulo 15 · Aprendizaje y Comportamiento Adaptable
  </div>
  <div style="font-size:18px;font-weight:bold;">
    Simulador 15.1 — Control Local de la Elección
  </div>
  <div style="font-size:12px;opacity:0.75;margin-top:6px;">
    Compara maximización momentánea y mejoramiento en programas concurrentes IV-IV
  </div>
</div>
"""

EXPLICACION = """
<div style="background:#EBF4FF;border-left:4px solid #2C5282;padding:12px 16px;
            margin-bottom:14px;border-radius:0 6px 6px 0;font-family:Georgia,serif;
            font-size:13px;color:#2D3748;line-height:1.6;">
  <b>¿Qué hace este simulador?</b><br>
  Simula una sesión de elección libre en un programa concurrente IV₁ – IV₂.
  Puedes comparar dos estrategias:
  <ul style="margin:6px 0 0 0;padding-left:20px;">
    <li><b style="color:#2C5282">Maximización momentánea:</b> el agente elige en cada ensayo
        la opción con mayor probabilidad instantánea de refuerzo.</li>
    <li><b style="color:#C05621">Mejoramiento:</b> el agente compara las tasas locales de
        refuerzo (reforzadores por tiempo dedicado) y se mueve hacia la más rentable.</li>
  </ul>
  Observa cómo cada estrategia converge —o no— a igualación al final de la sesión.
</div>
"""

# ─────────────────────────────────────────────────────────────────────────────
# CELDA 3 — Funciones de simulación
# ─────────────────────────────────────────────────────────────────────────────

def simular_iv(media_s, n_ensayos, semilla=None):
    """
    Genera los tiempos (en ensayos) en que se arma un reforzador en un
    programa IV con media `media_s` ensayos.
    Retorna: array booleano de longitud n_ensayos (True = reforzador armado).
    """
    rng = np.random.default_rng(semilla)
    intervalos = rng.geometric(p=1/media_s, size=n_ensayos*3)
    tiempos = np.cumsum(intervalos)
    tiempos = tiempos[tiempos <= n_ensayos]
    disponible = np.zeros(n_ensayos, dtype=bool)
    for t in tiempos:
        disponible[t-1] = True
    return disponible

def simular_maximizacion_momentanea(iv1, iv2, n_ensayos=300, semilla=42,
                                      t_desde_1_init=1, t_desde_2_init=1):
    """
    Modelo de maximización momentánea — versión probabilística (Shimp, 1966).

    En lugar del máximo estricto (que produce carreras largas en una opción),
    se usa la regla de Luce aplicada a las probabilidades momentáneas:
        P(elegir opción 1) = p1 / (p1 + p2)
    Esto captura la sensibilidad al estado momentáneo del entorno con
    variabilidad ensayo a ensayo, tal como se observa empíricamente.

    Los reforzadores se acumulan correctamente: el intervalo sigue corriendo
    mientras el agente está en la otra opción y el reforzador espera armado.

    iv1, iv2           : medias de los programas IV (en ensayos).
    t_desde_*_init     : estado inicial de los contadores (para sesiones en serie).
    """
    rng = np.random.default_rng(semilla)

    # Estado de disponibilidad (los reforzadores se acumulan)
    armado1 = False
    armado2 = False

    t_desde_1 = t_desde_1_init
    t_desde_2 = t_desde_2_init

    elecciones = []
    ref1 = ref2 = 0
    t_asignado_1 = t_asignado_2 = 0

    for ensayo in range(n_ensayos):
        # Armar reforzador si el intervalo se cumple y no hay uno ya armado
        if not armado1 and rng.random() < 1 / iv1:
            armado1 = True
        if not armado2 and rng.random() < 1 / iv2:
            armado2 = True

        # Probabilidad momentánea: P ≈ 1 − (1 − 1/IV)^t
        p1 = 1 - (1 - 1 / iv1) ** t_desde_1
        p2 = 1 - (1 - 1 / iv2) ** t_desde_2

        # Regla de Luce: elección proporcional a probabilidades momentáneas
        total_p = p1 + p2
        prob_1 = p1 / total_p if total_p > 0 else 0.5
        opcion = 1 if rng.random() < prob_1 else 2

        elecciones.append(opcion)

        if opcion == 1:
            t_asignado_1 += 1
            t_desde_1 = 1
            t_desde_2 += 1
            if armado1:
                ref1 += 1
                armado1 = False
        else:
            t_asignado_2 += 1
            t_desde_2 = 1
            t_desde_1 += 1
            if armado2:
                ref2 += 1
                armado2 = False

    elecciones = np.array(elecciones)
    return elecciones, ref1, ref2, t_asignado_1, t_asignado_2, t_desde_1, t_desde_2


def simular_mejoramiento(iv1, iv2, t1_inicial=0.5, n_sesiones=30,
                          n_ensayos_sesion=300, eta=0.15, semilla=42):
    """
    Modelo de mejoramiento (Herrnstein & Vaughan, 1980).
    En cada sesión, el agente asigna T1 del tiempo a la opción 1 y
    (1-T1) a la opción 2. Calcula las tasas locales y actualiza T1
    en la dirección de la mayor tasa.

    iv1, iv2  : medias de los programas IV (en ensayos/visita).
    t1_inicial: proporción inicial de tiempo para opción 1.
    n_sesiones: número de sesiones simuladas.
    eta        : tasa de cambio del sistema (velocidad de convergencia).

    Retorna: arrays de T1 por sesión, tasas locales, tasas de igualación.
    """
    rng = np.random.default_rng(semilla)

    # Reforzadores máximos por sesión (supuesto: se recolectan todos)
    r1_max = n_ensayos_sesion / iv1
    r2_max = n_ensayos_sesion / iv2

    T1_hist = [t1_inicial]
    local1_hist = []
    local2_hist = []

    T1 = t1_inicial

    for sesion in range(n_sesiones):
        T2 = 1 - T1

        # Tasa local: reforzadores obtenidos / tiempo dedicado
        # (Añadimos ruido pequeño para simular variabilidad natural)
        ruido = rng.normal(0, 0.02)
        local1 = (r1_max / T1) * (1 + ruido) if T1 > 0.02 else float("inf")
        local2 = (r2_max / T2) * (1 + ruido) if T2 > 0.02 else float("inf")

        local1_hist.append(local1)
        local2_hist.append(local2)

        # Regla de mejoramiento: moverse hacia la opción más rentable
        diferencia = local1 - local2
        delta = eta * np.tanh(diferencia / 20)   # función suave para estabilidad
        T1 = np.clip(T1 + delta, 0.05, 0.95)
        T1_hist.append(T1)

    # Igualación predicha
    T1_iguala = r1_max / (r1_max + r2_max)

    return (np.array(T1_hist[:-1]),
            np.array(local1_hist),
            np.array(local2_hist),
            T1_iguala)


# ─────────────────────────────────────────────────────────────────────────────
# CELDA 4 — Interfaz interactiva
# ─────────────────────────────────────────────────────────────────────────────

display(HTML(CABECERA + EXPLICACION))

# ── Controles ────────────────────────────────────────────────────────────────
w = lambda desc, **kw: widgets.IntSlider(description=desc, style={"description_width":"200px"},
                                          layout=widgets.Layout(width="420px"), **kw)
wf = lambda desc, **kw: widgets.FloatSlider(description=desc, style={"description_width":"200px"},
                                             layout=widgets.Layout(width="420px"), **kw)

iv1_w = w("IV₁ (media, en ensayos)",   min=5,  max=60, step=5,  value=15)
iv2_w = w("IV₂ (media, en ensayos)",   min=5,  max=60, step=5,  value=30)
t1_w  = wf("Proporción inicial T₁",     min=0.1, max=0.9, step=0.05, value=0.5)
ses_w = w("Número de sesiones",         min=5,  max=60, step=5,  value=25)
eta_w = wf("Velocidad de convergencia η", min=0.02, max=0.40, step=0.02, value=0.12)
sem_w = w("Semilla aleatoria",          min=1,  max=100, step=1, value=42)

modelo_w = widgets.ToggleButtons(
    options=["Mejoramiento", "Maximización momentánea", "Ambos modelos"],
    description="Modelo:",
    style={"description_width":"80px", "button_width":"170px"},
    layout=widgets.Layout(margin="10px 0"),
)

boton = widgets.Button(
    description="▶  Simular",
    button_style="",
    style={"button_color": AZUL, "font_weight": "bold"},
    layout=widgets.Layout(width="160px", height="36px"),
)

salida = widgets.Output()

controles = widgets.VBox([
    widgets.HTML("<b style='font-family:Georgia;color:#2C5282'>Parámetros del entorno</b>"),
    widgets.HBox([iv1_w, iv2_w]),
    widgets.HTML("<b style='font-family:Georgia;color:#2C5282'>Parámetros del modelo</b>"),
    widgets.HBox([t1_w, eta_w]),
    widgets.HBox([ses_w, sem_w]),
    modelo_w,
    boton,
    salida,
])

display(controles)

# ── Función de graficación ────────────────────────────────────────────────────

def graficar(b):
    with salida:
        clear_output(wait=True)

        iv1  = iv1_w.value
        iv2  = iv2_w.value
        t1_0 = t1_w.value
        nses = ses_w.value
        eta  = eta_w.value
        sem  = sem_w.value
        mod  = modelo_w.value

        T1_iguala = iv2 / (iv1 + iv2)   # igualación predicha

        fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
        fig.subplots_adjust(wspace=0.35)
        ax1, ax2 = axes

        sesiones = np.arange(1, nses + 1)

        if mod in ("Mejoramiento", "Ambos modelos"):
            T1, loc1, loc2, _ = simular_mejoramiento(
                iv1, iv2, t1_0, nses, eta=eta, semilla=sem)
            ax1.plot(sesiones, T1, "-o", color=NARANJA, lw=2, ms=4,
                     label="Mejoramiento")
            ax2.plot(sesiones, loc1, "-",  color=AZUL,   lw=1.8,
                     label="Tasa local opción 1 (IV₁)")
            ax2.plot(sesiones, loc2, "--", color=NARANJA,lw=1.8,
                     label="Tasa local opción 2 (IV₂)")

        if mod in ("Maximización momentánea", "Ambos modelos"):
            all_t1 = []
            # Los contadores t_desde se pasan entre sesiones para que el
            # estado del sistema sea continuo, igual que en el experimento real.
            # Se inicializan proporcionales a T1_inicial.
            td1 = max(2, int((1 - t1_0) * 20))
            td2 = max(2, int(t1_0 * 20))
            for bloque in range(nses):
                res = simular_maximizacion_momentanea(
                    iv1, iv2, n_ensayos=150, semilla=sem + bloque,
                    t_desde_1_init=td1, t_desde_2_init=td2)
                elecciones, r1, r2, ta1, ta2, td1, td2 = res
                total = ta1 + ta2
                all_t1.append(ta1 / total if total > 0 else 0.5)
            all_t1 = np.array(all_t1)
            # Media móvil ligera para reducir ruido manteniendo la tendencia
            smooth = np.convolve(all_t1, np.ones(3) / 3, mode="valid")
            s_ses  = np.arange(2, 2 + len(smooth))
            ax1.plot(s_ses, smooth, "-s", color=VERDE, lw=2, ms=4,
                     label="Maximización momentánea")

        # Línea de igualación
        ax1.axhline(T1_iguala, color=GRIS, lw=1.5, ls=":",
                    label=f"Igualación predicha (T₁ = {T1_iguala:.2f})")
        ax1.axhline(t1_0, color=GRIS, lw=1, ls="--", alpha=0.4,
                    label=f"T₁ inicial ({t1_0:.2f})")

        ax1.set_xlabel("Sesión", color=GRIS, fontsize=10)
        ax1.set_ylabel("Proporción de tiempo en opción 1 (T₁)", color=GRIS, fontsize=10)
        ax1.set_ylim(0, 1)
        ax1.set_xlim(0, nses + 1)
        ax1.legend(frameon=False, fontsize=8.5)
        ax1.set_title(f"Convergencia a igualación\n(IV₁ = {iv1} ensayos, IV₂ = {iv2} ensayos)",
                      color=AZUL, fontsize=10)
        estilo(ax1)

        # Panel derecho: tasas locales (solo mejoramiento)
        if mod in ("Mejoramiento", "Ambos modelos"):
            ax2.axhline(loc1[-1], color=GRIS, lw=1, ls=":",
                        label="Equilibrio")
            ax2.set_xlabel("Sesión", color=GRIS, fontsize=10)
            ax2.set_ylabel("Tasa local de refuerzo\n(reforzadores / tiempo asignado)",
                           color=GRIS, fontsize=10)
            ax2.set_xlim(0, nses + 1)
            ax2.legend(frameon=False, fontsize=8.5)
            ax2.set_title("Tasas locales durante el proceso\n(modelo de mejoramiento)",
                          color=AZUL, fontsize=10)
            estilo(ax2)
        else:
            ax2.set_visible(False)

        # Resumen numérico
        r1_max = 300 / iv1
        r2_max = 300 / iv2
        r_eq   = r1_max / (T1_iguala) if T1_iguala > 0 else float("inf")
        info = (f"IV₁ = {iv1} ensayos → {r1_max:.1f} ref/sesión  |  "
                f"IV₂ = {iv2} ensayos → {r2_max:.1f} ref/sesión\n"
                f"Igualación predicha: T₁ = {T1_iguala:.3f}  "
                f"(tasa local de equilibrio ≈ {r_eq:.1f} ref/sesión por unidad de tiempo)")
        fig.text(0.5, -0.04, info, ha="center", fontsize=8.5, color=GRIS)

        plt.tight_layout()
        plt.show()


boton.on_click(graficar)
graficar(None)   # render inicial


# ─────────────────────────────────────────────────────────────────────────────
# CELDA 5 — Ejercicios
# ─────────────────────────────────────────────────────────────────────────────

ejercicios_html = """
<div style="background:#F7FAFC;border:1px solid #CBD5E0;border-radius:8px;
            padding:18px 22px;font-family:Georgia,serif;font-size:13px;
            color:#2D3748;line-height:1.7;margin-top:16px;">
  <div style="font-size:15px;font-weight:bold;color:#2C5282;margin-bottom:12px;">
    Ejercicios guiados
  </div>

  <b>Ejercicio 1 (básico) — Equilibrio y relación de programas</b><br>
  Configura IV₁ = 15 y IV₂ = 30, con T₁ inicial = 0.5, y corre el modelo de mejoramiento.
  <ul>
    <li>¿A qué valor de T₁ converge el sistema?</li>
    <li>Calcula manualmente la igualación predicha: T₁* = IV₂ / (IV₁ + IV₂).
        ¿Coincide con lo que muestra el simulador?</li>
    <li>Ahora cambia a IV₁ = 20, IV₂ = 20. ¿Qué predices antes de correr?
        ¿Por qué?</li>
  </ul>

  <b>Ejercicio 2 (intermedio) — Punto de partida y convergencia</b><br>
  Mantén IV₁ = 10, IV₂ = 40. Corre el modelo de mejoramiento tres veces
  cambiando T₁ inicial a 0.1, 0.5 y 0.9.
  <ul>
    <li>¿Convergen al mismo punto de equilibrio independientemente del valor inicial?</li>
    <li>¿Difiere la velocidad de convergencia? ¿Por qué esperarías que sí o que no?</li>
    <li>¿Qué interpretación conductual tiene el valor T₁ inicial?</li>
  </ul>

  <b>Ejercicio 3 (intermedio) — Velocidad de adaptación</b><br>
  Usa IV₁ = 15, IV₂ = 45. Compara η = 0.06 y η = 0.30.
  <ul>
    <li>¿Cuántas sesiones tarda cada sistema en alcanzar el equilibrio?</li>
    <li>¿Un valor de η alto es siempre mejor? ¿Qué problema podría generar
        en un entorno donde los programas cambian frecuentemente?</li>
  </ul>

  <b>Ejercicio 4 (avanzado) — Comparación de modelos</b><br>
  Selecciona "Ambos modelos" con IV₁ = 15, IV₂ = 30.
  <ul>
    <li>¿Cuál modelo converge más rápido a igualación?</li>
    <li>¿Cuál produce más variabilidad sesión a sesión?
        ¿A qué se debe esa diferencia?</li>
    <li>Maximización momentánea asume que el organismo computa probabilidades
        de refuerzo instantáneas. Mejoramiento asume que estima tasas locales
        sobre tiempo reciente. ¿Qué experimento permitiría discriminar entre
        los dos mecanismos sin observar el equilibrio final?
        (Pista: piensa en la secuencia de elecciones ensayo a ensayo.)</li>
  </ul>
</div>
"""

display(HTML(ejercicios_html))
