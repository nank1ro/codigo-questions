#!/usr/bin/env python3
"""
Comprehensive fix for Spanish translations by copying from English and translating sections.
"""

import os
import re

# Translation dictionary for common instructions
TYPE2_INSTRUCTIONS = {
    "Fill in the blanks in order to print `\"Hello\"`": "Completa los espacios en blanco para imprimir `\"Hello\"`",
    "Use the _nil-coalescing operator_": "Usa el _operador de coalescencia nula_",
    "Complete the code in order to create a valid array": "Completa el código para crear un array válido",
    "Complete the code to print each element of the array": "Completa el código para imprimir cada elemento del array",
    "Complete the code to add an element to the array": "Completa el código para agregar un elemento al array",
    "Complete the code to remove an element from the array": "Completa el código para eliminar un elemento del array",
    "Use the append method to add an element to the array": "Usa el método append para agregar un elemento al array",
    "Complete the code to access the first element of the array": "Completa el código para acceder al primer elemento del array",
    "Complete the code to get the number of elements in the array": "Completa el código para obtener el número de elementos del array",
    "Create a for loop that prints each number": "Crea un bucle for que imprima cada número",
    "Create a while loop that prints numbers from 1 to 5": "Crea un bucle while que imprima números del 1 al 5",
    "Complete the code to create a function that returns the sum": "Completa el código para crear una función que devuelve la suma",
    "Complete the function to return the sum of two numbers": "Completa la función para devolver la suma de dos números",
    "Complete the function to print a message": "Completa la función para imprimir un mensaje",
    "Complete the code to create a class": "Completa el código para crear una clase",
    "Complete the class to add a property": "Completa la clase para agregar una propiedad",
    "Complete the class to add a method": "Completa la clase para agregar un método",
    "Use string interpolation to print the value": "Usa la interpolación de cadenas para imprimir el valor",
    "Complete the code to print the value": "Completa el código para imprimir el valor",
    "Complete the code to print a message": "Completa el código para imprimir un mensaje",
}

TYPE3_INSTRUCTIONS = {
    "What does this code display in the output?": "¿Qué muestra este código en la salida?",
    "What is the output of the following code?": "¿Cuál es la salida del siguiente código?",
    "What is the result of the following code?": "¿Cuál es el resultado del siguiente código?",
    "What is the keyword for an `if` statement?": "¿Cuál es la palabra clave para una sentencia `if`?",
    "What do we call statements that execute or omit code depending on whether a condition is `true` or `false`?": "¿Cómo llamamos a las sentencias que ejecutan o omiten código dependiendo de si una condición es `true` o `false`?",
    "What statement is used to execute a code block when a condition is true?": "¿Qué sentencia se usa para ejecutar un bloque de código cuando una condición es verdadera?",
    "Which of the following is NOT a valid variable name in Swift?": "¿Cuál de los siguientes NO es un nombre de variable válido en Swift?",
    "What is the maximum number of lines that a code block can have?": "¿Cuál es el número máximo de líneas que puede tener un bloque de código?",
    "What are the values that decide whether a code block runs or not?": "¿Cuáles son los valores que deciden si se ejecuta o no un bloque de código?",
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
}

TYPE3_ANSWERS = {
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
    "The index": "El índice",
    "The key": "La clave",
    "The value": "El valor",
    "The print() function": "La función print()",
    "The console.log() function": "La función console.log()",
}

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def translate_instruction(text):
    combined = {**TYPE2_INSTRUCTIONS, **TYPE3_INSTRUCTIONS}
    if text in combined:
        return combined[text]
    return text

def translate_answer_type3(text):
    if text in TYPE3_ANSWERS:
        return TYPE3_ANSWERS[text]
    # Preserve code keywords
    if text.lower() in ['if', 'else', 'for', 'while', 'true', 'false', 'null', 'nil', 'var', 'let', 'const']:
        return text
    return text

def fix_type2_exercise(en_path, es_path):
    """Fix a type 2 exercise by translating description and instructions only."""
    en_content = read_file(en_path)
    if not en_content:
        return False

    lines = en_content.split('\n')
    es_lines = []

    current_section = None
    description_lines = []
    instruction_lines = []
    skip_until_section = None

    for i, line in enumerate(lines):
        if line.startswith('---'):
            # Copy frontmatter
            es_lines.append(line)
            continue
        elif line.startswith('language:'):
            es_lines.append(line)
            continue
        elif line.startswith('exerciseType:'):
            es_lines.append(line)
            continue
        elif line.strip() == '---' and len(es_lines) > 0:
            es_lines.append(line)
            es_lines.append('')
            current_section = None
        elif line.startswith('# --description--'):
            current_section = 'description'
            es_lines.append(line)
            es_lines.append('')
        elif line.startswith('# --instructions--'):
            current_section = 'instructions'
            # Add translated description
            full_desc = ' '.join(description_lines)
            es_lines.append(full_desc)
            es_lines.append('')
            es_lines.append(line)
            es_lines.append('')
        elif line.startswith('# --') or line.startswith('```'):
            if current_section == 'instructions':
                # Add translated instruction
                full_instr = ' '.join(instruction_lines)
                es_lines.append(translate_instruction(full_instr))
                es_lines.append('')
                instruction_lines = []
            current_section = 'other'
            es_lines.append(line)
        elif current_section == 'description':
            description_lines.append(line)
        elif current_section == 'instructions':
            instruction_lines.append(line)
        else:
            es_lines.append(line)

    # Handle instructions at end if needed
    if instruction_lines and not any(translate_instruction(' '.join(instruction_lines)) in '\n'.join(es_lines)):
        # Need to add instruction
        for i, line in enumerate(es_lines):
            if line.startswith('# --solutions--'):
                full_instr = ' '.join(instruction_lines)
                es_lines.insert(i, translate_instruction(full_instr))
                es_lines.insert(i, '')
                break

    write_file(es_path, '\n'.join(es_lines))
    return True

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

    full_instruction = ' '.join(instructions)
    translated_instruction = translate_instruction(full_instruction)

    if code_block:
        es_lines.append(translated_instruction)
        es_lines.append('')
        for line in code_block:
            es_lines.append(line)
        es_lines.append('')
    else:
        es_lines.append(translated_instruction)
        es_lines.append('')

    es_lines.append('# --answers--')
    es_lines.append('')
    for ans in answers:
        translated_ans = translate_answer_type3(ans)
        es_lines.append(f"- {translated_ans}")
    es_lines.append('')

    es_lines.append('# --solutions--')
    es_lines.append('')
    if solution:
        translated_sol = translate_answer_type3(solution)
        es_lines.append(f"- {translated_sol}")
    es_lines.append('')

    write_file(es_path, '\n'.join(es_lines))
    return True

def fix_exercise(en_path, es_path):
    """Fix a Spanish exercise based on English version."""
    en_content = read_file(en_path)
    if not en_content:
        return False

    type_match = re.search(r'exerciseType:\s*(\d+)', en_content)
    if not type_match:
        return False

    exercise_type = int(type_match.group(1))

    if exercise_type == 2:
        return fix_type2_exercise(en_path, es_path)
    elif exercise_type == 3:
        return fix_type3_exercise(en_path, es_path)

    return False

# All files to fix
FILES_TO_FIX = [
    # Type 2 files
    ('/es/swift/conditionalStatements/8.md', '/en/swift/conditionalStatements/8.md'),
    ('/es/swift/conditionalStatements/21.md', '/en/swift/conditionalStatements/21.md'),
    ('/es/swift/conditionalStatements/30.md', '/en/swift/conditionalStatements/30.md'),
    ('/es/swift/conditionalStatements/31.md', '/en/swift/conditionalStatements/31.md'),
    ('/es/swift/conditionalStatements/33.md', '/en/swift/conditionalStatements/33.md'),
    ('/es/swift/conditionalStatements/35.md', '/en/swift/conditionalStatements/35.md'),
    ('/es/swift/variables/11.md', '/en/swift/variables/11.md'),
    ('/es/swift/booleans/3.md', '/en/swift/booleans/3.md'),
    ('/es/swift/arrays/1.md', '/en/swift/arrays/1.md'),
    ('/es/swift/arrays/5.md', '/en/swift/arrays/5.md'),
    ('/es/swift/arrays/9.md', '/en/swift/arrays/9.md'),
    ('/es/swift/arrays/13.md', '/en/swift/arrays/13.md'),
    ('/es/swift/dictionaries/12.md', '/en/swift/dictionaries/12.md'),
    ('/es/swift/forLoops/7.md', '/en/swift/forLoops/7.md'),
    ('/es/swift/forLoops/16.md', '/en/swift/forLoops/16.md'),
    ('/es/swift/whileLoops/8.md', '/en/swift/whileLoops/8.md'),
    ('/es/swift/whileLoops/39.md', '/en/swift/whileLoops/39.md'),
    ('/es/swift/whileLoops/43.md', '/en/swift/whileLoops/43.md'),
    ('/es/swift/functions/2.md', '/en/swift/functions/2.md'),
    ('/es/swift/functions/10.md', '/en/swift/functions/10.md'),
    ('/es/swift/functions/12.md', '/en/swift/functions/12.md'),
    ('/es/swift/classes/3.md', '/en/swift/classes/3.md'),
    ('/es/swift/classes/6.md', '/en/swift/classes/6.md'),
    ('/es/swift/classes/11.md', '/en/swift/classes/11.md'),
    ('/es/swift/stringInterpolation/24.md', '/en/swift/stringInterpolation/24.md'),
    ('/es/swift/output/1.md', '/en/swift/output/1.md'),
    ('/es/swift/output/8.md', '/en/swift/output/8.md'),
    ('/es/javascript/variables/1.md', '/en/javascript/variables/1.md'),
    ('/es/javascript/variables/2.md', '/en/javascript/variables/2.md'),
    ('/es/javascript/variables/3.md', '/en/javascript/variables/3.md'),
    ('/es/javascript/variables/4.md', '/en/javascript/variables/4.md'),
    ('/es/javascript/variables/5.md', '/en/javascript/variables/5.md'),
    ('/es/javascript/variables/9.md', '/en/javascript/variables/9.md'),
    ('/es/javascript/variables/15.md', '/en/javascript/variables/15.md'),
    ('/es/javascript/booleans/12.md', '/en/javascript/booleans/12.md'),
    ('/es/javascript/booleans/13.md', '/en/javascript/booleans/13.md'),
    ('/es/javascript/arithmeticOperators/16.md', '/en/javascript/arithmeticOperators/16.md'),
    ('/es/javascript/arithmeticOperators/17.md', '/en/javascript/arithmeticOperators/17.md'),
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
