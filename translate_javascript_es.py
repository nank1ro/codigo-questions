#!/usr/bin/env python3
"""
Smart translation of JavaScript exercises from English to Spanish.
Uses intelligent pattern matching and translation rules.
Run from the project root directory.

Usage:
    python3 translate_javascript_es.py
"""

import re
import json
from pathlib import Path
from typing import Optional

# Comprehensive translation mappings for JavaScript
TRANSLATIONS = {
    # Exact phrase matches (longest first, for priority)
    "Fill in the blanks": "Completa los espacios en blanco",
    "Fill in the empty spaces": "Completa los espacios vacíos",
    "Sort the items": "Ordena los elementos",
    "Which code produces": "¿Qué código produce",
    "Which code produces the following output": "¿Qué código produce la siguiente salida",
    "When we can use": "¿Cuándo podemos usar",
    "Why is this not": "¿Por qué esto no es",
    "Why is": "¿Por qué es",
    "Why": "¿Por qué",
    "What does this code display": "¿Qué muestra este código",
    "What does this code display in the output": "¿Qué muestra este código en la salida",
    "What does this code display in the console": "¿Qué muestra este código en la consola",
    "What does this code outputs": "¿Qué genera este código",
    "What's the": "¿Cuál es",
    "What is the": "¿Cuál es",
    "Display": "Muestra",
    "Display the string": "Muestra la cadena",
    "Display as output": "Muestra como salida",
    "to get the desired output": "para obtener la salida deseada",
    "to produce the following output": "para producir la siguiente salida",
    "the following output": "la siguiente salida",
    "to display the desired output": "para mostrar la salida deseada",
    "to display the value of a variable": "para mostrar el valor de una variable",
    "as output": "como salida",
    "the value of a variable": "el valor de una variable",
    "after we create the variable": "después de crear la variable",
    "before we create the variable": "antes de crear la variable",
    "before or after we create the variable": "antes o después de crear la variable",
    "there is a space between the words": "hay un espacio entre las palabras",
    "there is a space": "hay un espacio",
    "there is": "hay",
    "contains a space": "contiene un espacio",
    "the words are capitalized": "las palabras están en mayúsculas",
    "there are no double quotes around it": "no hay comillas dobles alrededor de ella",
    "How do we": "¿Cómo",
    "How often": "¿Con qué frecuencia",
    "How many": "¿Cuántos",
    "How": "¿Cómo",
    "for this variable name": "para este nombre de variable",
    "for a": "para",
    "variable name": "nombre de variable",

    # Variable/parameter related
    "Assign to the variable": "Asigna a la variable",
    "Assign to variable": "Asigna a la variable",
    "assign to the variable": "asigna a la variable",
    "Set to the value": "Establece al valor",
    "Set to value": "Establece al valor",
    "Set": "Establece",
    "Store the value": "Almacena el valor",
    "Create a new variable": "Crea una nueva variable",
    "Create a variable": "Crea una variable",
    "Update the value of the variable": "Actualiza el valor de la variable",
    "Update the value of": "Actualiza el valor de",
    "Update": "Actualiza",
    "Declare a variable": "Declara una variable",
    "Declare": "Declara",
    "the variable": "la variable",
    "a variable": "una variable",
    "the value": "el valor",
    "a value": "un valor",

    # Boolean/logic
    "the boolean value": "el valor booleano",
    "a boolean value": "un valor booleano",
    "Booleans represent one of two values": "Los booleanos representan uno de dos valores",
    "Booleans": "Booleanos",
    "You can evaluate any expression": "Puedes evaluar cualquier expresión",
    "get one of two answers": "obtener una de dos respuestas",

    # Description templates
    "is the traditional first program for beginning programming in a new language": "es el programa tradicional para comenzar la programación en un nuevo lenguaje",
    "We use the": "Usamos",
    "function to output data to the standard output device": "función para mostrar datos al dispositivo de salida estándar",
    "function to output data": "función para mostrar datos",
    "to output": "para mostrar",
    "to print": "para imprimir",

    # Variables description
    "Variables are containers for storing data values": "Las variables son contenedores para almacenar valores de datos",
    "Every variable in JavaScript is an object": "Toda variable en JavaScript es un objeto",
    "To create a variable": "Para crear una variable",
    "we need to give it a": "necesitamos darle",
    "keeping in mind that it must not contain spaces": "teniendo en cuenta que no debe contener espacios",
    "A variable is created the moment you first assign a value to it": "Una variable se crea en el momento en que le asignas un valor por primera vez",
    "In JavaScript you declare constants with the": "En JavaScript declaras constantes con",
    "The value of a constant can't be changed once it's set": "El valor de una constante no puede cambiar una vez que se establece",
    "whereas a variable can be set to a different value in the future": "mientras que una variable puede establecerse a un valor diferente en el futuro",
    "An example of a variable creation named": "Un ejemplo de creación de variable llamado",
    "is": "es",
    "In this way we have assigned the value": "De esta manera hemos asignado el valor",
    "to the variable named": "a la variable nombrada",
    "If we print the variable": "Si imprimimos la variable",
    "we get back the number": "obtenemos el número",

    # Variables section specific
    "Variables are called in this way because the value they store can change": "Las variables se llaman así porque el valor que almacenan puede cambiar",
    "We can update": "Podemos actualizar",
    "by using = and giving it a new value": "usando = y dándole un nuevo valor",
    "In JavaScript string variables can be declared using both double quotes and single quotes": "En JavaScript las variables de cadena se pueden declarar usando tanto comillas dobles como simples",
    "both are the same string": "ambas son la misma cadena",
    "If we want a variable name with multiple words, we use": "Si queremos un nombre de variable con múltiples palabras, usamos",
    "It is the practice of writing phrases such that each word in the middle of the phrase begins with a capital letter": "Es la práctica de escribir frases de modo que cada palabra en el medio de la frase comience con una letra mayúscula",
    "Use camel case for this variable name": "Usa camelCase para este nombre de variable",
    "use camel case": "usa camelCase",
    "camelCase": "camelCase",

    # Template literals section
    "Template literals": "Literales de plantilla",
    "Learn how to interpolate strings with different data types": "Aprende cómo interpolar cadenas con diferentes tipos de datos",

    # Output section
    "Output": "Salida",
    "Learn how to output a value": "Aprende cómo mostrar un valor",
    "Your program should print the string": "Tu programa debe imprimir la cadena",

    # Operators
    "Arithmetic Operators": "Operadores Aritméticos",
    "Learn how to perform arithmetic operations on variables and values": "Aprende cómo realizar operaciones aritméticas en variables y valores",
    "Assignment Operators": "Operadores de Asignación",
    "Learn how to assign values to variables": "Aprende cómo asignar valores a variables",
    "Comparison and Logical Operators": "Operadores de Comparación y Lógicos",
    "Learn how to compare values": "Aprende cómo comparar valores",

    # Conditional statements
    "Conditional Statements": "Sentencias Condicionales",
    "Learn how to make decisions": "Aprende cómo tomar decisiones",

    # Loops
    "While Loops": "Bucles While",
    "For Loops": "Bucles For",
    "Learn how to repeat a set of statements": "Aprende cómo repetir un conjunto de sentencias",

    # Arrays
    "Arrays": "Arrays",
    "Learn how to store different values into one variable": "Aprende cómo almacenar diferentes valores en una variable",

    # Objects
    "Objects": "Objetos",
    "Learn how to store values with keys": "Aprende cómo almacenar valores con claves",

    # Functions
    "Functions": "Funciones",
    "Learn how to divide code by specific tasks": "Aprende cómo dividir el código por tareas específicas",

    # Classes
    "Classes": "Clases",
    "Learn object-oriented programming": "Aprende programación orientada a objetos",

    # Assertion descriptions
    "must be equal to": "debe ser igual a",
    "must return": "debe devolver",
    "should print": "debe imprimir",
    "should return the string": "debe devolver la cadena",

    # Multiple choice answers
    "We can't": "No podemos",
    "Never": "Nunca",
    "Only once": "Solo una vez",
    "Only twice": "Solo dos veces",
    "We display it in the console first, then we can update it": "La mostramos en la consola primero, luego podemos actualizarla",
    "By setting the variable to a new value": "Estableciendo la variable a un nuevo valor",
    "As often as we want": "Tan frecuentemente como queramos",
    "Both words need to be capitalized": "Ambas palabras necesitan estar capitalizadas",
    "Because both words need to be capitalized": "Porque ambas palabras necesitan estar capitalizadas",
    "Because it's not descriptive": "Porque no es descriptivo",
    "Because it contains a space between first and name": "Porque contiene un espacio entre first y name",
    "Because it contains a space": "Porque contiene un espacio",

    # Challenges
    "Addition": "Suma",
    "Cajero automático": "Cajero automático",
    "Hello World!": "¡Hola Mundo!",
    "Raindrops": "Gotas de lluvia",
    "Sum of digits": "Suma de dígitos",
    "Two for one": "Dos por uno",
    "100 doors": "100 puertas",
    "Ackermann function": "Función de Ackermann",
    "Multiples of 3 or 5": "Múltiplos de 3 o 5",
    "Even Fibonacci numbers": "Números de Fibonacci pares",
    "Largest prime factor": "Factor primo más grande",
    "Largest palindrome product": "Producto palíndromo más grande",
    "Smallest multiple": "Múltiplo más pequeño",
    "Sum square difference": "Diferencia de suma de cuadrados",
    "10001st prime": "Número primo 10001",
    "Largest product in a series": "Producto más grande en una serie",
    "Special pythagorean triplet": "Triplete pitagórico especial",
    "Summation of primes": "Suma de números primos",
    "Arithmetic mean": "Media aritmética",
    "Roman numeral converter": "Convertidor de números romanos",
    "Leap year": "Año bisiesto",
}


def split_by_code_blocks(text: str) -> list:
    """Split text by code blocks (``` ... ```)."""
    pattern = r'(```[^`]*```)'
    return re.split(pattern, text, flags=re.DOTALL)


def split_by_inline_code(text: str) -> list:
    """Split text by inline code (`...`)."""
    pattern = r'(`[^`]+`)'
    return re.split(pattern, text)


def translate_prose(text: str) -> str:
    """Translate prose text (not code)."""
    if not text or not text.strip():
        return text

    result = text

    # Process translations in order of length (longest first)
    # to avoid substring conflicts
    for english_phrase in sorted(TRANSLATIONS.keys(), key=len, reverse=True):
        spanish_phrase = TRANSLATIONS[english_phrase]

        # Case-sensitive replacement for exact phrases
        result = result.replace(english_phrase, spanish_phrase)

        # Also handle title case (first letter capitalized)
        if english_phrase and english_phrase[0].islower():
            title_english = english_phrase[0].upper() + english_phrase[1:]
            title_spanish = spanish_phrase[0].upper() + spanish_phrase[1:]
            result = result.replace(title_english, title_spanish)

    return result


def process_section(content: str, section_name: str) -> str:
    """Process a section of the markdown file."""
    pattern = rf'(# --{section_name}--\s*\n)(.*?)(?=\n# --|$)'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return content

    section_header = match.group(1)
    section_content = match.group(2)

    # Split by code blocks
    parts = split_by_code_blocks(section_content)
    translated_parts = []

    for part in parts:
        if part.startswith('```'):
            # Keep code blocks as-is
            translated_parts.append(part)
        else:
            # For text, split by inline code and translate non-code parts
            inline_parts = split_by_inline_code(part)
            translated_inline = []
            for inline_part in inline_parts:
                if inline_part.startswith('`') and inline_part.endswith('`'):
                    # Keep inline code as-is
                    translated_inline.append(inline_part)
                else:
                    # Translate prose
                    translated_inline.append(translate_prose(inline_part))
            translated_parts.append(''.join(translated_inline))

    translated_section = ''.join(translated_parts)
    replacement = section_header + translated_section

    # Find the exact match and replace it
    original_match = match.group(0)
    return content.replace(original_match, replacement, 1)


def process_answers(content: str) -> str:
    """Process answers section (translate text, preserve code)."""
    pattern = rf'# --answers--\s*\n(.*?)(?=\n# --|$)'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return content

    answers = match.group(1)
    lines = answers.strip().split('\n')
    translated_lines = []

    for line in lines:
        if line.startswith('- '):
            answer_text = line[2:]

            # Check if it's purely code/operators
            if is_code_element(answer_text):
                translated_lines.append(line)
            elif is_string_literal(answer_text):
                translated_lines.append(line)
            else:
                # Translate if it's text
                translated_text = translate_prose(answer_text)
                translated_lines.append(f'- {translated_text}')
        elif line.startswith('```'):
            translated_lines.append(line)
        else:
            translated_lines.append(line)

    translated = '\n'.join(translated_lines)
    original_section = match.group(0)
    new_section = f'# --answers--\n{translated}'
    return content.replace(original_section, new_section, 1)


def is_code_element(text: str) -> bool:
    """Check if text is a code element (keyword, operator, etc)."""
    code_elements = {
        '==', '=', '!=', '<', '>', '<=', '>=', '+', '-', '*', '/', '%',
        '&', '|', '^', '~', '!', '&&', '||', '++', '--', '+=', '-=',
        '*=', '/=', '%=', '&=', '|=', '^=', '<<', '>>',
        'true', 'false', 'if', 'else', 'for', 'while', 'do', 'switch',
        'case', 'default', 'break', 'continue', 'return', 'void', 'let',
        'const', 'var', 'function', 'class', 'console.log', 'parseInt',
        'console', 'log', 'require', 'assert', '(', ')', '[', ']', '{', '}',
        ',', ';', '.', '->',
    }
    return text.strip() in code_elements or text.strip().startswith('"')


def is_string_literal(text: str) -> bool:
    """Check if text is a string literal."""
    return text.strip().startswith('"') or text.strip().startswith("'")


def translate_file(filepath: Path) -> bool:
    """Translate a single markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Process sections in order
        content = process_section(content, "description")
        content = process_section(content, "instructions")
        content = process_answers(content)
        content = process_section(content, "asserts")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")
        return False


def translate_data_json(filepath: Path) -> bool:
    """Translate data.json files."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, dict):
            for key in data:
                if isinstance(data[key], dict):
                    if 'title' in data[key]:
                        data[key]['title'] = translate_prose(data[key]['title'])
                    if 'description' in data[key]:
                        data[key]['description'] = translate_prose(data[key]['description'])
                    if 'name' in data[key]:
                        data[key]['name'] = translate_prose(data[key]['name'])

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return True
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")
        return False


def main():
    """Main translation process for JavaScript exercises."""
    base_path = Path('/Users/ale/github/codigo-questions/es/javascript')

    if not base_path.exists():
        print(f"ERROR: Path not found: {base_path}")
        return

    # Translate challenges data.json
    challenges_data_json = base_path / 'challenges' / 'data.json'
    if challenges_data_json.exists():
        if translate_data_json(challenges_data_json):
            print(f"✓ Translated: {challenges_data_json.relative_to(base_path)}")
        else:
            print(f"✗ Failed: {challenges_data_json.relative_to(base_path)}")

    # Translate main data.json
    main_data_json = base_path / 'data.json'
    if main_data_json.exists():
        if translate_data_json(main_data_json):
            print(f"✓ Translated: {main_data_json.relative_to(base_path)}")
        else:
            print(f"✗ Failed: {main_data_json.relative_to(base_path)}")

    # Translate all .md files (except _theory.md)
    count = 0
    failed = 0
    md_files = sorted([f for f in base_path.rglob('*.md') if '_theory.md' not in str(f)])

    print(f"\nTranslating {len(md_files)} markdown files...\n")

    for i, md_file in enumerate(md_files, 1):
        if translate_file(md_file):
            count += 1
            print(f"[{i:3d}/{len(md_files)}] ✓ {md_file.relative_to(base_path)}")
        else:
            failed += 1
            print(f"[{i:3d}/{len(md_files)}] ✗ {md_file.relative_to(base_path)}")

    print(f"\n{'='*60}")
    print(f"Translation complete!")
    print(f"✓ Successfully translated: {count}")
    print(f"✗ Failed: {failed}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
