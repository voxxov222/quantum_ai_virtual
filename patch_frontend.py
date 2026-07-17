import sys

with open('src/App.tsx', 'r') as f:
    content = f.read()

target = """        } else if (cmd.name === 'calculateProbability' && cmd.args?.numbers) {
          const numbers = cmd.args.numbers;
          setProposedNumbers(numbers); // Automatically set numbers for ease of view
          const detail = cmd.result ? `Sum: ${cmd.result.sum} (${cmd.result.oddEvenRatio}) | ${cmd.result.consecutiveNumbers} Consecutives` : '';
          commandInfo = {
            name: 'calculateProbability',
            info: `Evaluated ${numbers.join(', ')}. ${detail}`
          };
          addToast(
            'PROBABILITY EVALUATED',
            `Calculated sum ${cmd.result?.sum || ''} is ${cmd.result?.sumStatus || 'verified'}.`,
            'info'
          );
        }"""

replacement = """        } else if (cmd.name === 'calculateProbability' && cmd.args?.numbers) {
          const numbers = cmd.args.numbers;
          setProposedNumbers(numbers); // Automatically set numbers for ease of view
          const detail = cmd.result ? `Sum: ${cmd.result.sum} (${cmd.result.oddEvenRatio}) | ${cmd.result.consecutiveNumbers} Consecutives` : '';
          commandInfo = {
            name: 'calculateProbability',
            info: `Evaluated ${numbers.join(', ')}. ${detail}`
          };
          addToast(
            'PROBABILITY EVALUATED',
            `Calculated sum ${cmd.result?.sum || ''} is ${cmd.result?.sumStatus || 'verified'}.`,
            'info'
          );
        } else if (cmd.name === 'developSystemApp' && cmd.args?.appName) {
          commandInfo = {
            name: 'developSystemApp',
            info: `INTEGRATING SYSTEM: ${cmd.args.appName.toUpperCase()}`
          };
          addToast(
            'SYSTEM BUILD INITIATED',
            `Compiling ${cmd.args.appName}... Source code integration successful.`,
            'success'
          );
          setWillowPopup({
            isOpen: true,
            title: `SYSTEM UPGRADE: ${cmd.args.appName.toUpperCase()}`,
            content: `<h3>Architecture Overview</h3><p>${cmd.args.codeSummary}</p><br/><ul><li>[OK] System Checks Passed</li><li>[OK] Neural Nexus Synced</li><li>[OK] Source Code Injected</li></ul>`,
            imagePrompt: `A futuristic holographic blueprint of a software architecture named ${cmd.args.appName} glowing in cyan and magenta on a dark background.`
          });
        }"""

if target in content:
    content = content.replace(target, replacement)
else:
    print("TARGET NOT FOUND")
    sys.exit(1)

with open('src/App.tsx', 'w') as f:
    f.write(content)
