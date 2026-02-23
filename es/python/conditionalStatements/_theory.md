Continuemos con el ejemplo anterior.
```python
buen_clima = True
if (buen_clima):
    # jugar afuera
```
Hemos visto que la sentencia `if` ejecuta el bloque de código solo si la condición es `True`.
Otra cosa importante a considerar está representada por los **dos puntos** `:` y la **sangría**, que indican el inicio de un bloque de código.
La sangría se refiere a los espacios al comienzo de una línea de código.
Donde en otros lenguajes de programación la sangría en el código es solo para legibilidad, la sangría en Python es esencial.
Puedes usar tu número favorito de espacios (2, 4, 6, 8), teniendo en cuenta que el preferido es 4.
Aquí en la aplicación, sugerimos usar la tecla **TAB** para sangrar tus líneas de código

---

Acabamos de ver cómo ejecutar un bloque de código si se cumple una condición, ahora veamos cómo ejecutar otro bloque de código si la primera condición falla.
Vamos a jugar afuera si el clima es agradable; de lo contrario, nos quedamos en casa.
En Python podemos usar la sentencia `else`, como:
```python
buen_clima = True
if (buen_clima):
    # jugar afuera
else:
    # quedarse en casa
```

---

Supongamos que tenemos otra condición para verificar, como en este ejemplo:
```python
numero = 3
if (numero == 2):
    print("el número es 2")
elif (numero == 3):
    print("el número es 3")
else:
    print("hacer otra cosa")
```
y la salida de este código es `el número es 3`.
Primero, verifiquemos si el número es igual a 2, esto es falso.
Así que pasemos a la segunda sentencia y verifiquemos si `numero` es igual a 3, siendo verdadero ejecutamos el siguiente bloque de código imprimiendo `el número es 3`

---

Podemos agregar tantas sentencias `elif` como queramos, no hay límites
```python
numero = 4
if (numero == 2):
    print("el número es 2")
elif (numero == 3):
    print("el número es 3")
elif (numero == 4):
    print("el número es 4")
elif (numero == 5):
    print("el número es 5")
elif (numero == 6):
    print("el número es 6")
```
y la salida de este código es `el número es 4`.

---

También podemos anidar una sentencia condicional (`if`, `elif` u `else`) dentro de otra sentencia condicional, para crear una estructura más compleja.
```python
numero = 4
if (numero < 3):
    print("el número es menor que 3")
else:
    if (numero == 3):
        print("el número es 3")
    elif (numero == 4):
        print("el número es 4")
    else:
        print("el número es mayor que 4")
```
y la salida de este código es `el número es 4`.

---

La toma de decisiones es necesaria cuando queremos ejecutar código solo si se cumple una determinada condición.
Supongamos que queremos jugar afuera solo si el clima es agradable.
En programación, podemos guardar una variable booleana `buen_clima` y realizar la acción de jugar afuera `if` esta variable es `True`, como:
```python
buen_clima = True
if (buen_clima):
    # jugar afuera
```
