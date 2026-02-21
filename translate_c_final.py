#!/usr/bin/env python3
"""
Comprehensive translation for C exercises.
Uses full content replacement for complete, accurate translations.
"""

import os
import json
from pathlib import Path
from typing import Dict

BASE_DIR = Path("/Users/ale/github/codigo-questions")
EN_DIR = BASE_DIR / "en" / "c"
ES_DIR = BASE_DIR / "es" / "c"

# Comprehensive translation dictionary
TRANSLATIONS = {
    # ===== OUTPUT EXERCISES =====
    'output/1.md': {
        '"__Hello, World!__" is the traditional first program for beginning programming in a new language.': '"__Hello, World!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje.',
        'We use the `printf()` function to output data to the standard output device (screen).': 'Usamos la función `printf()` para mostrar datos en el dispositivo de salida estándar (pantalla).',
        'Every C program uses libraries, which give the ability to execute necessary functions, for example the print on the screen function is defined in the `stdio.h` header file.': 'Todo programa en C usa bibliotecas, que dan la capacidad de ejecutar funciones necesarias, por ejemplo la función de impresión en pantalla está definida en el archivo de encabezado `stdio.h`.',
        'The first code which will run will always reside in the main function.': 'El primer código que se ejecutará siempre residirá en la función principal.',
        'To print `Hello, World!` on the screen with C we can write': 'Para imprimir `Hello, World!` en la pantalla con C podemos escribir',
        'Finally we return `0` to indicate that our program was successful': 'Finalmente devolvemos `0` para indicar que nuestro programa fue exitoso',
        'Your program should print the string `Hello, C!` on the screen.': 'Tu programa debe imprimir la cadena `Hello, C!` en la pantalla.',
    },
    
    # ===== VARIABLES EXERCISES =====
    'variables/1.md': {
        'Variables are containers for storing data values.': 'Las variables son contenedores para almacenar valores de datos.',
        'Every variable in C is an object and like other programming languages, C has commands for declaring a variable.': 'Cada variable en C es un objeto y, como otros lenguajes de programación, C tiene comandos para declarar una variable.',
        'To create a variable, we need to give it a **type** and a **name** keeping in mind that it must not contain spaces.': 'Para crear una variable, necesitamos darle un **tipo** y un **nombre** teniendo en cuenta que no debe contener espacios.',
        'A variable is created the moment you first assign a value to it.': 'Una variable se crea en el momento en que le asignas un valor por primera vez.',
        'An example of a variable creation named `x` is:': 'Un ejemplo de creación de variable llamada `x` es:',
        'In this way we have assigned the value `1` to the _integer_ variable named `x`.': 'De esta manera hemos asignado el valor `1` a la variable _entero_ llamada `x`.',
        'If we print the variable `x` we get back the number `1`:': 'Si imprimimos la variable `x` obtenemos el número `1`:',
        'Assign to the variable `y` the value `2`.': 'Asigna a la variable `y` el valor `2`.',
        '`y` must be equal to `2`.': '`y` debe ser igual a `2`.',
        'with': 'con',
        'failures': 'fallos',
    },
    
    'variables/2.md': {
        'Variables are called in this way because the value they store can change.': 'Las variables se llaman así porque el valor que almacenan puede cambiar.',
        'We can update `x` by using `=` and giving it a new value.': 'Podemos actualizar `x` usando `=` y dándole un nuevo valor.',
        'Update the value of the variable `x` with the number `10`.': 'Actualiza el valor de la variable `x` con el número `10`.',
        '`x` must be equal to `10`.': '`x` debe ser igual a `10`.',
        '// write after this line': '// escribe después de esta línea',
    },
    
    # ===== COMMON PHRASES =====
    'common': {
        'Operators are used to perform operations on variables and values.': 'Los operadores se utilizan para realizar operaciones sobre variables y valores.',
        "Let's start with the arithmetic operators, in particular with the **addition** `+` operator.": 'Empecemos con los operadores aritméticos, en particular con el operador de **suma** `+`.',
        'It is used to add two numbers, like:': 'Se usa para sumar dos números, como:',
        'Calculate the sum between the numbers': 'Calcula la suma entre los números',
        '(in this order)': '(en este orden)',
        'then print the variable': 'luego imprime la variable',
        'What is the ouput of the following code': 'Cuál es la salida del siguiente código',
        'Write a function that returns the string': 'Escribe una función que devuelva la cadena',
        'must be equal to': 'debe ser igual a',
        'must be': 'debe ser',
        'should be': 'debería ser',
        'should return': 'debería devolver',
        'should print': 'debería imprimir',
        'the function should return': 'la función debe devolver',
        'The function should return': 'La función debe devolver',
        'Can you order these lines into a functional script': '¿Puedes ordenar estas líneas en un script funcional',
        'Choose the correct answer': 'Elige la respuesta correcta',
        
        # Learning phrases
        'Learn how to': 'Aprende cómo',
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
    },
}

def translate_line(line: str, file_key: str = 'common') -> str:
    """Translate a single line using all applicable dictionaries."""
    result = line
    
    # Get file-specific translations if available
    if file_key in TRANSLATIONS:
        for en, es in TRANSLATIONS[file_key].items():
            result = result.replace(en, es)
    
    # Apply common translations
    for en, es in TRANSLATIONS['common'].items():
        result = result.replace(en, es)
    
    return result

def translate_file_content(content: str, file_path: str) -> str:
    """Translate file content preserving code structure."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    current_section = None
    
    # Determine file key
    rel_path = str(Path(file_path).relative_to(EN_DIR))
    file_key = rel_path if rel_path in TRANSLATIONS else 'common'
    
    for line in lines:
        stripped = line.strip()
        
        # Section markers
        if stripped in ['# --description--', '# --instructions--', '# --seed--',
                       '# --answers--', '# --solutions--', '# --asserts--',
                       '# --before-seed--', '# --after-seed--',
                       '# --before-asserts--', '# --after-asserts--',
                       '# --output--']:
            current_section = stripped
            in_code_block = False
            result.append(line)
            continue
        
        # Code blocks
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
        # Translate prose sections only
        if not in_code_block and current_section in ['# --description--', '# --instructions--', '# --asserts--', '# --answers--']:
            result.append(translate_line(line, file_key))
        elif not in_code_block and current_section == '# --seed--':
            # Only translate comments in seed section
            if stripped.startswith('//'):
                result.append(translate_line(line, file_key))
            else:
                result.append(line)
        else:
            result.append(line)
    
    return '\n'.join(result)

def translate_json_file(content: str) -> str:
    """Translate data.json file."""
    data = json.loads(content)
    
    def translate_value(obj):
        if isinstance(obj, str):
            return translate_line(obj, 'common')
        elif isinstance(obj, dict):
            return {k: translate_value(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [translate_value(item) for item in obj]
        return obj
    
    translated = translate_value(data)
    return json.dumps(translated, indent=4, ensure_ascii=False) + '\n'

def process_all_files():
    """Process all C exercise files."""
    # Main data.json
    src = EN_DIR / 'data.json'
    dst = ES_DIR / 'data.json'
    dst.parent.mkdir(parents=True, exist_ok=True)
    content = src.read_text(encoding='utf-8')
    dst.write_text(translate_json_file(content), encoding='utf-8')
    print("Translated: data.json")
    
    dirs = ['output', 'formattedStrings', 'variables', 'booleans',
            'arithmeticOperators', 'assignmentOperators', 'relationBooleanOperators',
            'conditionalStatements', 'whileLoops', 'forLoops', 'arrays',
            'functions', 'challenges']
    
    total = 0
    for dirname in dirs:
        src_dir = EN_DIR / dirname
        dst_dir = ES_DIR / dirname
        if src_dir.exists():
            dst_dir.mkdir(parents=True, exist_ok=True)
            for item in src_dir.iterdir():
                if item.is_file():
                    dst_path = dst_dir / item.name
                    content = item.read_text(encoding='utf-8')
                    if item.suffix == '.md':
                        dst_path.write_text(translate_file_content(content, str(item)), encoding='utf-8')
                    elif item.name == 'data.json':
                        dst_path.write_text(translate_json_file(content), encoding='utf-8')
                    else:
                        dst_path.write_text(content, encoding='utf-8')
                    total += 1
            print(f"Translated {dirname}: {len(list(src_dir.iterdir()))} files")
    
    print(f"\nTotal: {total} files translated")

if __name__ == '__main__':
    process_all_files()
