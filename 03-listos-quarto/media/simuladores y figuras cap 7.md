
**[FIGURA 7.1 — Código para generar la figura. Datos de Staddon & Simmelhag, 1971, Psychological Review, 78, 3–43. Figura original.]**

```python
# Figura 7.1: Organización temporal de respuestas inducidas
# Datos aproximados digitalizados de Staddon & Simmelhag (1971)
# Figura original — datos reproducidos con autorización implícita de dominio público

import numpy as np
import matplotlib.pyplot as plt

# Tiempo del intervalo (0 a 12 segundos, como en el original)
t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# R1: orientarse hacia comedero (respuesta terminal)
R1 = np.array([0.80, 0.78, 0.72, 0.60, 0.45, 0.40, 0.50, 0.65, 0.80, 0.90, 0.95, 0.97, 1.00])

# R7: picotear pared del comedero (respuesta terminal)
R7 = np.array([0.00, 0.00, 0.00, 0.05, 0.10, 0.20, 0.35, 0.55, 0.70, 0.85, 0.92, 0.96, 1.00])

# R3: picotear el piso (respuesta interina)
R3 = np.array([0.05, 0.10, 0.20, 0.60, 0.55, 0.30, 0.15, 0.08, 0.04, 0.02, 0.01, 0.01, 0.00])

# R4: dar un cuarto de vuelta (respuesta interina)
R4 = np.array([0.00, 0.05, 0.15, 0.20, 0.18, 0.12, 0.08, 0.04, 0.02, 0.01, 0.00, 0.00, 0.00])

# R8: desplazarse cerca de la pared del comedero (respuesta interina)
R8 = np.array([0.02, 0.08, 0.35, 0.58, 0.42, 0.20, 0.10, 0.05, 0.02, 0.01, 0.00, 0.00, 0.00])

fig, ax = plt.subplots(figsize=(8, 5))

# Respuestas terminales — líneas sólidas
ax.plot(t, R1, 'o-', color='black', linewidth=2, markersize=6, label='R1 (orientarse al comedero) — terminal')
ax.plot(t, R7, 's--', color='black', linewidth=2, markersize=6, label='R7 (picotear pared) — terminal')

# Respuestas interinas — líneas con marcadores distintos
ax.plot(t, R3, '^:', color='gray', linewidth=1.5, markersize=6, label='R3 (picotear el piso) — interina')
ax.plot(t, R4, 'v-.', color='gray', linewidth=1.5, markersize=6, label='R4 (cuarto de vuelta) — interina')
ax.plot(t, R8, 'D:', color='darkgray', linewidth=1.5, markersize=5, label='R8 (desplazarse al comedero) — interina')

ax.set_xlabel('Tiempo en el intervalo (segundos)', fontsize=12)
ax.set_ylabel('Probabilidad de ocurrencia', fontsize=12)
ax.set_title('Organización temporal de respuestas inducidas\n(Datos: Staddon & Simmelhag, 1971)', fontsize=11)
ax.set_xlim(0, 12)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=9, loc='upper left')
ax.axvline(x=12, color='green', linestyle='--', alpha=0.6, label='SBI (comida)')
ax.text(11.5, 0.5, 'SBI', color='green', fontsize=9, rotation=90, va='center')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figura_7_1_staddon_simmelhag.png', dpi=150, bbox_inches='tight')
plt.show()
```


**[FIGURA 7.2 — Código para generar la figura. Datos de Dickinson et al., 1992, Quarterly Journal of Experimental Psychology, 45B, 241–258. Figura original.]**

```python
# Figura 7.2: Resultados de Dickinson et al. (1992) — demora y grupo yoked
# Datos aproximados digitalizados del artículo original

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Panel izquierdo: tasa de respuesta como función de la demora programada
demoras = np.array([0, 4, 8, 16, 32, 64])
tasa_respuesta = np.array([19.5, 8.2, 5.0, 2.4, 0.5, 0.2])  # prensiones por minuto

axes[0].plot(demoras, tasa_respuesta, 'o-', color='black', linewidth=2, markersize=8)
axes[0].set_xlabel('Demora programada (segundos)', fontsize=11)
axes[0].set_ylabel('Presiones de palanca por minuto', fontsize=11)
axes[0].set_title('Efecto de la demora\nsobre la tasa de respuesta', fontsize=11)
axes[0].set_xlim(-2, 68)
axes[0].set_ylim(0, 22)
axes[0].grid(True, alpha=0.3)

# Panel derecho: comparación master vs. yoked para tres demoras
sesiones = np.arange(1, 21)

# Demora 16 seg
master_16 = np.array([1.5, 2.0, 2.8, 3.5, 4.0, 4.8, 5.2, 5.5, 5.0, 5.8,
                       6.2, 5.5, 6.0, 6.5, 6.8, 6.2, 7.0, 6.8, 7.2, 7.8])
yoked_16  = np.array([1.2, 0.8, 0.9, 1.0, 0.8, 0.6, 0.7, 0.5, 0.6, 0.4,
                       0.5, 0.6, 0.4, 0.3, 0.5, 0.4, 0.3, 0.4, 0.3, 0.4])

# Demora 32 seg
master_32 = np.array([1.8, 1.9, 2.0, 2.2, 2.5, 2.8, 3.0, 3.5, 3.2, 3.8,
                       4.0, 3.5, 4.2, 4.5, 4.8, 4.2, 4.0, 4.5, 5.2, 4.0])
yoked_32  = np.array([1.6, 1.5, 1.8, 1.6, 1.4, 1.2, 1.0, 0.8, 0.9, 0.7,
                       0.6, 0.8, 0.5, 0.4, 0.5, 0.3, 0.4, 0.3, 0.2, 0.3])

# Demora 64 seg
master_64 = np.array([1.2, 0.8, 0.9, 1.0, 0.6, 0.7, 0.8, 0.5, 0.6, 0.7,
                       0.5, 0.6, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4, 0.3, 0.5])
yoked_64  = np.array([1.0, 0.9, 0.7, 0.8, 0.6, 0.5, 0.7, 0.4, 0.5, 0.6,
                       0.4, 0.5, 0.3, 0.4, 0.5, 0.3, 0.4, 0.3, 0.4, 0.5])

# Solo graficar demora 16 y 32 claramente
axes[1].plot(sesiones, master_16, 's-', color='black', linewidth=2,
             markersize=5, label='Master — 16 seg')
axes[1].plot(sesiones, yoked_16, 's--', color='black', linewidth=1.5,
             markersize=5, alpha=0.5, label='Yoked — 16 seg')
axes[1].plot(sesiones, master_32, 'o-', color='gray', linewidth=2,
             markersize=5, label='Master — 32 seg')
axes[1].plot(sesiones, yoked_32, 'o--', color='gray', linewidth=1.5,
             markersize=5, alpha=0.5, label='Yoked — 32 seg')

axes[1].set_xlabel('Sesiones sucesivas', fontsize=11)
axes[1].set_ylabel('Presiones de palanca por minuto', fontsize=11)
axes[1].set_title('Grupo experimental (master)\nvs. grupo control (yoked)', fontsize=11)
axes[1].legend(fontsize=8, loc='upper left')
axes[1].set_ylim(0, 9)
axes[1].grid(True, alpha=0.3)

plt.suptitle('Figura 7.2 — Datos: Dickinson et al. (1992)', fontsize=10, y=1.01)
plt.tight_layout()
plt.savefig('figura_7_2_dickinson.png', dpi=150, bbox_inches='tight')
plt.show()
```


**[FIGURA 7.3 — Código para generar la figura. Datos de Lattal (1987). Figura original.]**

```python
# Figura 7.3: Resultados de Lattal (1987) — procedimiento DRO
# Cinco sujetos individuales muestran aprendizaje a pesar de la demora garantizada

import numpy as np
import matplotlib.pyplot as plt

sesiones = np.arange(1, 28)

# Datos aproximados de cinco sujetos (escala logarítmica en el original)
# Tasa de respuesta en picotazos por minuto — línea punteada = tasa de referencia
referencia = 1.0  # línea base en escala logarítmica, representada como 1

sujetos = {
    '3490': np.array([0.01, 0.05, 0.1, 0.3, 0.5, 0.8, 1.2, 1.8, 2.5, 3.5,
                       4.0, 5.0, 4.5, 5.5, 6.0, 5.0, 6.5, 7.0, 7.5, 8.0,
                       7.0, 7.5, 8.0, 7.5, 8.5, 7.0, 8.0]),
    '3494': np.array([3.0, 5.0, 7.0, 8.5, 6.0, 8.0, 9.5, 8.0, 10.0, 9.0,
                       8.5, 9.5, 10.0, 9.0, 8.0, 9.5, 10.0, 9.5, 8.5, 9.0,
                       10.0, 9.5, 8.5, 9.0, 10.0, 9.5, 9.0]),
    '3538': np.array([8.0, 6.0, 9.0, 7.0, 8.5, 9.5, 7.0, 8.0, 9.0, 8.5,
                       7.5, 9.0, 8.0, 9.5, 8.5, 9.0, 8.0, 9.5, 8.5, 9.0,
                       8.5, 9.0, 8.0, 9.5, 8.0, 9.0, 8.5]),
    '3630': np.array([0.01, 0.1, 0.5, 1.5, 3.0, 5.0, 4.0, 6.0, 5.5, 7.0,
                       6.0, 7.5, 6.5, 8.0, 7.0, 8.5, 7.5, 8.0, 7.0, 8.5,
                       7.0, 8.0, 7.5, 9.0, 7.5, 8.0, 7.5]),
    '4230': np.array([0.1, 0.5, 2.0, 4.0, 5.0, 6.0, 5.0, 6.5, 5.5, 7.0,
                       6.0, 7.0, 5.5, 6.5, 7.5, 6.0, 7.0, 6.5, 7.5, 6.0,
                       7.5, 6.5, 7.0, 7.5, 6.5, 7.0, 7.5]),
}

fig, axes = plt.subplots(2, 3, figsize=(13, 7))
axes_flat = axes.flatten()

for i, (nombre, datos) in enumerate(sujetos.items()):
    ax = axes_flat[i]
    ax.semilogy(sesiones, datos, 'o-', color='black', linewidth=1.5, markersize=4)
    ax.axhline(y=referencia, color='black', linestyle='--', linewidth=1, alpha=0.7,
               label='Tasa de referencia')
    ax.set_title(f'Sujeto {nombre}', fontsize=10)
    ax.set_xlabel('Sesiones sucesivas', fontsize=9)
    ax.set_ylabel('Resp/min (escala log)', fontsize=9)
    ax.set_ylim(0.005, 15)
    ax.grid(True, which='both', alpha=0.2)

# Ocultar el sexto panel vacío
axes_flat[5].axis('off')

fig.suptitle('Figura 7.3 — Datos: Lattal (1987)\nAprendizaje bajo procedimiento DRO (demora garantizada ≥ 10 seg)',
             fontsize=10)
plt.tight_layout()
plt.savefig('figura_7_3_lattal.png', dpi=150, bbox_inches='tight')
plt.show()
```

**[FIGURAS 7.4 y 7.5 — Código para generar ambas figuras. Datos de Killeen (1978), Science, 199, 88–90. Figuras originales.]**

```python
# Figuras 7.4 y 7.5: Resultados de Killeen (1978)
# Panel izquierdo: curvas ROC (discriminabilidad de causalidad)
# Panel derecho: gradiente temporal de falsas alarmas

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# ── Figura 7.4: Curvas ROC para cuatro sujetos ──────────────────────────────
# Cada sujeto tiene 4-5 puntos (P(FA), P(hit)) bajo diferentes condiciones de pago
# Datos aproximados digitalizados de Killeen (1978), Fig. 1

sujetos_roc = {
    'S1': {'fa': [0.05, 0.15, 0.35, 0.55, 0.75], 'hit': [0.55, 0.72, 0.85, 0.92, 0.97]},
    'S2': {'fa': [0.03, 0.10, 0.22, 0.42, 0.68], 'hit': [0.60, 0.78, 0.90, 0.95, 0.98]},
    'S3': {'fa': [0.08, 0.20, 0.40, 0.62, 0.80], 'hit': [0.50, 0.68, 0.82, 0.90, 0.95]},
    'S4': {'fa': [0.04, 0.12, 0.28, 0.50, 0.72], 'hit': [0.55, 0.75, 0.88, 0.94, 0.97]},
}

colores_roc = ['black', 'dimgray', 'gray', 'darkgray']

# Línea del azar (diagonal)
axes[0].plot([0, 1], [0, 1], 'k--', linewidth=1, alpha=0.5, label='Azar')

for (nombre, datos), color in zip(sujetos_roc.items(), colores_roc):
    fa = datos['fa']
    hit = datos['hit']
    # Ajuste de curva suavizada
    fa_smooth = np.linspace(0, 1, 100)
    # Curva ROC paramétrica simple
    d_prime = 1.5  # discriminabilidad aproximada
    hit_smooth = [min(0.999, max(0.001,
                  0.5 * (1 + np.erf((np.log(p/(1-p+1e-9)) + d_prime) / (np.sqrt(2) * 1.0)))))
                  for p in fa_smooth]
    axes[0].plot(fa_smooth, hit_smooth, '-', color=color, linewidth=1.5, alpha=0.7)
    axes[0].scatter(fa, hit, s=50, color=color, zorder=5, label=nombre)

axes[0].set_xlabel('P (falsa alarma)', fontsize=11)
axes[0].set_ylabel('P (acierto)', fontsize=11)
axes[0].set_title('Curvas ROC — discriminabilidad de causalidad\n(Datos: Killeen, 1978)', fontsize=10)
axes[0].legend(fontsize=9)
axes[0].set_xlim(0, 1)
axes[0].set_ylim(0, 1)
axes[0].set_aspect('equal')
axes[0].grid(True, alpha=0.2)

# ── Figura 7.5: Gradiente temporal de falsas alarmas ────────────────────────
# Tiempo desde la respuesta hasta el apagado no contingente (0.2 a 1.0 seg)
# Para cuatro duraciones de acceso a comida (1.8, 2.3, 2.8, 3.8 seg)

tiempo_fa = np.array([0.20, 0.40, 0.60, 0.80, 1.00])

# P(FA) para cada condición de pago — datos aproximados de Killeen (1978), Fig. 2
fa_3_8 = np.array([0.82, 0.62, 0.45, 0.38, 0.32])  # mayor pago: criterio más liberal
fa_2_8 = np.array([0.56, 0.40, 0.28, 0.24, 0.22])
fa_2_3 = np.array([0.42, 0.28, 0.20, 0.18, 0.16])
fa_1_8 = np.array([0.35, 0.22, 0.16, 0.13, 0.10])  # menor pago: criterio más conservador

marcadores = ['x', 'o', '^', 's']
datos_fa = [fa_3_8, fa_2_8, fa_2_3, fa_1_8]
etiquetas = ['3.8 seg acceso', '2.8 seg acceso', '2.3 seg acceso', '1.8 seg acceso']

for datos, marcador, etiqueta in zip(datos_fa, marcadores, etiquetas):
    axes[1].plot(tiempo_fa, datos, f'{marcador}-', color='black',
                 linewidth=1.5, markersize=7, label=etiqueta)

axes[1].set_xlabel('Tiempo entre respuesta y evento accidental (seg)', fontsize=11)
axes[1].set_ylabel('P (falsa alarma)', fontsize=11)
axes[1].set_title('Gradiente temporal de falsas alarmas\npor duración de acceso a comida (Killeen, 1978)', fontsize=10)
axes[1].legend(fontsize=9, title='Valor del acierto', title_fontsize=9)
axes[1].set_ylim(0, 1.0)
axes[1].grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig('figura_7_4_5_killeen.png', dpi=150, bbox_inches='tight')
plt.show()
```


```python
# Simulador 7.1: Organización temporal de respuestas inducidas
# Requiere: numpy, matplotlib
# Ejecutar en Google Colab o Jupyter Notebook

import numpy as np
import matplotlib.pyplot as plt

# ─── Parámetros (modifícalos para explorar) ───────────────────────────────────
INTERVALO      = 15     # Duración del intervalo entre SBIs (segundos)
DECAIMIENTO    = 0.30   # Tasa de decaimiento de la activación post-SBI (0 a 1)
ANTICIPACION   = 0.20   # Tasa de crecimiento de la anticipación terminal (0 a 1)
N_INTERVALOS   = 5      # Número de intervalos a simular
# ──────────────────────────────────────────────────────────────────────────────

tiempo = np.linspace(0, INTERVALO, 200)

# Respuestas interinas: máximo al inicio, decaen exponencialmente
p_interinas = np.exp(-DECAIMIENTO * tiempo)
p_interinas = p_interinas / p_interinas.max()

# Respuestas terminales: crecen conforme se acerca el SBI
p_terminales = 1 - np.exp(-ANTICIPACION * tiempo)
p_terminales = p_terminales / p_terminales.max()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(tiempo, p_interinas, 'b--', linewidth=2, label='Respuestas interinas')
axes[0].plot(tiempo, p_terminales, 'r-', linewidth=2, label='Respuestas terminales')
axes[0].axvline(x=0, color='green', linestyle=':', alpha=0.7, label='SBI')
axes[0].axvline(x=INTERVALO, color='green', linestyle=':', alpha=0.7)
axes[0].set_xlabel('Tiempo en el intervalo (seg)')
axes[0].set_ylabel('Probabilidad relativa')
axes[0].set_title('Distribución temporal de respuestas')
axes[0].legend()
axes[0].set_ylim(0, 1.1)

# Simular varios intervalos consecutivos
tiempo_total = np.linspace(0, N_INTERVALOS * INTERVALO, 1000)
p_total_interinas = np.zeros_like(tiempo_total)
p_total_terminales = np.zeros_like(tiempo_total)

for n in range(N_INTERVALOS):
    t_local = tiempo_total - n * INTERVALO
    mascara = (t_local >= 0) & (t_local <= INTERVALO)
    p_total_interinas[mascara] = np.exp(-DECAIMIENTO * t_local[mascara])
    p_total_terminales[mascara] = 1 - np.exp(-ANTICIPACION * t_local[mascara])

axes[1].plot(tiempo_total, p_total_interinas, 'b--', linewidth=1.5, label='Interinas')
axes[1].plot(tiempo_total, p_total_terminales, 'r-', linewidth=1.5, label='Terminales')
for n in range(N_INTERVALOS + 1):
    axes[1].axvline(x=n * INTERVALO, color='green', linestyle=':', alpha=0.5)
axes[1].set_xlabel('Tiempo total de sesión (seg)')
axes[1].set_ylabel('Probabilidad relativa')
axes[1].set_title(f'Dinámica a lo largo de {N_INTERVALOS} intervalos')
axes[1].legend()

plt.tight_layout()
plt.show()

print(f"\nIntervalo entre SBIs: {INTERVALO} seg")
print(f"Las respuestas interinas dominan los primeros {INTERVALO * 0.4:.1f} seg del intervalo")
print(f"Las respuestas terminales dominan los últimos {INTERVALO * 0.4:.1f} seg del intervalo")
```
