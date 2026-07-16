import sys

with open('README.md', 'r') as f:
    content = f.read()

content = content.replace("https://bet49-etvmigp2u-enterupteds-projects-e79e57e0.vercel.app/", "https://quantumai-flax.vercel.app/")

target_init = """# 2. Synchronize Quantum Dependencies
npm install

# 3. Boot the Hub
npm run dev
```"""

replacement_init = """# 2. Synchronize Quantum Dependencies
npm install

# 3. Start up with coding agent
npx plugins add vercel/vercel-plugin

# 4. Boot the Hub
npm run dev
```"""

content = content.replace(target_init, replacement_init)

with open('README.md', 'w') as f:
    f.write(content)
