Una tarea muy común es construir una lista nueva a partir de una existente.
Con un bucle `for` y `append()` se necesitan varias líneas:
```python
nums = [1, 2, 3]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6]
```
Python ofrece una forma más corta para exactamente esta tarea: la **list comprehension**, que construye toda la lista en una sola expresión:
```python
doubled = [n * 2 for n in nums]
```
La sintaxis es `[expresión for elemento in iterable]`: la parte `for` recorre los elementos, y la expresión de la izquierda se evalúa para cada uno.
El resultado es una lista completamente nueva, exactamente igual a la construida con el bucle.

---

La expresión de la izquierda puede ser cualquier cosa que produzca un valor: un cálculo, una llamada a función, una llamada a método.
La variable del bucle puede tener el nombre que quieras, y existe solo dentro de los corchetes:
```python
prices = [10, 20]
with_tax = [price * 1.2 for price in prices]
print(with_tax)  # [12.0, 24.0]
```

---

Una comprehension también puede **filtrar** los elementos.
Agrega una condición `if` después de la parte `for`: solo los elementos para los que la condición es `True` terminan en la nueva lista:
```python
nums = [5, 12, 8, 20]
big = [n for n in nums if n > 10]
print(big)  # [12, 20]
```
Esto es lo mismo que un bucle con un `if` dentro, y reemplaza `filter()` con una lambda de una forma más legible.

---

La condición de filtro puede ser cualquier expresión que dé un booleano, incluidas llamadas a función como `len()`:
```python
words = ["a", "bee", "cat"]
short = [w for w in words if len(w) < 3]
print(short)  # ['a']
```

---

El iterable no tiene que ser una lista: funciona cualquier cosa sobre la que puedas iterar, y `range()` es un favorito.
Es la forma más rápida de construir una lista de números:
```python
squares = [n * n for n in range(4)]
print(squares)  # [0, 1, 4, 9]
```
Recuerda que `range(start, stop)` excluye `stop`.

---

Las comprehensions son excelentes para **transformar strings**.
Llama a un método de string en cada elemento, o construye un nuevo string con un f-string:
```python
names = ["ana", "bob"]
greetings = [f"Hi {name.capitalize()}" for name in names]
print(greetings)  # ['Hi Ana', 'Hi Bob']
```

---

Dentro de una comprehension puedes usar cualquier variable definida antes, por ejemplo como límite de un `range()`.

---

A veces no quieres descartar elementos, sino elegir **un valor diferente** para algunos de ellos.
Usa una expresión condicional `a if condición else b` como expresión, a la izquierda del `for`:
```python
nums = [3, -1, 4]
signs = ["+" if n > 0 else "-" for n in nums]
print(signs)  # ['+', '-', '+']
```
Ten en cuenta la posición: el `if-else` va **antes** del `for` y siempre produce un valor, mientras que el `if` de filtro va **después** del `for` y no tiene `else`.

---

Las dos condiciones pueden combinarse en la misma comprehension: un `if-else` para elegir el valor, y un `if` de filtro al final para omitir algunos elementos.
```python
nums = [1, 2, 3, 4]
result = ["big" if n > 2 else "small" for n in nums if n != 3]
print(result)  # ['small', 'small', 'big']
```

---

Las dos posiciones de `if` se confunden fácilmente, así que mantenlas separadas:
```python
values = [n if n > 0 else 0 for n in nums]  # if-else antes del for: elige un valor, else obligatorio
positives = [n for n in nums if n > 0]      # if después del for: filtra, else no permitido
```
Poner un `else` después del filtro `if` es un error de sintaxis.

---

Una comprehension puede tener **más de un `for`**.
Funcionan como bucles anidados: el primer `for` es el bucle externo, el segundo es el interno.
```python
pairs = [a + b for a in ["x", "y"] for b in ["1", "2"]]
print(pairs)  # ['x1', 'x2', 'y1', 'y2']
```

---

El `for` interno puede usar la variable del externo.
Esta es la forma clásica de **aplanar** una lista de listas en una sola lista:
```python
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```
La función `sum()` luego suma todos los números de una lista.

---

También puedes iterar sobre un **diccionario**.
Con `.items()` la parte `for` desempaqueta cada par en dos variables, una clave y un valor:
```python
ages = {"ana": 31, "bob": 25}
lines = [f"{name} is {age}" for name, age in ages.items()]
print(lines)  # ['ana is 31', 'bob is 25']
```

---

La misma idea funciona para diccionarios: una **dict comprehension** usa llaves y una expresión `key: value`:
```python
names = ["ana", "bob"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'ana': 3, 'bob': 3}
```

---

Las llaves **sin** la parte `key: value` dan una **set comprehension**.
Un set es una colección desordenada que conserva solo valores únicos, por lo que los duplicados desaparecen automáticamente:
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)  # {1, 2, 3}
```

---

**¿Cuándo deberías usar una comprehension?**
Es perfecta cuando el resultado es una lista (o un dict, o un set) y la lógica cabe en una línea legible: una transformación simple, un filtro opcional.
Si necesitas varias sentencias, más de dos `for` anidados, o la línea se vuelve difícil de leer, escribe en su lugar un bucle `for` simple: el código será más largo, pero más claro.
Una comprehension también reemplaza la mayoría de los usos de `map()` y `filter()` con lambdas:
```python
doubled = list(map(lambda n: n * 2, nums))
doubled = [n * 2 for n in nums]  # same result, easier to read
```
