#!/usr/bin/env python3
"""
Smart translation of C exercises from English to Spanish.
Uses intelligent pattern matching and translation rules.
"""

import re
import json
from pathlib import Path
from typing import Tuple

# Comprehensive translation mappings
TRANSLATIONS = {
    # Exact phrase matches (longest first, for priority)
    "Fill in the blanks": "Completa los espacios en blanco",
    "Fill in the empty spaces": "Completa los espacios vacíos",
    "Sort the items": "Ordena los elementos",
    "Which code produces": "¿Cuál código produce",
    "When we can use": "¿Cuándo podemos usar",
    "Why is this not": "¿Por qué esto no es",
    "Display": "Muestra",
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
    "the words are capitalized": "las palabras están en mayúsculas",
    "there are no double quotes around it": "no hay comillas dobles alrededor de ella",

    # Variable/parameter related
    "Assign to the variable": "Asigna a la variable",
    "Assign to variable": "Asigna a la variable",
    "assign to the variable": "asigna a la variable",
    "the variable": "la variable",
    "a variable": "una variable",
    "the value": "el valor",
    "a value": "un valor",

    # Boolean/logic
    "the boolean value": "el valor booleano",
    "a boolean value": "un valor booleano",
    "Booleans represent one of two values": "Los booleanos representan uno de dos valores",
    "You can evaluate any expression": "Puedes evaluar cualquier expresión",
    "get one of two answers": "obtener una de dos respuestas",

    # Description templates
    "is the traditional first program for beginning programming in a new language": "es el programa tradicional de principiante para comenzar la programación en un nuevo lenguaje",
    "We use the": "Usamos",
    "function to output data to the standard output device": "función para mostrar datos al dispositivo de salida estándar",
    "Every C program uses libraries": "Cada programa C usa bibliotecas",
    "which give the ability to execute necessary functions": "que dan la capacidad de ejecutar funciones necesarias",
    "the print on the screen function is defined in the": "la función de impresión en pantalla se define en",
    "header file": "archivo de encabezado",
    "The first code which will run will always reside in the main function": "El primer código que se ejecutará siempre residirá en la función main",
    "To print": "Para imprimir",
    "on the screen with C we can write": "en la pantalla con C podemos escribir",
    "Finally we return": "Finalmente devolvemos",
    "to indicate that our program was successful": "para indicar que nuestro programa fue exitoso",

    # Variables description
    "Variables are containers for storing data values": "Las variables son contenedores para almacenar valores de datos",
    "Every variable in C is an object": "Cada variable en C es un objeto",
    "like other programming languages": "como otros lenguajes de programación",
    "has commands for declaring a variable": "tiene comandos para declarar una variable",
    "To create a variable": "Para crear una variable",
    "we need to give it a": "necesitamos darle",
    "keeping in mind that it must not contain spaces": "teniendo en cuenta que no debe contener espacios",
    "A variable is created the moment you first assign a value to it": "Una variable se crea en el momento en que le asignas un valor por primera vez",
    "An example of a variable creation named": "Un ejemplo de creación de variable llamado",
    "is": "es",
    "In this way we have assigned the value": "De esta manera hemos asignado el valor",
    "to the _integer_ variable named": "a la variable _entero_ nombrada",
    "If we print the variable": "Si imprimimos la variable",
    "we get back the number": "obtenemos el número",

    # Operators
    "Arithmetic Operators": "Operadores Aritméticos",
    "Learn how to perform arithmetic operations on variables and values": "Aprende cómo realizar operaciones aritméticas en variables y valores",
    "Assignment Operators": "Operadores de Asignación",
    "Learn how to assign values to variables": "Aprende cómo asignar valores a variables",
    "Relational and Boolean Operators": "Operadores Relacionales y Booleanos",
    "Learn how to compare values": "Aprende cómo comparar valores",

    # Loops
    "While Loops": "Bucles While",
    "For Loops": "Bucles For",
    "Learn how to repeat a set of statements": "Aprende cómo repetir un conjunto de declaraciones",

    # Arrays
    "Learn how to store different values into one variable": "Aprende cómo almacenar diferentes valores en una variable",

    # Functions
    "Learn how to divide code by specific tasks": "Aprende cómo dividir código por tareas específicas",

    # Common single words
    "variable": "variable",
    "value": "valor",
    "variable": "variable",
    "type": "tipo",
    "number": "número",
    "string": "cadena",
    "output": "salida",
    "true": "verdadero",
    "false": "falso",
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

def process_section(content: str, section_name: str, translate_fn=None) -> str:
    """Process a section of the markdown file."""
    if translate_fn is None:
        translate_fn = translate_prose

    pattern = rf'(# --{section_name}--\s*\n)(.*?)(?=\n# --|$)'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return content

    section_header = match.group(1)
    section_content = match.group(2)

    # Split by code blocks
    parts = split_by_code_blocks(section_content)
    translated_parts = []

    for i, part in enumerate(parts):
        if part.startswith('```'):
            # Keep code blocks as-is
            translated_parts.append(part)
        else:
            # For text, split by inline code and translate non-code parts
            inline_parts = split_by_inline_code(part)
            translated_inline = []
            for j, inline_part in enumerate(inline_parts):
                if inline_part.startswith('`') and inline_part.endswith('`'):
                    # Keep inline code as-is
                    translated_inline.append(inline_part)
                else:
                    # Translate prose
                    translated_inline.append(translate_fn(inline_part))
            translated_parts.append(''.join(translated_inline))

    translated_section = ''.join(translated_parts)
    replacement = section_header + translated_section

    # Find the exact match and replace it
    original_match = match.group(0)
    return content.replace(original_match, replacement, 1)

def process_answers(content: str) -> str:
    """Process answers section (translate text, preserve code)."""
    answers = extract_section(content, "answers")
    if not answers:
        return content

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
    original_section = f'# --answers--\n{answers}'
    new_section = f'# --answers--\n{translated}'
    return content.replace(original_section, new_section, 1)

def is_code_element(text: str) -> bool:
    """Check if text is a code element (keyword, operator, etc)."""
    code_elements = {
        '==', '=', '!=', '<', '>', '<=', '>=', '+', '-', '*', '/', '%',
        '&', '|', '^', '~', '!', '&&', '||', '++', '--', '+=', '-=',
        '*=', '/=', '%=', '&=', '|=', '^=', '<<', '>>',
        'true', 'false', 'if', 'else', 'for', 'while', 'do', 'switch',
        'case', 'default', 'break', 'continue', 'return', 'void', 'int',
        'char', 'float', 'double', 'bool', 'printf', 'scanf', 'const',
        'static', 'struct', 'union', 'enum', '(', ')', '[', ']', '{', '}',
        ',', ';', '.', '->',
    }
    return text.strip() in code_elements or text.strip().startswith('"')

def is_string_literal(text: str) -> bool:
    """Check if text is a string literal."""
    return text.strip().startswith('"') or text.strip().startswith("'")

def extract_section(content: str, section_name: str) -> str:
    """Extract section content."""
    pattern = rf'# --{section_name}--\s*\n(.*?)(?=\n# --|$)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1) if match else None

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

def translate_challenges_data_json(filepath: Path) -> bool:
    """Translate challenges data.json."""
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

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return True
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")
        return False

def main():
    """Main translation process."""
    base_path = Path('/Users/ale/github/codigo-questions/es/c')

    # Translate challenges data.json
    challenges_data_json = base_path / 'challenges' / 'data.json'
    if challenges_data_json.exists():
        translate_challenges_data_json(challenges_data_json)
        print(f"Translated: {challenges_data_json}")

    # Translate all .md files (except _theory.md)
    count = 0
    total_files = sum(1 for _ in base_path.rglob('*.md') if '_theory.md' not in str(_))

    for md_file in sorted(base_path.rglob('*.md')):
        if '_theory.md' in str(md_file):
            continue

        if translate_file(md_file):
            count += 1
            print(f"[{count}/{total_files}] {md_file.relative_to(base_path)}")
        else:
            print(f"[FAILED] {md_file.relative_to(base_path)}")

    print(f"\nTranslation complete! Processed {count} markdown files.")

if __name__ == '__main__':
    main()
