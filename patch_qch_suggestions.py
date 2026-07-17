import sys

with open('src/components/QuantumCoreHub.tsx', 'r') as f:
    content = f.read()

target_priority = """  const priority = [
    { cmd: "build", hint: "build <description> — generate real code via your Gemini backend" },
    { cmd: "agent.create", hint: "open the agent forge" },
    { cmd: "node.add", hint: "drop a new module node onto the graph" },
    { cmd: "view.hologram", hint: "toggle the 3D hologram module view" },
    { cmd: "help", hint: "list everything the hub understands" },
    { cmd: "clear", hint: "clear the terminal buffer" },
    { cmd: "whoami", hint: "show the active agent" },
    { cmd: "system.status", hint: "view core metrics" },
    { cmd: "agent.list", hint: "list active agents" },
    { cmd: "node.list", hint: "list nodes" },
    { cmd: "quantum.scan", hint: "scan local spacetime" }
  ];"""

replacement_priority = """  const priority = [
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
  ];"""

content = content.replace(target_priority, replacement_priority)

target_slice = """  const suggestions = useMemo(() => {
    if (!input.trim()) return COMMAND_INDEX.slice(0, 8);
    const q = input.toLowerCase();
    return COMMAND_INDEX.filter((c) => c.cmd.includes(q)).slice(0, 8);
  }, [input]);"""

replacement_slice = """  const suggestions = useMemo(() => {
    if (!input.trim()) return COMMAND_INDEX.slice(0, 20);
    const q = input.toLowerCase();
    return COMMAND_INDEX.filter((c) => c.cmd.includes(q)).slice(0, 20);
  }, [input]);"""

content = content.replace(target_slice, replacement_slice)

target_css = """        {showSug && suggestions.length > 0 && (
          <div className="absolute bottom-full left-3 right-3 mb-1 rounded-lg border overflow-hidden z-10" style={{ borderColor: "#1e293b", background: "#0b1120" }}>"""

replacement_css = """        {showSug && suggestions.length > 0 && (
          <div className="absolute bottom-full left-3 right-3 mb-1 rounded-lg border overflow-y-auto z-10 custom-scrollbar max-h-[300px]" style={{ borderColor: "#1e293b", background: "#0b1120" }}>"""

content = content.replace(target_css, replacement_css)

with open('src/components/QuantumCoreHub.tsx', 'w') as f:
    f.write(content)
