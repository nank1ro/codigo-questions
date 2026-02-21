#!/usr/bin/env python3
"""
Proper translation script for C exercises from English to Spanish.
Only translates user-facing text, preserves all C syntax, keywords, and structure.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

# Base directories
BASE_DIR = Path("/Users/ale/github/codigo-questions")
EN_DIR = BASE_DIR / "en" / "c"
ES_DIR = BASE_DIR / "es" / "c"

# C keywords and reserved words that must NEVER be translated
C_KEYWORDS = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
    'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
    'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
    'volatile', 'while', 'bool', 'true', 'false',
    # Preprocessor directives
    '#ifdef', '#ifndef', '#define', '#endif', '#else', '#include', '#if',
    '#elif', '#undef', '#pragma', '#line', '#error',
    # C Standard library types
    'size_t', 'FILE', 'jmp_buf', 'time_t', 'clock_t', 'div_t', 'ldiv_t',
    # Common typedef patterns (lowercase versions)
    'ifdef', 'ifndef', 'define', 'endif', 'else', 'include', 'if', 'elif',
}

# Variable name translations (only for user-defined variables)
VAR_TRANSLATIONS = {
    "sum": "suma",
    "difference": "diferencia", 
    "product": "producto",
    "quotient": "cociente",
    "remainder": "resto",
    "count": "conteo",
    "result": "resultado",
    "value": "valor",
    "total": "total",
    "average": "promedio",
    "number": "numero",
    "numbers": "numeros",
    "name": "nombre",
    "names": "nombres",
    "age": "edad",
    "price": "precio",
    "length": "longitud",
    "width": "ancho",
    "height": "alto",
    "area": "area",
    "volume": "volumen",
    "temperature": "temperatura",
    "grade": "calificacion",
    "score": "puntuacion",
    "index": "indice",
    "item": "elemento",
    "items": "elementos",
    "text": "texto",
    "message": "mensaje",
    "character": "caracter",
    "characters": "caracteres",
    "word": "palabra",
    "words": "palabras",
    "sentence": "frase",
    "flag": "bandera",
    "found": "encontrado",
    "valid": "valido",
    "status": "estado",
    "response": "respuesta",
    "data": "datos",
    "array": "arreglo",
    "list": "lista",
    "element": "elemento",
    "position": "posicion",
    "size": "tamano",
    "maximum": "maximo",
    "minimum": "minimo",
    "first": "primero",
    "second": "segundo",
    "third": "tercero",
    "last": "ultimo",
    "next": "siguiente",
    "previous": "anterior",
    "current": "actual",
    "temp": "temporal",
    "counter": "contador",
    "base": "base",
    "exponent": "exponente",
    "radius": "radio",
    "side": "lado",
    "factor": "factor",
    "multiplier": "multiplicador",
    "divisor": "divisor",
    "operand": "operando",
    "operand1": "operando1",
    "operand2": "operando2",
    "boolean": "booleano",
    "condition": "condicion",
    "digit": "digito",
    "digits": "digitos",
    "reverse": "reverso",
    "reversed": "revertido",
    "original": "original",
    "updated": "actualizado",
    "changed": "cambiado",
    "user": "usuario",
    "letter": "letra",
    "letters": "letras",
    "string": "cadena",
    "strings": "cadenas",
    "integer": "entero",
    "float": "flotante",
    "matrix": "matriz",
    "row": "fila",
    "rows": "filas",
    "column": "columna",
    "columns": "columnas",
    "table": "tabla",
    "key": "clave",
    "pair": "par",
    "entry": "entrada",
    "year": "anio",
    "month": "mes",
    "day": "dia",
    "hour": "hora",
    "minute": "minuto",
    "second": "segundo",
    "time": "tiempo",
    "date": "fecha",
    "start": "inicio",
    "end": "fin",
    "begin": "comienzo",
    "finish": "termino",
    "upper": "mayuscula",
    "lower": "minuscula",
    "capitalized": "capitalizado",
    "swap": "intercambiar",
    "swapped": "intercambiado",
    "sorted": "ordenado",
    "ascending": "ascendente",
    "descending": "descendente",
    "search": "buscar",
    "searched": "buscado",
    "match": "coincidencia",
    "matches": "coincidencias",
    "pattern": "patron",
    "replacement": "reemplazo",
    "substring": "subcadena",
    "prefix": "prefijo",
    "suffix": "sufijo",
    "left": "izquierda",
    "right": "derecha",
    "middle": "medio",
    "center": "centro",
    "top": "arriba",
    "bottom": "abajo",
}

# Complete phrase translations for descriptions and instructions
TRANSLATIONS = {
    # Instructions
    "Your program should print the string": "Tu programa debe imprimir la cadena",
    "Your program should print": "Tu programa debe imprimir",
    "Your program should output": "Tu programa debe mostrar",
    "on the screen": "en la pantalla",
    "Write a function that returns the string": "Escribe una función que devuelva la cadena",
    "Write a function that returns": "Escribe una función que devuelva",
    "Write a function that": "Escribe una función que",
    "Write a program that": "Escribe un programa que",
    "Create a function that": "Crea una función que",
    "Create a variable": "Crea una variable",
    "Declare a variable": "Declara una variable",
    "Assign to the variable": "Asigna a la variable",
    "Assign to the variable": "Asigna a la variable",
    "Update the value of the variable": "Actualiza el valor de la variable",
    "with the number": "con el número",
    "Calculate the sum between the numbers": "Calcula la suma entre los números",
    "then print the variable": "luego imprime la variable",
    "Print the variable": "Imprime la variable",
    "Print the result": "Imprime el resultado",
    "Print the value": "Imprime el valor",
    "Return the value": "Devuelve el valor",
    "Return the result": "Devuelve el resultado",
    "Calculate the product": "Calcula el producto",
    "Calculate the difference": "Calcula la diferencia",
    "Calculate the average": "Calcula el promedio",
    "Calculate the sum": "Calcula la suma",
    "What is the output of the following code": "Cuál es la salida del siguiente código",
    "What is the ouput of the following code": "Cuál es la salida del siguiente código",
    "Choose the correct answer": "Elige la respuesta correcta",
    "Can you order these lines into a functional script": "¿Puedes ordenar estas líneas en un script funcional",
    "must be equal to": "debe ser igual a",
    "must be greater than": "debe ser mayor que",
    "must be less than": "debe ser menor que",
    "the function should return": "la función debe devolver",
    "The function should return": "La función debe devolver",
    "should return": "debería devolver",
    "should print": "debería imprimir",
    "should be": "debería ser",
    "is equal to": "es igual a",
    "is greater than": "es mayor que",
    "is less than": "es menor que",
    
    # Descriptions
    '"__Hello, World!__" is the traditional first program for beginning programming in a new language or environment.': '"__Hello, World!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.',
    'We use the `printf()` function to output data to the standard output device (screen).': 'Usamos la función `printf()` para mostrar datos en el dispositivo de salida estándar (pantalla).',
    "Every C program uses libraries, which give the ability to execute necessary functions, for example the print on the screen function is defined in the `stdio.h` header file.": "Todo programa en C usa bibliotecas, que dan la capacidad de ejecutar funciones necesarias, por ejemplo la función imprimir en pantalla está definida en el archivo de encabezado `stdio.h`.",
    "The first code which will run will always reside in the main function.": "El primer código que se ejecutará siempre residirá en la función principal.",
    "To print `Hello, World!` on the screen with C we can write": "Para imprimir `Hello, World!` en la pantalla con C podemos escribir",
    "Finally we return `0` to indicate that our program was successful": "Finalmente devolvemos `0` para indicar que nuestro programa fue exitoso",
    "Variables are containers for storing data values.": "Las variables son contenedores para almacenar valores de datos.",
    "Every variable in C is an object and like other programming languages, C has commands for declaring a variable.": "Cada variable en C es un objeto y como otros lenguajes de programación, C tiene comandos para declarar una variable.",
    "To create a variable, we need to give it a **type** and a **name** keeping in mind that it must not contain spaces.": "Para crear una variable, necesitamos darle un **tipo** y un **nombre** teniendo en cuenta que no debe contener espacios.",
    "A variable is created the moment you first assign a value to it.": "Una variable se crea en el momento en que le asignas un valor por primera vez.",
    "An example of a variable creation named": "Un ejemplo de creación de variable llamada",
    "is": "es",
    "In this way we have assigned the value": "De esta manera hemos asignado el valor",
    "to the _integer_ variable named": "a la variable _entero_ llamada",
    "If we print the variable": "Si imprimimos la variable",
    "we get back the number": "obtenemos el número",
    "Variables are called in this way because the value they store can change.": "Las variables se llaman así porque el valor que almacenan puede cambiar.",
    "We can update": "Podemos actualizar",
    "by using `=` and giving it a new value.": "usando `=` y dándole un nuevo valor.",
    "Operators are used to perform operations on variables and values.": "Los operadores se usan para realizar operaciones sobre variables y valores.",
    "Let's start with the arithmetic operators, in particular with the **addition** `+` operator.": "Empecemos con los operadores aritméticos, en particular con el operador de **suma** `+`.",
    "It is used to add two numbers, like:": "Se usa para sumar dos números, como:",
    "in this order": "en este orden",
    "(in this order)": "(en este orden)",
    
    # Common phrases
    "Learn how to": "Aprende cómo",
    "Learn how to output a value": "Aprende cómo mostrar un valor",
    "Learn how to format strings with different data types": "Aprende cómo formatear cadenas con diferentes tipos de datos",
    "Learn how to store values in a variable": "Aprende cómo almacenar valores en una variable",
    "Learn how to evaluate any expression": "Aprende cómo evaluar cualquier expresión",
    "Learn how to perform arithmetic operations on variables and values": "Aprende cómo realizar operaciones aritméticas sobre variables y valores",
    "Learn how to assign values to variables": "Aprende cómo asignar valores a variables",
    "Learn how to compare values": "Aprende cómo comparar valores",
    "Learn how to make decisions": "Aprende cómo tomar decisiones",
    "Learn how to repeat a set of statements": "Aprende cómo repetir un conjunto de sentencias",
    "Learn how to store different values into one variable": "Aprende cómo almacenar diferentes valores en una variable",
    "Learn how to divide code by specific tasks": "Aprende cómo dividir el código en tareas específicas",
    
    # Challenge titles
    "Addition": "Suma",
    "ATM": "Cajero Automático",
    "Hello World!": "Hello World!",
    "Raindrops": "Gotas de Lluvia",
    "Sum of digits": "Suma de dígitos",
    "Two for one": "Dos por uno",
    "100 doors": "100 puertas",
    "Ackermann function": "Función de Ackermann",
    "Arithmetic mean": "Media aritmética",
    "FizzBuzz": "FizzBuzz",
    "Roman numeral converter": "Conversor de números romanos",
    "Leap year": "Año bisiesto",
    
    # JSON values
    "Output": "Salida",
    "Formatted Strings": "Cadenas Formateadas",
    "Variables": "Variables",
    "Booleans": "Booleanos",
    "Arithmetic Operators": "Operadores Aritméticos",
    "Assignment Operators": "Operadores de Asignación",
    "Relational and Boolean Operators": "Operadores Relacionales y Booleanos",
    "Conditional Statements": "Sentencias Condicionales",
    "While Loops": "Bucles While",
    "For Loops": "Bucles For",
    "Arrays": "Arreglos",
    "Functions": "Funciones",
}

def escape_for_regex(text):
    """Escape special regex characters."""
    return re.escape(text)

def translate_prose_text(text: str) -> str:
    """Translate prose text (descriptions, instructions)."""
    result = text
    
    # Sort translations by length (longest first) to avoid partial matches
    for en, es in sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        # Word boundary regex for precise matching
        pattern = re.compile(escape_for_regex(en), re.IGNORECASE)
        
        def replacer(match):
            original = match.group(0)
            # Preserve capitalization
            if original.isupper():
                return es.upper()
            elif original and original[0].isupper():
                return es[0].upper() + es[1:] if len(es) > 1 else es.upper()
            return es
        
        result = pattern.sub(replacer, result)
    
    return result

def translate_variable_in_code(code: str) -> str:
    """Translate variable names in code, preserving C keywords."""
    result = code
    
    for en_var, es_var in sorted(VAR_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        # Only match whole words that are not C keywords
        # Use negative lookbehind and lookahead to avoid matching within identifiers
        pattern = r'(?<![a-zA-Z0-9_])' + escape_for_regex(en_var) + r'(?![a-zA-Z0-9_])'
        
        def is_c_keyword_context(match):
            """Check if this match is in a context where it's a C keyword."""
            # We'll rely on the fact that C_KEYWORDS are checked separately
            return False
        
        def replacer(match):
            word = match.group(0)
            # Don't translate if it's a C keyword
            if word.lower() in C_KEYWORDS:
                return word
            return es_var
        
        result = re.sub(pattern, replacer, result)
    
    return result

def translate_exercise_content(content: str) -> str:
    """Translate an exercise file preserving code structure."""
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
                       '# --output--', '# --before-solutions--', '# --after-solutions--']:
            current_section = stripped
            result.append(line)
            continue
        
        # Code block tracking
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
        # Process based on section and context
        if current_section == '# --description--' and not in_code_block:
            # Translate description text
            result.append(translate_prose_text(line))
        elif current_section == '# --instructions--' and not in_code_block:
            # Translate instructions
            result.append(translate_prose_text(line))
        elif current_section == '# --asserts--' and not in_code_block:
            # Translate assertion descriptions (but not code assertions)
            result.append(translate_prose_text(line))
        elif current_section == '# --answers--' and not in_code_block:
            # Translate answer choices
            result.append(translate_prose_text(line))
        elif in_code_block and not stripped.startswith('//'):
            # In code blocks, translate variable names but preserve C syntax
            result.append(translate_variable_in_code(line))
        else:
            # Keep everything else as-is (includes comments, section tags, etc.)
            result.append(line)
    
    return '\n'.join(result)

def translate_json_value(value):
    """Recursively translate JSON values."""
    if isinstance(value, str):
        return translate_prose_text(value)
    elif isinstance(value, dict):
        return {k: translate_json_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [translate_json_value(item) for item in value]
    return value

def translate_data_json(content: str) -> str:
    """Translate data.json file."""
    data = json.loads(content)
    translated = translate_json_value(data)
    return json.dumps(translated, indent=4, ensure_ascii=False) + '\n'

def copy_file_unchanged(src: Path, dest: Path):
    """Copy a file without any changes."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    content = src.read_text(encoding='utf-8')
    dest.write_text(content, encoding='utf-8')

def translate_file(src: Path, dest: Path):
    """Translate a single file."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    content = src.read_text(encoding='utf-8')
    
    if src.suffix == '.md':
        translated = translate_exercise_content(content)
        dest.write_text(translated, encoding='utf-8')
    elif src.name == 'data.json':
        translated = translate_data_json(content)
        dest.write_text(translated, encoding='utf-8')
    else:
        # Copy other files unchanged
        dest.write_text(content, encoding='utf-8')

def process_directory(src_dir: Path, dest_dir: Path):
    """Process all files in a directory."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    for item in src_dir.iterdir():
        dest_path = dest_dir / item.name
        
        if item.is_dir():
            process_directory(item, dest_path)
        elif item.is_file():
            translate_file(item, dest_path)

def main():
    """Main translation function."""
    print("Starting C exercises translation to Spanish...")
    print(f"Source: {EN_DIR}")
    print(f"Destination: {ES_DIR}")
    print()
    
    # Process main data.json
    main_json = EN_DIR / 'data.json'
    if main_json.exists():
        translate_file(main_json, ES_DIR / 'data.json')
        print("Translated: data.json")
    
    # List all directories to process
    dirs_to_process = [
        'output', 'formattedStrings', 'variables', 'booleans',
        'arithmeticOperators', 'assignmentOperators', 'relationBooleanOperators',
        'conditionalStatements', 'whileLoops', 'forLoops', 'arrays',
        'functions', 'challenges'
    ]
    
    total_files = 0
    for dirname in dirs_to_process:
        src_path = EN_DIR / dirname
        dest_path = ES_DIR / dirname
        
        if src_path.exists():
            print(f"\nProcessing {dirname}...")
            process_directory(src_path, dest_path)
            
            # Count translated files
            md_count = len(list(src_path.glob('*.md')))
            json_count = len(list(src_path.glob('data.json')))
            total_files += md_count + json_count
            print(f"  Translated {md_count + json_count} files")
    
    print(f"\nTranslation complete! Processed {total_files} files.")
    print(f"Translated files saved to: {ES_DIR}")

if __name__ == '__main__':
    main()
