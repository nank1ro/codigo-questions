Una **excepción** es la forma que tiene Python de decir que una instrucción no puede llevarse a cabo. Dividir entre cero, convertir `"abc"` en un entero o leer una clave inexistente de un diccionario lanzan una. Cuando nadie la maneja, el programa se detiene justo ahí e imprime un **traceback**:
```python
print(10 / 0)
```
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```
El traceback enumera las líneas que se estaban ejecutando, y la última línea da el **tipo de excepción** (`ZeroDivisionError`) y su mensaje (`division by zero`). Esa última línea es la primera que hay que leer.

Para mantener vivo el programa, coloca la instrucción arriesgada en un bloque `try` y describe la recuperación en un bloque `except`:
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```
Python ejecuta el bloque `try`; si se lanza la excepción nombrada, salta directamente al bloque `except` correspondiente y continúa con el resto del programa.

---

El bloque `try` se detiene en la **primera** instrucción que lanza; las líneas posteriores se omiten y el control pasa al bloque `except`. Nada dentro del bloque `try` se deshace, así que mantenlo tan corto como sea posible:
```python
def half(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "undefined"

print(half(2))  # 5.0
print(half(0))  # undefined
```
Un `return` dentro de `except` funciona como cualquier otro `return`, lo que hace de `try`/`except` una forma natural de devolver un valor de respaldo en lugar de fallar.

---

Una excepción que ningún bloque `except` coincide sigue viajando hacia afuera: fuera de la línea, fuera de la función que la ejecutó, fuera de su llamador, y así sucesivamente. Si nada la captura antes de la parte superior del programa, Python imprime el traceback y el proceso termina con un estado de salida distinto de cero. Las líneas posteriores a la instrucción que falló nunca se ejecutan.

---

Una cláusula `except` solo captura el tipo que nombra, y sus subclases. Ese es el punto: todo lo demás sigue viajando hacia afuera, de modo que un error que no esperabas sigue apareciendo como un traceback en lugar de ser tragado.

`int(text)` lanza **`ValueError`** cuando el texto no describe un número entero, así que ese es el tipo a nombrar al leer la entrada del usuario:
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("12"))    # 12
print(to_int("oops"))  # 0
```
Nombrar `ValueError` aquí es una decisión, no una formalidad: `int(None)` lanza `TypeError`, que esta función deliberadamente **no** captura, porque pasar `None` es un error de programación y debería verse.

---

Elegir el tipo más estrecho que cubre el fallo que esperas es lo que hace confiable el manejo de errores. Una función que lee texto debería recuperarse de un texto inválido (`ValueError`) pero no debe ocultar que se llamó con el tipo de argumento equivocado (`TypeError`) — ese error le corresponde al llamador, así que déjalo pasar.

---

Un bloque `try` puede ir seguido de **varias** cláusulas `except`, cada una manejando un fallo diferente con una recuperación diferente. Python compara la excepción lanzada contra ellas de arriba a abajo y ejecuta la **primera** que coincide; las demás se omiten:
```python
try:
    value = 100 / int(text)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
Como la primera coincidencia gana, el orden importa cuando los tipos están relacionados: una cláusula para un tipo general colocada encima de una cláusula para uno más específico ganaría siempre, dejando la cláusula específica inalcanzable.

---

Cuando varios fallos merecen la **misma** recuperación, listarlos como una tupla en una sola cláusula es más corto que repetir el bloque:
```python
try:
    value = int(text) / divisor
except (ValueError, ZeroDivisionError):
    value = 0
```
Los paréntesis son obligatorios: `except ValueError, ZeroDivisionError:` es un error de sintaxis en Python 3. Una tupla sigue siendo una lista explícita de tipos.

---

`except:` sin ningún tipo detrás es un **except desnudo**. Coincide con todo, incluidas excepciones que no tienen nada que ver con la operación que estabas protegiendo, así que la regla es simple: nombra siempre los tipos de los que realmente puedes recuperarte.

---

Una excepción es un objeto, y `as` la asocia a un nombre para que el manejador pueda examinarla:
```python
try:
    int("abc")
except ValueError as e:
    print(e)                   # invalid literal for int() with base 10: 'abc'
    print(type(e).__name__)    # ValueError
```
`str(e)` — que es lo que usan `print(e)` y una ranura de f-string — da el mensaje con el que se construyó la excepción, y `type(e).__name__` da el nombre de la clase como texto. El nombre asociado por `as` solo existe dentro del bloque `except`; Python lo elimina cuando el bloque termina.

---

Un bloque `try` puede ir seguido de un bloque `else`, que se ejecuta **solo cuando el bloque `try` terminó sin lanzar nada**:
```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print(number * 2)
```
Poner `print(number * 2)` dentro del bloque `try` también funcionaría, pero entonces un `ValueError` lanzado por la propia impresión se confundiría con un fallo de conversión. `else` mantiene el bloque `try` reducido a la única instrucción que se está protegiendo, y contiene todo lo que debe ocurrir en caso de éxito.

---

Un bloque `finally` se ejecuta **pase lo que pase**: tras un bloque `try` limpio, tras un bloque `except`, incluso mientras una excepción que nadie capturó viaja hacia fuera, e incluso cuando el bloque `try` o `except` ejecuta un `return`:
```python
def read(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")
```
Ambos caminos imprimen `done` antes de que el valor salga de la función. Esa garantía es para lo que sirve `finally`: cerrar un fichero, liberar un bloqueo, restaurar un ajuste. La forma completa es `try` / `except` / `else` / `finally`; un `try` necesita al menos un `except` o un `finally`, y `else` solo funciona junto a un `except`.

---

Tu propio código también puede lanzar excepciones, con la instrucción `raise` seguida de un objeto excepción:
```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```
`raise` detiene la función de inmediato, exactamente igual que lo haría un fallo integrado. Devolver en su lugar un valor de error — `-1`, `None`, `False` — es fácil de olvidar para quien llama; una excepción no se puede ignorar por accidente.

Elige el tipo que describa el problema: `ValueError` cuando el argumento tiene el tipo correcto pero un valor imposible, `TypeError` cuando tiene directamente el tipo equivocado. El texto que se pasa a la excepción es su mensaje.

---

Un puñado de excepciones integradas cubre la mayoría de los fallos cotidianos:

| Excepción | Se lanza cuando | Ejemplo |
|---|---|---|
| `ValueError` | el tipo es correcto pero el valor es imposible | `int("abc")` |
| `TypeError` | el tipo en sí es incorrecto | `"x" + 1` |
| `ZeroDivisionError` | una división o módulo tiene divisor cero | `1 / 0` |
| `KeyError` | un diccionario no tiene esa clave | `{"a": 1}["b"]` |
| `IndexError` | un índice de secuencia está fuera de rango | `[1, 2][5]` |

Recurrir a una de estas en lugar de inventar un tipo nuevo mantiene tus errores legibles para cualquiera que conozca Python.

---

A veces un manejador debe reaccionar ante un fallo sin asumir la responsabilidad de él: registrarlo, contarlo, cerrar algo — y luego dejar que quien llama se ocupe. Un `raise` a solas dentro de un bloque `except` **vuelve a lanzar** la excepción que se está manejando, con su tipo, mensaje y traceback originales intactos:
```python
try:
    value = int(text)
except ValueError:
    print("could not read the value")
    raise
```
Escribir `raise ValueError(...)` en su lugar crearía una excepción nueva con su propio traceback — ya no sería el mismo fallo que capturaste, que es justo lo que un `raise` a solas conserva.

---

Cuando ningún tipo integrado encaja, define el tuyo heredando de `Exception`. Un cuerpo vacío suele bastar — el nombre es el mensaje para quien lee:
```python
class ConfigError(Exception):
    pass
```
Se comporta como cualquier otra excepción: `raise ConfigError("bad port")`, y `except ConfigError:` la captura.

Traducir un fallo de bajo nivel a tu propio tipo es habitual, y el error original no debería perderse en el proceso. `raise NewError(...) from original` los **encadena**: guarda `original` en el atributo `__cause__` de la nueva excepción, y el traceback muestra ambos bajo *The above exception was the direct cause of the following exception*:
```python
try:
    port = int(text)
except ValueError as e:
    raise ConfigError("bad port") from e
```
Sin `from e` los dos siguen quedando enlazados de forma implícita, pero `from` dice en voz alta que el primer error causó el segundo.
