import sys

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add to type Category
type_target = "type Category = 'simple' | 'swarms' | 'engines' | 'analytics' | 'string3d' | 'qvm' | 'hyper4d' | 'summary' | 'data' | 'willow' | 'agent_research' | 'winnings' | 'blog_forum' | 'dashy' | 'dashy_view';"
type_replacement = "type Category = 'simple' | 'swarms' | 'engines' | 'analytics' | 'string3d' | 'qvm' | 'hyper4d' | 'summary' | 'data' | 'willow' | 'agent_research' | 'winnings' | 'blog_forum' | 'dashy' | 'dashy_view' | 'quantum_core';"
if type_target in content:
    content = content.replace(type_target, type_replacement)

with open('src/App.tsx', 'w') as f:
    f.write(content)
