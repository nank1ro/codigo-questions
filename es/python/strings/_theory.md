Una **cadena** (string) es un fragmento de texto: una secuencia de caracteres entre comillas.
Python acepta tanto comillas simples `'...'` como dobles `"..."`, y ambas funcionan exactamente igual:
```python
name = 'Ada'
language = "Python"
```
La elección importa cuando el propio texto contiene una comilla.
Un apóstrofo dentro de comillas simples terminaría la cadena demasiado pronto, así que envuelve ese texto en comillas dobles:
```python
print("It's sunny")  # It's sunny
```

---

La función incorporada `len()` devuelve la **longitud** de una cadena, es decir, cuántos caracteres contiene.
Los espacios y la puntuación también cuentan como caracteres:
```python
print(len("hello"))     # 5
print(len("hi there"))  # 8
print(len(""))          # 0
```

---

Cada carácter de una cadena tiene una posición llamada **índice**.
Los índices empiezan en `0`, no en `1`: el primer carácter está en el índice `0`, el segundo en el índice `1`, y así sucesivamente.
Escribe el índice entre corchetes después de la cadena para leer un solo carácter:
```python
word = "python"
print(word[0])  # p
print(word[1])  # y
print(word[5])  # n
```
Pedir un índice que no existe, como `word[6]`, provoca un `IndexError`.

---

Los índices también pueden ser **negativos**: cuentan desde el final de la cadena.
`-1` es el último carácter, `-2` el anterior a él, y así sucesivamente:
```python
word = "python"
print(word[-1])  # n
print(word[-2])  # o
```
Esto es útil porque no necesitas saber la longitud de la cadena para llegar a su final.

---

Un **slice** (corte) extrae una parte de una cadena.
Escribe `[start:end]` entre corchetes: el carácter en `start` se incluye, el que está en `end` se **excluye**:
```python
word = "python"
print(word[0:3])  # pyt
print(word[2:4])  # th
```
Puedes omitir `start` para cortar desde el principio, o `end` para cortar hasta el final:
```python
print(word[:2])  # py
print(word[2:])  # thon
```
Un slice nunca provoca un error: un `end` mayor que la longitud simplemente se detiene en el último carácter.

---

Ya sabes que `+` une dos cadenas (**concatenación**).
El operador `*` **repite** una cadena un número determinado de veces:
```python
print("ab" * 3)        # ababab
print("=" * 10)        # ==========
print("Hi" + "!" * 3)  # Hi!!!
```
La repetición es una forma rápida de dibujar separadores y patrones simples.

---

El operador `in` comprueba si una cadena **contiene** otra.
Devuelve `True` o `False`, así que encaja de forma natural dentro de un `if`:
```python
email = "ada@mail.com"
print("@" in email)      # True
print("xyz" in email)    # False
if " " in email:
    print("No spaces allowed")
```
`not in` hace la comprobación contraria.

---

Las cadenas vienen con muchos **métodos** incorporados: funciones que se llaman con un punto después de la cadena.
`upper()` devuelve el texto en mayúsculas, `lower()` en minúsculas:
```python
word = "Python"
print(word.upper())  # PYTHON
print(word.lower())  # python
print(word)          # Python
```
Fíjate en que los métodos **devuelven una cadena nueva**: la `word` original no cambia.
`lower()` se usa a menudo para comparar textos sin distinguir mayúsculas de minúsculas: `"Yes".lower() == "yes"`.

---

Las cadenas son **inmutables**: una vez creadas, sus caracteres no se pueden cambiar.
Asignar a un índice provoca un `TypeError`:
```python
word = "dog"
word[1] = "i"  # TypeError: 'str' object does not support item assignment
```
Para "cambiar" una cadena, construyes una nueva, por ejemplo con slices y concatenación, y la guardas en la variable:
```python
word = word[0] + "i" + word[2:]
print(word)  # dig
```

---

El texto escrito por los usuarios suele tener espacios adicionales alrededor.
El método `strip()` devuelve una copia de la cadena **sin espacios en blanco al principio ni al final** (espacios, tabulaciones y saltos de línea):
```python
name = "   Ada  "
print("[" + name.strip() + "]")  # [Ada]
```
Los espacios en medio del texto se mantienen.
`lstrip()` elimina solo el lado izquierdo y `rstrip()` solo el lado derecho.

---

`split()` divide una cadena en una **lista** de partes.
Sin argumentos, divide por espacios en blanco; con un argumento, divide por ese separador:
```python
print("a b  c".split())      # ['a', 'b', 'c']
print("2024-01-31".split("-"))  # ['2024', '01', '31']
```
`join()` hace lo contrario: une los elementos de una lista en una sola cadena.
Se llama sobre el **separador**, y la lista es el argumento:
```python
words = ["one", "two", "three"]
print(", ".join(words))  # one, two, three
print("".join(words))    # onetwothree
```

---

`replace(old, new)` devuelve una copia de la cadena en la que **todas** las apariciones de `old` se reemplazan por `new`:
```python
text = "a-b-c"
print(text.replace("-", "+"))  # a+b+c
```
Como las cadenas son inmutables, recuerda guardar el resultado si quieres conservarlo.

---

`find(sub)` devuelve el **índice** de la primera aparición de `sub`, o `-1` si no se encuentra:
```python
text = "hello world"
print(text.find("o"))  # 4
print(text.find("z"))  # -1
```
`count(sub)` devuelve **cuántas veces** aparece `sub`:
```python
print(text.count("o"))   # 2
print(text.count("ll"))  # 1
```

---

`startswith(prefix)` y `endswith(suffix)` devuelven `True` o `False` según cómo empieza o termina la cadena:
```python
url = "https://codigo.dev"
print(url.startswith("https"))  # True
print(url.endswith(".com"))     # False
```
Son la forma habitual de comprobar extensiones de archivo, protocolos o prefijos.

---

Algunos caracteres no se pueden escribir directamente dentro de una cadena.
Una **secuencia de escape** es una barra invertida `\` seguida de una letra o símbolo que representa un carácter especial:

- `\n` un salto de línea
- `\t` un tabulador
- `\"` una comilla doble dentro de una cadena con comillas dobles
- `\'` una comilla simple dentro de una cadena con comillas simples
- `\\` una barra invertida literal

```python
print("Line 1\nLine 2")
print("She said \"hi\"")
```
imprime:
```
Line 1
Line 2
She said "hi"
```
Cada secuencia de escape cuenta como **un** carácter, aunque escribas dos.

---

Una cadena que abarca **varias líneas** se puede escribir con **comillas triples** `"""..."""` (o `'''...'''`).
Cada salto de línea dentro de las comillas pasa a formar parte de la cadena, así que no necesitas `\n`:
```python
poem = """Roses are red,
Violets are blue"""
print(poem)
```
imprime:
```
Roses are red,
Violets are blue
```
Las cadenas con comillas triples también pueden contener comillas simples y dobles libremente.

---

Como cada método de cadena devuelve una cadena nueva, puedes **encadenar** métodos uno tras otro.
Cada llamada trabaja sobre el resultado de la anterior:
```python
text = "  Hello World  "
print(text.strip().lower())  # hello world
```
Un slice también acepta un tercer valor, el **paso** (step).
El paso `-1` recorre la cadena hacia atrás, el truco clásico para invertirla:
```python
print("abc"[::-1])  # cba
```

---

Un **slug** es una versión de un título apta para URLs: en minúsculas, sin espacios alrededor, y con las palabras separadas por guiones, como `hello-world`.
Construir uno es solo una cadena de los métodos que ya has aprendido: `strip()`, `lower()` y `replace()`.
