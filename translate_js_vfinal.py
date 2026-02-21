#!/usr/bin/env python3
"""
Final comprehensive Spanish translation for JavaScript exercises.
This version handles partial text matches and adds more translations.
"""

import json
import shutil
from pathlib import Path
import re

# Complete phrase translations
TRANSLATIONS = {
    # Phrases from classes/1.md
    'JavaScript is an object-oriented programming language, which means it manipulates programming constructs called objects.': 'JavaScript es un lenguaje de programación orientado a objetos, lo que significa que manipula constructos de programación llamados objetos.',
    'For example, when you call:': 'Por ejemplo, cuando llamas:',
    'JavaScript checks to see if `arrayName` has a `push()` method (which all arrays have) and executes that method if it finds it.': 'JavaScript verifica si `arrayName` tiene un método `push()` (que todos los arreglos tienen) y ejecuta ese método si lo encuentra.',
    
    # Objects
    '**Objects** are similar to arrays, but you access values by looking up a *key* instead of an index': 'Los **objetos** son similares a los arreglos, pero accedes a los valores buscando una *clave* en lugar de un índice',
    'A key can be any string or number.': 'Una clave puede ser cualquier cadena o número.',
    'Objects are enclosed in curly brackets, like so:': 'Los objetos se encierran entre llaves, así:',
    'This is a dictionary called `objectName` with three *key-value pairs*.': 'Este es un diccionario llamado `objectName` con tres *pares clave-valor*.',
    'The key `key1` points to the value `1`, `key2` to `2`, and so on.': 'La clave `key1` apunta al valor `1`, `key2` a `2`, y así sucesivamente.',
    'Object properties are basically `key: value` pairs.': 'Las propiedades del objeto son básicamente pares `clave: valor`.',
    'Not everything in JavaScript is an object.': 'No todo en JavaScript es un objeto.',
    
    # Variable phrases
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
    'You can access an individual item of the array by its index.': 'Puedes acceder a un elemento individual del arreglo por su índice.',
    'An index is like an address that identifies the item\'s place in the array.': 'Un índice es como una dirección que identifica el lugar del elemento en el arreglo.',
    'The index appears directly after the array name, in between brackets, like this:': 'El índice aparece directamente después del nombre del arreglo, entre corchetes, así:',
    'Array indices begin with `0`, **not** `1`! You access the first item of an array like this: `arrayName[0]`.': 'Los índices del arreglo comienzan con `0`, **no** con `1`! Accedes al primer elemento de un arreglo así: `arrayName[0]`.',
    'The second item in an array is at index 1: `arrayName[1]`.': 'El segundo elemento de un arreglo está en el índice 1: `arrayName[1]`.',
    'An array index behaves like any other variable name.': 'Un índice de arreglo se comporta como cualquier otro nombre de variable.',
    'It can be used to access as well as assign values.': 'Se puede usar para acceder así como para asignar valores.',
    'Array elements could be of any type.': 'Los elementos del arreglo pueden ser de cualquier tipo.',
    'An array doesn\'t have to have a fixed length.': 'Un arreglo no tiene que tener una longitud fija.',
    'You can add items to the end of an array any time you like!': '¡Puedes agregar elementos al final de un arreglo en cualquier momento!',
    'To add an item to an array we use the `push` function:': 'Para agregar un elemento a un arreglo usamos la función `push`:',
    'Sometimes, you only want to access a portion of an array.': 'A veces, solo quieres acceder a una porción de un arreglo.',
    'Keep in mind that the right index is excluded': 'Ten en cuenta que el índice derecho está excluido',
    'We can slice an array as we want!': '¡Podemos cortar un arreglo como queramos!',
    'Sometimes you need to search for an item in an array.': 'A veces necesitas buscar un elemento en un arreglo.',
    'In JavaScript we can loop through an array in a very simple way using the `for..of` keywords:': 'En JavaScript podemos iterar a través de un arreglo de una manera muy simple usando las palabras clave `for..of`:',
    'A variable name follows the `for` keyword, it will be assigned the value of each array item in turn.': 'Un nombre de variable sigue a la palabra clave `for`, se le asignará el valor de cada elemento del arreglo a su vez.',
    
    # Functions
    'You might have considered the situation where you would like to reuse a piece of code, just with a few different values.': 'Podrías haber considerado la situación en la que te gustaría reutilizar un fragmento de código, solo con algunos valores diferentes.',
    'Instead of rewriting the whole code, it\'s much cleaner to define a function, which can then be used repeatedly.': 'En lugar de reescribir todo el código, es mucho más limpio definir una función, que luego se puede usar repetidamente.',
    'In JavaScript we use the `function` keyword followed by the name of the function:': 'En JavaScript usamos la palabra clave `function` seguida del nombre de la función:',
    
    # Booleans
    'JavaScript has a basic Boolean type, called `boolean`.': 'JavaScript tiene un tipo Boolean básico, llamado `boolean`.',
    'Boolean values are referred to as logical, because they can only ever be true or false.': 'Los valores booleanos se conocen como lógicos, porque solo pueden ser verdaderos o falsos.',
    'You can evaluate any expression in JavaScript, and get one of two answers, `true` or `false`.': 'Puedes evaluar cualquier expresión en JavaScript y obtener una de dos respuestas, `true` o `false`.',
    
    # Output
    '"__Hello, World!__" is the traditional first program for beginning programming in a new language.': '"__¡Hola, mundo!__" es el primer programa tradicional para comenzar a programar en un nuevo lenguaje.',
    '__"Hello, World!"__ is the traditional first program for beginning programming in a new language or environment.': '__"¡Hola, mundo!"__ es el primer programa tradicional para comenzar a programar en un nuevo lenguaje o entorno.',
    'We use the `console.log()` function to output data to the standard output device (screen).': 'Usamos la función `console.log()` para mostrar datos en el dispositivo de salida estándar (pantalla).',
    'To print `Hello, World!` on the screen with JavaScript we can write': 'Para imprimir `Hello, World!` en la pantalla con JavaScript podemos escribir',
    
    # Template literals
    'In JavaScript we can use the `+` sign to display two or more strings together, like:': 'En JavaScript podemos usar el signo `+` para mostrar dos o más cadenas juntas, como:',
    
    # Conditional statements
    'Decision making is required when we want to execute code only if a certain condition is satisfied.': 'La toma de decisiones es necesaria cuando queremos ejecutar código solo si se cumple una determinada condición.',
    'Declarations conditionally executed based on the results of an `if...else` block.': 'Declaraciones ejecutadas condicionalmente basadas en los resultados de un bloque `if...else`.',
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
    'To assign a value to a variable we can use the `=` sign, like:': 'Para asignar un valor a una variable podemos usar el signo `=`, como:',
    
    # Arithmetic operators
    'Operators are used to perform operations on variables and values.': 'Los operadores se usan para realizar operaciones sobre variables y valores.',
    'Let\'s start with the arithmetic operators, in particular with the **addition** `+` operator.': 'Comencemos con los operadores aritméticos, en particular con el operador de **suma** `+`.',
    'It is used to add two numbers, like:': 'Se usa para sumar dos números, como:',
    'Let\'s continue with the **subtraction** `-` operator.': 'Continuemos con el operador de **resta** `-`.',
    'It is used to subtract one number from another, like:': 'Se usa para restar un número de otro, como:',
    'Let\'s see the **multiplication** `*` operator.': 'Veamos el operador de **multiplicación** `*`.',
    'It is used to multiply two numbers together, like:': 'Se usa para multiplicar dos números, como:',
    'Let\'s see the **division** `/` operator.': 'Veamos el operador de **división** `/`.',
    'It is used to divide two numbers together, like:': 'Se usa para dividir dos números, como:',
    'Let\'s see the **remainder** `%` operator.': 'Veamos el operador de **resto** `%`.',
    'It is used to find the remainder after a division between two numbers, like:': 'Se usa para encontrar el resto después de una división entre dos números, como:',
    'This evaluates to 1 because 5 divided by 2 has a quotient of 2 and a remainder of 1': 'Esto evalúa a 1 porque 5 dividido por 2 tiene un cociente de 2 y un resto de 1',
    'This other evaluates to 0 because 9 divided by 3 has a quotient of 3 and leaves a remainder of 0': 'Este otro evalúa a 0 porque 9 dividido por 3 tiene un cociente de 3 y deja un resto de 0',
    
    # Instructions
    'Assign to the variable `y` the value `2`.': 'Asigna a la variable `y` el valor `2`.',
    'Assign to the variable `num` the value `20`, then print its value': 'Asigna a la variable `num` el valor `20`, luego imprime su valor',
    'Calculate the sum between the numbers 4 and 9 (in this order), then print the variable `sum`': 'Calcula la suma entre los números 4 y 9 (en este orden), luego imprime la variable `sum`',
    'Calculate the difference between the numbers 9 and 4, then print the variable `difference`': 'Calcula la diferencia entre los números 9 y 4, luego imprime la variable `difference`',
    'Calculate the product between the numbers 9 and 4 (in this order), then print the variable `product`': 'Calcula el producto entre los números 9 y 4 (en este orden), luego imprime la variable `product`',
    'Calculate the quotient between the numbers 40 and 5, then print the variable `quotient`': 'Calcula el cociente entre los números 40 y 5, luego imprime la variable `quotient`',
    'Calculate the remainder between the numbers 10 and 4, then print the variable `remainder`': 'Calcula el resto entre los números 10 y 4, luego imprime la variable `remainder`',
    'Calculate the difference between 25 and 15': 'Calcula la diferencia entre 25 y 15',
    'Calculate the remainder from the division between 22 and 6, then print the `result`': 'Calcula el resto de la división entre 22 y 6, luego imprime el `result`',
    'Calculate the product of `result` with the value `5` using the *multiplication assignment* operator, then print its value': 'Calcula el producto de `result` con el valor `5` usando el operador de *asignación de multiplicación*, luego imprime su valor',
    'Calculate the quotient of `result` diving its value by `5` using the *division assignment* operator, then print its value': 'Calcula el cociente de `result` dividiendo su valor por `5` usando el operador de *asignación de división*, luego imprime su valor',
    'Calculate the remainder of `result` with the value `3` using the *remainder assignment* operator, then print its value': 'Calcula el resto de `result` con el valor `3` usando el operador de *asignación de resto*, luego imprime su valor',
    'Add to the variable `num` the value `15` using the *addition assignment* operator, then print its value': 'Agrega a la variable `num` el valor `15` usando el operador de *asignación de adición*, luego imprime su valor',
    'Subtract `1` from the `counter` variable': 'Resta `1` a la variable `counter`',
    'Assign a string to the variable `age` and display its value.': 'Asigna una cadena a la variable `age` y muestra su valor.',
    'Assign the boolean value `false` to the variable `musicOn`, then print its value': 'Asigna el valor booleano `false` a la variable `musicOn`, luego imprime su valor',
    'Assign to the `Animal` instance, the `"female"` gender.': 'Asigna a la instancia de `Animal`, el género `"female"`.',
    'Print the gender of the `Animal` instance': 'Imprime el género de la instancia de `Animal`',
    'Assign to the variable `counter` a number': 'Asigna un número a la variable `counter`',
    'Assign to the variable `musicOn` the boolean value `true`': 'Asigna a la variable `musicOn` el valor booleano `true`',
    'Complete the code in order to create a valid array': 'Completa el código para crear un arreglo válido',
    'Complete the code in order to create a valid dictionary (object)': 'Completa el código para crear un diccionario válido (objeto)',
    'Complete the code in order to create a valid function called `sayHello`': 'Completa el código para crear una función válida llamada `sayHello`',
    'Complete the code in order to create a valid function called `sumAllNumbers` passing the following array of numbers `[15, 24, 31, 79]` and `true` to print the result': 'Completa el código para crear una función válida llamada `sumAllNumbers` pasando el siguiente arreglo de números `[15, 24, 31, 79]` y `true` para imprimir el resultado',
    'Complete the code in order to call the function with the name `Smith`': 'Completa el código para llamar a la función con el nombre `Smith`',
    'Complete the code in order to call the function without the _default_ argument': 'Completa el código para llamar a la función sin el argumento _predeterminado_',
    'Complete the code in order to calculate the average for the following list of numbers `1, 4, 6, 7, 9`.': 'Completa el código para calcular el promedio de la siguiente lista de números `1, 4, 6, 7, 9`.',
    'Use the `reducer()` function to calculate the sum of the numbers': 'Usa la función `reducer()` para calcular la suma de los números',
    'Complete the code in order to print the following numbers `(3, 24, 9, 12, 18)` using a `forEach` loop': 'Completa el código para imprimir los siguientes números `(3, 24, 9, 12, 18)` usando un bucle `forEach`',
    'Complete the code in order to print the length of the array': 'Completa el código para imprimir la longitud del arreglo',
    'Complete the code in order to print the sum between the **second** and the **fourth** item of the array': 'Completa el código para imprimir la suma entre el **segundo** y el **cuarto** elemento del arreglo',
    'Add the missing parts of the template literal': 'Agrega las partes faltantes del literal de plantilla',
    'Add one more _key-value pair_ to the `user` variable, with the name `"profession"` for the key and `"Developer"` as the value': 'Agrega un par _clave-valor_ más a la variable `user`, con el nombre `"profession"` para la clave y `"Developer"` como valor',
    'Add a new `else if` statement checking if `time` is equal to `0` and, in the code block, print the string `"It\'s midnight"`': 'Agrega una nueva declaración `else if` que verifique si `time` es igual a `0` y, en el bloque de código, imprime la cadena `"It\'s midnight"`',
    'Add a method, `description`, to your `Animal` class.': 'Agrega un método, `description`, a tu clase `Animal`.',
    'Using two separate print statements, it should print out the `gender` and `legs` of the animal it\'s called on.': 'Usando dos declaraciones de impresión separadas, debe imprimir el `gender` y `legs` del animal en el que se llama.',
    'Then call `description` method': 'Luego llama al método `description`',
    'Add the parameters `gender` and `legs` inside the class': 'Agrega los parámetros `gender` y `legs` dentro de la clase',
    'Assign `4` as default value to the `legs` parameter.': 'Asigna `4` como valor predeterminado al parámetro `legs`.',
    'Create an instance of the `Animal` class called `dog`': 'Crea una instancia de la clase `Animal` llamada `dog`',
    'Can you make `Dog` a subclass of `Animal`?': '¿Puedes hacer que `Dog` sea una subclase de `Animal`?',
    '`legs` should be inside the `Animal` class while `breed` should be inside the `Dog` class': '`legs` debe estar dentro de la clase `Animal` mientras que `breed` debe estar dentro de la clase `Dog`',
    'The `Animal` class should have a method `speak()` that returns a string.': 'La clase `Animal` debe tener un método `speak()` que devuelve una cadena.',
    'The `Dog` class should have a method `speak()` that returns a different string.': 'La clase `Dog` debe tener un método `speak()` que devuelve una cadena diferente.',
    'The `speak()` method should return `Bau Bau!!`': 'El método `speak()` debe devolver `Bau Bau!!`',
    'The `Dog` class should have a method that returns the string `Bau Bau!!`': 'La clase `Dog` debe tener un método que devuelve la cadena `Bau Bau!!`',
    'Your program should print the string `Hello, JavaScript!` on the screen.': 'Tu programa debe imprimir la cadena `Hello, JavaScript!` en la pantalla.',
    'Do the same with the code below': 'Haz lo mismo con el código de abajo',
    'Create an `if` statement checking if the `time` is lower than `12`, then in the code block print the string `"It\'s morning"`': 'Crea una declaración `if` que verifique si `time` es menor que `12`, luego en el bloque de código imprime la cadena `"It\'s morning"`',
    'What is the ouput of the following code?': '¿Cuál es la salida del siguiente código?',
    'Can you order these lines into a functional code?': '¿Puedes ordenar estas líneas en un código funcional?',
    'Can you order these lines so that `"dog"` is displayed in the output?': '¿Puedes ordenar estas líneas para que se muestre `"dog"` en la salida?',
    'Can you order these lines so they form a proper __function__?': '¿Puedes ordenar estas líneas para que formen una __función__ adecuada?',
    'Can you find one way to create an array?': '¿Puedes encontrar una forma de crear un arreglo?',
    'Fill in the blanks with the `while` loop to repeat the block of code': 'Completa los espacios con el bucle `while` para repetir el bloque de código',
    'Complete the `for` loop in the following code': 'Completa el bucle `for` en el siguiente código',
    'Complete the `for` loop in the following code in order to execute the code block `3` times': 'Completa el bucle `for` en el siguiente código para ejecutar el bloque de código `3` veces',
    'Complete the `for` loop in the following code in order to repeat the code block **3** times': 'Completa el bucle `for` en el siguiente código para repetir el bloque de código **3** veces',
    'Use a `for` loop to print the numbers from `3` to `6` (both included)': 'Usa un bucle `for` para imprimir los números de `3` a `6` (ambos incluidos)',
    'Check if `num` is equal to `5`, printing the boolean result': 'Verifica si `num` es igual a `5`, imprimiendo el resultado booleano',
    'Check if `num` is **greater than** `7`, printing the boolean result': 'Verifica si `num` es **mayor que** `7`, imprimiendo el resultado booleano',
    'Check if `num` is **greater than or equal to** to `8`, printing the boolean result': 'Verifica si `num` es **mayor o igual que** `8`, imprimiendo el resultado booleano',
    'Check if `num` is **less than** `3`, printing the boolean result': 'Verifica si `num` es **menor que** `3`, imprimiendo el resultado booleano',
    'Check if `num` is **less than or equal to** to `8`, printing the boolean result': 'Verifica si `num` es **menor o igual que** `8`, imprimiendo el resultado booleano',
    'Check if `word` is **NOT** equal to `dog`, printing the boolean result': 'Verifica si `word` es **distinto de** `dog`, imprimiendo el resultado booleano',
    'Compare the `counter` variable with a number': 'Compara la variable `counter` con un número',
    'At the end of the loop, `counter` is equal to `9`': 'Al final del bucle, `counter` es igual a `9`',
    'Because dictionaries variables are mutable, they can be changed in many ways.': 'Debido a que las variables de diccionario son mutables, se pueden cambiar de muchas formas.',
    'Items can be removed from a dictionary with the \'delete\' keyword:': 'Los elementos se pueden eliminar de un diccionario con la palabra clave \'delete\':',
    'will remove the key `keyName` and its associated value from the dictionary.': 'eliminará la clave `keyName` y su valor asociado del diccionario.',
    'As for arrays, we can loop between dictionary elements using the `Object.entries()` method.': 'Al igual que con los arreglos, podemos iterar entre los elementos del diccionario usando el método `Object.entries()`.',
    'Accessing dictionary values by key is just like accessing array values by index:': 'Acceder a los valores del diccionario por clave es igual que acceder a los valores del arreglo por índice:',
    'Use the `indexOf()` method to print the index of `"dog"`.': 'Usa el método `indexOf()` para imprimir el índice de `"dog"`.',
    'Then use the `splice()` method to add `"bear"` as first item of the array': 'Luego usa el método `splice()` para agregar `"bear"` como primer elemento del arreglo',
    'We can also insert items into an array in a specific index, using the `splice()` method:': 'También podemos insertar elementos en un arreglo en un índice específico, usando el método `splice()`:',
    'The code above prints the first index that contains the string `"Zac"`, `1` in this case.': 'El código anterior imprime el primer índice que contiene la cadena `"Zac"`, `1` en este caso.',
    'The code above inserts `"Ali"` at index `1`, which moves everything, after this index, down by 1.': 'El código anterior inserta `"Ali"` en el índice `1`, que mueve todo, después de este índice, hacia abajo por 1.',
    'The second value `0` means _deleteCount_, in this case, we don\'t delete any item in the array;': 'El segundo valor `0` significa _deleteCount_, en este caso, no eliminamos ningún elemento del arreglo;',
    'but if we had specified `1` the value `Zac` would have been removed from the array': 'pero si hubiéramos especificado `1`, el valor `Zac` habría sido eliminado del arreglo',
    'First, we create an array called `numbers`.': 'Primero, creamos un arreglo llamado `numbers`.',
    'Then, we take a subsection of the array and store it in the slice array.': 'Luego, tomamos una subsección del arreglo y la almacenamos en el arreglo slice.',
    'We do this by defining the indices we want to include after the name of the array: `numbers.slice(1, 3)`.': 'Hacemos esto definiendo los índices que queremos incluir después del nombre del arreglo: `numbers.slice(1, 3)`.',
    'Consider the following code:': 'Considera el siguiente código:',
    '// Grabs the first two items': '// Toma los primeros dos elementos',
    'listName.slice(0, 2);': 'listName.slice(0, 2);',
    '// Grabs the fourth through last items': '// Toma del cuarto al último elemento',
    'listName.slice(3);': 'listName.slice(3);',
    'If your array slice includes the very first or last item in an array, the index for that item doesn\'t have to be included': 'Si tu slice de arreglo incluye el primer o último elemento de un arreglo, el índice de ese elemento no tiene que estar incluido',
    'In fact, above we have, in order, a string, an integer and a boolean.': 'De hecho, arriba tenemos, en orden, una cadena, un entero y un booleano.',
    'But we can also have arrays with arrays as well!': '¡Pero también podemos tener arreglos con arreglos!',
    'Now you know the basics of JavaScript!': '¡Ahora conoces los conceptos básicos de JavaScript!',
    'Each property is separated by a comma.': 'Cada propiedad está separada por una coma.',
    'You can think of an object as a single data structure that contains data as well as functions;': 'Puedes pensar en un objeto como una única estructura de datos que contiene datos así como funciones;',
    'the functions of an object are called its methods.': 'las funciones de un objeto se llaman sus métodos.',
    'Call the `pop()` method to remove the last item from the list': 'Llama al método `pop()` para eliminar el último elemento de la lista',
    'Print a boolean checking if `num` is equal to `5`': 'Imprime un booleano verificando si `num` es igual a `5`',
    'Add a valid comment to the function': 'Agrega un comentario válido a la función',
    'Choose the correct variable for a user who has just logged out': 'Elige la variable correcta para un usuario que acaba de cerrar sesión',
    'Use the spread operator `...` to copy all properties from one object to another.': 'Usa el operador de propagación `...` para copiar todas las propiedades de un objeto a otro.',
    
    # Asserts
    '`y` must be equal to `2`.': '`y` debe ser igual a `2`.',
    'The function should return "Hello, World!".': 'La función debe devolver "Hello, World!".',
    
    # Common output phrases
    'Hello, World!': '¡Hola, mundo!',
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
    
    # Comments
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
    '// DO NOT EDIT FROM HERE': '// DO NOT EDIT FROM HERE',
    '// DO NOT EDIT UNTIL HERE': '// DO NOT EDIT UNTIL HERE',
    
    # Test messages
    'Test Case': 'Caso de prueba',
    'failed': 'falló',
    'Executed': 'Ejecutados',
    'tests, with': 'pruebas, con',
    'failures': 'fallos',
    
    # Challenge descriptions
    'Write a function that returns the string `"Hello, World!"`.': 'Escribe una función que devuelva la cadena `"Hello, World!"`.',
    '- If the number is a multiple of `3` the output should be `"Fizz"`': '- Si el número es múltiplo de `3` la salida debería ser `"Fizz"`',
    '- If the number given is a multiple of `5`, the output should be `"Buzz"`.': '- Si el número dado es múltiplo de `5`, la salida debería ser `"Buzz"`.',
    '- If the number given is a multiple of both `3` and `5`, the output should be `"FizzBuzz"`.': '- Si el número dado es múltiplo de ambos `3` y `5`, la salida debería ser `"FizzBuzz"`.',
    '- If the number is not a multiple of either `3` or `5`, the number should be output on its own as shown in the examples below.': '- Si el número no es múltiplo de `3` o `5`, el número debería salir por sí solo como se muestra en los ejemplos a continuación.',
    '- The output should always be a string even if it is not a multiple of `3` or `5`.': '- La salida siempre debe ser una cadena incluso si no es múltiplo de `3` o `5`.',
    'Examples:': 'Ejemplos:',
    '2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.': '2520 es el número más pequeño que se puede dividir por cada uno de los números del 1 al 10 sin ningún resto.',
    'A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.': 'Un número palíndromo se lee igual en ambas direcciones. El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.',
    'By considering the terms in the Fibonacci sequence whose values do not exceed `n`, find the sum of the even-valued terms.': 'Al considerar los términos de la secuencia de Fibonacci cuyos valores no exceden `n`, encuentra la suma de los términos pares.',
    'By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.': 'Al listar los primeros seis números primos: 2, 3, 5, 7, 11 y 13, podemos ver que el 6º primo es 13.',
    'A Pythagorean triplet is a set of three natural numbers, `a` < `b` < `c`, for which, <latex>a^2 + b^2 = c^2</latex>': 'Un triplete pitagórico es un conjunto de tres números naturales, `a` < `b` < `c`, para los cuales, <latex>a^2 + b^2 = c^2</latex>',
    'For example, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>': 'Por ejemplo, <latex>3^2 + 4^2 = 9 + 16 = 25 = 5^2</latex>',
    'There exists exactly one Pythagorean triplet for which `a` + `b` + `c` = 1000.': 'Existe exactamente un triplete pitagórico para el cual `a` + `b` + `c` = 1000.',
    'Find the product of `a`, `b` and `c`.': 'Encuentra el producto de `a`, `b` y `c`.',
    'The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.': 'La suma de los primos menores que 10 es 2 + 3 + 5 + 7 = 17.',
    'Find the sum of all the primes below two million.': 'Encuentra la suma de todos los primos menores de dos millones.',
    'The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.': 'Los cuatro dígitos adyacentes en el número de 1000 dígitos que tienen el mayor producto son 9 × 9 × 8 × 9 = 5832.',
    'Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.': 'Encuentra los trece dígitos adyacentes en el número de 1000 dígitos que tienen el mayor producto.',
    'What is the value of this product?': '¿Cuál es el valor de este producto?',
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
