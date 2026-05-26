#!/usr/bin/env python3
"""
Figuras 13.1–13.4: pasada final de ajustes de layout.
"""

import numpy as np
import matplotlib.pyplot as plt

AZUL    = "#2C5282"
NARANJA = "#C05621"
VERDE   = "#276749"
GRIS    = "#718096"
GRIS_CLARO = "#CBD5E0"

plt.rcParams.update({
    "font.family": "serif", "font.size": 10,
    "axes.labelsize": 11, "axes.titlesize": 12,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "axes.edgecolor": GRIS, "axes.linewidth": 0.8,
    "xtick.color": GRIS, "ytick.color": GRIS,
    "text.color": "#1A202C",
})

DPI = 250
OUT = "/home/claude/figs_v3/"
import os; os.makedirs(OUT, exist_ok=True)


def cum_from_rate_segments(segments, dt=0.05):
    t_all, c_all = [], []
    t_cur, c_cur = 0.0, 0.0
    for dur, rate in segments:
        n = max(int(dur / dt), 2)
        ts = np.linspace(0, dur, n)
        if callable(rate):
            rates = rate(ts / dur)
        else:
            rates = np.full(n, float(rate))
        cum = np.cumsum(rates * dt) + c_cur
        t_all.extend(ts + t_cur)
        c_all.extend(cum)
        t_cur += dur
        c_cur = cum[-1]
    return np.array(t_all), np.array(c_all)


# ═══════════════════════════════════════════════════════════════
# 13.1  —  Registro acumulativo
# ═══════════════════════════════════════════════════════════════

def fig_13_1():
    fig, ax = plt.subplots(figsize=(7, 3.8))

    segments = [
        (8.0, 4.0),   # moderate
        (7.0, 0.0),   # pause
        (6.0, 10.0),  # high
        (11.0, 1.5),  # low
    ]
    t, c = cum_from_rate_segments(segments)
    ax.plot(t, c, color=AZUL, linewidth=2.2)

    # Annotations — positioned to avoid overlap
    ax.text(4, 6, "Tasa moderada", fontsize=9, color=AZUL,
            fontstyle="italic", ha="center")

    ax.annotate("Pausa\n(pendiente ≈ 0)",
                xy=(11.5, 16.0), xytext=(16, 8),
                fontsize=9, color=NARANJA, ha="center", fontstyle="italic",
                arrowprops=dict(arrowstyle="->", color=NARANJA, lw=1.3))

    ax.text(18.5, 42, "Tasa alta\n(pendiente pronunciada)",
            fontsize=9, color=AZUL, fontstyle="italic", ha="center")

    ax.text(27, 56, "Tasa baja\n(pendiente suave)",
            fontsize=9, color=GRIS, fontstyle="italic", ha="center")

    ax.text(0.02, 0.97,
            "Cada respuesta sube la pluma un escalón.\n"
            "El papel avanza con el tiempo.\n"
            "Pendiente = tasa de respuesta.",
            transform=ax.transAxes, fontsize=8.5, va="top",
            color=GRIS, fontstyle="italic",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#F7FAFC",
                      edgecolor=GRIS_CLARO, linewidth=0.8))

    ax.set_xlabel("Tiempo", fontsize=10)
    ax.set_ylabel("Respuestas acumuladas", fontsize=10)
    ax.set_xlim(0, 33); ax.set_ylim(0, max(c) * 1.2)
    ax.set_xticks([]); ax.set_yticks([])

    # Top rule
    fig.patches.append(plt.Rectangle((0, 0.97), 1, 0.03,
        transform=fig.transFigure, facecolor=AZUL, edgecolor="none", zorder=10))
    fig.text(0.5, 0.01,
        "Figura 13.1. El registro acumulativo. La pendiente de la línea "
        "es la tasa de respuesta.",
        ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0, 0.05, 1, 0.96])
    fig.savefig(OUT + "fig_13_1_registro_acumulativo.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


# ═══════════════════════════════════════════════════════════════
# 13.2  —  Cuatro programas
# ═══════════════════════════════════════════════════════════════

def fig_13_2():
    fig, axes = plt.subplots(2, 2, figsize=(8.5, 6.5))

    # ── RF ──
    ax = axes[0, 0]
    segs, rt = [], []
    for _ in range(5):
        segs.append((3.0, 0.0))    # pause
        segs.append((5.0, 12.0))   # run
        rt.append(sum(s[0] for s in segs))
    t, c = cum_from_rate_segments(segs)
    ax.plot(t, c, color=AZUL, lw=1.8)
    for r in rt:
        i = min(np.searchsorted(t, r), len(c)-1)
        ax.plot(r, c[i], "|", color=NARANJA, ms=10, mew=2)
    ax.set_title("Razón Fija (RF)", fontsize=10, fontweight="bold", color=AZUL)
    ax.text(0.5, -0.22, "Pago por pieza producida",
            transform=ax.transAxes, fontsize=8, ha="center",
            color=GRIS, fontstyle="italic")

    # ── RV ──
    ax = axes[0, 1]
    segs, rt = [], []
    tot = 0
    for d in [6.5, 8.2, 5.0, 7.8, 6.0, 9.0, 5.5]:
        segs.append((d, 14.0))
        tot += d; rt.append(tot)
    t, c = cum_from_rate_segments(segs)
    ax.plot(t, c, color=AZUL, lw=1.8)
    for r in rt:
        i = min(np.searchsorted(t, r), len(c)-1)
        ax.plot(r, c[i], "|", color=NARANJA, ms=10, mew=2)
    ax.set_title("Razón Variable (RV)", fontsize=10, fontweight="bold", color=AZUL)
    ax.text(0.5, -0.22, "Vendedor a comisión",
            transform=ax.transAxes, fontsize=8, ha="center",
            color=GRIS, fontstyle="italic")

    # ── FI (scallop) ──
    ax = axes[1, 0]
    def scallop(f): return 8.0 * f ** 2.0
    segs, rt = [], []
    for _ in range(5):
        segs.append((8.0, scallop))
        rt.append(sum(s[0] for s in segs))
    t, c = cum_from_rate_segments(segs)
    ax.plot(t, c, color=AZUL, lw=1.8)
    for r in rt:
        i = min(np.searchsorted(t, r), len(c)-1)
        ax.plot(r, c[i], "|", color=NARANJA, ms=10, mew=2)
    ax.set_title("Intervalo Fijo (IF)", fontsize=10, fontweight="bold", color=AZUL)
    ax.text(0.5, -0.22, "Examen programado / salario quincenal",
            transform=ax.transAxes, fontsize=8, ha="center",
            color=GRIS, fontstyle="italic")

    # ── IV ──
    ax = axes[1, 1]
    segs, rt = [], []
    tot = 0
    for d in [5.0, 8.5, 3.0, 10.0, 6.5, 4.0, 7.0, 9.0]:
        segs.append((d, 5.0))
        tot += d; rt.append(tot)
    t, c = cum_from_rate_segments(segs)
    ax.plot(t, c, color=AZUL, lw=1.8)
    for r in rt:
        i = min(np.searchsorted(t, r), len(c)-1)
        ax.plot(r, c[i], "|", color=NARANJA, ms=10, mew=2)
    ax.set_title("Intervalo Variable (IV)", fontsize=10, fontweight="bold", color=AZUL)
    ax.text(0.5, -0.22, "Esperar el autobús",
            transform=ax.transAxes, fontsize=8, ha="center",
            color=GRIS, fontstyle="italic")

    for r in range(2):
        for cc in range(2):
            a = axes[r][cc]
            a.set_xticks([]); a.set_yticks([])
            a.set_xlabel("Tiempo", fontsize=8, color=GRIS)
            if cc == 0:
                a.set_ylabel("Resp. acumuladas", fontsize=8, color=GRIS)
            a.set_xlim(left=0); a.set_ylim(bottom=0)

    # Headers BELOW the blue rule
    fig.patches.append(plt.Rectangle((0, 0.975), 1, 0.025,
        transform=fig.transFigure, facecolor=AZUL, edgecolor="none", zorder=10))
    fig.text(0.30, 0.96, "Criterio: Número de respuestas",
             ha="center", fontsize=9, color=GRIS, fontstyle="italic")
    fig.text(0.74, 0.96, "Criterio: Tiempo transcurrido",
             ha="center", fontsize=9, color=GRIS, fontstyle="italic")
    fig.text(0.01, 0.73, "Fijo", ha="center", fontsize=9, color=GRIS,
             rotation=90, fontstyle="italic")
    fig.text(0.01, 0.30, "Variable", ha="center", fontsize=9, color=GRIS,
             rotation=90, fontstyle="italic")

    fig.text(0.5, 0.005,
        "Figura 13.2. Los cuatro programas básicos de refuerzo. "
        "Nótese la diferencia en pendiente entre razón (alta) e intervalo (moderada),\n"
        "las pausas post-reforzador en los programas fijos, "
        "y el festoneo (aceleración progresiva) en intervalo fijo.",
        ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0.03, 0.06, 1, 0.95])
    fig.savefig(OUT + "fig_13_2_cuatro_programas.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


# ═══════════════════════════════════════════════════════════════
# 13.3  —  Adquisición IF (cuatro paneles)
# ═══════════════════════════════════════════════════════════════

def fig_13_3():
    fig, axes = plt.subplots(1, 4, figsize=(11, 4))

    interval = 6.0

    def phase1(f): return 5.0 * np.ones_like(f)
    def phase2(f): return 5.5 * (1.0 - 0.3 * f)
    def phase3(f):
        p = 0.15
        return np.where(f < p, 0.3, 6.0 * ((f - p) / (1 - p)) ** 1.0)
    def phase4(f):
        p = 0.35
        return np.where(f < p, 0.15, 9.0 * ((f - p) / (1 - p)) ** 2.0)

    configs = [
        ("I — Tasa constante", phase1,
         "Lo que predice la\nley del efecto simple"),
        ("II — Alta post-refuerzo", phase2,
         "Lo que predice\nBush y Mosteller"),
        ("III — Pausa incipiente", phase3,
         "Inicio de discriminación\ntemporal"),
        ("IV — Festoneo maduro", phase4,
         "Discriminación\ntemporal completa"),
    ]

    for i, (title, rate_func, annot) in enumerate(configs):
        ax = axes[i]
        segs, rt = [], []
        for _ in range(5):
            segs.append((interval, rate_func))
            rt.append(sum(s[0] for s in segs))
        t, c = cum_from_rate_segments(segs)
        ax.plot(t, c, color=AZUL, lw=1.7)
        for r in rt:
            idx = min(np.searchsorted(t, r), len(c)-1)
            ax.plot(r, c[idx], "|", color=NARANJA, ms=8, mew=1.8)

        ax.set_title(title, fontsize=9, fontweight="bold", color=AZUL)

        # Annotation box at bottom-left
        ax.text(0.05, 0.08, annot, transform=ax.transAxes,
                fontsize=7.5, ha="left", va="bottom", color=GRIS,
                fontstyle="italic",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#F7FAFC",
                          edgecolor=GRIS_CLARO, lw=0.6, alpha=0.95))

        ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlabel("Tiempo", fontsize=7.5, color=GRIS)
        if i == 0:
            ax.set_ylabel("Respuestas acumuladas", fontsize=9, color=GRIS)
        ax.set_xlim(0, interval * 5); ax.set_ylim(bottom=0)

    fig.patches.append(plt.Rectangle((0, 0.97), 1, 0.03,
        transform=fig.transFigure, facecolor=AZUL, edgecolor="none", zorder=10))
    fig.text(0.5, 0.005,
        "Figura 13.3. Adquisición del festoneo en intervalo fijo (adaptado de "
        "Ferster y Skinner, 1957). Las fases I–II muestran lo que predice\n"
        "la ley del efecto simple; las fases III–IV muestran la inversión del "
        "patrón con el entrenamiento.",
        ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0, 0.07, 1, 0.96])
    fig.savefig(OUT + "fig_13_3_adquisicion_FI.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


# ═══════════════════════════════════════════════════════════════
# 13.4  —  Cajas acopladas
# ═══════════════════════════════════════════════════════════════

def fig_13_4():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.5, 5.5),
                                    gridspec_kw={"hspace": 0.35})

    reinf_t = np.cumsum([3.0, 4.5, 2.8, 5.2, 3.5, 4.0, 3.8, 5.5, 2.5,
                         4.8, 3.2, 5.0, 4.2, 3.0, 4.5])
    max_t = reinf_t[-1] + 2

    vr_rate, vi_rate = 5.0, 1.0
    t = np.linspace(0, max_t, 2000)
    max_y = vr_rate * max_t * 1.05

    ax1.plot(t, vr_rate * t, color=AZUL, lw=2.2)
    ax2.plot(t, vi_rate * t, color=VERDE, lw=2.2)

    for rt in reinf_t:
        ax1.plot(rt, vr_rate * rt, "|", color=NARANJA, ms=10, mew=2)
        ax2.plot(rt, vi_rate * rt, "|", color=NARANJA, ms=10, mew=2)

    ax1.set_ylim(0, max_y); ax2.set_ylim(0, max_y)
    ax1.set_xlim(0, max_t); ax2.set_xlim(0, max_t)

    ax1.set_title("Razón Variable  (paloma líder)", fontsize=11,
                  color=AZUL, fontweight="bold", pad=8)
    ax1.text(0.95, 0.80, "≈ 5 resp/s", transform=ax1.transAxes,
             ha="right", fontsize=10, color=AZUL, fontweight="bold")

    ax2.set_title("Intervalo Variable  (paloma acoplada)", fontsize=11,
                  color=VERDE, fontweight="bold", pad=8)
    ax2.text(0.95, 0.80, "≈ 1 resp/s", transform=ax2.transAxes,
             ha="right", fontsize=10, color=VERDE, fontweight="bold")

    for ax in [ax1, ax2]:
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_ylabel("Resp. acumuladas", fontsize=9, color=GRIS)
    ax2.set_xlabel("Tiempo", fontsize=9, color=GRIS)

    # Key message between panels
    fig.text(0.5, 0.495,
             "↑ Mismos reforzadores, mismos tiempos — solo cambia la regla ↓",
             ha="center", va="center", fontsize=9, color=NARANJA,
             fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.35", facecolor="#FFFAF0",
                       edgecolor=NARANJA, lw=0.8))

    fig.patches.append(plt.Rectangle((0, 0.975), 1, 0.025,
        transform=fig.transFigure, facecolor=AZUL, edgecolor="none", zorder=10))
    fig.text(0.5, 0.01,
        "Figura 13.4. Experimento de cajas acopladas (Catania, 1971). "
        "Misma escala vertical en ambos paneles.\n"
        "La diferencia en pendiente (~5×) se debe exclusivamente a la "
        "estructura de la regla, no a la tasa de reforzamiento.",
        ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0, 0.06, 1, 0.96])
    fig.savefig(OUT + "fig_13_4_cajas_acopladas.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    fig_13_1(); print("✓ 13.1")
    fig_13_2(); print("✓ 13.2")
    fig_13_3(); print("✓ 13.3")
    fig_13_4(); print("✓ 13.4")
