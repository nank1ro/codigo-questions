#!/usr/bin/env python3
"""
Fix trailing space in after-asserts section for JavaScript files.
"""
import os

FILES = [
    '/Users/ale/github/codigo-questions/es/javascript/arithmeticOperators/17.md',
    '/Users/ale/github/codigo-questions/es/javascript/booleans/12.md',
    '/Users/ale/github/codigo-questions/es/javascript/booleans/13.md',
    '/Users/ale/github/codigo-questions/es/javascript/whileLoops/38.md',
]

for file_path in FILES:
    with open(file_path, 'r') as f:
        content = f.read()

    # Fix the after-asserts section to have trailing space
    content = content.replace(
        '```javascript\n// DO NOT EDIT FROM HERE\nconsole.log',
        '```javascript\n// DO NOT EDIT FROM HERE \nconsole.log'
    )

    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Fixed {file_path}")

print("Done!")
