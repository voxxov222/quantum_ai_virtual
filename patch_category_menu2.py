import sys

with open('src/App.tsx', 'r') as f:
    content = f.read()

target = """        </div>
      </div>

      {/* CORE DISPLAY FLOOR */}"""

replacement = """        </div>
      </div>
      </header>

      {/* CORE DISPLAY FLOOR */}"""

if target in content:
    content = content.replace(target, replacement)
    print("Fixed!")
else:
    print("Target not found.")

with open('src/App.tsx', 'w') as f:
    f.write(content)
