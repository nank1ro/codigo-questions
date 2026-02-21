#!/usr/bin/env python3
"""
Translation script for Kotlin exercises from English to Spanish.
Uses carefully constructed translation dictionary based on existing Spanish translations.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

# Base directories
BASE_DIR = Path("/Users/ale/github/codigo-questions")
EN_DIR = BASE_DIR / "en" / "kotlin"
ES_DIR = BASE_DIR / "es" / "kotlin"

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

# Comprehensive translation dictionary based on existing Spanish translations
# Organized by category for clarity

# ===== DESCRIPTIONS =====
DESCRIPTIONS = {
    # Variables
    "Variables are containers for storing data values.": "Las variables son contenedores para almacenar valores de datos.",
    "Every variable in Kotlin is an object.": "Cada variable en Kotlin es un objeto.",
    "To create a variable, we need to give it a __name__ keeping in mind that it must not contain spaces.": "Para crear una variable, necesitamos darle un __nombre__ teniendo en cuenta que no debe contener espacios.",
    "A variable is created the moment you first assign a value to it.": "Una variable se crea en el momento en que le asignas un valor por primera vez.",
    "In Kotlin you declare constants with the `val` (short for _value_) keyword and variables with the `var` (short for _variable_) keyword.": "En Kotlin declaras constantes con la palabra clave `val` (abreviatura de _value_) y variables con la palabra clave `var` (abreviatura de _variable_).",
    "The value of a constant can't be changed once it's set, whereas a variable can be set to a different value in the future.": "El valor de una constante no puede cambiarse una vez que se establece, mientras que una variable puede establecerse a un valor diferente en el futuro.",
    "An example of a variable creation named `x` is:": "Un ejemplo de creación de una variable llamada `x` es:",
    "In this way we have assigned the value `1` to the variable named `x`.": "De esta manera hemos asignado el valor `1` a la variable llamada `x`.",
    "If we print the variable `x` we get back the number `1`:": "Si imprimimos la variable `x` obtenemos el número `1`:",

    "Variables are called in this way because the value they store can change.": "Las variables se llaman así porque el valor que almacenan puede cambiar.",
    "We can update `x` by using `=` and giving it a new value.": "Podemos actualizar `x` usando `=` y dándole un nuevo valor.",
    "We can also give variables the values of other variables.": "También podemos dar a variables los valores de otras variables.",
    "Here, we can give to the `y` variable the value of `x`": "Aquí, podemos darle a la variable `y` el valor de `x`",
    "We can assign to a variable the result of an operation.": "Podemos asignar a una variable el resultado de una operación.",

    # Output
    '"__Hello, World!__" is the traditional first program for beginning programming in a new language.': '"__¡Hola, Mundo!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje.',
    "We use the `println()` function to output data to the standard output device (screen).": "Usamos la función `println()` para mostrar datos en el dispositivo de salida estándar (pantalla).",
    "To print `Hello, World!` on the screen with Kotlin we can write": "Para imprimir `Hello, World!` en la pantalla con Kotlin podemos escribir",
    "`println()` moves the cursor to a new line after displaying its parameter, so subsequent output appears on the next line.": "`println()` mueve el cursor a una nueva línea después de mostrar su parámetro, así que la salida subsequente aparece en la siguiente línea.",
    "You can use `print()` instead, which leaves the cursor on the same line.": "Puedes usar `print()` en su lugar, que deja el cursor en la misma línea.",

    # String Templates
    "String templates are a simple and effective way to embed references to variables or expressions directly into a string literal.": "Las plantillas de cadena son una forma simple y efectiva de incrustar referencias a variables o expresiones directamente en un literal de cadena.",
    "This is done by prefixing the variable name with a `$` character.": "Esto se hace prefijando el nombre de la variable con un carácter `$`.",
    "The expression inside the curly braces is evaluated and the result is concatenated into the string.": "La expresión dentro de los corchetes se evalúa y el resultado se concatena en la cadena.",
    "We can also use expressions inside the template.": "También podemos usar expresiones dentro de la plantilla.",
    "You can use curly braces inside the template to perform simple operations.": "Puedes usar corchetes dentro de la plantilla para realizar operaciones simples.",

    # Booleans
    "A Boolean is a type that can only have two values, either `true` or `false`.": "Un Booleano es un tipo que solo puede tener dos valores, ya sea `true` o `false`.",
    "Booleans are the result of comparison operations.": "Los Booleanos son el resultado de operaciones de comparación.",
    "We can use comparison operators to compare values.": "Podemos usar operadores de comparación para comparar valores.",
    "The result of a comparison is a Boolean value.": "El resultado de una comparación es un valor Booleano.",
    "The result of the operation is a Boolean.": "El resultado de la operación es un Booleano.",

    # Arithmetic Operators
    "Operators are used to perform operations on variables and values.": "Los operadores se usan para realizar operaciones sobre variables y valores.",
    "Let's start with arithmetic operators, in particular with the `+` operator.": "Empecemos con los operadores aritméticos, en particular con el operador `+`.",
    "It is used to add two numbers.": "Se usa para sumar dos números.",
    "The `-` operator is used to subtract two numbers.": "El operador `-` se usa para restar dos números.",
    "The `*` operator is used to multiply two numbers.": "El operador `*` se usa para multiplicar dos números.",
    "The `/` operator is used to divide two numbers.": "El operador `/` se usa para dividir dos números.",
    "The `%` operator is used to get the remainder of a division.": "El operador `%` se usa para obtener el resto de una división.",

    # Comparison and Logical Operators
    "Comparison operators are used to compare two values.": "Los operadores de comparación se usan para comparar dos valores.",
    "Logical operators are used to combine Boolean values.": "Los operadores lógicos se usan para combinar valores Booleanos.",
    "The `&&` operator returns `true` if both operands are `true`.": "El operador `&&` devuelve `true` si ambos operandos son `true`.",
    "The `||` operator returns `true` if at least one operand is `true`.": "El operador `||` devuelve `true` si al menos un operando es `true`.",
    "The `!` operator returns the opposite of the operand.": "El operador `!` devuelve lo opuesto del operando.",

    # Conditional Statements
    "Conditional statements are used to make decisions based on different conditions.": "Las sentencias condicionales se usan para tomar decisiones basadas en diferentes condiciones.",
    "In Kotlin we have `if`, `else if`, and `else` statements.": "En Kotlin tenemos sentencias `if`, `else if` y `else`.",
    "The `if` statement is used to specify a block of code to be executed if the condition is true.": "La sentencia `if` se usa para especificar un bloque de código que se ejecutará si la condición es verdadera.",
    "The `else if` statement is used to specify a new condition if the first condition is false.": "La sentencia `else if` se usa para especificar una nueva condición si la primera condición es falsa.",
    "The `else` statement is used to specify a block of code to be executed if the condition is false.": "La sentencia `else` se usa para especificar un bloque de código que se ejecutará si la condición es falsa.",
    "When you have many conditions to check, you can use `when` as a more concise alternative.": "Cuando tienes muchas condiciones para verificar, puedes usar `when` como una alternativa más concisa.",

    # While Loops
    "A loop is used to repeat a block of code.": "Un bucle se usa para repetir un bloque de código.",
    "The `while` loop loops through a block of code as long as the condition is true.": "El bucle `while` repite un bloque de código mientras la condición sea verdadera.",
    "Be careful not to create an infinite loop.": "Ten cuidado de no crear un bucle infinito.",
    "The `do-while` loop is similar to the `while` loop, but it executes the block of code at least once.": "El bucle `do-while` es similar al bucle `while`, pero ejecuta el bloque de código al menos una vez.",

    # For Loops
    "The `for` loop is used to iterate over a sequence.": "El bucle `for` se usa para iterar sobre una secuencia.",
    "Use the `step` keyword to specify the step.": "Usa la palabra clave `step` para especificar el paso.",

    # Lists
    "A List is an ordered collection of elements.": "Una Lista es una colección ordenada de elementos.",
    "Lists are mutable, meaning you can add, remove, or modify elements.": "Las listas son mutables, lo que significa que puedes agregar, eliminar o modificar elementos.",
    "To create a list, use the `listOf()` function.": "Para crear una lista, usa la función `listOf()`.",
    "To create a mutable list, use the `mutableListOf()` function.": "Para crear una lista mutable, usa la función `mutableListOf()`.",
    "You can access elements by their index using square brackets.": "Puedes acceder a los elementos por su índice usando corchetes.",
    "The first element has index 0.": "El primer elemento tiene índice 0.",
    "You can use the `size` property to get the number of elements in the list.": "Puedes usar la propiedad `size` para obtener el número de elementos en la lista.",
    "You can use the `add()` method to add an element to the list.": "Puedes usar el método `add()` para agregar un elemento a la lista.",
    "You can use the `remove()` method to remove an element from the list.": "Puedes usar el método `remove()` para eliminar un elemento de la lista.",
    "You can use the `contains()` method to check if the list contains an element.": "Puedes usar el método `contains()` para verificar si la lista contiene un elemento.",

    # Sets
    "A Set is an unordered collection of unique elements.": "Un Conjunto es una colección desordenada de elementos únicos.",
    "Sets are mutable, meaning you can add or remove elements.": "Los conjuntos son mutables, lo que significa que puedes agregar o eliminar elementos.",
    "To create a set, use the `setOf()` function.": "Para crear un conjunto, usa la función `setOf()`.",
    "To create a mutable set, use the `mutableSetOf()` function.": "Para crear un conjunto mutable, usa la función `mutableSetOf()`.",
    "You can use the `add()` method to add an element to the set.": "Puedes usar el método `add()` para agregar un elemento al conjunto.",
    "You can use the `remove()` method to remove an element from the set.": "Puedes usar el método `remove()` para eliminar un elemento del conjunto.",
    "You can use the `contains()` method to check if the set contains an element.": "Puedes usar el método `contains()` para verificar si el conjunto contiene un elemento.",
    "You can use the `size` property to get the number of elements in the set.": "Puedes usar la propiedad `size` para obtener el número de elementos en el conjunto.",
}

# ===== INSTRUCTIONS =====
INSTRUCTIONS = {
    # Variables
    "Assign to the variable `y` the value `2`.": "Asigna a la variable `y` el valor `2`.",
    "Update the value of the variable `x` with the number `10`.": "Actualiza el valor de la variable `x` con el número `10`.",
    "Create a new variable named `y` and assign it the value of the variable `x`.": "Crea una nueva variable llamada `y` y asígnale el valor de la variable `x`.",
    "Assign to the variable `result` the sum of the variables `x` and `y`.": "Asigna a la variable `result` la suma de las variables `x` y `y`.",
    "Assign to the variable `result` the product of the variables `x` and `y`.": "Asigna a la variable `result` el producto de las variables `x` y `y`.",

    # Output
    "Your program should print the string `Hello, Kotlin!` on the screen.": "Tu programa debe imprimir la cadena `Hello, Kotlin!` en la pantalla.",
    "Your program should print the string `Hello, Kotlin!` using two `print()` statements.": "Tu programa debe imprimir la cadena `Hello, Kotlin!` usando dos sentencias `print()`.",
    "Print the variable `x` on the screen.": "Imprime la variable `x` en la pantalla.",
    "Print the variables `x` and `y` on the screen, separated by a space.": "Imprime las variables `x` y `y` en la pantalla, separadas por un espacio.",

    # String Templates
    "Use a string template to print the variables `x` and `y` on the screen.": "Usa una plantilla de cadena para imprimir las variables `x` y `y` en la pantalla.",
    "Print the variable `x` inside the template, with a message.": "Imprime la variable `x` dentro de la plantilla, con un mensaje.",
    "Use a string template to print the sum of `x` and `y`.": "Usa una plantilla de cadena para imprimir la suma de `x` y `y`.",

    # Booleans
    "Store the result of the operation `x > y` in the variable `result`.": "Almacena el resultado de la operación `x > y` en la variable `result`.",
    "Store the result of the operation `x == y` in the variable `result`.": "Almacena el resultado de la operación `x == y` en la variable `result`.",
    "Check if `x` is greater than `y` and store the result in the variable `result`.": "Verifica si `x` es mayor que `y` y almacena el resultado en la variable `result`.",
    "Create a variable that stores whether `x` is equal to `y`.": "Crea una variable que almacene si `x` es igual a `y`.",

    # Arithmetic Operators
    "Calculate the sum of `x` and `y` and store the result in the variable `sum`.": "Calcula la suma de `x` y `y` y almacena el resultado en la variable `sum`.",
    "Calculate the difference between `x` and `y` and store the result in the variable `difference`.": "Calcula la diferencia entre `x` y `y` y almacena el resultado en la variable `difference`.",
    "Calculate the product of `x` and `y` and store the result in the variable `product`.": "Calcula el producto de `x` y `y` y almacena el resultado en la variable `product`.",
    "Calculate the quotient of `x` and `y` and store the result in the variable `quotient`.": "Calcula el cociente de `x` y `y` y almacena el resultado en la variable `quotient`.",
    "Calculate the remainder of `x` divided by `y` and store the result in the variable `remainder`.": "Calcula el resto de `x` dividido por `y` y almacena el resultado en la variable `remainder`.",

    # Comparison and Logical Operators
    "Check if `x` is greater than `y` and store the result in the variable `result`.": "Verifica si `x` es mayor que `y` y almacena el resultado en la variable `result`.",
    "Check if `x` is less than `y` and store the result in the variable `result`.": "Verifica si `x` es menor que `y` y almacena el resultado en la variable `result`.",
    "Check if `x` is equal to `y` and store the result in the variable `result`.": "Verifica si `x` es igual a `y` y almacena el resultado en la variable `result`.",
    "Use the `&&` operator to combine two conditions.": "Usa el operador `&&` para combinar dos condiciones.",
    "Use the `||` operator to check if at least one condition is true.": "Usa el operador `||` para verificar si al menos una condición es verdadera.",
    "Use the `!` operator to negate a condition.": "Usa el operador `!` para negar una condición.",

    # Conditional Statements
    "Use an `if` statement to check if `x` is greater than `y`.": "Usa una sentencia `if` para verificar si `x` es mayor que `y`.",
    "Use an `if-else` statement with `x` and `y` to check if `x` is less than `y`.": "Usa una sentencia `if-else` con `x` y `y` para verificar si `x` es menor que `y`.",
    "Use an `if-else if-else` statement to check multiple conditions.": "Usa una sentencia `if-else if-else` para verificar múltiples condiciones.",
    "Use a `when` expression to check multiple conditions.": "Usa una expresión `when` para verificar múltiples condiciones.",

    # While Loops
    "Use a `while` loop to print the numbers from 1 to 10.": "Usa un bucle `while` para imprimir los números del 1 al 10.",
    "Use a `while` loop to calculate the sum of numbers from 1 to 10.": "Usa un bucle `while` para calcular la suma de los números del 1 al 10.",
    "Use a `while` loop to print the even numbers from 1 to 10.": "Usa un bucle `while` para imprimir los números pares del 1 al 10.",

    # For Loops
    "Use a `for` loop to print the numbers from 1 to 10.": "Usa un bucle `for` para imprimir los números del 1 al 10.",
    "Use a `for` loop to iterate over a range of numbers.": "Usa un bucle `for` para iterar sobre un rango de números.",
    "Use a `for` loop to iterate over a list.": "Usa un bucle `for` para iterar sobre una lista.",
    "Use a `for` loop with step 2 to print the even numbers from 1 to 10.": "Usa un bucle `for` con paso 2 para imprimir los números pares del 1 al 10.",

    # Lists
    "Create a list of numbers.": "Crea una lista de números.",
    "Access the first element of the list.": "Accede al primer elemento de la lista.",
    "Access the last element of the list.": "Accede al último elemento de la lista.",
    "Add an element to the list.": "Agrega un elemento a la lista.",
    "Remove an element from the list.": "Elimina un elemento de la lista.",
    "Update an element in the list.": "Actualiza un elemento en la lista.",
    "Get the size of the list.": "Obtén el tamaño de la lista.",
    "Check if the list contains an element.": "Verifica si la lista contiene un elemento.",
    "Iterate over the list.": "Itera sobre la lista.",

    # Sets
    "Create a set of numbers.": "Crea un conjunto de números.",
    "Add an element to the set.": "Agrega un elemento al conjunto.",
    "Remove an element from the set.": "Elimina un elemento del conjunto.",
    "Check if the set contains an element.": "Verifica si el conjunto contiene un elemento.",
    "Get the size of the set.": "Obtén el tamaño del conjunto.",
    "Iterate over the set.": "Itera sobre el conjunto.",

    # Challenges
    "Write a function that returns the string \"Hello, World!\".": "Escribe una función que devuelva la cadena \"¡Hola, Mundo!\".",
    "Sort the items to produce the following output: `Hello Kotlin!`?": "Ordena los elementos para producir la siguiente salida: `Hello Kotlin!`?",
    "Which code produces the following output: `Hello Kotlin!`?": "¿Qué código produce la siguiente salida: `Hello Kotlin!`?",
    "Complete the blanks to get the desired output: `Hello Kotlin!`": "Completa los espacios en blanco para obtener la salida deseada: `Hello Kotlin!`",
}

# ===== ASSERTS =====
ASSERTS = {
    "`y` must be equal to `2`.": "`y` debe ser igual a `2`.",
    "`x` must be equal to `10`.": "`x` debe ser igual a `10`.",
    "`y` must be equal to `x`.": "`y` debe ser igual a `x`.",
    "`sum` must be equal to the sum of `x` and `y`.": "`sum` debe ser igual a la suma de `x` y `y`.",
    "`product` must be equal to the product of `x` and `y`.": "`product` debe ser igual al producto de `x` y `y`.",
    "The function should return \"Hello, World!\".": "La función debe devolver \"¡Hola, Mundo!\".",
    "The output should be:": "La salida debe ser:",
}

# ===== ANSWERS =====
ANSWERS = {
    "println": "println",
    "print": "print",
    '"Hello': '"Hello',
    'Kotlin!"': 'Kotlin!"',
    "Hello": "Hello",
    "Kotlin!": "Kotlin!",
}

# ===== COMMENTS =====
COMMENTS = {
    "// write after this line": "// escribe después de esta línea",
    "// prints 1": "// imprime 1",
    "// prints 2": "// imprime 2",
    "// prints 5": "// imprime 5",
    "// DO NOT EDIT FROM HERE": "// DO NOT EDIT FROM HERE",
    "// DO NOT EDIT UNTIL HERE": "// DO NOT EDIT UNTIL HERE",
}

# ===== TEST MESSAGES =====
TEST_MESSAGES = {
    "Test Case '--err-t$_testCount--' failed": "Test Case '--err-t$_testCount--' failed",
    "Executed $_testCount tests, with $_testFailedCount failures": "Executed $_testCount tests, with $_testFailedCount failures",
}

# ===== DATA.JSON TRANSLATIONS =====
DATA_JSON_TITLES = {
    "Output": "Salida",
    "Learn how to output a value": "Aprende a mostrar un valor",
    "String templates": "Plantillas de cadena",
    "Learn how to interpolate strings with different data types": "Aprende a interpolar cadenas con diferentes tipos de datos",
    "Variables": "Variables",
    "Learn how to store values in a variable": "Aprende a almacenar valores en una variable",
    "Booleans": "Booleanos",
    "Learn how to evaluate any expression": "Aprende a evaluar cualquier expresión",
    "Arithmetic Operators": "Operadores Aritméticos",
    "Learn how to perform arithmetic operations on variables and values": "Aprende a realizar operaciones aritméticas sobre variables y valores",
    "Comparison and Logical Operators": "Operadores de Comparación y Lógicos",
    "Learn how to compare values": "Aprende a comparar valores",
    "Conditional Statements": "Sentencias Condicionales",
    "Learn how to make decisions": "Aprende a tomar decisiones",
    "While Loops": "Bucles While",
    "Learn how to repeat a set of statements": "Aprende a repetir un conjunto de sentencias",
    "For Loops": "Bucles For",
    "Learn how to repeat a set of statements": "Aprende a repetir un conjunto de sentencias",
    "Lists": "Listas",
    "Learn how to store elements into an ordered collection": "Aprende a almacenar elementos en una colección ordenada",
    "Sets": "Conjuntos",
    "Learn how to store unique elements into an unordered collection": "Aprende a almacenar elementos únicos en una colección desordenada",
}

CHALLENGE_TITLES = {
    "Addition": "Suma",
    "ATM": "Cajero automático",
    "Hello World!": "¡Hola Mundo!",
    "Raindrops": "Gotas de lluvia",
    "Sum of digits": "Suma de dígitos",
    "Two for one": "Dos por uno",
    "100 doors": "100 puertas",
    "Ackermann function": "Función de Ackermann",
    "Multiples of 3 or 5": "Múltiplos de 3 o 5",
    "Even Fibonacci numbers": "Números pares de Fibonacci",
    "Arithmetic mean": "Media aritmética",
    "FizzBuzz": "FizzBuzz",
    "Roman numeral converter": "Conversor de números romanos",
    "Leap year": "Año bisiesto",
}

# Additional common translations
COMMON_TRANSLATIONS = {
    # Numbers and values
    "Assign to the variable `x` the value `5`.": "Asigna a la variable `x` el valor `5`.",
    "Assign to the variable `x` the value `10`.": "Asigna a la variable `x` el valor `10`.",
    "Assign to the variable `x` the value `15`.": "Asigna a la variable `x` el valor `15`.",
    "Assign to the variable `x` the value `20`.": "Asigna a la variable `x` el valor `20`.",
    "Assign to the variable `x` the value `100`.": "Asigna a la variable `x` el valor `100`.",
    "Create a variable named `x` with the value `5`.": "Crea una variable llamada `x` con el valor `5`.",
    "Create a variable named `x` with the value `10`.": "Crea una variable llamada `x` con el valor `10`.",
    "Create a variable named `message` with the value `Hello, Kotlin!`.": "Crea una variable llamada `message` con el valor `Hello, Kotlin!`.",
    "Declare a variable named `month` with the value of `june`.": "Declara una variable llamada `month` con el valor de `june`.",
    "Update the value of the variable `x` with the number `3`.": "Actualiza el valor de la variable `x` con el número `3`.",
    "Update the value of the variable `x` with the number `15`.": "Actualiza el valor de la variable `x` con el número `15`.",

    # More descriptions
    "When we update a variable, it forgets its previous value. Here we can display the `x` variable twice and see how its value updates.": "Cuando actualizamos una variable, olvida su valor anterior. Aquí podemos mostrar la variable `x` dos veces y ver cómo se actualiza su valor.",
    "In Kotlin string variables can be declared only by using double quotes:": "En Kotlin las variables de cadena solo se pueden declarar usando comillas dobles:",
    "In Kotlin you can declare constants with `val` and variables with `var`.": "En Kotlin puedes declarar constantes con `val` y variables con `var`.",
    "The difference between `val` and `var` is that `val` is read-only (like a constant), while `var` can be modified.": "La diferencia entre `val` y `var` es que `val` es de solo lectura (como una constante), mientras que `var` puede modificarse.",
    "A constant can be declared using the `val` keyword.": "Una constante se puede declarar usando la palabra clave `val`.",
    "A variable can be declared using the `var` keyword.": "Una variable se puede declarar usando la palabra clave `var`.",

    # More asserts
    "`x` must be equal to `3`.": "`x` debe ser igual a `3`.",
    "`x` must be equal to `5`.": "`x` debe ser igual a `5`.",
    "`x` must be equal to `15`.": "`x` debe ser igual a `15`.",
    "`x` must be equal to `20`.": "`x` debe ser igual a `20`.",
    "`x` must be equal to `100`.": "`x` debe ser igual a `100`.",
    "`month` must be equal to `\"june\"`.": "`month` debe ser igual a `\"june\"`.",
    "`message` must be equal to `\"Hello, Kotlin!\"`.": "`message` debe ser igual a `\"Hello, Kotlin!\"`.",

    # Comments
    "// prints 3": "// imprime 3",
    "// prints 5": "// imprime 5",
    "// prints 10": "// imprime 10",
    "// prints 15": "// imprime 15",
    "// prints 20": "// imprime 20",
    "// prints 100": "// imprime 100",

    # Common phrases
    "Write the code after the comment.": "Escribe el código después del comentario.",
    "Complete the code.": "Completa el código.",
    "Fill in the blanks.": "Rellena los espacios en blanco.",
    "Your code should produce the following output:": "Tu código debe producir la siguiente salida:",
    "The expected output is:": "La salida esperada es:",
    "Choose the correct option": "Elige la opción correcta",
    "Select all that apply": "Selecciona todas las que apliquen",
}

# Combine all dictionaries
ALL_TRANSLATIONS = {}
ALL_TRANSLATIONS.update(DESCRIPTIONS)
ALL_TRANSLATIONS.update(INSTRUCTIONS)
ALL_TRANSLATIONS.update(ASSERTS)
ALL_TRANSLATIONS.update(COMMENTS)
ALL_TRANSLATIONS.update(TEST_MESSAGES)
ALL_TRANSLATIONS.update(COMMON_TRANSLATIONS)

def translate_line(line: str, current_section: str, in_code_block: bool) -> str:
    """Translate a single line based on context."""
    if not line or not line.strip():
        return line

    # In code blocks, only translate specific comments
    if in_code_block:
        if line.strip().startswith('//'):
            for en, es in COMMENTS.items():
                if en in line:
                    return line.replace(en, es)
        return line

    # Try exact match first
    if line.strip() in ALL_TRANSLATIONS:
        return ALL_TRANSLATIONS[line.strip()]

    # Try partial match (for lines with extra whitespace or punctuation)
    stripped = line.strip()
    for en, es in ALL_TRANSLATIONS.items():
        if en in stripped:
            # Preserve leading/trailing whitespace
            leading = line[:len(line) - len(line.lstrip())]
            trailing = line[len(line.rstrip()):]
            return leading + line.replace(en, es).strip() + trailing

    return line

def translate_exercise_file(content: str) -> str:
    """Translate a single exercise file."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    in_frontmatter = False
    current_section = None

    for line in lines:
        # Check for frontmatter
        if line.strip() == '---':
            in_frontmatter = not in_frontmatter
            result.append(line)
            continue

        # Don't translate frontmatter
        if in_frontmatter:
            result.append(line)
            continue

        # Check for section tags
        stripped_line = line.strip()
        if stripped_line in SECTION_TAGS:
            current_section = stripped_line
            in_code_block = False
            result.append(line)
            continue

        # Track code blocks
        if stripped_line.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        # Translate the line
        translated = translate_line(line, current_section, in_code_block)

        # Preserve trailing spaces for fill-in-blank answers
        if line and not line[-1].strip() and translated and translated.strip():
            trailing_spaces = len(line) - len(line.rstrip())
            translated = translated.rstrip() + ' ' * trailing_spaces

        result.append(translated)

    return '\n'.join(result)

def translate_data_json(content: str, is_challenges: bool = False) -> str:
    """Translate data.json file."""
    data = json.loads(content)

    def translate_value(obj):
        if isinstance(obj, dict):
            result = {}
            for key, value in obj.items():
                if key in ['title', 'description', 'name']:
                    # Try to translate the value
                    translated = None
                    if is_challenges:
                        translated = CHALLENGE_TITLES.get(value)
                    else:
                        translated = DATA_JSON_TITLES.get(value)
                    result[key] = translated if translated else value
                else:
                    result[key] = value
            return result
        return obj

    indent = 2 if is_challenges else 4
    return json.dumps(translate_value(data), indent=indent, ensure_ascii=False) + '\n'

def process_directory(src_dir: Path, dest_dir: Path, is_challenges: bool = False):
    """Process all files in a directory."""
    dest_dir.mkdir(parents=True, exist_ok=True)

    for item in sorted(src_dir.iterdir()):
        if item.is_file():
            if item.suffix == '.md':
                content = item.read_text(encoding='utf-8')
                translated = translate_exercise_file(content)
                (dest_dir / item.name).write_text(translated, encoding='utf-8')
                print(f"  ✓ {item.name}")
            elif item.name == 'data.json':
                content = item.read_text(encoding='utf-8')
                translated = translate_data_json(content, is_challenges)
                (dest_dir / item.name).write_text(translated, encoding='utf-8')
                print(f"  ✓ {item.name}")
            else:
                # Copy other files as-is
                content = item.read_text(encoding='utf-8')
                (dest_dir / item.name).write_text(content, encoding='utf-8')

def main():
    """Main translation function."""
    print("="*70)
    print("KOTLIN EXERCISES TRANSLATION TO SPANISH")
    print("="*70)
    print(f"Source: {EN_DIR}")
    print(f"Destination: {ES_DIR}")
    print()

    # Create destination directory
    ES_DIR.mkdir(parents=True, exist_ok=True)

    # Process main data.json
    if (EN_DIR / 'data.json').exists():
        print("Translating data.json (main)...")
        content = (EN_DIR / 'data.json').read_text(encoding='utf-8')
        translated = translate_data_json(content)
        (ES_DIR / 'data.json').write_text(translated, encoding='utf-8')
        print("  ✓ data.json")
        print()

    # List of directories to process
    directories = [
        ('output', False),
        ('stringTemplates', False),
        ('variables', False),
        ('booleans', False),
        ('arithmeticOperators', False),
        ('comparisonLogicalOperators', False),
        ('conditionalStatements', False),
        ('whileLoops', False),
        ('forLoops', False),
        ('lists', False),
        ('sets', False),
        ('challenges', True),
    ]

    total_files = 0
    total_md = 0
    total_json = 0

    for dirname, is_challenges in directories:
        src_path = EN_DIR / dirname
        dest_path = ES_DIR / dirname

        if src_path.exists() and src_path.is_dir():
            print(f"Processing {dirname}/...")

            process_directory(src_path, dest_path, is_challenges)

            # Count files
            md_count = len(list(src_path.glob('*.md')))
            json_count = len(list(src_path.glob('data.json')))
            total_md += md_count
            total_json += json_count
            total_files += md_count + json_count
            print()

    print("="*70)
    print("TRANSLATION COMPLETE!")
    print("="*70)
    print(f"Total files processed: {total_files}")
    print(f"  - Markdown exercises: {total_md}")
    print(f"  - JSON files: {total_json}")
    print(f"Translated files saved to: {ES_DIR}")
    print("="*70)

if __name__ == '__main__':
    main()
