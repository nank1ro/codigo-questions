#!/usr/bin/env python3
"""
Expanded translation with comprehensive phrase coverage.
"""

import json
from pathlib import Path

BASE_DIR = Path("/Users/ale/github/codigo-questions")
EN_DIR = BASE_DIR / "en" / "c"
ES_DIR = BASE_DIR / "es" / "c"

# Comprehensive phrase translations
TRANSLATIONS = {
    # Previous translations
    '"__Hello, World!__" is the traditional first program for beginning programming in a new language.': '"__Hello, World!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje.',
    'We use the `printf()` function to output data to the standard output device (screen).': 'Usamos la función `printf()` para mostrar datos en el dispositivo de salida estándar (pantalla).',
    'Every C program uses libraries, which give the ability to execute necessary functions, for example the print on the screen function is defined in the `stdio.h` header file.': 'Todo programa en C usa bibliotecas, que dan la capacidad de ejecutar funciones necesarias, por ejemplo la función de impresión en pantalla está definida en el archivo de encabezado `stdio.h`.',
    'The first code which will run will always reside in the main function.': 'El primer código que se ejecutará siempre residirá en la función principal.',
    'To print `Hello, World!` on the screen with C we can write': 'Para imprimir `Hello, World!` en la pantalla con C podemos escribir',
    'Finally we return `0` to indicate that our program was successful': 'Finalmente devolvemos `0` para indicar que nuestro programa fue exitoso',
    'Your program should print the string `Hello, C!` on the screen.': 'Tu programa debe imprimir la cadena `Hello, C!` en la pantalla.',
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
    'Operators are used to perform operations on variables and values.': 'Los operadores se utilizan para realizar operaciones sobre variables y valores.',
    "Let's start with the arithmetic operators, in particular with the **addition** `+` operator.": 'Empecemos con los operadores aritméticos, en particular con el operador de **suma** `+`.',
    'It is used to add two numbers, like:': 'Se usa para sumar dos números, como:',
    'Calculate the sum between the numbers 4 and 9 (in this order), then print the variable `sum`': 'Calcula la suma entre los números 4 y 9 (en este orden), luego imprime la variable `sum`',
    'What is the ouput of the following code': 'Cuál es la salida del siguiente código',
    '__"Hello, World!"__ is the traditional first program for beginning programming in a new language or environment.': '__"Hello, World!"__ es el primer programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.',
    'Write a function that returns the string "Hello, World!".': 'Escribe una función que devuelva la cadena "Hello, World!".',
    'The function should return "Hello, World!".': 'La función debe devolver "Hello, World!".',
    
    # ===== NEW TRANSLATIONS =====
    # Arrays
    'Arrays are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.': 'Los arreglos son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un solo nombre de variable.',
    'An array stores multiple values of a single type and uses **indexes** to distinguish these values.': 'Un arreglo almacena múltiples valores de un solo tipo y usa **índices** para distinguir estos valores.',
    'You can assign items to an array with an expression of the form:': 'Puedes asignar elementos a un arreglo con una expresión de la forma:',
    '`data_type` is the type of data you\'ll be using for the array, for example `int`, `double`, etc.': '`data_type` es el tipo de dato que usarás para el arreglo, por ejemplo `int`, `double`, etc.',
    '`array_name` is the name of the variable that stores the items.': '`array_name` es el nombre de la variable que almacena los elementos.',
    '`array_size` is the maximum size that the array can have.': '`array_size` es el tamaño máximo que el arreglo puede tener.',
    'Finally, `item1` and `item2` are the values that we want to save in the array': 'Finalmente, `item1` y `item2` son los valores que queremos guardar en el arreglo',
    'Complete the code in order to create a valid array': 'Completa el código para crear un arreglo válido',
    
    # For Loops
    'We know how to repeat code using a `while` loop.': 'Sabemos cómo repetir código usando un bucle `while`.',
    'Like this program repeating statements to display `hello`': 'Como este programa repitiendo sentencias para mostrar `hello`',
    'But we can do the same with `for` loops:': 'Pero podemos hacer lo mismo con bucles `for`:',
    'Complete the `for` loop in the following code': 'Completa el bucle `for` en el siguiente código',
    
    # While Loops
    'Often in programming, we need to repeat a block of code, for example:': 'A menudo en programación, necesitamos repetir un bloque de código, por ejemplo:',
    'This produces the following output:': 'Esto produce la siguiente salida:',
    'Obviously, for long statements we would spend a lot of time writing the code, but fortunately, we can use loops.': 'Obviamente, para sentencias largas gastaríamos mucho tiempo escribiendo el código, pero afortunadamente, podemos usar bucles.',
    "Let's learn the `while` loop, getting the same output above.": 'Aprendamos el bucle `while`, obteniendo la misma salida anterior.',
    'So we created a variable `count` assigning `2`, the initial value.': 'Así creamos una variable `count` asignando `2`, el valor inicial.',
    'Then we have used the `while` statement that will run the block of code until the condition `count <= 5` is `true`.': 'Luego hemos usado la sentencia `while` que ejecutará el bloque de código hasta que la condición `count <= 5` sea `true`.',
    'Inside the block of code, we should **NOT** miss to add the line `count++;`.': 'Dentro del bloque de código, **NO** debemos olvidar agregar la línea `count++;`.',
    'It increments the `count` value, otherwise, our loop will be infinite': 'Incrementa el valor de `count`, de lo contrario, nuestro bucle será infinito',
    'Fill in the blanks with the `while` loop to repeat the block of code': 'Rellena los espacios con el bucle `while` para repetir el bloque de código',
    
    # Functions
    'Functions are blocks of code that perform a specific task.': 'Las funciones son bloques de código que realizan una tarea específica.',
    'They allow us to reuse code and make our programs more modular.': 'Nos permiten reutilizar código y hacer nuestros programas más modulares.',
    'To declare a function, we specify its return type, name, and parameters.': 'Para declarar una función, especificamos su tipo de retorno, nombre y parámetros.',
    'The `return` statement sends a value back to the caller.': 'La sentencia `return` envía un valor de vuelta al llamador.',
    'Write a function that returns the sum of two numbers.': 'Escribe una función que devuelva la suma de dos números.',
    
    # Common phrases
    'with': 'con',
    'failures': 'fallos',
    'Fill in the blanks': 'Rellena los espacios',
}

def translate_line(line: str) -> str:
    """Translate a line using complete phrases."""
    result = line
    for en, es in sorted(TRANSLATIONS.items(), key=len, reverse=True):
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
        
        if stripped in ['# --description--', '# --instructions--', '# --seed--',
                       '# --answers--', '# --solutions--', '# --asserts--',
                       '# --before-seed--', '# --after-seed--',
                       '# --before-asserts--', '# --after-asserts--',
                       '# --output--']:
            current_section = stripped
            in_code_block = False
            result.append(line)
            continue
        
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
        if not in_code_block and current_section in ['# --description--', '# --instructions--', '# --asserts--', '# --answers--']:
            result.append(translate_line(line))
        elif not in_code_block and current_section == '# --seed--' and stripped.startswith('//'):
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
    
    print(f"\nTotal: {total} files")

if __name__ == '__main__':
    process_all()
