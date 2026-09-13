Una **expresión regular** (regex) es un pequeño lenguaje de patrones que describe texto. Python lo proporciona en el módulo estándar `re`:
```python
import re
```

`re.search(pattern, text)` busca el patrón en cualquier parte del texto. Devuelve un **objeto de coincidencia** (match object) cuando encuentra algo, y `None` cuando no. `match.group()` devuelve el fragmento de texto que coincidió:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
```

Dos partes del patrón hacen el trabajo aquí. `\d` significa *cualquier dígito*, y `+` significa *uno o más del elemento anterior*, así que `\d+` se lee como "uno o más dígitos". Otras abreviaturas útiles son `\w` (una letra, dígito o guion bajo) y `\s` (un espacio, tabulación o salto de línea).

Los patrones se escriben como **cadenas crudas** (raw strings), con una `r` antes de las comillas. En una cadena normal de Python la barra invertida inicia una secuencia de escape, así que `"\d"` es una advertencia esperando ocurrir y `"\n"` se convertiría en un salto de línea real en lugar de los dos caracteres que el motor de regex espera. El prefijo `r` convierte la barra invertida de nuevo en un carácter ordinario, así que `r"\d"` es exactamente lo que recibe el motor. Usa siempre `r"..."` para los patrones.

---

`re.search` escanea todo el texto, pero `re.match` solo prueba el patrón al **mismo principio**:
```python
import re

print(re.search(r"\d+", "order 42"))  # <re.Match object; span=(6, 8), match='42'>
print(re.match(r"\d+", "order 42"))   # None
print(re.match(r"\d+", "42 orders"))  # <re.Match object; span=(0, 2), match='42'>
```

Ambas devuelven `None` cuando nada coincide, y un objeto de coincidencia siempre es verdadero, así que la forma habitual de preguntar "¿coincidió?" es un simple `if`:
```python
if re.search(r"\d", text):
    print("there is a digit")
```
Cuando se necesita un `True` o un `False` real, compara con `is not None` o envuelve la llamada en `bool(...)`.

---

Hay un tercer punto de entrada, `re.fullmatch`, que tiene éxito solo cuando el patrón cubre **todo** el texto, desde el primer carácter hasta el último. Es la herramienta adecuada para la validación:
```python
import re

print(bool(re.fullmatch(r"\d+", "2026")))    # True
print(bool(re.fullmatch(r"\d+", "2026!")))   # False
```

Así que las tres funciones difieren solo en dónde puede situarse el patrón: `re.match` al principio del texto, `re.search` en cualquier parte del texto y `re.fullmatch` sobre la totalidad del texto.

---

Un objeto de coincidencia lleva más que el texto coincidente. Además de `.group()` ofrece la posición de la coincidencia dentro de la cadena original:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
print(match.start())  # 6
print(match.end())    # 8
print(match.span())   # (6, 8)
```
`.start()` es el índice del primer carácter coincidente, `.end()` es el índice justo después del último, y `.span()` devuelve ambos como una tupla. Eso significa que `text[match.start():match.end()]` siempre es igual a `match.group()`.

Como `re.search` puede devolver `None`, leer `.group()` directamente provoca un `AttributeError` cuando nada coincidió; comprueba primero el resultado.

---

Los paréntesis redondos dentro de un patrón crean un **grupo de captura**: una parte de la coincidencia que puede leerse por separado. Los grupos se numeran de izquierda a derecha, empezando por `1`:
```python
import re

match = re.search(r"(\w+)@(\w+)", "write to ada@example today")
print(match.group())   # ada@example
print(match.group(1))  # ada
print(match.group(2))  # example
print(match.groups())  # ('ada', 'example')
```
`match.group(0)` es la coincidencia completa, exactamente como `match.group()`, y `match.groups()` devuelve todos los grupos como una tupla. Pedir un número de grupo que no existe provoca un `IndexError`.

---

Contar paréntesis para encontrar el grupo `3` se vuelve tedioso rápidamente. A un grupo se le puede dar un nombre con `(?P<name>...)` y luego leerlo con `match.group("name")`:
```python
import re

match = re.search(r"(?P<hour>\d\d):(?P<minute>\d\d)", "starts at 09:30")
print(match.group("hour"))    # 09
print(match.group("minute"))  # 30
print(match.groupdict())      # {'hour': '09', 'minute': '30'}
```
`match.groupdict()` devuelve todos los grupos con nombre como un diccionario. Los grupos con nombre conservan también su número, así que `match.group(1)` sigue funcionando.

El ejemplo usa además un **cuantificador** con llaves: `\d{2}` significa exactamente dos dígitos, `\d{2,4}` significa entre dos y cuatro, y `\d{2,}` significa dos o más. Son la versión precisa de `+` (uno o más), `*` (cero o más) y `?` (cero o uno).

---

Los corchetes definen una **clase de caracteres**: un conjunto de caracteres, cualquiera de los cuales se acepta en esa posición. `[aeiou]` coincide con una vocal, `[0-9]` con un dígito y `[a-z]` con una letra minúscula. Un `^` justo después del corchete de apertura invierte el significado, así que `[^0-9]` coincide con cualquier cosa que *no* sea un dígito.

Fuera de una clase, `^` y `$` son **anclas**: `^` ata el patrón al principio del texto y `$` al final. Con `re.fullmatch` las anclas están implícitas, por eso la validación se lee mejor con él:
```python
import re

print(bool(re.fullmatch(r"[a-z]{3,8}", "ada")))  # True
print(bool(re.fullmatch(r"[a-z]{3,8}", "Ada")))  # False
```

---

`re.search` se detiene en la primera coincidencia. `re.findall(pattern, text)` recoge en cambio **todas** las coincidencias y las devuelve como una lista de cadenas:
```python
import re

print(re.findall(r"\d+", "a1 bb22 ccc333"))  # ['1', '22', '333']
print(re.findall(r"\d+", "no digits"))       # []
```
La lista está vacía cuando nada coincide, así que no hay ningún `None` que comprobar: se puede recorrer en un bucle o medir con `len(...)` directamente. Ten en cuenta que `findall` devuelve cadenas simples, no objetos de coincidencia, por lo que las posiciones no están disponibles.

---

Cuando se necesitan la posición o los grupos de cada coincidencia, `re.finditer(pattern, text)` es la llamada adecuada: recorre el texto y produce un **objeto de coincidencia** por cada coincidencia, de una en una:
```python
import re

for match in re.finditer(r"\d+", "a1 bb22"):
    print(match.group(), match.start())
# 1 1
# 22 5
```
`finditer` produce un iterador, no una lista, así que puede usarse en un bucle `for` o en una comprensión. Donde `findall` da solo el texto, `finditer` da todo lo que un objeto de coincidencia sabe.

---

`findall` cambia de comportamiento cuando el patrón contiene grupos de captura. Con exactamente un grupo devuelve el contenido de ese grupo en lugar de la coincidencia completa, y con dos o más devuelve una tupla de grupos por cada coincidencia:
```python
import re

print(re.findall(r"\d+-\d+", "10-20 30-40"))    # ['10-20', '30-40']
print(re.findall(r"(\d+)-\d+", "10-20 30-40"))  # ['10', '30']
```
Esto vale la pena recordarlo: añadir paréntesis a un patrón solo para agrupar cambia silenciosamente lo que `findall` devuelve. `re.finditer` nunca se comporta así, porque un objeto de coincidencia siempre conserva tanto la coincidencia completa como los grupos.

---

`re.sub(pattern, replacement, text)` devuelve una nueva cadena donde cada coincidencia ha sido reemplazada. Las cadenas son inmutables, así que el texto original queda intacto:
```python
import re

print(re.sub(r"\d", "#", "call 555 now"))     # call ### now
print(re.sub(r"\s+", " ", "too    many gaps"))  # too many gaps
```

El reemplazo puede referirse a los grupos de captura con `\1`, `\2`, ... (o `\g<name>` para un grupo con nombre), lo que hace de reordenar texto una tarea de una sola línea. El reemplazo también es una cadena cruda, por la misma razón de la barra invertida:
```python
import re

print(re.sub(r"(\w+), (\w+)", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
```
Un argumento `count` limita cuántas coincidencias se reemplazan: `re.sub(r"\d", "#", "1 2 3", count=1)` da `# 2 3`.

---

El reemplazo dado a `re.sub` también puede ser una **función**. Se llama una vez por cada coincidencia, recibe el objeto de coincidencia y debe devolver la cadena que se pondrá en su lugar. Así un reemplazo puede depender de lo que se encontró:
```python
import re

def shout(match):
    return match.group().upper()

print(re.sub(r"[a-z]+", shout, "one two"))  # ONE TWO
```
La función se pasa por nombre, sin paréntesis: escribir `shout(match)` la llamaría inmediatamente en lugar de entregarla a `re.sub`.

---

`str.split` solo puede cortar por un separador fijo. `re.split(pattern, text)` corta por cualquier cosa que el patrón describa, que es lo que suele necesitar una entrada desordenada:
```python
import re

print("a, b;c".split(","))            # ['a', ' b;c']
print(re.split(r"[,;]", "a, b;c"))    # ['a', ' b', 'c']
print(re.split(r"[,;\s]+", "a, b;c")) # ['a', 'b', 'c']
```
Escribir el separador como `[,;\s]+` hace que toda una secuencia de comas, puntos y comas y espacios cuente como un solo corte, en lugar de dejar cadenas vacías entre ellas.

Un argumento `maxsplit` se detiene tras un número dado de cortes, dejando el resto del texto en el último elemento: `re.split(r"\s+", "a b c", maxsplit=1)` da `['a', 'b c']`.

---

Cada llamada a `re.search` o `re.findall` tiene que buscar primero la cadena del patrón en una caché interna. `re.compile(pattern)` se salta esa búsqueda y devuelve un **objeto de patrón** que lleva los mismos métodos:
```python
import re

word_re = re.compile(r"[a-z]+")
print(word_re.search("ab 12").group())  # ab
print(word_re.findall("cd ef"))         # ['cd', 'ef']
print(word_re.sub("*", "ab cd"))        # * *
```
El texto es el único argumento que queda, porque el patrón ya está horneado en el objeto. Compilar compensa cuando el mismo patrón se usa muchas veces, por ejemplo dentro de un bucle, y además le da al patrón un nombre que explica qué coincide.

---

Los **flags** cambian cómo se aplica un patrón. Todas las funciones de `re` los aceptan como un argumento `flags`, y `re.compile` los guarda en el objeto de patrón:
```python
import re

print(re.search(r"cat", "A Cat", flags=re.IGNORECASE).group())  # Cat
title_re = re.compile(r"^#.*", re.MULTILINE)
```
Los dos que se usan más a menudo son `re.IGNORECASE`, que hace que las letras coincidan en cualquiera de las dos formas (mayúscula o minúscula), y `re.MULTILINE`, que hace que `^` y `$` coincidan al principio y al final de cada línea en lugar de en la totalidad del texto. Varios flags se combinan con `|`, como en `re.IGNORECASE | re.MULTILINE`.

Un flag solo cambia las reglas de coincidencia: el texto devuelto es siempre el texto que realmente había, con su forma original.
