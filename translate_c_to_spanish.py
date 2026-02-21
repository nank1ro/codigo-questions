#!/usr/bin/env python3
"""
Translation script for C exercises from English to Spanish.
Translates all user-facing text while preserving code structure.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List

# Base directories
BASE_DIR = Path("/Users/ale/github/codigo-questions")
EN_DIR = BASE_DIR / "en" / "c"
ES_DIR = BASE_DIR / "es" / "c"

# Variable name translations (English -> Spanish)
VAR_TRANSLATIONS = {
    # Common variable names
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
    "output": "salida",
    "input": "entrada",
    "character": "caracter",
    "characters": "caracteres",
    "word": "palabra",
    "words": "palabras",
    "sentence": "frase",
    "flag": "bandera",
    "found": "encontrado",
    "valid": "valido",
    "status": "estado",
    "error": "error",
    "success": "exito",
    "response": "respuesta",
    "data": "datos",
    "array": "arreglo",
    "list": "lista",
    "element": "elemento",
    "position": "posicion",
    "size": "tamano",
    "maximum": "maximo",
    "minimum": "minimo",
    "max": "max",
    "min": "min",
    "first": "primero",
    "second": "segundo",
    "third": "tercero",
    "last": "ultimo",
    "next": "siguiente",
    "previous": "anterior",
    "current": "actual",
    "temp": "temporal",
    "counter": "contador",
    "i": "i",  # Loop variables stay same
    "j": "j",
    "k": "k",
    "x": "x",
    "y": "y",
    "z": "z",
    "n": "n",
    "a": "a",
    "b": "b",
    "c": "c",
    "base": "base",
    "exponent": "exponente",
    "radius": "radio",
    "side": "lado",
    "radius": "radio",
    "factor": "factor",
    "multiplier": "multiplicador",
    "divisor": "divisor",
    "operand": "operando",
    "operand1": "operando1",
    "operand2": "operando2",
    "boolean": "booleano",
    "condition": "condicion",
    "isTrue": "esVerdadero",
    "isFalse": "esFalso",
    "isEqual": "esIgual",
    "isGreater": "esMayor",
    "isLess": "esMenor",
    "digit": "digito",
    "digits": "digitos",
    "sum_of_digits": "suma_de_digitos",
    "reverse": "reverso",
    "reversed": "revertido",
    "original": "original",
    "new": "nuevo",
    "old": "viejo",
    "updated": "actualizado",
    "changed": "cambiado",
    "user": "usuario",
    "password": "contrasena",
    "email": "correo",
    "username": "nombre_usuario",
    "letter": "letra",
    "letters": "letras",
    "string": "cadena",
    "strings": "cadenas",
    "integer": "entero",
    "float": "flotante",
    "double": "doble",
    "matrix": "matriz",
    "row": "fila",
    "rows": "filas",
    "column": "columna",
    "columns": "columnas",
    "table": "tabla",
    "key": "clave",
    "value": "valor",
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
    "datetime": "fecha_hora",
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

# Common phrases translations
PHRASE_TRANSLATIONS = {
    # Instructions
    "Your program should print": "Tu programa debe imprimir",
    "Your program should output": "Tu programa debe mostrar",
    "Write a function that": "Escribe una función que",
    "Write a program that": "Escribe un programa que",
    "Create a function that": "Crea una función que",
    "Create a variable": "Crea una variable",
    "Declare a variable": "Declara una variable",
    "Assign to the variable": "Asigna a la variable",
    "Update the value of the variable": "Actualiza el valor de la variable",
    "Calculate the sum": "Calcula la suma",
    "Calculate the product": "Calcula el producto",
    "Calculate the difference": "Calcula la diferencia",
    "Calculate the average": "Calcula el promedio",
    "Print the variable": "Imprime la variable",
    "Print the result": "Imprime el resultado",
    "Print the value": "Imprime el valor",
    "Return the value": "Devuelve el valor",
    "Return the result": "Devuelve el resultado",
    "Return": "Devuelve",
    "Output": "Muestra",
    "Display": "Muestra",
    "Show": "Muestra",
    "store": "almacenar",
    "Store": "Almacena",
    "add": "agregar",
    "Add": "Agrega",
    "remove": "eliminar",
    "Remove": "Elimina",
    "delete": "borrar",
    "Delete": "Borra",
    "insert": "insertar",
    "Insert": "Inserta",
    "append": "agregar",
    "Append": "Agrega al final",
    "push": "empujar",
    "pop": "sacar",
    "peek": "ver",
    "contains": "contiene",
    "is empty": "está vacío",
    "is not empty": "no está vacío",
    "is equal to": "es igual a",
    "is not equal to": "no es igual a",
    "is greater than": "es mayor que",
    "is less than": "es menor que",
    "is greater than or equal to": "es mayor o igual que",
    "is less than or equal to": "es menor o igual que",
    "What is the output": "Cuál es la salida",
    "What is the result": "Cuál es el resultado",
    "What is the value": "Cuál es el valor",
    "Choose the correct answer": "Elige la respuesta correcta",
    "Select the correct option": "Selecciona la opción correcta",
    "Which of the following": "Cuál de los siguientes",
    "Can you order these lines": "¿Puedes ordenar estas líneas",
    "Order the code": "Ordena el código",
    "Arrange the following": "Organiza lo siguiente",
    "must be equal to": "debe ser igual a",
    "must be": "debe ser",
    "should be": "debería ser",
    "should return": "debería devolver",
    "should print": "debería imprimir",
    "between the numbers": "entre los números",
    "from the array": "del arreglo",
    "in the array": "en el arreglo",
    "to the array": "al arreglo",
    "in this order": "en este orden",
    "and then": "y luego",
    "then print": "luego imprime",
    "followed by": "seguido por",
    "using": "usando",
    "with": "con",
    "without": "sin",
    "from": "desde",
    "to": "hasta",
    "for": "para",
    "each": "cada",
    "all": "todos",
    "every": "cada",
    "some": "algunos",
    "any": "algún",
    "none": "ninguno",
    "both": "ambos",
    "either": "cualquiera",
    "neither": "ninguno de los dos",
    "if": "si",
    "else": "sino",
    "when": "cuando",
    "while": "mientras",
    "until": "hasta",
    "through": "a través de",
    "during": "durante",
    "before": "antes de",
    "after": "después de",
    "at the beginning": "al principio",
    "at the end": "al final",
    "first element": "primer elemento",
    "last element": "último elemento",
    "next element": "siguiente elemento",
    "previous element": "elemento anterior",
    "current element": "elemento actual",
    "empty string": "cadena vacía",
    "null value": "valor nulo",
    "zero": "cero",
    "one": "uno",
    "two": "dos",
    "three": "tres",
    "four": "cuatro",
    "five": "cinco",
    "six": "seis",
    "seven": "siete",
    "eight": "ocho",
    "nine": "nueve",
    "ten": "diez",
    "number of": "número de",
    "count of": "cantidad de",
    "sum of": "suma de",
    "product of": "producto de",
    "difference between": "diferencia entre",
    "quotient of": "cociente de",
    "remainder of": "resto de",
    "the function should return": "la función debe devolver",
    "the variable": "la variable",
    "the value": "el valor",
    "the result": "el resultado",
    "the array": "el arreglo",
    "the string": "la cadena",
    "the number": "el número",
    "the character": "el carácter",
    "an integer": "un entero",
    "a float": "un flotante",
    "a string": "una cadena",
    "a character": "un carácter",
    "an array": "un arreglo",
    "a function": "una función",
    "a variable": "una variable",
    "a loop": "un bucle",
    "a condition": "una condición",
    "a statement": "una sentencia",
    "an expression": "una expresión",
    "a comment": "un comentario",
    "an error": "un error",
    "an exception": "una excepción",
    "the following": "lo siguiente",
    "below": "abajo",
    "above": "arriba",
    "here": "aquí",
    "there": "allí",
    "this": "esto",
    "that": "eso",
    "these": "estos",
    "those": "esos",
    "learn how to": "aprende cómo",
    "Learn how to": "Aprende cómo",
    "is the traditional first program": "es el primer programa tradicional",
    "is the traditional": "es el tradicional",
    "for beginning programming": "para comenzar a programar",
    "in a new language": "en un nuevo lenguaje",
    "or environment": "o entorno",
    "We use the": "Usamos el",
    "function to": "función para",
    "output data to": "mostrar datos en",
    "the standard output device": "el dispositivo de salida estándar",
    "screen": "pantalla",
    "Every C program uses libraries": "Todo programa en C usa bibliotecas",
    "which give the ability to": "que dan la capacidad de",
    "execute necessary functions": "ejecutar funciones necesarias",
    "for example": "por ejemplo",
    "the print on the screen function": "la función imprimir en pantalla",
    "is defined in the": "está definida en el",
    "header file": "archivo de encabezado",
    "The first code which will run": "El primer código que se ejecutará",
    "will always reside in": "siempre residirá en",
    "the main function": "la función principal",
    "To print": "Para imprimir",
    "on the screen with C": "en la pantalla con C",
    "we can write": "podemos escribir",
    "Finally we return": "Finalmente devolvemos",
    "to indicate that": "para indicar que",
    "our program was successful": "nuestro programa fue exitoso",
    "are containers for storing data values": "son contenedores para almacenar valores de datos",
    "are called in this way because": "se llaman así porque",
    "the value they store can change": "el valor que almacenan puede cambiar",
    "We can update": "Podemos actualizar",
    "by using": "usando",
    "and giving it a new value": "y dándole un nuevo valor",
    "To create a variable": "Para crear una variable",
    "we need to give it a": "necesitamos darle una",
    "type": "tipo",
    "name": "nombre",
    "keeping in mind that": "teniendo en cuenta que",
    "it must not contain spaces": "no debe contener espacios",
    "is created the moment you": "se crea en el momento en que",
    "first assign a value to it": "le asignas un valor por primera vez",
    "An example of a": "Un ejemplo de",
    "creation named": "creación llamado",
    "is": "es",
    "In this way we have assigned the value": "De esta manera hemos asignado el valor",
    "to the": "al",
    "variable named": "variable llamada",
    "If we print the": "Si imprimimos la",
    "we get back the number": "obtenemos el número",
    "Operators are used to": "Los operadores se usan para",
    "perform operations on": "realizar operaciones sobre",
    "variables and values": "variables y valores",
    "Let's start with": "Empecemos con",
    "in particular with the": "en particular con el",
    "operator": "operador",
    "It is used to": "Se usa para",
    "add two numbers": "sumar dos números",
    "subtract two numbers": "restar dos números",
    "multiply two numbers": "multiplicar dos números",
    "divide two numbers": "dividir dos números",
    "like": "como",
    "Calculate the sum between": "Calcula la suma entre",
    "(in this order)": "(en este orden)",
    "then print the variable": "luego imprime la variable",
    "What is the ouput of the following code": "Cuál es la salida del siguiente código",
    "Can you order these lines into a functional script": "¿Puedes ordenar estas líneas en un script funcional",
}

# Section headers - keep these untranslated
SECTION_TAGS = [
    "# --description--",
    "# --instructions--",
    "# --seed--",
    "# --answers--",
    "# --solutions--",
    "# --asserts--",
    "# --before-seed--",
    "# --after-seed--",
    "# --before-asserts--",
    "# --after-asserts--",
    "# --output--",
    "# --before-solutions--",
    "# --after-solutions--",
]

def translate_text(text: str, in_code_block: bool = False) -> str:
    """Translate text content while preserving code elements."""
    if not text:
        return text
    
    result = text
    
    # Apply phrase translations (longer phrases first)
    for en, es in sorted(PHRASE_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        # Case-insensitive replacement with smart casing
        pattern = re.compile(re.escape(en), re.IGNORECASE)
        
        def replace_match(match):
            original = match.group(0)
            # Preserve original casing pattern
            if original.isupper():
                return es.upper()
            elif original[0].isupper():
                return es[0].upper() + es[1:]
            return es
        
        result = pattern.sub(replace_match, result)
    
    # Translate variable names in code (but not keywords)
    if in_code_block or result.startswith("```"):
        for en_var, es_var in VAR_TRANSLATIONS.items():
            # Only translate if it's a standalone identifier (word boundaries)
            # But avoid translating C keywords, function names, or strings
            pattern = r'\b' + re.escape(en_var) + r'\b'
            result = re.sub(pattern, es_var, result)
    
    return result

def translate_frontmatter(content: str) -> str:
    """Translate frontmatter values (keep keys intact)."""
    lines = content.split('\n')
    in_frontmatter = False
    result = []
    
    for line in lines:
        if line.strip() == '---':
            if not in_frontmatter:
                in_frontmatter = True
            else:
                in_frontmatter = False
            result.append(line)
        elif in_frontmatter:
            # Translate frontmatter values
            if ':' in line and not line.strip().startswith('#'):
                key, value = line.split(':', 1)
                value = value.strip()
                if value and not value.isdigit() and value not in ['c', '1', '2', '3', '4']:
                    # Translate the value
                    translated = translate_text(value)
                    result.append(f"{key}:{translated}")
                else:
                    result.append(line)
            else:
                result.append(line)
        else:
            result.append(line)
    
    return '\n'.join(result)

def translate_exercise_file(content: str) -> str:
    """Translate a single exercise file."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    current_section = None
    
    for line in lines:
        # Check for section tags
        if line.strip() in SECTION_TAGS:
            current_section = line.strip()
            in_code_block = False
            result.append(line)
            continue
        
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
        # Skip empty lines and comments in code
        if not line.strip() or (in_code_block and line.strip().startswith('//')):
            result.append(line)
            continue
        
        # Translate based on section
        if current_section == "# --description--" and not in_code_block:
            result.append(translate_text(line))
        elif current_section == "# --instructions--" and not in_code_block:
            result.append(translate_text(line))
        elif current_section == "# --asserts--" and not in_code_block:
            # Translate assertion descriptions
            result.append(translate_text(line))
        elif current_section == "# --answers--" and not in_code_block:
            # Translate answer options
            result.append(translate_text(line))
        elif in_code_block:
            # Translate variable names in code
            result.append(translate_text(line, in_code_block=True))
        else:
            result.append(line)
    
    return '\n'.join(result)

def translate_data_json(content: str) -> str:
    """Translate data.json file."""
    data = json.loads(content)
    
    def translate_value(obj):
        if isinstance(obj, dict):
            result = {}
            for key, value in obj.items():
                if key in ['title', 'description', 'name']:
                    result[key] = translate_text(value)
                else:
                    result[key] = value
            return result
        return obj
    
    return json.dumps(translate_value(data), indent=4, ensure_ascii=False) + '\n'

def process_directory(src_dir: Path, dest_dir: Path):
    """Process all files in a directory."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    for item in src_dir.iterdir():
        if item.is_file():
            if item.suffix == '.md':
                # Read and translate markdown file
                content = item.read_text(encoding='utf-8')
                translated = translate_exercise_file(content)
                (dest_dir / item.name).write_text(translated, encoding='utf-8')
                print(f"Translated: {item.name}")
            elif item.name == 'data.json':
                # Read and translate data.json
                content = item.read_text(encoding='utf-8')
                translated = translate_data_json(content)
                (dest_dir / item.name).write_text(translated, encoding='utf-8')
                print(f"Translated: {item.name}")
            else:
                # Copy other files as-is
                content = item.read_text(encoding='utf-8')
                (dest_dir / item.name).write_text(content, encoding='utf-8')

def main():
    """Main translation function."""
    print("Starting C exercises translation to Spanish...")
    print(f"Source: {EN_DIR}")
    print(f"Destination: {ES_DIR}")
    print()
    
    # Create destination directory
    ES_DIR.mkdir(parents=True, exist_ok=True)
    
    # Process main data.json
    if (EN_DIR / 'data.json').exists():
        content = (EN_DIR / 'data.json').read_text(encoding='utf-8')
        translated = translate_data_json(content)
        (ES_DIR / 'data.json').write_text(translated, encoding='utf-8')
        print("Translated: data.json (main)")
    
    # List of directories to process (in order)
    directories = [
        'output',
        'formattedStrings',
        'variables',
        'booleans',
        'arithmeticOperators',
        'assignmentOperators',
        'relationBooleanOperators',
        'conditionalStatements',
        'whileLoops',
        'forLoops',
        'arrays',
        'functions',
        'challenges',
    ]
    
    total_files = 0
    for dirname in directories:
        src_path = EN_DIR / dirname
        dest_path = ES_DIR / dirname
        
        if src_path.exists() and src_path.is_dir():
            print(f"\nProcessing {dirname}...")
            process_directory(src_path, dest_path)
            
            # Count files
            file_count = len(list(src_path.glob('*.md'))) + len(list(src_path.glob('data.json')))
            total_files += file_count
    
    print(f"\nTranslation complete! Processed {total_files} files.")
    print(f"Translated files saved to: {ES_DIR}")

if __name__ == '__main__':
    main()
