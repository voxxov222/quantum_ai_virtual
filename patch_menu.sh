#!/bin/bash
cat << 'INNER_EOF' > src/components/InteractiveOrbitalMenu.tsx.patch
--- src/components/InteractiveOrbitalMenu.tsx	2026-07-15 17:50:00.000000000 -0700
+++ src/components/InteractiveOrbitalMenu.tsx	2026-07-15 17:50:00.000000000 -0700
@@ -139,134 +139,129 @@
 
       {/* Cybernetic Floating Strategy Moons Array */}
-      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-1 gap-3 items-stretch relative min-h-[190px]">
+      <div className="flex flex-col gap-4 relative min-h-[190px]">
         
         {/* Connection node layout details */}
         <div className="absolute inset-0 bg-[radial-gradient(#1e293b_1px,transparent_1px)] [background-size:16px_16px] opacity-15 pointer-events-none" />
 
+        {/* Dropdown for selecting strategy centered */}
+        <div className="flex flex-col items-center justify-center pt-2 relative z-10">
+          <label className="text-[10px] text-cyan-500 font-mono font-bold tracking-widest uppercase mb-2">
+            Select Active Tool Set
+          </label>
+          <div className="relative w-full max-w-sm">
+            <select 
+              value={selectedStrategy}
+              onChange={(e) => onSelectStrategy(e.target.value)}
+              className="w-full appearance-none bg-slate-950 border border-cyan-500/50 rounded-xl px-4 py-3 text-sm font-mono text-cyan-300 font-bold focus:outline-none focus:border-cyan-400 focus:ring-1 focus:ring-cyan-400/50 cursor-pointer shadow-[0_0_15px_rgba(6,182,212,0.15)] text-center text-center-last"
+            >
+              {activeChannelStrategies.map((strat) => (
+                <option key={strat.id} value={strat.id} className="bg-slate-900 text-slate-300">
+                  {strat.name}
+                </option>
+              ))}
+            </select>
+            <div className="absolute inset-y-0 right-4 flex items-center pointer-events-none">
+              <Sliders className="w-4 h-4 text-cyan-500" />
+            </div>
+          </div>
+        </div>
+
         <AnimatePresence mode="popLayout">
-          {activeChannelStrategies.map((strat, index) => {
-            const isSelected = selectedStrategy === strat.id;
+          {activeChannelStrategies.filter(s => s.id === selectedStrategy).map((strat, index) => {
             const stats = strategyHitRate(strat.id);
             const catInfo = getStrategyCategory(strat.id);
-            const isHovered = hoveredStratId === strat.id;
 
-            // Generate slow-moving floating offset offsets based on index and angle
-            const floatX = Math.sin(rotationAngle + (index * 1.5)) * 4;
-            const floatY = Math.cos(rotationAngle + (index * 1.5)) * 4;
-
-            let borderTheme = isSelected ? catInfo.borderClass : 'border-slate-900/80 hover:border-slate-800';
-            let bgTheme = isSelected 
-              ? `${catInfo.glowClass} border-opacity-70 bg-black/60` 
-              : 'bg-slate-950/40 hover:bg-slate-900/60 text-slate-300';
+            let borderTheme = catInfo.borderClass;
+            let bgTheme = `${catInfo.glowClass} border-opacity-70 bg-black/60`;
              return (
-              <motion.button
+              <motion.div
                 key={strat.id}
                 initial={{ opacity: 0, x: -16 }}
                 animate={{ 
                   opacity: 1, 
                   x: 0, 
-                  y: isSelected ? floatY : 0,
-                  boxShadow: isSelected ? '0 0 15px rgba(6,182,212,0.05)' : '' 
+                  y: 0,
+                  boxShadow: '0 0 15px rgba(6,182,212,0.05)'
                 }}
                 exit={{ opacity: 0, x: 20 }}
                 transition={{ duration: 0.35, ease: 'easeOut' }}
-                onClick={() => onSelectStrategy(strat.id)}
-                onMouseEnter={() => setHoveredStratId(strat.id)}
-                onMouseLeave={() => setHoveredStratId(null)}
-                className={`p-3.5 rounded-xl border text-left flex flex-col justify-between gap-2.5 transition-all duration-300 relative group cursor-pointer select-none overflow-hidden ${borderTheme} ${bgTheme}`}
+                className={`p-3.5 rounded-xl border text-left flex flex-col justify-between gap-2.5 transition-all duration-300 relative group select-none overflow-hidden ${borderTheme} ${bgTheme}`}
               >
                 {/* Horizontal scan line sweep for actively selected strategy card */}
-                {isSelected && (
-                  <div className="absolute inset-0 bg-[linear-gradient(to_bottom,transparent_90%,rgba(6,182,212,0.1)_100%)] bg-[size:100%_20px] pointer-events-none animate-[scanline_2.5s_linear_infinite]" />
-                )}
+                <div className="absolute inset-0 bg-[linear-gradient(to_bottom,transparent_90%,rgba(6,182,212,0.1)_100%)] bg-[size:100%_20px] pointer-events-none animate-[scanline_2.5s_linear_infinite]" />
 
                 <div className="flex justify-between items-start w-full gap-2">
                   <div className="flex items-center gap-2 shrink truncate">
-                    <div className={`w-1.5 h-1.5 rounded-full ${isSelected ? 'animate-ping' : ''} ${
+                    <div className={`w-1.5 h-1.5 rounded-full animate-ping ${
                       catInfo.color === 'cyan' ? 'bg-cyan-400' :
                       catInfo.color === 'purple' ? 'bg-purple-400' :
                       catInfo.color === 'magenta' ? 'bg-pink-400' : 'bg-amber-400'
                     }`} />
                     <span className="text-[10.5px] font-mono leading-tight font-extrabold tracking-wide uppercase truncate">
                       {strat.name.replace(/^[0-9.]+\s*/, '')}
                     </span>
                   </div>
                   
                   {stats && stats.hitRate > 0 && (
                     <span className={`text-[8px] font-mono font-black border px-1.5 py-0.5 rounded uppercase tracking-wider shrink-0 ${
                       stats.hitRate >= 45 
                         ? 'bg-emerald-950/60 border-emerald-500/30 text-emerald-300' 
                         : 'bg-cyan-950/60 border-cyan-500/30 text-cyan-300'
                     }`}>
                       {stats.hitRate}% HIT
                     </span>
                   )}
                   {strategyWinningStreaks[strat.id] !== undefined && strategyWinningStreaks[strat.id] > 0 && (
                     <span className="text-[8px] font-mono font-black border px-1.5 py-0.5 rounded uppercase tracking-wider shrink-0 bg-amber-950/60 border-amber-500/30 text-amber-300">
                       {strategyWinningStreaks[strat.id]} STREAK
                     </span>
                   )}
                 </div>
 
                 <p className="text-[10px] text-slate-400 leading-relaxed font-sans line-clamp-2 select-none">
                   {strat.desc}
                 </p>
 
                 {/* Consecutive Wins / Match History Bar Chart */}
                 <div className="flex flex-col gap-1.5 mt-1 border-t border-slate-900/40 pt-1.5 select-none">
                   <span className="text-[7px] font-mono text-slate-500 uppercase tracking-widest block font-bold leading-none">
                     STREAK HISTORY (LAST 5 RECORDS):
                   </span>
                   <div className="flex items-end gap-2 h-7 mt-0.5">
                     {(strategyStreakHistories?.[strat.id] || [0, 0, 0, 0, 0]).map((matches, i) => {
                       const percent = (matches / 6) * 100;
                       const isWin = matches >= 3;
                       const barColor = isWin 
                         ? 'bg-gradient-to-t from-emerald-600 to-emerald-400 shadow-[0_0_6px_rgba(16,185,129,0.35)]' 
                         : 'bg-slate-800/80 hover:bg-slate-750';
                       
                       return (
                         <div key={i} className="flex-1 flex flex-col items-center gap-0.5 group/bar relative">
                           <div 
                             className={`w-full rounded-sm min-h-[3px] transition-all duration-500 ${barColor}`}
                             style={{ height: `${Math.max(3, percent * 0.22)}px` }}
                           />
                           <span className="text-[6.5px] font-mono text-slate-500 leading-none group-hover/bar:text-cyan-400 transition-colors">
                             {matches}
                           </span>
                           
                           <div className="absolute bottom-6 scale-0 group-hover/bar:scale-100 transition-transform origin-bottom bg-slate-950 border border-slate-850 text-[6.5px] font-mono text-cyan-450 px-1.5 py-0.5 rounded shadow-xl whitespace-nowrap z-20 pointer-events-none">
                             {isWin ? 'WIN' : 'LOSS'}: {matches} Matches
                           </div>
                         </div>
                       );
                     })}
                   </div>
                 </div>
 
                 {/* Micro metrics tracking dashboard info */}
                 <div className="flex justify-between items-center text-[8px] font-mono border-t border-slate-900/60 pt-2 select-none">
                   <span className="text-slate-500 uppercase tracking-widest leading-none">
                     ENGINE VECTOR KEY: <span className="text-slate-400 font-extrabold">{strat.id.toUpperCase()}</span>
                   </span>
                   <span className="text-slate-500 uppercase leading-none">
                     Status: <span className="text-emerald-400 font-bold">READY</span>
                   </span>
                 </div>
 
                 {/* Orbit beam lock visual decorator */}
-                {isSelected && (
-                  <div className={`absolute top-0 right-0 w-[4px] h-full ${
-                    catInfo.color === 'cyan' ? 'bg-cyan-400' :
-                    catInfo.color === 'purple' ? 'bg-purple-400' :
-                    catInfo.color === 'magenta' ? 'bg-pink-400' : 'bg-amber-400'
-                  }`} />
-                )}
-              </motion.button>
+                <div className={`absolute top-0 right-0 w-[4px] h-full ${
+                  catInfo.color === 'cyan' ? 'bg-cyan-400' :
+                  catInfo.color === 'purple' ? 'bg-purple-400' :
+                  catInfo.color === 'magenta' ? 'bg-pink-400' : 'bg-amber-400'
+                }`} />
+              </motion.div>
             );
           })}
INNER_EOF
patch -p0 < src/components/InteractiveOrbitalMenu.tsx.patch
