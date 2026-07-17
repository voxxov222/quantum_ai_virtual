import sys

with open('server.ts', 'r') as f:
    content = f.read()

target = """        {
          id: 'dwave-ocean-sdk',
          name: 'D-Wave Ocean SDK',
          description: 'A suite of open-source Python tools on the D-Wave system for solving NP-hard optimization topologies natively.',
          url: 'https://github.com/dwavesystems/dwave-ocean-sdk.git',
          type: 'Quantum Annealing'
        }"""
replacement = """        {
          id: 'dwave-ocean-sdk',
          name: 'D-Wave Ocean SDK',
          description: 'A suite of open-source Python tools on the D-Wave system for solving NP-hard optimization topologies natively.',
          url: 'https://github.com/dwavesystems/dwave-ocean-sdk.git',
          type: 'Quantum Annealing'
        },
        {
          id: 'Cirq',
          name: 'Google Cirq',
          description: 'A Python software library for writing, manipulating, and optimizing quantum circuits and running them against quantum computers and simulators.',
          url: 'https://github.com/quantumlib/Cirq.git',
          type: 'Circuit Construction'
        }"""

if target in content:
    content = content.replace(target, replacement)

with open('server.ts', 'w') as f:
    f.write(content)
