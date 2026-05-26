#!/usr/bin/env python3
"""
Figuras del Capítulo 13: La Ley del Efecto y los Programas de Refuerzo
Aprendizaje y Comportamiento Adaptable: Principios y Modelos

Paleta del libro:
  azul   #2C5282
  naranja #C05621
  verde  #276749
  gris   #718096
  fondo  blanco
  tipografía serif
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import matplotlib.patheffects as pe

# ─── Paleta y estilo global ────────────────────────────────────
AZUL    = "#2C5282"
NARANJA = "#C05621"
VERDE   = "#276749"
GRIS    = "#718096"
GRIS_CLARO = "#CBD5E0"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": GRIS,
    "axes.linewidth": 0.8,
    "xtick.color": GRIS,
    "ytick.color": GRIS,
    "text.color": "#1A202C",
})

DPI = 250
OUT = "/home/claude/figs/"

import os
os.makedirs(OUT, exist_ok=True)

# ═══════════════════════════════════════════════════════════════
# FIGURA 13.1  —  Cómo funciona el registro acumulativo
# ═══════════════════════════════════════════════════════════════

def fig_13_1():
    fig, ax = plt.subplots(figsize=(7, 3.5))

    # Simulate a cumulative record with varying rates
    np.random.seed(42)
    # Phase 1: moderate rate
    iri1 = np.random.exponential(2.0, 15)
    # Phase 2: pause
    pause = [8.0]
    # Phase 3: high rate
    iri2 = np.random.exponential(0.8, 20)
    # Phase 4: low rate
    iri3 = np.random.exponential(4.0, 8)

    iris = np.concatenate([iri1, pause, iri2, iri3])
    times = np.cumsum(iris)
    cum_resp = np.arange(1, len(times) + 1)

    # Build step function
    t_plot = [0]
    c_plot = [0]
    for i in range(len(times)):
        t_plot.extend([times[i], times[i]])
        c_plot.extend([c_plot[-1], cum_resp[i]])

    ax.plot(t_plot, c_plot, color=AZUL, linewidth=1.8)

    # Annotations
    # High rate region
    t_high_start = times[16]
    t_high_end = times[34]
    ax.annotate("Tasa alta\n(pendiente pronunciada)",
                xy=((t_high_start + t_high_end) / 2, 28),
                fontsize=8.5, color=AZUL, ha="center",
                fontstyle="italic")

    # Pause region
    t_pause_start = times[14]
    t_pause_end = times[15]
    ax.annotate("Pausa\n(pendiente ≈ 0)",
                xy=((t_pause_start + t_pause_end) / 2, 16),
                xytext=((t_pause_start + t_pause_end) / 2 + 5, 10),
                fontsize=8.5, color=NARANJA, ha="center",
                fontstyle="italic",
                arrowprops=dict(arrowstyle="->", color=NARANJA, lw=1.2))

    # Low rate region
    ax.annotate("Tasa baja\n(pendiente suave)",
                xy=(times[-3], cum_resp[-3]),
                xytext=(times[-3] - 12, cum_resp[-3] + 5),
                fontsize=8.5, color=GRIS, ha="center",
                fontstyle="italic",
                arrowprops=dict(arrowstyle="->", color=GRIS, lw=1.2))

    # Small diagram: mechanism explanation
    ax.text(0.02, 0.97,
            "Cada respuesta sube la pluma un escalón.\n"
            "El papel avanza con el tiempo.\n"
            "Pendiente = tasa de respuesta.",
            transform=ax.transAxes, fontsize=8, va="top",
            color=GRIS, fontstyle="italic",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#F7FAFC",
                      edgecolor=GRIS_CLARO, linewidth=0.8))

    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Respuestas acumuladas")
    ax.set_xlim(0, times[-1] * 1.05)
    ax.set_ylim(0, cum_resp[-1] * 1.15)
    ax.set_xticks([])
    ax.set_yticks([])

    # Top blue line
    fig.patches.append(plt.Rectangle((0, 0.96), 1, 0.04,
                       transform=fig.transFigure, facecolor=AZUL,
                       edgecolor="none", zorder=10))

    fig.text(0.5, 0.01,
             "Figura 13.1. El registro acumulativo. La pendiente de la línea es la tasa de respuesta:\n"
             "pronunciada indica tasa alta, plana indica pausa.",
             ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0, 0.06, 1, 0.95])
    fig.savefig(OUT + "fig_13_1_registro_acumulativo.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


# ═══════════════════════════════════════════════════════════════
# FIGURA 13.2  —  Tabla-diagrama de los cuatro programas
# ═══════════════════════════════════════════════════════════════

def fig_13_2():
    fig, axes = plt.subplots(2, 2, figsize=(8, 5.5))

    programs = {
        (0, 0): ("Razón Fija (RF)", "Pago por pieza producida",
                 "ratio_fixed"),
        (0, 1): ("Razón Variable (RV)", "Comisión por venta\n(n.º variable de intentos)",
                 "ratio_variable"),
        (1, 0): ("Intervalo Fijo (IF)", "Salario quincenal",
                 "interval_fixed"),
        (1, 1): ("Intervalo Variable (IV)", "Esperar el autobús\n(frecuencia impredecible)",
                 "interval_variable"),
    }

    np.random.seed(7)

    for (r, c), (title, example, ptype) in programs.items():
        ax = axes[r][c]

        # Generate cumulative record
        if ptype == "ratio_fixed":
            # High rate with post-reinforcement pauses
            segments = []
            for _ in range(4):
                pause = np.zeros(8)
                burst = np.ones(20)
                segments.append(np.concatenate([pause, burst]))
            data = np.concatenate(segments)
            reinf_idx = []
            cum = 0
            for i, d in enumerate(data):
                cum += d
                if cum > 0 and cum % 20 == 0:
                    reinf_idx.append(i)

        elif ptype == "ratio_variable":
            # High steady rate, no pauses
            data = np.random.binomial(1, 0.85, 120).astype(float)
            reinf_idx = list(range(15, 120, np.random.randint(12, 20)))
            reinf_idx = [15, 28, 45, 58, 72, 88, 103]

        elif ptype == "interval_fixed":
            # Scallop pattern
            segments = []
            reinf_idx = []
            pos = 0
            for _ in range(4):
                n = 30
                t = np.linspace(0, 1, n)
                rates = t ** 2.5  # accelerating
                resp = np.random.binomial(1, rates * 0.9)
                segments.append(resp)
                reinf_idx.append(pos + n - 1)
                pos += n
            data = np.concatenate(segments)

        elif ptype == "interval_variable":
            # Moderate steady rate
            data = np.random.binomial(1, 0.45, 120).astype(float)
            reinf_idx = [18, 35, 42, 65, 78, 95, 110]

        cum = np.cumsum(data)
        x = np.arange(len(data))

        color = AZUL
        ax.plot(x, cum, color=color, linewidth=1.5)

        # Mark reinforcers
        for ri in reinf_idx:
            if ri < len(cum):
                ax.plot(ri, cum[ri], "|", color=NARANJA, markersize=8,
                        markeredgewidth=1.5)

        ax.set_title(title, fontsize=10, fontweight="bold", color=AZUL)
        ax.text(0.5, -0.18, example, transform=ax.transAxes,
                fontsize=7.5, ha="center", color=GRIS, fontstyle="italic")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel("Tiempo", fontsize=8, color=GRIS)
        if c == 0:
            ax.set_ylabel("Resp. acumuladas", fontsize=8, color=GRIS)

    # Column headers
    fig.text(0.3, 0.98, "Criterio: Número de respuestas", ha="center",
             fontsize=9, color=GRIS, fontstyle="italic")
    fig.text(0.75, 0.98, "Criterio: Tiempo transcurrido", ha="center",
             fontsize=9, color=GRIS, fontstyle="italic")

    # Row headers
    fig.text(0.01, 0.72, "Fijo", ha="center", fontsize=9, color=GRIS,
             rotation=90, fontstyle="italic")
    fig.text(0.01, 0.3, "Variable", ha="center", fontsize=9, color=GRIS,
             rotation=90, fontstyle="italic")

    # Top blue line
    fig.patches.append(plt.Rectangle((0, 0.97), 1, 0.03,
                       transform=fig.transFigure, facecolor=AZUL,
                       edgecolor="none", zorder=10))

    fig.text(0.5, 0.01,
             "Figura 13.2. Los cuatro programas básicos de refuerzo con registros acumulativos "
             "estilizados. Marcas naranjas: entrega de reforzador.",
             ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0.03, 0.05, 1, 0.96])
    fig.savefig(OUT + "fig_13_2_cuatro_programas.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


# ═══════════════════════════════════════════════════════════════
# FIGURA 13.3  —  Adquisición del patrón de IF (Ferster & Skinner)
# ═══════════════════════════════════════════════════════════════

def fig_13_3():
    fig, ax = plt.subplots(figsize=(7, 4.5))

    np.random.seed(21)
    total_cum = 0
    x_offset = 0
    all_x = []
    all_y = []

    phases = [
        ("I", 0.5, 6),     # fairly constant rate
        ("II", 0.7, 6),    # high after reinf, some pauses
        ("III", 1.5, 6),   # clear pauses, beginning scallop
        ("IV", 2.5, 8),    # mature scallop
    ]

    phase_boundaries = []
    phase_labels = []

    for phase_name, scallop_exp, n_intervals in phases:
        phase_start = x_offset
        for interval in range(n_intervals):
            n = 40  # time steps per interval
            t = np.linspace(0, 1, n)

            if scallop_exp < 1.0:
                # Early: roughly constant, slight decrease after reinf
                rates = 0.4 + 0.1 * np.random.randn(n)
                rates = np.clip(rates, 0.05, 0.8)
            else:
                # Scallop: low at start, accelerating
                base = t ** scallop_exp
                rates = base * 0.7 + 0.05
                # Add pause at beginning proportional to scallop
                pause_len = min(int(scallop_exp * 4), n // 2)
                rates[:pause_len] = 0.02

            resp = np.random.binomial(1, np.clip(rates, 0, 1))
            cum = np.cumsum(resp) + total_cum
            x = np.arange(n) + x_offset

            all_x.extend(x)
            all_y.extend(cum)

            # Reinforcement mark at end of interval
            ax.plot(x[-1], cum[-1], "|", color=NARANJA, markersize=6,
                    markeredgewidth=1.2)

            total_cum = cum[-1]
            x_offset += n

        phase_boundaries.append((phase_start, x_offset))
        phase_labels.append(phase_name)

    ax.plot(all_x, all_y, color=AZUL, linewidth=1.2)

    # Phase labels
    for (start, end), label in zip(phase_boundaries, phase_labels):
        mid = (start + end) / 2
        ax.text(mid, max(all_y) * 1.05, label,
                ha="center", fontsize=11, fontweight="bold",
                color=GRIS)
        if label != "I":
            ax.axvline(start, color=GRIS_CLARO, linewidth=0.8,
                       linestyle="--", zorder=0)

    ax.set_xlabel("Tiempo (sesiones sucesivas →)", color=GRIS)
    ax.set_ylabel("Respuestas acumuladas", color=GRIS)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, max(all_y) * 1.15)

    # Top blue line
    fig.patches.append(plt.Rectangle((0, 0.96), 1, 0.04,
                       transform=fig.transFigure, facecolor=AZUL,
                       edgecolor="none", zorder=10))

    fig.text(0.5, 0.01,
             "Figura 13.3. Adquisición del festoneo en intervalo fijo. Fase I: tasa relativamente constante "
             "(predicción de B&M). Fase IV: festoneo\nmaduro — pausa post-reforzador y aceleración "
             "progresiva. Adaptado de Ferster y Skinner (1957).",
             ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0, 0.06, 1, 0.95])
    fig.savefig(OUT + "fig_13_3_adquisicion_FI.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


# ═══════════════════════════════════════════════════════════════
# FIGURA 13.4  —  Cajas acopladas (Catania, 1971)
# ═══════════════════════════════════════════════════════════════

def fig_13_4():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 4.5), sharex=True)

    np.random.seed(33)

    # VR pigeon: high rate
    n = 300
    vr_iri = np.random.exponential(0.6, n)
    vr_times = np.cumsum(vr_iri)
    vr_cum = np.arange(1, n + 1)

    # Build step function for VR
    t_vr = [0]
    c_vr = [0]
    for i in range(len(vr_times)):
        t_vr.extend([vr_times[i], vr_times[i]])
        c_vr.extend([c_vr[-1], vr_cum[i]])

    # VI pigeon (yoked): same reinforcer times, but much lower rate
    n_vi = 60
    vi_iri = np.random.exponential(3.0, n_vi)
    vi_times = np.cumsum(vi_iri)
    vi_cum = np.arange(1, n_vi + 1)

    t_vi = [0]
    c_vi = [0]
    for i in range(len(vi_times)):
        t_vi.extend([vi_times[i], vi_times[i]])
        c_vi.extend([c_vi[-1], vi_cum[i]])

    # Reinforcement times (from VR schedule, every ~30 responses)
    reinf_times = vr_times[29::30]

    max_t = min(vr_times[-1], vi_times[-1])

    ax1.plot(t_vr, c_vr, color=AZUL, linewidth=1.5)
    for rt in reinf_times:
        if rt < max_t:
            idx = np.searchsorted(vr_times, rt)
            if idx < len(vr_cum):
                ax1.plot(rt, vr_cum[idx], "|", color=NARANJA,
                         markersize=8, markeredgewidth=1.5)

    ax1.set_ylabel("Resp. acumuladas", fontsize=9, color=GRIS)
    ax1.set_title("Razón Variable (paloma líder)", fontsize=10,
                  color=AZUL, fontweight="bold")
    ax1.text(0.97, 0.15, "≈ 5 resp/s", transform=ax1.transAxes,
             ha="right", fontsize=9, color=AZUL, fontstyle="italic")
    ax1.set_xticks([])
    ax1.set_yticks([])

    ax2.plot(t_vi, c_vi, color=VERDE, linewidth=1.5)
    for rt in reinf_times:
        if rt < max_t:
            idx = np.searchsorted(vi_times, rt)
            if idx < len(vi_cum):
                ax2.plot(rt, vi_cum[idx], "|", color=NARANJA,
                         markersize=8, markeredgewidth=1.5)

    ax2.set_ylabel("Resp. acumuladas", fontsize=9, color=GRIS)
    ax2.set_xlabel("Tiempo", fontsize=9, color=GRIS)
    ax2.set_title("Intervalo Variable (paloma acoplada)", fontsize=10,
                  color=VERDE, fontweight="bold")
    ax2.text(0.97, 0.15, "≈ 1 resp/s", transform=ax2.transAxes,
             ha="right", fontsize=9, color=VERDE, fontstyle="italic")
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_xlim(0, max_t)

    # Annotation: same reinforcement rate
    fig.text(0.98, 0.5, "Misma tasa\nde reforzamiento",
             ha="right", va="center", fontsize=9, color=NARANJA,
             fontstyle="italic", rotation=-90)

    # Top blue line
    fig.patches.append(plt.Rectangle((0, 0.96), 1, 0.04,
                       transform=fig.transFigure, facecolor=AZUL,
                       edgecolor="none", zorder=10))

    fig.text(0.5, 0.01,
             "Figura 13.4. Experimento de cajas acopladas (Catania, 1971). Ambas palomas reciben "
             "la misma tasa de reforzamiento (marcas naranjas\nalineadas), pero la paloma bajo "
             "razón variable responde ~5 veces más rápido que la acoplada bajo intervalo variable.",
             ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0, 0.07, 0.95, 0.95])
    fig.savefig(OUT + "fig_13_4_cajas_acopladas.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


# ═══════════════════════════════════════════════════════════════
# FIGURA 13.5  —  Funciones de retroalimentación (VR vs VI)
# ═══════════════════════════════════════════════════════════════

def fig_13_5():
    fig, ax = plt.subplots(figsize=(6, 4.5))

    R = np.linspace(0, 120, 500)  # Response rate

    # VR: r = R/n, with n=30
    vr = R / 30.0

    # VI rich: r = 1/t * R/(R + k), approximate with t=30s, k=5
    vi_rich = (1 / 30.0) * R / (R + 5)
    # Scale to make asymptote = 1/30 ≈ 2/min
    vi_rich = 2.0 * R / (R + 5)

    # VI lean: t=120s
    vi_lean = 0.5 * R / (R + 5)

    ax.plot(R, vr, color=AZUL, linewidth=2.2, linestyle="--",
            label="RV (razón variable)")
    ax.plot(R, vi_rich, color=VERDE, linewidth=2,
            label="IV rico (intervalo corto)")
    ax.plot(R, vi_lean, color=GRIS, linewidth=2,
            label="IV pobre (intervalo largo)")

    # Max response rate line
    ax.axvline(100, color=NARANJA, linewidth=1.2, linestyle=":",
               label="Tasa máxima")
    ax.text(102, 3.5, "Máx", fontsize=8, color=NARANJA, fontstyle="italic")

    # Asymptote lines for VI
    ax.axhline(2.0, color=VERDE, linewidth=0.6, linestyle=":", alpha=0.5)
    ax.axhline(0.5, color=GRIS, linewidth=0.6, linestyle=":", alpha=0.5)

    ax.set_xlabel("Tasa de respuesta, $R$ (resp/min)", fontsize=10)
    ax.set_ylabel("Tasa de reforzamiento, $r$ (ref/min)", fontsize=10)
    ax.set_xlim(0, 125)
    ax.set_ylim(0, 4.5)
    ax.legend(fontsize=8.5, framealpha=0.9, loc="upper left")

    # Top blue line
    fig.patches.append(plt.Rectangle((0, 0.96), 1, 0.04,
                       transform=fig.transFigure, facecolor=AZUL,
                       edgecolor="none", zorder=10))

    fig.text(0.5, 0.01,
             "Figura 13.5. Funciones de retroalimentación. En RV (línea punteada azul) la relación "
             "es proporcional. En IV (curvas sólidas)\nla tasa de reforzamiento se estabiliza en una "
             "asíntota determinada por el intervalo programado.",
             ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0, 0.06, 1, 0.95])
    fig.savefig(OUT + "fig_13_5_funciones_retroalimentacion.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


# ═══════════════════════════════════════════════════════════════
# FIGURA 13.6  —  Familia de funciones de Rachlin (r = d·R^m)
# ═══════════════════════════════════════════════════════════════

def fig_13_6():
    fig, ax = plt.subplots(figsize=(6, 4.5))

    R = np.linspace(0.01, 1.0, 500)  # Normalized response rate
    d = 0.1

    ms = [1.0, 0.5, 0.2, 0.1, 0.05]
    colors = [AZUL, "#3B6BAA", GRIS, "#8FA5B8", GRIS_CLARO]
    labels = ["$m = 1.0$ (RV)", "$m = 0.5$", "$m = 0.2$",
              "$m = 0.1$", "$m = 0.05$ (≈ Tiempo fijo)"]

    for m, color, label in zip(ms, colors, labels):
        r = d * R ** m
        ax.plot(R, r, color=color, linewidth=2, label=label)

    ax.set_xlabel("Tasa de respuesta, $R$ (normalizada)", fontsize=10)
    ax.set_ylabel("Tasa de reforzamiento, $r$", fontsize=10)
    ax.set_xlim(0, 1.05)
    ax.set_ylim(0, 0.115)
    ax.legend(fontsize=8.5, framealpha=0.9, loc="upper left")

    # Top blue line
    fig.patches.append(plt.Rectangle((0, 0.96), 1, 0.04,
                       transform=fig.transFigure, facecolor=AZUL,
                       edgecolor="none", zorder=10))

    fig.text(0.5, 0.01,
             "Figura 13.6. Familia de funciones de retroalimentación de Rachlin, "
             "$r = d \\cdot R^m$. Conforme $m$ decrece, la función se vuelve\n"
             "más cóncava y la tasa de reforzamiento se satura más rápidamente.",
             ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0, 0.06, 1, 0.95])
    fig.savefig(OUT + "fig_13_6_rachlin.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


# ═══════════════════════════════════════════════════════════════
# FIGURA 13.7  —  Sistema de retroalimentación (diagrama de bloques)
# ═══════════════════════════════════════════════════════════════

def fig_13_7():
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")

    # Organism box (top)
    org_box = plt.Rectangle((1.5, 3.0), 3, 1.2, facecolor="#EBF4FF",
                             edgecolor=AZUL, linewidth=2, zorder=5)
    ax.add_patch(org_box)
    ax.text(3.0, 3.6, "Función del organismo", ha="center", va="center",
            fontsize=10, fontweight="bold", color=AZUL)
    ax.text(3.0, 3.2, "$R = f(r)$", ha="center", va="center",
            fontsize=11, color=AZUL, fontstyle="italic")

    # Environment box (bottom)
    env_box = plt.Rectangle((5.5, 3.0), 3, 1.2, facecolor="#F0FFF4",
                             edgecolor=VERDE, linewidth=2, zorder=5)
    ax.add_patch(env_box)
    ax.text(7.0, 3.6, "Función del entorno", ha="center", va="center",
            fontsize=10, fontweight="bold", color=VERDE)
    ax.text(7.0, 3.2, "(programa de refuerzo)", ha="center", va="center",
            fontsize=9, color=VERDE, fontstyle="italic")

    # Arrows
    # Top arrow: organism → environment (response rate)
    ax.annotate("", xy=(5.4, 4.0), xytext=(4.6, 4.0),
                arrowprops=dict(arrowstyle="-|>", color=AZUL, lw=2))
    ax.text(5.0, 4.35, "Tasa de respuesta ($R$)", ha="center",
            fontsize=9, color=AZUL)

    # Bottom arrow: environment → organism (reinforcement rate)
    ax.annotate("", xy=(4.6, 3.2), xytext=(5.4, 3.2),
                arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=2))
    ax.text(5.0, 2.75, "Tasa de reforzamiento ($r$)", ha="center",
            fontsize=9, color=VERDE)

    # Equilibrium note
    ax.text(5.0, 1.8,
            "El equilibrio se alcanza cuando ambas funciones\n"
            "son mutuamente consistentes.",
            ha="center", fontsize=8.5, color=GRIS, fontstyle="italic",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#F7FAFC",
                      edgecolor=GRIS_CLARO, linewidth=0.8))

    # Top blue line
    fig.patches.append(plt.Rectangle((0, 0.94), 1, 0.06,
                       transform=fig.transFigure, facecolor=AZUL,
                       edgecolor="none", zorder=10))

    fig.text(0.5, 0.03,
             "Figura 13.7. El sistema de retroalimentación entre organismo y entorno. "
             "La tasa de respuesta determina, a través del\nprograma, la tasa de "
             "reforzamiento, y esta a su vez determina la tasa de respuesta.",
             ha="center", fontsize=8, color=GRIS, fontstyle="italic")

    plt.tight_layout(rect=[0, 0.08, 1, 0.93])
    fig.savefig(OUT + "fig_13_7_sistema_retroalimentacion.png", dpi=DPI,
                facecolor="white", bbox_inches="tight")
    plt.close()


# ═══════════════════════════════════════════════════════════════
# Generar todas las figuras
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    fig_13_1()
    print("✓ Fig 13.1 — Registro acumulativo")
    fig_13_2()
    print("✓ Fig 13.2 — Cuatro programas")
    fig_13_3()
    print("✓ Fig 13.3 — Adquisición del patrón IF")
    fig_13_4()
    print("✓ Fig 13.4 — Cajas acopladas")
    fig_13_5()
    print("✓ Fig 13.5 — Funciones de retroalimentación")
    fig_13_6()
    print("✓ Fig 13.6 — Rachlin")
    fig_13_7()
    print("✓ Fig 13.7 — Sistema de retroalimentación")
    print(f"\nTodas las figuras guardadas en {OUT}")
