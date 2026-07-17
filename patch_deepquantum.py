import sys

with open('server.ts', 'r') as f:
    content = f.read()

# 1. Update libraryDefinitions
target_lib = """        {
          id: 'Cirq',
          name: 'Google Cirq',
          description: 'A Python software library for writing, manipulating, and optimizing quantum circuits and running them against quantum computers and simulators.',
          url: 'https://github.com/quantumlib/Cirq.git',
          type: 'Circuit Construction'
        }
      ];"""

replacement_lib = """        {
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

if target_lib in content:
    content = content.replace(target_lib, replacement_lib)

# 2. Update repoMap
target_repoMap = """      'dwave-ocean-sdk': 'https://github.com/dwavesystems/dwave-ocean-sdk.git',
      'Cirq': 'https://github.com/quantumlib/Cirq.git'
    };"""

replacement_repoMap = """      'dwave-ocean-sdk': 'https://github.com/dwavesystems/dwave-ocean-sdk.git',
      'Cirq': 'https://github.com/quantumlib/Cirq.git',
      'deepquantum': 'https://github.com/TuringQ/deepquantum.git'
    };"""

if target_repoMap in content:
    content = content.replace(target_repoMap, replacement_repoMap)

# 3. Update fallback corpus matching logic
target_fallback = """      } else if (key.includes('cirq') || key.includes('google')) {
        matchedTerm = 'cirq';
      }"""
replacement_fallback = """      } else if (key.includes('cirq') || key.includes('google')) {
        matchedTerm = 'cirq';
      } else if (key.includes('deepquantum') || key.includes('turing') || key.includes('dq')) {
        matchedTerm = 'deepquantum';
      }"""

if target_fallback in content:
    content = content.replace(target_fallback, replacement_fallback)

# 4. Add to fallbackCorpus
target_corpus = """    const fallbackCorpus: Record<string, { title: string; desc: string; code: string; language: string; url: string }[]> = {"""
replacement_corpus = """    const fallbackCorpus: Record<string, { title: string; desc: string; code: string; language: string; url: string }[]> = {
      'deepquantum': [
        {
          title: "DeepQuantum Quantum Neural Network",
          desc: "Implementation of a basic Quantum Neural Network using TuringQ's DeepQuantum.",
          language: "python",
          url: "https://github.com/TuringQ/deepquantum.git",
          code: `import deepquantum as dq
import deepquantum.nn as dqnn
import torch
import torch.nn as nn

class QNN(nn.Module):
    def __init__(self, n_qubits):
        super().__init__()
        self.n_qubits = n_qubits
        # Quantum encoder
        self.encoder = dqnn.Encoder(n_qubits, basis='Rx')
        # Parameterized Quantum Circuit (Ansatz)
        self.ansatz = dqnn.Ansatz(n_qubits, layers=2)
        # Observable measurement
        self.measure = dqnn.MeasureAll(n_qubits)
        
    def forward(self, x):
        # Encode classical data to quantum state
        q_state = self.encoder(x)
        # Evolve state
        q_state = self.ansatz(q_state)
        # Measure
        exp_vals = self.measure(q_state)
        return exp_vals`
        }
      ],"""

if target_corpus in content:
    content = content.replace(target_corpus, replacement_corpus)

with open('server.ts', 'w') as f:
    f.write(content)
