import { useState } from "react";

const levels = [
  {
    id: "ultimate",
    label: "¿Por qué existe?",
    sublabel: "Causas últimas",
    marr: "Nivel computacional",
    tinbergen: "Función · Evolución",
    killeen: "Logra · Representa",
    example: "¿Qué problema adaptativo resuelve la quimiotaxis?",
    color: "#2D3A4A",
    accent: "#6FB3D2",
    height: "h-28",
    width: "w-3/5",
  },
  {
    id: "proximate",
    label: "¿Cómo funciona?",
    sublabel: "Causas próximas",
    marr: "Nivel algorítmico",
    tinbergen: "Mecanismo · Desarrollo",
    killeen: "Induce · Logra",
    example: "¿Qué regla de decisión produce el ascenso de colina?",
    color: "#3A4A2D",
    accent: "#8FC87A",
    height: "h-28",
    width: "w-4/5",
  },
  {
    id: "implementation",
    label: "¿En qué sustrato?",
    sublabel: "Implementación",
    marr: "Nivel de implementación",
    tinbergen: "Mecanismo físico",
    killeen: "Subyace",
    example: "¿Qué receptores y vías moleculares producen la respuesta?",
    color: "#3A2D4A",
    accent: "#B07FD4",
    height: "h-28",
    width: "w-full",
  },
];

export default function NivelesAnalisis() {
  const [active, setActive] = useState(null);

  return (
    <div
      style={{ fontFamily: "'Georgia', serif" }}
      className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-8"
    >
      <div className="w-full max-w-2xl">
        {/* Title */}
        <div className="text-center mb-10">
          <p
            style={{ fontFamily: "'Georgia', serif", letterSpacing: "0.15em" }}
            className="text-xs uppercase text-gray-400 mb-2"
          >
            Marco de análisis
          </p>
          <h1
            style={{ fontFamily: "'Georgia', serif" }}
            className="text-2xl font-normal text-gray-800 mb-1"
          >
            Niveles de Análisis del Comportamiento
          </h1>
          <p className="text-sm text-gray-500">
            Tinbergen · Marr · Killeen — haz clic en cada nivel
          </p>
        </div>

        {/* Pyramid */}
        <div className="flex flex-col items-center gap-1 mb-8">
          {levels.map((level) => (
            <button
              key={level.id}
              onClick={() => setActive(active === level.id ? null : level.id)}
              className={`
                ${level.width} ${level.height}
                flex flex-col items-center justify-center
                rounded-sm transition-all duration-300 cursor-pointer
                border border-transparent
                ${active === level.id ? "opacity-100 scale-100 shadow-lg" : "opacity-80 hover:opacity-95"}
              `}
              style={{
                backgroundColor:
                  active === level.id ? level.color : level.color + "CC",
                borderColor: active === level.id ? level.accent : "transparent",
              }}
            >
              <span
                style={{ color: level.accent, letterSpacing: "0.05em" }}
                className="text-xs uppercase font-normal mb-0.5"
              >
                {level.sublabel}
              </span>
              <span className="text-white text-base font-normal">
                {level.label}
              </span>
            </button>
          ))}
        </div>

        {/* Detail panel */}
        <div
          className="transition-all duration-300 overflow-hidden"
          style={{ minHeight: active ? "160px" : "0px" }}
        >
          {active && (() => {
            const level = levels.find((l) => l.id === active);
            return (
              <div
                className="rounded p-6 border"
                style={{
                  backgroundColor: level.color + "18",
                  borderColor: level.accent + "55",
                }}
              >
                <div className="grid grid-cols-3 gap-4 mb-4">
                  <div>
                    <p
                      style={{
                        color: level.accent,
                        letterSpacing: "0.1em",
                        fontFamily: "'Georgia', serif",
                      }}
                      className="text-xs uppercase mb-1"
                    >
                      Marr
                    </p>
                    <p className="text-sm text-gray-700">{level.marr}</p>
                  </div>
                  <div>
                    <p
                      style={{
                        color: level.accent,
                        letterSpacing: "0.1em",
                        fontFamily: "'Georgia', serif",
                      }}
                      className="text-xs uppercase mb-1"
                    >
                      Tinbergen
                    </p>
                    <p className="text-sm text-gray-700">{level.tinbergen}</p>
                  </div>
                  <div>
                    <p
                      style={{
                        color: level.accent,
                        letterSpacing: "0.1em",
                        fontFamily: "'Georgia', serif",
                      }}
                      className="text-xs uppercase mb-1"
                    >
                      Killeen
                    </p>
                    <p className="text-sm text-gray-700">{level.killeen}</p>
                  </div>
                </div>
                <div
                  className="border-t pt-3"
                  style={{ borderColor: level.accent + "33" }}
                >
                  <p
                    style={{
                      color: level.accent,
                      letterSpacing: "0.1em",
                      fontFamily: "'Georgia', serif",
                    }}
                    className="text-xs uppercase mb-1"
                  >
                    Ejemplo en este libro
                  </p>
                  <p className="text-sm text-gray-600 italic">{level.example}</p>
                </div>
              </div>
            );
          })()}
        </div>

        {/* Legend */}
        <div className="mt-8 flex justify-center gap-8">
          {[
            { label: "Marco de Tinbergen", desc: "4 preguntas del comportamiento" },
            { label: "Marco de Marr", desc: "3 niveles computacionales" },
            { label: "Marco de Killeen", desc: "4 tipos de causas" },
          ].map((item) => (
            <div key={item.label} className="text-center">
              <p className="text-xs font-normal text-gray-700">{item.label}</p>
              <p className="text-xs text-gray-400">{item.desc}</p>
            </div>
          ))}
        </div>

        {/* Caption */}
        <p className="text-center text-xs text-gray-400 mt-8 leading-relaxed max-w-lg mx-auto">
          <strong className="text-gray-500">Figura 1.1.</strong> Los tres marcos para los niveles de análisis del comportamiento describen el mismo espacio de preguntas con vocabularios distintos. Los niveles no compiten: cada uno responde una pregunta diferente sobre el mismo fenómeno. Adaptado de Dayan y Abbott (2001).
        </p>
      </div>
    </div>
  );
}
