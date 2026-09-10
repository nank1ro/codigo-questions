Los operadores de comparación comparan dos valores y devuelven un **booleano**, `True` o `False`: `==` igual, `!=` distinto, `<` menor que, `>` mayor que, `<=` menor o igual, `>=` mayor o igual:
```python
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age < 18)   # False
print(age >= 18)  # True
```
El resultado se puede guardar en una variable o mostrar directamente. Un solo `=` es una asignación, no una comparación.

---

Los operadores de comparación no se limitan a los números. Las cadenas se comparan carácter a carácter usando sus puntos de código, así que `"apple" < "banana"` es `True` y, como toda letra mayúscula va antes que las minúsculas, `"Zoo" < "apple"` también es `True`. Las listas y las tuplas se comparan elemento a elemento de la misma forma:
```python
print("cat" < "dog")       # True
print([1, 2, 3] < [1, 3])  # True
print((1, 2) == (1, 2))    # True
```
Una comparación es una expresión, así que una función puede hacer `return a < b` directamente en lugar de envolverla en un `if`.

---

Las comparaciones se pueden **encadenar**: `1 < x < 10` comprueba que `x` sea mayor que `1` **y** menor que `10`, exactamente como `1 < x and x < 10`, pero `x` se evalúa una sola vez:
```python
x = 5
print(1 < x < 10)   # True
print(1 < x <= 5)   # True
print(10 < x < 20)  # False
```
Cualquier operador de comparación se puede encadenar y cada uno se aplica a sus dos vecinos: `a < b == c` significa `a < b and b == c`. Leer una cadena como un rango, `low < x < high`, es el uso más común.

---

Los operadores lógicos combinan booleanos. `and` es `True` solo cuando ambos lados son `True`, `or` cuando al menos uno lo es, y `not` invierte un único valor:
```python
age = 20
member = False
print(age >= 18 and member)  # False
print(age >= 18 or member)   # True
print(not member)            # True
```
Las comparaciones tienen mayor precedencia que los operadores lógicos, así que `age >= 18 and member` no necesita paréntesis. Los paréntesis son necesarios para agrupar un `or` dentro de un `and`: `a and (b or c)`.

---

Cuando `not`, `and` y `or` aparecen en una misma expresión, Python aplica primero `not`, luego `and` y luego `or`. Así que `a or b and c` significa `a or (b and c)`, y `not a == b` significa `not (a == b)`:
```python
x = 6
print(x == 6 or x < 10 and x > 100)  # True: x == 6 or (False)
print(not x == 6)                    # False
```
Cuando se busca una agrupación distinta, añade paréntesis; además hacen la expresión más fácil de leer.

---

Todo valor tiene un **valor de verdad**. `bool(value)` devuelve `False` para `0`, `0.0`, `None`, la cadena vacía `""` y los contenedores vacíos como `[]`, `{}` y `set()`; cualquier otro valor es verdadero, incluidos `"0"` y `[0]`:
```python
print(bool(0), bool(""), bool(None))   # False False False
print(bool(42), bool("0"), bool([0]))  # True True True
```
`if`, `while`, `and`, `or` y `not` usan esta regla, así que `if items:` comprueba que la lista no esté vacía y `not name` comprueba que la cadena esté vacía; no hace falta escribir `len(items) > 0` ni `name == ""`.

---

Como `if value:` ya aplica el valor de verdad, comparar con `== True` o `== False` es innecesario e incluso puede ser incorrecto: `2 == True` es `False`, y sin embargo `2` es verdadero. Comprueba el valor en sí:
```python
values = [0, 1, "", "a", None, [], [0]]
for value in values:
    if value:
        print(value)  # 1, a, [0]
```

---

`and` y `or` no siempre devuelven `True` o `False`: devuelven uno de sus **operandos**. `a and b` devuelve `a` si es falso, y si no `b`; `a or b` devuelve `a` si es verdadero, y si no `b`:
```python
print(0 and "x")       # 0
print(3 and "x")       # x
print("" or "none")    # none
print("hi" or "none")  # hi
```
El resultado es verdadero o falso exactamente cuando lo es toda la expresión, y por eso `if a and b:` sigue funcionando. Un uso habitual es un valor por defecto: `name = user_input or "guest"`.

---

Los operadores lógicos son de **cortocircuito**: `and` se detiene en cuanto un operando es falso y `or` en cuanto uno es verdadero, porque el resultado ya se conoce. Los operandos restantes nunca se evalúan, así que si son llamadas a funciones no se ejecutan:
```python
def check(n):
    print("checking", n)
    return n > 0

check(-1) and check(5)  # prints only "checking -1"
check(2) or check(-3)   # prints only "checking 2"
```

---

`==` compara **valores**; `is` compara la **identidad**, es decir, si ambos nombres se refieren exactamente al mismo objeto. Dos listas iguales construidas por separado son `==` pero no `is`:
```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # True False True
```
`is` está pensado para singletons como `None`, `True` y `False`: escribe `value is None` o `value is not None`, nunca `value == None`, porque una clase puede definir `==` para devolver cualquier cosa. Usar `is` con números o cadenas no es fiable y Python lo advierte.

---

La evaluación en cortocircuito es una forma segura de **proteger** una operación que fallaría con algunos valores. En `word is not None and len(word) < 4`, `len(word)` se ejecuta solo cuando `word` no es `None`, así que la llamada nunca lanza un error. La protección debe ir primero:
```python
def is_short(word):
    return word is not None and len(word) < 4

print(is_short(None))   # False
print(is_short("cat"))  # True
```
Ten en cuenta que `and` devuelve un operando: `word and len(word) < 4` da `None` para `None` y `""` para la cadena vacía, no `False`. Protege con una comparación real cuando se necesite un booleano.

---

El operador `in` comprueba la **pertenencia**: si un elemento está en una lista, tupla o conjunto, si una subcadena está en una cadena, o si una clave está en un diccionario. `not in` es su negación:
```python
fruits = ["apple", "pear"]
print("pear" in fruits)          # True
print("kiwi" not in fruits)      # True
print("ex" in "text")            # True
print("age" in {"name": "Ada"})  # False, only keys are checked
```
Ambos devuelven un booleano y se leen como en inglés, lo que los convierte en la forma preferida de comprobar la pertenencia en lugar de escribir un bucle.
