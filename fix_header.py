with open('src/App.tsx', 'r') as f:
    content = f.read()

target = '        </div>\n      </div>\n      {/* CORE DISPLAY FLOOR */}'
replacement = '        </div>\n      </div>\n      </header>\n      {/* CORE DISPLAY FLOOR */}'

if target in content:
    content = content.replace(target, replacement)
    print("Fixed!")
else:
    print("Not found.")

with open('src/App.tsx', 'w') as f:
    f.write(content)
