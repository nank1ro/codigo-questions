#!/usr/bin/env python3
"""
Comprehensive Spanish translation for JavaScript exercises.
Translates all user-facing text while preserving code structure.
"""

import json
import shutil
from pathlib import Path
import re

# Complete phrase translations (English -> Spanish)
# Sorted by length (longest first) to ensure proper matching
TRANSLATIONS = {
    # Variable types and declarations
    'Variables are containers for storing data values.': 'Las variables son contenedores para almacenar valores de datos.',
    'Every variable in JavaScript is an object.': 'Cada variable en JavaScript es un objeto.',
    'To create a variable, we need to give it a **name** keeping in mind that it must not contain spaces.': 'Para crear una variable, necesitamos darle un **nombre** teniendo en cuenta que no debe contener espacios.',
    'A variable is created the moment you first assign a value to it.': 'Una variable se crea en el momento en que le asignas un valor por primera vez.',
    'In JavaScript you declare constants with the `let` or `const` keywords and variables with the `var` keyword.': 'En JavaScript declaras constantes con las palabras clave `let` o `const` y variables con la palabra clave `var`.',
    'The value of a constant can\'t be changed once it\'s set, whereas a variable can be set to a different value in the future.': 'El valor de una constante no se puede cambiar una vez establecido, mientras que una variable puede establecerse a un valor diferente en el futuro.',
    'An example of a variable creation named `x` is:': 'Un ejemplo de creación de una variable llamada `x` es:',
    'In this way we have assigned the value `1` to the variable named `x`.': 'De esta manera hemos asignado el valor `1` a la variable llamada `x`.',
    'If we print the variable `x` we get back the number `1`:': 'Si imprimimos la variable `x` obtenemos el número `1`:',

    # Arrays
    'Arrays are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.': 'Los arreglos son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un solo nombre de variable.',
    'An array stores multiple values of one or multiple types and uses **indexes** to distinguish these values.': 'Un arreglo almacena múltiples valores de uno o varios tipos y usa **índices** para distinguir estos valores.',
    'You can assign items to an array with an expression of the form:': 'Puedes asignar elementos a un arreglo con una expresión de la forma:',

    # Functions
    'You might have considered the situation where you would like to reuse a piece of code, just with a few different values.': 'Podrías haber considerado la situación en la que te gustaría reutilizar un fragmento de código, solo con algunos valores diferentes.',
    'Instead of rewriting the whole code, it\'s much cleaner to define a function, which can then be used repeatedly.': 'En lugar de reescribir todo el código, es mucho más limpio definir una función, que luego se puede usar repetidamente.',
    'In JavaScript we use the `function` keyword followed by the name of the function:': 'En JavaScript usamos la palabra clave `function` seguida del nombre de la función:',

    # Booleans
    'JavaScript has a basic Boolean type, called `boolean`.': 'JavaScript tiene un tipo Boolean básico, llamado `boolean`.',
    'Boolean values are referred to as logical, because they can only ever be true or false.': 'Los valores booleanos se conocen como lógicos, porque solo pueden ser verdaderos o falsos.',
    'You can evaluate any expression in JavaScript, and get one of two answers, `true` or `false`.': 'Puedes evaluar cualquier expresión en JavaScript y obtener una de dos respuestas, `true` o `false`.',

    # Output
    '"__Hello, World!__" is the traditional first program for beginning programming in a new language.': '"__Hello, World!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje.',
    'We use the `console.log()` function to output data to the standard output device (screen).': 'Usamos la función `console.log()` para mostrar datos en el dispositivo de salida estándar (pantalla).',
    'To print `Hello, World!` on the screen with JavaScript we can write': 'Para imprimir `Hello, World!` en la pantalla con JavaScript podemos escribir',

    # Template literals
    'In JavaScript we can use the `+` sign to display two or more strings together, like:': 'En JavaScript podemos usar el signo `+` para mostrar dos o más cadenas juntas, como:',

    # Conditional statements
    'Decision making is required when we want to execute code only if a certain condition is satisfied.': 'La toma de decisiones es necesaria cuando queremos ejecutar código solo si se cumple una determinada condición.',
    'Let\'s assume we want to play outside only if the weather is nice.': 'Supongamos que queremos jugar afuera solo si el clima es agradable.',
    'In programming, we can save a boolean variable `niceWeather` and perform the action of playing outside `if` this variable is `true`, like:': 'En programación, podemos guardar una variable booleana `niceWeather` y realizar la acción de jugar afuera `if` esta variable es `true`, como:',

    # While loops
    'Often in programming, we need to repeat a block of code, for example:': 'A menudo en programación, necesitamos repetir un bloque de código, por ejemplo:',
    'This produces the following output:': 'Esto produce la siguiente salida:',
    'Obviously, for long statements we would spend a lot of time writing the code, but fortunately, we can use loops.': 'Obviamente, para declaraciones largas pasaríamos mucho tiempo escribiendo el código, pero por suerte, podemos usar bucles.',
    'Let\'s learn the `while` loop, getting the same output above.': 'Aprendamos el bucle `while`, obteniendo la misma salida anterior.',
    'So we created a variable `count` assigning `2`, the initial value.': 'Así creamos una variable `count` asignando `2`, el valor inicial.',
    'Then we have used the `while` statement that will run the block of code until the condition `count <= 5` is `true`.': 'Luego hemos usado la declaración `while` que ejecutará el bloque de código hasta que la condición `count <= 5` sea `true`.',
    'Inside the block of code, we should **NOT** miss to add the line `count += 1`.': 'Dentro del bloque de código, **NO** debemos olvidar agregar la línea `count += 1`.',
    'It increments the `count` value, otherwise, our loop will be infinite': 'Incrementa el valor de `count`, de lo contrario, nuestro bucle será infinito',

    # For loops
    'We know how to repeat code using a `while` loop.': 'Sabemos cómo repetir código usando un bucle `while`.',
    'Like this program repeating statements to display `hello`': 'Como este programa que repite declaraciones para mostrar `hello`',
    'But we can do the same with `for` loops:': 'Pero podemos hacer lo mismo con bucles `for`:',

    # Comparison operators
    'Let\'s start with the **equal** `==` comparison operator.': 'Comencemos con el operador de comparación **igual** `==`.',
    'It returns a **boolean** (`true` or `false`) stating whether two expressions are equal, for example:': 'Devuelve un **booleano** (`true` o `false`) indicando si dos expresiones son iguales, por ejemplo:',

    # Assignment operators
    'We\'ve already learned that to assign a value to a variable we can use the `=` sign, like:': 'Ya hemos aprendido que para asignar un valor a una variable podemos usar el signo `=`, como:',

    # Objects
    '**Objects** are similar to arrays, but you access values by looking up a *key* instead of an index': 'Los **objetos** son similares a los arreglos, pero accedes a los valores buscando una *clave* en lugar de un índice',
    'A key can be any string or number.': 'Una clave puede ser cualquier cadena o número.',
    'Objects are enclosed in curly brackets, like so:': 'Los objetos se encierran entre llaves, así:',
    'This is a dictionary called `objectName` with three *key-value pairs*.': 'Este es un diccionario llamado `objectName` con tres *pares clave-valor*.',
    'The key `key1` points to the value `1`, `key2` to `2`, and so on.': 'La clave `key1` apunta al valor `1`, `key2` a `2`, y así sucesivamente.',

    # Arithmetic operators
    'Operators are used to perform operations on variables and values.': 'Los operadores se usan para realizar operaciones sobre variables y valores.',
    'Let\'s start with the arithmetic operators, in particular with the **addition** `+` operator.': 'Comencemos con los operadores aritméticos, en particular con el operador de **suma** `+`.',
    'It is used to add two numbers, like:': 'Se usa para sumar dos números, como:',

    # Instructions
    'Assign to the variable `y` the value `2`.': 'Asigna a la variable `y` el valor `2`.',
    'Assign to the variable `num` the value `20`, then print its value': 'Asigna a la variable `num` el valor `20`, luego imprime su valor',
    'Calculate the sum between the numbers 4 and 9 (in this order), then print the variable `sum`': 'Calcula la suma entre los números 4 y 9 (en este orden), luego imprime la variable `sum`',
    'Complete the code in order to create a valid array': 'Completa el código para crear un arreglo válido',
    'Complete the code in order to create a valid function called `sayHello`': 'Completa el código para crear una función válida llamada `sayHello`',
    'Assign to the variable `musicOn` the boolean value `true`': 'Asigna a la variable `musicOn` el valor booleano `true`',
    'Your program should print the string `Hello, JavaScript!` on the screen.': 'Tu programa debe imprimir la cadena `Hello, JavaScript!` en la pantalla.',
    'Do the same with the code below': 'Haz lo mismo con el código de abajo',
    'Create an `if` statement checking if the `time` is lower than `12`, then in the code block print the string `"It\'s morning"`': 'Crea una declaración `if` que verifique si `time` es menor que `12`, luego en el bloque de código imprime la cadena `"It\'s morning"`',
    'What is the ouput of the following code?': '¿Cuál es la salida del siguiente código?',
    'Can you order these lines into a functional code?': '¿Puedes ordenar estas líneas en un código funcional?',
    'Fill in the blanks with the `while` loop to repeat the block of code': 'Completa los espacios con el bucle `while` para repetir el bloque de código',
    'Complete the `for` loop in the following code': 'Completa el bucle `for` en el siguiente código',
    'Print a boolean checking if `num` is equal to `5`': 'Imprime un booleano verificando si `num` es igual a `5`',
    'Complete the code in order to create a valid dictionary (object)': 'Completa el código para crear un diccionario válido (objeto)',

    # Assert descriptions
    '`y` must be equal to `2`.': '`y` debe ser igual a `2`.',
    'The function should return "Hello, World!".': 'La función debe devolver "Hello, World!".',

    # Greetings
    'Hello, World!': '¡Hola, mundo!',
    'It\'s morning': 'Es por la mañana',
    'The first name is': 'El nombre es',

    # Comments
    '// prints 1': '// imprime 1',
    '// prints "Hello!"': '// imprime "Hello!"',
    '// prints 8': '// imprime 8',
    '// prints true': '// imprime true',
    '// prints false': '// imprime false',
    '// prints "Hello JavaScript!"': '// imprime "Hello JavaScript!"',
    '// play outside': '// jugar afuera',
    '// DO NOT EDIT FROM HERE': '// DO NOT EDIT FROM HERE',
    '// DO NOT EDIT UNTIL HERE': '// DO NOT EDIT UNTIL HERE',

    # Test messages
    'Test Case': 'Caso de prueba',
    'failed': 'falló',
    'Executed': 'Ejecutados',
    'tests, with': 'pruebas, con',
    'failures': 'fallos',

    # Challenge descriptions
    '__"Hello, World!"__ is the traditional first program for beginning programming in a new language or environment.': '__"Hello, World!"__ es el primer programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.',
    'Write a function that returns the string `"Hello, World!"`.': 'Escribe una función que devuelva la cadena `"Hello, World!"`.',

    # Variable names in comments/strings
    'count': 'conteo',
    'sum': 'suma',
    'name': 'nombre',
    'first name': 'nombre',
    'number': 'número',
    'numbers': 'números',
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

# Section tags (must not be translated)
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

def translate_text(text):
    """Translate text using phrase replacements."""
    result = text

    # Sort translations by length (longest first) for proper matching
    for en, es in sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        if en in result:
            result = result.replace(en, es)

    return result

def translate_line(line, in_code_block):
    """Translate a single line based on context."""
    stripped = line.strip()

    # Never translate section tags
    if any(tag in stripped for tag in SECTION_TAGS):
        return line

    # Handle DO NOT EDIT comments - translate messages but preserve structure
    if '// DO NOT EDIT' in line:
        result = line
        if 'failed' in line:
            result = result.replace('failed', 'falló')
        if 'Test Case' in line:
            result = result.replace('Test Case', 'Caso de prueba')
        if 'Executed' in line:
            result = result.replace('Executed', 'Ejecutados')
        if 'tests, with' in line:
            result = result.replace('tests, with', 'pruebas, con')
        if 'failures' in line:
            result = result.replace('failures', 'fallos')
        return result

    # Handle error tags
    if '--err-t' in line:
        if 'failed' in line:
            return line.replace('failed', 'falló')
        return line

    # Handle code blocks - translate string contents and comments
    if in_code_block:
        result = line

        # Translate comments
        if '//' in result:
            comment_start = result.find('//')
            before_comment = result[:comment_start]
            comment = result[comment_start:]
            translated_comment = translate_text(comment[2:])
            result = before_comment + '//' + translated_comment

        # Translate string literals
        def replace_string(match):
            quote = match.group(1)
            content = match.group(2)
            # Translate string content
            translated = translate_text(content)
            return quote + translated + quote

        # Match strings (both single and double quotes, backticks)
        result = re.sub(r'(["\'`])(.*?)(?<!\\)\1', replace_string, result)

        return result
    else:
        # Outside code blocks - translate all text
        return translate_text(line)

def translate_exercise_file(content):
    """Translate an exercise markdown file."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    in_yaml = False

    for i, line in enumerate(lines):
        # YAML frontmatter
        if i == 0 and line.startswith('---'):
            in_yaml = True
            result.append(line)
            continue
        if in_yaml:
            result.append(line)
            if line.strip() == '---':
                in_yaml = False
            continue

        # Code block detection
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        # Translate the line
        result.append(translate_line(line, in_code_block))

    return '\n'.join(result)

def translate_data_json(content):
    """Translate main data.json file."""
    data = json.loads(content)
    result = {}

    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = {}
            for sub_key, sub_value in value.items():
                if sub_key in ['title', 'name', 'description']:
                    if sub_value in DATA_JSON_TRANSLATIONS:
                        result[key][sub_key] = DATA_JSON_TRANSLATIONS[sub_value]
                    else:
                        # Try translations
                        translated = sub_value
                        for en, es in sorted(DATA_JSON_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
                            translated = translated.replace(en, es)
                        result[key][sub_key] = translated
                else:
                    result[key][sub_key] = sub_value
        else:
            result[key] = value

    return json.dumps(result, indent=4, ensure_ascii=False) + '\n'

def translate_challenges_data_json(content):
    """Translate challenges data.json file."""
    data = json.loads(content)
    result = {}

    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = {}
            for sub_key, sub_value in value.items():
                if sub_key == 'name':
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
    """Copy and translate all files."""
    src_path = Path(src_dir)
    dst_path = Path(dst_dir)

    files_translated = []

    for item in sorted(src_path.rglob('*')):
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

    # Clear destination
    if es_base.exists():
        shutil.rmtree(es_base)
    es_base.mkdir(parents=True, exist_ok=True)

    # Translate all files
    files = copy_and_translate_directory(en_base, es_base)

    print(f'\nTranslation complete!')
    print(f'Total files created: {len(files)}')

    md_files = [f for f in files if f.endswith('.md')]
    json_files = [f for f in files if f.endswith('.json')]
    print(f'  - Markdown files: {len(md_files)}')
    print(f'  - JSON files: {len(json_files)}')

    dirs = {}
    for f in files:
        parent = str(Path(f).parent)
        dirs[parent] = dirs.get(parent, 0) + 1

    print(f'\nFiles by directory:')
    for dir_path in sorted(dirs.keys()):
        print(f'  - {dir_path}: {dirs[dir_path]} files')

if __name__ == '__main__':
    main()
