Un **set** es una colección de elementos **únicos**: el mismo valor puede aparecer solo una vez, sin importar cuántas veces lo escribas.
Un set también está **desordenado**: no hay un primer ni un último elemento, por lo que no puedes leer un elemento por índice.
Los sets son ideales cuando solo te importa *qué* valores están presentes, no cuántas veces ni en qué posición.
Creas un set escribiendo sus elementos entre llaves `{...}`:
```python
colors = {"red", "blue", "red"}
print(len(colors))  # 2
```
El `"red"` duplicado se descarta, por lo que `len()` cuenta solo los elementos distintos.

---

La función incorporada `set()` construye un set a partir de cualquier colección, por ejemplo una lista o una cadena.
Como un set conserva cada valor una sola vez, esta es la forma clásica de **eliminar duplicados**:
```python
nums = [1, 2, 2, 3]
unique = set(nums)
print(len(unique))  # 3
```
Para comprobar si un valor está presente usa el operador `in`, que devuelve `True` o `False`:
```python
print(2 in unique)  # True
print(9 in unique)  # False
```
Las comprobaciones de pertenencia en un set son muy rápidas, incluso con miles de elementos.

---

Hay una trampa al crear un **set vacío**.
Las llaves también son la sintaxis de los diccionarios, por lo que `{}` crea un **diccionario** vacío, no un set:
```python
empty = {}
print(type(empty))  # <class 'dict'>
```
Para obtener un set vacío debes llamar a `set()` sin argumentos:
```python
empty = set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
```

---

Los sets son **mutables**: puedes agregar y quitar elementos después de crearlos.
`add(value)` inserta un valor; agregar uno que ya está presente no cambia nada:
```python
letters = {"a", "b"}
letters.add("c")
letters.add("a")
print(len(letters))  # 3
```
Hay dos formas de quitar un elemento:
- `remove(value)` lo elimina, pero lanza un `KeyError` si el valor no está en el set
- `discard(value)` lo elimina si está presente y **no hace nada** en caso contrario, sin error
```python
letters.remove("a")
letters.discard("z")  # "z" no está, pero no hay error
letters.remove("z")   # KeyError: 'z'
```

---

`pop()` elimina **un elemento arbitrario** del set y lo devuelve.
Como un set no tiene orden, no puedes elegir qué elemento se elimina; llamar a `pop()` en un set vacío lanza un `KeyError`:
```python
tickets = {101, 102, 103}
picked = tickets.pop()
print(len(tickets))  # 2
```
`clear()` elimina **todos** los elementos, dejando un set vacío:
```python
tickets.clear()
print(len(tickets))  # 0
```

---

Puedes recorrer un set con `for`, exactamente igual que una lista:
```python
for color in {"red", "blue"}:
    print(color)
```
Como un set está desordenado, los elementos pueden salir en **cualquier orden**, y ese orden puede incluso cambiar entre ejecuciones.
Cuando necesites un orden predecible, pasa el set a `sorted()`, que devuelve una **lista** ordenada de sus elementos:
```python
for color in sorted({"red", "blue"}):
    print(color)  # blue, then red
```

---

La **unión** de dos sets es un nuevo set con los elementos de **ambos**, sin duplicados.
Usa el operador `|` o el método `union()`:
```python
a = {1, 2}
b = {2, 3}
print(a | b)        # {1, 2, 3}
print(a.union(b))   # {1, 2, 3}
```
Ni `a` ni `b` se modifican: las operaciones de sets siempre devuelven un set nuevo.

---

La **intersección** de dos sets contiene solo los elementos presentes en **ambos**.
Usa el operador `&` o el método `intersection()`:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)               # {2, 3}
print(a.intersection(b))   # {2, 3}
```
Si los sets no tienen nada en común, el resultado es un set vacío.

---

La **diferencia** `a - b` contiene los elementos de `a` que **no** están en `b`.
El orden importa: `a - b` y `b - a` suelen ser diferentes:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}
print(b - a)  # {4}
```
La **diferencia simétrica** `a ^ b` contiene los elementos que están en **exactamente uno** de los dos sets:
```python
print(a ^ b)  # {1, 4}
```
Las formas de método son `difference()` y `symmetric_difference()`.

---

Los operadores y los métodos no son perfectamente equivalentes.
Los operadores `|`, `&`, `-` y `^` funcionan solo cuando **ambos** operandos son sets.
Los métodos `union()`, `intersection()`, `difference()` y `symmetric_difference()` aceptan **cualquier iterable**, como una lista o una cadena:
```python
a = {1, 2}
print(a.union([2, 3]))  # {1, 2, 3}
print(a | [2, 3])       # TypeError: unsupported operand type(s) for |: 'set' and 'list'
```

---

Los sets también se pueden **comparar** entre sí.
`a.issubset(b)`, o `a <= b`, es `True` cuando cada elemento de `a` también está en `b`.
`a.issuperset(b)`, o `a >= b`, es `True` cuando `a` contiene cada elemento de `b`.
`a.isdisjoint(b)` es `True` cuando los dos sets no tienen **ningún** elemento en común:
```python
small = {1, 2}
big = {1, 2, 3}
print(small <= big)              # True
print(big.issuperset(small))     # True
print(small.isdisjoint({8, 9}))  # True
```

---

Un set solo puede contener elementos **hasheables**, es decir, valores que no pueden cambiar: números, cadenas, `True`/`False` y **tuplas**.
Intentar agregar una lista, un diccionario u otro set lanza un `TypeError`:
```python
points = set()
points.add((1, 2))  # ok, una tupla
points.add([1, 2])  # TypeError: unhashable type: 'list'
```
Los sets de tuplas son útiles para llevar el registro de pares únicos, como coordenadas o registros (nombre, edad):
```python
visits = [(1, 2), (1, 2), (3, 4)]
print(len(set(visits)))  # 2
```

---

Un **frozenset** es un set **inmutable**: una vez creado, no puedes agregar ni quitar elementos.
Créalo con `frozenset()` a partir de cualquier colección:
```python
days = frozenset(["sat", "sun"])
print("sat" in days)  # True
days.add("mon")       # AttributeError: 'frozenset' object has no attribute 'add'
```
Al imprimir un frozenset se muestra su tipo alrededor de los elementos, como `frozenset({'sat', 'sun'})`.
Como no puede cambiar, un frozenset es hasheable: a diferencia de un set normal, puede ser un elemento de otro set o una clave de diccionario.
Todas las operaciones de solo lectura (`in`, `len()`, `|`, `&`, `-`, `^`, comparaciones) funcionan como siempre.

---

Una **set comprehension** construye un set en una sola expresión, con la misma sintaxis que una list comprehension pero con llaves:
```python
nums = [1, 2, 2, 3]
squares = {n * n for n in nums}
print(squares)  # {1, 4, 9}
```
Un `if` opcional filtra los elementos, y los duplicados producidos por la expresión se descartan automáticamente:
```python
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

---

Las operaciones de sets también pueden modificar un set **en el sitio**, en lugar de devolver uno nuevo.
`update(iterable)` agrega cada elemento de cualquier colección, como `add()` pero para muchos valores a la vez:
```python
inventory = {"sword"}
inventory.update(["potion", "map"])
print(len(inventory))  # 3
```
Los operadores aumentados también funcionan en el sitio: `|=` agrega los elementos de otro set, `&=` conserva solo los comunes, `-=` quita los elementos de otro set:
```python
inventory -= {"map"}
print(sorted(inventory))  # ['potion', 'sword']
```

---

Dos sets son **iguales** cuando contienen los mismos elementos, sin importar el orden en que fueron escritos:
```python
print({1, 2, 3} == {3, 1, 2})  # True
```
Comparar la longitud de una colección con la longitud de su set es una forma rápida de detectar duplicados: si el set es **más pequeño**, algún valor apareció más de una vez:
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)) < len(emails))  # True
```
El método de lista `count(value)` indica cuántas veces aparece un valor, lo que ayuda a encontrar *cuáles* valores están duplicados.
