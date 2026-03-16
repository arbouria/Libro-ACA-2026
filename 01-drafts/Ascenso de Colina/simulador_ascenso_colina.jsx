import { useState, useEffect, useRef, useCallback } from "react";

// ── Constants ──────────────────────────────────────────────────────────────
const W = 500, H = 500;
const CELL = 5;
const COLS = W / CELL, ROWS = H / CELL;

// Generate a smooth nutrient landscape with multiple peaks
function buildLandscape(seed = 42) {
  const grid = new Float32Array(COLS * ROWS);
  const peaks = [
    { x: 0.75, y: 0.25, strength: 1.0, sigma: 0.18 },  // main peak (large)
    { x: 0.2,  y: 0.7,  strength: 0.55, sigma: 0.12 }, // local max (trap)
    { x: 0.55, y: 0.65, strength: 0.3, sigma: 0.09 },  // small bump
  ];
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      let val = 0;
      const nx = c / COLS, ny = r / ROWS;
      for (const p of peaks) {
        const dx = nx - p.x, dy = ny - p.y;
        val += p.strength * Math.exp(-(dx * dx + dy * dy) / (2 * p.sigma * p.sigma));
      }
      // Add gentle background gradient so it's never completely flat
      val += 0.05 * (1 - nx) + 0.03 * ny;
      grid[r * COLS + c] = val;
    }
  }
  // Normalize 0-1
  let mn = Infinity, mx = -Infinity;
  for (let i = 0; i < grid.length; i++) { mn = Math.min(mn, grid[i]); mx = Math.max(mx, grid[i]); }
  for (let i = 0; i < grid.length; i++) grid[i] = (grid[i] - mn) / (mx - mn);
  return grid;
}

function sampleLandscape(grid, x, y) {
  const c = Math.min(COLS - 1, Math.max(0, Math.round(x / CELL)));
  const r = Math.min(ROWS - 1, Math.max(0, Math.round(y / CELL)));
  return grid[r * COLS + c];
}

// ── Color mapping for landscape ───────────────────────────────────────────
function concentrationColor(v) {
  // Blue (low) → Teal → Green → Yellow (high)
  const stops = [
    [0,   [15, 32, 80]],
    [0.3, [20, 80, 120]],
    [0.6, [30, 140, 100]],
    [0.85,[160, 200, 60]],
    [1.0, [255, 240, 20]],
  ];
  for (let i = 0; i < stops.length - 1; i++) {
    const [t0, c0] = stops[i];
    const [t1, c1] = stops[i + 1];
    if (v >= t0 && v <= t1) {
      const t = (v - t0) / (t1 - t0);
      return c0.map((ch, j) => Math.round(ch + t * (c1[j] - ch)));
    }
  }
  return [255, 240, 20];
}

const LANDSCAPE = buildLandscape();

// Pre-render landscape to ImageData
function buildLandscapeImage() {
  const img = new ImageData(W, H);
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      const v = LANDSCAPE[r * COLS + c];
      const [R, G, B] = concentrationColor(v);
      for (let dy = 0; dy < CELL; dy++) {
        for (let dx = 0; dx < CELL; dx++) {
          const px = ((r * CELL + dy) * W + (c * CELL + dx)) * 4;
          img.data[px]     = R;
          img.data[px + 1] = G;
          img.data[px + 2] = B;
          img.data[px + 3] = 255;
        }
      }
    }
  }
  return img;
}

const LANDSCAPE_IMG = buildLandscapeImage();

// ── Agent logic ───────────────────────────────────────────────────────────
function createAgent(startX = 60, startY = 380) {
  return {
    x: startX, y: startY,
    vx: 0, vy: 0,
    Y: 0,
    prevX: 0,
    mode: "explore",   // "explore" | "exploit"
    steps: 0,
    exploitSteps: 0,
    exploreSteps: 0,
    maxConc: 0,
    history: [{ x: startX, y: startY, mode: "explore" }],
  };
}

const SPEED = 2.8;
const TUMBLE_STEPS = 8;   // steps in one tumble before resampling direction
const RUN_MIN = 12;        // minimum run steps before checking again

function stepAgent(agent, a, b, noiseLevel, landscape) {
  const ag = { ...agent, history: agent.history };
  const prevX = ag.x, prevY = ag.y;

  // Sample current and previous concentration
  const Xt1 = sampleLandscape(landscape, ag.x, ag.y);
  const Xt  = sampleLandscape(landscape, ag.prevX || ag.x, ag.prevY || ag.y);

  // Noise
  const noise = (Math.random() - 0.5) * noiseLevel * 0.4;

  // Update decision variable
  const dX = (Xt1 - Xt) + noise;
  ag.Y = a * ag.Y + b * dX;
  ag.steps++;

  const threshold = 0;

  if (ag.Y > threshold) {
    // EXPLOIT — run straight
    ag.mode = "exploit";
    ag.exploitSteps++;
    // Small wobble so it looks biological
    const wobble = (Math.random() - 0.5) * 0.3;
    const angle = Math.atan2(ag.vy, ag.vx) + wobble;
    ag.vx = Math.cos(angle) * SPEED;
    ag.vy = Math.sin(angle) * SPEED;
  } else {
    // EXPLORE — tumble: pick random direction
    ag.mode = "explore";
    ag.exploreSteps++;
    if (ag.steps % TUMBLE_STEPS === 0) {
      const angle = Math.random() * 2 * Math.PI;
      ag.vx = Math.cos(angle) * SPEED;
      ag.vy = Math.sin(angle) * SPEED;
    }
  }

  // Move
  let nx = ag.x + ag.vx;
  let ny = ag.y + ag.vy;

  // Bounce off walls
  if (nx < 4)     { nx = 4;     ag.vx = Math.abs(ag.vx); }
  if (nx > W - 4) { nx = W - 4; ag.vx = -Math.abs(ag.vx); }
  if (ny < 4)     { ny = 4;     ag.vy = Math.abs(ag.vy); }
  if (ny > H - 4) { ny = H - 4; ag.vy = -Math.abs(ag.vy); }

  ag.prevX = prevX;
  ag.prevY = prevY;
  ag.x = nx;
  ag.y = ny;

  const conc = sampleLandscape(landscape, ag.x, ag.y);
  ag.maxConc = Math.max(ag.maxConc, conc);

  // Keep trail (max 400 points)
  const newHistory = [...ag.history, { x: nx, y: ny, mode: ag.mode }];
  ag.history = newHistory.length > 400 ? newHistory.slice(newHistory.length - 400) : newHistory;

  return ag;
}

// ── Chart: Y over time ────────────────────────────────────────────────────
function YChart({ yHistory, threshold }) {
  const W2 = 300, H2 = 80;
  if (yHistory.length < 2) return null;
  const mn = Math.min(...yHistory, threshold - 0.1);
  const mx = Math.max(...yHistory, threshold + 0.1);
  const range = mx - mn || 1;
  const pts = yHistory.slice(-W2).map((v, i) => {
    const x = (i / (Math.min(yHistory.length, W2) - 1)) * (W2 - 4) + 2;
    const y = H2 - 4 - ((v - mn) / range) * (H2 - 8);
    return `${x},${y}`;
  }).join(" ");
  const zeroY = H2 - 4 - ((threshold - mn) / range) * (H2 - 8);
  return (
    <svg width={W2} height={H2} style={{ background: "#0d1117", borderRadius: 6, display: "block" }}>
      <line x1={0} y1={zeroY} x2={W2} y2={zeroY} stroke="#4a9" strokeDasharray="3,3" strokeWidth={1} />
      <text x={W2 - 4} y={zeroY - 3} fill="#4a9" fontSize={9} textAnchor="end">umbral</text>
      <polyline points={pts} fill="none" stroke="#7ec8e3" strokeWidth={1.5} />
    </svg>
  );
}

// ── Concentration chart ───────────────────────────────────────────────────
function ConcChart({ concHistory }) {
  const W2 = 300, H2 = 60;
  if (concHistory.length < 2) return null;
  const pts = concHistory.slice(-W2).map((v, i) => {
    const x = (i / (Math.min(concHistory.length, W2) - 1)) * (W2 - 4) + 2;
    const y = H2 - 4 - v * (H2 - 8);
    return `${x},${y}`;
  }).join(" ");
  return (
    <svg width={W2} height={H2} style={{ background: "#0d1117", borderRadius: 6, display: "block" }}>
      <polyline points={pts} fill="none" stroke="#f0c040" strokeWidth={1.5} />
    </svg>
  );
}

// ── Main component ────────────────────────────────────────────────────────
export default function AscensoDeColina() {
  const canvasRef = useRef(null);
  const animRef   = useRef(null);
  const agentRef  = useRef(createAgent());

  const [params, setParams] = useState({ a: 0.88, b: 0.7, noise: 0.2 });
  const [running, setRunning] = useState(false);
  const [step, setStep]       = useState(0);
  const [yHistory, setYHistory]     = useState([]);
  const [concHistory, setConcHistory] = useState([]);
  const [mode, setMode]   = useState("explore");
  const [conc, setConc]   = useState(0);
  const [maxConc, setMaxConc] = useState(0);
  const [showLegend, setShowLegend] = useState(true);

  // Draw everything onto canvas
  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    // Background landscape
    ctx.putImageData(LANDSCAPE_IMG, 0, 0);

    const ag = agentRef.current;
    const hist = ag.history;

    // Draw trail
    for (let i = 1; i < hist.length; i++) {
      const alpha = (i / hist.length) * 0.7;
      const p = hist[i];
      const prev = hist[i - 1];
      ctx.beginPath();
      ctx.moveTo(prev.x, prev.y);
      ctx.lineTo(p.x, p.y);
      ctx.strokeStyle = p.mode === "exploit"
        ? `rgba(255, 120, 50, ${alpha})`
        : `rgba(120, 200, 255, ${alpha * 0.6})`;
      ctx.lineWidth = p.mode === "exploit" ? 1.8 : 1.2;
      ctx.stroke();
    }

    // Draw agent
    const r = 6;
    ctx.beginPath();
    ctx.arc(ag.x, ag.y, r, 0, Math.PI * 2);
    ctx.fillStyle = ag.mode === "exploit" ? "#ff7832" : "#7ed6f8";
    ctx.fill();
    ctx.strokeStyle = "white";
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Direction arrow (only in exploit mode)
    if (ag.mode === "exploit" && (ag.vx !== 0 || ag.vy !== 0)) {
      const len = 14;
      const norm = Math.sqrt(ag.vx ** 2 + ag.vy ** 2);
      const dx = (ag.vx / norm) * len;
      const dy = (ag.vy / norm) * len;
      ctx.beginPath();
      ctx.moveTo(ag.x, ag.y);
      ctx.lineTo(ag.x + dx, ag.y + dy);
      ctx.strokeStyle = "rgba(255,255,255,0.8)";
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }

    // Peak markers
    const peaks = [
      { x: 0.75 * W, y: 0.25 * H, label: "Fuente\nprincipal", major: true },
      { x: 0.2  * W, y: 0.70 * H, label: "Máximo\nlocal", major: false },
    ];
    for (const pk of peaks) {
      ctx.beginPath();
      ctx.arc(pk.x, pk.y, pk.major ? 8 : 6, 0, Math.PI * 2);
      ctx.strokeStyle = pk.major ? "#fff" : "rgba(255,255,255,0.6)";
      ctx.lineWidth = pk.major ? 2 : 1.5;
      ctx.setLineDash([4, 3]);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.font = "10px Arial";
      ctx.fillStyle = "rgba(255,255,255,0.9)";
      ctx.textAlign = "center";
      const lines = pk.label.split("\n");
      lines.forEach((l, i) => ctx.fillText(l, pk.x, pk.y - 12 - i * 13));
    }
  }, []);

  // Tick
  const tick = useCallback(() => {
    agentRef.current = stepAgent(
      agentRef.current, params.a, params.b, params.noise, LANDSCAPE
    );
    const ag = agentRef.current;
    setStep(s => s + 1);
    setMode(ag.mode);
    setConc(sampleLandscape(LANDSCAPE, ag.x, ag.y));
    setMaxConc(ag.maxConc);
    setYHistory(prev => {
      const next = [...prev, ag.Y];
      return next.length > 600 ? next.slice(next.length - 600) : next;
    });
    setConcHistory(prev => {
      const c = sampleLandscape(LANDSCAPE, ag.x, ag.y);
      const next = [...prev, c];
      return next.length > 600 ? next.slice(next.length - 600) : next;
    });
    draw();
  }, [params, draw]);

  useEffect(() => {
    draw();
  }, [draw]);

  useEffect(() => {
    if (running) {
      const id = setInterval(tick, 40);
      animRef.current = id;
      return () => clearInterval(id);
    }
  }, [running, tick]);

  const reset = () => {
    if (animRef.current) clearInterval(animRef.current);
    setRunning(false);
    agentRef.current = createAgent();
    setStep(0);
    setYHistory([]);
    setConcHistory([]);
    setMode("explore");
    setConc(0);
    setMaxConc(0);
    setTimeout(draw, 20);
  };

  const Slider = ({ label, param, min, max, step: st = 0.01, hint }) => (
    <div style={{ marginBottom: 14 }}>
      <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 4 }}>
        <span style={{ color: "#c9d1d9", fontSize: 13, fontWeight: 600 }}>{label}</span>
        <span style={{ color: "#7ec8e3", fontSize: 13, fontFamily: "monospace" }}>
          {params[param].toFixed(2)}
        </span>
      </div>
      <input
        type="range" min={min} max={max} step={st}
        value={params[param]}
        onChange={e => setParams(p => ({ ...p, [param]: parseFloat(e.target.value) }))}
        style={{ width: "100%", accentColor: "#7ec8e3" }}
      />
      {hint && <div style={{ fontSize: 11, color: "#8b949e", marginTop: 3 }}>{hint}</div>}
    </div>
  );

  const exploitPct = step > 0
    ? Math.round((agentRef.current.exploitSteps / step) * 100) : 0;

  return (
    <div style={{
      background: "#0d1117", color: "#c9d1d9", fontFamily: "Arial, sans-serif",
      minHeight: "100vh", padding: "20px", boxSizing: "border-box"
    }}>
      <div style={{ maxWidth: 860, margin: "0 auto" }}>

        {/* Header */}
        <div style={{ marginBottom: 16 }}>
          <h2 style={{ color: "#e6edf3", margin: "0 0 4px", fontSize: 20 }}>
            Simulador: Ascenso de Colina
          </h2>
          <p style={{ margin: 0, fontSize: 13, color: "#8b949e" }}>
            Una bacteria busca nutrientes siguiendo gradientes químicos sin receptores de distancia.
            Ajusta los parámetros y observa cómo cambia la estrategia.
          </p>
        </div>

        <div style={{ display: "flex", gap: 16, flexWrap: "wrap" }}>

          {/* Canvas */}
          <div style={{ flex: "0 0 auto" }}>
            <canvas
              ref={canvasRef} width={W} height={H}
              style={{ borderRadius: 8, border: "1px solid #30363d", display: "block" }}
            />
            {/* Legend */}
            {showLegend && (
              <div style={{ display: "flex", gap: 16, marginTop: 8, fontSize: 12, color: "#8b949e" }}>
                <span><span style={{ color: "#7ed6f8" }}>━</span> Exploración (maromas)</span>
                <span><span style={{ color: "#ff7832" }}>━</span> Explotación (nado recto)</span>
                <span>○ Picos de concentración</span>
              </div>
            )}
          </div>

          {/* Controls */}
          <div style={{ flex: "1 1 220px", minWidth: 220 }}>

            {/* Mode indicator */}
            <div style={{
              background: mode === "exploit" ? "rgba(255,120,50,0.15)" : "rgba(126,214,248,0.1)",
              border: `1px solid ${mode === "exploit" ? "#ff7832" : "#7ed6f8"}`,
              borderRadius: 8, padding: "10px 14px", marginBottom: 14,
              display: "flex", justifyContent: "space-between", alignItems: "center"
            }}>
              <div>
                <div style={{ fontSize: 11, color: "#8b949e", marginBottom: 2 }}>Modo actual</div>
                <div style={{
                  fontSize: 15, fontWeight: 700,
                  color: mode === "exploit" ? "#ff7832" : "#7ed6f8"
                }}>
                  {mode === "exploit" ? "⟶ Explotación" : "↺ Exploración"}
                </div>
              </div>
              <div style={{ textAlign: "right" }}>
                <div style={{ fontSize: 11, color: "#8b949e" }}>Y(t)</div>
                <div style={{ fontFamily: "monospace", fontSize: 14, color: "#e6edf3" }}>
                  {agentRef.current?.Y?.toFixed(3) ?? "0.000"}
                </div>
              </div>
            </div>

            {/* Stats */}
            <div style={{
              background: "#161b22", borderRadius: 8, padding: "10px 14px", marginBottom: 14,
              display: "grid", gridTemplateColumns: "1fr 1fr", gap: "8px 12px", fontSize: 12
            }}>
              <div>
                <div style={{ color: "#8b949e" }}>Concentración</div>
                <div style={{ color: "#f0c040", fontFamily: "monospace" }}>
                  {(conc * 100).toFixed(1)}%
                </div>
              </div>
              <div>
                <div style={{ color: "#8b949e" }}>Máx. alcanzado</div>
                <div style={{ color: "#4ac", fontFamily: "monospace" }}>
                  {(maxConc * 100).toFixed(1)}%
                </div>
              </div>
              <div>
                <div style={{ color: "#8b949e" }}>Pasos</div>
                <div style={{ color: "#e6edf3", fontFamily: "monospace" }}>{step}</div>
              </div>
              <div>
                <div style={{ color: "#8b949e" }}>% explotación</div>
                <div style={{ color: "#ff9870", fontFamily: "monospace" }}>{exploitPct}%</div>
              </div>
            </div>

            {/* Sliders */}
            <div style={{ background: "#161b22", borderRadius: 8, padding: "12px 14px", marginBottom: 14 }}>
              <Slider label="a — Adaptación sensorial" param="a" min={0.1} max={0.99}
                hint={params.a > 0.9 ? "Adaptación lenta: explota largamente" : params.a < 0.5 ? "Adaptación rápida: explora más" : "Balance moderado"} />
              <Slider label="b — Sensibilidad al cambio" param="b" min={0.1} max={2.0}
                hint={params.b > 1.4 ? "Muy sensible: responde a ruido" : params.b < 0.4 ? "Poco sensible: ignora cambios pequeños" : "Sensibilidad normal"} />
              <Slider label="Ruido ambiental" param="noise" min={0} max={1.0}
                hint={params.noise > 0.6 ? "Ruido alto: señal difícil de seguir" : params.noise < 0.2 ? "Entorno limpio" : "Ruido moderado"} />
            </div>

            {/* Buttons */}
            <div style={{ display: "flex", gap: 8 }}>
              <button onClick={() => setRunning(r => !r)} style={{
                flex: 1, padding: "9px 0", borderRadius: 6, border: "none", cursor: "pointer",
                background: running ? "#21262d" : "#238636",
                color: running ? "#c9d1d9" : "white", fontWeight: 600, fontSize: 14
              }}>
                {running ? "⏸ Pausar" : "▶ Iniciar"}
              </button>
              <button onClick={reset} style={{
                padding: "9px 14px", borderRadius: 6, border: "1px solid #30363d",
                background: "transparent", color: "#8b949e", cursor: "pointer", fontSize: 14
              }}>
                ↺ Reiniciar
              </button>
            </div>

            {/* Presets */}
            <div style={{ marginTop: 12 }}>
              <div style={{ fontSize: 11, color: "#8b949e", marginBottom: 6 }}>Experimentos rápidos:</div>
              <div style={{ display: "flex", flexDirection: "column", gap: 5 }}>
                {[
                  { label: "Atrapado en máximo local", a: 0.97, b: 0.5, noise: 0.05 },
                  { label: "Exploración excesiva",     a: 0.25, b: 1.0, noise: 0.1 },
                  { label: "Balance óptimo",           a: 0.88, b: 0.7, noise: 0.15 },
                  { label: "Entorno muy ruidoso",      a: 0.70, b: 1.5, noise: 0.85 },
                ].map(preset => (
                  <button key={preset.label} onClick={() => { reset(); setTimeout(() => setParams({ a: preset.a, b: preset.b, noise: preset.noise }), 50); }} style={{
                    padding: "6px 10px", borderRadius: 5, border: "1px solid #30363d",
                    background: "#161b22", color: "#c9d1d9", cursor: "pointer",
                    fontSize: 11, textAlign: "left"
                  }}>
                    {preset.label}
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Charts */}
        <div style={{ marginTop: 16, display: "flex", gap: 16, flexWrap: "wrap" }}>
          <div style={{ flex: "1 1 300px" }}>
            <div style={{ fontSize: 11, color: "#8b949e", marginBottom: 4 }}>
              Variable de decisión Y(t) — explotar cuando Y &gt; 0
            </div>
            <YChart yHistory={yHistory} threshold={0} />
          </div>
          <div style={{ flex: "1 1 300px" }}>
            <div style={{ fontSize: 11, color: "#8b949e", marginBottom: 4 }}>
              Concentración detectada X(t)
            </div>
            <ConcChart concHistory={concHistory} />
          </div>
        </div>

        {/* Equation display */}
        <div style={{
          marginTop: 16, background: "#161b22", borderRadius: 8,
          padding: "12px 16px", fontSize: 13
        }}>
          <div style={{ color: "#8b949e", marginBottom: 8, fontSize: 11 }}>
            La ecuación que rige este simulador:
          </div>
          <div style={{ fontFamily: "monospace", color: "#e6edf3", fontSize: 15, letterSpacing: 1 }}>
            Y(t+1) = <span style={{ color: "#7ec8e3" }}>a</span> · Y(t) + <span style={{ color: "#f0c040" }}>b</span> · [X(t+1) − X(t)]
          </div>
          <div style={{ marginTop: 10, display: "flex", gap: 20, fontSize: 12, color: "#8b949e" }}>
            <span>
              <span style={{ color: "#7ec8e3" }}>a = {params.a.toFixed(2)}</span>
              {" "}(adaptación sensorial)
            </span>
            <span>
              <span style={{ color: "#f0c040" }}>b = {params.b.toFixed(2)}</span>
              {" "}(sensibilidad al cambio)
            </span>
            <span>Y &gt; 0 → explotar, Y ≤ 0 → explorar</span>
          </div>
        </div>

      </div>
    </div>
  );
}
