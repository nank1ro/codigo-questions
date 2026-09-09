En Python una función es un **valor**, igual que un número o una cadena. Puedes guardarla en una variable, meterla en una lista o pasarla a otra función. Solo los paréntesis la llaman: `shout` es la función en sí, `shout("hi")` es su resultado:
```python
def shout(text):
    return text.upper() + "!"

say = shout
print(say("hi"))  # HI!
```
Una función que recibe otra función como parámetro, o que retorna una, se llama **función de orden superior**. Dentro de ella, el parámetro se llama con paréntesis como cualquier otra función:
```python
def apply(func, value):
    return func(value)

print(apply(shout, "bye"))  # BYE!
print(apply(len, "bye"))    # 3
```

---

Pasar una función como argumento permite que quien llama decida **qué** hacer, mientras que la función de orden superior decide **cuántas veces** o **sobre qué**. El parámetro función puede llamarse tantas veces como sea necesario, y su resultado puede volver a pasársele:
```python
def repeat(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def add_one(n):
    return n + 1

print(repeat(add_one, 0, 3))  # 3
```
Cualquier callable sirve: una función `def`, una función integrada como `len` o una `lambda`.

---

La función integrada `map(func, iterable)` llama a `func` sobre cada elemento y produce los resultados, uno por cada elemento. Retorna un *map object* perezoso, así que envuélvelo en `list()` para ver los valores:
```python
numbers = [1, 2, 3]
print(list(map(lambda n: n * 10, numbers)))  # [10, 20, 30]
```
Se puede pasar cualquier callable, no solo una lambda: una función integrada como `len`, o un método tomado de su clase, como `str.upper`, que recibe la cadena como su primer argumento:
```python
names = ["ada", "linus"]
print(list(map(str.upper, names)))  # ['ADA', 'LINUS']
print(list(map(len, names)))        # [3, 5]
```

---

La función integrada `filter(func, iterable)` conserva solo los elementos para los que `func` retorna un valor verdadero. Como `map`, retorna un objeto perezoso que debe convertirse en lista:
```python
numbers = [4, -2, 7, 0]
print(list(filter(lambda n: n > 0, numbers)))  # [4, 7]
```
La función que se pasa a `filter` se llama **predicado**: toma un elemento y responde una pregunta de sí/no sobre él. Pasar `None` en lugar de una función conserva los elementos que son verdaderos por sí mismos, descartando `0`, `""` y `None`.

---

`sorted(iterable, key=func)` ordena los elementos según el valor que `func` retorna para cada uno de ellos, sin cambiar los elementos en sí. Añade `reverse=True` para obtener los mayores primero:
```python
words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                # ['fig', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'kiwi', 'fig']
```
El ordenamiento es **estable**: los elementos cuyas claves son iguales conservan su orden original. La función `key` se llama una vez por elemento y sus resultados solo se usan para comparar, así que la salida sigue conteniendo las palabras originales, no sus longitudes.

---

La función `key` puede elegir **cualquier parte** de un elemento. Para una lista de tuplas, `lambda s: s[1]` ordena por el segundo elemento de cada tupla; para una lista de diccionarios, `lambda d: d["age"]` ordena por un valor:
```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))  # [('c', 1), ('b', 2), ('a', 3)]
```
`min` y `max` aceptan el mismo parámetro `key`, así que `max(pairs, key=lambda p: p[1])` retorna `('a', 3)`: la tupla completa, no solo el número.

---

Una función también puede **retornar** una función. Define una función interna con `def` y retórnala sin llamarla:
```python
def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada
```
La función interna sigue usando `greeting` incluso después de que `make_greeter` haya terminado: **recuerda** las variables del ámbito donde fue creada. Tal función se llama un **closure**. Cada llamada a `make_greeter` crea un closure nuevo e independiente con su propio `greeting`.

---

Un closure puede leer las variables de la función que lo envuelve, pero asignar a una de ellas crea en su lugar una **nueva variable local**. Para actualizar la variable externa, declárala con `nonlocal` dentro de la función interna:
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```
`global` buscaría `count` a nivel de módulo, donde no existe. Con `nonlocal`, cada llamada a la función retornada actualiza el mismo `count`, así que el closure lleva estado entre llamadas, como un objeto diminuto.

---

`reduce(func, iterable, initial)` del módulo `functools` pliega una secuencia en un **único valor**. Llama a `func` con el resultado hasta el momento y el siguiente elemento, empezando por `initial`:
```python
from functools import reduce

total = reduce(lambda acc, n: acc + n, [1, 2, 3], 0)
print(total)  # 6
```
Los pasos son `0 + 1`, luego `1 + 2`, luego `3 + 3`. Cuando se omite `initial`, el primer elemento se usa como valor inicial, pero entonces una secuencia vacía lanza un `TypeError`, así que da un valor inicial siempre que la secuencia pueda estar vacía.

---

`partial(func, *fixed)` de `functools` construye una nueva función con algunos argumentos **ya rellenados**. Llamar al resultado proporciona los restantes:
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```
Los argumentos posicionales dados a `partial` rellenan los primeros parámetros; los argumentos de palabra clave fijan un parámetro por su nombre y aún pueden sobrescribirse al llamar. Un partial es un callable normal, así que puede pasarse a `map`, `sorted` o cualquier otra función de orden superior.

---

`partial` resulta útil con funciones integradas que aceptan opciones. `int(text, base=16)` interpreta una cadena hexadecimal; fijar la base da un convertidor de un argumento que encaja con `map`:
```python
from functools import partial

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))                      # 255
print(list(map(hex_to_int, ["a", "10"])))    # [10, 16]
```
El objeto partial recuerda lo que envuelve: `hex_to_int.func` es `int`, y `hex_to_int.keywords` es `{'base': 16}`.

---

Un **decorador** es una función de orden superior que toma una función y retorna una nueva que la envuelve, normalmente para añadir comportamiento antes o después de la llamada original:
```python
def announce(func):
    def wrapper(name):
        print("calling " + func.__name__)
        return func(name)
    return wrapper
```
`func.__name__` es el nombre con el que se definió la función. Aplicar el decorador es solo una llamada: `greet = announce(greet)`. La sintaxis `@` colocada en la línea **anterior** a un `def` hace exactamente eso:
```python
@announce
def greet(name):
    return "Hello, " + name
```
El decorador debe definirse antes de usarse con `@`, porque el reemplazo ocurre tan pronto como se ejecuta el `def`.

---

Un decorador que solo acepta un argumento es de poca utilidad. Para envolver **cualquier** función, el wrapper recoge cada argumento posicional en `*args` y cada argumento de palabra clave en `**kwargs`, y los reenvía sin cambios:
```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name, punctuation="!"):
    return "hello " + name + punctuation

print(greet("ada"))                    # HELLO ADA!
print(greet("ada", punctuation="?"))   # HELLO ADA?
```
Dentro del wrapper, `args` es una tupla y `kwargs` un diccionario; el `*` y el `**` en la llamada los desempaquetan de nuevo en argumentos separados.

---

`any(iterable)` retorna `True` si **al menos un** elemento es verdadero, `all(iterable)` si **todos** los son. Combinan naturalmente con una **expresión generadora**: una list comprehension escrita sin los corchetes, que produce los valores de uno en uno en lugar de construir una lista:
```python
ages = [21, 34, 17]
print(any(age >= 18 for age in ages))  # True
print(all(age >= 18 for age in ages))  # False
```
Como los valores se generan perezosamente, `any` se detiene en el primer `True` y `all` en el primer `False`, sin evaluar el resto. `sum` también acepta una expresión generadora: `sum(1 for age in ages if age >= 18)` cuenta los adultos.
