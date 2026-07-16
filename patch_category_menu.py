import sys

with open('src/App.tsx', 'r') as f:
    lines = f.readlines()

new_content = """      {/* CATEGORY MENU */}
      <div className="flex flex-col items-center justify-center border-b border-cyan-500/10 px-4 py-3 bg-slate-950/60 w-full relative z-40">
        <label className="text-[10px] text-cyan-500 font-mono font-bold tracking-widest uppercase mb-1.5">
          Select Operations Module
        </label>
        <div className="relative w-full max-w-sm">
          <select 
            value={activeCategory}
            onChange={(e) => setActiveCategory(e.target.value as any)}
            className="w-full appearance-none bg-slate-950 border border-cyan-500/50 rounded-lg px-4 py-2.5 text-xs sm:text-sm font-mono text-cyan-300 font-bold tracking-wider uppercase focus:outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400/50 cursor-pointer shadow-[0_0_15px_rgba(6,182,212,0.15)] text-center text-center-last"
          >
            {[
              { id: 'simple', label: '⚡ SIMPLE PREDICTIONS' },
              { id: 'swarms', label: '🧬 AGENT SWARMS' },
              { id: 'engines', label: 'QUANTUM ENGINES' },
              { id: 'analytics', label: 'PATTERN ANALYTICS' },
              { id: 'string3d', label: '🌌 STRING WIREFRAME 3D' },
              { id: 'qvm', label: '⚛️ QUANTUM VM' },
              { id: 'hyper4d', label: '🌀 4D HYPER WAVE COLLAPSE' },
              { id: 'summary', label: 'INSIGHTS & SUMMARY' },
              { id: 'data', label: 'HISTORICAL DATA' },
              { id: 'willow', label: 'W.I.L.L.O.W. HUB' },
              { id: 'agent_research', label: '🧠 CONSCIOUS AGENT' },
              { id: 'winnings', label: '🏆 WINNINGS & SUCCESS' },
              { id: 'blog_forum', label: '💬 COMMUNITY & BLOG' },
              { id: 'dashy_view', label: '📊 BET DASHBOARD' },
              { id: 'dashy', label: '🎛️ DASHBOARD BUILDER' }
            ].map(cat => (
              <option key={cat.id} value={cat.id} className="bg-slate-900 text-slate-300">
                {cat.label}
              </option>
            ))}
          </select>
          <div className="absolute inset-y-0 right-4 flex items-center pointer-events-none">
            <Sliders className="w-4 h-4 text-cyan-500" />
          </div>
        </div>
      </div>\n"""

with open('src/App.tsx', 'w') as f:
    f.writelines(lines[:4303])
    f.write(new_content)
    f.writelines(lines[4339:])

