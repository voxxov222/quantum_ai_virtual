import sys

with open('server.ts', 'r') as f:
    content = f.read()

target = """        {
          id: 'dwave-ocean-sdk',
          name: 'D-Wave Ocean SDK (D-Wave)',
          description: 'A suite of open-source Python tools for solving hard problems with quantum annealing, Ising models, and QUBO mappings.',
          url: 'https://github.com/dwavesystems/dwave-ocean-sdk.git',
          type: 'Annealing & Optimization'
        }
      ];"""

replacement = """        {
          id: 'dwave-ocean-sdk',
          name: 'D-Wave Ocean SDK (D-Wave)',
          description: 'A suite of open-source Python tools for solving hard problems with quantum annealing, Ising models, and QUBO mappings.',
          url: 'https://github.com/dwavesystems/dwave-ocean-sdk.git',
          type: 'Annealing & Optimization'
        },
        {
          id: 'Cirq',
          name: 'Google Cirq',
          description: 'A Python software library for writing, manipulating, and optimizing quantum circuits and running them against quantum computers and simulators.',
          url: 'https://github.com/quantumlib/Cirq.git',
          type: 'Circuit Construction'
        },
        {
          id: 'deepquantum',
          name: 'DeepQuantum (TuringQ)',
          description: 'A tensor-network-based quantum machine learning framework by TuringQ.',
          url: 'https://github.com/TuringQ/deepquantum.git',
          type: 'Quantum ML Framework'
        }
      ];"""

if target in content:
    content = content.replace(target, replacement)
else:
    print("Could not find target")

with open('server.ts', 'w') as f:
    f.write(content)
