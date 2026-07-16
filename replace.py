import sys

with open("src/components/InteractiveOrbitalMenu.tsx", "r") as f:
    content = f.read()

target = """      {/* Cybernetic Floating Strategy Moons Array */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-1 gap-3 items-stretch relative min-h-[190px]">
        
        {/* Connection node layout details */}
        <div className="absolute inset-0 bg-[radial-gradient(#1e293b_1px,transparent_1px)] [background-size:16px_16px] opacity-15 pointer-events-none" />"""

replacement = """      {/* Cybernetic Floating Strategy Moons Array */}
      <div className="flex flex-col gap-4 relative min-h-[190px]">
        
        {/* Connection node layout details */}
        <div className="absolute inset-0 bg-[radial-gradient(#1e293b_1px,transparent_1px)] [background-size:16px_16px] opacity-15 pointer-events-none" />

        {/* Dropdown for selecting strategy centered */}
        <div className="flex flex-col items-center justify-center pt-2 relative z-10">
          <label className="text-[10px] text-cyan-500 font-mono font-bold tracking-widest uppercase mb-2">
            Select Active Tool Set
          </label>
          <div className="relative w-full max-w-sm">
            <select 
              value={selectedStrategy}
              onChange={(e) => onSelectStrategy(e.target.value)}
              className="w-full appearance-none bg-slate-950 border border-cyan-500/50 rounded-xl px-4 py-3 text-sm font-mono text-cyan-300 font-bold focus:outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400/50 cursor-pointer shadow-[0_0_15px_rgba(6,182,212,0.15)] text-center text-center-last"
            >
              {activeChannelStrategies.map((strat) => (
                <option key={strat.id} value={strat.id} className="bg-slate-900 text-slate-300">
                  {strat.name}
                </option>
              ))}
            </select>
          </div>
        </div>"""

if target in content:
    content = content.replace(target, replacement)
    
target2 = """        <AnimatePresence mode="popLayout">
          {activeChannelStrategies.map((strat, index) => {
            const isSelected = selectedStrategy === strat.id;
            const stats = strategyHitRate(strat.id);
            const catInfo = getStrategyCategory(strat.id);
            const isHovered = hoveredStratId === strat.id;

            // Generate slow-moving floating offset offsets based on index and angle
            const floatX = Math.sin(rotationAngle + (index * 1.5)) * 4;
            const floatY = Math.cos(rotationAngle + (index * 1.5)) * 4;

            let borderTheme = isSelected ? catInfo.borderClass : 'border-slate-900/80 hover:border-slate-800';
            let bgTheme = isSelected 
              ? `${catInfo.glowClass} border-opacity-70 bg-black/60` 
              : 'bg-slate-950/40 hover:bg-slate-900/60 text-slate-300';

            return (
              <motion.button
                key={strat.id}
                initial={{ opacity: 0, x: -16 }}
                animate={{ 
                  opacity: 1, 
                  x: 0, 
                  y: isSelected ? floatY : 0,
                  boxShadow: isSelected ? '0 0 15px rgba(6,182,212,0.05)' : '' 
                }}
                exit={{ opacity: 0, x: 20 }}
                transition={{ duration: 0.35, ease: 'easeOut' }}
                onClick={() => onSelectStrategy(strat.id)}
                onMouseEnter={() => setHoveredStratId(strat.id)}
                onMouseLeave={() => setHoveredStratId(null)}
                className={`p-3.5 rounded-xl border text-left flex flex-col justify-between gap-2.5 transition-all duration-300 relative group cursor-pointer select-none overflow-hidden ${borderTheme} ${bgTheme}`}
              >"""
              
replacement2 = """        <AnimatePresence mode="popLayout">
          {activeChannelStrategies.filter(s => s.id === selectedStrategy).map((strat, index) => {
            const isSelected = true;
            const stats = strategyHitRate(strat.id);
            const catInfo = getStrategyCategory(strat.id);

            let borderTheme = catInfo.borderClass;
            let bgTheme = `${catInfo.glowClass} border-opacity-70 bg-black/60`;

            return (
              <motion.div
                key={strat.id}
                initial={{ opacity: 0, x: -16 }}
                animate={{ 
                  opacity: 1, 
                  x: 0, 
                  y: 0,
                  boxShadow: '0 0 15px rgba(6,182,212,0.05)'
                }}
                exit={{ opacity: 0, x: 20 }}
                transition={{ duration: 0.35, ease: 'easeOut' }}
                className={`p-3.5 rounded-xl border text-left flex flex-col justify-between gap-2.5 transition-all duration-300 relative group select-none overflow-hidden ${borderTheme} ${bgTheme}`}
              >"""

if target2 in content:
    content = content.replace(target2, replacement2)
    
target3 = """                {/* Orbit beam lock visual decorator */}
                {isSelected && (
                  <div className={`absolute top-0 right-0 w-[4px] h-full ${
                    catInfo.color === 'cyan' ? 'bg-cyan-400' :
                    catInfo.color === 'purple' ? 'bg-purple-400' :
                    catInfo.color === 'magenta' ? 'bg-pink-400' : 'bg-amber-400'
                  }`} />
                )}
              </motion.button>"""

replacement3 = """                {/* Orbit beam lock visual decorator */}
                <div className={`absolute top-0 right-0 w-[4px] h-full ${
                  catInfo.color === 'cyan' ? 'bg-cyan-400' :
                  catInfo.color === 'purple' ? 'bg-purple-400' :
                  catInfo.color === 'magenta' ? 'bg-pink-400' : 'bg-amber-400'
                }`} />
              </motion.div>"""

if target3 in content:
    content = content.replace(target3, replacement3)
    
with open("src/components/InteractiveOrbitalMenu.tsx", "w") as f:
    f.write(content)
