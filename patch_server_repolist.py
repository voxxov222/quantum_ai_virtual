import sys

with open('server.ts', 'r') as f:
    content = f.read()

target = """    const repoMap: Record<string, string> = {
      'covalent': 'https://github.com/AgnostiqHQ/covalent.git',
      'Qualtran': 'https://github.com/quantumlib/Qualtran.git',
      'quantum': 'https://github.com/tensorflow/quantum.git',
      'qsim': 'https://github.com/quantumlib/qsim.git',
      'OpenFermion': 'https://github.com/quantumlib/OpenFermion.git',
      'dwave-ocean-sdk': 'https://github.com/dwavesystems/dwave-ocean-sdk.git'
    };"""

replacement = """    const repoMap: Record<string, string> = {
      'covalent': 'https://github.com/AgnostiqHQ/covalent.git',
      'Qualtran': 'https://github.com/quantumlib/Qualtran.git',
      'quantum': 'https://github.com/tensorflow/quantum.git',
      'qsim': 'https://github.com/quantumlib/qsim.git',
      'OpenFermion': 'https://github.com/quantumlib/OpenFermion.git',
      'dwave-ocean-sdk': 'https://github.com/dwavesystems/dwave-ocean-sdk.git',
      'Cirq': 'https://github.com/quantumlib/Cirq.git'
    };"""

if target in content:
    content = content.replace(target, replacement)
    print("Patched repoMap")
else:
    print("Target repoMap not found")

target_terminal = """      const completion = await ai.models.generateContent({
        model: 'gemini-2.5-pro',
        contents: [
          { role: 'user', parts: [{ text: `The user typed this command into a quantum terminal: "${command}". 
You are a highly advanced quantum OS. Write a plausible, matrix-style tech output for this command.
Limit it to 2-3 short sentences. No markdown formatting.` }] }
        ]
      });"""

replacement_terminal = """      const completion = await ai.models.generateContent({
        model: 'gemini-2.5-pro',
        contents: [
          { role: 'user', parts: [{ text: `The user typed this command into a quantum terminal: "${command}". 
You are a highly advanced quantum OS with access to tools like Cirq, Qsim, D-Wave, and Qualtran. Write a plausible, matrix-style tech output for this command, acknowledging any library tools.
Limit it to 2-4 short sentences. No markdown formatting.` }] }
        ]
      });"""

if target_terminal in content:
    content = content.replace(target_terminal, replacement_terminal)
    print("Patched terminal prompt")
else:
    print("Target terminal prompt not found")

with open('server.ts', 'w') as f:
    f.write(content)
