#!/usr/bin/env python3
"""
Translate C exercises from English to Spanish.
Processes description, instructions, answers, and asserts text sections.
Preserves code blocks, frontmatter, and spacing.
"""

import os
import re
import json
from pathlib import Path

# Translation dictionary with common terms and phrases
TRANSLATIONS = {
    # Common phrases
    "Learn how to": "Aprende cómo",
    "output a value": "mostrar un valor",
    "format strings with different data types": "formatear cadenas con diferentes tipos de datos",
    "store values in a variable": "almacenar valores en una variable",
    "evaluate any expression": "evaluar cualquier expresión",
    "perform arithmetic operations on variables and values": "realizar operaciones aritméticas en variables y valores",
    "assign values to variables": "asignar valores a variables",
    "compare values": "comparar valores",
    "make decisions": "tomar decisiones",
    "repeat a set of statements": "repetir un conjunto de declaraciones",
    "store different values into one variable": "almacenar diferentes valores en una variable",
    "divide code by specific tasks": "dividir código por tareas específicas",

    # General terms
    "container": "contenedor",
    "containers": "contenedores",
    "storing": "almacenar",
    "variable": "variable",
    "variables": "variables",
    "value": "valor",
    "values": "valores",
    "data": "datos",
    "data types": "tipos de datos",
    "function": "función",
    "functions": "funciones",
    "program": "programa",
    "programming": "programación",
    "language": "lenguaje",
    "operation": "operación",
    "operations": "operaciones",
    "operator": "operador",
    "operators": "operadores",
    "statement": "declaración",
    "statements": "declaraciones",
    "condition": "condición",
    "conditions": "condiciones",
    "loop": "bucle",
    "loops": "bucles",
    "array": "arreglo",
    "arrays": "arreglos",
    "element": "elemento",
    "elements": "elementos",
    "index": "índice",
    "indices": "índices",
    "parameter": "parámetro",
    "parameters": "parámetros",
    "argument": "argumento",
    "arguments": "argumentos",
    "return": "devolver",
    "returns": "devuelve",
    "result": "resultado",
    "results": "resultados",
    "output": "salida",
    "input": "entrada",
    "string": "cadena",
    "strings": "cadenas",
    "character": "carácter",
    "characters": "caracteres",
    "integer": "entero",
    "integers": "enteros",
    "number": "número",
    "numbers": "números",
    "boolean": "booleano",
    "booleans": "booleanos",
    "true": "verdadero",
    "false": "falso",
    "expression": "expresión",
    "expressions": "expresiones",
    "evaluate": "evaluar",
    "evaluates": "evalúa",
    "compare": "comparar",
    "compares": "compara",
    "equal": "igual",
    "equality": "igualdad",
    "greater": "mayor",
    "less": "menor",
    "sum": "suma",
    "subtract": "restar",
    "multiply": "multiplicar",
    "divide": "dividir",
    "increment": "incremento",
    "decrement": "decremento",
    "assign": "asignar",
    "assignment": "asignación",
    "print": "imprimir",
    "prints": "imprime",
    "display": "mostrar",
    "show": "mostrar",
    "define": "definir",
    "definition": "definición",
    "declare": "declarar",
    "declaration": "declaración",
    "initialize": "inicializar",
    "initialization": "inicialización",
    "type": "tipo",
    "types": "tipos",
    "name": "nombre",
    "space": "espacio",
    "must": "debe",
    "should": "debería",
    "required": "requerido",
    "optional": "opcional",
    "example": "ejemplo",
    "examples": "ejemplos",
    "code": "código",
    "instruction": "instrucción",
    "instructions": "instrucciones",
    "complete": "completar",
    "fill": "llenar",
    "placeholder": "marcador de posición",
    "assign to the variable": "asigna a la variable",
    "assign to variable": "asigna a la variable",
    "print the": "imprime",
    "print a": "imprime",
    "check if": "verifica si",
    "checking if": "verificando si",
}

def translate_text(text, preserve_case=False):
    """
    Translate text using the translation dictionary.
    Handles case-insensitive matching while preserving original case in output.
    """
    if not text:
        return text

    # Create working copy
    result = text

    # Replace multi-word phrases first (longest first to avoid partial matches)
    sorted_phrases = sorted(TRANSLATIONS.keys(), key=len, reverse=True)

    for english_phrase in sorted_phrases:
        spanish_phrase = TRANSLATIONS[english_phrase]

        # Handle various case combinations
        # Original case
        result = result.replace(english_phrase, spanish_phrase)
        # Title case
        result = result.replace(english_phrase.title(), spanish_phrase.title())
        # Capitalize first letter
        if english_phrase and english_phrase[0].isupper():
            result = result.replace(english_phrase[0].upper() + english_phrase[1:],
                                  spanish_phrase[0].upper() + spanish_phrase[1:])

    return result

def extract_section(content, section_name):
    """Extract section content from markdown."""
    pattern = rf'# --{section_name}--\s*\n(.*?)(?=\n# --|$)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1) if match else None

def process_description(content):
    """Process and translate description section."""
    description = extract_section(content, "description")
    if not description:
        return content

    # Split by code blocks
    parts = re.split(r'(```[^`]*```)', description, flags=re.DOTALL)
    translated_parts = []

    for i, part in enumerate(parts):
        if part.startswith('```'):
            # Keep code blocks as-is
            translated_parts.append(part)
        else:
            # Translate text, preserve backticks for inline code
            # Split by inline code
            inline_parts = re.split(r'(`[^`]+`)', part)
            translated_inline = []
            for j, inline_part in enumerate(inline_parts):
                if inline_part.startswith('`') and inline_part.endswith('`'):
                    # Keep inline code as-is
                    translated_inline.append(inline_part)
                else:
                    # Translate text
                    translated_inline.append(translate_text(inline_part))
            translated_parts.append(''.join(translated_inline))

    translated = ''.join(translated_parts)
    return content.replace(f'# --description--\n{description}', f'# --description--\n{translated}')

def process_instructions(content):
    """Process and translate instructions section."""
    instructions = extract_section(content, "instructions")
    if not instructions:
        return content

    # Split by code blocks
    parts = re.split(r'(```[^`]*```)', instructions, flags=re.DOTALL)
    translated_parts = []

    for i, part in enumerate(parts):
        if part.startswith('```'):
            translated_parts.append(part)
        else:
            inline_parts = re.split(r'(`[^`]+`)', part)
            translated_inline = []
            for j, inline_part in enumerate(inline_parts):
                if inline_part.startswith('`') and inline_part.endswith('`'):
                    translated_inline.append(inline_part)
                else:
                    translated_inline.append(translate_text(inline_part))
            translated_parts.append(''.join(translated_inline))

    translated = ''.join(translated_parts)
    return content.replace(f'# --instructions--\n{instructions}', f'# --instructions--\n{translated}')

def process_answers(content):
    """Process and translate answers section (only text, not code)."""
    answers = extract_section(content, "answers")
    if not answers:
        return content

    lines = answers.split('\n')
    translated_lines = []

    for line in lines:
        if line.startswith('- '):
            # Extract answer text
            answer_text = line[2:]

            # Don't translate if it looks like code (operators, keywords, etc)
            # Check if it's purely punctuation or operators
            if answer_text.strip() in ['==', '=', '!=', '<', '>', '<=', '>=', '+', '-', '*', '/', '%', '&', '|', '^', '~', '!', '&&', '||', '++', '--', '+=',' -=', '*=', '/=', '%=', '&=', '|=', '^=', '<<', '>>', 'true', 'false', 'if', 'else', 'for', 'while', 'do', 'switch', 'case', 'default', 'break', 'continue', 'return', 'void', 'int', 'char', 'float', 'double', 'bool', 'printf', 'scanf', 'const', 'static', 'struct', 'union', 'enum']:
                translated_lines.append(line)
            elif answer_text.strip() in ['Hello, ', 'C!', '"Hello, ', '"true"', 'C"', 'Hello, ', 'World!', '"Hello, World!"']:
                # Keep string literals as-is
                translated_lines.append(line)
            else:
                # Translate if it's text
                translated_text = translate_text(answer_text)
                translated_lines.append(f'- {translated_text}')
        else:
            translated_lines.append(line)

    translated = '\n'.join(translated_lines)
    return content.replace(f'# --answers--\n{answers}', f'# --answers--\n{translated}')

def process_asserts(content):
    """Process and translate asserts text descriptions."""
    asserts = extract_section(content, "asserts")
    if not asserts:
        return content

    # Split by code blocks
    parts = re.split(r'(```[^`]*```)', asserts, flags=re.DOTALL)
    translated_parts = []

    for i, part in enumerate(parts):
        if part.startswith('```'):
            translated_parts.append(part)
        else:
            inline_parts = re.split(r'(`[^`]+`)', part)
            translated_inline = []
            for j, inline_part in enumerate(inline_parts):
                if inline_part.startswith('`') and inline_part.endswith('`'):
                    translated_inline.append(inline_part)
                else:
                    translated_inline.append(translate_text(inline_part))
            translated_parts.append(''.join(translated_inline))

    translated = ''.join(translated_parts)
    return content.replace(f'# --asserts--\n{asserts}', f'# --asserts--\n{translated}')

def translate_file(filepath):
    """Translate a single exercise file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Process each section
    content = process_description(content)
    content = process_instructions(content)
    content = process_answers(content)
    content = process_asserts(content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def translate_data_json(filepath):
    """Translate data.json file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key in data:
        if 'title' in data[key]:
            data[key]['title'] = translate_text(data[key]['title'])
        if 'description' in data[key]:
            data[key]['description'] = translate_text(data[key]['description'])

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return True

def main():
    """Main translation process."""
    base_path = Path('/Users/ale/github/codigo-questions/es/c')

    # Translate data.json
    data_json_path = base_path / 'data.json'
    if data_json_path.exists():
        translate_data_json(data_json_path)
        print(f"Translated: {data_json_path}")

    # Translate challenges data.json
    challenges_data_json = base_path / 'challenges' / 'data.json'
    if challenges_data_json.exists():
        translate_data_json(challenges_data_json)
        print(f"Translated: {challenges_data_json}")

    # Translate all .md files (except _theory.md)
    count = 0
    for md_file in sorted(base_path.rglob('*.md')):
        if '_theory.md' in str(md_file):
            continue

        try:
            translate_file(md_file)
            print(f"Translated: {md_file}")
            count += 1
        except Exception as e:
            print(f"ERROR translating {md_file}: {e}")

    print(f"\nTranslation complete! Processed {count} markdown files.")

if __name__ == '__main__':
    main()
