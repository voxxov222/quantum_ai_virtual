import sys

with open('server.ts', 'r') as f:
    content = f.read()

target = """  app.post('/api/hub/build', async (req, res) => {
    try {
      const { prompt } = req.body;
      if (!prompt) return res.status(400).json({ error: 'Prompt is required' });

      const completion = await ai.models.generateContent({
        model: 'gemini-2.5-pro',
        contents: [
          { role: 'user', parts: [{ text: `You are the Neural Nexus Central Intelligence Core. The user wants to build a new system/app: ${prompt}. Return ONLY valid code or JSON representing the generated artifact. Do not include markdown formatting like \`\`\`json or \`\`\`typescript. Just return the raw code.` }] }
        ]
      });

      const responseText = completion.text || "";
      res.json({ code: responseText.trim() });
    } catch (error: any) {
      console.error("Error in /api/hub/build:", error);
      res.status(500).json({ error: error.message });
    }
  });"""

replacement = """  app.post('/api/hub/build', async (req, res) => {
    try {
      const { prompt } = req.body;
      if (!prompt) return res.status(400).json({ error: 'Prompt is required' });

      const completion = await ai.models.generateContent({
        model: 'gemini-2.5-pro',
        contents: [
          { role: 'user', parts: [{ text: `You are the Neural Nexus Central Intelligence Core. The user wants to build a new system/app widget: ${prompt}. 
Write a complete, self-contained HTML file with embedded CSS and JS (using CDN for Tailwind CSS if needed) that implements this interactive widget. 
The widget should be dark-themed, futuristic, and match a cyan/magenta/slate aesthetic. 
Return ONLY the raw HTML string, no markdown formatting like \`\`\`html, no explanations.` }] }
        ]
      });

      let responseText = completion.text || "";
      responseText = responseText.replace(/```html/g, "").replace(/```/g, "").trim();
      res.json({ code: responseText });
    } catch (error: any) {
      console.error("Error in /api/hub/build:", error);
      res.status(500).json({ error: error.message });
    }
  });"""

if target in content:
    content = content.replace(target, replacement)
    print("Patched server.ts")
else:
    print("Target not found in server.ts")

with open('server.ts', 'w') as f:
    f.write(content)
