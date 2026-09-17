Se requiere tomar decisiones cuando queremos ejecutar código solo si se cumple cierta condición.
Supongamos que queremos jugar afuera solo si el clima es agradable.
En programación, podemos guardar una variable booleana `nice_weather` y realizar la acción de jugar afuera `if` esta variable es `True`, como:
```python
nice_weather = True
if (nice_weather):
    # play outside
```

---

Continuemos con el ejemplo anterior.
```python
nice_weather = True
if (nice_weather):
    # play outside
```
Hemos visto que la instrucción `if` ejecuta el bloque de código solo si la condición es `True`.
Otra cosa importante a considerar está representada por los **dos puntos** `:` y la **indentación**, que indican el inicio de un bloque de código.
La indentación se refiere a los espacios al principio de una línea de código.
Mientras que en otros lenguajes de programación la indentación en el código es solo para la legibilidad, en Python la indentación es esencial.
Puedes usar tu número de espacios favorito (2, 4, 6, 8), teniendo en cuenta que el preferido es 4.
Aquí en la aplicación, sugerimos usar la tecla **TAB** para indentar tus líneas de código

---

Acabamos de ver cómo ejecutar un bloque de código si ocurre una condición, ahora veamos cómo ejecutar otro bloque de código si la primera condición falla.
Vamos a jugar afuera si el clima es agradable; de lo contrario, nos quedamos en casa.
En Python podemos usar la instrucción `else`, como:
```python
nice_weather = True
if (nice_weather):
    # play outside
else:
    # stay home
```

---

Supongamos que tenemos otra condición que verificar, como en este ejemplo:
```python
num = 3
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
else:
    print("do something else")
```
y la salida de este código es `the number is 3`.
Primero, comprobemos si el número es igual a 2, esto es falso.
Así que pasemos a la segunda instrucción y comprobemos si `num` es igual a 3, siendo verdadero ejecutamos el siguiente bloque de código imprimiendo `the number is 3`

---

Podemos agregar tantas instrucciones `elif` como queramos, no hay límites
```python
num = 4
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
elif (num == 4):
    print("the number is 4")
elif (num == 5):
    print("the number is 5")
elif (num == 6):
    print("the number is 6")
```
y la salida de este código es `the number is 4`.

---

También podemos anidar una instrucción condicional (`if`, `elif` o `else`) dentro de otra instrucción condicional, para crear una estructura más compleja.
```python
num = 4
if (num < 3):
    print("the number is lower than 3")
else:
    if (num == 3):
        print("the number is 3")
    elif (num == 4):
        print("the number is 4")
    else:
        print("the number is greather than 4")
```
y la salida de este código es `the number is 4`.

---

Ahora que comprendemos cómo funcionan las declaraciones condicionales `if`, podemos crear nuestras propias.
Recordemos que la declaración `if` requiere una palabra clave `if` seguida de una condición y luego dos puntos `:`.

---

Cuando queremos ejecutar código solo si una condición es verdadera, usamos la declaración `if`.
El bloque de código dentro del `if` se ejecutará solo cuando la condición sea `True`.

---

Es importante recordar que el bloque de código dentro de un `if` solo se ejecuta si la condición es `True`.
Si la condición es `False`, el bloque se omite completamente y el programa continúa con el siguiente código.

---

La declaración `if` es una de las herramientas más útiles en programación.
Nos permite escribir código que responde a diferentes situaciones y condiciones.

---

Comprender cómo se ejecuta el código dentro de una declaración `if` es fundamental.
La indentación y la condición son los dos elementos clave que determinan si el código se ejecutará.

---

Cuando tenemos una condición `False`, el bloque de código en el `if` no se ejecutará.
Esto es uno de los conceptos más importantes para entender cómo funcionan las declaraciones condicionales.

---

Las declaraciones condicionales son herramientas que deciden qué código ejecutar basándose en si una condición es verdadera o falsa.
Estas declaraciones son el corazón de la programación de lógica condicional.

---

Una declaración `if` es la forma más simple de crear una rama condicional en nuestro código.
Nos permite ejecutar código específico solo cuando se cumple una determinada condición.

---

La sintaxis correcta de una declaración `if` en Python es muy importante.
Necesitamos la palabra clave `if`, la condición, y los dos puntos `:` al final.

---

Practicar la sintaxis correcta de las declaraciones `if` es esencial para escribir código Python correcto.
Cuando tenemos condiciones complejas, es importante escribirlas de forma clara y precisa.

---

Cuando trabajamos con variables booleanas, podemos usarlas directamente como condiciones en una declaración `if`.
No es necesario compararlas explícitamente con `True` o `False`.

---

El bloque de código dentro de una declaración `if` puede contener múltiples líneas de código.
Cada línea debe estar indentada correctamente para ser parte del bloque.

---

Las variables booleanas son simples pero poderosas en la programación condicional.
Pueden ser `True` o `False`, y esto determina el flujo de nuestro programa.

---

Cuando queremos NO ejecutar el bloque de código, debemos asegurarnos de que la condición sea `False`.
Esto es útil cuando queremos controlar explícitamente qué código se ejecuta y cuándo.

---

Un bloque de código es el conjunto de instrucciones que se ejecutan dentro de una estructura condicional.
La indentación es lo que define dónde comienza y dónde termina un bloque.

---

La indentación en Python es muy importante para definir la estructura del código.
Un código que está al mismo nivel de indentación que la declaración `if` no es parte del bloque condicional.

---

Los bloques de código pueden ser tan largos como sea necesario.
No hay límite en la cantidad de líneas que podemos incluir dentro de un bloque condicional.

---

La declaración `if` es la forma fundamental de crear decisiones en el código.
Nos permite controlar exactamente qué código se ejecuta en función de determinadas condiciones.

---

Cuando una condición es `False`, el bloque de código dentro del `if` se omite completamente.
El programa continúa ejecutándose desde la siguiente línea que no está dentro del `if`.

---

Cuando queremos que una línea de código se ejecute siempre, sin importar las condiciones anteriores, simplemente no la indentamos.
Esto la coloca fuera del bloque `if` y siempre se ejecutará.

---

El bloque de código dentro de una declaración `if` puede ejecutar múltiples instrucciones.
Todas las líneas indentadas después del `if` son parte del bloque condicional.

---

Asignar el valor correcto a una variable booleana es fundamental para controlar el flujo del programa.
`True` hace que se ejecute el bloque, mientras que `False` lo omite.

---

Para controlar cuándo se ejecuta un bloque de código, necesitamos establecer la condición correcta.
Una condición `False` asegura que el bloque se omita completamente.

---

La palabra clave `if` es la más importante en las estructuras condicionales de Python.
Es el punto de partida para cualquier decisión que queramos hacer en nuestro código.

---

Para evitar que se ejecute un bloque de código, usamos `False` como condición.
Esto detendrá completamente la ejecución de todas las líneas dentro del `if`.

---

Para ejecutar un bloque de código, necesitamos que la condición sea `True`.
`True` es uno de los dos valores booleanos posibles que podemos usar como condición.

---

La sintaxis de la declaración `if` requiere que escribamos todo correctamente.
La palabra clave `if`, la condición, y los dos puntos `:` son todos necesarios.

---

Las sentencias condicionales son las herramientas fundamentales para tomar decisiones en programación.
Nos permiten crear código que responde de manera diferente a situaciones distintas.

---

El operador `not` es una herramienta útil en Python que invierte el valor booleano.
Si una variable es `True`, el operador `not` la convierte en `False`, y viceversa.

---

Podemos usar variables booleanas en combinación con el operador `not` para crear lógica inversa.
Esto es especialmente útil cuando queremos verificar lo opuesto de una condición.

---

La condición en una declaración `if` debe escribirse correctamente para que Python entienda dónde comienza el bloque.
La posición correcta es siempre entre la palabra clave `if` y los dos puntos `:`.

---

Los bloques de código dentro de una declaración `if` pueden ser tan grandes como sea necesario.
Python no tiene límites en la cantidad de líneas que podemos indenta dentro de un `if`.

---

Llenar espacios en blanco es una excelente forma de practicar la sintaxis de las declaraciones `if`.
Cada espacio representa una parte importante de la estructura que debemos completar.

---

Un bloque de código en Python es una parte crucial de cualquier estructura condicional.
Determina qué instrucciones se ejecutan en función de si la condición es verdadera o falsa.

---

Los valores booleanos (`True` y `False`) son la base de toda lógica condicional en programación.
Son los únicos dos valores que necesitamos para controlar el flujo de nuestro código.
