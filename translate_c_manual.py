#!/usr/bin/env python3
"""
Manual translation mapping for C exercises.
This ensures all unique phrases are properly translated.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List

BASE_DIR = Path("/Users/ale/github/codigo-questions")
EN_DIR = BASE_DIR / "en" / "c"
ES_DIR = BASE_DIR / "es" / "c"

# Complete phrase mappings - English to Spanish
PHRASE_MAP = {
    # Output exercises
    '"__Hello, World!__" is the traditional first program for beginning programming in a new language.': '"__Hello, World!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje.',
    'We use the `printf()` function to output data to the standard output device (screen).': 'Usamos la función `printf()` para mostrar datos en el dispositivo de salida estándar (pantalla).',
    'Every C program uses libraries, which give the ability to execute necessary functions, for example the print on the screen function is defined in the `stdio.h` header file.': 'Todo programa en C usa bibliotecas, que dan la capacidad de ejecutar funciones necesarias, por ejemplo la función de impresión en pantalla está definida en el archivo de encabezado `stdio.h`.',
    'The first code which will run will always reside in the main function.': 'El primer código que se ejecutará siempre residirá en la función principal.',
    'To print `Hello, World!` on the screen with C we can write': 'Para imprimir `Hello, World!` en la pantalla con C podemos escribir',
    'Finally we return `0` to indicate that our program was successful': 'Finalmente devolvemos `0` para indicar que nuestro programa fue exitoso',
    'Your program should print the string': 'Tu programa debe imprimir la cadena',
    'on the screen': 'en la pantalla',
    
    # Variables exercises  
    'Variables are containers for storing data values.': 'Las variables son contenedores para almacenar valores de datos.',
    'Every variable in C is an object and like other programming languages, C has commands for declaring a variable.': 'Cada variable en C es un objeto y, como otros lenguajes de programación, C tiene comandos para declarar una variable.',
    'To create a variable, we need to give it a **type** and a **name** keeping in mind that it must not contain spaces.': 'Para crear una variable, necesitamos darle un **tipo** y un **nombre** teniendo en cuenta que no debe contener espacios.',
    'A variable is created the moment you first assign a value to it.': 'Una variable se crea en el momento en que le asignas un valor por primera vez.',
    'An example of a variable creation named': 'Un ejemplo de creación de variable llamada',
    'is': 'es',
    'In this way we have assigned the value': 'De esta manera hemos asignado el valor',
    'to the _integer_ variable named': 'a la variable _entero_ llamada',
    'If we print the variable': 'Si imprimimos la variable',
    'we get back the number': 'obtenemos el número',
    'Variables are called in this way because the value they store can change.': 'Las variables se llaman así porque el valor que almacenan puede cambiar.',
    'We can update': 'Podemos actualizar',
    'by using `=` and giving it a new value.': 'usando `=` y dándole un nuevo valor.',
    'Update the value of the variable': 'Actualiza el valor de la variable',
    'with the number': 'con el número',
    'Assign to the variable': 'Asigna a la variable',
    'the value': 'el valor',
    
    # Arithmetic operators
    'Operators are used to perform operations on variables and values.': 'Los operadores se utilizan para realizar operaciones sobre variables y valores.',
    "Let's start with the arithmetic operators, in particular with the **addition** `+` operator.": 'Empecemos con los operadores aritméticos, en particular con el operador de **suma** `+`.',
    'It is used to add two numbers, like:': 'Se usa para sumar dos números, como:',
    'Calculate the sum between the numbers': 'Calcula la suma entre los números',
    '(in this order)': '(en este orden)',
    'then print the variable': 'luego imprime la variable',
    'What is the ouput of the following code': 'Cuál es la salida del siguiente código',
    
    # Common phrases
    'Write a function that': 'Escribe una función que',
    'returns the string': 'devuelva la cadena',
    'must be equal to': 'debe ser igual a',
    'can you order these lines into a functional script': '¿puedes ordenar estas líneas en un script funcional',
    
    # Learning descriptions
    'Learn how to output a value': 'Aprende cómo mostrar un valor',
    'Learn how to format strings with different data types': 'Aprende cómo formatear cadenas con diferentes tipos de datos',
    'Learn how to store values in a variable': 'Aprende cómo almacenar valores en una variable',
    'Learn how to evaluate any expression': 'Aprende cómo evaluar cualquier expresión',
    'Learn how to perform arithmetic operations on variables and values': 'Aprende cómo realizar operaciones aritméticas sobre variables y valores',
    'Learn how to assign values to variables': 'Aprende cómo asignar valores a variables',
    'Learn how to compare values': 'Aprende cómo comparar valores',
    'Learn how to make decisions': 'Aprende cómo tomar decisiones',
    'Learn how to repeat a set of statements': 'Aprende cómo repetir un conjunto de sentencias',
    'Learn how to store different values into one variable': 'Aprende cómo almacenar diferentes valores en una variable',
    'Learn how to divide code by specific tasks': 'Aprende cómo dividir el código en tareas específicas',
    
    # Titles
    'Output': 'Salida',
    'Formatted Strings': 'Cadenas Formateadas',
    'Variables': 'Variables',
    'Booleans': 'Booleanos',
    'Arithmetic Operators': 'Operadores Aritméticos',
    'Assignment Operators': 'Operadores de Asignación',
    'Relational and Boolean Operators': 'Operadores Relacionales y Booleanos',
    'Conditional Statements': 'Sentencias Condicionales',
    'While Loops': 'Bucles While',
    'For Loops': 'Bucles For',
    'Arrays': 'Arreglos',
    'Functions': 'Funciones',
    
    # Challenge names
    'Addition': 'Suma',
    'ATM': 'Cajero Automático',
    'Raindrops': 'Gotas de Lluvia',
    'Sum of digits': 'Suma de dígitos',
    'Two for one': 'Dos por uno',
    '100 doors': '100 puertas',
    'Ackermann function': 'Función de Ackermann',
    'Arithmetic mean': 'Media aritmética',
    'FizzBuzz': 'FizzBuzz',
    'Roman numeral converter': 'Conversor de números romanos',
    'Leap year': 'Año bisiesto',
}

# Variable translations
VAR_MAP = {
    'sum': 'suma',
    'product': 'producto',
    'count': 'conteo',
    'result': 'resultado',
    'value': 'valor',
    'total': 'total',
    'number': 'numero',
    'numbers': 'numeros',
    'average': 'promedio',
    'digit': 'digito',
    'digits': 'digitos',
}

def apply_translations(text: str) -> str:
    """Apply all translations to text, longest first."""
    result = text
    # Sort by length descending to match longer phrases first
    for en, es in sorted(PHRASE_MAP.items(), key=len, reverse=True):
        # Case-sensitive replacement
        if en in result:
            result = result.replace(en, es)
    return result

def translate_content(content: str) -> str:
    """Translate file content properly."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    in_before_seed = False
    current_section = None
    
    for line in lines:
        stripped = line.strip()
        
        # Track sections
        if stripped in ['# --description--', '# --instructions--', '# --seed--',
                       '# --answers--', '# --solutions--', '# --asserts--',
                       '# --before-seed--', '# --after-seed--',
                       '# --before-asserts--', '# --after-asserts--',
                       '# --output--']:
            current_section = stripped
            in_code_block = False
            result.append(line)
            continue
        
        # Track code blocks
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
        # Translate prose sections
        if not in_code_block and current_section in ['# --description--', '# --instructions--', '# --asserts--', '# --answers--']:
            result.append(apply_translations(line))
        elif not in_code_block and current_section == '# --seed--' and not stripped.startswith('#include') and not stripped.startswith('int') and not stripped.startswith('char') and not stripped.startswith('float') and not stripped.startswith('double') and not stripped.startswith('void') and not stripped.startswith('for') and not stripped.startswith('while') and not stripped.startswith('if') and not stripped.startswith('return'):
            # Translate comments in seed but not code
            result.append(apply_translations(line))
        else:
            result.append(line)
    
    return '\n'.join(result)

def translate_file(src: Path, dest: Path):
    """Translate a single file."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    content = src.read_text(encoding='utf-8')
    
    if src.suffix == '.md':
        translated = translate_content(content)
        dest.write_text(translated, encoding='utf-8')
    elif src.name == 'data.json':
        # Translate JSON values
        data = json.loads(content)
        def translate_json(obj):
            if isinstance(obj, str):
                return apply_translations(obj)
            elif isinstance(obj, dict):
                return {k: translate_json(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [translate_json(i) for i in obj]
            return obj
        translated_data = translate_json(data)
        dest.write_text(json.dumps(translated_data, indent=4, ensure_ascii=False) + '\n', encoding='utf-8')
    else:
        dest.write_text(content, encoding='utf-8')

def process_all():
    """Process all C exercise files."""
    # Main data.json
    translate_file(EN_DIR / 'data.json', ES_DIR / 'data.json')
    print("Translated: data.json")
    
    dirs = ['output', 'formattedStrings', 'variables', 'booleans',
            'arithmeticOperators', 'assignmentOperators', 'relationBooleanOperators',
            'conditionalStatements', 'whileLoops', 'forLoops', 'arrays',
            'functions', 'challenges']
    
    total = 0
    for dirname in dirs:
        src = EN_DIR / dirname
        dst = ES_DIR / dirname
        if src.exists():
            for item in src.iterdir():
                if item.is_file():
                    translate_file(item, dst / item.name)
                    total += 1
            print(f"Translated {dirname}: {len(list(src.iterdir()))} files")
    
    print(f"\nTotal: {total} files translated")

if __name__ == '__main__':
    process_all()
