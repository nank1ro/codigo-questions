#!/usr/bin/env python3
"""
Fix Spanish translations by completely rewriting them from English versions.
"""

import os
import re
from pathlib import Path

# Translation dictionary for common instructions
INSTRUCTION_TRANSLATIONS = {
    "What does this code display in the output?": "¿Qué muestra este código en la salida?",
    "What is the output of the following code?": "¿Cuál es la salida del siguiente código?",
    "What is the result of the following code?": "¿Cuál es el resultado del siguiente código?",
    "What is the keyword for an `if` statement?": "¿Cuál es la palabra clave para una sentencia `if`?",
    "What do we call statements that execute or omit code depending on whether a condition is `true` or `false`?": "¿Cómo llamamos a las sentencias que ejecutan o omiten código dependiendo de si una condición es `true` o `false`?",
    "What statement is used to execute a code block when a condition is true?": "¿Qué sentencia se usa para ejecutar un bloque de código cuando una condición es verdadera?",
    "Which of the following is NOT a valid variable name in Swift?": "¿Cuál de los siguientes NO es un nombre de variable válido en Swift?",
    "What is the maximum number of lines that a code block can have?": "¿Cuál es el número máximo de líneas que puede tener un bloque de código?",
    "What are the values that decide whether a code block runs or not?": "¿Cuáles son los valores que deciden si se ejecuta o no un bloque de código?",
    "Make the code block run by assigning a value to the variable": "Haz que el bloque de código se ejecute asignando un valor a la variable",
    "Create an `else if` statement checking if `hour` is equal to `12` and in the code block print the string `\"It's noon\"`": "Crea una sentencia `else if` verificando si `hora` es igual a `12` y, en el bloque de código, imprime la cadena `\"Es mediodía\"`",
    "Which print statement is part of the statement's code block?": "¿Qué sentencia de impresión es parte del bloque de código de la sentencia?",
    "Why is `first name` not a valid variable name?": "¿Por qué `primer nombre` no es un nombre de variable válido?",
    "Why is `second name` not a valid variable name?": "¿Por qué `segundo nombre` no es un nombre de variable válido?",
    "What is the result of `true && false`?": "¿Cuál es el resultado de `true && false`?",
    "What is the result of `true || false`?": "¿Cuál es el resultado de `true || false`?",
    "What is the result of `!true`?": "¿Cuál es el resultado de `!true`?",
    "What type of value is a boolean?": "¿Qué tipo de valor es un booleano?",
    "What do you need to access an element in an array?": "¿Qué necesitas para acceder a un elemento en un array?",
    "What is the index of the first element in an array?": "¿Cuál es el índice del primer elemento en un array?",
    "How do you get the number of elements in an array?": "¿Cómo obtienes el número de elementos en un array?",
    "What keyword is used to add an element to an array?": "¿Qué palabra clave se usa para agregar un elemento a un array?",
    "What keyword is used to remove an element from an array?": "¿Qué palabra clave se usa para eliminar un elemento de un array?",
    "What do you use to store key-value pairs in Swift?": "¿Qué usas para almacenar pares clave-valor en Swift?",
    "How do you access a value in a dictionary using its key?": "¿Cómo accedes a un valor en un diccionario usando su clave?",
    "How do you add a new key-value pair to a dictionary?": "¿Cómo agregas un nuevo par clave-valor a un diccionario?",
    "How do you remove a key-value pair from a dictionary?": "¿Cómo eliminas un par clave-valor de un diccionario?",
    "What is a loop in programming?": "¿Qué es un bucle en programación?",
    "What keyword is used to create a for loop in Swift?": "¿Qué palabra clave se usa para crear un bucle for en Swift?",
    "What keyword is used to create a while loop in Swift?": "¿Qué palabra clave se usa para crear un bucle while en Swift?",
    "What is the difference between a for loop and a while loop?": "¿Cuál es la diferencia entre un bucle for y un bucle while?",
    "What is a function in Swift?": "¿Qué es una función en Swift?",
    "What keyword is used to declare a function in Swift?": "¿Qué palabra clave se usa para declarar una función en Swift?",
    "What do you call a value that is passed into a function?": "¿Cómo llamas a un valor que se pasa a una función?",
    "What keyword is used to return a value from a function?": "¿Qué palabra clave se usa para devolver un valor de una función?",
    "What is a class in Swift?": "¿Qué es una clase en Swift?",
    "What keyword is used to declare a class in Swift?": "¿Qué palabra clave se usa para declarar una clase en Swift?",
    "What is a property in a class?": "¿Qué es una propiedad en una clase?",
    "What is a method in a class?": "¿Qué es un método en una clase?",
    "What is inheritance in Swift?": "¿Qué es la herencia en Swift?",
    "How do you create an instance of a class?": "¿Cómo creas una instancia de una clase?",
    "What is string interpolation in Swift?": "¿Qué es la interpolación de cadenas en Swift?",
    "What symbol is used for string interpolation in Swift?": "¿Qué símbolo se usa para la interpolación de cadenas en Swift?",
    "How do you print a value in Swift?": "¿Cómo imprimes un valor en Swift?",
    "How do you print a string in Swift?": "¿Cómo imprimes una cadena en Swift?",
    "What is the result of `10 + 5`?": "¿Cuál es el resultado de `10 + 5`?",
    "What is the result of `10 - 5`?": "¿Cuál es el resultado de `10 - 5`?",
    "What is the result of `10 * 5`?": "¿Cuál es el resultado de `10 * 5`?",
    "What is the result of `10 / 5`?": "¿Cuál es el resultado de `10 / 5`?",
    "What is the result of `10 % 3`?": "¿Cuál es el resultado de `10 % 3`?",
    "What is the result of `10 == 10`?": "¿Cuál es el resultado de `10 == 10`?",
    "What is the result of `10 != 5`?": "¿Cuál es el resultado de `10 != 5`?",
    "What is the result of `10 > 5`?": "¿Cuál es el resultado de `10 > 5`?",
    "What is the result of `10 < 5`?": "¿Cuál es el resultado de `10 < 5`?",
    "What is the result of `10 >= 10`?": "¿Cuál es el resultado de `10 >= 10`?",
    "What is the result of `10 <= 5`?": "¿Cuál es el resultado de `10 <= 5`?",
    "What is a variable in JavaScript?": "¿Qué es una variable en JavaScript?",
    "What keywords are used to declare variables in JavaScript?": "¿Qué palabras clave se usan para declarar variables en JavaScript?",
    "What is the difference between `var`, `let`, and `const`?": "¿Cuál es la diferencia entre `var`, `let` y `const`?",
    "What is a boolean in JavaScript?": "¿Qué es un booleano en JavaScript?",
    "What are the two boolean values in JavaScript?": "¿Cuáles son los dos valores booleanos en JavaScript?",
    "What is a while loop in JavaScript?": "¿Qué es un bucle while en JavaScript?",
    "What is the difference between a while loop and a do-while loop?": "¿Cuál es la diferencia entre un bucle while y un bucle do-while?",
}

# Translation dictionary for common answers
ANSWER_TRANSLATIONS = {
    "Hello!": "¡Hello!",
    "Nothing because the code block gets skipped": "Nada porque el bloque de código se omite",
    "Because both words need to be capitalized": "Porque ambas palabras deben estar en mayúsculas",
    "Because it's not descriptive": "Porque no es descriptivo",
    "Because it contains a space between first and name": "Porque contiene un espacio entre first y name",
    "Because it contains a space between second and name": "Porque contiene un espacio entre second y name",
    "One": "Uno",
    "Two": "Dos",
    "Four": "Cuatro",
    "As many as we want": "Los que queramos",
    "Conditions": "Condiciones",
    "Strings": "Strings",
    "Integers": "Integers",
    "Booleans": "Booleanos",
    "true": "true",
    "false": "false",
    "null": "null",
    "undefined": "undefined",
    "nil": "nil",
    "The index": "El índice",
    "The key": "La clave",
    "The value": "El valor",
    "The print() function": "La función print()",
    "The console.log() function": "La función console.log()",
    "The var keyword": "La palabra clave var",
    "The let keyword": "La palabra clave let",
    "The const keyword": "La palabra clave const",
}

# Answers that should NOT be translated (code keywords, etc.)
PRESERVE_ANSWERS = {
    'if', 'else', 'for', 'while', 'switch', 'case', 'break', 'continue',
    'return', 'var', 'let', 'const', 'func', 'function', 'class', 'struct',
    'true', 'false', 'null', 'undefined', 'nil',
    '==', '!=', '<', '>', '<=', '>=', '===', '!==',
    '+', '-', '*', '/', '%', '++', '--',
    '&&', '||', '!',
    '=', '+=', '-=', '*=', '/=', '%=',
    ':', ';', '{', '}', '[', ']', '(', ')',
    'print', 'console.log', 'console', 'log',
    'Hello!', 'Nothing because the code block gets skipped',
}

def should_preserve_answer(answer):
    """Check if an answer should be preserved (not translated)."""
    ans = answer.strip()
    # Check if it's a code keyword
    if ans.lower() in PRESERVE_ANSWERS:
        return True
    # Check if it's purely code/symbols
    if re.match(r'^[\s\w\+\-\*/\=\>\<\!\&\|\:\;\{\}\[\]\(\)]+$', ans):
        # If it contains only code symbols and keywords, preserve it
        if any(kw in ans.lower() for kw in ['if', 'else', 'for', 'while', 'true', 'false', 'null', 'var', 'let', 'const']):
            return True
        if any(op in ans for op in ['==', '!=', '<=', '>=', '&&', '||', '+=', '-=']):
            return True
    return False

def translate_instruction(text):
    """Translate an instruction to Spanish."""
    if text in INSTRUCTION_TRANSLATIONS:
        return INSTRUCTION_TRANSLATIONS[text]
    return text

def translate_answer(text):
    """Translate an answer to Spanish."""
    if should_preserve_answer(text):
        return text
    if text in ANSWER_TRANSLATIONS:
        return ANSWER_TRANSLATIONS[text]
    return text

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

def fix_type3_exercise(en_path, es_path):
    """Fix a type 3 exercise (choose answer)."""
    en_content = read_file(en_path)
    if not en_content:
        return False

    lines = en_content.split('\n')
    es_lines = ['---', 'language: swift', 'exerciseType: 3', '---', '', '']

    current_section = None
    instructions = []
    answers = []
    solution = None
    code_block = []

    for line in lines:
        if line.startswith('# --instructions--'):
            current_section = 'instructions'
        elif line.startswith('# --answers--'):
            current_section = 'answers'
        elif line.startswith('# --solutions--'):
            current_section = 'solutions'
        elif line.startswith('# --'):
            current_section = None
        elif current_section == 'instructions':
            if line.strip().startswith('```'):
                code_block.append(line)
            elif code_block:
                code_block.append(line)
            elif line.strip():
                instructions.append(line)
        elif current_section == 'answers':
            if line.strip().startswith('-'):
                ans = line.strip()[1:].strip()
                answers.append(ans)
        elif current_section == 'solutions':
            if line.strip().startswith('-'):
                solution = line.strip()[1:].strip()

    # Build Spanish content
    es_lines.append('# --instructions--')
    es_lines.append('')

    # Translate and add instructions
    full_instruction = ' '.join(instructions)
    translated_instruction = translate_instruction(full_instruction)

    # Check if there's a code block in the instructions
    if code_block:
        es_lines.append(translated_instruction)
        es_lines.append('')
        for line in code_block:
            es_lines.append(line)
        es_lines.append('')
    else:
        es_lines.append(translated_instruction)
        es_lines.append('')

    # Add answers
    es_lines.append('# --answers--')
    es_lines.append('')
    for ans in answers:
        translated_ans = translate_answer(ans)
        es_lines.append(f"- {translated_ans}")
    es_lines.append('')

    # Add solution
    es_lines.append('# --solutions--')
    es_lines.append('')
    if solution:
        translated_sol = translate_answer(solution)
        es_lines.append(f"- {translated_sol}")
    es_lines.append('')

    write_file(es_path, '\n'.join(es_lines))
    return True

def fix_exercise_from_english(en_path, es_path):
    """Fix a Spanish exercise based on English version."""
    en_content = read_file(en_path)
    if not en_content:
        return False

    # Check exercise type
    type_match = re.search(r'exerciseType:\s*(\d+)', en_content)
    if not type_match:
        return False

    exercise_type = int(type_match.group(1))

    if exercise_type == 3:
        return fix_type3_exercise(en_path, es_path)

    # For other types, do a simpler fix
    # TODO: Implement other exercise types
    return False

# List of files to fix
FILES_TO_FIX = [
    # Swift conditionalStatements
    ('/es/swift/conditionalStatements/8.md', '/en/swift/conditionalStatements/8.md'),
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
    # Swift variables
    ('/es/swift/variables/11.md', '/en/swift/variables/11.md'),
    ('/es/swift/variables/14.md', '/en/swift/variables/14.md'),
    ('/es/swift/variables/16.md', '/en/swift/variables/16.md'),
    ('/es/swift/variables/20.md', '/en/swift/variables/20.md'),
    # Swift booleans
    ('/es/swift/booleans/3.md', '/en/swift/booleans/3.md'),
    ('/es/swift/booleans/4.md', '/en/swift/booleans/4.md'),
    ('/es/swift/booleans/5.md', '/en/swift/booleans/5.md'),
    ('/es/swift/booleans/6.md', '/en/swift/booleans/6.md'),
    ('/es/swift/booleans/7.md', '/en/swift/booleans/7.md'),
    # Swift arrays
    ('/es/swift/arrays/1.md', '/en/swift/arrays/1.md'),
    ('/es/swift/arrays/5.md', '/en/swift/arrays/5.md'),
    ('/es/swift/arrays/9.md', '/en/swift/arrays/9.md'),
    ('/es/swift/arrays/13.md', '/en/swift/arrays/13.md'),
    ('/es/swift/arrays/14.md', '/en/swift/arrays/14.md'),
    # Swift dictionaries
    ('/es/swift/dictionaries/12.md', '/en/swift/dictionaries/12.md'),
    # Swift forLoops
    ('/es/swift/forLoops/7.md', '/en/swift/forLoops/7.md'),
    ('/es/swift/forLoops/9.md', '/en/swift/forLoops/9.md'),
    ('/es/swift/forLoops/10.md', '/en/swift/forLoops/10.md'),
    ('/es/swift/forLoops/13.md', '/en/swift/forLoops/13.md'),
    ('/es/swift/forLoops/16.md', '/en/swift/forLoops/16.md'),
    ('/es/swift/forLoops/18.md', '/en/swift/forLoops/18.md'),
    # Swift whileLoops
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
    # Swift functions
    ('/es/swift/functions/2.md', '/en/swift/functions/2.md'),
    ('/es/swift/functions/10.md', '/en/swift/functions/10.md'),
    ('/es/swift/functions/11.md', '/en/swift/functions/11.md'),
    ('/es/swift/functions/12.md', '/en/swift/functions/12.md'),
    # Swift classes
    ('/es/swift/classes/3.md', '/en/swift/classes/3.md'),
    ('/es/swift/classes/6.md', '/en/swift/classes/6.md'),
    ('/es/swift/classes/9.md', '/en/swift/classes/9.md'),
    ('/es/swift/classes/10.md', '/en/swift/classes/10.md'),
    ('/es/swift/classes/11.md', '/en/swift/classes/11.md'),
    # Swift comparisonLogicalOperators
    ('/es/swift/comparisonLogicalOperators/16.md', '/en/swift/comparisonLogicalOperators/16.md'),
    ('/es/swift/comparisonLogicalOperators/17.md', '/en/swift/comparisonLogicalOperators/17.md'),
    ('/es/swift/comparisonLogicalOperators/18.md', '/en/swift/comparisonLogicalOperators/18.md'),
    ('/es/swift/comparisonLogicalOperators/19.md', '/en/swift/comparisonLogicalOperators/19.md'),
    ('/es/swift/comparisonLogicalOperators/20.md', '/en/swift/comparisonLogicalOperators/20.md'),
    ('/es/swift/comparisonLogicalOperators/21.md', '/en/swift/comparisonLogicalOperators/21.md'),
    ('/es/swift/comparisonLogicalOperators/22.md', '/en/swift/comparisonLogicalOperators/22.md'),
    ('/es/swift/comparisonLogicalOperators/23.md', '/en/swift/comparisonLogicalOperators/23.md'),
    # Swift stringInterpolation
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
    # Swift output
    ('/es/swift/output/1.md', '/en/swift/output/1.md'),
    ('/es/swift/output/3.md', '/en/swift/output/3.md'),
    ('/es/swift/output/6.md', '/en/swift/output/6.md'),
    ('/es/swift/output/7.md', '/en/swift/output/7.md'),
    ('/es/swift/output/8.md', '/en/swift/output/8.md'),
    # JavaScript variables
    ('/es/javascript/variables/1.md', '/en/javascript/variables/1.md'),
    ('/es/javascript/variables/2.md', '/en/javascript/variables/2.md'),
    ('/es/javascript/variables/3.md', '/en/javascript/variables/3.md'),
    ('/es/javascript/variables/4.md', '/en/javascript/variables/4.md'),
    ('/es/javascript/variables/5.md', '/en/javascript/variables/5.md'),
    ('/es/javascript/variables/9.md', '/en/javascript/variables/9.md'),
    ('/es/javascript/variables/15.md', '/en/javascript/variables/15.md'),
    # JavaScript booleans
    ('/es/javascript/booleans/12.md', '/en/javascript/booleans/12.md'),
    ('/es/javascript/booleans/13.md', '/en/javascript/booleans/13.md'),
    # JavaScript arithmeticOperators
    ('/es/javascript/arithmeticOperators/16.md', '/en/javascript/arithmeticOperators/16.md'),
    ('/es/javascript/arithmeticOperators/17.md', '/en/javascript/arithmeticOperators/17.md'),
    # JavaScript whileLoops
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
            if fix_exercise_from_english(en_path, es_path):
                print(f"✓ Fixed {es_rel}")
                fixed += 1
            else:
                print(f"✗ Skipped {es_rel} (not type 3)")
                failed += 1
        except Exception as e:
            print(f"✗ Error {es_rel}: {e}")
            failed += 1

    print(f"\nFixed: {fixed}, Failed/Skipped: {failed}")

if __name__ == '__main__':
    main()
