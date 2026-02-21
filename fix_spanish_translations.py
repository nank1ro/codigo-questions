#!/usr/bin/env python3
"""
Fix Spanish translations by comparing with English versions.
Translates instructions and answers while preserving code keywords.
"""

import os
import re
from pathlib import Path

# Swift keywords that should NOT be translated
SWIFT_KEYWORDS = {
    'if', 'else', 'for', 'while', 'switch', 'case', 'default', 'break', 'continue',
    'return', 'var', 'let', 'func', 'class', 'struct', 'enum', 'protocol', 'init',
    'import', 'true', 'false', 'nil', 'self', 'super', 'override', 'extension',
    'static', 'private', 'internal', 'public', 'fileprivate', 'open', 'lazy',
    'mutating', 'weak', 'unowned', 'strong', 'copy', 'typealias', 'associatedtype',
    'inout', 'throw', 'throws', 'rethrows', 'try', 'catch', 'guard', 'defer',
    'repeat', 'where', 'as', 'is', 'in', 'get', 'set', 'willSet', 'didSet',
    'subscript', 'init', 'deinit', 'operator', 'precedencegroup', 'infix', 'postfix',
    'prefix', 'assignment', 'async', 'await', 'yield'
}

# JavaScript keywords that should NOT be translated
JS_KEYWORDS = {
    'if', 'else', 'for', 'while', 'switch', 'case', 'break', 'continue', 'return',
    'var', 'let', 'const', 'function', 'class', 'extends', 'constructor', 'new',
    'this', 'super', 'import', 'export', 'from', 'default', 'true', 'false', 'null',
    'undefined', 'typeof', 'instanceof', 'void', 'delete', 'in', 'of', 'async',
    'await', 'try', 'catch', 'finally', 'throw', 'with', 'debugger', 'yield'
}

# Common answer patterns that should NOT be translated
CODE_PATTERNS = {
    # Comparison operators
    '==', '!=', '<', '>', '<=', '>=', '===', '!==',
    # Arithmetic operators
    '+', '-', '*', '/', '%', '**', '++', '--',
    # Logical operators
    '&&', '||', '!',
    # Assignment operators
    '=', '+=', '-=', '*=', '/=', '%=', '**=',
    # Other symbols
    ':', ';', '{', '}', '[', ']', '(', ')',
    # Common values
    'true', 'false', 'null', 'undefined', 'nil',
    # Print/output statements
    'print', 'console.log', 'console', 'log',
}

def should_preserve_as_code(text):
    """Check if text should be preserved as code (not translated)."""
    text = text.strip()
    # Check if it's a keyword
    if text.lower() in SWIFT_KEYWORDS or text.lower() in JS_KEYWORDS:
        return True
    # Check if it's a code pattern
    if text in CODE_PATTERNS:
        return True
    # Check if it looks like code (has operators, special chars)
    if any(op in text for op in ['==', '!=', '<=', '>=', '+=', '-=', '&&', '||', '=>', '->']):
        return True
    return False

def read_file(path):
    """Read file content."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def write_file(path, content):
    """Write content to file."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def parse_exercise(content):
    """Parse exercise into sections."""
    sections = {}
    current_section = None
    current_content = []

    for line in content.split('\n'):
        if line.startswith('# --'):
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = line.strip()
            current_content = []
        else:
            current_content.append(line)

    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()

    return sections

def build_exercise(sections):
    """Build exercise from sections."""
    lines = []
    for section, content in sections.items():
        lines.append(section)
        if content:
            lines.append(content)
        lines.append('')
    return '\n'.join(lines)

def translate_instruction(en_text):
    """Translate English instruction to Spanish."""
    translations = {
        "What is the keyword for an `if` statement?": "¿Cuál es la palabra clave para una sentencia `if`?",
        "Why is `first name` not a valid variable name?": "¿Por qué `primer nombre` no es un nombre de variable válido?",
        "Why is `second name` not a valid variable name?": "¿Por qué `segundo nombre` no es un nombre de variable válido?",
        "What is the maximum number of lines that a code block can have?": "¿Cuál es el número máximo de líneas que puede tener un bloque de código?",
        "What are the values that decide whether a code block runs or not?": "¿Cuáles son los valores que deciden si se ejecuta o no un bloque de código?",
        "What statement is used to execute a code block?": "¿Qué sentencia se utiliza para ejecutar un bloque de código?",
        "Which of the following is not a valid Swift variable name?": "¿Cuál de los siguientes no es un nombre de variable válido en Swift?",
        "What type of value is a boolean?": "¿Qué tipo de valor es un booleano?",
        "What is the result of `true && false`?": "¿Cuál es el resultado de `true && false`?",
        "What is the result of `true || false`?": "¿Cuál es el resultado de `true || false`?",
        "What is the result of `!true`?": "¿Cuál es el resultado de `!true`?",
        "How do you declare an array in Swift?": "¿Cómo declaras un array en Swift?",
        "How do you access the first element of an array?": "¿Cómo accedes al primer elemento de un array?",
        "What is the index of the first element in an array?": "¿Cuál es el índice del primer elemento en un array?",
        "How do you add an element to an array?": "¿Cómo agregas un elemento a un array?",
        "How do you remove an element from an array?": "¿Cómo eliminas un elemento de un array?",
        "What is a dictionary in Swift?": "¿Qué es un diccionario en Swift?",
        "How do you declare a dictionary in Swift?": "¿Cómo declaras un diccionario en Swift?",
        "How do you access a value in a dictionary?": "¿Cómo accedes a un valor en un diccionario?",
        "How do you add a key-value pair to a dictionary?": "¿Cómo agregas un par clave-valor a un diccionario?",
        "How do you remove a key-value pair from a dictionary?": "¿Cómo eliminas un par clave-valor de un diccionario?",
        "What is a for loop in Swift?": "¿Qué es un bucle for en Swift?",
        "How do you write a for loop in Swift?": "¿Cómo escribes un bucle for en Swift?",
        "What is a while loop in Swift?": "¿Qué es un bucle while en Swift?",
        "How do you write a while loop in Swift?": "¿Cómo escribes un bucle while en Swift?",
        "What is the difference between a for loop and a while loop?": "¿Cuál es la diferencia entre un bucle for y un bucle while?",
        "What is a function in Swift?": "¿Qué es una función en Swift?",
        "How do you declare a function in Swift?": "¿Cómo declaras una función en Swift?",
        "How do you call a function in Swift?": "¿Cómo llamas a una función en Swift?",
        "What is a parameter in a function?": "¿Qué es un parámetro en una función?",
        "What is a return value in a function?": "¿Qué es un valor de retorno en una función?",
        "What is a class in Swift?": "¿Qué es una clase en Swift?",
        "How do you declare a class in Swift?": "¿Cómo declaras una clase en Swift?",
        "What is a property in a class?": "¿Qué es una propiedad en una clase?",
        "What is a method in a class?": "¿Qué es un método en una clase?",
        "What is inheritance in Swift?": "¿Qué es la herencia en Swift?",
        "How do you create an instance of a class?": "¿Cómo creas una instancia de una clase?",
        "What is string interpolation in Swift?": "¿Qué es la interpolación de cadenas en Swift?",
        "How do you use string interpolation in Swift?": "¿Cómo usas la interpolación de cadenas en Swift?",
        "What is the output of the following code?": "¿Cuál es la salida del siguiente código?",
        "How do you print a value in Swift?": "¿Cómo imprimes un valor en Swift?",
        "How do you print a string in Swift?": "¿Cómo imprimes una cadena en Swift?",
        "How do you concatenate strings in Swift?": "¿Cómo concatenas cadenas en Swift?",
        "What is the `+` operator used for with strings?": "¿Para qué se usa el operador `+` con cadenas?",
        "Make the code block run by assigning a value to the variable": "Haz que el bloque de código se ejecute asignando un valor a la variable",
        "Create an `else if` statement checking if `hour` is equal to `12` and in the code block print the string `\"It's noon\"`": "Crea una sentencia `else if` verificando si `hora` es igual a `12` y, en el bloque de código, imprime la cadena `\"Es mediodía\"`",
        "Which print statement is part of the statement's code block?": "¿Qué sentencia de impresión es parte del bloque de código de la sentencia?",
        "What do we call statements that execute or omit code depending on whether a condition is `true` or `false`?": "¿Cómo llamamos a las sentencias que ejecutan o omiten código dependiendo de si una condición es `verdadera` o `falsa`?",
        # JavaScript specific
        "What is a variable in JavaScript?": "¿Qué es una variable en JavaScript?",
        "How do you declare a variable in JavaScript?": "¿Cómo declaras una variable en JavaScript?",
        "What is the difference between `var`, `let`, and `const`?": "¿Cuál es la diferencia entre `var`, `let` y `const`?",
        "What is a boolean in JavaScript?": "¿Qué es un booleano en JavaScript?",
        "What are the boolean values in JavaScript?": "¿Cuáles son los valores booleanos en JavaScript?",
        "What is the result of `2 + 2`?": "¿Cuál es el resultado de `2 + 2`?",
        "What is the result of `10 - 5`?": "¿Cuál es el resultado de `10 - 5`?",
        "What is the result of `3 * 4`?": "¿Cuál es el resultado de `3 * 4`?",
        "What is the result of `20 / 4`?": "¿Cuál es el resultado de `20 / 4`?",
        "What is the result of `10 % 3`?": "¿Cuál es el resultado de `10 % 3`?",
        "What is a while loop in JavaScript?": "¿Qué es un bucle while en JavaScript?",
        "How do you write a while loop in JavaScript?": "¿Cómo escribes un bucle while en JavaScript?",
        "What is the difference between `while` and `do-while` loops?": "¿Cuál es la diferencia entre los bucles `while` y `do-while`?",
    }

    # Check for exact match first
    if en_text in translations:
        return translations[en_text]

    # If no exact match, return original (would need actual translation API)
    return en_text

def translate_answer(en_answer):
    """Translate English answer to Spanish, preserving code keywords."""
    # Check if it should be preserved as code
    if should_preserve_as_code(en_answer):
        return en_answer

    translations = {
        "One": "Uno",
        "Two": "Dos",
        "Three": "Tres",
        "Four": "Cuatro",
        "Five": "Cinco",
        "As many as we want": "Los que queramos",
        "Conditions": "Condiciones",
        "Strings": "Strings",
        "Integers": "Integers",
        "Booleans": "Booleanos",
        "Because both words need to be capitalized": "Porque ambas palabras deben estar en mayúsculas",
        "Because it's not descriptive": "Porque no es descriptivo",
        "Because it contains a space between first and name": "Porque contiene un espacio entre primer y nombre",
        "Because it contains a space between second and name": "Porque contiene un espacio entre segundo y nombre",
        "A number": "Un número",
        "A string": "Una cadena",
        "A boolean": "Un booleano",
        "An object": "Un objeto",
        "An array": "Un array",
        "A function": "Una función",
        "true": "true",
        "false": "false",
        "null": "null",
        "undefined": "undefined",
        "nil": "nil",
        "Yes": "Sí",
        "No": "No",
        "All of the above": "Todas las anteriores",
        "None of the above": "Ninguna de las anteriores",
    }

    # Check for exact match
    if en_answer in translations:
        return translations[en_answer]

    return en_answer

def fix_exercise(en_path, es_path):
    """Fix a Spanish exercise by comparing with English version."""
    en_content = read_file(en_path)
    es_content = read_file(es_path)

    if not en_content or not es_content:
        return False

    en_sections = parse_exercise(en_content)
    es_sections = parse_exercise(es_content)

    # Get frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---', en_content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(0)

    # Fix instructions
    if '# --instructions--' in en_sections and '# --instructions--' in es_sections:
        en_instr = en_sections['# --instructions--']
        # Only translate if the Spanish looks wrong (mixed English/Spanish)
        if any(word in es_sections['# --instructions--'].lower() for word in ['the ', 'and ', 'for ', 'what ', 'why ', 'how ']):
            es_sections['# --instructions--'] = translate_instruction(en_instr)

    # Fix answers for type 3 exercises
    if '# --answers--' in en_sections and '# --answers--' in es_sections:
        en_answers = [a.strip('- ').strip() for a in en_sections['# --answers--'].split('\n') if a.strip()]
        es_answers_raw = es_sections['# --answers--'].split('\n')
        es_answers = [a.strip('- ').strip() for a in es_answers_raw if a.strip()]

        # Only fix if answers look wrong
        if len(en_answers) == len(es_answers):
            new_es_answers = []
            for i, en_ans in enumerate(en_answers):
                # If Spanish answer has mixed English, translate it
                es_ans = es_answers[i] if i < len(es_answers) else en_ans
                if any(word in es_ans.lower() for word in ['the ', 'and ', 'because ', 'both ']):
                    new_es_answers.append(f"- {translate_answer(en_ans)}")
                else:
                    # Keep original Spanish answer if it looks OK
                    new_es_answers.append(f"- {es_ans}")
            es_sections['# --answers--'] = '\n'.join(new_es_answers)

    # Fix solution for type 3 exercises
    if '# --solutions--' in en_sections and '# --solutions--' in es_sections:
        en_sol = en_sections['# --solutions--'].strip('- ').strip()
        es_sol = es_sections['# --solutions--'].strip('- ').strip()

        # If solution is in English or mixed, translate it
        if any(word in es_sol.lower() for word in ['the ', 'and ', 'because ', 'both ', 'conditions']):
            es_sections['# --solutions--'] = f"- {translate_answer(en_sol)}"

    # Rebuild file
    lines = [frontmatter, '']
    for section, content in es_sections.items():
        lines.append(section)
        if content:
            lines.append(content)
        lines.append('')

    write_file(es_path, '\n'.join(lines))
    return True

# List of files to fix
FILES_TO_FIX = [
    ('/es/swift/conditionalStatements/13.md', '/en/swift/conditionalStatements/13.md'),
    ('/es/swift/conditionalStatements/15.md', '/en/swift/conditionalStatements/15.md'),
    ('/es/swift/conditionalStatements/21.md', '/en/swift/conditionalStatements/21.md'),
    ('/es/swift/conditionalStatements/24.md', '/en/swift/conditionalStatements/24.md'),
    ('/es/swift/conditionalStatements/25.md', '/en/swift/conditionalStatements/25.md'),
    ('/es/swift/conditionalStatements/30.md', '/en/swift/conditionalStatements/30.md'),
    ('/es/swift/conditionalStatements/31.md', '/en/swift/conditionalStatements/31.md'),
    ('/es/swift/conditionalStatements/33.md', '/en/swift/conditionalStatements/33.md'),
    ('/es/swift/conditionalStatements/34.md', '/en/swift/conditionalStatements/34.md'),
    ('/es/swift/conditionalStatements/35.md', '/en/swift/conditionalStatements/35.md'),
    ('/es/swift/conditionalStatements/41.md', '/en/swift/conditionalStatements/41.md'),
    ('/es/swift/conditionalStatements/42.md', '/en/swift/conditionalStatements/42.md'),
    ('/es/swift/conditionalStatements/44.md', '/en/swift/conditionalStatements/44.md'),
    ('/es/swift/conditionalStatements/45.md', '/en/swift/conditionalStatements/45.md'),
    ('/es/swift/conditionalStatements/8.md', '/en/swift/conditionalStatements/8.md'),
    ('/es/swift/variables/10.md', '/en/swift/variables/10.md'),
    ('/es/swift/variables/11.md', '/en/swift/variables/11.md'),
    ('/es/swift/variables/14.md', '/en/swift/variables/14.md'),
    ('/es/swift/variables/16.md', '/en/swift/variables/16.md'),
    ('/es/swift/variables/20.md', '/en/swift/variables/20.md'),
    ('/es/swift/booleans/3.md', '/en/swift/booleans/3.md'),
    ('/es/swift/booleans/4.md', '/en/swift/booleans/4.md'),
    ('/es/swift/booleans/5.md', '/en/swift/booleans/5.md'),
    ('/es/swift/booleans/6.md', '/en/swift/booleans/6.md'),
    ('/es/swift/booleans/7.md', '/en/swift/booleans/7.md'),
    ('/es/swift/arrays/1.md', '/en/swift/arrays/1.md'),
    ('/es/swift/arrays/5.md', '/en/swift/arrays/5.md'),
    ('/es/swift/arrays/9.md', '/en/swift/arrays/9.md'),
    ('/es/swift/arrays/13.md', '/en/swift/arrays/13.md'),
    ('/es/swift/arrays/14.md', '/en/swift/arrays/14.md'),
    ('/es/swift/dictionaries/1.md', '/en/swift/dictionaries/1.md'),
    ('/es/swift/dictionaries/5.md', '/en/swift/dictionaries/5.md'),
    ('/es/swift/dictionaries/12.md', '/en/swift/dictionaries/12.md'),
    ('/es/swift/forLoops/7.md', '/en/swift/forLoops/7.md'),
    ('/es/swift/forLoops/9.md', '/en/swift/forLoops/9.md'),
    ('/es/swift/forLoops/10.md', '/en/swift/forLoops/10.md'),
    ('/es/swift/forLoops/13.md', '/en/swift/forLoops/13.md'),
    ('/es/swift/forLoops/16.md', '/en/swift/forLoops/16.md'),
    ('/es/swift/forLoops/18.md', '/en/swift/forLoops/18.md'),
    ('/es/swift/whileLoops/8.md', '/en/swift/whileLoops/8.md'),
    ('/es/swift/whileLoops/9.md', '/en/swift/whileLoops/9.md'),
    ('/es/swift/whileLoops/10.md', '/en/swift/whileLoops/10.md'),
    ('/es/swift/whileLoops/11.md', '/en/swift/whileLoops/11.md'),
    ('/es/swift/whileLoops/12.md', '/en/swift/whileLoops/12.md'),
    ('/es/swift/whileLoops/13.md', '/en/swift/whileLoops/13.md'),
    ('/es/swift/whileLoops/19.md', '/en/swift/whileLoops/19.md'),
    ('/es/swift/whileLoops/20.md', '/en/swift/whileLoops/20.md'),
    ('/es/swift/whileLoops/21.md', '/en/swift/whileLoops/21.md'),
    ('/es/swift/whileLoops/27.md', '/en/swift/whileLoops/27.md'),
    ('/es/swift/whileLoops/28.md', '/en/swift/whileLoops/28.md'),
    ('/es/swift/whileLoops/29.md', '/en/swift/whileLoops/29.md'),
    ('/es/swift/whileLoops/30.md', '/en/swift/whileLoops/30.md'),
    ('/es/swift/whileLoops/31.md', '/en/swift/whileLoops/31.md'),
    ('/es/swift/whileLoops/32.md', '/en/swift/whileLoops/32.md'),
    ('/es/swift/whileLoops/33.md', '/en/swift/whileLoops/33.md'),
    ('/es/swift/whileLoops/34.md', '/en/swift/whileLoops/34.md'),
    ('/es/swift/whileLoops/39.md', '/en/swift/whileLoops/39.md'),
    ('/es/swift/whileLoops/43.md', '/en/swift/whileLoops/43.md'),
    ('/es/swift/whileLoops/44.md', '/en/swift/whileLoops/44.md'),
    ('/es/swift/functions/2.md', '/en/swift/functions/2.md'),
    ('/es/swift/functions/10.md', '/en/swift/functions/10.md'),
    ('/es/swift/functions/11.md', '/en/swift/functions/11.md'),
    ('/es/swift/functions/12.md', '/en/swift/functions/12.md'),
    ('/es/swift/classes/3.md', '/en/swift/classes/3.md'),
    ('/es/swift/classes/6.md', '/en/swift/classes/6.md'),
    ('/es/swift/classes/9.md', '/en/swift/classes/9.md'),
    ('/es/swift/classes/10.md', '/en/swift/classes/10.md'),
    ('/es/swift/classes/11.md', '/en/swift/classes/11.md'),
    ('/es/swift/comparisonLogicalOperators/16.md', '/en/swift/comparisonLogicalOperators/16.md'),
    ('/es/swift/comparisonLogicalOperators/17.md', '/en/swift/comparisonLogicalOperators/17.md'),
    ('/es/swift/comparisonLogicalOperators/18.md', '/en/swift/comparisonLogicalOperators/18.md'),
    ('/es/swift/comparisonLogicalOperators/19.md', '/en/swift/comparisonLogicalOperators/19.md'),
    ('/es/swift/comparisonLogicalOperators/20.md', '/en/swift/comparisonLogicalOperators/20.md'),
    ('/es/swift/comparisonLogicalOperators/21.md', '/en/swift/comparisonLogicalOperators/21.md'),
    ('/es/swift/comparisonLogicalOperators/22.md', '/en/swift/comparisonLogicalOperators/22.md'),
    ('/es/swift/comparisonLogicalOperators/23.md', '/en/swift/comparisonLogicalOperators/23.md'),
    ('/es/swift/stringInterpolation/9.md', '/en/swift/stringInterpolation/9.md'),
    ('/es/swift/stringInterpolation/10.md', '/en/swift/stringInterpolation/10.md'),
    ('/es/swift/stringInterpolation/11.md', '/en/swift/stringInterpolation/11.md'),
    ('/es/swift/stringInterpolation/12.md', '/en/swift/stringInterpolation/12.md'),
    ('/es/swift/stringInterpolation/13.md', '/en/swift/stringInterpolation/13.md'),
    ('/es/swift/stringInterpolation/15.md', '/en/swift/stringInterpolation/15.md'),
    ('/es/swift/stringInterpolation/17.md', '/en/swift/stringInterpolation/17.md'),
    ('/es/swift/stringInterpolation/19.md', '/en/swift/stringInterpolation/19.md'),
    ('/es/swift/stringInterpolation/21.md', '/en/swift/stringInterpolation/21.md'),
    ('/es/swift/stringInterpolation/23.md', '/en/swift/stringInterpolation/23.md'),
    ('/es/swift/stringInterpolation/24.md', '/en/swift/stringInterpolation/24.md'),
    ('/es/swift/output/1.md', '/en/swift/output/1.md'),
    ('/es/swift/output/3.md', '/en/swift/output/3.md'),
    ('/es/swift/output/6.md', '/en/swift/output/6.md'),
    ('/es/swift/output/7.md', '/en/swift/output/7.md'),
    ('/es/swift/output/8.md', '/en/swift/output/8.md'),
    ('/es/javascript/arithmeticOperators/16.md', '/en/javascript/arithmeticOperators/16.md'),
    ('/es/javascript/arithmeticOperators/17.md', '/en/javascript/arithmeticOperators/17.md'),
    ('/es/javascript/booleans/12.md', '/en/javascript/booleans/12.md'),
    ('/es/javascript/booleans/13.md', '/en/javascript/booleans/13.md'),
    ('/es/javascript/variables/1.md', '/en/javascript/variables/1.md'),
    ('/es/javascript/variables/2.md', '/en/javascript/variables/2.md'),
    ('/es/javascript/variables/3.md', '/en/javascript/variables/3.md'),
    ('/es/javascript/variables/4.md', '/en/javascript/variables/4.md'),
    ('/es/javascript/variables/5.md', '/en/javascript/variables/5.md'),
    ('/es/javascript/variables/9.md', '/en/javascript/variables/9.md'),
    ('/es/javascript/variables/15.md', '/en/javascript/variables/15.md'),
    ('/es/javascript/whileLoops/38.md', '/en/javascript/whileLoops/38.md'),
]

def main():
    base_path = '/Users/ale/github/codigo-questions'
    fixed = 0
    failed = 0

    for es_rel, en_rel in FILES_TO_FIX:
        es_path = base_path + es_rel
        en_path = base_path + en_rel
        try:
            if fix_exercise(en_path, es_path):
                print(f"✓ Fixed {es_rel}")
                fixed += 1
            else:
                print(f"✗ Failed {es_rel}")
                failed += 1
        except Exception as e:
            print(f"✗ Error {es_rel}: {e}")
            failed += 1

    print(f"\nFixed: {fixed}, Failed: {failed}")

if __name__ == '__main__':
    main()
