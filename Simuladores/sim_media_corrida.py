# ============================================================
# Simulador: Media y Mediana Corrida
# Capítulo 8: El Modelo de Bush y Mosteller
# Aprendizaje y Comportamiento Adaptable: Principios y Modelos
# Arturo Bouzas
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

AZUL  = '#2C5282'
GRIS  = '#718096'
VERDE = '#276749'

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
    'axes.labelsize'   : 11,
})

# Serie de contagios del capítulo
DATOS_BASE = np.array([10, 14, 11, 16, 13, 9, 85, 12, 18, 15, 20, 17, 13, 19, 16],
                       dtype=float)


def aplicar_filtro(datos, ventana, usar_mediana):
    """Aplica mediana o media corrida. Devuelve índices y valores suavizados."""
    mitad = ventana // 2
    n = len(datos)
    idx, vals = [], []
    for i in range(mitad, n - mitad):
        w = datos[i - mitad : i + mitad + 1]
        vals.append(np.median(w) if usar_mediana else np.mean(w))
        idx.append(i)
    return np.array(idx), np.array(vals)


def graficar_filtro(ventana=3, usar_mediana=True):
    datos = DATOS_BASE.copy()
    dias  = np.arange(1, len(datos) + 1)
    nombre = 'mediana' if usar_mediana else 'media'

    idx_s, vals_s = aplicar_filtro(datos, ventana, usar_mediana)
    dias_s = idx_s + 1   # convertir a base-1

    fig, ax = plt.subplots(figsize=(9, 4.5))

    # Datos originales
    ax.plot(dias, datos, color=GRIS, linewidth=1.5,
            marker='o', markersize=5,
            markerfacecolor='white', markeredgecolor=GRIS,
            label='datos originales', zorder=2)

    # Anotar el valor aberrante
    idx_aber = 7   # día 7
    ax.annotate(
        f'valor aberrante\n(día {idx_aber}: {int(datos[idx_aber-1])})',
        xy=(idx_aber, datos[idx_aber - 1]),
        xytext=(idx_aber + 1.5, datos[idx_aber - 1] - 12),
        fontsize=8, color=GRIS,
        arrowprops=dict(arrowstyle='->', color=GRIS, lw=1.2),
        ha='left'
    )

    # Serie suavizada
    ax.plot(dias_s, vals_s, color=AZUL, linewidth=2.8,
            marker='s', markersize=5, markerfacecolor=AZUL,
            label=f'{nombre} corrida (ventana = {ventana})', zorder=3)

    # Puntos sin ventana completa (extremos)
    mitad = ventana // 2
    extremos_idx  = list(range(1, mitad + 1)) + list(range(len(datos) - mitad + 1, len(datos) + 1))
    extremos_vals = [datos[i - 1] for i in extremos_idx]
    ax.scatter(extremos_idx, extremos_vals, color=GRIS, s=20,
               zorder=2, alpha=0.4, label='puntos sin ventana completa')

    ax.set_xlabel('Día')
    ax.set_ylabel('Contagios diarios (miles)')
    ax.set_ylim(0, max(datos) * 1.2)
    ax.set_xticks(dias)
    ax.legend(fontsize=9, framealpha=0.9)

    # Título
    mitad_v = ventana // 2
    ax.set_title(
        f'{nombre.capitalize()} corrida — ventana de {ventana} días   '
        f'(cada punto suavizado usa los {ventana} días centrados a su alrededor)',
        fontsize=9, color=GRIS
    )

    plt.tight_layout()
    plt.show()

    # ── Tabla comparativa ──────────────────────────────────────
    print(f"\n{'Día':<6} {'Original':<14} {nombre.capitalize()+' corrida':<18} {'Nota'}")
    print('─' * 56)
    for i, d in enumerate(datos):
        dia = i + 1
        if i in idx_s:
            j = list(idx_s).index(i)
            nota = '← aberrante eliminado' if i == idx_aber - 1 else ''
            print(f"  {dia:<5} {int(d):<14} {vals_s[j]:<18.1f} {nota}")
        else:
            print(f"  {dia:<5} {int(d):<14} {'—':<18} ← sin ventana completa")

    # ── Conexión con la ecuación ───────────────────────────────
    print(f'\nLimitaciones del filtro de ventana {ventana}:')
    print(f'  1. Cada observación dentro de la ventana pesa igual (1/{ventana}).')
    print( '  2. Las observaciones fuera de la ventana pesan exactamente cero.')
    print( '  3. El organismo necesita almacenar las últimas', ventana, 'observaciones.')
    print( '\nEl filtro exponencial (modelo de B&M) resuelve los tres problemas:')
    print( '  1. Pesos decrecientes: los eventos recientes pesan más.')
    print( '  2. Todos los eventos pasados contribuyen (peso > 0).')
    print( '  3. Solo necesita V_{t} y R_t — sin almacenar historial.')


# ── Controles ──────────────────────────────────────────────────
estilo = {'description_width': '90px'}

w_vent = widgets.IntSlider(
    value=3, min=3, max=9, step=2,
    description='Ventana:', style=estilo,
    layout=widgets.Layout(width='380px'))

w_tipo = widgets.ToggleButtons(
    options=[('Mediana', True), ('Media', False)],
    value=True,
    description='Filtro:',
    style={'description_width': '60px', 'button_width': '90px'})

ui = widgets.VBox([
    widgets.HTML('<b style="color:#2C5282; font-family:serif;">'
                 'Simulador: Media y Mediana Corrida</b>'),
    widgets.HBox([w_vent, w_tipo]),
])

out = widgets.interactive_output(
    graficar_filtro,
    {'ventana': w_vent, 'usar_mediana': w_tipo}
)

display(ui, out)
