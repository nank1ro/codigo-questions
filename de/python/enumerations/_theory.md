Eine **Enumeration** (oder *Enum*) definiert einen gemeinsamen Typ für eine Gruppe verwandter, fester Werte, wie die Wochentage oder die Farben einer Ampel.
Statt lose Zeichenketten oder Zahlen weiterzureichen, gibst du jedem Wert einen **Namen**, wodurch der Code lesbarer wird und Tippfehler zu Fehlern werden.
In Python erstellst du ein Enum, indem du `Enum` aus dem Modul `enum` importierst und eine Klasse deklarierst, die davon erbt.
Jedes Klassenattribut ist ein **Member** des Enums, mit einem Namen und einem Wert:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
Konventionsgemäß werden Member-Namen in Großbuchstaben geschrieben. Du greifst auf einen Member über die Klasse zu, und beim Ausgeben werden der Klassen- und der Member-Name angezeigt:
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

Jeder Member eines Enums hat zwei Attribute: `name`, den Bezeichner, den du in der Klasse geschrieben hast, und `value`, den Wert, den du ihm zugewiesen hast:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
Der Wert kann einen beliebigen Typ haben, nicht nur eine ganze Zahl: Zeichenketten, Tupel und Floats sind häufige Auswahlmöglichkeiten.
Ein Member ist ein normales Objekt, du kannst ihn also in einer Variable speichern und seine Attribute später lesen:
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

Jeder Enum-Member existiert **nur einmal**: jedes Mal, wenn du `Color.RED` schreibst, erhältst du exakt dasselbe Objekt.
Deshalb kannst du Member sowohl mit `is` (Identität) als auch mit `==` vergleichen, und beide liefern dasselbe Ergebnis:
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
Ein Member ist **nicht** gleich seinem Rohwert, denn ein Member und eine schlichte Zahl sind verschiedene Dinge:
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
Das macht Enums sicher: Eine `1`, die aus einem anderen Teil des Programms stammt, kann nicht mit `Color.RED` verwechselt werden.

---

Eine Enum-Klasse ist **iterierbar**: eine `for`-Schleife über die Klasse besucht jeden Member, in der Reihenfolge, in der sie deklariert wurden:
```python
for color in Color:
    print(color.name, color.value)
```
`len()` liefert, wie viele Member das Enum hat, und `list(Color)` erstellt daraus eine Liste:
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
Innerhalb einer Liste werden Member mit ihrer `repr()` angezeigt, die den Wert zwischen spitzen Klammern enthält.

---

Du erhältst einen Member ausgehend von seinem **Wert**, indem du die Klasse wie eine Funktion aufrufst, oder ausgehend von seinem **Namen** mit eckigen Klammern:
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
Beides ist praktisch, wenn der Wert oder der Name von außerhalb des Programms kommt, etwa aus einer Datei oder einer Benutzereingabe.
Wenn nichts übereinstimmt, löst `Color(9)` einen `ValueError` aus und `Color["PINK"]` einen `KeyError`.

---

Oft kommt es nicht auf die genauen Werte an: du brauchst nur, dass sich die Member unterscheiden.
In diesem Fall kannst du Python die Werte mit `auto()` wählen lassen, das ebenfalls aus dem Modul `enum` importiert wird.
Es weist dem ersten Member `1` zu und zählt dann hoch:
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

Ein einfacher `Enum`-Member kann nicht mit `<` verglichen oder zu einer Zahl addiert werden.
Wenn die Member **Stufen** darstellen, die eine Ordnung brauchen, erbe stattdessen von `IntEnum`: seine Member sind auch ganze Zahlen, daher unterstützen sie Vergleiche, Arithmetik und Sortierung:
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
Ein `IntEnum`-Member ist auch gleich seinem Ganzzahlwert: `Priority.LOW == 1` ist `True`.

---

`StrEnum` (verfügbar seit Python 3.11) ist das Zeichenketten-Gegenstück zu `IntEnum`: seine Member sind auch Zeichenketten, gleich ihrem Wert.
Das macht sie praktisch, überall wo einfache Zeichenketten erwartet werden, etwa bei Konfigurationsschlüsseln oder API-Parametern:
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
Anders als bei einem einfachen `Enum` liefert die Umwandlung eines `StrEnum`-Members in Text mit `str()` oder in einem f-String seinen **Wert**, nicht `Mode.DARK`.

---

Ein Enum ist eine Klasse, daher kann es wie jede andere Klasse **Methoden** und **Properties** haben.
In ihnen ist `self` der Member, auf dem die Methode aufgerufen wurde, du kannst dir also `self.name`, `self.value` ansehen oder `self` mit anderen Membern vergleichen:
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
Jeder einfache Wert, der im Klassenkörper zugewiesen wird, wird zu einem Member, während Funktionen und Properties das nie werden, egal wo sie auftauchen.

---

Wenn zwei Member denselben Wert haben, ist der zweite kein neuer Member, sondern ein **Alias** des ersten:
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
Aliase werden beim Iterieren übersprungen und von `len()` nicht mitgezählt.
Normalerweise ist ein doppelter Wert ein Fehler. Der `unique`-Dekorator, importiert aus `enum`, bringt Python dazu, einen `ValueError` auszulösen, sobald ein Enum mit Aliasen deklariert wird:
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

Ein `Flag` ist ein Enum, dessen Member **kombiniert** werden können: ein Wert kann mehrere Member gleichzeitig halten, wie ein Satz von Optionen.
Deklariere seine Member mit `auto()`, das bei einem `Flag` Zweierpotenzen (`1`, `2`, `4`, ...) zuweist, sodass jede Kombination einen eigenen Wert hat:
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
Verwende `|`, um Member zu kombinieren, `in`, um zu prüfen, ob ein Member Teil einer Kombination ist, und `value`, um die resultierende Zahl zu sehen:
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

Enums passen natürlich zur `match`-Anweisung (verfügbar seit Python 3.10), die einen Wert mit einer Reihe von `case`-Mustern vergleicht und den ersten passenden ausführt:
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
Schreibe den Member immer mit seiner Klasse, wie `Light.RED`: ein bloßer Name wie `case RED:` würde nichts vergleichen, er würde den Wert nur in eine neue Variable `RED` einfangen und auf alles passen.
Der Platzhalter `case _:` ist der Standardfall und muss zuletzt kommen, denn jedes Muster danach wäre nie erreichbar.

---

Enum-Member sind **hashbar**, daher können sie als Wörterbuch-Schlüssel und als Set-Elemente verwendet werden.
Ein Wörterbuch mit einem Enum als Schlüssel ist eine saubere Art, Daten an jeden Member anzuhängen, und der Zugriff mit einem Member ist sicherer als eine rohe Zeichenkette, die sich verschreiben lässt:
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
Da Member in jeder Sammlung vorkommen können, funktioniert auch alles, was du über Listen, Sets und Comprehensions weißt, mit ihnen:
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

Ein Member-Wert kann ein **Tupel** sein, womit du jedem Member mehrere Daten anhängen kannst.
Wenn das Enum eine `__init__`-Methode definiert, ruft Python sie einmal pro Member auf und entpackt das Tupel in ihre Parameter, sodass du jedes Stück in seinem eigenen Attribut speichern kannst:
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
Der `value` des Members bleibt das ganze Tupel.

---

Über die Klasse zu iterieren und Member anhand ihres Namens nachzuschlagen funktioniert gut zusammen, wenn du Daten verarbeitest, die von außen kommen, wie Log-Zeilen oder eine Datei.
Eine Dict Comprehension über die Klasse bereitet einen Eintrag pro Member vor, dann wandelt `Level[name]` jede eingehende Zeichenkette in den passenden Member um:
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
Da das Enum die Deklarationsreihenfolge beibehält, liefert das nachfolgende Iterieren über `counts` die Member in derselben Reihenfolge.

---

Neben normalen Methoden kann ein Enum **Klassenmethoden** mit `@classmethod` definieren. Sie erhalten die Enum-Klasse selbst als `cls`, daher sind sie der richtige Ort für alternative Wege, einen Member zu finden:
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
Zusammen mit `auto()`, Methoden, Properties und Nachschlägen kannst du damit Enums bauen, die ihr eigenes Verhalten mitbringen.
