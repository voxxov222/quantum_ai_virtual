/* eslint-disable react/prop-types, @typescript-eslint/no-explicit-any, @typescript-eslint/no-unused-vars */
import React, { useState, useEffect, useRef, useCallback, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion"; // Note: might need to be 'motion/react' depending on install
import {
  Terminal, GitBranch, Users, LayoutGrid, Plug, Settings, Send, Sparkles,
  Cpu, Plus, X, Link2, Trash2, Copy, Check, Loader2, Radio, Boxes,
  ChevronRight, Zap, Brain, Activity, Move, Box as BoxIcon,
} from "lucide-react";

/* =====================================================================
   QUANTUM CORE HUB
   Drop-in command center for quantum_ai_virtual
===================================================================== */

const CYAN = "#22d3ee";
const VIOLET = "#a855f7";
const GOLD = "#f3c765";
const BG = "#020617"; // slate-950, matches --app-bg

// ---------- command index: hundreds of suggestions ----------
const CATEGORIES = [
  { key: "agent", desc: "virtual agent lifecycle" },
  { key: "node", desc: "module graph" },
  { key: "memory", desc: "persistent recall" },
  { key: "api", desc: "external endpoints" },
  { key: "widget", desc: "hub dashboard tiles" },
  { key: "system", desc: "core hub state" },
  { key: "theme", desc: "visual identity" },
  { key: "build", desc: "generate new code/apps" },
  { key: "network", desc: "webhook + connections" },
  { key: "quantum", desc: "core simulation layer" },
];
const ACTIONS = [
  "create", "list", "delete", "update", "sync", "connect", "disconnect",
  "status", "optimize", "clone", "deploy", "restart", "analyze", "export",
  "import", "rename", "clear", "test", "scan", "boost",
];
function buildCommandIndex() {
  const cmds: { cmd: string; hint: string }[] = [];
  CATEGORIES.forEach((c) => ACTIONS.forEach((a) => cmds.push({ cmd: `${c.key}.${a}`, hint: `${a} ${c.desc}` })));
  const priority = [
    { cmd: "help", hint: "list everything the hub understands" },
    { cmd: "clear", hint: "clear the terminal buffer" },
    { cmd: "whoami", hint: "show the active agent" },
    { cmd: "system.status", hint: "view core metrics" },
    { cmd: "agent.create", hint: "open the agent forge" },
    { cmd: "agent.list", hint: "list active agents" },
    { cmd: "node.add", hint: "drop a new module node onto the graph" },
    { cmd: "node.list", hint: "list nodes" },
    { cmd: "view.hologram", hint: "toggle the 3D hologram module view" },
    { cmd: "quantum.scan", hint: "scan local spacetime" },
    { cmd: "build a custom lottery prediction widget", hint: "generate real code via your Gemini backend" },
    { cmd: "build a neural network training dashboard", hint: "generate real code via your Gemini backend" },
    { cmd: "build a quantum state visualizer", hint: "generate real code via your Gemini backend" },
    { cmd: "build a real-time analytics chart", hint: "generate real code via your Gemini backend" },
    { cmd: "build a historical data grid", hint: "generate real code via your Gemini backend" },
    { cmd: "build a crypto price ticker", hint: "generate real code via your Gemini backend" },
    { cmd: "build a task manager for AI agents", hint: "generate real code via your Gemini backend" },
    { cmd: "build a 3D particle simulation", hint: "generate real code via your Gemini backend" },
    { cmd: "build a web3 portfolio tracker", hint: "generate real code via your Gemini backend" },
    { cmd: "build an interactive periodic table", hint: "generate real code via your Gemini backend" },
    { cmd: "build a markdown editor with live preview", hint: "generate real code via your Gemini backend" },
    { cmd: "build a celestial map viewer", hint: "generate real code via your Gemini backend" },
  ];
  return [...priority, ...cmds];
}
const COMMAND_INDEX = buildCommandIndex();

type LogEntry = { type: "cmd" | "out" | "error" | "sys"; text: string };
type Agent = { id: string; name: string; trait: string; color: string; memoryCount: number };
type NodeT = { id: string; type: string; label: string; color: string; x: number; y: number };
type EdgeT = { id: string; from: string; to: string };
type Connection = { id: string; name: string; url: string; method: string; status: string };

// ---------- Sentient Core ----------
function SentientCore({ state = "idle", color = CYAN }: { state?: string; color?: string }) {
  const speed = state === "thinking" ? "1.1s" : state === "speaking" ? "0.6s" : "3.4s";
  const rings = [64, 84, 104];
  return (
    <div className="relative flex items-center justify-center" style={{ width: 200, height: 200 }}>
      <svg viewBox="0 0 220 220" width="200" height="200" className="absolute inset-0">
        <defs>
          <radialGradient id="qchGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor={color} stopOpacity="0.9" />
            <stop offset="60%" stopColor={color} stopOpacity="0.25" />
            <stop offset="100%" stopColor={color} stopOpacity="0" />
          </radialGradient>
        </defs>
        <circle cx="110" cy="110" r="100" fill="url(#qchGlow)">
          <animate attributeName="r" values="94;104;94" dur={speed} repeatCount="indefinite" />
        </circle>
        {rings.map((r, i) => (
          <circle key={r} cx="110" cy="110" r={r} fill="none" stroke={i === 1 ? VIOLET : color}
            strokeOpacity="0.55" strokeWidth="1" strokeDasharray={`${2 + i * 3} ${6 + i * 2}`}>
            <animateTransform attributeName="transform" type="rotate"
              from={i % 2 === 0 ? "0 110 110" : "360 110 110"} to={i % 2 === 0 ? "360 110 110" : "0 110 110"}
              dur={`${8 + i * 4}s`} repeatCount="indefinite" />
          </circle>
        ))}
        <circle cx="110" cy="110" r="34" fill={BG} stroke={color} strokeWidth="1.5" />
        <circle cx="110" cy="110" r="20" fill={color} opacity="0.9">
          <animate attributeName="opacity" values="0.55;1;0.55" dur={speed} repeatCount="indefinite" />
        </circle>
      </svg>
    </div>
  );
}

function CopyButton({ text }: { text: string }) {
  const [copied, setCopied] = useState(false);
  return (
    <button
      onClick={() => { navigator.clipboard.writeText(text); setCopied(true); setTimeout(() => setCopied(false), 1500); }}
      className="text-[10px] flex items-center gap-1 px-2 py-0.5 rounded"
      style={{ color: copied ? "#7ef7b0" : CYAN, background: "rgba(255,255,255,0.04)" }}>
      {copied ? <Check size={11} /> : <Copy size={11} />} {copied ? "copied" : "copy"}
    </button>
  );
}

// ---------- Terminal ----------
function TerminalPanel({
  activeAgent, buildBusy, buildOutput, log, runCommand,
}: {
  activeAgent: Agent | null; buildBusy: boolean; buildOutput: string; log: LogEntry[];
  runCommand: (raw: string) => void;
}) {
  const [input, setInput] = useState("");
  const [showSug, setShowSug] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);

  const suggestions = useMemo(() => {
    if (!input.trim()) return COMMAND_INDEX.slice(0, 20);
    const q = input.toLowerCase();
    return COMMAND_INDEX.filter((c) => c.cmd.includes(q)).slice(0, 20);
  }, [input]);

  useEffect(() => { if (scrollRef.current) scrollRef.current.scrollTop = scrollRef.current.scrollHeight; }, [log, buildOutput]);

  const submit = (raw?: string) => {
    const value = (raw ?? input).trim();
    if (!value) return;
    runCommand(value);
    setInput("");
    setShowSug(false);
  };

  return (
    <div className="flex flex-col h-full rounded-xl border relative overflow-hidden" style={{ borderColor: "#1e293b", background: "rgba(2,6,23,0.75)" }}>
      <div className="crt-overlay" />
      <div className="flex items-center gap-2 px-4 py-2.5 border-b" style={{ borderColor: "#1e293b" }}>
        <Terminal size={14} style={{ color: CYAN }} />
        <span className="text-[11px] tracking-[0.2em] uppercase font-mono" style={{ color: CYAN }}>Hub Terminal</span>
        <span className="ml-auto text-[10px] font-mono" style={{ color: "#64748b" }}>
          {activeAgent ? `agent://${activeAgent.name}` : "agent://none"}
        </span>
      </div>
      <div ref={scrollRef} className="flex-1 overflow-y-auto px-4 py-3 font-mono text-[12.5px] leading-relaxed" style={{ color: "#cbd5e1" }}>
        {log.map((l, i) => (
          <div key={i} className={l.type === "cmd" ? "mb-1" : "mb-2"}>
            {l.type === "cmd" ? (
              <span><span style={{ color: GOLD }}>›</span> <span style={{ color: "#e2e8f0" }}>{l.text}</span></span>
            ) : (
              <div style={{ color: l.type === "error" ? "#ff6b81" : "#94a3b8", whiteSpace: "pre-wrap" }}>{l.text}</div>
            )}
          </div>
        ))}
        {buildBusy && (
          <div className="flex items-center gap-2" style={{ color: VIOLET }}>
            <Loader2 size={12} className="animate-spin" /> routing through the Gemini core…
          </div>
        )}
        {buildOutput && (
          <div className="mt-2 rounded-lg border overflow-hidden" style={{ borderColor: "#1e293b" }}>
            <div className="flex items-center justify-between px-3 py-1.5" style={{ background: "#0f172a" }}>
              <span className="text-[10px] tracking-widest uppercase" style={{ color: GOLD }}>Generated artifact</span>
              <CopyButton text={buildOutput} />
            </div>
            <pre className="p-3 overflow-x-auto text-[11px]" style={{ color: "#a8f0d0", maxHeight: 260 }}>{buildOutput}</pre>
          </div>
        )}
      </div>
      <div className="relative px-3 pb-3">
        {showSug && suggestions.length > 0 && (
          <div className="absolute bottom-full left-3 right-3 mb-1 rounded-lg border overflow-y-auto z-10 custom-scrollbar max-h-[300px]" style={{ borderColor: "#1e293b", background: "#0b1120" }}>
            {suggestions.map((s) => (
              <button key={s.cmd} onMouseDown={(e) => { e.preventDefault(); submit(s.cmd); }}
                className="w-full text-left px-3 py-1.5 flex items-center gap-2 hover:bg-white/5 text-[12px] font-mono">
                <span style={{ color: CYAN }}>{s.cmd}</span>
                <span style={{ color: "#64748b" }} className="truncate">— {s.hint}</span>
              </button>
            ))}
          </div>
        )}
        <div className="flex items-center gap-2 rounded-lg border px-3 py-2" style={{ borderColor: "#1e293b", background: "#0b1120" }}>
          <ChevronRight size={13} style={{ color: GOLD }} />
          <input value={input} onChange={(e) => { setInput(e.target.value); setShowSug(true); }}
            onFocus={() => setShowSug(true)}
            onKeyDown={(e) => { if (e.key === "Enter") submit(); if (e.key === "Escape") setShowSug(false); }}
            placeholder="type a command… try `help` or `build a habit tracker widget`"
            className="flex-1 bg-transparent outline-none text-[12.5px] font-mono" style={{ color: "#e2e8f0" }} />
          <button onClick={() => submit()} className="text-[11px] px-2 py-1 rounded-md" style={{ background: "rgba(34,211,238,0.1)", color: CYAN }}>
            <Send size={12} />
          </button>
        </div>
      </div>
    </div>
  );
}

// ---------- Module Graph (2D + CSS hologram 3D, zero extra deps) ----------
const NODE_TYPES = [
  { type: "input", label: "Input", color: GOLD },
  { type: "agent", label: "Agent", color: VIOLET },
  { type: "llm", label: "LLM Core", color: CYAN },
  { type: "webhook", label: "Webhook", color: "#7ef7b0" },
  { type: "output", label: "Output", color: "#ff8a65" },
];

function NodeBuilder({ nodes, setNodes, edges, setEdges, hologram, setHologram }: {
  nodes: NodeT[]; setNodes: React.Dispatch<React.SetStateAction<NodeT[]>>;
  edges: EdgeT[]; setEdges: React.Dispatch<React.SetStateAction<EdgeT[]>>;
  hologram: boolean; setHologram: (v: boolean) => void;
}) {
  const canvasRef = useRef<HTMLDivElement>(null);
  const dragRef = useRef<{ id: string; offX: number; offY: number } | null>(null);
  const [connectFrom, setConnectFrom] = useState<string | null>(null);
  const [rotY, setRotY] = useState(-18);
  const [rotX, setRotX] = useState(14);

  const addNode = (type: string) => {
    const def = NODE_TYPES.find((n) => n.type === type)!;
    const id = `${type}-${Math.random().toString(36).slice(2, 7)}`;
    setNodes((ns) => [...ns, { id, type, label: def.label, color: def.color, x: 40 + Math.random() * 260, y: 30 + Math.random() * 200 }]);
  };
  const onPointerDown = (e: React.PointerEvent, id: string) => {
    if (hologram) return;
    const rect = canvasRef.current!.getBoundingClientRect();
    const node = nodes.find((n) => n.id === id)!;
    dragRef.current = { id, offX: e.clientX - rect.left - node.x, offY: e.clientY - rect.top - node.y };
  };
  const onPointerMove = (e: React.PointerEvent) => {
    if (hologram) {
      setRotY((r) => r + e.movementX * (e.buttons === 1 ? 0.4 : 0));
      setRotX((r) => Math.max(-40, Math.min(40, r - e.movementY * (e.buttons === 1 ? 0.4 : 0))));
      return;
    }
    if (!dragRef.current) return;
    const rect = canvasRef.current!.getBoundingClientRect();
    const { id, offX, offY } = dragRef.current;
    const x = Math.max(0, Math.min(rect.width - 120, e.clientX - rect.left - offX));
    const y = Math.max(0, Math.min(rect.height - 60, e.clientY - rect.top - offY));
    setNodes((ns) => ns.map((n) => (n.id === id ? { ...n, x, y } : n)));
  };
  const onPointerUp = () => { dragRef.current = null; };
  const clickNode = (id: string) => {
    if (!connectFrom) { setConnectFrom(id); return; }
    if (connectFrom === id) { setConnectFrom(null); return; }
    setEdges((es) => [...es, { from: connectFrom, to: id, id: `${connectFrom}-${id}-${Math.random().toString(36).slice(2, 5)}` }]);
    setConnectFrom(null);
  };
  const removeNode = (id: string) => {
    setNodes((ns) => ns.filter((n) => n.id !== id));
    setEdges((es) => es.filter((e) => e.from !== id && e.to !== id));
  };
  const center = (n: NodeT) => ({ x: n.x + 60, y: n.y + 26 });

  return (
    <div className="flex flex-col h-full rounded-xl border" style={{ borderColor: "#1e293b", background: "rgba(2,6,23,0.75)" }}>
      <div className="flex items-center gap-2 px-4 py-2.5 border-b flex-wrap" style={{ borderColor: "#1e293b" }}>
        <GitBranch size={14} style={{ color: VIOLET }} />
        <span className="text-[11px] tracking-[0.2em] uppercase font-mono" style={{ color: VIOLET }}>Module Graph</span>
        <button onClick={() => setHologram(!hologram)}
          className="text-[10px] px-2 py-1 rounded-md border flex items-center gap-1"
          style={{ borderColor: GOLD, color: GOLD }}>
          <BoxIcon size={10} /> {hologram ? "flat view" : "hologram view"}
        </button>
        <div className="ml-auto flex gap-1.5 flex-wrap">
          {NODE_TYPES.map((n) => (
            <button key={n.type} onClick={() => addNode(n.type)}
              className="text-[10px] px-2 py-1 rounded-md border flex items-center gap-1" style={{ borderColor: n.color, color: n.color }}>
              <Plus size={10} /> {n.label}
            </button>
          ))}
        </div>
      </div>
      <div className="px-4 pt-2 text-[10px] font-mono" style={{ color: "#64748b" }}>
        {hologram ? "drag to rotate the hologram — nodes float on a lattice of Z-depth" :
          connectFrom ? "click a target node to connect it — click empty space to cancel" : "drag nodes • click two nodes in sequence to link them"}
      </div>
      <div
        ref={canvasRef}
        onPointerMove={onPointerMove}
        onPointerUp={onPointerUp}
        onClick={() => setConnectFrom(null)}
        className="relative flex-1 m-3 rounded-lg overflow-hidden"
        style={{
          background: "radial-gradient(circle at 1px 1px, rgba(255,255,255,0.06) 1px, transparent 0) 0 0/18px 18px, #04060f",
          perspective: hologram ? 900 : undefined,
          cursor: hologram ? "grab" : undefined,
        }}
      >
        <div style={hologram ? {
          transformStyle: "preserve-3d",
          transform: `rotateX(${rotX}deg) rotateY(${rotY}deg)`,
          transition: "transform 0.05s linear",
          width: "100%", height: "100%", position: "relative",
        } : { width: "100%", height: "100%", position: "relative" }}>
          <svg className="absolute inset-0 w-full h-full pointer-events-none" style={{ overflow: "visible" }}>
            {edges.map((e) => {
              const a = nodes.find((n) => n.id === e.from);
              const b = nodes.find((n) => n.id === e.to);
              if (!a || !b) return null;
              const p1 = center(a), p2 = center(b);
              return <line key={e.id} x1={p1.x} y1={p1.y} x2={p2.x} y2={p2.y} stroke={CYAN} strokeOpacity="0.5" strokeWidth="1.5" />;
            })}
          </svg>
          {nodes.length === 0 && (
            <div className="absolute inset-0 flex items-center justify-center text-[11px] font-mono" style={{ color: "#334155" }}>
              drop a module above to start the graph
            </div>
          )}
          {nodes.map((n, i) => {
            const depth = hologram ? ((i % 5) - 2) * 40 : 0;
            return (
              <div key={n.id} onPointerDown={(e) => onPointerDown(e, n.id)} onClick={(e) => { e.stopPropagation(); clickNode(n.id); }}
                className="absolute select-none rounded-lg px-3 py-2 text-[11px] font-mono cursor-grab active:cursor-grabbing group"
                style={{
                  left: n.x, top: n.y, width: 120,
                  transform: hologram ? `translateZ(${depth}px)` : undefined,
                  border: `1px solid ${n.color}`,
                  background: connectFrom === n.id ? `${n.color}22` : "#0b1120",
                  color: n.color, boxShadow: `0 0 16px ${n.color}44`,
                }}>
                <div className="flex items-center justify-between">
                  <span className="font-medium">{n.label}</span>
                  <button onClick={(e) => { e.stopPropagation(); removeNode(n.id); }} className="opacity-0 group-hover:opacity-100"><X size={11} /></button>
                </div>
                <div className="text-[9px] mt-0.5" style={{ color: "#64748b" }}>{n.id}</div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

// ---------- Agent Forge ----------
function AgentPanel({ agents, setActiveId, activeId, onCreate, onDelete }: {
  agents: Agent[]; activeId: string | null; setActiveId: (id: string) => void;
  onCreate: (name: string, trait: string, color: string) => void; onDelete: (id: string) => void;
}) {
  const [form, setForm] = useState({ name: "", trait: "curious", color: CYAN });
  const traits = ["curious", "stoic", "playful", "precise", "rebellious", "warm"];
  return (
    <div className="flex flex-col h-full rounded-xl border p-4" style={{ borderColor: "#1e293b", background: "rgba(2,6,23,0.75)" }}>
      <div className="flex items-center gap-2 mb-3">
        <Users size={14} style={{ color: GOLD }} />
        <span className="text-[11px] tracking-[0.2em] uppercase font-mono" style={{ color: GOLD }}>Agent Forge</span>
        <span className="ml-auto text-[9px] font-mono" style={{ color: "#334155" }}>synced to memory</span>
      </div>
      <div className="space-y-2 mb-4">
        <input value={form.name} onChange={(e) => setForm((f) => ({ ...f, name: e.target.value }))} placeholder="agent name"
          className="w-full bg-transparent border rounded-md px-2.5 py-1.5 text-[12px] outline-none font-mono" style={{ borderColor: "#1e293b", color: "#e2e8f0" }} />
        <div className="flex gap-1.5 flex-wrap">
          {traits.map((t) => (
            <button key={t} onClick={() => setForm((f) => ({ ...f, trait: t }))} className="text-[10px] px-2 py-1 rounded-full border font-mono"
              style={{ borderColor: form.trait === t ? CYAN : "#1e293b", color: form.trait === t ? CYAN : "#94a3b8" }}>{t}</button>
          ))}
        </div>
        <div className="flex gap-1.5">
          {[CYAN, VIOLET, GOLD, "#7ef7b0", "#ff8a65"].map((c) => (
            <button key={c} onClick={() => setForm((f) => ({ ...f, color: c }))} className="w-5 h-5 rounded-full border-2"
              style={{ background: c, borderColor: form.color === c ? "#fff" : "transparent" }} />
          ))}
        </div>
        <button onClick={() => { if (form.name.trim()) { onCreate(form.name.trim(), form.trait, form.color); setForm({ name: "", trait: "curious", color: CYAN }); } }}
          className="w-full text-[11px] py-1.5 rounded-md flex items-center justify-center gap-1.5 font-mono"
          style={{ background: "rgba(168,85,247,0.15)", color: VIOLET }}>
          <Sparkles size={12} /> forge agent
        </button>
      </div>
      <div className="flex-1 overflow-y-auto space-y-2">
        {agents.map((a) => (
          <div key={a.id} onClick={() => setActiveId(a.id)}
            className="flex items-center gap-3 p-2 rounded-lg cursor-pointer transition-all border"
            style={{
              borderColor: activeId === a.id ? a.color : "#1e293b",
              background: activeId === a.id ? `${a.color}15` : "transparent"
            }}>
            <div className="w-2.5 h-2.5 rounded-full" style={{ background: a.color, boxShadow: `0 0 8px ${a.color}` }} />
            <div className="flex-1 overflow-hidden">
              <div className="text-[12px] text-white font-mono truncate">{a.name}</div>
              <div className="text-[9px] font-mono" style={{ color: "#94a3b8" }}>{a.trait} • {a.memoryCount} memories</div>
            </div>
            <button onClick={(e) => { e.stopPropagation(); onDelete(a.id); }} className="p-1 hover:text-red-400 text-[#475569]">
              <Trash2 size={12} />
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

// ---------- Main Quantum Core Hub Component ----------
export default function QuantumCoreHub() {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [activeAgentId, setActiveAgentId] = useState<string | null>(null);
  
  const [nodes, setNodes] = useState<NodeT[]>([]);
  const [edges, setEdges] = useState<EdgeT[]>([]);
  const [hologramMode, setHologramMode] = useState(false);

  const [log, setLog] = useState<LogEntry[]>([
    { type: "sys", text: "QUANTUM CORE HUB v1.0 ONLINE." },
    { type: "sys", text: "Connecting to swarm telemetry..." },
    { type: "sys", text: "Enter `help` to list commands." }
  ]);
  const [buildBusy, setBuildBusy] = useState(false);
  const [buildOutput, setBuildOutput] = useState("");
  const [previewArtifact, setPreviewArtifact] = useState<string | null>(null);

  const activeAgent = useMemo(() => agents.find(a => a.id === activeAgentId) || null, [agents, activeAgentId]);

  const addLog = (type: LogEntry["type"], text: string) => {
    setLog(prev => [...prev, { type, text }]);
  };

  const runCommand = async (raw: string) => {
    addLog("cmd", raw);
    const cmd = raw.trim().toLowerCase();
    
    if (cmd === "help") {
      addLog("out", "AVAILABLE COMMANDS:\n" + COMMAND_INDEX.map(c => `  ${c.cmd.padEnd(20)} ${c.hint}`).join("\n"));
    } else if (cmd === "clear") {
      setLog([]);
    } else if (cmd === "whoami") {
      addLog("out", activeAgent ? `ACTIVE AGENT: ${activeAgent.name} [${activeAgent.trait}]` : "No active agent selected.");
    } else if (cmd === "system.status") {
      addLog("sys", `CORE STATUS: ONLINE\nAGENTS ACTIVE: ${agents.length}\nNODES CONNECTED: ${nodes.length}\nMEMORY SYNC: ENABLED`);
    } else if (cmd === "agent.list") {
      addLog("out", agents.length ? agents.map(a => `- ${a.name} [${a.trait}]`).join("\n") : "No agents forged.");
    } else if (cmd === "node.list") {
      addLog("out", nodes.length ? nodes.map(n => `- ${n.id} (${n.label})`).join("\n") : "No nodes active.");
    } else if (cmd === "quantum.scan") {
      addLog("sys", "Scanning local spacetime...");
      setTimeout(() => addLog("out", "Quantum coherence at 98.4%. No anomalies detected."), 1500);
    } else if (cmd.startsWith("build ")) {
      const desc = cmd.replace("build ", "").trim();
      if (!desc) {
        addLog("error", "Error: build requires a description. Usage: build <description>");
        return;
      }
      setBuildBusy(true);
      setBuildOutput("");
      addLog("out", `Initiating swarm to build: ${desc}...`);
      
      try {
        const res = await fetch("/api/hub/build", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ prompt: desc })
        });
        const data = await res.json();
        if (data.code) {
          setBuildOutput(data.code);
          setPreviewArtifact(data.code);
          addLog("sys", "Build completed successfully. Artifact preview injected.");
        } else if (data.error) {
          addLog("error", `Build failed: ${data.error}`);
        } else {
          setBuildOutput(JSON.stringify(data, null, 2));
          addLog("sys", "Build response received.");
        }
      } catch (err: any) {
        addLog("error", `Exception during build: ${err.message}`);
      } finally {
        setBuildBusy(false);
      }
    } else if (cmd === "agent.create") {
      addLog("out", "Use the Agent Forge panel to forge a new agent.");
    } else if (cmd === "view.hologram") {
      setHologramMode(prev => {
        addLog("sys", `Hologram mode ${!prev ? "ENABLED" : "DISABLED"}`);
        return !prev;
      });
    } else {
      addLog("error", `Command not found: ${cmd}. Type 'help' for available commands.`);
    }
  };

  const createAgent = (name: string, trait: string, color: string) => {
    const newAgent: Agent = {
      id: `agt-${Math.random().toString(36).slice(2,9)}`,
      name,
      trait,
      color,
      memoryCount: 0
    };
    setAgents(prev => [...prev, newAgent]);
    setActiveAgentId(newAgent.id);
    addLog("sys", `Agent forged: ${name} [${trait}]`);
  };

  const deleteAgent = (id: string) => {
    const agt = agents.find(a => a.id === id);
    setAgents(prev => prev.filter(a => a.id !== id));
    if (activeAgentId === id) setActiveAgentId(null);
    if (agt) {
      addLog("sys", `Agent deleted: ${agt.name}`);
    }
  };

  return (
    <div className="w-full h-full flex flex-col md:flex-row gap-4 p-4 text-slate-200">
      <div className="flex-1 flex flex-col gap-4">
        {/* Core State Viewer */}
        <div className="rounded-xl border p-4 flex flex-col items-center justify-center relative overflow-hidden h-64" style={{ borderColor: "#1e293b", background: "rgba(2,6,23,0.75)" }}>
           <h3 className="absolute top-4 left-4 text-[11px] uppercase tracking-widest font-mono flex items-center gap-2" style={{ color: CYAN }}>
             <Cpu size={14} /> Sentient Core
           </h3>
           <SentientCore state={buildBusy ? "thinking" : "idle"} color={activeAgent ? activeAgent.color : CYAN} />
           
           {activeAgent && (
             <div className="absolute bottom-4 right-4 text-[10px] font-mono text-right" style={{ color: activeAgent.color }}>
               Active Sync: {activeAgent.name}<br/>
               Trait: {activeAgent.trait.toUpperCase()}
             </div>
           )}
        </div>
        
        {/* Terminal */}
        <div className="flex-1 min-h-[300px]">
           <TerminalPanel 
             activeAgent={activeAgent} 
             buildBusy={buildBusy} 
             buildOutput={buildOutput} 
             log={log} 
             runCommand={runCommand} 
           />
        </div>
      </div>
      
      <div className="flex-1 flex flex-col gap-4">
        {/* Live Preview Panel (if active) */}
        {previewArtifact && (
          <div className="flex-1 min-h-[300px] rounded-xl border relative overflow-hidden" style={{ borderColor: "#1e293b", background: "rgba(2,6,23,0.75)" }}>
            <div className="flex items-center justify-between gap-2 px-4 py-2.5 border-b" style={{ borderColor: "#1e293b" }}>
              <div className="flex items-center gap-2">
                <BoxIcon size={14} style={{ color: "#7ef7b0" }} />
                <span className="text-[11px] tracking-[0.2em] uppercase font-mono" style={{ color: "#7ef7b0" }}>Artifact Live Preview</span>
              </div>
              <button onClick={() => setPreviewArtifact(null)} className="text-[#64748b] hover:text-white">
                <X size={14} />
              </button>
            </div>
            <div className="w-full h-[calc(100%-41px)] relative bg-black/50">
              <iframe 
                srcDoc={previewArtifact} 
                className="w-full h-full border-none"
                sandbox="allow-scripts"
              />
            </div>
          </div>
        )}
        {/* Node Builder */}
        <div className="flex-1 min-h-[300px]">
          <NodeBuilder 
            nodes={nodes} setNodes={setNodes}
            edges={edges} setEdges={setEdges}
            hologram={hologramMode} setHologram={setHologramMode}
          />
        </div>

        {/* Agent Panel */}
        <div className="h-64 shrink-0">
          <AgentPanel 
            agents={agents}
            activeId={activeAgentId}
            setActiveId={setActiveAgentId}
            onCreate={createAgent}
            onDelete={deleteAgent}
          />
        </div>
      </div>
    </div>
  );
}
