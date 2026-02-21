#!/usr/bin/env python3
"""
Complete Swift to Spanish Exercise Translator
Performs comprehensive translation using direct text replacement.
"""

import os
import json
import re
from pathlib import Path

# Full translations organized by context
TRANSLATIONS = {
    # Common phrases
    "Calculate the sum between the numbers": "Calcula la suma entre los numeros",
    "Calculate the difference between the numbers": "Calcula la diferencia entre los numeros",
    "Calculate the product between the numbers": "Calcula el producto entre los numeros",
    "Calculate the quotient between the numbers": "Calcula el cociente entre los numeros",
    "Calculate the remainder between the numbers": "Calcula el resto entre los numeros",
    "then print the variable": "luego imprime la variable",
    "then print": "luego imprime",
    "Complete the code in order to": "Completa el codigo para",
    "Complete the code to": "Completa el codigo para",
    "Which output produces the following code": "Que salida produce el siguiente codigo",
    "What is the output of the following code": "Cual es la salida del siguiente codigo",
    "in this order": "en este orden",
    "in the following order": "en el siguiente orden",
    "from the division between": "de la division entre",
    "Multiplied by": "multiplicado por",
    "divided by": "dividido por",
    "subtract": "restar",
    "from": "de",
    "to": "a",
    "and finally": "y finalmente",

    # Operators descriptions
    "Operators are used to perform operations on variables and values": "Los operadores se utilizan para realizar operaciones en variables y valores",
    "Let's start with the arithmetic operators": "Comencemos con los operadores aritmeticos",
    "in particular with the": "en particular con el",
    "operator": "operador",
    "operators": "operadores",
    "It is used to add two numbers, like:": "Se usa para sumar dos numeros, por ejemplo:",
    "It is used to subtract one number from another, like:": "Se usa para restar un numero de otro, por ejemplo:",
    "It is used to multiply two numbers together, like:": "Se usa para multiplicar dos numeros, por ejemplo:",
    "It is used to divide two numbers together, like:": "Se usa para dividir dos numeros, por ejemplo:",
    "It is used to find the remainder after a division between two numbers, like:": "Se usa para encontrar el resto despues de una division entre dos numeros, por ejemplo:",
    "This evaluates to": "Esto evalua a",
    "because": "porque",
    "has a quotient of": "tiene un cociente de",
    "and a remainder of": "y un resto de",
    "leaves a remainder of": "deja un resto de",
    "This other evaluates to": "Este otro evalua a",
    "Let's continue with the": "Continuemos con el",
    "Let's see the": "Veamos el",

    # Arrays
    "Arrays are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name": "Los arreglos son un tipo de dato que puedes usar para almacenar una coleccion de diferentes piezas de informacion como una secuencia bajo un solo nombre de variable",
    "An array stores multiple values of one or multiple types and uses indexes to distinguish these values": "Un arreglo almacena multiples valores de uno o multiples tipos y usa indices para distinguir estos valores",
    "You can assign items to an array with an expression of the form:": "Puedes asignar elementos a un arreglo con una expresion de la forma:",
    "stands for the type of the items inside the array": "representa el tipo de los elementos dentro del arreglo",
    "for example, it can be": "por ejemplo, puede ser",
    "An array doesn't have to have a fixed length": "Un arreglo no tiene que tener una longitud fija",
    "You can add items to the end of an array any time you like": "Puedes agregar elementos al final de un arreglo cuando quieras",
    "To add an item to an array we use the": "Para agregar un elemento a un arreglo usamos el",
    "function:": "funcion:",
    "Just like strings, arrays have a": "Al igual que las cadenas, los arreglos tienen un",
    "An arrays's length is the number of items it contains": "La longitud de un arreglo es el numero de elementos que contiene",
    "Complete the code in order to print the length of the array": "Completa el codigo para imprimir la longitud del arreglo",
    "An array index behaves like any other variable name": "Un indice de arreglo se comporta como cualquier otro nombre de variable",
    "It can be used to access as well as assign values": "Se puede usar para acceder asi como para asignar valores",
    "You saw how to access an array index like this:": "Viste como acceder a un indice de arreglo asi:",
    "This is how an assignment works:": "Asi es como funciona una asignacion:",
    "Complete the code in order to replace the item that currently holds the value": "Completa el codigo para reemplazar el elemento que actualmente tiene el valor",
    "with the name": "con el nombre",
    "Prints the value": "Imprime el valor",
    "Assign the new value": "Asigna el nuevo valor",

    # Booleans
    "A boolean is a data type that can only have two possible values: true and false": "Un booleano es un tipo de dato que solo puede tener dos valores posibles: verdadero y falso",
    "Booleans are used to represent truth values": "Los booleanos se usan para representar valores de verdad",
    "The value true represents a logically true condition": "El valor verdadero representa una condicion logicamente verdadera",
    "The value false represents a logically false condition": "El valor falso representa una condicion logicamente falsa",
    "Comparison operators are used to compare two values": "Los operadores de comparacion se usan para comparar dos valores",
    "The result of a comparison is always a boolean value": "El resultado de una comparacion siempre es un valor booleano",
    "Here are the comparison operators in Swift:": "Aqui estan los operadores de comparacion en Swift:",
    "Greater than": "Mayor que",
    "Less than": "Menor que",
    "Greater than or equal to": "Mayor o igual que",
    "Less than or equal to": "Menor o igual que",
    "Equal to": "Igual a",
    "Not equal to": "No igual a",

    # Variables
    "A variable is a named location used to store data in memory": "Una variable es una ubicacion con nombre usada para almacenar datos en memoria",
    "You can think of a variable as a labeled box where you can store data": "Puedes pensar en una variable como una caja etiquetada donde puedes almacenar datos",
    "Variables are declared using the": "Las variables se declaran usando el",
    "keyword:": "palabra clave:",
    "followed by the variable name and optionally the type": "seguido del nombre de la variable y opcionalmente el tipo",
    "For example:": "Por ejemplo:",
    "A constant is like a variable, but its value cannot be changed once assigned": "Una constante es como una variable, pero su valor no puede ser cambiado una vez asignado",
    "Constants are declared using the": "Las constantes se declaran usando el",
    "keyword instead of": "palabra clave en lugar de",
    "Type inference means that the compiler can automatically deduce the type of a variable based on its initial value": "La inferencia de tipos significa que el compilador puede deducir automaticamente el tipo de una variable basandose en su valor inicial",
    "You don't always need to specify the type explicitly": "No siempre necesitas especificar el tipo explicitamente",
    "The compiler will figure it out from the value you assign": "El compilador lo deducira del valor que asignes",
    "Naming rules for variables:": "Reglas de nombramiento para variables:",
    "Must start with a letter or underscore": "Debe comenzar con una letra o guion bajo",
    "Can contain letters, numbers, and underscores": "Puede contener letras, numeros y guiones bajos",
    "Cannot contain spaces or special characters": "No puede contener espacios o caracteres especiales",
    "Cannot start with a number": "No puede comenzar con un numero",
    "Cannot be a reserved keyword": "No puede ser una palabra clave reservada",

    # Functions
    "A function is a reusable block of code that performs a specific task": "Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica",
    "Functions help you organize your code and avoid repetition": "Las funciones te ayudan a organizar tu codigo y evitar repeticion",
    "You define a function using the": "Defines una funcion usando el",
    "followed by the function name, parameters, and return type": "seguido del nombre de la funcion, parametros y tipo de retorno",
    "Parameters are values that you pass into a function": "Los parametros son valores que pasas a una funcion",
    "Return type is the type of value that the function returns": "El tipo de retorno es el tipo de valor que la funcion devuelve",
    "You call a function by using its name followed by parentheses": "Llamas a una funcion usando su nombre seguido de parentesis",
    "A function can return a value using the": "Una funcion puede devolver un valor usando el",
    "Functions can have default parameter values": "Las funciones pueden tener valores de parametro predeterminados",
    "If a parameter has a default value, you can omit it when calling the function": "Si un parametro tiene un valor predeterminado, puedes omitirlo al llamar a la funcion",
    "Functions can have multiple parameters": "Las funciones pueden tener multiples parametros",
    "Separate parameters with commas": "Separa los parametros con comas",

    # Conditionals
    "Conditional statements allow you to execute different code based on different conditions": "Las sentencias condicionales te permiten ejecutar diferente codigo basado en diferentes condiciones",
    "statement checks a condition and executes code if the condition is true": "verifica una condicion y ejecuta codigo si la condicion es verdadera",
    "The else statement executes code if the if condition is false": "La sentencia sino ejecuta codigo si la condicion si es falsa",
    "You can chain multiple conditions using": "Puedes encadenar multiples condiciones usando",
    "The switch statement provides an alternative way to handle multiple conditions": "La sentencia cambiar proporciona una forma alternativa de manejar multiples condiciones",
    "It's often cleaner than multiple": "A menudo es mas limpio que multiples",
    "statements:": "sentencias:",

    # Loops
    "Loops allow you to execute code repeatedly": "Los bucles te permiten ejecutar codigo repetidamente",
    "The for loop is used to iterate over a sequence": "El bucle para se usa para iterar sobre una secuencia",
    "The while loop executes code as long as a condition is true": "El bucle mientras ejecuta codigo mientras una condicion sea verdadera",
    "The repeat-while loop is similar to while, but it always executes at least once": "El bucle repetir-mientras es similar a mientras, pero siempre se ejecuta al menos una vez",
    "You can use the break statement to exit a loop early": "Puedes usar la sentencia romper para salir de un bucle temprano",
    "You can use the continue statement to skip to the next iteration": "Puedes usar la sentencia continuar para saltar a la siguiente iteracion",

    # Classes
    "A class is a blueprint for creating objects": "Una clase es un plano para crear objetos",
    "Classes define properties and methods": "Las clases definen propiedades y metodos",
    "Properties store values": "Las propiedades almacenan valores",
    "Methods define behavior": "Los metodos definen comportamiento",
    "You create an instance of a class using the": "Creas una instancia de una clase usando el",
    "Inheritance allows a class to inherit properties and methods from another class": "La herencia permite a una clase heredar propiedades y metodos de otra clase",
    "The subclass inherits from the superclass": "La subclase hereda de la superclase",

    # Instructions
    "Write a function that returns the string": "Escribe una funcion que devuelva la cadena",
    "Write": "Escribe",
    "Create": "Crea",
    "Define": "Define",
    "Implement": "Implementa",
    "Calculate": "Calcula",
    "Print": "Imprime",
    "Return": "Devuelve",
    "Add": "Anade",
    "Remove": "Elimina",
    "Insert": "Inserta",
    "Delete": "Elimina",
    "Update": "Actualiza",
    "Replace": "Reemplaza",
    "Append": "Agrega",
    "the sum": "la suma",
    "the difference": "la diferencia",
    "the product": "el producto",
    "the quotient": "el cociente",
    "the remainder": "el resto",
    "the result": "el resultado",
    "the length": "la longitud",
    "the size": "el tamano",
    "the value": "el valor",
    "the values": "los valores",
    "the name": "el nombre",
    "the names": "los nombres",
    "the text": "el texto",
    "the message": "el mensaje",
    "the array": "el arreglo",
    "the number": "el numero",
    "the numbers": "los numeros",
    "the count": "el conteo",
    "the total": "el total",
    "the index": "el indice",
    "the item": "el elemento",
    "the items": "los elementos",
    "the first": "el primero",
    "the last": "el ultimo",
    "the second": "el segundo",
    "the third": "el tercero",

    # Single word translations (applied last to avoid partial matches)
    "variable": "variable",
    "function": "funcion",
    "array": "arreglo",
    "string": "cadena",
    "boolean": "booleano",
    "true": "verdadero",
    "false": "falso",
    "number": "numero",
    "numbers": "numeros",
    "value": "valor",
    "values": "valores",
    "name": "nombre",
    "names": "nombres",
    "text": "texto",
    "code": "codigo",
    "data": "datos",
    "type": "tipo",
    "types": "tipos",
    "item": "elemento",
    "items": "elementos",
    "index": "indice",
    "indices": "indices",
    "length": "longitud",
    "size": "tamano",
    "count": "conteo",
    "sum": "suma",
    "difference": "diferencia",
    "product": "producto",
    "quotient": "cociente",
    "remainder": "resto",
    "result": "resultado",
    "total": "total",
    "output": "salida",
    "input": "entrada",
    "first": "primero",
    "last": "ultimo",
    "second": "segundo",
    "third": "tercero",
    "operator": "operador",
    "operators": "operadores",
    "operation": "operacion",
    "operations": "operaciones",
    "statement": "sentencia",
    "statements": "sentencias",
    "condition": "condicion",
    "conditions": "condiciones",
    "loop": "bucle",
    "loops": "bucles",
    "class": "clase",
    "classes": "clases",
    "method": "metodo",
    "methods": "metodos",
    "property": "propiedad",
    "properties": "propiedades",
    "parameter": "parametro",
    "parameters": "parametros",
    "argument": "argumento",
    "arguments": "argumentos",
    "keyword": "palabra clave",
    "keywords": "palabras clave",
    "constant": "constante",
    "constants": "constantes",
    "comment": "comentario",
    "comments": "comentarios",
    "example": "ejemplo",
    "examples": "ejemplos",
    "use": "usar",
    "using": "usando",
    "used": "usado",
    "perform": "realizar",
    "execute": "ejecutar",
    "store": "almacenar",
    "contains": "contiene",
    "between": "entre",
    "from": "de",
    "to": "a",
    "with": "con",
    "without": "sin",
    "for": "para",
    "and": "y",
    "or": "o",
    "not": "no",
    "but": "pero",
    "if": "si",
    "else": "sino",
    "then": "entonces",
    "when": "cuando",
    "where": "donde",
    "how": "como",
    "what": "que",
    "which": "cual",
    "who": "quien",
    "why": "por que",
    "because": "porque",
    "so": "asi que",
    "therefore": "por lo tanto",
    "however": "sin embargo",
    "although": "aunque",
    "though": "aunque",
    "while": "mientras",
    "during": "durante",
    "until": "hasta",
    "since": "desde",
    "before": "antes",
    "after": "despues",
    "now": "ahora",
    "later": "despues",
    "always": "siempre",
    "never": "nunca",
    "sometimes": "a veces",
    "often": "frecuentemente",
    "usually": "generalmente",
    "can": "puede",
    "cannot": "no puede",
    "can't": "no puede",
    "will": "podra",
    "won't": "no podra",
    "would": "habria",
    "should": "deberia",
    "could": "podria",
    "might": "podria",
    "must": "debe",
    "may": "puede",
    "need": "necesita",
    "needs": "necesita",
    "is": "es",
    "are": "son",
    "was": "era",
    "were": "eran",
    "been": "sido",
    "being": "siendo",
    "have": "tiene",
    "has": "tiene",
    "had": "tenia",
    "having": "teniendo",
    "do": "hacer",
    "does": "hace",
    "did": "hizo",
    "doing": "haciendo",
    "get": "obtener",
    "gets": "obtiene",
    "got": "obtuvo",
    "getting": "obteniendo",
    "make": "hacer",
    "makes": "hace",
    "made": "hizo",
    "making": "haciendo",
    "go": "ir",
    "goes": "va",
    "went": "fue",
    "going": "yendo",
    "see": "ver",
    "sees": "ve",
    "saw": "vio",
    "seeing": "viendo",
    "know": "saber",
    "knows": "sabe",
    "knew": "supo",
    "knowing": "sabiendo",
    "think": "pensar",
    "thinks": "piensa",
    "thought": "penso",
    "thinking": "pensando",
    "take": "tomar",
    "takes": "toma",
    "took": "tomo",
    "taking": "tomando",
    "come": "venir",
    "comes": "viene",
    "came": "vino",
    "coming": "viniendo",
    "want": "querer",
    "wants": "quiere",
    "wanted": "queria",
    "wanting": "queriendo",
    "look": "mirar",
    "looks": "mira",
    "looked": "miro",
    "looking": "mirando",
    "give": "dar",
    "gives": "da",
    "gave": "dio",
    "giving": "dando",
    "find": "encontrar",
    "finds": "encuentra",
    "found": "encontro",
    "finding": "encontrando",
    "tell": "decir",
    "tells": "dice",
    "told": "dijo",
    "telling": "diciendo",
    "ask": "preguntar",
    "asks": "pregunta",
    "asked": "pregunto",
    "asking": "preguntando",
    "work": "trabajar",
    "works": "funciona",
    "worked": "trabajo",
    "working": "trabajando",
    "seem": "parecer",
    "seems": "parece",
    "seemed": "parecio",
    "seeming": "pareciendo",
    "feel": "sentir",
    "feels": "siente",
    "felt": "sintio",
    "feeling": "sintiendo",
    "try": "intentar",
    "tries": "intenta",
    "tried": "intento",
    "trying": "intentando",
    "leave": "dejar",
    "leaves": "deja",
    "left": "dejo",
    "leaving": "dejando",
    "call": "llamar",
    "calls": "llama",
    "called": "llamo",
    "calling": "llamando",
    "show": "mostrar",
    "shows": "muestra",
    "showed": "mostro",
    "showing": "mostrando",
    "hold": "mantener",
    "holds": "mantiene",
    "held": "mantuvo",
    "holding": "manteniendo",
    "keep": "mantener",
    "keeps": "mantiene",
    "kept": "mantuvo",
    "keeping": "manteniendo",
    "let": "permitir",
    "lets": "permite",
    "begin": "comenzar",
    "begins": "comienza",
    "began": "comenzo",
    "beginning": "comenzando",
    "start": "empezar",
    "starts": "empieza",
    "started": "empezo",
    "starting": "empezando",
    "end": "terminar",
    "ends": "termina",
    "ended": "termino",
    "ending": "terminando",
    "learn": "aprender",
    "learns": "aprende",
    "learned": "aprendio",
    "learning": "aprendiendo",
    "change": "cambiar",
    "changes": "cambia",
    "changed": "cambio",
    "changing": "cambiando",
    "lead": "conducir",
    "leads": "conduce",
    "led": "condujo",
    "leading": "conduciendo",
    "understand": "entender",
    "understands": "entiende",
    "understood": "entendio",
    "understanding": "entendiendo",
    "watch": "ver",
    "watches": "ve",
    "watched": "vio",
    "watching": "viendo",
    "follow": "seguir",
    "follows": "sigue",
    "followed": "siguio",
    "following": "siguiendo",
    "stop": "parar",
    "stops": "para",
    "stopped": "paro",
    "stopping": "parando",
    "create": "crear",
    "creates": "crea",
    "created": "creo",
    "creating": "creando",
    "add": "anadir",
    "adds": "anade",
    "added": "anadio",
    "adding": "anadiendo",
    "join": "unir",
    "joins": "une",
    "joined": "unio",
    "joining": "uniendo",
    "spend": "gastar",
    "spends": "gasta",
    "spent": "gasto",
    "spending": "gastando",
    "grow": "crecer",
    "grows": "crece",
    "grew": "crecio",
    "growing": "creciendo",
    "open": "abrir",
    "opens": "abre",
    "opened": "abrio",
    "opening": "abriendo",
    "walk": "caminar",
    "walks": "camina",
    "walked": "camino",
    "walking": "caminando",
    "win": "ganar",
    "wins": "gana",
    "won": "gano",
    "winning": "ganando",
    "offer": "ofrecer",
    "offers": "ofrece",
    "offered": "ofrecio",
    "offering": "ofreciendo",
    "remember": "recordar",
    "remembers": "recuerda",
    "remembered": "recordo",
    "remembering": "recordando",
    "love": "amar",
    "loves": "ama",
    "loved": "amo",
    "loving": "amando",
    "consider": "considerar",
    "considers": "considera",
    "considered": "considero",
    "considering": "considerando",
    "appear": "aparecer",
    "appears": "aparece",
    "appeared": "aparecio",
    "appearing": "apareciendo",
    "buy": "comprar",
    "buys": "compra",
    "bought": "compro",
    "buying": "comprando",
    "wait": "esperar",
    "waits": "espera",
    "waited": "espero",
    "waiting": "esperando",
    "serve": "servir",
    "serves": "sirve",
    "served": "sirvio",
    "serving": "sirviendo",
    "die": "morir",
    "dies": "muere",
    "died": "murio",
    "dying": "muriendo",
    "send": "enviar",
    "sends": "envia",
    "sent": "envio",
    "sending": "enviando",
    "expect": "esperar",
    "expects": "espera",
    "expected": "esperaba",
    "expecting": "esperando",
    "build": "construir",
    "builds": "construye",
    "built": "construyo",
    "building": "construyendo",
    "stay": "quedarse",
    "stays": "se queda",
    "stayed": "se quedo",
    "staying": "quedandose",
    "fall": "caer",
    "falls": "cae",
    "fell": "cayo",
    "falling": "cayendo",
    "cut": "cortar",
    "cuts": "corta",
    "cutting": "cortando",
    "reach": "alcanzar",
    "reaches": "alcanza",
    "reached": "alcanzo",
    "reaching": "alcanzando",
    "kill": "matar",
    "kills": "mata",
    "killed": "mato",
    "killing": "matando",
    "remain": "permanecer",
    "remains": "permanece",
    "remained": "permanecio",
    "remaining": "permaneciendo",
    "suggest": "sugerir",
    "suggests": "sugiere",
    "suggested": "sugirio",
    "suggesting": "sugiriendo",
    "raise": "levantar",
    "raises": "levanta",
    "raised": "levanto",
    "raising": "levantando",
    "pass": "pasar",
    "passes": "pasa",
    "passed": "paso",
    "passing": "pasando",
    "sell": "vender",
    "sells": "vende",
    "sold": "vendio",
    "selling": "vendiendo",
    "require": "requerir",
    "requires": "requiere",
    "required": "requirio",
    "requiring": "requiriendo",
    "report": "reportar",
    "reports": "reporta",
    "reported": "reporto",
    "reporting": "reportando",
    "decide": "decidir",
    "decides": "decide",
    "decided": "decidio",
    "deciding": "decidiendo",
    "pull": "jalar",
    "pulls": "jala",
    "pulled": "jalo",
    "pulling": "jalando",
}

# Variable name translations
VAR_TRANSLATIONS = {
    "sum": "suma",
    "difference": "diferencia",
    "product": "producto",
    "quotient": "cociente",
    "remainder": "resto",
    "result": "resultado",
    "count": "conteo",
    "total": "total",
    "value": "valor",
    "name": "nombre",
    "names": "nombres",
    "numbers": "numeros",
    "number": "numero",
    "array": "arreglo",
    "text": "texto",
    "message": "mensaje",
    "output": "salida",
    "length": "longitud",
    "size": "tamano",
    "index": "indice",
    "item": "elemento",
    "items": "elementos",
}

def translate_text(text: str) -> str:
    """Translate text using phrase-first approach."""
    result = text

    # Apply translations from longest to shortest to avoid partial matches
    for en, es in sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        # Use word boundaries for single words, but allow partial matches for phrases
        if len(en.split()) == 1:
            pattern = r'\b' + re.escape(en) + r'\b'
            result = re.sub(pattern, es, result, flags=re.IGNORECASE)
        else:
            # For phrases, do case-insensitive replacement
            pattern = re.escape(en)
            result = re.sub(pattern, es, result, flags=re.IGNORECASE)

    return result

def translate_code_line(line: str, in_solutions: bool) -> str:
    """Translate a code line."""
    # Translate comments
    if '//' in line:
        parts = line.split('//', 1)
        if len(parts) == 2:
            code_part = parts[0]
            comment = parts[1]
            translated_comment = translate_text(comment)
            return f"{code_part}// {translated_comment.lstrip()}"

    if '#' in line and not line.strip().startswith('#'):
        parts = line.split('#', 1)
        if len(parts) == 2:
            code_part = parts[0]
            comment = parts[1]
            translated_comment = translate_text(comment)
            return f"{code_part}# {translated_comment.lstrip()}"

    # Translate variable names in solutions
    if in_solutions:
        result = line
        for en, es in VAR_TRANSLATIONS.items():
            pattern = r'\b' + re.escape(en) + r'\b'
            result = re.sub(pattern, es, result)
        return result

    return line

def translate_exercise(content: str) -> str:
    """Translate an exercise file."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    in_solutions = False
    in_answers = False
    in_translatable_section = False

    for line in lines:
        stripped = line.strip()

        # Check for section tags
        if stripped.startswith('# --'):
            in_solutions = '--solutions--' in stripped
            in_answers = '--answers--' in stripped
            in_translatable_section = stripped in [
                '# --description--',
                '# --instructions--',
                '# --output--',
                '# --answers--',
            ]
            result.append(line)
            continue

        # Track code blocks
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        # Handle content
        if in_code_block:
            result.append(translate_code_line(line, in_solutions))
        elif in_translatable_section or in_answers:
            result.append(translate_text(line))
        else:
            result.append(line)

    return '\n'.join(result)

def translate_data_json(data: dict) -> dict:
    """Translate data.json content."""
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = {
                'order': value.get('order'),
                'title': translate_text(value.get('title', '')),
                'description': translate_text(value.get('description', '')),
            }
        else:
            result[key] = value
    return result

def main():
    """Main translation function."""
    base_path = Path('/Users/ale/github/codigo-questions')
    source_dir = base_path / 'en' / 'swift'
    target_dir = base_path / 'es' / 'swift'

    md_files = list(source_dir.rglob('*.md'))
    json_files = list(source_dir.rglob('data.json'))

    print(f"Found {len(md_files)} markdown files and {len(json_files)} JSON files")

    translated_count = 0
    all_files = sorted(source_dir.rglob('*'), key=lambda x: str(x))

    for source_file in all_files:
        if source_file.is_dir():
            continue

        if source_file.name.startswith('_'):
            continue

        rel_path = source_file.relative_to(source_dir)
        target_file = target_dir / rel_path
        target_file.parent.mkdir(parents=True, exist_ok=True)

        if source_file.name == 'data.json':
            with open(source_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            translated_data = translate_data_json(data)
            with open(target_file, 'w', encoding='utf-8') as f:
                json.dump(translated_data, f, ensure_ascii=False, indent=2)
            print(f"Translated: {rel_path}")
            translated_count += 1

        elif source_file.suffix == '.md':
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()

            translated_content = translate_exercise(content)

            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)

            print(f"Translated: {rel_path}")
            translated_count += 1

    print(f"\nComplete! Translated {translated_count} files.")

if __name__ == '__main__':
    main()
