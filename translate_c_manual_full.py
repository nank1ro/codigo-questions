#!/usr/bin/env python3
"""
Manual full translation using complete phrase replacements.
This ensures proper Spanish translation without partial word replacements.
"""

import json
from pathlib import Path
from typing import Dict, Tuple, List

BASE_DIR = Path("/Users/ale/github/codigo-questions")
EN_DIR = BASE_DIR / "en" / "c"
ES_DIR = BASE_DIR / "es" / "c"

# Manual translation map - complete phrases only
PHRASE_TRANSLATIONS: Dict[str, str] = {
    # ===== OUTPUT EXERCISES =====
    '"__Hello, World!__" is the traditional first program for beginning programming in a new language.': '"__Hello, World!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje.',
    'We use the `printf()` function to output data to the standard output device (screen).': 'Usamos la función `printf()` para mostrar datos en el dispositivo de salida estándar (pantalla).',
    'Every C program uses libraries, which give the ability to execute necessary functions, for example the print on the screen function is defined in the `stdio.h` header file.': 'Todo programa en C usa bibliotecas, que dan la capacidad de ejecutar funciones necesarias, por ejemplo la función de impresión en pantalla está definida en el archivo de encabezado `stdio.h`.',
    'The first code which will run will always reside in the main function.': 'El primer código que se ejecutará siempre residirá en la función principal.',
    'To print `Hello, World!` on the screen with C we can write': 'Para imprimir `Hello, World!` en la pantalla con C podemos escribir',
    'Finally we return `0` to indicate that our program was successful': 'Finalmente devolvemos `0` para indicar que nuestro programa fue exitoso',
    'Your program should print the string `Hello, C!` on the screen.': 'Tu programa debe imprimir la cadena `Hello, C!` en la pantalla.',
    
    # ===== VARIABLES EXERCISES =====
    'Variables are containers for storing data values.': 'Las variables son contenedores para almacenar valores de datos.',
    'Every variable in C is an object and like other programming languages, C has commands for declaring a variable.': 'Cada variable en C es un objeto y, como otros lenguajes de programación, C tiene comandos para declarar una variable.',
    'To create a variable, we need to give it a **type** and a **name** keeping in mind that it must not contain spaces.': 'Para crear una variable, necesitamos darle un **tipo** y un **nombre** teniendo en cuenta que no debe contener espacios.',
    'A variable is created the moment you first assign a value to it.': 'Una variable se crea en el momento en que le asignas un valor por primera vez.',
    'An example of a variable creation named `x` is:': 'Un ejemplo de creación de variable llamada `x` es:',
    'In this way we have assigned the value `1` to the _integer_ variable named `x`.': 'De esta manera hemos asignado el valor `1` a la variable _entero_ llamada `x`.',
    'If we print the variable `x` we get back the number `1`:': 'Si imprimimos la variable `x` obtenemos el número `1`:',
    'Assign to the variable `y` the value `2`.': 'Asigna a la variable `y` el valor `2`.',
    '`y` must be equal to `2`.': '`y` debe ser igual a `2`.',
    'Variables are called in this way because the value they store can change.': 'Las variables se llaman así porque el valor que almacenan puede cambiar.',
    'We can update `x` by using `=` and giving it a new value.': 'Podemos actualizar `x` usando `=` y dándole un nuevo valor.',
    'Update the value of the variable `x` with the number `10`.': 'Actualiza el valor de la variable `x` con el número `10`.',
    '`x` must be equal to `10`.': '`x` debe ser igual a `10`.',
    
    # ===== ARITHMETIC OPERATORS =====
    'Operators are used to perform operations on variables and values.': 'Los operadores se utilizan para realizar operaciones sobre variables y valores.',
    "Let's start with the arithmetic operators, in particular with the **addition** `+` operator.": 'Empecemos con los operadores aritméticos, en particular con el operador de **suma** `+`.',
    'It is used to add two numbers, like:': 'Se usa para sumar dos números, como:',
    'Calculate the sum between the numbers 4 and 9 (in this order), then print the variable `sum`': 'Calcula la suma entre los números 4 y 9 (en este orden), luego imprime la variable `sum`',
    'What is the ouput of the following code': 'Cuál es la salida del siguiente código',
    
    # ===== CHALLENGES =====
    '__"Hello, World!"__ is the traditional first program for beginning programming in a new language or environment.': '__"Hello, World!"__ es el primer programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.',
    'Write a function that returns the string "Hello, World!".': 'Escribe una función que devuelva la cadena "Hello, World!".',
    'The function should return "Hello, World!".': 'La función debe devolver "Hello, World!".',
    
    # ===== DATA.JSON TITLES =====
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
    
    # ===== LEARNING PHRASES =====
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
    
    # ===== CHALLENGE NAMES =====
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
    
    # ===== OTHER COMMON PHRASES =====
    'with': 'con',
    'failures': 'fallos',
}

def translate_line(line: str) -> str:
    """Translate a line by replacing complete phrases."""
    result = line
    # Sort by length (longest first) to avoid partial matches
    for en, es in sorted(PHRASE_TRANSLATIONS.items(), key=len, reverse=True):
        if en in result:
            result = result.replace(en, es)
    return result

def translate_file_content(content: str) -> str:
    """Translate file content preserving structure."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    current_section = None
    
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
        
        # Only translate prose sections
        if not in_code_block and current_section in ['# --description--', '# --instructions--', '# --asserts--', '# --answers--']:
            result.append(translate_line(line))
        elif not in_code_block and current_section == '# --seed--' and stripped.startswith('//'):
            # Translate only comments in seed
            result.append(translate_line(line))
        else:
            result.append(line)
    
    return '\n'.join(result)

def translate_json_file(content: str) -> str:
    """Translate JSON file values."""
    data = json.loads(content)
    
    def translate_obj(obj):
        if isinstance(obj, str):
            return translate_line(obj)
        elif isinstance(obj, dict):
            return {k: translate_obj(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [translate_obj(item) for item in obj]
        return obj
    
    translated = translate_obj(data)
    return json.dumps(translated, indent=4, ensure_ascii=False) + '\n'

def process_all():
    """Process all files."""
    ES_DIR.mkdir(parents=True, exist_ok=True)
    
    # Process main data.json
    src = EN_DIR / 'data.json'
    dst = ES_DIR / 'data.json'
    dst.write_text(translate_json_file(src.read_text(encoding='utf-8')), encoding='utf-8')
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
                        dst_path.write_text(translate_file_content(content), encoding='utf-8')
                    elif item.name == 'data.json':
                        dst_path.write_text(translate_json_file(content), encoding='utf-8')
                    else:
                        dst_path.write_text(content, encoding='utf-8')
                    total += 1
            print(f"Translated {dirname}: {len(list(src_dir.iterdir()))} files")
    
    print(f"\nTotal: {total} files translated")

if __name__ == '__main__':
    process_all()
