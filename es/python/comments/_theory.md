Un **comentario** es una nota escrita dentro del código fuente para las personas que lo leen. Python ignora los comentarios por completo, así que nunca cambian lo que hace el programa.

El único tipo de comentario que tiene Python es el **comentario de una línea**: empieza con `#` y se extiende hasta el final de la línea.
```python
# Greets the user
print("Hello")
```
Usa comentarios para explicar para qué sirve un fragmento de código, o por qué se escribió de esa manera.

---

Un comentario no necesita su propia línea: puede ir después del código en la misma línea. Esto es un **comentario en línea**, y es un buen lugar para una nota breve sobre esa instrucción concreta:
```python
retries = 3  # give up after three attempts
```
Todo lo que va desde `#` hasta el final de la línea se ignora, mientras que el código que está antes se ejecuta como siempre.

La guía de estilo de Python, **PEP 8**, pide algo de espaciado aquí: al menos **dos espacios** entre el código y el `#`, y **un espacio** después del `#`. Un comentario en su propia línea solo necesita el espacio después del `#`.

---

Como Python descarta los comentarios por completo, añadir o borrar un comentario nunca cambia lo que hace un programa. Solo se ejecuta el código que **no** está comentado.

Esto hace que `#` sea una forma rápida de desactivar una línea de código sin borrarla. Esto se llama **comentar**:
```python
total = 10
# total = total + 5
print(total)  # prints 10
```
La segunda línea es ahora un comentario, así que `total` sigue siendo `10`. Quitar el `#` devuelve la línea a la vida.

Comentar es útil mientras experimentas, pero recuerda limpiar: el código que permanece comentado durante mucho tiempo solo confunde a quien lo lee después.

---

Muchos lenguajes tienen un segundo tipo de comentario, un **comentario de bloque** que abarca varias líneas, como `/* ... */`. Python no tiene tal sintaxis: `#` es todo lo que hay.

Cuando una explicación necesita más de una línea, pon un `#` delante de cada línea:
```python
# Prints the welcome banner.
# Called once when the app starts.
print("Welcome!")
```
El mismo truco comenta varias líneas de código a la vez: un `#` por línea. Cualquier editor puede añadir o quitar esos `#` para toda una selección con un solo atajo, así que cuesta menos de lo que parece.

---

A menudo verás una **cadena entre triples comillas** usada como si fuera un comentario de bloque:
```python
"""
This looks like a comment,
but it is a string.
"""
print("done")
```
Una cadena entre `"""` y `"""` puede abarcar varias líneas, y una cadena escrita por sí sola es una instrucción válida: Python la construye, no hace nada con ella y la descarta. No se imprime nada, así que el resultado parece un comentario.

No lo es. Es un literal de cadena, así que las reglas de las comillas siguen aplicando: una comilla sin cerrar o un `"""` perdido dentro de ella rompe el programa, mientras que dentro de un comentario `#` todo vale. También puede convertirse en una docstring por accidente si acaba siendo la primera instrucción de un archivo, una clase o una función. En cualquier otro lugar simplemente no va a ninguna parte: CPython descarta toda la instrucción al compilar.

Así que, para desactivar código, usa `#`. La cadena entre triples comillas tiene su propio trabajo, que empieza en el siguiente ejercicio.

---

Cuando una cadena es la **primera instrucción** dentro de una función, Python la trata como la documentación de esa función. Se llama **docstring**:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"
```
Por convención, una docstring se escribe entre triples comillas dobles, `"""`, incluso cuando cabe en una línea, para que pueda crecer después sin cambiar las comillas.

Escribe el resumen en tercera persona, como si describieras la función: "Returns...", "Adds...", "Checks...". La docstring debe ir antes de cualquier otra instrucción en el cuerpo, de lo contrario es solo una cadena ordinaria.

---

Una docstring no se descarta: Python la almacena en el atributo `__doc__` de la función, así que el programa puede leer su propia documentación mientras se ejecuta:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"

print(greet.__doc__)  # Returns the greeting for name.
```
Cuando una función no tiene docstring, `__doc__` es `None`. Esto es lo que imprime `help(greet)`, y lo que muestra un editor cuando pasas el cursor sobre el nombre.

---

Un archivo también puede documentarse. Una cadena escrita como la **primera instrucción del archivo**, antes de cualquier import o definición, es la **docstring del módulo**: dice para qué sirve todo el archivo.
```python
"""Tools for working with rectangles."""

def area(width, height):
    """Returns the area of a rectangle."""
    return width * height
```
Solo cuenta la primera instrucción. Un comentario puede situarse encima, pero cualquier código real en medio convierte la cadena de nuevo en una cadena ordinaria e inútil.

---

Las clases funcionan igual: una cadena colocada como primera instrucción del cuerpo de una clase es la docstring de esa clase, y se almacena en `__doc__`:
```python
class Point:
    """A point on a grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Point.__doc__)  # A point on a grid.
```
Cada método dentro de la clase también puede tener su propia docstring, que se lee con `Point.__init__.__doc__`. Así, los tres lugares que aceptan una docstring son la parte superior de un módulo, la parte superior de una clase y la parte superior de una función.

---

Las docstrings y los comentarios `#` parecen similares pero responden a preguntas diferentes.

Una **docstring** es para quien **usa** el código: qué hace la función, qué espera y qué devuelve. Sobrevive en `__doc__`, `help()` la lee, los editores la muestran y las herramientas de documentación la recopilan.

Un **comentario** es para quien **lee** el código: por qué esta línea está escrita de esta manera, qué significa el número extraño, qué error evita. Existe solo en el archivo fuente y desaparece una vez que el programa se ejecuta.

```python
def timeout():
    """Returns the number of seconds to wait for the server."""
    # the server drops idle connections after 35 seconds
    return 30
```
Así: la documentación de la función va en la docstring, las notas sobre la implementación van en los comentarios.

---

Cuando una línea no basta, una docstring crece hasta un formato fijo, descrito en **PEP 257**: un resumen de una línea, una línea en blanco, luego los detalles, y el `"""` de cierre en una línea propia.
```python
def to_seconds(minutes):
    """Returns the number of seconds in the given minutes.

    minutes is a whole number and is never negative.
    """
    return minutes * 60
```
La línea en blanco importa: las herramientas muestran la primera línea por sí sola, como descripción corta, y guardan el resto para quien quiera leer más.

---

La docstring tiene que ser la **primera línea del cuerpo**, por encima de cualquier otra instrucción. Una cadena escrita después del `return`, o en cualquier otro lugar del cuerpo, es solo una cadena: `__doc__` sigue siendo `None` y ninguna herramienta la mostrará jamás.

---

Algunos comentarios siguen una convención que los editores entienden. Los **marcadores** más comunes son:
- `# TODO: ...` señala algo que todavía necesita escribirse
- `# FIXME: ...` señala código que se sabe que está mal y debe corregirse

```python
limit = 10
# TODO: read the limit from the settings
```
Para Python son comentarios ordinarios; los editores los recopilan en un panel dedicado, así que el trabajo pendiente es fácil de encontrar. Un `TODO` suele ir junto a un marcador de posición que mantiene el programa en funcionamiento hasta que se escribe el código real.

Cuando termines el trabajo, sustituye el marcador de posición y borra el marcador en el mismo cambio, para que el comentario nunca mienta sobre el estado del código.

---

Un comentario colocado encima de una función para decir qué hace la función está en el lugar equivocado. La docstring es el lugar para eso: se adjunta a la función, `help()` la encuentra y los editores la muestran, mientras que un comentario `#` encima del `def` es invisible para todos ellos.

```python
# adds a and b
def add(a, b):
    return a + b
```
Mover la misma frase una línea abajo, entre triples comillas, la convierte en documentación real:
```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```

---

Python busca `#` solo en el código, nunca dentro de una **cadena**. Entre comillas, `#` es un carácter ordinario:
```python
print("black is #000000")  # a hex colour
```
El primer `#` es parte del texto, el segundo inicia un comentario real. Lo mismo ocurre con `"""` dentro de un comentario `#`: ahí es solo tres caracteres de comilla, y no inicia nada.

---

Un buen comentario explica **por qué** el código hace algo, no **qué** hace. El código ya muestra lo que sucede; repetirlo con palabras añade ruido y queda obsoleto tan pronto como cambia el código:
```python
# set timeout to 30
timeout = 30
```
La razón detrás del número es lo que un lector no puede adivinar:
```python
# the server drops idle connections after 35 seconds, so stop earlier
timeout = 30
```
Si un comentario solo repite la línea de abajo, bórralo o sustitúyelo por la razón. Los mejores comentarios son los que dicen algo que el código no puede.
