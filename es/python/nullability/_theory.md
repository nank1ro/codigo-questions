A veces una variable aún **no tiene ningún valor** que guardar: un usuario que no ha iniciado sesión, una búsqueda que no encontró nada, una preferencia que nunca se eligió. Python representa esto con el valor especial `None`.
`None` es un valor como cualquier otro: puedes asignarlo, imprimirlo y pasarlo a funciones. Su tipo es `NoneType`, y hay exactamente **un** `None` en todo el programa, así que cada `None` que escribas se refiere al mismo objeto:
```python
winner = None
print(winner)                 # None
print(type(winner).__name__)  # NoneType
print(winner is None)         # True
```
`None` no es `0`, ni una cadena vacía, ni `False`: es un valor aparte que significa "aquí no hay nada".

---

Cada llamada a una función produce un valor, incluso cuando la función parece no devolver nada. Una función **sin** instrucción `return`, o con un `return` sin valor, devuelve `None`:
```python
def say_hello():
    print("hello")

result = say_hello()
print(result)  # None
```
Por esto al llamar `print(my_list.append(3))` se muestra `None`: `append` modifica la lista en su lugar y no devuelve nada.
Una función que solo realiza una acción (imprimir, guardar, modificar una lista) normalmente devuelve `None`, mientras que una función que calcula algo debe devolverlo explícitamente con `return`.

---

Para comprobar si una variable contiene `None`, usa `is` e `is not`, nunca `==`:
```python
if user is None:
    print("nobody logged in")
if user is not None:
    print("welcome")
```
`==` pregunta "¿son estos valores *iguales*?", y cualquier clase puede responder a esa pregunta a su manera definiendo el método `__eq__`. `is` pregunta "¿son estos el *mismo objeto*?", y nada puede cambiar esa respuesta.
Como solo hay un `None`, `is None` siempre es correcto y algo más rápido, mientras que `== None` puede dar una respuesta sorprendente con objetos que tengan un `__eq__` personalizado.

---

`None` cuenta como **falso** en una condición, así que `if not value:` es `True` cuando `value` es `None`. Es tentador usarlo como comprobación de `None`, pero la misma prueba también es `True` para `0`, `""`, `[]` y cualquier otro valor vacío:
```python
count = 0
if not count:
    print("missing?")   # printed, but 0 is a real value!
```
Cuando "sin valor" y "valor vacío" deben tratarse de forma distinta, comprueba primero `is None` y después la veracidad:
```python
if count is None:
    print("no count yet")
elif not count:
    print("count is zero")
```
Usa `if not value:` solo cuando de verdad quieras tratar `None` y los valores vacíos de la misma manera.

---

Un parámetro puede tener un **valor por defecto**, que se usa cuando quien llama omite el argumento. `None` es el valor por defecto habitual para "no proporcionado":
```python
def greet(name=None):
    if name is None:
        name = "stranger"
    print("Hello, " + name)

greet()       # Hello, stranger
greet("Ada")  # Hello, Ada
```
Esto importa con listas y diccionarios. Un valor por defecto se evalúa **una sola vez**, cuando se define la función, así que `def add(item, items=[])` comparte la misma lista en cada llamada que omita `items`, y los elementos se acumulan. La solución es usar `None` por defecto y crear una lista nueva dentro de la función:
```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

Leer una clave inexistente de un diccionario con `[]` lanza un `KeyError`. El método `get` es la alternativa segura: devuelve el valor cuando la clave existe y `None` cuando no:
```python
ages = {"Ada": 36}
print(ages.get("Ada"))    # 36
print(ages.get("Grace"))  # None
```
`get` acepta un segundo argumento, el valor a devolver **en lugar de** `None` cuando la clave no existe:
```python
print(ages.get("Grace", 0))  # 0
```
Esta es la forma más común en que `None` aparece en el código del día a día: una búsqueda que no encontró nada.

---

Una función que devuelve un número **o** `None` debería indicarlo en su firma. Un **type hint** es una anotación que documenta el tipo esperado: `name: str` para un parámetro y `-> int` para el valor de retorno. Python no obliga a cumplir las anotaciones, pero los editores y los lectores dependen de ellas:
```python
def parse_age(text: str) -> int | None:
    if text.isdigit():
        return int(text)
    return None
```
`int | None` se lee "un `int` o `None`". La forma antigua `Optional[int]` del módulo `typing` significa exactamente lo mismo, y todavía te la encontrarás en código existente.
Cada vez que veas `| None` en una firma, recuerda comprobar el resultado antes de usarlo.

---

Las funciones que pueden recibir `None` suelen empezar con una **guarda**: un `if` que retorna antes de tiempo cuando no hay nada que procesar. El resto de la función puede entonces asumir que el valor está presente, sin anidar todo dentro de un `else`:
```python
def shout(text):
    if text is None:
        return None
    return text.upper() + "!"
```
Las guardas van primero, en el orden en que deben hacerse las comprobaciones: no puedes llamar a `text.split()` antes de saber que `text` no es `None`.

---

El operador `or` no devuelve `True` o `False`: devuelve su operando **izquierdo** cuando este es verdadero, y su operando **derecho** en caso contrario. Esto da una forma de una sola línea para proporcionar un valor de respaldo:
```python
name = None
print(name or "anonymous")  # anonymous
name = "Ada"
print(name or "anonymous")  # Ada
```
La trampa es que `or` mira la veracidad, no `None`: `0`, `""` y `[]` también se reemplazan por el respaldo. Usa `x or fallback` solo cuando todos los valores vacíos deban convertirse también en el respaldo.

---

Cuando `0` o `""` deben conservarse y solo `None` debe reemplazarse, el respaldo necesita una comprobación explícita con `is None`. La forma compacta es la **expresión condicional**, `a if condition else b`, que se evalúa como `a` cuando la condición es verdadera y como `b` en caso contrario:
```python
timeout = 0
seconds = timeout if timeout is not None else 30
print(seconds)  # 0, not 30
```

---

Una lista puede contener `None` junto a valores reales, por ejemplo lecturas que fallaron o respuestas que se omitieron. La mayoría de las operaciones no lo aceptan: `sum([8, None])` lanza un `TypeError`.
Filtra los valores `None` con una list comprehension cuya condición sea `is not None`:
```python
readings = [3, None, 5]
valid = [r for r in readings if r is not None]
print(valid)  # [3, 5]
```
Usar `if r` en su lugar también descartaría cada `0`, así que sé explícito cuando cero es una lectura válida.

---

Una búsqueda seguida de una comprobación de `None` normalmente necesita dos líneas: una para guardar el resultado y otra para probarlo. El operador de **expresión de asignación** `:=`, apodado el *walrus*, asigna un valor **dentro** de una expresión, así que ambos pasos caben en el `if`:
```python
ages = {"Ada": 36}
if (age := ages.get("Ada")) is not None:
    print(age + 1)  # 37
```
Los paréntesis son obligatorios: sin ellos, `:=` intentaría asignar toda la comparación. Después del `if`, `age` sigue disponible como cualquier otra variable.

---

No todo "no encontrado" se notifica con `None`. Algunas funciones antiguas devuelven en su lugar un valor **centinela**, un valor normal al que se le da un significado especial. El método de cadenas `find` devuelve el índice de una subcadena, o `-1` cuando está ausente:
```python
print("banana".find("n"))  # 2
print("banana".find("x"))  # -1
```
La función `re.match(pattern, text)` del módulo `re` comprueba si `text` empieza con `pattern`, y devuelve un objeto de coincidencia, o `None` cuando no coincide.
`None` es la convención más segura: `-1` es un índice válido, así que `text[text.find("x")]` devuelve silenciosamente el último carácter en lugar de fallar, mientras que usar `None` como índice lanza un error de inmediato.

---

`None` no puede ordenarse: `None < 1` lanza un `TypeError`, porque Python no tiene idea de si "nada" es más pequeño o más grande que un número.
Esto importa cuando se usa `None` como valor inicial de una búsqueda, como "el mejor valor visto hasta ahora, si lo hay". Cada comparación debe protegerse con una comprobación `is None` colocada **primero**, de modo que `or` cortocircuite y la comparación se omita cuando todavía no hay nada que comparar:
```python
if best is None or value > best:
    best = value
```
Escrito al revés, `value > best or best is None` compararía con `None` en la primera iteración y fallaría.
