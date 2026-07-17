import sys

with open('server.ts', 'r') as f:
    content = f.read()

endpoint_code = """  app.post('/api/hub/build', async (req, res) => {
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
  });

  app.post('/api/gemini/chat', async (req, res) => {"""

content = content.replace("  app.post('/api/gemini/chat', async (req, res) => {", endpoint_code)

with open('server.ts', 'w') as f:
    f.write(content)
