Cada valor en Python tiene un **tipo** que indica qué clase de dato es y qué puedes hacer con él.
Los tipos básicos integrados son:
- `int`, un número entero como `42` o `-3`
- `float`, un número con parte decimal como `3.5`
- `str`, un fragmento de texto como `"hello"`
- `bool`, uno de los dos valores `True` y `False`
- `NoneType`, el tipo del valor especial `None`, que significa "ningún valor"

La función integrada `type()` devuelve el tipo de un valor. Al imprimirla se muestra el nombre de la clase:
```python
print(type(42))     # <class 'int'>
print(type("hi"))   # <class 'str'>
```
Nunca escribirás `NoneType` tú mismo: `type(None)` lo devuelve, pero el nombre no es un integrado como los otros cuatro.

---

`type()` devuelve la clase de un valor, así que puedes compararla con un nombre de clase usando `is`:
```python
age = 30
print(type(age) is int)  # True
```
La mayoría de las veces, sin embargo, solo quieres saber **si** un valor es de un cierto tipo. Ese es el trabajo de `isinstance(value, cls)`, que devuelve `True` o `False`:
```python
print(isinstance(age, int))    # True
print(isinstance(age, str))    # False
```
El segundo argumento también puede ser una **tupla** de clases: el resultado es `True` si el valor pertenece a alguna de ellas:
```python
print(isinstance(2.5, (int, float)))  # True
```

---

Python es de **tipado dinámico**: el tipo pertenece al **valor**, no a la variable.
Una variable es solo un nombre unido a un valor, y puedes unirla a un valor de un tipo diferente en cualquier momento:
```python
x = 10
print(type(x))  # <class 'int'>
x = "ten"
print(type(x))  # <class 'str'>
```
No se necesita ninguna declaración ni conversión: el valor anterior simplemente se olvida.
Esto es cómodo, pero también significa que el tipo de una variable solo se conoce cuando el programa se ejecuta, así que mezclar tipos por error aparece como un error en tiempo de ejecución, no antes.

---

Ya conoces los operadores aritméticos. Lo que importa aquí es el **tipo del resultado**.
Combinar un `int` con un `float` da un `float`, incluso cuando la parte decimal es cero:
```python
print(3 + 0.5)   # 3.5
print(2 * 1.0)   # 2.0
```
La **división verdadera** `/` siempre devuelve un `float`, incluso cuando los números se dividen exactamente:
```python
print(10 / 5)    # 2.0
print(7 / 2)     # 3.5
```
La **división entera** `//` redondea el resultado hacia abajo al número entero más cercano (así `-7 // 2` es `-4`) y devuelve un `int` cuando ambos operandos son enteros. Junto con el resto `%` divide una cantidad en partes enteras:
```python
print(7 // 2)    # 3
print(7 % 2)     # 1
```

---

Los valores no cambian de tipo por sí solos: para convertir un valor a otro tipo llamas al nombre del tipo como una función. Esto se llama **conversión** (o *casting*):
```python
print(int("42"))      # 42
print(float("3.5"))   # 3.5
print(str(7))         # '7'
print(int(3.9))       # 3
```
`int()` y `float()` leen números escritos como texto, que es lo que obtienes de la entrada del usuario o de los archivos. `str()` convierte cualquier cosa en texto, de modo que puede unirse con `+` a otras cadenas.
Ten en cuenta que `int(3.9)` no redondea: descarta la parte decimal.

---

Una conversión puede fallar. `int("abc")` no puede producir un número, así que lanza un `ValueError` y el programa se detiene:
```python
int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
int("3.5")   # ValueError as well: "3.5" is not a whole number
```
Para mantener el programa en ejecución puedes capturar el error con `try` / `except`: el código del bloque `try` se ejecuta, y si lanza el error indicado, el bloque `except` se ejecuta en su lugar:
```python
try:
    number = int(text)
except ValueError:
    number = 0
```
Cuando la conversión tiene éxito, el bloque `except` se omite.

---

Cada valor puede interpretarse como un booleano. `bool()` convierte un valor a `True` o `False`, y la misma regla se aplica cuando un valor se usa directamente en un `if`.
Los valores que cuentan como **falsos** son los "vacíos":
- el número `0` (y `0.0`)
- la cadena vacía `""`
- colecciones vacías como `[]`, `{}`, `()` y `set()`
- `None`

Cualquier valor no vacío es **verdadero**, incluidos los números negativos y las cadenas que solo parecen vacías, como `"0"` o `" "`:
```python
print(bool(0))     # False
print(bool(-1))    # True
print(bool(""))    # False
print(bool("0"))   # True
```
Por esto `if name:` es una forma común de comprobar que una cadena no está vacía.

---

`bool` es una **subclase** de `int`: `True` se comporta como `1` y `False` como `0` dondequiera que se espera un número:
```python
print(True + 1)     # 2
print(True == 1)    # True
print(False * 10)   # 0
```
`sum()` suma los elementos de una lista, así que sumar una lista de booleanos **cuenta** cuántos son `True`:
```python
answers = [True, False, True]
print(sum(answers))  # 2
```
Debido a la relación de subclase, `isinstance(True, int)` devuelve `True`, mientras que `type(True)` sigue siendo `bool`.

---

`None` es un valor propio que significa "aquí no hay nada". Es lo que devuelve una función cuando no tiene instrucción `return`, y es un marcador de posición común para un valor que aún no se conoce.
Como solo hay un `None`, compruébalo con `is`, no con `==`:
```python
result = None
if result is None:
    print("no result yet")
```
Cada tipo tiene un atributo `__name__` con su nombre como cadena, lo que resulta útil para mensajes:
```python
print(type(3).__name__)     # int
print(type(None).__name__)  # NoneType
```

---

Imprimir un `float` muestra tantos dígitos como se necesiten para representarlo exactamente, lo que a menudo son demasiados:
```python
print(19.999 * 3)  # 59.997
print(10 / 3)      # 3.3333333333333335
```
Dentro de una f-string puedes añadir una **especificación de formato** después de dos puntos. `.2f` significa "número de punto fijo con 2 decimales":
```python
total = 10 / 3
print(f"{total:.2f}")   # 3.33
print(f"{total:.0f}")   # 3
```
El valor se redondea al número de decimales solicitado, y se añaden ceros cuando es necesario: `f"{2.5:.2f}"` da `2.50`.

---

El formato solo cambia cómo se muestra un número. Para obtener un **valor** redondeado usa la función integrada `round()`:
```python
print(round(3.14159, 2))  # 3.14
print(round(2.71828, 1))  # 2.7
```
Con un solo argumento `round()` redondea al número entero más cercano y devuelve un `int`; con un número de decimales devuelve un `float`:
```python
print(round(3.7))     # 4
print(round(3.7, 0))  # 4.0
```
Ten en cuenta que los valores exactamente a medio camino entre dos números se redondean al **par**: `round(2.5)` es `2` y `round(3.5)` es `4`.

---

Un `float` se almacena en binario con un número fijo de bits, así que la mayoría de los números decimales solo pueden **aproximarse**. El error es diminuto pero aparece en la aritmética:
```python
print(0.1 + 0.2)   # 0.30000000000000004
```
Por esta razón no debes comparar floats con igualdad exacta. Redondea ambos lados, o usa `math.isclose()`, que comprueba que dos números son iguales dentro de una tolerancia diminuta:
```python
import math
print(round(0.1 + 0.2, 2) == 0.3)  # True
print(math.isclose(0.1 + 0.2, 0.3))  # True
```
Los enteros no tienen este problema: `1 + 2 == 3` siempre es `True`.

---

A diferencia de muchos lenguajes, los enteros de Python **no tienen tamaño máximo**: un `int` crece para contener tantos dígitos como sean necesarios, así que los cálculos grandes siguen siendo exactos:
```python
print(3 ** 100)  # 515377520732011331036461129765621272702107522001
```
Un `float`, por otro lado, conserva solo unos 15 dígitos significativos, así que la misma potencia como float pierde precisión:
```python
print(3.0 ** 100)  # 5.153775207320113e+47
```
Como `str()` funciona con cualquier `int`, una forma rápida de contar los dígitos de un número es medir la longitud de su texto.

---

Puedes escribir el tipo esperado de una variable, parámetro o valor de retorno como un **type hint**: dos puntos después del nombre para variables y parámetros, una flecha `->` antes de los dos puntos para el valor de retorno:
```python
count: int = 3

def greet(name: str) -> str:
    return "Hi " + name
```
Los type hints son **documentación** para las personas y para herramientas como los editores: Python **no** los comprueba. Este código se ejecuta sin quejarse e imprime `hello`:
```python
count: int = "hello"
print(count)
```
Los type hints dejan claros los tipos previstos, pero el valor sigue decidiendo el tipo real.

---

Las conversiones pueden combinarse. `int("3.7")` falla, pero `float("3.7")` funciona, y `int()` de un `float` descarta la parte decimal:
```python
number = float("3.7")   # 3.7
print(int(number))      # 3
```
`bool()` sigue las reglas de veracidad: `bool("")` es `False`, y ten en cuenta que `bool("False")` es `True`, porque es una cadena no vacía.

---

El texto que viene de fuera siempre es una `str`, y depende de tu programa averiguar qué tipo contiene realmente.
Un enfoque común es probar primero la conversión más **estricta**, y recurrir a la siguiente cuando lanza un `ValueError`:
```python
try:
    value = int(text)
except ValueError:
    value = float(text)
```
Anidar un segundo `try` dentro del bloque `except` te permite recurrir una vez más, por ejemplo para conservar el texto tal cual.
