#!/usr/bin/env python3
"""
Complete translation with comprehensive phrase mapping.
"""

import json
from pathlib import Path
from typing import Dict

BASE_DIR = Path("/Users/ale/github/codigo-questions")
EN_DIR = BASE_DIR / "en" / "c"
ES_DIR = BASE_DIR / "es" / "c"

# Complete translation map
TRANSLATIONS = {
    # Articles and connectors
    ' and ': ' y ',
    ' or ': ' o ',
    ' with ': ' con ',
    ' from ': ' de ',
    ' to ': ' a ',
    ' in ': ' en ',
    ' on ': ' en ',
    ' for ': ' para ',
    ' of ': ' de ',
    ' the ': ' el ' if True else ' the ',  # Context-dependent
    ' a ': ' un ',
    ' an ': ' un ',
    ' is ': ' es ',
    ' are ': ' son ',
    
    # Programming terms
    'output': 'salida',
    'print': 'imprimir',
    'store': 'almacenar',
    'value': 'valor',
    'values': 'valores',
    'variable': 'variable',
    'variables': 'variables',
    'function': 'función',
    'functions': 'funciones',
    'program': 'programa',
    'programs': 'programas',
    'code': 'código',
    'string': 'cadena',
    'strings': 'cadenas',
    'number': 'número',
    'numbers': 'números',
    'character': 'carácter',
    'array': 'arreglo',
    'operator': 'operador',
    'operators': 'operadores',
    'statement': 'sentencia',
    'statements': 'sentencias',
    'expression': 'expresión',
    'loop': 'bucle',
    'condition': 'condición',
    
    # Verbs
    'Write': 'Escribe',
    'Create': 'Crea',
    'Declare': 'Declara',
    'Assign': 'Asigna',
    'Update': 'Actualiza',
    'Calculate': 'Calcula',
    'Return': 'Devuelve',
    'Print': 'Imprime',
    'Show': 'Muestra',
    'Display': 'Muestra',
    'Use': 'Usa',
    'Get': 'Obtén',
    'Add': 'Agrega',
    'Remove': 'Elimina',
    'Insert': 'Inserta',
    'Order': 'Ordena',
    'Choose': 'Elige',
    'Select': 'Selecciona',
    
    # Nouns
    'sum': 'suma',
    'product': 'producto',
    'difference': 'diferencia',
    'quotient': 'cociente',
    'average': 'promedio',
    'result': 'resultado',
    'screen': 'pantalla',
    'keyboard': 'teclado',
    'device': 'dispositivo',
    'library': 'biblioteca',
    'libraries': 'bibliotecas',
    'command': 'comando',
    'commands': 'comandos',
    'type': 'tipo',
    'name': 'nombre',
    'container': 'contenedor',
    'containers': 'contenedores',
    'data': 'datos',
    'object': 'objeto',
    'objects': 'objetos',
    'language': 'lenguaje',
    'languages': 'lenguajes',
    'environment': 'entorno',
    'example': 'ejemplo',
    'stack': 'pila',
    'file': 'archivo',
    'header': 'encabezado',
    
    # Adjectives
    'traditional': 'tradicional',
    'necessary': 'necesarias',
    'standard': 'estándar',
    'first': 'primer',
    'second': 'segundo',
    'last': 'último',
    'new': 'nuevo',
    'integer': 'entero',
    'successful': 'exitoso',
    'functional': 'funcional',
    'correct': 'correcta',
    'equal': 'igual',
    'greater': 'mayor',
    'less': 'menor',
    
    # Pronouns and determiners
    'We': 'Nosotros',
    'You': 'Tú',
    'It': 'Esto',
    'This': 'Este',
    'That': 'Ese',
    'These': 'Estos',
    'Those': 'Esos',
    'Each': 'Cada',
    'All': 'Todos',
    'Some': 'Algunos',
    'Any': 'Algún',
    'Both': 'Ambos',
    
    # Prepositions and conjunctions
    'from': 'desde',
    'to': 'a',
    'with': 'con',
    'without': 'sin',
    'by': 'por',
    'through': 'a través de',
    'during': 'durante',
    'before': 'antes de',
    'after': 'después de',
    'while': 'mientras',
    'until': 'hasta',
    'when': 'cuando',
    'where': 'donde',
    'how': 'cómo',
    'if': 'si',
    'else': 'sino',
    'then': 'luego',
    'because': 'porque',
    'although': 'aunque',
    'however': 'sin embargo',
    
    # Common phrases
    'Hello, World': 'Hello, World',
    'Hello, C': 'Hello, C',
    'must be': 'debe ser',
    'should be': 'debería ser',
    'must be equal to': 'debe ser igual a',
    'should return': 'debería devolver',
    'should print': 'debería imprimir',
    'can you': 'puedes',
    'following': 'siguiente',
    'between': 'entre',
    'into': 'en',
    'keeping': 'teniendo',
    'mind that': 'en cuenta que',
    'reside': 'residirá',
    'execute': 'ejecutar',
    'giving': 'dándole',
    'updating': 'actualizando',
    'assigning': 'asignando',
    'storing': 'almacenar',
    'evaluating': 'evaluar',
    'performing': 'realizar',
    'comparing': 'comparar',
    'repeating': 'repetir',
    'dividing': 'dividir',
    'beginning': 'comenzar',
    'defined': 'definida',
    'called': 'llamada',
    'named': 'llamada',
    'keeping in mind': 'teniendo en cuenta',
    
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

def translate_line(line: str) -> str:
    """Translate a line using the dictionary."""
    result = line
    
    # Sort by length (longest first) for proper replacement
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
        
        # Section markers - preserve unchanged
        if stripped in ['# --description--', '# --instructions--', '# --seed--',
                       '# --answers--', '# --solutions--', '# --asserts--',
                       '# --before-seed--', '# --after-seed--',
                       '# --before-asserts--', '# --after-asserts--',
                       '# --output--', '# --before-solutions--', '# --after-solutions--']:
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
    # Process main data.json
    src = EN_DIR / 'data.json'
    dst = ES_DIR / 'data.json'
    dst.parent.mkdir(parents=True, exist_ok=True)
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
