const fs = require('fs');

let md = JSON.parse(fs.readFileSync('metadata.json', 'utf8'));
md.name = "Quantum Ai open source";
md.description = "A Quantum AI Open Source initiative for conceptual visualization, analyzing, simulating, and generating probabilistic permutations leveraging swarm-driven artificial intelligence.";
fs.writeFileSync('metadata.json', JSON.stringify(md, null, 2));

let pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'));
pkg.name = "quantum-ai-open-source";
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
