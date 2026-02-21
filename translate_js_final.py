#!/usr/bin/env python3
"""
Comprehensive Spanish translation for JavaScript exercises.
This version includes an expanded translation dictionary.
"""

import json
import shutil
from pathlib import Path
import re

# Complete phrase translations - sorted alphabetically for easy lookup
TRANSLATIONS = {
    # A
    '"__Hello, World!__" is the traditional first program for beginning programming in a new language.': '"__¡Hola, mundo!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje.',
    '"__Hello, World!__" is the traditional first program for beginning programming in a new language or environment.': '"__¡Hola, mundo!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.',
    'A key can be any string or number.': 'Una clave puede ser cualquier cadena o número.',
    'A Pythagorean triplet is a set of three natural numbers, `a` < `b` < `c`, for which, <latex>a^2 + b^2 = c^2</latex>\nFor example, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>\nThere exists exactly one Pythagorean triplet for which `a` + `b` + `c` = 1000.': 'Un triplete pitagórico es un conjunto de tres números naturales, `a` < `b` < `c`, para los cuales, <latex>a^2 + b^2 = c^2</latex>\nPor ejemplo, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>\nExiste exactamente un triplete pitagórico para el cual `a` + `b` + `c` = 1000.',
    'A variable is created the moment you first assign a value to it.': 'Una variable se crea en el momento en que le asignas un valor por primera vez.',
    'Accessing dictionary values by key is just like accessing array values by index:': 'Acceder a los valores del diccionario por clave es igual que acceder a los valores del arreglo por índice:',
    'Add a method, `description`, to your `Animal` class.\nUsing two separate print statements, it should print out the `gender` and `legs` of the animal it\'s called on.\nThen call `description` method': 'Agrega un método, `description`, a tu clase `Animal`.\nUsando dos declaraciones de impresión separadas, debe imprimir el `gender` y `legs` del animal en el que se llama.\nLuego llama al método `description`',
    'Add a new `else if` statement checking if `time` is equal to `0` and, in the code block, print the string `"It\'s midnight"`': 'Agrega una nueva declaración `else if` que verifique si `time` es igual a `0` y, en el bloque de código, imprime la cadena `"It\'s midnight"`',
    'Add one more _key-value pair_ to the `user` variable, with the name `"profession"` for the key and `"Developer"` as the value': 'Agrega un par _clave-valor_ más a la variable `user`, con el nombre `"profession"` para la clave y `"Developer"` como valor',
    'Add the missing parts of the template literal': 'Agrega las partes faltantes del literal de plantilla',
    'Add the parameters `gender` and `legs` inside the class': 'Agrega los parámetros `gender` y `legs` dentro de la clase',
    'Add to the variable `num` the value `15` using the *addition assignment* operator, then print its value': 'Agrega a la variable `num` el valor `15` usando el operador de *asignación de adición*, luego imprime su valor',
    'An array doesn\'t have to have a fixed length.\nYou can add items to the end of an array any time you like!\nTo add an item to an array we use the `push` function:': 'Un arreglo no tiene que tener una longitud fija.\n¡Puedes agregar elementos al final de un arreglo en cualquier momento!\nPara agregar un elemento a un arreglo usamos la función `push`:',
    'An array index behaves like any other variable name.\nIt can be used to access as well as assign values.\nYou saw how to access an array index like this:\nThis is how an assignment works:': 'Un índice de arreglo se comporta como cualquier otro nombre de variable.\nSe puede usar para acceder así como para asignar valores.\nViste cómo acceder a un índice de arreglo así:\nAsí es como funciona una asignación:',
    'An array stores multiple values of one or multiple types and uses **indexes** to distinguish these values.': 'Un arreglo almacena múltiples valores de uno o varios tipos y usa **índices** para distinguir estos valores.',
    'An example of a variable creation named `x` is:': 'Un ejemplo de creación de una variable llamada `x` es:',
    'An index is like an address that identifies the item\'s place in the array.': 'Un índice es como una dirección que identifica el lugar del elemento en el arreglo.',
    'Array elements could be of any type.\nIn fact, above we have, in order, a string, an integer and a boolean.\nBut we can also have arrays with arrays as well!': 'Los elementos del arreglo pueden ser de cualquier tipo.\nDe hecho, arriba tenemos, en orden, una cadena, un entero y un booleano.\n¡Pero también podemos tener arreglos con arreglos!',
    'Array indices begin with `0`, **not** `1`! You access the first item of an array like this: `arrayName[0]`.\nThe second item in an array is at index 1: `arrayName[1]`.': 'Los índices del arreglo comienzan con `0`, **no** con `1`! Accedes al primer elemento de un arreglo así: `arrayName[0]`.\nEl segundo elemento de un arreglo está en el índice 1: `arrayName[1]`.',
    'Arrays are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.': 'Los arreglos son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un solo nombre de variable.',
    'As for arrays, we can loop between dictionary elements using the `Object.entries()` method.': 'Al igual que con los arreglos, podemos iterar entre los elementos del diccionario usando el método `Object.entries()`.',
    'Assign `4` as default value to the `legs` parameter.\nCreate an instance of the `Animal` class called `dog`': 'Asigna `4` como valor predeterminado al parámetro `legs`.\nCrea una instancia de la clase `Animal` llamada `dog`',
    'Assign a string to the variable `age` and display its value.': 'Asigna una cadena a la variable `age` y muestra su valor.',
    'Assign the boolean value `false` to the variable `musicOn`, then print its value': 'Asigna el valor booleano `false` a la variable `musicOn`, luego imprime su valor',
    'Assign to the `Animal` instance, the `"female"` gender.\nPrint the gender of the `Animal` instance': 'Asigna a la instancia de `Animal`, el género `"female"`.\nImprime el género de la instancia de `Animal`',
    'Assign to the variable `counter` a number': 'Asigna un número a la variable `counter`',
    'Assign to the variable `musicOn` the boolean value `true`': 'Asigna a la variable `musicOn` el valor booleano `true`',
    'Assign to the variable `num` the value `20`, then print its value': 'Asigna a la variable `num` el valor `20`, luego imprime su valor',
    'Assign to the variable `y` the value `2`.': 'Asigna a la variable `y` el valor `2`.',
    'At the end of the loop, `counter` is equal to `9`': 'Al final del bucle, `counter` es igual a `9`',

    # B
    'Because dictionaries variables are mutable, they can be changed in many ways.\nItems can be removed from a dictionary with the \'delete\' keyword:\nwill remove the key `keyName` and its associated value from the dictionary.': 'Debido a que las variables de diccionario son mutables, se pueden cambiar de muchas formas.\nLos elementos se pueden eliminar de un diccionario con la palabra clave \'delete\':\neliminará la clave `keyName` y su valor asociado del diccionario.',
    'Boolean values are referred to as logical, because they can only ever be true or false.': 'Los valores booleanos se conocen como lógicos, porque solo pueden ser verdaderos o falsos.',
    'Boolean values are referred to as logical, because they can only ever be true or false.\nYou can evaluate any expression in JavaScript, and get one of two answers, `true` or `false`.': 'Los valores booleanos se conocen como lógicos, porque solo pueden ser verdaderos o falsos.\nPuedes evaluar cualquier expresión en JavaScript y obtener una de dos respuestas, `true` o `false`.',
    'By considering the terms in the Fibonacci sequence whose values do not exceed `n`, find the sum of the even-valued terms.': 'Al considerar los términos de la secuencia de Fibonacci cuyos valores no exceden `n`, encuentra la suma de los términos pares.',
    'By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.': 'Al listar los primeros seis números primos: 2, 3, 5, 7, 11 y 13, podemos ver que el 6º primo es 13.',

    # C
    'Calculate the difference between 25 and 15': 'Calcula la diferencia entre 25 y 15',
    'Calculate the difference between the numbers 9 and 4, then print the variable `difference`': 'Calcula la diferencia entre los números 9 y 4, luego imprime la variable `difference`',
    'Calculate the product between the numbers 9 and 4 (in this order), then print the variable `product`': 'Calcula el producto entre los números 9 y 4 (en este orden), luego imprime la variable `product`',
    'Calculate the product of `result` with the value `5` using the *multiplication assignment* operator, then print its value': 'Calcula el producto de `result` con el valor `5` usando el operador de *asignación de multiplicación*, luego imprime su valor',
    'Calculate the quotient between the numbers 40 and 5, then print the variable `quotient`': 'Calcula el cociente entre los números 40 y 5, luego imprime la variable `quotient`',
    'Calculate the quotient of `result` diving its value by `5` using the *division assignment* operator, then print its value': 'Calcula el cociente de `result` dividiendo su valor por `5` usando el operador de *asignación de división*, luego imprime su valor',
    'Calculate the remainder between the numbers 10 and 4, then print the variable `remainder`': 'Calcula el resto entre los números 10 y 4, luego imprime la variable `remainder`',
    'Calculate the remainder from the division between 22 and 6, then print the `result`': 'Calcula el resto de la división entre 22 y 6, luego imprime el `result`',
    'Calculate the remainder of `result` with the value `3` using the *remainder assignment* operator, then print its value': 'Calcula el resto de `result` con el valor `3` usando el operador de *asignación de resto*, luego imprime su valor',
    'Calculate the sum between the numbers 4 and 9 (in this order), then print the variable `sum`': 'Calcula la suma entre los números 4 y 9 (en este orden), luego imprime la variable `sum`',
    'Call the `pop()` method to remove the last item from the list': 'Llama al método `pop()` para eliminar el último elemento de la lista',
    'Can you find one way to create an array?': '¿Puedes encontrar una forma de crear un arreglo?',
    'Can you make `Dog` a subclass of `Animal`?\n`legs` should be inside the `Animal` class while `breed` should be inside the `Dog` class': '¿Puedes hacer que `Dog` sea una subclase de `Animal`?\n`legs` debe estar dentro de la clase `Animal` mientras que `breed` debe estar dentro de la clase `Dog`',
    'Can you order these lines into a functional code?': '¿Puedes ordenar estas líneas en un código funcional?',
    'Can you order these lines so that `"dog"` is displayed in the output?': '¿Puedes ordenar estas líneas para que se muestre `"dog"` en la salida?',
    'Can you order these lines so they form a proper __function__?': '¿Puedes ordenar estas líneas para que formen una __función__ adecuada?',
    'Check if `num` is **greater than or equal to** to `8`, printing the boolean result': 'Verifica si `num` es **mayor o igual que** `8`, imprimiendo el resultado booleano',
    'Check if `num` is **greater than** `7`, printing the boolean result': 'Verifica si `num` es **mayor que** `7`, imprimiendo el resultado booleano',
    'Check if `num` is **less than or equal to** to `8`, printing the boolean result': 'Verifica si `num` es **menor o igual que** `8`, imprimiendo el resultado booleano',
    'Check if `num` is **less than** `3`, printing the boolean result': 'Verifica si `num` es **menor que** `3`, imprimiendo el resultado booleano',
    'Check if `num` is equal to `5`, printing the boolean result': 'Verifica si `num` es igual a `5`, imprimiendo el resultado booleano',
    'Check if `word` is **NOT** equal to `dog`, printing the boolean result': 'Verifica si `word` es **distinto de** `dog`, imprimiendo el resultado booleano',
    'Choose the correct variable for a user who has just logged out': 'Elige la variable correcta para un usuario que acaba de cerrar sesión',
    'Compare the `counter` variable with a number': 'Compara la variable `counter` con un número',
    'Complete the `for` loop in the following code': 'Completa el bucle `for` en el siguiente código',
    'Complete the `for` loop in the following code in order to execute the code block `3` times': 'Completa el bucle `for` en el siguiente código para ejecutar el bloque de código `3` veces',
    'Complete the `for` loop in the following code in order to repeat the code block **3** times': 'Completa el bucle `for` en el siguiente código para repetir el bloque de código **3** veces',
    'Complete the code in order to calculate the average for the following list of numbers `1, 4, 6, 7, 9`.\nUse the `reducer()` function to calculate the sum of the numbers': 'Completa el código para calcular el promedio de la siguiente lista de números `1, 4, 6, 7, 9`.\nUsa la función `reducer()` para calcular la suma de los números',
    'Complete the code in order to call the function with the name `Smith`': 'Completa el código para llamar a la función con el nombre `Smith`',
    'Complete the code in order to call the function without the _default_ argument': 'Completa el código para llamar a la función sin el argumento _predeterminado_',
    'Complete the code in order to create a valid array': 'Completa el código para crear un arreglo válido',
    'Complete the code in order to create a valid dictionary (object)': 'Completa el código para crear un diccionario válido (objeto)',
    'Complete the code in order to create a valid function called `sayHello`': 'Completa el código para crear una función válida llamada `sayHello`',
    'Complete the code in order to create a valid function called `sumAllNumbers` passing the following array of numbers `[15, 24, 31, 79]` and `true` to print the result': 'Completa el código para crear una función válida llamada `sumAllNumbers` pasando el siguiente arreglo de números `[15, 24, 31, 79]` y `true` para imprimir el resultado',
    'Complete the code in order to print the following numbers `(3, 24, 9, 12, 18)` using a `forEach` loop': 'Completa el código para imprimir los siguientes números `(3, 24, 9, 12, 18)` usando un bucle `forEach`',
    'Complete the code in order to print the length of the array': 'Completa el código para imprimir la longitud del arreglo',
    'Complete the code in order to print the sum between the **second** and the **fourth** item of the array': 'Completa el código para imprimir la suma entre el **segundo** y el **cuarto** elemento del arreglo',

    # D
    'Decision making is required when we want to execute code only if a certain condition is satisfied.': 'La toma de decisiones es necesaria cuando queremos ejecutar código solo si se cumple una determinada condición.',
    'Declarations conditionally executed based on the results of an `if...else` block.': 'Declaraciones ejecutadas condicionalmente basadas en los resultados de un bloque `if...else`.',

    # E
    'Each property is separated by a comma.': 'Cada propiedad está separada por una coma.',
    'Every variable in JavaScript is an object.': 'Cada variable en JavaScript es un objeto.',
    
    # F
    'Fill in the blanks with the `while` loop to repeat the block of code': 'Completa los espacios con el bucle `while` para repetir el bloque de código',
    'For example, when you call:\nJavaScript checks to see if `arrayName` has a `push()` method (which all arrays have) and executes that method if it finds it.': 'Por ejemplo, cuando llamas:\nJavaScript verifica si `arrayName` tiene un método `push()` (que todos los arreglos tienen) y ejecuta ese método si lo encuentra.',

    # H
    'Hello, World!': '¡Hola, mundo!',

    # I
    'If we print the variable `x` we get back the number `1`:': 'Si imprimimos la variable `x` obtenemos el número `1`:',
    'In JavaScript you declare constants with the `let` or `const` keywords and variables with the `var` keyword.': 'En JavaScript declaras constantes con las palabras clave `let` o `const` y variables con la palabra clave `var`.',
    'In JavaScript we can loop through an array in a very simple way using the `for..of` keywords:': 'En JavaScript podemos iterar a través de un arreglo de una manera muy simple usando las palabras clave `for..of`:',
    'In JavaScript we can use the `+` sign to display two or more strings together, like:': 'En JavaScript podemos usar el signo `+` para mostrar dos o más cadenas juntas, como:',
    'In JavaScript we use the `function` keyword followed by the name of the function:': 'En JavaScript usamos la palabra clave `function` seguida del nombre de la función:',
    'In fact, above we have, in order, a string, an integer and a boolean.': 'De hecho, arriba tenemos, en orden, una cadena, un entero y un booleano.',
    'In this way we have assigned the value `1` to the variable named `x`.': 'De esta manera hemos asignado el valor `1` a la variable llamada `x`.',
    'Inside the block of code, we should **NOT** miss to add the line `count += 1`.\nIt increments the `count` value, otherwise, our loop will be infinite': 'Dentro del bloque de código, **NO** debemos olvidar agregar la línea `count += 1`.\nIncrementa el valor de `count`, de lo contrario, nuestro bucle será infinito',
    'Instead of rewriting the whole code, it\'s much cleaner to define a function, which can then be used repeatedly.': 'En lugar de reescribir todo el código, es mucho más limpio definir una función, que luego se puede usar repetidamente.',
    'It is used to add two numbers, like:': 'Se usa para sumar dos números, como:',
    'It is used to divide two numbers together, like:': 'Se usa para dividir dos números, como:',
    'It is used to find the remainder after a division between two numbers, like:': 'Se usa para encontrar el resto después de una división entre dos números, como:',
    'It is used to multiply two numbers together, like:': 'Se usa para multiplicar dos números, como:',
    'It is used to subtract one number from another, like:': 'Se usa para restar un número de otro, como:',
    'It returns a **boolean** (`true` or `false`) stating whether two expressions are equal, for example:': 'Devuelve un **booleano** (`true` o `false`) indicando si dos expresiones son iguales, por ejemplo:',

    # J
    'JavaScript has a basic Boolean type, called `boolean`.': 'JavaScript tiene un tipo Boolean básico, llamado `boolean`.',
    'JavaScript is an object-oriented programming language, which means it manipulates programming constructs called objects.\nYou can think of an object as a single data structure that contains data as well as functions; the functions of an object are called its methods.': 'JavaScript es un lenguaje de programación orientado a objetos, lo que significa que manipula constructos de programación llamados objetos.\nPuedes pensar en un objeto como una única estructura de datos que contiene datos así como funciones; las funciones de un objeto se llaman sus métodos.',

    # K
    'Keep in mind that the right index is excluded': 'Ten en cuenta que el índice derecho está excluido',

    # L
    'Let\'s assume we want to play outside only if the weather is nice.': 'Supongamos que queremos jugar afuera solo si el clima es agradable.',
    'Let\'s continue with the **subtraction** `-` operator.': 'Continuemos con el operador de **resta** `-`.',
    'Let\'s learn the `while` loop, getting the same output above.': 'Aprendamos el bucle `while`, obteniendo la misma salida anterior.',
    'Let\'s see the **division** `/` operator.': 'Veamos el operador de **división** `/`.',
    'Let\'s see the **multiplication** `*` operator.': 'Veamos el operador de **multiplicación** `*`.',
    'Let\'s see the **remainder** `%` operator.': 'Veamos el operador de **resto** `%`.',
    'Let\'s start with the **equal** `==` comparison operator.': 'Comencemos con el operador de comparación **igual** `==`.',
    'Let\'s start with the arithmetic operators, in particular with the **addition** `+` operator.': 'Comencemos con los operadores aritméticos, en particular con el operador de **suma** `+`.',
    'Like this program repeating statements to display `hello`': 'Como este programa que repite declaraciones para mostrar `hello`',

    # N
    'Not everything in JavaScript is an object.': 'No todo en JavaScript es un objeto.',
    'Now you know the basics of JavaScript!': '¡Ahora conoces los conceptos básicos de JavaScript!',

    # O
    'Object properties are basically `key: value` pairs.': 'Las propiedades del objeto son básicamente pares `clave: valor`.',
    'Objects are enclosed in curly brackets, like so:': 'Los objetos se encierran entre llaves, así:',
    'Often in programming, we need to repeat a block of code, for example:': 'A menudo en programación, necesitamos repetir un bloque de código, por ejemplo:',
    'Operators are used to perform operations on variables and values.': 'Los operadores se usan para realizar operaciones sobre variables y valores.',
    'Obviously, for long statements we would spend a lot of time writing the code, but fortunately, we can use loops.': 'Obviamente, para declaraciones largas pasaríamos mucho tiempo escribiendo el código, pero por suerte, podemos usar bucles.',

    # P
    'Print a boolean checking if `num` is equal to `5`': 'Imprime un booleano verificando si `num` es igual a `5`',
    'Print the gender of the `Animal` instance': 'Imprime el género de la instancia de `Animal`',

    # S
    'So we created a variable `count` assigning `2`, the initial value.': 'Así creamos una variable `count` asignando `2`, el valor inicial.',
    'Sometimes, you only want to access a portion of an array.': 'A veces, solo quieres acceder a una porción de un arreglo.',
    'Sometimes you need to search for an item in an array.': 'A veces necesitas buscar un elemento en un arreglo.',
    'Subtract `1` from the `counter` variable': 'Resta `1` a la variable `counter`',

    # T
    'The `Animal` class should have a method `speak()` that returns a string.': 'La clase `Animal` debe tener un método `speak()` que devuelve una cadena.',
    'The `Dog` class should have a method `speak()` that returns a different string.': 'La clase `Dog` debe tener un método `speak()` que devuelve una cadena diferente.',
    'The `Dog` class should have a method that returns the string `Bau Bau!!`': 'La clase `Dog` debe tener un método que devuelve la cadena `Bau Bau!!`',
    'The `speak()` method should return `Bau Bau!!`': 'El método `speak()` debe devolver `Bau Bau!!`',
    'The code above inserts `"Ali"` at index `1`, which moves everything, after this index, down by 1.\nThe second value `0` means _deleteCount_, in this case, we don\'t delete any item in the array; but if we had specified `1` the value `Zac` would have been removed from the array': 'El código anterior inserta `"Ali"` en el índice `1`, que mueve todo, después de este índice, hacia abajo por 1.\nEl segundo valor `0` significa _deleteCount_, en este caso, no eliminamos ningún elemento del arreglo; pero si hubiéramos especificado `1`, el valor `Zac` habría sido eliminado del arreglo',
    'The code above prints the first index that contains the string `"Zac"`, `1` in this case.': 'El código anterior imprime el primer índice que contiene la cadena `"Zac"`, `1` en este caso.',
    'The function should return "Hello, World!".': 'La función debe devolver "¡Hola, mundo!".',
    'The index appears directly after the array name, in between brackets, like this:': 'El índice aparece directamente después del nombre del arreglo, entre corchetes, así:',
    'The key `key1` points to the value `1`, `key2` to `2`, and so on.': 'La clave `key1` apunta al valor `1`, `key2` a `2`, y así sucesivamente.',
    'The value of a constant can\'t be changed once it\'s set, whereas a variable can be set to a different value in the future.': 'El valor de una constante no se puede cambiar una vez establecido, mientras que una variable puede establecerse a un valor diferente en el futuro.',
    'Then we have used the `while` statement that will run the block of code until the condition `count <= 5` is `true`.': 'Luego hemos usado la declaración `while` que ejecutará el bloque de código hasta que la condición `count <= 5` sea `true`.',
    'Then use the `splice()` method to add `"bear"` as first item of the array': 'Luego usa el método `splice()` para agregar `"bear"` como primer elemento del arreglo',
    'This is a dictionary called `objectName` with three *key-value pairs*.': 'Este es un diccionario llamado `objectName` con tres *pares clave-valor*.',
    'This is how an assignment works:': 'Así es como funciona una asignación:',
    'This other evaluates to 0 because 9 divided by 3 has a quotient of 3 and leaves a remainder of 0': 'Este otro evalúa a 0 porque 9 dividido por 3 tiene un cociente de 3 y deja un resto de 0',
    'This produces the following output:': 'Esto produce la siguiente salida:',
    'To assign a value to a variable we can use the `=` sign, like:': 'Para asignar un valor a una variable podemos usar el signo `=`, como:',
    'To create a variable, we need to give it a **name** keeping in mind that it must not contain spaces.': 'Para crear una variable, necesitamos darle un **nombre** teniendo en cuenta que no debe contener espacios.',
    'To print `Hello, World!` on the screen with JavaScript we can write': 'Para imprimir `Hello, World!` en la pantalla con JavaScript podemos escribir',
    'To add an item to an array we use the `push` function:': 'Para agregar un elemento a un arreglo usamos la función `push`:',

    # U
    'Use the `indexOf()` method to print the index of `"dog"`.': 'Usa el método `indexOf()` para imprimir el índice de `"dog"`.',
    'Use a `for` loop to print the numbers from `3` to `6` (both included)': 'Usa un bucle `for` para imprimir los números de `3` a `6` (ambos incluidos)',
    'Use the spread operator `...` to copy all properties from one object to another.': 'Usa el operador de propagación `...` para copiar todas las propiedades de un objeto a otro.',

    # V
    'Variables are containers for storing data values.': 'Las variables son contenedores para almacenar valores de datos.',
    'You can access an individual item of the array by its index.': 'Puedes acceder a un elemento individual del arreglo por su índice.',
    'You can assign items to an array with an expression of the form:': 'Puedes asignar elementos a un arreglo con una expresión de la forma:',
    'You can think of an object as a single data structure that contains data as well as functions; the functions of an object are called its methods.': 'Puedes pensar en un objeto como una única estructura de datos que contiene datos así como funciones; las funciones de un objeto se llaman sus métodos.',
    'You might have considered the situation where you would like to reuse a piece of code, just with a few different values.': 'Podrías haber considerado la situación en la que te gustaría reutilizar un fragmento de código, solo con algunos valores diferentes.',
    'You saw how to access an array index like this:': 'Viste cómo acceder a un índice de arreglo así:',
    'We can also insert items into an array in a specific index, using the `splice()` method:': 'También podemos insertar elementos en un arreglo en un índice específico, usando el método `splice()`:',
    'We can slice an array as we want!': '¡Podemos cortar un arreglo como queramos!',
    'We do this by defining the indices we want to include after the name of the array: `numbers.slice(1, 3)`.': 'Hacemos esto definiendo los índices que queremos incluir después del nombre del arreglo: `numbers.slice(1, 3)`.',
    'We know how to repeat code using a `while` loop.': 'Sabemos cómo repetir código usando un bucle `while`.',
    'We use the `console.log()` function to output data to the standard output device (screen).': 'Usamos la función `console.log()` para mostrar datos en el dispositivo de salida estándar (pantalla).',
    'We\'ve already learned that to assign a value to a variable we can use the `=` sign, like:': 'Ya hemos aprendido que para asignar un valor a una variable podemos usar el signo `=`, como:',
    'Write a function that returns the string `"Hello, World!"`.': 'Escribe una función que devuelva la cadena `"Hello, World!"`.',

    # Comments and output
    '// prints 1': '// imprime 1',
    '// prints 2': '// imprime 2',
    '// prints 8': '// imprime 8',
    '// prints 15': '// imprime 15',
    '// prints 0': '// imprime 0',
    '// prints ["a", "b", "c"]': '// imprime ["a", "b", "c"]',
    '// prints "Hello!"': '// imprime "Hello!"',
    '// prints "Hello, World!"': '// imprime "Hello, World!"',
    '// prints true': '// imprime true',
    '// prints false': '// imprime false',
    '// prints 1, 2, 3': '// imprime 1, 2, 3',
    '// play outside': '// jugar afuera',

    # Test messages
    'Test Case': 'Caso de prueba',
    'failed': 'falló',
    'Executed': 'Ejecutados',
    'tests, with': 'pruebas, con',
    'failures': 'fallos',

    # Challenge names
    'Hello World!': '¡Hola, mundo!',
    'The first name is': 'El nombre es',
    'It\'s morning': 'Es por la mañana',
    'It\'s midday': 'Es mediodía',
    'It\'s afternoon': 'Es por la tarde',
    'It\'s evening': 'Es por la noche',
    'It\'s midnight': 'Es medianoche',
    'the number is 2': 'el número es 2',
    'the number is 3': 'el número es 3',
    'the number is 4': 'el número es 4',
    'the number is 5': 'el número es 5',
    'the number is 6': 'el número es 6',
    'the number is greather than 4': 'el número es mayor que 4',
    'the number is lower than 3': 'el número es menor que 3',
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
    for en, es in sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True):
        if en in result:
            result = result.replace(en, es)
    return result

def translate_line(line, in_code_block):
    """Translate a single line based on context."""
    stripped = line.strip()
    
    if any(tag in stripped for tag in SECTION_TAGS):
        return line
    
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
    
    if '--err-t' in line:
        if 'failed' in line:
            return line.replace('failed', 'falló')
        return line
    
    if in_code_block:
        result = line
        if '//' in result:
            comment_start = result.find('//')
            before_comment = result[:comment_start]
            comment = result[comment_start:]
            translated_comment = translate_text(comment[2:])
            result = before_comment + '//' + translated_comment
        
        def replace_string(match):
            quote = match.group(1)
            content = match.group(2)
            translated = translate_text(content)
            return quote + translated + quote
        
        result = re.sub(r'(["\'`])(.*?)(?<!\\)\1', replace_string, result)
        return result
    else:
        return translate_text(line)

def translate_exercise_file(content):
    """Translate an exercise markdown file."""
    lines = content.split('\n')
    result = []
    in_code_block = False
    in_yaml = False
    
    for i, line in enumerate(lines):
        if i == 0 and line.startswith('---'):
            in_yaml = True
            result.append(line)
            continue
        if in_yaml:
            result.append(line)
            if line.strip() == '---':
                in_yaml = False
            continue
        
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
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
    
    if es_base.exists():
        shutil.rmtree(es_base)
    es_base.mkdir(parents=True, exist_ok=True)
    
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
