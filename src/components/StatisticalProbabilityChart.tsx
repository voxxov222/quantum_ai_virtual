import React, { useMemo } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';
import { Activity } from 'lucide-react';

interface StatisticalProbabilityChartProps {
  draws: any[];
}

export default function StatisticalProbabilityChart({ draws }: StatisticalProbabilityChartProps) {
  const data = useMemo(() => {
    const counts: Record<number, number> = {};
    for (let i = 1; i <= 49; i++) {
      counts[i] = 0;
    }

    const recentDraws = draws.slice(0, 100);
    recentDraws.forEach(draw => {
      draw.numbers.forEach((num: number) => {
        if (counts[num] !== undefined) {
          counts[num]++;
        }
      });
    });

    return Object.entries(counts).map(([num, count]) => ({
      number: parseInt(num),
      frequency: count,
      probability: (count / recentDraws.length) * 100
    }));
  }, [draws]);

  return (
    <div className="bg-slate-950/80 border border-cyan-500/20 rounded-xl p-4 flex flex-col gap-4 w-full">
      <div className="flex items-center gap-2 mb-2">
        <Activity className="w-5 h-5 text-cyan-400" />
        <h3 className="text-sm font-mono font-bold text-cyan-400 tracking-wider">STATISTICAL PROBABILITY DISTRIBUTION</h3>
      </div>
      <div className="h-[300px] w-full">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
            <XAxis dataKey="number" stroke="#64748b" tick={{ fill: '#64748b', fontSize: 10 }} tickLine={false} axisLine={false} />
            <YAxis stroke="#64748b" tick={{ fill: '#64748b', fontSize: 10 }} tickLine={false} axisLine={false} />
            <Tooltip
              contentStyle={{ backgroundColor: '#020617', borderColor: '#06b6d4', borderRadius: '8px' }}
              itemStyle={{ color: '#22d3ee' }}
              labelStyle={{ color: '#94a3b8', marginBottom: '4px' }}
              formatter={(value: number) => [`${value} hits (${((value / Math.min(draws.length, 100)) * 100).toFixed(1)}%)`, 'Frequency']}
              labelFormatter={(label) => `Number ${label}`}
            />
            <Bar dataKey="frequency" radius={[4, 4, 0, 0]}>
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.frequency > (Math.min(draws.length, 100) * 0.15) ? '#a855f7' : '#06b6d4'} />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div className="text-[10px] font-mono text-slate-500 text-center">
        * Displaying draw frequency over the most recent {Math.min(draws.length, 100)} draw cycles. Purple bars indicate high-frequency hot zones (&gt;15% occurrence rate).
      </div>
    </div>
  );
}
