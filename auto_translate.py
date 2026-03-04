#!/usr/bin/env python3
"""
Automatic translation of C exercises from English to Spanish
Run this script from the proyecto root directory to translate all remaining files.

Usage:
    python3 auto_translate.py

This script will:
1. Translate all .md files in es/c/ (except _theory.md)
2. Preserve code blocks, inline code, and frontmatter
3. Create backup of original files (optional)
"""

import re
import json
from pathlib import Path
from typing import Optional

class CExerciseTranslator:
    def __init__(self):
        self.translations = {
            # Instructions
            "Fill in the blanks": "Completa los espacios en blanco",
            "Fill in the empty spaces": "Completa los espacios vacíos",
            "Display": "Muestra",
            "Sort the items": "Ordena los elementos",
            "Which code produces": "¿Cuál código produce",
            "When we can use": "¿Cuándo podemos usar",
            "Why is this not": "¿Por qué esto no es",
            "to get the desired output": "para obtener la salida deseada",
            "to produce the following output": "para producir la siguiente salida",
            "as output": "como salida",
            "Print the name using": "Imprime el nombre usando",
            "Assign to the variable": "Asigna a la variable",
            "Create a new variable": "Crea una nueva variable",
            "Update the value of": "Actualiza el valor de",

            # Descriptions
            "is the traditional first program": "es el programa tradicional",
            "function to output data": "función para mostrar datos",
            "function to display": "función para mostrar",
            "Every C program uses libraries": "Cada programa C usa bibliotecas",
            "The first code which will run": "El primer código que se ejecutará",
            "Variables are containers for storing": "Las variables son contenedores para almacenar",
            "Every variable in C is an object": "Cada variable en C es un objeto",
            "We can also give variables": "También podemos dar a las variables",
            "Variables are called in this way because": "Las variables se llaman de esta manera porque",
            "the value they store can change": "el valor que almacenan puede cambiar",
            "We can update": "Podemos actualizar",
            "by using = and giving it a new value": "usando = y dándole un nuevo valor",
            "Formatted strings allow us": "Las cadenas formateadas nos permiten",
            "In C we use the printf function": "En C usamos la función printf",
            "is used to display a": "se usa para mostrar",
            "is used to display an": "se usa para mostrar",
            "single character": "un solo carácter",
            "array of characters": "arreglo de caracteres",
            "or a string": "o una cadena",
            "to display an integer": "para mostrar un entero",

            # Asserts
            "must be equal to": "debe ser igual a",
            "must return": "debe devolver",
            "should print": "debe imprimir",
            "should return the string": "debe devolver la cadena",
            "The function should return": "La función debe devolver",

            # Multiple choice answers - Output
            "Before or after we create the variable": "Antes o después de crear la variable",
            "Before we create the variable": "Antes de crear la variable",
            "After we create the variable": "Después de crear la variable",
            "Because there is a space between the words": "Porque hay un espacio entre las palabras",
            "Because the words are capitalized": "Porque las palabras están en mayúsculas",
            "Because there are no double quotes around it": "Porque no hay comillas dobles alrededor de ella",

            # Booleans
            "Booleans represent one of two values": "Los booleanos representan uno de dos valores",
            "You can evaluate any expression": "Puedes evaluar cualquier expresión",
            "get one of two answers": "obtener una de dos respuestas",
            "the boolean value": "el valor booleano",
            "a boolean value": "un valor booleano",

            # Arithmetic
            "The multiplication operator": "El operador de multiplicación",
            "The division operator": "El operador de división",
            "The remainder operator": "El operador de resto",
            "performs multiplication": "realiza la multiplicación",
            "performs division": "realiza la división",
            "to multiply": "para multiplicar",
            "to divide": "para dividir",

            # Assignment
            "The += operator": "El operador +=",
            "The -= operator": "El operador -=",
            "The *= operator": "El operador *=",
            "The /= operator": "El operador /=",
            "adds a value": "añade un valor",
            "subtracts a value": "resta un valor",
            "multiplies by a value": "multiplica por un valor",
            "divides by a value": "divide por un valor",

            # Relations
            "equal to": "igual a",
            "not equal to": "no igual a",
            "less than": "menor que",
            "greater than": "mayor que",
            "The == operator": "El operador ==",
            "The != operator": "El operador !=",
            "The < operator": "El operador <",
            "The > operator": "El operador >",
            "The <= operator": "El operador <=",
            "The >= operator": "El operador >=",
            "stating whether two expressions are": "indicando si dos expresiones son",
            "returns true": "devuelve verdadero",
            "returns false": "devuelve falso",

            # Conditionals
            "If x is equal to": "Si x es igual a",
            "If x is greater than": "Si x es mayor que",
            "If x is less than": "Si x es menor que",
            "if the condition is true": "si la condición es verdadera",
            "if the condition is false": "si la condición es falsa",
            "The if statement": "La declaración if",
            "The else statement": "La declaración else",
            "is used to make a decision": "se usa para tomar una decisión",

            # Loops
            "The while loop": "El bucle while",
            "The for loop": "El bucle for",
            "is used to execute": "se usa para ejecutar",
            "as long as a condition is": "mientras una condición sea",
            "You can use the break statement": "Puedes usar la declaración break",
            "to exit the loop": "para salir del bucle",
            "The loop will": "El bucle",
            "counter": "contador",
            "iterate": "iterar",

            # Arrays
            "An array is a": "Un arreglo es",
            "collection of elements": "colección de elementos",
            "of the same type": "del mismo tipo",
            "The first element": "El primer elemento",
            "has an index of": "tiene un índice de",
            "The length of": "La longitud de",

            # Functions
            "A function is a": "Una función es",
            "block of code": "bloque de código",
            "that performs a": "que realiza una",
            "specific task": "tarea específica",
            "You can call": "Puedes llamar",
            "many times": "muchas veces",
            "A function can": "Una función puede",
            "parameters": "parámetros",
            "arguments": "argumentos",
            "return a value": "devolver un valor",
            "return type": "tipo de retorno",
            "function definition": "definición de función",
            "function call": "llamada de función",
        }

    def translate_text(self, text: str) -> str:
        """Translate text using dictionary mappings."""
        if not text or not isinstance(text, str):
            return text

        result = text
        # Sort by length (longest first) to match longer phrases before shorter ones
        for english, spanish in sorted(self.translations.items(), key=lambda x: len(x[0]), reverse=True):
            result = result.replace(english, spanish)
            # Try capitalized versions
            if english and english[0].islower():
                cap_en = english[0].upper() + english[1:]
                cap_es = spanish[0].upper() + spanish[1:]
                result = result.replace(cap_en, cap_es)

        return result

    def extract_section(self, content: str, section_name: str) -> Optional[str]:
        """Extract a section from markdown."""
        pattern = rf'# --{section_name}--\s*\n(.*?)(?=\n# --|$)'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1) if match else None

    def is_code_only(self, text: str) -> bool:
        """Check if text is code (operators, keywords, etc)."""
        code_elements = {
            '==', '=', '!=', '<', '>', '<=', '>=', '+', '-', '*', '/', '%',
            '&', '|', '^', '~', '!', '&&', '||', '++', '--', '+=', '-=', '*=', '/=',
            'true', 'false', 'if', 'else', 'for', 'while', 'do', 'switch', 'case',
            'printf', 'scanf', 'int', 'char', 'float', 'double', 'bool', 'void',
        }
        return text.strip() in code_elements

    def translate_section(self, content: str, section_name: str) -> str:
        """Translate a section, preserving code blocks."""
        section = self.extract_section(content, section_name)
        if not section:
            return content

        # Split by code blocks
        parts = re.split(r'(```[^`]*```)', section, flags=re.DOTALL)
        translated = []

        for part in parts:
            if part.startswith('```'):
                # Keep code blocks
                translated.append(part)
            else:
                # Split by inline code
                inline_parts = re.split(r'(`[^`]+`)', part)
                translated_inline = []
                for inline_part in inline_parts:
                    if inline_part.startswith('`') and inline_part.endswith('`'):
                        # Keep inline code
                        translated_inline.append(inline_part)
                    else:
                        # Translate text
                        translated_inline.append(self.translate_text(inline_part))
                translated.append(''.join(translated_inline))

        new_section = ''.join(translated)
        pattern = rf'(# --{section_name}--\s*\n){re.escape(section)}'
        return re.sub(pattern, rf'\1{new_section}', content, count=1)

    def translate_answers(self, content: str) -> str:
        """Translate answers section (only text, not code)."""
        answers = self.extract_section(content, "answers")
        if not answers:
            return content

        lines = answers.split('\n')
        translated_lines = []

        for line in lines:
            if line.startswith('- '):
                text = line[2:]
                # Skip if it's code
                if self.is_code_only(text) or text.strip().startswith('"'):
                    translated_lines.append(line)
                else:
                    # Translate
                    translated_lines.append(f'- {self.translate_text(text)}')
            else:
                translated_lines.append(line)

        new_answers = '\n'.join(translated_lines)
        pattern = rf'(# --answers--\s*\n){re.escape(answers)}'
        return re.sub(pattern, rf'\1{new_answers}', content, count=1)

    def translate_file(self, filepath: Path) -> bool:
        """Translate a single file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Translate each section
            content = self.translate_section(content, "description")
            content = self.translate_section(content, "instructions")
            content = self.translate_answers(content)
            content = self.translate_section(content, "asserts")

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            return True
        except Exception as e:
            print(f"ERROR {filepath}: {e}")
            return False

def main():
    base_path = Path('es/c')
    translator = CExerciseTranslator()

    count = 0
    errors = 0

    # Get all .md files except _theory.md
    files = sorted([f for f in base_path.rglob('*.md') if '_theory.md' not in str(f)])

    print(f"Found {len(files)} files to translate\n")

    for i, filepath in enumerate(files, 1):
        if translator.translate_file(filepath):
            print(f"[{i:3d}/{len(files)}] ✓ {filepath.relative_to(base_path)}")
            count += 1
        else:
            print(f"[{i:3d}/{len(files)}] ✗ {filepath.relative_to(base_path)}")
            errors += 1

    print(f"\n✓ Translated: {count}")
    print(f"✗ Errors: {errors}")
    print("\nTranslation complete!")

if __name__ == '__main__':
    main()
