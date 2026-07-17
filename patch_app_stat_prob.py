import sys

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add to type Category
target_type = " | 'dashy_view' | 'quantum_core';"
replacement_type = " | 'dashy_view' | 'quantum_core' | 'stat_prob';"
if target_type in content:
    content = content.replace(target_type, replacement_type)

# Add to widget options
target_widget = "{ id: 'summary', label: 'Insights & Summary' },"
replacement_widget = "{ id: 'summary', label: 'Insights & Summary' },\n                        { id: 'stat_prob', label: 'Probability Distribution' },"
if target_widget in content:
    content = content.replace(target_widget, replacement_widget)

# Add to dropdown options (line 4340 area)
target_dropdown = "{ id: 'summary', label: 'INSIGHTS & SUMMARY' },"
replacement_dropdown = "{ id: 'summary', label: 'INSIGHTS & SUMMARY' },\n              { id: 'stat_prob', label: 'PROBABILITY DISTRIBUTION' },"
if target_dropdown in content:
    content = content.replace(target_dropdown, replacement_dropdown)

# Import StatisticalProbabilityChart
target_import = "import Markdown from 'react-markdown';"
replacement_import = "import StatisticalProbabilityChart from './components/StatisticalProbabilityChart';\nimport Markdown from 'react-markdown';"
if target_import in content:
    content = content.replace(target_import, replacement_import)

# Render widget
target_render = """        {/* W.I.L.L.O.W. HUB */}
        {isWidgetVisible('willow') && ("""
replacement_render = """        {/* STATISTICAL PROBABILITY CHART */}
        {isWidgetVisible('stat_prob') && (
          <section className="flex flex-col gap-6 w-full" style={{ order: getWidgetOrder('stat_prob') }}>
            <StatisticalProbabilityChart draws={draws} />
          </section>
        )}

        {/* W.I.L.L.O.W. HUB */}
        {isWidgetVisible('willow') && ("""
if target_render in content:
    content = content.replace(target_render, replacement_render)

with open('src/App.tsx', 'w') as f:
    f.write(content)
