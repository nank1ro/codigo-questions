#!/usr/bin/env python3
"""
Translates JavaScript exercises from English to Spanish.
Translates user-facing text while preserving code structure, keywords, and section tags.
"""

import json
import os
import re
import shutil
from pathlib import Path

# Variable name translations (English -> Spanish)
VAR_TRANSLATIONS = {
    # Common variable names
    'sum': 'suma',
    'count': 'conteo',
    'result': 'resultado',
    'total': 'total',
    'value': 'valor',
    'name': 'nombre',
    'number': 'numero',
    'numbers': 'numeros',
    'index': 'indice',
    'length': 'longitud',
    'size': 'tamano',
    'item': 'elemento',
    'items': 'elementos',
    'array': 'arreglo',
    'product': 'producto',
    'difference': 'diferencia',
    'quotient': 'cociente',
    'remainder': 'resto',
    'average': 'promedio',
    'mean': 'media',
    'max': 'maximo',
    'min': 'minimo',
    'first': 'primero',
    'last': 'ultimo',
    'next': 'siguiente',
    'previous': 'anterior',
    'current': 'actual',
    'temp': 'temporal',
    'output': 'salida',
    'input': 'entrada',
    'text': 'texto',
    'message': 'mensaje',
    'error': 'error',
    'data': 'datos',
    'status': 'estado',
    'flag': 'bandera',
    'isTrue': 'esVerdadero',
    'isFalse': 'esFalso',
    'isValid': 'esValido',
    'isEmpty': 'estaVacio',
    'hasValue': 'tieneValor',
    'found': 'encontrado',
    'search': 'busqueda',
    'replace': 'reemplazar',
    'substring': 'subcadena',
    'character': 'caracter',
    'position': 'posicion',
    'start': 'inicio',
    'end': 'fin',
    'middle': 'medio',
    'left': 'izquierda',
    'right': 'derecha',
    'top': 'superior',
    'bottom': 'inferior',
    'width': 'ancho',
    'height': 'alto',
    'x': 'x',
    'y': 'y',
    'z': 'z',
    'i': 'i',
    'j': 'j',
    'k': 'k',
    'n': 'n',
    'm': 'm',
    'count': 'conteo',
    'counter': 'contador',
    'index': 'indice',
    'loop': 'bucle',
    'condition': 'condicion',
    'statement': 'declaracion',
    'expression': 'expresion',
    'function': 'funcion',
    'method': 'metodo',
    'parameter': 'parametro',
    'argument': 'argumento',
    'return': 'retorno',
    'class': 'clase',
    'object': 'objeto',
    'property': 'propiedad',
    'key': 'clave',
    'val': 'valor',
    'entry': 'entrada',
    'map': 'mapa',
    'set': 'conjunto',
    'list': 'lista',
    'queue': 'cola',
    'stack': 'pila',
    'tree': 'arbol',
    'node': 'nodo',
    'root': 'raiz',
    'leaf': 'hoja',
    'branch': 'rama',
    'parent': 'padre',
    'child': 'hijo',
    'sibling': 'hermano',
    'time': 'tiempo',
    'date': 'fecha',
    'year': 'anio',
    'month': 'mes',
    'day': 'dia',
    'hour': 'hora',
    'minute': 'minuto',
    'second': 'segundo',
    'musicOn': 'musicaActivada',
    'niceWeather': 'buenClima',
    'num1': 'numero1',
    'num2': 'numero2',
    'num3': 'numero3',
    'sumResult': 'resultadoSuma',
    'multResult': 'resultadoMultiplicacion',
    'divResult': 'resultadoDivision',
    'modResult': 'resultadoModulo',
    'base': 'base',
    'exponent': 'exponente',
    'power': 'potencia',
    'square': 'cuadrado',
    'cube': 'cubo',
    'factorial': 'factorial',
    'fibonacci': 'fibonacci',
    'prime': 'primo',
    'isPrime': 'esPrimo',
    'even': 'par',
    'odd': 'impar',
    'multiple': 'multiplo',
    'divisor': 'divisor',
    'str': 'cadena',
    'string': 'cadena',
    'char': 'caracter',
    'bool': 'booleano',
    'boolean': 'booleano',
    'int': 'entero',
    'integer': 'entero',
    'float': 'flotante',
    'double': 'doble',
    'arr': 'arreglo',
    'obj': 'objeto',
    'func': 'funcion',
    'fn': 'fn',
    'cb': 'retornoLlamada',
    'callback': 'retornoLlamada',
    'promise': 'promesa',
    'async': 'asincrono',
    'await': 'esperar',
    'tryCatch': 'intentarCapturar',
    'num1': 'numero1',
    'num2': 'numero2',
    'num3': 'numero3',
    'numA': 'numeroA',
    'numB': 'numeroB',
    'numX': 'numeroX',
    'numY': 'numeroY',
    'myVar': 'miVariable',
    'myArray': 'miArreglo',
    'myObject': 'miObjeto',
    'myFunction': 'miFuncion',
    'myString': 'miCadena',
    'myNumber': 'miNumero',
    'testVar': 'variablePrueba',
    'demoValue': 'valorDemo',
    'sample': 'muestra',
    'example': 'ejemplo',
    'newVar': 'nuevaVariable',
    'oldVar': 'variableAntigua',
    'tempVar': 'variableTemporal',
    'firstName': 'nombre',
    'lastName': 'apellido',
    'fullName': 'nombreCompleto',
    'email': 'correo',
    'password': 'contrasena',
    'username': 'nombreUsuario',
    'userId': 'idUsuario',
    'user': 'usuario',
    'admin': 'administrador',
    'guest': 'invitado',
    'member': 'miembro',
    'role': 'rol',
    'permission': 'permiso',
    'config': 'configuracion',
    'settings': 'configuracion',
    'options': 'opciones',
    'params': 'parametros',
    'args': 'argumentos',
    'props': 'propiedades',
    'state': 'estado',
    'context': 'contexto',
    'store': 'tienda',
    'reducer': 'reductor',
    'action': 'accion',
    'dispatch': 'despachar',
    'effect': 'efecto',
    'memo': 'memo',
    'ref': 'referencia',
    'useEffect': 'usarEfecto',
    'useState': 'usarEstado',
    'useRef': 'usarReferencia',
    'useMemo': 'usarMemo',
    'useCallback': 'usarRetornoLlamada',
}

# Text translations (English -> Spanish)
TEXT_TRANSLATIONS = {
    # Common phrases
    'Hello, World!': '¡Hola, mundo!',
    'Hello, World': 'Hola, mundo',
    'Hello, JavaScript!': '¡Hola, JavaScript!',
    'Hello JavaScript!': '¡Hola, JavaScript!',
    "Hello, JavaScript!": "¡Hola, JavaScript!",
    'Hello': 'Hola',
    'World': 'Mundo',
    'JavaScript': 'JavaScript',

    # Exercise instruction phrases
    'Assign to the variable': 'Asigna a la variable',
    'the value': 'el valor',
    'Complete the code': 'Completa el código',
    'in order to create a valid': 'para crear un/a',
    'array': 'arreglo',
    'function': 'función',
    'object': 'objeto',
    'class': 'clase',
    'statement': 'declaración',
    'loop': 'bucle',
    'Your program should print': 'Tu programa debe imprimir',
    'on the screen': 'en la pantalla',
    'Write a function that returns': 'Escribe una función que devuelva',
    'the string': 'la cadena',
    'Create an': 'Crea un/a',
    'statement': 'declaración',
    'checking if': 'verificando si',
    'is lower than': 'es menor que',
    'is greater than': 'es mayor que',
    'is equal to': 'es igual a',
    'then in the code block print': 'luego en el bloque de código imprime',
    'Can you order these lines into a functional code?': '¿Puedes ordenar estas líneas en un código funcional?',
    'What is the ouput of the following code?': '¿Cuál es la salida del siguiente código?',
    'Do the same with the code below': 'Haz lo mismo con el código de abajo',

    # Common words
    'and': 'y',
    'or': 'o',
    'but': 'pero',
    'if': 'si',
    'else': 'sino',
    'then': 'entonces',
    'when': 'cuando',
    'while': 'mientras',
    'for': 'para',
    'from': 'desde',
    'to': 'a',
    'with': 'con',
    'without': 'sin',
    'using': 'usando',
    'use': 'usa',
    'into': 'en',
    'inside': 'dentro',
    'outside': 'fuera',
    'between': 'entre',
    'through': 'a través',
    'during': 'durante',
    'before': 'antes de',
    'after': 'después de',
    'above': 'encima de',
    'below': 'debajo de',
    'under': 'bajo',
    'over': 'sobre',
    'again': 'de nuevo',
    'once': 'una vez',
    'twice': 'dos veces',
    'always': 'siempre',
    'never': 'nunca',
    'sometimes': 'a veces',
    'usually': 'generalmente',
    'often': 'frecuentemente',
    'rarely': 'rara vez',
    'now': 'ahora',
    'later': 'más tarde',
    'soon': 'pronto',
    'already': 'ya',
    'not yet': 'todavía no',
    'still': 'todavía',
    'also': 'también',
    'too': 'también',
    'very': 'muy',
    'quite': 'bastante',
    'rather': 'más bien',
    'almost': 'casi',
    'nearly': 'casi',
    'hardly': 'apenas',
    'just': 'solo',
    'only': 'solamente',
    'even': 'incluso',
    'exactly': 'exactamente',
    'approximately': 'aproximadamente',
    'about': 'aproximadamente',
    'around': 'alrededor de',
    'here': 'aquí',
    'there': 'allí',
    'everywhere': 'en todas partes',
    'somewhere': 'en algún lugar',
    'anywhere': 'en cualquier lugar',
    'nowhere': 'en ningún sitio',

    # Programming concepts
    'variable': 'variable',
    'function': 'función',
    'method': 'método',
    'argument': 'argumento',
    'parameter': 'parámetro',
    'return': 'devolver',
    'returns': 'devuelve',
    'array': 'arreglo',
    'object': 'objeto',
    'string': 'cadena',
    'number': 'número',
    'boolean': 'booleano',
    'true': 'verdadero',
    'false': 'falso',
    'null': 'nulo',
    'undefined': 'indefinido',
    'loop': 'bucle',
    'condition': 'condición',
    'statement': 'declaración',
    'expression': 'expresión',
    'operator': 'operador',
    'comment': 'comentario',
    'syntax': 'sintaxis',
    'error': 'error',
    'exception': 'excepción',
    'debug': 'depurar',
    'compile': 'compilar',
    'execute': 'ejecutar',
    'run': 'ejecutar',
    'print': 'imprimir',
    'output': 'salida',
    'input': 'entrada',
    'value': 'valor',
    'type': 'tipo',
    'length': 'longitud',
    'size': 'tamaño',
    'index': 'índice',
    'position': 'posición',
    'element': 'elemento',
    'item': 'elemento',
    'property': 'propiedad',
    'key': 'clave',
    'class': 'clase',
    'instance': 'instancia',
    'constructor': 'constructor',
    'prototype': 'prototipo',
    'inheritance': 'herencia',
    'scope': 'ámbito',
    'closure': 'cierre',
    'callback': 'retorno de llamada',
    'promise': 'promesa',
    'async': 'asíncrono',
    'await': 'esperar',
    'module': 'módulo',
    'import': 'importar',
    'export': 'exportar',
    'default': 'predeterminado',
    'const': 'const',
    'let': 'let',
    'var': 'var',
    'this': 'esto',
    'super': 'super',
    'extends': 'extiende',
    'static': 'estático',
    'get': 'obtener',
    'set': 'establecer',
    'try': 'intentar',
    'catch': 'capturar',
    'finally': 'finalmente',
    'throw': 'lanzar',
    'new': 'nuevo',
    'delete': 'eliminar',
    'typeof': 'tipo de',
    'instanceof': 'instancia de',
    'in': 'en',
    'of': 'de',
    'void': 'vacío',
}

# Data.json title and description translations
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
ERROR_TAGS = [
    '--err-t',
]

# DO NOT EDIT comments
DO_NOT_EDIT_PATTERNS = [
    '// DO NOT EDIT FROM HERE',
    '// DO NOT EDIT UNTIL HERE',
]

def translate_var_name(match):
    """Translate a variable name while preserving context."""
    var_name = match.group(0)
    # Preserve original capitalization pattern
    if var_name in VAR_TRANSLATIONS:
        return VAR_TRANSLATIONS[var_name]
    # Try lowercase version
    if var_name.lower() in VAR_TRANSLATIONS:
        translated = VAR_TRANSLATIONS[var_name.lower()]
        # Preserve original capitalization
        if var_name[0].isupper():
            return translated[0].upper() + translated[1:]
        return translated
    return var_name

def translate_text_content(text, in_code_block=False, in_string_literal=False):
    """Translate user-facing text while preserving code structure."""
    if not text or text.strip() == '':
        return text

    # Don't translate if it's just a number, symbol, or single word that's code
    if in_code_block and not in_string_literal:
        # Check if this is a string literal
        if text.strip().startswith('"') or text.strip().startswith("'") or text.strip().startswith('`'):
            # This is a string literal, translate its content
            return translate_string_literal(text)

        # In code blocks but not in string literals - only translate variable names
        # Don't translate keywords, operators, or function calls
        return text

    # Translate full text content outside code
    result = text
    for en, es in sorted(TEXT_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        # Use word boundaries for whole word replacement
        pattern = r'\b' + re.escape(en) + r'\b'
        result = re.sub(pattern, es, result, flags=re.IGNORECASE)

    return result

def translate_string_literal(text):
    """Translate content inside string literals."""
    # Handle different quote types
    for quote in ['"""', "'''", '```', '"', "'", '`']:
        if text.startswith(quote) and text.endswith(quote):
            content = text[len(quote):-len(quote)]
            translated = translate_text_content(content, in_code_block=False, in_string_literal=True)
            return quote + translated + quote
    return text

def translate_line(line, in_code_block, in_string_literal):
    """Translate a single line while preserving structure."""
    result = line

    # Never translate section tags
    for tag in SECTION_TAGS:
        if tag in line:
            return line

    # Never translate DO NOT EDIT comments
    for pattern in DO_NOT_EDIT_PATTERNS:
        if pattern in line:
            return line

    # Never translate error tags like --err-t1--
    if any(tag in line for tag in ERROR_TAGS):
        # But translate the error message if present
        if 'failed' in line.lower():
            return line.replace('failed', 'falló').replace('Failed', 'Falló')
        return line

    # Preserve trailing spaces for fill-in-blank answers
    trailing_space = ''
    if line and not line.endswith('\n') and line.rstrip() != line:
        trailing_space = line[len(line.rstrip()):]

    # Translate string literals
    string_pattern = r'(["\'`])(?:(?=(\\?))\2.)*?\1'
    def replace_string(match):
        quote = match.group(1)
        content = match.group(0)[1:-1]
        # Translate content if it's user-facing text
        translated = content
        for en, es in sorted(TEXT_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
            if en in content and en not in ['var', 'let', 'const', 'function', 'return', 'if', 'else', 'for', 'while', 'class', 'extends', 'import', 'export', 'default', 'new', 'this', 'super', 'try', 'catch', 'finally', 'throw', 'typeof', 'instanceof']:
                translated = translated.replace(en, es)
        return quote + translated + quote

    result = re.sub(string_pattern, replace_string, result)

    # Translate variable names in certain contexts
    if in_code_block and not in_string_literal:
        # Translate variable names in declarations and assignments
        for var_en, var_es in sorted(VAR_TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
            # Match whole word variable names
            pattern = r'\b' + re.escape(var_en) + r'\b'
            result = re.sub(pattern, var_es, result)

    # Translate comments
    if '//' in result and not in_string_literal:
        comment_start = result.find('//')
        before_comment = result[:comment_start]
        comment = result[comment_start:]
        # Translate comment content
        translated_comment = translate_text_content(comment[2:], in_code_block=False, in_string_literal=False)
        result = before_comment + '//' + translated_comment

    # Translate inline text content (outside code blocks)
    if not in_code_block:
        result = translate_text_content(result, in_code_block=False, in_string_literal=False)

    if trailing_space:
        result = result.rstrip() + trailing_space

    return result

def translate_exercise_file(content):
    """Translate an exercise markdown file."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    code_fence = None
    in_yaml = False

    for i, line in enumerate(lines):
        # Check for YAML frontmatter
        if i == 0 and line.startswith('---'):
            in_yaml = True
            result.append(line)
            continue
        if in_yaml:
            result.append(line)
            if line.startswith('---'):
                in_yaml = False
            continue

        # Check for code blocks
        if line.strip().startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_fence = line.strip()[3:]
            else:
                in_code_block = False
                code_fence = None
            result.append(line)
            continue

        # Translate the line
        translated = translate_line(line, in_code_block, False)
        result.append(translated)

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
                        # Try to translate word by word
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
