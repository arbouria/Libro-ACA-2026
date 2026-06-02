import matplotlib.pyplot as plt
import numpy as np

AZUL    = "#2C5282"
NARANJA = "#C05621"
VERDE   = "#276749"
GRIS    = "#718096"

plt.rcParams.update({
    "font.family":     "serif",
    "font.serif":      ["Georgia", "Palatino", "DejaVu Serif"],
    "axes.linewidth":  0.8,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.size": 4,
    "ytick.major.size": 4,
    "axes.spines.top":   False,
    "axes.spines.right": False,
})

SCALE = 2.5
fig, (axA, axB) = plt.subplots(2, 1,
    figsize=(6 * SCALE, 6.4 * SCALE), dpi=150)

x = np.arange(1, 11)

# ── Panel A ───────────────────────────────────────────────────────
alt = [0.15, 0.20, 0.24, 0.30, 0.35, 0.40, 0.47, 0.50, 0.50, 0.50]
act = [0.15, 0.155, 0.16, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19]

axA.plot(x, alt, color=NARANJA, marker="o", ms=7, lw=2,
         label="Tecla alternativa (IV 3')")
axA.plot(x, act, color=AZUL, marker="s", ms=7, lw=2,
         linestyle="--", label="Tecla actual (IV 1')")

axA.set_ylabel("P (reforzador disponible)", fontsize=11 * SCALE/2.5)
axA.set_xlim(0.5, 10.5);  axA.set_ylim(0, 0.58)
axA.set_xticks(x);         axA.set_xticklabels([])
axA.tick_params(labelsize=9 * SCALE/2.5)
axA.set_title("Panel A — Probabilidad de refuerzo disponible",
              fontsize=13 * SCALE/2.5, fontweight="bold", color=AZUL, pad=10)
axA.legend(fontsize=9 * SCALE/2.5, frameon=False, loc="upper left")

# ── Panel B ───────────────────────────────────────────────────────
s58  = [0.29, 0.29, 0.26, 0.27, 0.24, 0.24, 0.21, 0.21, 0.20, 0.17]
s59  = [0.25, 0.25, 0.22, 0.20, 0.20, 0.16, 0.16, 0.15, 0.12, 0.11]
s60  = [0.21, 0.19, 0.19, 0.16, 0.13, 0.13, 0.10, 0.09, 0.08, 0.05]
pred = [0.14, 0.17, 0.20, 0.23, 0.26, 0.30, 0.34, 0.38, 0.41, 0.44]

axB.plot(x, s58,  color=AZUL,    marker="o", ms=7, lw=2, label="Sujeto 58")
axB.plot(x, s59,  color=VERDE,   marker="s", ms=7, lw=2, label="Sujeto 59")
axB.plot(x, s60,  color=NARANJA, marker="^", ms=7, lw=2, label="Sujeto 60")
axB.plot(x, pred, color=GRIS,    lw=2, linestyle="--",    label="Predicción del modelo")

axB.set_ylabel("P (cambiar a opción alterna)", fontsize=11 * SCALE/2.5)
axB.set_xlabel("Elecciones consecutivas de la opción actual",
               fontsize=11 * SCALE/2.5, labelpad=10)
axB.set_xlim(0.5, 10.5);  axB.set_ylim(0, 0.50)
axB.set_xticks(x)
axB.tick_params(axis="both", labelsize=9 * SCALE/2.5)
axB.set_title("Panel B — Probabilidad observada de cambio",
              fontsize=13 * SCALE/2.5, fontweight="bold", color=AZUL, pad=10)
axB.legend(fontsize=9 * SCALE/2.5, frameon=False, loc="upper right")

# ── Layout primero ────────────────────────────────────────────────
plt.subplots_adjust(left=0.11, right=0.97, top=0.97, bottom=0.16, hspace=0.32)

# ── Top rule: después de fijar layout ────────────────────────────
fig.canvas.draw()
for ax in (axA, axB):
    p = ax.get_position()
    fig.add_artist(plt.Line2D(
        [p.x0, p.x1], [p.y1, p.y1],
        transform=fig.transFigure, color=AZUL, lw=2.5, clip_on=False
    ))

# ── Caption ───────────────────────────────────────────────────────
caption = (
    "Figura 15.1.  Mientras la probabilidad de refuerzo en la alternativa crece con cada "
    "respuesta consecutiva a la opción actual (Panel A), la probabilidad de cambiar "
    "no aumenta — contrariamente a la predicción del modelo de maximización momentánea "
    "(Panel B)."
)
fig.text(0.11, 0.01, caption,
         ha="left", va="bottom",
         fontsize=9 * SCALE/2.5, color="#4A5568",
         wrap=True, linespacing=1.5,
         transform=fig.transFigure)

out = "/mnt/user-data/outputs/fig15_1_nevin_iv_iv.png"
fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
print(f"Guardada: {out}")
plt.close()
