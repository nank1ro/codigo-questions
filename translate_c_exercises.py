#!/usr/bin/env python3
"""
Translate C exercises from English to Spanish.
Translates user-facing text while preserving code structure, keywords, and section tags.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

def translate_exercise_file(content: str) -> str:
    """Translate an entire exercise file with proper Spanish translations."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    current_section = None

    for line in lines:
        stripped = line.strip()

        # Track code blocks
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            result.append(line)
            continue

        # Track sections
        if stripped.startswith("# --") and stripped.endswith("--"):
            current_section = stripped[3:-3].strip()
            result.append(line)
            continue

        # Skip translation for:
        # - Frontmatter
        # - Code blocks
        # - before-seed, before-asserts, after-asserts (contain test framework code)
        # - before-seed contains CException framework that must stay in English
        if in_code_block or current_section in ['before-seed', 'before-asserts', 'after-asserts', 'seed']:
            result.append(line)
        else:
            result.append(translate_line(line, current_section))

    return '\n'.join(result)

def translate_line(line: str, section: str) -> str:
    """Translate a single line based on the section."""
    # Don't translate empty lines or just whitespace
    if not line.strip():
        return line

    # Don't translate section tags
    if line.strip().startswith("# --"):
        return line

    # Don't translate frontmatter delimiters
    if line.strip().startswith("---"):
        return line

    # Handle frontmatter key-value pairs
    if ":" in line and not line.strip().startswith("#"):
        parts = line.split(":", 1)
        if len(parts) == 2:
            key, value = parts[0].strip(), parts[1].strip()
            # Keep language, exerciseType as-is
            if key in ["language", "exerciseType"]:
                return line
            # Translate title
            if key == "title" and value:
                return f"{parts[0].strip()}: {translate_title(value.strip())}"
            # Translate difficulty (stays number)
            if key == "difficulty":
                return line
        return line

    # Translate based on section
    if section == "description":
        return translate_description_line(line)
    elif section == "instructions":
        return translate_instructions_line(line)
    elif section == "asserts":
        return translate_asserts_line(line)
    elif section == "answers":
        return translate_answers_line(line)
    elif section == "output":
        return translate_output_line(line)
    elif section == "solutions":
        # Keep solutions unchanged (code)
        return line
    else:
        return translate_general_line(line)

def translate_title(title: str) -> str:
    """Translate a title."""
    translations = {
        "Hello World!": "Hola, Mundo!",
        "Addition": "Suma",
        "ATM": "Cajero Automatico",
        "Raindrops": "Gotas de Lluvia",
        "Sum of digits": "Suma de digitos",
        "Two for one": "Dos por uno",
        "100 doors": "100 puertas",
        "Ackermann function": "Funcion de Ackermann",
        "Arithmetic mean": "Media aritmetica",
        "FizzBuzz": "FizzBuzz",
        "Roman numeral converter": "Conversor de numeros romanos",
        "Leap year": "Anio bisiesto",
    }
    return translations.get(title, title)

def translate_description_line(line: str) -> str:
    """Translate a description line."""
    result = line

    # Full sentence translations for descriptions
    translations = [
        ('Variables are containers for storing data values.',
         'Las variables son contenedores para almacenar valores de datos.'),
        ('Every variable in C is an object and like other programming languages, C has commands for declaring a variable.',
         'Cada variable en C es un objeto y, como otros lenguajes de programacion, C tiene comandos para declarar una variable.'),
        ('To create a variable, we need to give it a **type** and a **name** keeping in mind that it must not contain spaces.',
         'Para crear una variable, necesitamos darle un **tipo** y un **nombre**, teniendo en cuenta que no debe contener espacios.'),
        ('A variable is created the moment you first assign a value to it.',
         'Una variable se crea en el momento en que le asignas un valor por primera vez.'),
        ('An example of a variable creation named `x` is:',
         'Un ejemplo de creacion de una variable llamada `x` es:'),
        ('In this way we have assigned the value `1` to the _integer_ variable named `x`.',
         'De esta manera hemos asignado el valor `1` a la variable _entera_ llamada `x`.'),
        ('If we print the variable `x` we get back the number `1`:',
         'Si imprimimos la variable `x`, obtenemos el numero `1`:'),
        ('Variables are called in this way because the value they store can change.',
         'Las variables se llaman asi porque el valor que almacenan puede cambiar.'),
        ('We can update `x` by using `=` and giving it a new value.',
         'Podemos actualizar `x` usando `=` y dandole un nuevo valor.'),
        ('"Hello, World!" is the traditional first program for beginning programming in a new language.',
         '"Hola, Mundo!" es el programa tradicional para comenzar a programar en un nuevo lenguaje.'),
        ('We use the `printf()` function to output data to the standard output device (screen).',
         'Usamos la funcion `printf()` para mostrar datos en el dispositivo de salida estandar (pantalla).'),
        ('Every C program uses libraries, which give the ability to execute necessary functions, for example the print on the screen function is defined in the `stdio.h` header file.',
         'Todo programa en C usa bibliotecas que dan la capacidad de ejecutar funciones necesarias; por ejemplo, la funcion de imprimir en pantalla esta definida en el archivo de encabezado `stdio.h`.'),
        ('The first code which will run will always reside in the main function.',
         'El primer codigo que se ejecutara siempre estara en la funcion principal.'),
        ('To print `Hello, World!` on the screen with C we can write',
         'Para imprimir `Hola, Mundo!` en la pantalla con C, podemos escribir'),
        ('Finally we return `0` to indicate that our program was successful',
         'Finalmente retornamos `0` para indicar que nuestro programa fue exitoso'),
    ]

    for eng, spa in translations:
        if eng in result:
            result = result.replace(eng, spa)

    return result

def translate_instructions_line(line: str) -> str:
    """Translate an instructions line."""
    result = line

    translations = [
        ('Assign to the variable `y` the value `2`.',
         'Asigna a la variable `y` el valor `2`.'),
        ('Update the value of the variable `x` with the number `10`.',
         'Actualiza el valor de la variable `x` con el numero `10`.'),
        ('Your program should print the string `Hello, C!` on the screen.',
         'Tu programa debe imprimir la cadena `Hola, C!` en la pantalla.'),
        ('Write a function that returns the string "Hello, World!".',
         'Escribe una funcion que retorne la cadena "Hola, Mundo!".'),
        ('write after this line',
         'escribe despues de esta linea'),
    ]

    for eng, spa in translations:
        if eng in result:
            result = result.replace(eng, spa)

    return result

def translate_asserts_line(line: str) -> str:
    """Translate an asserts line."""
    result = line

    translations = [
        ('`y` must be equal to `2`.',
         '`y` debe ser igual a `2`.'),
        ('`x` must be equal to `10`.',
         '`x` debe ser igual a `10`.'),
        ('The function should return "Hello, World!".',
         'La funcion debe retornar "Hola, Mundo!".'),
    ]

    for eng, spa in translations:
        if eng in result:
            result = result.replace(eng, spa)

    return result

def translate_answers_line(line: str) -> str:
    """Translate an answers line (preserving trailing spaces)."""
    # Answer lines start with "- "
    if line.strip().startswith("- "):
        # Keep answers as-is since they contain code/strings
        return line

    return line

def translate_output_line(line: str) -> str:
    """Translate an output line."""
    result = line

    translations = [
        ('Hello C!', 'Hola C!'),
    ]

    for eng, spa in translations:
        if eng in result:
            result = result.replace(eng, spa)

    return result

def translate_general_line(line: str) -> str:
    """Translate a general line."""
    return line

def translate_data_json(content: str, is_challenges: bool = False) -> str:
    """Translate a data.json file."""
    data = json.loads(content)

    if is_challenges:
        for key in data:
            if "name" in data[key]:
                data[key]["name"] = translate_title(data[key]["name"])
    else:
        for key in data:
            if "title" in data[key]:
                data[key]["title"] = translate_title(data[key]["title"])
            if "description" in data[key]:
                data[key]["description"] = translate_description(data[key]["description"])

    return json.dumps(data, indent=4 if is_challenges else None, ensure_ascii=False) + ("\n" if is_challenges else "")

def translate_title(title: str) -> str:
    """Translate a title."""
    translations = {
        "Output": "Salida",
        "Formatted Strings": "Cadenas Formateadas",
        "Variables": "Variables",
        "Booleans": "Booleanos",
        "Arithmetic Operators": "Operadores Aritmeticos",
        "Assignment Operators": "Operadores de Asignacion",
        "Relational and Boolean Operators": "Operadores Relacionales y Booleanos",
        "Conditional Statements": "Sentencias Condicionales",
        "While Loops": "Bucles While",
        "For Loops": "Bucles For",
        "Arrays": "Arreglos",
        "Functions": "Funciones",
        "Hello World!": "Hola, Mundo!",
        "Addition": "Suma",
        "ATM": "Cajero Automatico",
        "Raindrops": "Gotas de Lluvia",
        "Sum of digits": "Suma de digitos",
        "Two for one": "Dos por uno",
        "100 doors": "100 puertas",
        "Ackermann function": "Funcion de Ackermann",
        "Arithmetic mean": "Media aritmetica",
        "FizzBuzz": "FizzBuzz",
        "Roman numeral converter": "Conversor de numeros romanos",
        "Leap year": "Anio bisiesto",
    }
    return translations.get(title, title)

def translate_description(desc: str) -> str:
    """Translate a description."""
    translations = {
        "Learn how to output a value": "Aprende como mostrar un valor",
        "Learn how to format strings with different data types": "Aprende como formatear cadenas con diferentes tipos de datos",
        "Learn how to store values in a variable": "Aprende como almacenar valores en una variable",
        "Learn how to evaluate any expression": "Aprende como evaluar cualquier expresion",
        "Learn how to perform arithmetic operations on variables and values": "Aprende como realizar operaciones aritmeticas sobre variables y valores",
        "Learn how to assign values to variables": "Aprende como asignar valores a variables",
        "Learn how to compare values": "Aprende como comparar valores",
        "Learn how to make decisions": "Aprende como tomar decisiones",
        "Learn how to repeat a set of statements": "Aprende como repetir un conjunto de sentencias",
        "Learn how to store different values into one variable": "Aprende como almacenar diferentes valores en una variable",
        "Learn how to divide code by specific tasks": "Aprende como dividir el codigo en tareas especificas",
    }
    return translations.get(desc, desc)

def main():
    """Main translation function."""
    en_base = Path("/Users/ale/github/codigo-questions/en/c")
    es_base = Path("/Users/ale/github/codigo-questions/es/c")

    # List of argument directories
    arguments = [
        "output",
        "formattedStrings",
        "variables",
        "booleans",
        "arithmeticOperators",
        "assignmentOperators",
        "relationBooleanOperators",
        "conditionalStatements",
        "whileLoops",
        "forLoops",
        "arrays",
        "functions",
    ]

    files_created = 0

    # Translate main data.json
    print("Translating main data.json...")
    en_data = en_base / "data.json"
    es_data = es_base / "data.json"
    if en_data.exists():
        es_data.write_text(translate_data_json(en_data.read_text(), is_challenges=False), encoding='utf-8')
        files_created += 1
        print(f"  Created: {es_data}")

    # Translate each argument directory
    for arg in arguments:
        print(f"\nTranslating {arg}...")
        en_arg = en_base / arg
        es_arg = es_base / arg
        es_arg.mkdir(parents=True, exist_ok=True)

        # Get all .md files (excluding _theory.md)
        md_files = sorted(en_arg.glob("*.md"))
        md_files = [f for f in md_files if f.name != "_theory.md"]

        for md_file in md_files:
            en_content = md_file.read_text()
            es_content = translate_exercise_file(en_content)
            es_file = es_arg / md_file.name
            es_file.write_text(es_content, encoding='utf-8')
            files_created += 1
            print(f"  Created: {es_file}")

    # Translate challenges
    print("\nTranslating challenges...")
    en_challenges = en_base / "challenges"
    es_challenges = es_base / "challenges"

    for md_file in sorted(en_challenges.glob("*.md")):
        if md_file.name == "data.json":
            continue
        en_content = md_file.read_text()
        es_content = translate_exercise_file(en_content)
        es_file = es_challenges / md_file.name
        es_file.write_text(es_content, encoding='utf-8')
        files_created += 1
        print(f"  Created: {es_file}")

    # Translate challenges data.json
    print("\nTranslating challenges data.json...")
    en_challenges_data = en_challenges / "data.json"
    es_challenges_data = es_challenges / "data.json"
    if en_challenges_data.exists():
        es_challenges_data.write_text(translate_data_json(en_challenges_data.read_text(), is_challenges=True), encoding='utf-8')
        files_created += 1
        print(f"  Created: {es_challenges_data}")

    print(f"\n{'='*50}")
    print(f"Translation complete! Total files created: {files_created}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
