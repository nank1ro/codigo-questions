Una **enumeración** (o *enum*) define un tipo común para un grupo de valores relacionados y fijos, como los días de la semana o los colores de un semáforo.
En lugar de pasar cadenas o números sueltos, le das a cada valor un **nombre**, de modo que el código es más legible y los errores tipográficos se convierten en errores.
En Python creas un enum importando `Enum` del módulo `enum` y declarando una clase que hereda de él.
Cada atributo de la clase es un **miembro** del enum, con un nombre y un valor:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
Por convención los nombres de los miembros se escriben en mayúsculas. Accedes a un miembro a través de la clase, e imprimirlo muestra los nombres de la clase y del miembro:
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

Cada miembro de un enum tiene dos atributos: `name`, el identificador que escribiste en la clase, y `value`, el valor que le asignaste:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
El valor puede ser de cualquier tipo, no solo un entero: cadenas, tuplas y floats son opciones habituales.
Un miembro es un objeto normal, por lo que puedes guardarlo en una variable y leer sus atributos más adelante:
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

Cada miembro de un enum existe **una sola vez**: cada vez que escribes `Color.RED` obtienes exactamente el mismo objeto.
Por esta razón puedes comparar miembros con `is` (identidad) así como con `==`, y ambos dan el mismo resultado:
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
Un miembro **no** es igual a su valor crudo, porque un miembro y un número simple son cosas diferentes:
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
Esto es lo que hace seguros a los enums: un `1` que proviene de otra parte del programa no puede confundirse con `Color.RED`.

---

Una clase enum es **iterable**: un bucle `for` sobre la clase visita cada miembro, en el orden en que fueron declarados:
```python
for color in Color:
    print(color.name, color.value)
```
`len()` devuelve cuántos miembros tiene el enum, y `list(Color)` construye una lista con ellos:
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
Dentro de una lista, los miembros se muestran con su `repr()`, que incluye el valor entre corchetes angulares.

---

Puedes obtener un miembro a partir de su **valor** llamando a la clase como una función, o a partir de su **nombre** usando corchetes:
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
Ambos son útiles cuando el valor o el nombre proviene de fuera del programa, como un archivo o la entrada del usuario.
Si nada coincide, `Color(9)` lanza un `ValueError` y `Color["PINK"]` lanza un `KeyError`.

---

A menudo los valores exactos no importan: solo necesitas que los miembros sean distintos.
En ese caso puedes dejar que Python elija los valores con `auto()`, que también se importa del módulo `enum`.
Asigna `1` al primer miembro y luego va contando:
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

Un miembro de un `Enum` normal no puede compararse con `<` ni sumarse a un número.
Cuando los miembros representan **niveles** que necesitan un orden, hereda de `IntEnum` en su lugar: sus miembros también son enteros, por lo que admiten comparaciones, aritmética y ordenamiento:
```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH > Priority.LOW)  # True
print(Priority.LOW + 1)              # 2
print(int(Priority.MEDIUM))          # 2
```
Un miembro de `IntEnum` también es igual a su valor entero: `Priority.LOW == 1` es `True`.

---

`StrEnum` (disponible desde Python 3.11) es la contraparte de cadenas de `IntEnum`: sus miembros también son cadenas, iguales a su valor.
Esto los hace convenientes dondequiera que se esperan cadenas simples, como claves de configuración o parámetros de una API:
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
A diferencia de un `Enum` normal, convertir un miembro de `StrEnum` a texto con `str()` o dentro de una f-string da su **valor**, no `Mode.DARK`.

---

Un enum es una clase, por lo que puede tener **métodos** y **propiedades** como cualquier otra clase.
Dentro de ellos, `self` es el miembro sobre el que se llamó al método, por lo que puedes mirar `self.name`, `self.value` o comparar `self` con otros miembros:
```python
from enum import Enum

class Light(Enum):
    RED = 1
    GREEN = 2

    def can_go(self):
        return self is Light.GREEN

    @property
    def label(self):
        return self.name.lower()

print(Light.GREEN.can_go())  # True
print(Light.RED.label)       # red
```
Cualquier valor simple asignado en el cuerpo de la clase se convierte en un miembro, mientras que las funciones y las propiedades nunca lo hacen, sin importar dónde aparezcan.

---

Si dos miembros comparten el mismo valor, el segundo no es un miembro nuevo sino un **alias** del primero:
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
Los alias se omiten al iterar y no se cuentan con `len()`.
Normalmente un valor duplicado es un error. El decorador `unique`, importado de `enum`, hace que Python lance un `ValueError` tan pronto como se declara un enum con alias:
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

Un `Flag` es un enum cuyos miembros pueden **combinarse**: un valor puede contener varios miembros a la vez, como un conjunto de opciones.
Declara sus miembros con `auto()`, que para un `Flag` asigna potencias de dos (`1`, `2`, `4`, ...), de modo que cada combinación tiene un valor distinto:
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
Usa `|` para combinar miembros, `in` para comprobar si un miembro es parte de una combinación y `value` para ver el número resultante:
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

Los enums se combinan naturalmente con la declaración `match` (disponible desde Python 3.10), que compara un valor con una serie de patrones `case` y ejecuta el primero que coincide:
```python
def action(light):
    match light:
        case Light.RED:
            return "Stop"
        case Light.GREEN:
            return "Go"
        case _:
            return "Slow down"
```
Escribe siempre el miembro con su clase, como `Light.RED`: un nombre suelto como `case RED:` no compararía nada, solo capturaría el valor en una nueva variable `RED` y coincidiría con todo.
El comodín `case _:` es el predeterminado y debe ir al final, porque cualquier patrón después de él nunca podría alcanzarse.

---

Los miembros de un enum son **hasheables**, por lo que pueden usarse como claves de diccionario y como elementos de un set.
Un diccionario con claves de un enum es una forma limpia de adjuntar datos a cada miembro, y buscarlo con un miembro es más seguro que usar una cadena simple que podría escribirse mal:
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
Como los miembros pueden aparecer en cualquier colección, todo lo que sabes sobre listas, sets y comprehensions también funciona con ellos:
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

El valor de un miembro puede ser una **tupla**, lo que te permite adjuntar varios datos a cada miembro.
Si el enum define un método `__init__`, Python lo llama una vez por miembro, desempaquetando la tupla en sus parámetros, por lo que puedes guardar cada dato en su propio atributo:
```python
from enum import Enum

class Planet(Enum):
    EARTH = (5.97, 6371)
    MARS = (0.64, 3390)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

print(Planet.MARS.radius)  # 3390
print(Planet.MARS.value)   # (0.64, 3390)
```
El `value` del miembro sigue siendo la tupla completa.

---

Iterar sobre la clase y buscar miembros por nombre funcionan bien juntos cuando procesas datos que provienen de fuera, como líneas de registro o un archivo.
Una dictionary comprehension sobre la clase prepara una entrada por miembro, y luego `Level[name]` convierte cada cadena entrante en el miembro correspondiente:
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
Como el enum conserva el orden de declaración, iterar sobre `counts` después da los miembros en ese mismo orden.

---

Además de los métodos normales, un enum puede definir **métodos de clase** con `@classmethod`. Reciben la propia clase del enum como `cls`, por lo que son el lugar adecuado para formas alternativas de encontrar un miembro:
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
Junto con `auto()`, los métodos, las propiedades y las búsquedas, esto te permite construir enums que llevan su propio comportamiento.
