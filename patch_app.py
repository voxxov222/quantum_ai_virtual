import sys

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add import
import_target = "import Markdown from 'react-markdown';"
import_replacement = "import QuantumCoreHub from './components/QuantumCoreHub';\nimport Markdown from 'react-markdown';"
if import_target in content:
    content = content.replace(import_target, import_replacement)

# Add to dropdown menu
dropdown_target = "{ id: 'dashy', label: '🎛️ DASHBOARD BUILDER' }"
dropdown_replacement = "{ id: 'dashy', label: '🎛️ DASHBOARD BUILDER' },\n              { id: 'quantum_core', label: '🧠 QUANTUM CORE HUB' }"
if dropdown_target in content:
    content = content.replace(dropdown_target, dropdown_replacement)

# Add to core display floor
display_target = "{/* 🎛️ DASHBOARD BUILDER SECTION */}"
display_replacement = """{/* 🧠 QUANTUM CORE HUB SECTION */}
        {activeCategory === 'quantum_core' && (
          <section className="flex flex-col gap-6 w-full h-[800px]">
            <QuantumCoreHub />
          </section>
        )}

        {/* 🎛️ DASHBOARD BUILDER SECTION */}"""
if display_target in content:
    content = content.replace(display_target, display_replacement)

with open('src/App.tsx', 'w') as f:
    f.write(content)
