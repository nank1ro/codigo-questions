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
Recordemos que la declaración `if` requiere una palabra clave `if` seguida de una condición entre paréntesis y luego dos puntos `:`.

---

Cuando queremos ejecutar código solo si una condición es verdadera, usamos la declaración `if`.
El bloque de código dentro del `if` se ejecutará solo cuando la condición sea `True`.

---

Es importante recordar que el bloque de código dentro de un `if` solo se ejecuta si la condición es `True`.
Si la condición es `False`, el bloque se omite completamente y el programa continúa con el siguiente código.

---

La declaración `if` es una de las herramientas más útiles en programación.
Nos permite escribir código que responde a diferentes situaciones y condiciones.
