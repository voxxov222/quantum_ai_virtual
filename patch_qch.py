import sys

with open('src/components/QuantumCoreHub.tsx', 'r') as f:
    content = f.read()

# Add new commands to buildCommandIndex
old_index = """    { cmd: "whoami", hint: "show the active agent" },
  ];
  return [...priority, ...cmds];
}"""
new_index = """    { cmd: "whoami", hint: "show the active agent" },
    { cmd: "system.status", hint: "view core metrics" },
    { cmd: "agent.list", hint: "list active agents" },
    { cmd: "node.list", hint: "list nodes" },
    { cmd: "quantum.scan", hint: "scan local spacetime" }
  ];
  return [...priority, ...cmds];
}"""
content = content.replace(old_index, new_index)

# Update state variables
old_state = """  const [buildBusy, setBuildBusy] = useState(false);
  const [buildOutput, setBuildOutput] = useState("");"""
new_state = """  const [buildBusy, setBuildBusy] = useState(false);
  const [buildOutput, setBuildOutput] = useState("");
  const [previewArtifact, setPreviewArtifact] = useState<string | null>(null);"""
content = content.replace(old_state, new_state)

# Update runCommand
old_run = """        if (data.code) {
          setBuildOutput(data.code);
          addLog("sys", "Build completed successfully.");
        } else if (data.error) {"""
new_run = """        if (data.code) {
          setBuildOutput(data.code);
          setPreviewArtifact(data.code);
          addLog("sys", "Build completed successfully. Artifact preview injected.");
        } else if (data.error) {"""
content = content.replace(old_run, new_run)

# Add handling for the new commands
old_cmd = """    } else if (cmd === "whoami") {
      addLog("out", activeAgent ? `ACTIVE AGENT: ${activeAgent.name} [${activeAgent.trait}]` : "No active agent selected.");
    } else if (cmd.startsWith("build ")) {"""
new_cmd = """    } else if (cmd === "whoami") {
      addLog("out", activeAgent ? `ACTIVE AGENT: ${activeAgent.name} [${activeAgent.trait}]` : "No active agent selected.");
    } else if (cmd === "system.status") {
      addLog("sys", `CORE STATUS: ONLINE\\nAGENTS ACTIVE: ${agents.length}\\nNODES CONNECTED: ${nodes.length}\\nMEMORY SYNC: ENABLED`);
    } else if (cmd === "agent.list") {
      addLog("out", agents.length ? agents.map(a => `- ${a.name} [${a.trait}]`).join("\\n") : "No agents forged.");
    } else if (cmd === "node.list") {
      addLog("out", nodes.length ? nodes.map(n => `- ${n.id} (${n.label})`).join("\\n") : "No nodes active.");
    } else if (cmd === "quantum.scan") {
      addLog("sys", "Scanning local spacetime...");
      setTimeout(() => addLog("out", "Quantum coherence at 98.4%. No anomalies detected."), 1500);
    } else if (cmd.startsWith("build ")) {"""
content = content.replace(old_cmd, new_cmd)

# Add Preview Panel UI
old_render = """      <div className="flex-1 flex flex-col gap-4">
        {/* Node Builder */}
        <div className="flex-1 min-h-[300px]">"""
new_render = """      <div className="flex-1 flex flex-col gap-4">
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
        <div className="flex-1 min-h-[300px]">"""
content = content.replace(old_render, new_render)


with open('src/components/QuantumCoreHub.tsx', 'w') as f:
    f.write(content)
