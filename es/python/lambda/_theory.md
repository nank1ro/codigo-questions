A veces necesitas una función diminuta una sola vez, por ejemplo para duplicar un número.
Escribir un bloque `def` completo para eso resulta pesado.
Python ofrece una forma más corta: la expresión **lambda**, una función _anónima_ escrita en una sola línea:
```python
lambda x: x * 2
```
La sintaxis es `lambda parámetros: expresión`.
Una lambda no tiene nombre, pero puedes guardarla en una variable y llamarla como cualquier otra función:
```python
double = lambda x: x * 2
print(double(4))  # 8
```

---

Observa que el cuerpo de la lambda no tiene la palabra clave `return`.
El cuerpo es una **expresión única**, y su valor se retorna automáticamente:
```python
square = lambda n: n * n
print(square(3))  # 9
```

---

Una lambda puede tomar **más de un parámetro**.
Sepáralos con comas, igual que en una función `def`:
```python
power = lambda base, exp: base ** exp
print(power(2, 3))  # 8
```

---

Debido a que el cuerpo debe ser una única expresión, una lambda **no puede contener sentencias**.
Ni `return`, ni bloques `if`, ni bucles, ni asignaciones:
```python
# SyntaxError
increment = lambda x: return x + 1
```
Si necesitas algo de eso, escribe en su lugar una función `def` normal.

---

Los parámetros de una lambda también admiten **valores por defecto**:
```python
greet = lambda name="World": f"Hello, {name}!"
print(greet())       # Hello, World!
print(greet("Ana"))  # Hello, Ana!
```

---

Ni siquiera tienes que guardar una lambda: puedes **llamarla inmediatamente**.
Envuelve la lambda entre paréntesis y luego añade los argumentos:
```python
print((lambda x: x + 1)(4))  # 5
```

---

Donde las lambdas realmente brillan es como **argumentos de otras funciones**.
`sorted()` acepta un parámetro `key`: una función que se llama sobre cada elemento, y su resultado decide el orden.
Una lambda es perfecta para esto:
```python
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana']
```

---

La lambda de `key` puede elegir cualquier parte de un elemento.
Para una lista de listas, `lambda p: p[1]` ordena por el segundo elemento de cada lista interna.

---

`map()` aplica una función a **cada elemento** de una lista.
Retorna un objeto especial _map_, así que envuélvelo en `list()` para ver los valores:
```python
nums = [1, 2, 3]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6]
```

---

`filter()` conserva solo los elementos para los que la función retorna `True`:
```python
nums = [5, 12, 8, 20]
big = list(filter(lambda n: n > 10, nums))
print(big)  # [12, 20]
```

---

Imprimir un objeto `map` directamente no muestra sus valores: obtienes algo como `<map object at 0x7f2b1c>`.
Solo `list()` (o un bucle) lo convierte en los valores que esperas.

---

Las lambdas no se limitan a las funciones integradas: **tus propias funciones** pueden tomar una función como parámetro y llamarla.
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 3))  # 30
```

---

`max()` y `min()` también aceptan una función `key`, igual que `sorted()`:
```python
words = ["hi", "hello", "hey"]
print(max(words, key=lambda w: len(w)))  # hello
```

---

**¿Cuándo deberías preferir `def`?**
Una lambda es ideal para una función corta y desechable pasada como argumento.
Si la lógica necesita un nombre, varias líneas, un docstring, o se reutiliza en muchos lugares, una función `def` es más clara.
Un último truco: `sorted()` también acepta `reverse=True` para obtener primero los valores más grandes:
```python
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]
```
