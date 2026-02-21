#!/usr/bin/env python3
"""
Fix JavaScript variables exercises in Spanish.
"""

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_js_file(en_path, es_path):
    """Copy English file and translate instructions only."""
    en_content = read_file(en_path)
    if not en_content:
        return False

    lines = en_content.split('\n')
    es_lines = []
    current_section = None
    description_lines = []
    instruction_lines = []

    for i, line in enumerate(lines):
        # Keep frontmatter as-is
        if line.startswith('---') or line.startswith('language:') or line.startswith('exerciseType:'):
            es_lines.append(line)
        elif line.startswith('# --description--'):
            current_section = 'description'
            es_lines.append(line)
            es_lines.append('')
        elif line.startswith('# --instructions--'):
            current_section = 'instructions'
            # Add translated description
            if description_lines:
                full_desc = ' '.join(description_lines)
                # For now, keep description in English as it contains code examples
                es_lines.append(full_desc)
                es_lines.append('')
            es_lines.append(line)
            es_lines.append('')
        elif line.startswith('# --') or line.startswith('```'):
            if current_section == 'instructions' and instruction_lines:
                # Translate instruction
                full_instr = ' '.join(instruction_lines)
                es_lines.append(translate_instruction(full_instr))
                es_lines.append('')
                instruction_lines = []
            current_section = 'code'
            es_lines.append(line)
        elif current_section == 'description':
            description_lines.append(line)
        elif current_section == 'instructions':
            instruction_lines.append(line)
        else:
            es_lines.append(line)

    # Handle instructions at end
    if instruction_lines:
        for i, line in enumerate(es_lines):
            if line.startswith('# --before-seed--'):
                full_instr = ' '.join(instruction_lines)
                es_lines.insert(i, translate_instruction(full_instr))
                es_lines.insert(i, '')
                break

    write_file(es_path, '\n'.join(es_lines))
    return True

def translate_instruction(text):
    """Translate instruction to Spanish."""
    translations = {
        "Assign to the variable `y` the value `2`.": "Asigna a la variable `y` el valor `2`.",
        "Create a new variable named `y` and assign it the value of the variable `x`.": "Crea una nueva variable llamada `y` y asígnale el valor de la variable `x`.",
        "Update the value of the variable `x` with the number `10`.": "Actualiza el valor de la variable `x` con el número `10`.",
        "Update the value of the variable `x` with the number `3`.": "Actualiza el valor de la variable `x` con el número `3`.",
        "Declare a variable named `month` with the value of `\"june\"` (lowercased).": 'Declara una variable llamada `month` con el valor de `"june"` (en minúsculas).',
        "Set `isLogged` to value `true`": "Establece `isLogged` al valor `true`",
        "Set `amount` to the value `\"50 dollars\"`": 'Establece `amount` al valor `"50 dollars"`',
    }
    if text in translations:
        return translations[text]
    return text

# Files to fix
FILES = [
    ('/Users/ale/github/codigo-questions/es/javascript/variables/1.md',
     '/Users/ale/github/codigo-questions/en/javascript/variables/1.md'),
    ('/Users/ale/github/codigo-questions/es/javascript/variables/2.md',
     '/Users/ale/github/codigo-questions/en/javascript/variables/2.md'),
    ('/Users/ale/github/codigo-questions/es/javascript/variables/3.md',
     '/Users/ale/github/codigo-questions/en/javascript/variables/3.md'),
    ('/Users/ale/github/codigo-questions/es/javascript/variables/4.md',
     '/Users/ale/github/codigo-questions/en/javascript/variables/4.md'),
    ('/Users/ale/github/codigo-questions/es/javascript/variables/5.md',
     '/Users/ale/github/codigo-questions/en/javascript/variables/5.md'),
    ('/Users/ale/github/codigo-questions/es/javascript/variables/9.md',
     '/Users/ale/github/codigo-questions/en/javascript/variables/9.md'),
    ('/Users/ale/github/codigo-questions/es/javascript/variables/15.md',
     '/Users/ale/github/codigo-questions/en/javascript/variables/15.md'),
]

def main():
    fixed = 0
    for es_path, en_path in FILES:
        try:
            if fix_js_file(en_path, es_path):
                print(f"✓ Fixed {es_path}")
                fixed += 1
        except Exception as e:
            print(f"✗ Error {es_path}: {e}")
    print(f"\nFixed: {fixed}")

if __name__ == '__main__':
    main()
