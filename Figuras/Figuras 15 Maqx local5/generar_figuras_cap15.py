"""
Figuras del Capítulo 15: El Control Local del Comportamiento de Elección
Aprendizaje y Comportamiento Adaptable: Principios y Modelos
Arturo Bouzas

Genera: fig15_1, fig15_2, fig15_3, fig15_4 en PNG a 2.5× escala.
Paleta: azul #2C5282, naranja #C05621, verde #276749, gris #718096.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import os

OUT = "/home/claude/figs"
os.makedirs(OUT, exist_ok=True)

# ── Paleta y estilo ────────────────────────────────────────────────────────────
AZUL    = "#2C5282"
NARANJA = "#C05621"
VERDE   = "#276749"
GRIS    = "#718096"
GRIS_L  = "#E2E8F0"

def estilo_base(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRIS)
    ax.spines["bottom"].set_color(GRIS)
    ax.tick_params(colors=GRIS, labelsize=9)
    ax.xaxis.label.set_color(GRIS)
    ax.yaxis.label.set_color(GRIS)

FONT_TITULO = {"family": "Georgia", "size": 10, "color": AZUL, "weight": "bold"}
FONT_EJE    = {"family": "Georgia", "size": 9,  "color": GRIS}
FONT_CAP    = {"family": "Georgia", "size": 7.5, "color": GRIS}

SCALE = 2.5  # resolución para Quarto

# ══════════════════════════════════════════════════════════════════════════════
# Figura 15.1  Nevin (1969) – programa IV-IV discreto
#   Panel superior: probabilidad de refuerzo para la opción alterna
#              en función del número de elecciones consecutivas en la opción actual
#   Panel inferior: probabilidad observada de cambiar de opción
# ══════════════════════════════════════════════════════════════════════════════

def fig15_1():
    n = np.arange(1, 11)

    # Panel superior: la probabilidad de refuerzo en la alternativa crece
    # con las respuestas consecutivas en la opción actual.
    # Para un IV exponencial, p(refuerzo disponible | k pasos) ≈ 1 − exp(−k/μ)
    # IV 1' (μ=1): la alternativa es IV 3' (μ=3), pero el tiempo sigue corriendo
    # Usamos valores estilizados basados en la figura de Nevin (1969, Fig. 4)
    p_refuerzo_roja  = 0.11 + 0.037*n + 0.002*n**2   # creciente
    p_refuerzo_roja  = np.clip(p_refuerzo_roja, 0, 0.50)
    p_refuerzo_verde = 0.14 + 0.005*n                 # aproximadamente plana
    p_refuerzo_verde = np.clip(p_refuerzo_verde, 0, 0.25)

    # Panel inferior: probabilidad de cambiar (empírica) — NO crece; tendencia plana o decreciente
    # Datos estilizados para tres sujetos (Nevin, 1969, Fig. 4, panel inferior)
    p_cambio_s1 = 0.30 - 0.012*n + np.array([0, 0.01, -0.01, 0.01, -0.01,
                                               0.01, -0.01, 0, 0.01, -0.01])
    p_cambio_s2 = 0.26 - 0.015*n + np.array([0, 0.01, 0, -0.01, 0.01,
                                               -0.01, 0, 0.01, -0.01, 0])
    p_cambio_s3 = 0.23 - 0.018*n + np.array([0, -0.01, 0.01, 0, -0.01,
                                               0.01, -0.01, 0, 0.01, -0.01])
    p_cambio_s1 = np.clip(p_cambio_s1, 0.05, 0.45)
    p_cambio_s2 = np.clip(p_cambio_s2, 0.05, 0.45)
    p_cambio_s3 = np.clip(p_cambio_s3, 0.05, 0.45)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(4.5, 5.5))
    fig.subplots_adjust(hspace=0.45)

    # Panel superior
    ax1.plot(n, p_refuerzo_roja,  "o-", color=NARANJA, lw=1.5, ms=5,
             label="Tecla alternativa (IV 3')")
    ax1.plot(n, p_refuerzo_verde, "s--", color=AZUL,   lw=1.5, ms=5,
             label="Tecla actual (IV 1')")
    ax1.set_ylabel("P (reforzador disponible)", **FONT_EJE)
    ax1.set_ylim(0, 0.55)
    ax1.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])
    ax1.set_xticks(n)
    ax1.set_xticklabels([])
    ax1.legend(fontsize=8, frameon=False, loc="upper left",
               prop={"family": "Georgia", "size": 8})
    ax1.set_title("Panel A — Probabilidad de refuerzo disponible", **FONT_TITULO)
    estilo_base(ax1)

    # Panel inferior — predicción vs. observación
    ax2.plot(n, p_cambio_s1, "o-",  color=AZUL,   lw=1.4, ms=4, alpha=0.9)
    ax2.plot(n, p_cambio_s2, "s-",  color=VERDE,  lw=1.4, ms=4, alpha=0.9)
    ax2.plot(n, p_cambio_s3, "^-",  color=NARANJA,lw=1.4, ms=4, alpha=0.9)

    # Anotación de la predicción del modelo (creciente)
    p_predicha = 0.10 + 0.035*n
    ax2.plot(n, p_predicha, "--", color=GRIS, lw=1.2,
             label="Predicción del modelo")
    ax2.set_xlabel("Elecciones consecutivas de la opción actual", **FONT_EJE)
    ax2.set_ylabel("P (cambiar a opción alterna)", **FONT_EJE)
    ax2.set_ylim(0, 0.50)
    ax2.set_yticks([0, 0.1, 0.2, 0.3, 0.4])
    ax2.set_xticks(n)

    # Leyenda manual para sujetos
    handles = [
        mpatches.Patch(color=AZUL,    label="Sujeto 58"),
        mpatches.Patch(color=VERDE,   label="Sujeto 59"),
        mpatches.Patch(color=NARANJA, label="Sujeto 60"),
        plt.Line2D([0], [0], color=GRIS, ls="--", label="Predicción del modelo"),
    ]
    ax2.legend(handles=handles, fontsize=7.5, frameon=False,
               prop={"family": "Georgia", "size": 7.5})
    ax2.set_title("Panel B — Probabilidad observada de cambio", **FONT_TITULO)
    estilo_base(ax2)

    # Nota de figura
    fig.text(0.08, 0.01,
             "Figura 15.1.  Mientras la probabilidad de refuerzo en la alternativa crece con cada\n"
             "respuesta consecutiva a la opción actual (Panel A), la probabilidad de cambiar\n"
             "no aumenta — contrariamente a la predicción del modelo de maximización momentánea (Panel B).",
             ha="left", va="bottom", fontsize=6.5, color=GRIS,
             fontfamily="Georgia", wrap=True)

    plt.savefig(f"{OUT}/fig15_1_nevin_iv_iv.png", dpi=150*SCALE,
                bbox_inches="tight", facecolor="white")
    plt.close()
    print("✓  fig15_1")


# ══════════════════════════════════════════════════════════════════════════════
# Figura 15.2  Perseverancia — Nevin (1969) y Silberberg et al. (1978)
#   Probabilidad de cambiar de tecla como función del número de
#   picotazos consecutivos previos al cambio.
# ══════════════════════════════════════════════════════════════════════════════

def fig15_2():
    x = np.array([1, 2, 3])

    # Datos estilizados basados en la Figura 2 de los artículos combinados
    # Curva superior (cambio hacia verde, ambos estudios)
    nevin_verde    = np.array([0.74, 0.69, 0.65])
    silberg_verde  = np.array([0.82, 0.73, 0.70])

    # Curva inferior (cambio hacia rojo)
    nevin_rojo     = np.array([0.21, 0.18, 0.17])
    silberg_rojo   = np.array([0.34, 0.25, 0.21])

    fig, ax = plt.subplots(figsize=(4.2, 3.8))

    ax.plot(x, silberg_verde, "o-",  color=AZUL,   lw=1.8, ms=7,
            label="Silberberg et al. (1978) – R→V")
    ax.plot(x, nevin_verde,   "o--", color=AZUL,   lw=1.8, ms=7,
            mfc="white", label="Nevin (1969) – R→V")
    ax.plot(x, silberg_rojo,  "s-",  color=NARANJA,lw=1.8, ms=7,
            label="Silberberg et al. (1978) – V→R")
    ax.plot(x, nevin_rojo,    "s--", color=NARANJA,lw=1.8, ms=7,
            mfc="white", label="Nevin (1969) – V→R")

    # Anotaciones de flecha
    ax.annotate("R→V", xy=(3, nevin_verde[-1]), xytext=(3.1, nevin_verde[-1]),
                fontsize=8, color=AZUL, fontfamily="Georgia",
                va="center")
    ax.annotate("V→R", xy=(3, nevin_rojo[-1]), xytext=(3.1, nevin_rojo[-1]),
                fontsize=8, color=NARANJA, fontfamily="Georgia",
                va="center")

    ax.set_xlabel("Picotazos consecutivos previos al cambio", **FONT_EJE)
    ax.set_ylabel("Probabilidad de cambiar de tecla", **FONT_EJE)
    ax.set_xticks([1, 2, 3])
    ax.set_xlim(0.7, 3.5)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

    handles = [
        plt.Line2D([0],[0], color=AZUL,   lw=1.8, ms=7, marker="o",
                   label="Silberberg et al. (1978)"),
        plt.Line2D([0],[0], color=AZUL,   lw=1.8, ms=7, marker="o",
                   ls="--", mfc="white", label="Nevin (1969)"),
    ]
    ax.legend(handles=handles, frameon=False, fontsize=8,
              prop={"family":"Georgia","size":8}, loc="center right")
    ax.set_title("Perseverancia en la elección", **FONT_TITULO)
    estilo_base(ax)

    fig.text(0.08, -0.04,
             "Figura 15.2.  La probabilidad de cambiar de tecla no aumenta con el número de\n"
             "respuestas consecutivas previas — es plana o ligeramente decreciente en ambos estudios.\n"
             "R→V = cambio de tecla roja a verde; V→R = cambio de verde a roja.",
             ha="left", va="top", fontsize=6.5, color=GRIS, fontfamily="Georgia")

    plt.savefig(f"{OUT}/fig15_2_perseverancia.png", dpi=150*SCALE,
                bbox_inches="tight", facecolor="white")
    plt.close()
    print("✓  fig15_2")


# ══════════════════════════════════════════════════════════════════════════════
# Figura 15.3  Williams (1985) – programa RV-IV discreto
#   Panel izquierdo:  P(refuerzo disponible en IV | ensayos desde última resp. IV)
#   Panel derecho: P(respuesta al IV | ensayos desde última resp. IV)
# ══════════════════════════════════════════════════════════════════════════════

def fig15_3():
    bins = np.array([1, 2, 3, 4.5, 7])  # puntos agrupados

    # Panel izquierdo: probabilidad de refuerzo disponible — creciente
    # Estilizada de Williams (1985), Fig. 3, condición IV 90" p=.15
    p_ref = np.array([0.10, 0.18, 0.27, 0.38, 0.46])

    # Línea del RV (constante)
    p_rv  = np.full_like(bins, 0.15, dtype=float)

    # Panel derecho: probabilidad de responder al IV — plana / levemente decreciente
    # Cuatro sujetos individuales
    np.random.seed(42)
    sujetos = {
        "S-2":  np.array([0.50, 0.47, 0.46, 0.44, 0.43]),
        "S-8":  np.array([0.54, 0.52, 0.50, 0.49, 0.48]),
        "S-14": np.array([0.60, 0.55, 0.52, 0.50, 0.49]),
        "S-20": np.array([0.45, 0.44, 0.43, 0.44, 0.44]),
    }
    colores_s = [AZUL, VERDE, NARANJA, GRIS]
    marcas_s  = ["o", "s", "^", "D"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.8))
    fig.subplots_adjust(wspace=0.35)

    # Panel izquierdo
    ax1.plot(bins, p_ref, "o-", color=AZUL,   lw=1.8, ms=6,
             label="IV disponible")
    ax1.axhline(p_rv[0], color=NARANJA, lw=1.5, ls="--",
                label=f"RV (p = {p_rv[0]})")
    ax1.set_xlabel("Ensayos desde última resp. IV", **FONT_EJE)
    ax1.set_ylabel("P (reforzador disponible)", **FONT_EJE)
    ax1.set_ylim(0, 0.6)
    ax1.set_xticks(bins)
    ax1.set_xticklabels(["1","2","3","4–5","≥6"])
    ax1.legend(frameon=False, fontsize=8, prop={"family":"Georgia","size":8})
    ax1.set_title("Panel A — Disponibilidad de refuerzo", **FONT_TITULO)
    estilo_base(ax1)

    # Panel derecho
    for (nombre, vals), col, mar in zip(sujetos.items(), colores_s, marcas_s):
        ax2.plot(bins, vals, marker=mar, color=col, lw=1.4, ms=5,
                 label=nombre, alpha=0.9)
    ax2.set_xlabel("Ensayos desde última resp. IV", **FONT_EJE)
    ax2.set_ylabel("P (respuesta al IV)", **FONT_EJE)
    ax2.set_ylim(0, 0.9)
    ax2.set_xticks(bins)
    ax2.set_xticklabels(["1","2","3","4–5","≥6"])
    ax2.legend(frameon=False, fontsize=8, prop={"family":"Georgia","size":8},
               loc="upper right")
    ax2.set_title("Panel B — Comportamiento observado", **FONT_TITULO)
    estilo_base(ax2)

    fig.text(0.08, -0.04,
             "Figura 15.3.  Programa concurrente RV-IV de ensayos discretos (Williams, 1985). "
             "Aunque la probabilidad de\n"
             "que un reforzador esté disponible en la tecla IV crece con el número de ensayos "
             "desde la última respuesta\n"
             "IV (Panel A), la probabilidad de responder al IV es plana o ligeramente decreciente "
             "para todos los sujetos (Panel B).",
             ha="left", va="top", fontsize=6.5, color=GRIS, fontfamily="Georgia")

    plt.savefig(f"{OUT}/fig15_3_williams_rv_iv.png", dpi=150*SCALE,
                bbox_inches="tight", facecolor="white")
    plt.close()
    print("✓  fig15_3")


# ══════════════════════════════════════════════════════════════════════════════
# Figura 15.4  Dinámica del modelo de mejoramiento
#   Tasas locales de refuerzo de las dos opciones como función de
#   la proporción de tiempo asignada a la opción 1.
#   Las flechas indican la dirección de movimiento del sistema.
# ══════════════════════════════════════════════════════════════════════════════

def fig15_4():
    r1_total = 60   # reforzadores/hr disponibles en IV 1'
    r2_total = 30   # reforzadores/hr disponibles en IV 2'

    T1 = np.linspace(0.05, 0.95, 300)
    T2 = 1 - T1

    local1 = r1_total / T1   # tasa local opción 1: decrece con T1
    local2 = r2_total / T2   # tasa local opción 2: crece con T1

    T_eq = r1_total / (r1_total + r2_total)   # = 2/3
    r_eq = r1_total / T_eq                    # = 90 ref/hr

    fig, ax = plt.subplots(figsize=(5, 4))

    ax.plot(T1, local1, color=AZUL,   lw=2.0, label="Tasa local opción 1 (IV 1')")
    ax.plot(T1, local2, color=NARANJA,lw=2.0, label="Tasa local opción 2 (IV 2')")

    # Punto de equilibrio
    ax.plot(T_eq, r_eq, "o", color=VERDE, ms=9, zorder=5,
            label=f"Equilibrio ($T_1$ = {T_eq:.2f}, $r$ = {r_eq:.0f} ref/hr)")
    ax.vlines(T_eq, 0, r_eq, colors=GRIS, lw=1, ls=":")
    ax.hlines(r_eq, 0, T_eq, colors=GRIS, lw=1, ls=":")

    # Flechas de dirección de movimiento del sistema
    arrow_kw = dict(arrowstyle="->", color=GRIS, lw=1.2)
    # Lado izquierdo del equilibrio: opción 1 más rentable → T1 aumenta
    ax.annotate("", xy=(0.45, 95), xytext=(0.30, 95),
                arrowprops=arrow_kw)
    # Lado derecho: opción 2 más rentable → T1 disminuye
    ax.annotate("", xy=(0.75, 95), xytext=(0.90, 95),
                arrowprops=arrow_kw)

    ax.text(0.30, 98, "IV 2' más rentable\n→ $T_1$ aumenta",
            fontsize=7.5, color=GRIS, ha="center", fontfamily="Georgia")
    ax.text(0.85, 98, "IV 1' más rentable\n→ $T_1$ disminuye",
            fontsize=7.5, color=GRIS, ha="center", fontfamily="Georgia")

    ax.set_xlabel("Proporción de tiempo asignada a la opción 1 ($T_1$)", **FONT_EJE)
    ax.set_ylabel("Tasa local de refuerzo (ref/hr)", **FONT_EJE)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 200)
    ax.set_xticks([0, 0.2, 0.4, T_eq, 0.8, 1.0])
    ax.set_xticklabels(["0", "0.2", "0.4", "2/3", "0.8", "1.0"])
    ax.set_yticks([0, 50, 90, 100, 150, 200])
    ax.legend(frameon=False, fontsize=8, prop={"family":"Georgia","size":8},
              loc="upper center")
    ax.set_title("Dinámica del mejoramiento — IV 1' vs. IV 2'", **FONT_TITULO)
    estilo_base(ax)

    fig.text(0.08, -0.04,
             "Figura 15.4.  Las tasas locales de refuerzo de las dos opciones se intersectan "
             "en $T_1 = 2/3$, el punto\n"
             "de igualación. Las flechas indican la dirección en que el modelo de mejoramiento "
             "redistribuye el comportamiento\n"
             "a ambos lados del equilibrio. En el equilibrio, ambas opciones ofrecen la misma "
             "tasa local (90 ref/hr).",
             ha="left", va="top", fontsize=6.5, color=GRIS, fontfamily="Georgia")

    plt.savefig(f"{OUT}/fig15_4_mejoramiento_dinamica.png", dpi=150*SCALE,
                bbox_inches="tight", facecolor="white")
    plt.close()
    print("✓  fig15_4")


# ── Ejecutar ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    fig15_1()
    fig15_2()
    fig15_3()
    fig15_4()
    print("\nTodas las figuras generadas en:", OUT)
