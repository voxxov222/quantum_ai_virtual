import sys

with open('src/App.tsx', 'r') as f:
    content = f.read()

target = "const [activeCategory, setActiveCategory] = useState<'engines' | 'analytics' | 'summary' | 'data' | 'willow' | 'simple' | 'swarms' | 'string3d' | 'qvm' | 'dashy' | 'dashy_view' | 'winnings' | 'hyper4d' | 'agent_research' | 'blog_forum'>('engines');"
replacement = "const [activeCategory, setActiveCategory] = useState<'engines' | 'analytics' | 'summary' | 'data' | 'willow' | 'simple' | 'swarms' | 'string3d' | 'qvm' | 'dashy' | 'dashy_view' | 'winnings' | 'hyper4d' | 'agent_research' | 'blog_forum' | 'quantum_core'>('engines');"
if target in content:
    content = content.replace(target, replacement)
else:
    print("Target not found")

with open('src/App.tsx', 'w') as f:
    f.write(content)
