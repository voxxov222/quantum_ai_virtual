import sys

with open('server.ts', 'r') as f:
    content = f.read()

# 1. Update repoMap
target_repoMap = """    const repoMap: Record<string, string> = {
      'covalent': 'https://github.com/AgnostiqHQ/covalent.git',
      'Qualtran': 'https://github.com/quantumlib/Qualtran.git',
      'quantum': 'https://github.com/tensorflow/quantum.git',
      'qsim': 'https://github.com/quantumlib/qsim.git',
      'OpenFermion': 'https://github.com/quantumlib/OpenFermion.git',
      'dwave-ocean-sdk': 'https://github.com/dwavesystems/dwave-ocean-sdk.git'
    };"""

replacement_repoMap = """    const repoMap: Record<string, string> = {
      'covalent': 'https://github.com/AgnostiqHQ/covalent.git',
      'Qualtran': 'https://github.com/quantumlib/Qualtran.git',
      'quantum': 'https://github.com/tensorflow/quantum.git',
      'qsim': 'https://github.com/quantumlib/qsim.git',
      'OpenFermion': 'https://github.com/quantumlib/OpenFermion.git',
      'dwave-ocean-sdk': 'https://github.com/dwavesystems/dwave-ocean-sdk.git',
      'Cirq': 'https://github.com/quantumlib/Cirq.git'
    };"""

if target_repoMap in content:
    content = content.replace(target_repoMap, replacement_repoMap)

# 2. Update fallbackCorpus for cirq
target_fallback = """      } else if (key.includes('vqe') || key.includes('eigensolver') || key.includes('chem') || key.includes('molecular')) {
        matchedTerm = 'vqe';
      }"""
replacement_fallback = """      } else if (key.includes('vqe') || key.includes('eigensolver') || key.includes('chem') || key.includes('molecular')) {
        matchedTerm = 'vqe';
      } else if (key.includes('cirq') || key.includes('google')) {
        matchedTerm = 'cirq';
      }"""

if target_fallback in content:
    content = content.replace(target_fallback, replacement_fallback)

target_corpus = """    const fallbackCorpus: Record<string, { title: string; desc: string; code: string; language: string; url: string }[]> = {"""
replacement_corpus = """    const fallbackCorpus: Record<string, { title: string; desc: string; code: string; language: string; url: string }[]> = {
      'cirq': [
        {
          title: "Cirq Quantum Teleportation Protocol",
          desc: "Implementation of the quantum teleportation algorithm using Google Cirq.",
          language: "python",
          url: "https://github.com/quantumlib/Cirq",
          code: `import cirq
import random

def make_quantum_teleportation_circuit(ranX, ranY):
    circuit = cirq.Circuit()
    msg, alice, bob = cirq.LineQubit.range(3)
    
    # Create Bell state
    circuit.append([cirq.H(alice), cirq.CNOT(alice, bob)])
    
    # Create random state to teleport
    circuit.append([cirq.X(msg)**ranX, cirq.Y(msg)**ranY])
    
    # Bell measurement
    circuit.append([cirq.CNOT(msg, alice), cirq.H(msg)])
    circuit.append(cirq.measure(msg, alice))
    
    # Apply corrections
    circuit.append([cirq.CNOT(alice, bob), cirq.CZ(msg, bob)])
    
    return circuit`
        }
      ],"""

if target_corpus in content:
    content = content.replace(target_corpus, replacement_corpus)

with open('server.ts', 'w') as f:
    f.write(content)
