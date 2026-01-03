# Snippets de Ecuaciones Comunes

## Ecuaciones en Línea

Usar `$ecuación$` para ecuaciones en línea con el texto.

Ejemplo: La velocidad $v = \frac{d}{t}$ relaciona distancia y tiempo.

## Ecuaciones en Bloque

Usar `$$ecuación$$` para ecuaciones destacadas:

$$
E = mc^2
$$

## Ecuaciones Numeradas (Quarto)

```latex
$$
E = mc^2
$$ {#eq-energia}
```

Referencia en el texto: Como vemos en @eq-energia...

## Fracciones

```latex
$$
\frac{numerador}{denominador}
$$
```

## Integrales

```latex
$$
\int_{a}^{b} f(x) \, dx
$$
```

Integral definida:
$$
\int_{0}^{\infty} e^{-x} \, dx = 1
$$

## Derivadas

```latex
$$
\frac{d}{dx} f(x) = f'(x)
$$
```

Derivada parcial:
$$
\frac{\partial f}{\partial x}
$$

## Sumatorias

```latex
$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$
```

## Matrices

```latex
$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$
```

## Sistemas de Ecuaciones

```latex
$$
\begin{cases}
x + y = 5 \\
2x - y = 1
\end{cases}
$$
```

## Vectores

```latex
$$
\vec{v} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}
$$
```

## Límites

```latex
$$
\lim_{x \to \infty} \frac{1}{x} = 0
$$
```

## Raíces

```latex
$$
\sqrt{x^2 + y^2}
$$
```

Raíz n-ésima:
$$
\sqrt[n]{x}
$$

## Operadores Comunes

- Producto: `\cdot` → $a \cdot b$
- Producto cruz: `\times` → $\vec{a} \times \vec{b}$
- Producto punto: `\cdot` → $\vec{a} \cdot \vec{b}$
- Aproximadamente: `\approx` → $\pi \approx 3.14$
- Proporcional: `\propto` → $F \propto ma$
- Menor/mayor o igual: `\leq`, `\geq` → $x \geq 0$
- Flechas: `\rightarrow`, `\Rightarrow` → $x \rightarrow y$

## Letras Griegas Comunes

- `\alpha`, `\beta`, `\gamma`, `\delta`
- `\epsilon`, `\theta`, `\lambda`, `\mu`
- `\pi`, `\rho`, `\sigma`, `\tau`
- `\phi`, `\psi`, `\omega`
- Mayúsculas: `\Delta`, `\Sigma`, `\Omega`

## Plantilla de Demostración

```latex
$$
\begin{align}
f(x) &= x^2 + 2x + 1 \\
     &= (x+1)^2 \\
     &= (x+1)(x+1)
\end{align}
$$
```

## Ecuaciones Físicas Comunes

### Cinemática
```latex
$$
v_f = v_i + at
$$
```

### Segunda Ley de Newton
```latex
$$
\vec{F} = m\vec{a}
$$
```

### Energía Cinética
```latex
$$
E_k = \frac{1}{2}mv^2
$$
```

### Ley de Coulomb
```latex
$$
F = k\frac{q_1 q_2}{r^2}
$$
```

### Ecuación de Onda
```latex
$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
$$
```

## Consejos

1. **Vista previa**: MWeb renderiza LaTeX en tiempo real
2. **Espaciado**: Usa `\,` para espacio pequeño, `\quad` para espacio medio
3. **Alineación**: Usa `\begin{align}...\end{align}` para múltiples líneas
4. **Texto en ecuaciones**: Usa `\text{texto aquí}` dentro de ecuaciones
5. **Tamaño**: `\displaystyle` fuerza tamaño grande en línea

Ejemplo de texto en ecuación:
$$
E_{\text{total}} = E_{\text{cinética}} + E_{\text{potencial}}
$$
