#!/usr/bin/env python3
"""
Translates JavaScript exercises from English to Spanish.
Uses proper phrase-level translations instead of word-by-word.
"""

import json
import os
import re
import shutil
from pathlib import Path

# Proper phrase translations (English -> Spanish)
PHRASE_TRANSLATIONS = {
    # Greetings and basic phrases
    'Hello, World!': '¡Hola, mundo!',
    'Hello, World': 'Hola, mundo',
    'Hello, JavaScript!': '¡Hola, JavaScript!',
    'Hello JavaScript!': '¡Hola, JavaScript!',
    "Hello, JavaScript!": "¡Hola, JavaScript!",
    'It\'s morning': 'Es por la mañana',

    # Full description phrases
    'Variables are containers for storing data values.': 'Las variables son contenedores para almacenar valores de datos.',
    'Every variable in JavaScript is an object.': 'Cada variable en JavaScript es un objeto.',
    'To create a variable, we need to give it a **name** keeping in mind that it must not contain spaces.': 'Para crear una variable, necesitamos darle un **nombre** teniendo en cuenta que no debe contener espacios.',
    'A variable is created the moment you first assign a value to it.': 'Una variable se crea en el momento en que le asignas un valor por primera vez.',
    'In JavaScript you declare constants with the `let` or `const` keywords and variables with the `var` keyword.': 'En JavaScript declaras constantes con las palabras clave `let` o `const` y variables con la palabra clave `var`.',
    'The value of a constant can\'t be changed once it\'s set, whereas a variable can be set to a different value in the future.': 'El valor de una constante no se puede cambiar una vez establecido, mientras que una variable se puede establecer a un valor diferente en el futuro.',
    'An example of a variable creation named `x` is:': 'Un ejemplo de creación de una variable llamada `x` es:',
    'In this way we have assigned the value `1` to the variable named `x`:': 'De esta manera hemos asignado el valor `1` a la variable llamada `x`:',
    'If we print the variable `x` we get back the number `1`:': 'Si imprimimos la variable `x` obtenemos el número `1`:',
    '// prints 1': '// imprime 1',

    # Arrays
    'Arrays are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.': 'Los arreglos son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un solo nombre de variable.',
    'An array stores multiple values of one or multiple types and uses **indexes** to distinguish these values.': 'Un arreglo almacena múltiples valores de uno o varios tipos y usa **índices** para distinguir estos valores.',
    'You can assign items to an array with an expression of the form:': 'Puedes asignar elementos a un arreglo con una expresión de la forma:',

    # Functions
    'You might have considered the situation where you would like to reuse a piece of code, just with a few different values.': 'Podrías haber considerado la situación en la que te gustaría reutilizar un fragmento de código, solo con algunos valores diferentes.',
    'Instead of rewriting the whole code, it\'s much cleaner to define a function, which can then be used repeatedly.': 'En lugar de reescribir todo el código, es mucho más limpio definir una función, que luego se puede usar repetidamente.',
    'In JavaScript we use the `function` keyword followed by the name of the function:': 'En JavaScript usamos la palabra clave `function` seguida del nombre de la función:',
    '// prints "Hello!"': '// imprime "Hello!"',

    # Booleans
    'JavaScript has a basic Boolean type, called `boolean`.': 'JavaScript tiene un tipo booleano básico, llamado `boolean`.',
    'Boolean values are referred to as logical, because they can only ever be true or false.': 'Los valores booleanos se conocen como lógicos, porque solo pueden ser verdaderos o falsos.',
    'You can evaluate any expression in JavaScript, and get one of two answers, `true` or `false`.': 'Puedes evaluar cualquier expresión en JavaScript y obtener una de dos respuestas, `true` o `false`.',

    # Output
    '"__Hello, World!__" is the traditional first program for beginning programming in a new language.': '"__Hello, World!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje.',
    'We use the `console.log()` function to output data to the standard output device (screen).': 'Usamos la función `console.log()` para mostrar datos en el dispositivo de salida estándar (pantalla).',
    'To print `Hello, World!` on the screen with JavaScript we can write': 'Para imprimir `Hello, World!` en la pantalla con JavaScript podemos escribir',

    # Template literals
    'In JavaScript we can use the `+` sign to display two or more strings together, like:': 'En JavaScript podemos usar el signo `+` para mostrar dos o más cadenas juntas, como:',
    '// prints "Hello JavaScript!"': '// imprime "Hello JavaScript!"',

    # Conditional statements
    'Decision making is required when we want to execute code only if a certain condition is satisfied.': 'La toma de decisiones es necesaria cuando queremos ejecutar código solo si se cumple una determinada condición.',
    'Let\'s assume we want to play outside only if the weather is nice.': 'Supongamos que queremos jugar afuera solo si el clima es agradable.',
    'In programming, we can save a boolean variable `niceWeather` and perform the action of playing outside `if` this variable is `true`, like:': 'En programación, podemos guardar una variable booleana `niceWeather` y realizar la acción de jugar afuera `if` esta variable es `true`, como:',
    '// play outside': '// jugar afuera',

    # Instructions
    'Assign to the variable `y` the value `2`.': 'Asigna a la variable `y` el valor `2`.',
    'Complete the code in order to create a valid array': 'Completa el código para crear un arreglo válido',
    'Complete the code in order to create a valid function called `sayHello`': 'Completa el código para crear una función válida llamada `sayHello`',
    'Assign to the variable `musicOn` the boolean value `true`': 'Asigna a la variable `musicOn` el valor booleano `true`',
    'Your program should print the string `Hello, JavaScript!` on the screen.': 'Tu programa debe imprimir la cadena `Hello, JavaScript!` en la pantalla.',
    'Do the same with the code below': 'Haz lo mismo con el código de abajo',
    'Create an `if` statement checking if the `time` is lower than `12`, then in the code block print the string `"It\'s morning"`': 'Crea una declaración `if` que verifique si `time` es menor que `12`, luego en el bloque de código imprime la cadena `"It\'s morning"`',
    'What is the ouput of the following code?': '¿Cuál es la salida del siguiente código?',
    'Can you order these lines into a functional code?': '¿Puedes ordenar estas líneas en un código funcional?',

    # Assert descriptions
    '`y` must be equal to `2`.': '`y` debe ser igual a `2`.',
    'The function should return "Hello, World!".': 'La función debe devolver "Hello, World!".',

    # DO NOT EDIT comments - test messages
    'Test Case': 'Caso de prueba',
    'failed': 'falló',
    'Executed': 'Ejecutados',
    'tests, with': 'pruebas, con',
    'failures': 'fallos',

    # Challenge descriptions
    '__"Hello, World!"__ is the traditional first program for beginning programming in a new language or environment.': '__"Hello, World!"__ es el primer programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.',
    'Write a function that returns the string `"Hello, World!"`.': 'Escribe una función que devuelva la cadena `"Hello, World!"`.',
    'The function should return "Hello, World!".': 'La función debe devolver "Hello, World!".',
}

# Word translations (only use these for isolated words)
WORD_TRANSLATIONS = {
    'value': 'valor',
    'values': 'valores',
    'variable': 'variable',
    'name': 'nombre',
    'store': 'almacenar',
    'print': 'imprimir',
    'output': 'salida',
    'function': 'función',
    'string': 'cadena',
    'number': 'número',
    'boolean': 'booleano',
    'array': 'arreglo',
    'object': 'objeto',
    'code': 'código',
    'create': 'crear',
    'assign': 'asignar',
    'return': 'devolver',
    'execute': 'ejecutar',
    'statement': 'declaración',
    'expression': 'expresión',
    'keyword': 'palabra clave',
    'type': 'tipo',
    'data': 'datos',
    'information': 'información',
    'collection': 'colección',
    'sequence': 'secuencia',
    'piece': 'fragmento',
    'pieces': 'fragmentos',
    'reuse': 'reutilizar',
    'define': 'definir',
    'use': 'usar',
    'call': 'llamar',
    'evaluate': 'evaluar',
    'display': 'mostrar',
    'check': 'verificar',
    'order': 'ordenar',
    'lower': 'menor',
    'greater': 'mayor',
    'equal': 'igual',
}

# Variable name translations (English -> Spanish)
VAR_TRANSLATIONS = {
    'tryCatch': 'intentarCapturar',
    'args': 'argumentos',
    'name': 'nombre',
    'sayHello': 'sayHello',
    'sayHi': 'sayHi',
    'musicOn': 'musicaActivada',
    'niceWeather': 'buenClima',
    'num': 'numero',
    'numbers': 'numeros',
    'animals': 'animales',
    'arrayName': 'nombreArreglo',
    'product': 'producto',
    'sum': 'suma',
    'count': 'conteo',
    'result': 'resultado',
    'total': 'total',
    'index': 'indice',
    'length': 'longitud',
    'item': 'elemento',
    'items': 'elementos',
    'str': 'cadena',
    'text': 'texto',
    'char': 'caracter',
    'message': 'mensaje',
    'time': 'tiempo',
    'date': 'fecha',
    'day': 'dia',
    'hour': 'hora',
    'minute': 'minuto',
    'second': 'segundo',
    'found': 'encontrado',
    'search': 'busqueda',
    'first': 'primero',
    'last': 'ultimo',
    'next': 'siguiente',
    'previous': 'anterior',
    'current': 'actual',
    'temp': 'temporal',
    'input': 'entrada',
    'output': 'salida',
    'error': 'error',
    'data': 'datos',
    'status': 'estado',
    'flag': 'bandera',
    'isTrue': 'esVerdadero',
    'isFalse': 'esFalso',
    'isValid': 'esValido',
    'isEmpty': 'estaVacio',
    'hasValue': 'tieneValor',
}

# Data.json translations
DATA_JSON_TRANSLATIONS = {
    'Output': 'Salida',
    'Learn how to output a value': 'Aprende a mostrar un valor',
    'Template literals': 'Literales de plantilla',
    'Learn how to interpolate strings with different data types': 'Aprende a interpolar cadenas con diferentes tipos de datos',
    'Variables': 'Variables',
    'Learn how to store values in a variable': 'Aprende a almacenar valores en una variable',
    'Booleans': 'Booleanos',
    'Learn how to evaluate any expression': 'Aprende a evaluar cualquier expresión',
    'Arithmetic Operators': 'Operadores aritméticos',
    'Learn how to perform arithmetic operations on variables and values': 'Aprende a realizar operaciones aritméticas sobre variables y valores',
    'Assignment Operators': 'Operadores de asignación',
    'Learn how to assign values to variables': 'Aprende a asignar valores a variables',
    'Comparison and Logical Operators': 'Operadores de comparación y lógicos',
    'Learn how to compare values': 'Aprende a comparar valores',
    'Conditional Statements': 'Declaraciones condicionales',
    'Learn how to make decisions': 'Aprende a tomar decisiones',
    'While Loops': 'Bucles while',
    'Learn how to repeat a set of statements': 'Aprende a repetir un conjunto de declaraciones',
    'For Loops': 'Bucles for',
    'Learn how to repeat a set of statements': 'Aprende a repetir un conjunto de declaraciones',
    'Arrays': 'Arreglos',
    'Learn how to store different values into one variable': 'Aprende a almacenar diferentes valores en una variable',
    'Objects': 'Objetos',
    'Learn how to store values with keys': 'Aprende a almacenar valores con claves',
    'Functions': 'Funciones',
    'Learn how to divide code by specific tasks': 'Aprende a dividir el código en tareas específicas',
    'Classes': 'Clases',
    'Learn object-oriented programming': 'Aprende programación orientada a objetos',

    # Challenge names
    'Hello World!': '¡Hola, mundo!',
    'Addition': 'Suma',
    'ATM': 'Cajero automático',
    'Raindrops': 'Gotas de lluvia',
    'Sum of digits': 'Suma de dígitos',
    'Two for one': 'Dos por uno',
    '100 doors': '100 puertas',
    'Ackermann function': 'Función de Ackermann',
    'Multiples of 3 or 5': 'Múltiplos de 3 o 5',
    'Even Fibonacci numbers': 'Números pares de Fibonacci',
    'Largest prime factor': 'Mayor factor primo',
    'Largest palindrome product': 'Mayor producto palíndromo',
    'Smallest multiple': 'Múltiplo más pequeño',
    'Sum square difference': 'Diferencia de suma de cuadrados',
    '10001st prime': 'Primo 10001',
    'Largest product in a series': 'Mayor producto en una serie',
    'Special pythagorean triplet': 'Triplete pitagórico especial',
    'Summation of primes': 'Suma de primos',
    'Arithmetic mean': 'Media aritmética',
    'FizzBuzz': 'FizzBuzz',
    'Roman numeral converter': 'Conversor de números romanos',
    'Leap year': 'Año bisiesto',
}

# Section tags that must NOT be translated
SECTION_TAGS = [
    '--description--',
    '--instructions--',
    '--seed--',
    '--before-seed--',
    '--solutions--',
    '--asserts--',
    '--before-asserts--',
    '--after-asserts--',
    '--output--',
    '--answers--',
]

# Error tags that must NOT be translated
ERROR_TAG_PREFIX = '--err-t'

# DO NOT EDIT comments
DO_NOT_EDIT_PATTERNS = [
    '// DO NOT EDIT FROM HERE',
    '// DO NOT EDIT UNTIL HERE',
]

def translate_text_line(line):
    """Translate a line of text using phrase and word translations."""
    result = line

    # First, try phrase-level translations (longest first)
    for en, es in sorted(PHRASE_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        if en in result:
            result = result.replace(en, es)

    # Then, try word-level translations for remaining untranslated parts
    # Only apply these if the line still has English words
    for en, es in sorted(WORD_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        # Use word boundary to match whole words
        pattern = r'\b' + re.escape(en) + r's?\b'  # Handle plurals
        if re.search(pattern, result, re.IGNORECASE):
            # Check if this word hasn't been translated yet
            result = re.sub(pattern, lambda m: es if en not in PHRASE_TRANSLATIONS or en not in result else m.group(0), result, flags=re.IGNORECASE)

    return result

def translate_string_literal(content):
    """Translate content inside string literals."""
    result = content

    # Translate phrases in strings
    for en, es in sorted(PHRASE_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        if en in result:
            result = result.replace(en, es)

    return result

def translate_code_line(line):
    """Translate a line of code - only translate variable names and string contents."""
    result = line

    # Translate string literals
    def replace_string(match):
        quote = match.group(1)
        content = match.group(2)
        translated = translate_string_literal(content)
        return quote + translated + quote

    # Match strings with quotes
    result = re.sub(r'(["\'`])(.*?)(?<!\\)\1', replace_string, result)

    # Translate variable names in certain patterns
    # Only translate in specific contexts to avoid breaking code
    for var_en, var_es in VAR_TRANSLATIONS.items():
        # Match variable names in declarations or assignments
        # Be careful not to translate function names being called
        patterns = [
            r'\b' + var_en + r'\s*=',  # assignments
            r'\bfunction\s+' + var_en + r'\b',  # function declarations (but we might want to keep original function names)
            r'\bconst\s+' + var_en + r'\b',  # const declarations
            r'\blet\s+' + var_en + r'\b',  # let declarations
            r'\bvar\s+' + var_en + r'\b',  # var declarations
        ]

        for pattern in patterns:
            result = re.sub(pattern, var_en + ' = ' if '=' in pattern else var_es, result)

    return result

def translate_exercise_file(content):
    """Translate an exercise markdown file."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    in_yaml = False

    for i, line in enumerate(lines):
        # Check for YAML frontmatter
        if i == 0 and line.startswith('---'):
            in_yaml = True
            result.append(line)
            continue
        if in_yaml:
            result.append(line)
            if line.strip() == '---':
                in_yaml = False
            continue

        # Check for section tags - never translate these
        stripped = line.strip()
        if any(tag in stripped for tag in SECTION_TAGS):
            result.append(line)
            continue

        # Check for DO NOT EDIT comments
        if any(pattern in line for pattern in DO_NOT_EDIT_PATTERNS):
            # But translate test messages
            if 'failed' in line:
                line = line.replace('failed', 'falló')
            if 'Executed' in line:
                line = line.replace('Executed', 'Ejecutados')
            if 'tests, with' in line:
                line = line.replace('tests, with', 'pruebas, con')
            if 'failures' in line:
                line = line.replace('failures', 'fallos')
            if 'Test Case' in line:
                line = line.replace('Test Case', 'Caso de prueba')
            result.append(line)
            continue

        # Check for error tags
        if ERROR_TAG_PREFIX in line:
            if 'failed' in line:
                line = line.replace('failed', 'falló').replace('Failed', 'Falló')
            result.append(line)
            continue

        # Check for code blocks
        if stripped.startswith('```'):
            if not in_code_block:
                in_code_block = True
            else:
                in_code_block = False
            result.append(line)
            continue

        # Translate based on context
        if in_code_block:
            result.append(translate_code_line(line))
        else:
            result.append(translate_text_line(line))

    return '\n'.join(result)

def translate_data_json(content):
    """Translate a data.json file."""
    data = json.loads(content)
    result = {}

    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = {}
            for sub_key, sub_value in value.items():
                if sub_key in ['title', 'name', 'description']:
                    # Translate titles and descriptions
                    if sub_value in DATA_JSON_TRANSLATIONS:
                        result[key][sub_key] = DATA_JSON_TRANSLATIONS[sub_value]
                    else:
                        # Try phrase translations first
                        translated = sub_value
                        for en, es in sorted(PHRASE_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
                            translated = translated.replace(en, es)
                        result[key][sub_key] = translated
                else:
                    result[key][sub_key] = sub_value
        else:
            result[key] = value

    return json.dumps(result, indent=4, ensure_ascii=False) + '\n'

def translate_challenges_data_json(content):
    """Translate the challenges data.json file."""
    data = json.loads(content)
    result = {}

    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = {}
            for sub_key, sub_value in value.items():
                if sub_key == 'name':
                    # Translate challenge names
                    if sub_value in DATA_JSON_TRANSLATIONS:
                        result[key][sub_key] = DATA_JSON_TRANSLATIONS[sub_value]
                    else:
                        result[key][sub_key] = sub_value
                else:
                    result[key][sub_key] = sub_value
        else:
            result[key] = value

    return json.dumps(result, indent=2, ensure_ascii=False) + '\n'

def copy_and_translate_file(src_path, dst_path):
    """Copy and translate a single file."""
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if src_path.name == 'data.json':
        if 'challenges' in str(src_path):
            translated = translate_challenges_data_json(content)
        else:
            translated = translate_data_json(content)
    elif src_path.suffix == '.md':
        translated = translate_exercise_file(content)
    else:
        translated = content

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(translated)

def copy_and_translate_directory(src_dir, dst_dir):
    """Copy and translate all files from src to dst."""
    src_path = Path(src_dir)
    dst_path = Path(dst_dir)

    files_translated = []

    for item in src_path.rglob('*'):
        if item.is_file():
            relative_path = item.relative_to(src_path)
            dst_file = dst_path / relative_path

            copy_and_translate_file(item, dst_file)
            files_translated.append(str(dst_file))

    return files_translated

def main():
    en_base = Path('/Users/ale/github/codigo-questions/en/javascript')
    es_base = Path('/Users/ale/github/codigo-questions/es/javascript')

    print(f'Translating JavaScript exercises from {en_base} to {es_base}')

    # Clear destination first
    if es_base.exists():
        shutil.rmtree(es_base)

    # Create destination directory
    es_base.mkdir(parents=True, exist_ok=True)

    # Translate all files
    files = copy_and_translate_directory(en_base, es_base)

    print(f'\nTranslation complete!')
    print(f'Total files created: {len(files)}')

    # Count by type
    md_files = [f for f in files if f.endswith('.md')]
    json_files = [f for f in files if f.endswith('.json')]

    print(f'  - Markdown files: {len(md_files)}')
    print(f'  - JSON files: {len(json_files)}')

    # Count by directory
    dirs = {}
    for f in files:
        parent = str(Path(f).parent)
        dirs[parent] = dirs.get(parent, 0) + 1

    print(f'\nFiles by directory:')
    for dir_path in sorted(dirs.keys()):
        print(f'  - {dir_path}: {dirs[dir_path]} files')

if __name__ == '__main__':
    main()
