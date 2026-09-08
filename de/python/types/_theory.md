Jeder Wert in Python hat einen **Typ**, der aussagt, um welche Art von Daten es sich handelt und was du damit machen kannst.
Die grundlegenden eingebauten Typen sind:
- `int`, eine ganze Zahl wie `42` oder `-3`
- `float`, eine Zahl mit Dezimalteil wie `3.5`
- `str`, ein Stück Text wie `"hello"`
- `bool`, einer der beiden Werte `True` und `False`
- `NoneType`, der Typ des speziellen Werts `None`, der "keinen Wert" bedeutet

Die eingebaute Funktion `type()` gibt den Typ eines Werts zurück. Beim Ausgeben zeigt sie den Klassennamen:
```python
print(type(42))     # <class 'int'>
print(type("hi"))   # <class 'str'>
```
`NoneType` schreibst du nie selbst: `type(None)` gibt ihn zurück, aber der Name ist kein Built-in wie die anderen vier.

---

`type()` gibt die Klasse eines Werts zurück, daher kannst du sie mit einem Klassennamen vergleichen, indem du `is` verwendest:
```python
age = 30
print(type(age) is int)  # True
```
In den meisten Fällen willst du aber nur wissen, **ob** ein Wert einen bestimmten Typ hat. Das ist die Aufgabe von `isinstance(value, cls)`, das `True` oder `False` zurückgibt:
```python
print(isinstance(age, int))    # True
print(isinstance(age, str))    # False
```
Das zweite Argument kann auch ein **Tupel** von Klassen sein: Das Ergebnis ist `True`, wenn der Wert zu einem davon gehört:
```python
print(isinstance(2.5, (int, float)))  # True
```

---

Python ist **dynamisch typisiert**: Der Typ gehört zum **Wert**, nicht zur Variable.
Eine Variable ist nur ein Name, der an einen Wert angehängt ist, und du kannst ihn jederzeit an einen Wert eines anderen Typs anhängen:
```python
x = 10
print(type(x))  # <class 'int'>
x = "ten"
print(type(x))  # <class 'str'>
```
Es ist weder eine Deklaration noch eine Umwandlung nötig: Der alte Wert wird einfach vergessen.
Das ist praktisch, bedeutet aber auch, dass der Typ einer Variable erst bekannt ist, wenn das Programm läuft. Wer daher versehentlich Typen vermischt, bekommt erst zur Laufzeit einen Fehler, nicht vorher.

---

Du kennst die arithmetischen Operatoren bereits. Was hier zählt, ist der **Typ des Ergebnisses**.
Die Kombination eines `int` mit einem `float` ergibt einen `float`, auch wenn der Dezimalteil null ist:
```python
print(3 + 0.5)   # 3.5
print(2 * 1.0)   # 2.0
```
Die **echte Division** `/` gibt immer einen `float` zurück, selbst wenn die Zahlen exakt teilbar sind:
```python
print(10 / 5)    # 2.0
print(7 / 2)     # 3.5
```
Die **Ganzzahldivision** `//` rundet das Ergebnis auf die nächstkleinere ganze Zahl ab (daher ist `-7 // 2` gleich `-4`) und gibt einen `int` zurück, wenn beide Operanden Ganzzahlen sind. Zusammen mit dem Rest `%` zerlegt sie eine Menge in ganze Teile:
```python
print(7 // 2)    # 3
print(7 % 2)     # 1
```

---

Werte ändern ihren Typ nicht von selbst: Um einen Wert in einen anderen Typ umzuwandeln, rufst du den Typnamen wie eine Funktion auf. Das nennt man **Umwandlung** (oder *Casting*):
```python
print(int("42"))      # 42
print(float("3.5"))   # 3.5
print(str(7))         # '7'
print(int(3.9))       # 3
```
`int()` und `float()` lesen Zahlen, die als Text geschrieben sind – das bekommst du von Benutzereingaben oder aus Dateien. `str()` macht aus allem Text, sodass es mit `+` an andere Zeichenketten angehängt werden kann.
Beachte, dass `int(3.9)` nicht rundet: Es verwirft den Dezimalteil.

---

Eine Umwandlung kann fehlschlagen. `int("abc")` kann keine Zahl erzeugen, daher wirft es einen `ValueError` und das Programm stoppt:
```python
int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
int("3.5")   # ValueError as well: "3.5" is not a whole number
```
Damit das Programm weiterläuft, kannst du den Fehler mit `try` / `except` abfangen: Der Code im `try`-Block läuft, und wenn er den genannten Fehler auslöst, wird stattdessen der `except`-Block ausgeführt:
```python
try:
    number = int(text)
except ValueError:
    number = 0
```
Wenn die Umwandlung gelingt, wird der `except`-Block übersprungen.

---

Jeder Wert kann als boolescher Wert interpretiert werden. `bool()` wandelt einen Wert in `True` oder `False` um, und dieselbe Regel wird angewendet, wenn ein Wert direkt in einem `if` verwendet wird.
Als **falsch** gelten die "leeren" Werte:
- die Zahl `0` (und `0.0`)
- die leere Zeichenkette `""`
- leere Sammlungen wie `[]`, `{}`, `()` und `set()`
- `None`

Jeder nicht-leere Wert ist **wahr**, auch negative Zahlen und Zeichenketten, die nur leer aussehen, wie `"0"` oder `" "`:
```python
print(bool(0))     # False
print(bool(-1))    # True
print(bool(""))    # False
print(bool("0"))   # True
```
Deshalb ist `if name:` eine gängige Methode, um zu prüfen, dass eine Zeichenkette nicht leer ist.

---

`bool` ist eine **Unterklasse** von `int`: `True` verhält sich wie `1` und `False` wie `0`, wo immer eine Zahl erwartet wird:
```python
print(True + 1)     # 2
print(True == 1)    # True
print(False * 10)   # 0
```
`sum()` addiert die Elemente einer Liste. Wenn man also eine Liste von booleschen Werten summiert, **zählt** man, wie viele davon `True` sind:
```python
answers = [True, False, True]
print(sum(answers))  # 2
```
Wegen der Unterklasse-Beziehung gibt `isinstance(True, int)` `True` zurück, während `type(True)` weiterhin `bool` ist.

---

`None` ist ein eigener Wert, der "nichts hier" bedeutet. Er ist das, was eine Funktion zurückgibt, wenn sie keine `return`-Anweisung hat, und er ist ein gängiger Platzhalter für einen Wert, der noch nicht bekannt ist.
Da es nur ein einziges `None` gibt, prüfe mit `is` darauf, nicht mit `==`:
```python
result = None
if result is None:
    print("no result yet")
```
Jeder Typ hat ein Attribut `__name__` mit seinem Namen als Zeichenkette, was für Meldungen praktisch ist:
```python
print(type(3).__name__)     # int
print(type(None).__name__)  # NoneType
```

---

Beim Ausgeben eines `float` werden so viele Ziffern angezeigt, wie nötig sind, um ihn exakt darzustellen – das sind oft zu viele:
```python
print(19.999 * 3)  # 59.997
print(10 / 3)      # 3.3333333333333335
```
Innerhalb eines f-Strings kannst du nach einem Doppelpunkt eine **Formatspezifikation** anhängen. `.2f` bedeutet "Festkommazahl mit 2 Dezimalstellen":
```python
total = 10 / 3
print(f"{total:.2f}")   # 3.33
print(f"{total:.0f}")   # 3
```
Der Wert wird auf die angeforderte Anzahl von Dezimalstellen gerundet, und bei Bedarf werden Nullen angehängt: `f"{2.5:.2f}"` ergibt `2.50`.

---

Formatierung ändert nur, wie eine Zahl angezeigt wird. Um einen gerundeten **Wert** zu erhalten, verwende die eingebaute Funktion `round()`:
```python
print(round(3.14159, 2))  # 3.14
print(round(2.71828, 1))  # 2.7
```
Mit einem einzigen Argument rundet `round()` auf die nächste ganze Zahl und gibt einen `int` zurück; mit einer Anzahl von Dezimalstellen gibt es einen `float` zurück:
```python
print(round(3.7))     # 4
print(round(3.7, 0))  # 4.0
```
Beachte, dass Werte, die genau in der Mitte zwischen zwei Zahlen liegen, auf die **gerade** Zahl gerundet werden: `round(2.5)` ist `2` und `round(3.5)` ist `4`.

---

Ein `float` wird binär mit einer festen Anzahl von Bits gespeichert, daher können die meisten Dezimalzahlen nur **angenähert** dargestellt werden. Der Fehler ist winzig, zeigt sich aber in Rechnungen:
```python
print(0.1 + 0.2)   # 0.30000000000000004
```
Aus diesem Grund solltest du Gleitkommazahlen nicht auf exakte Gleichheit vergleichen. Runde beide Seiten oder verwende `math.isclose()`, das prüft, ob zwei Zahlen innerhalb einer winzigen Toleranz gleich sind:
```python
import math
print(round(0.1 + 0.2, 2) == 0.3)  # True
print(math.isclose(0.1 + 0.2, 0.3))  # True
```
Ganzzahlen haben dieses Problem nicht: `1 + 2 == 3` ist immer `True`.

---

Anders als in vielen Sprachen haben Python-Ganzzahlen **keine maximale Größe**: Ein `int` wächst, um so viele Ziffern wie nötig aufzunehmen, sodass große Berechnungen exakt bleiben:
```python
print(3 ** 100)  # 515377520732011331036461129765621272702107522001
```
Ein `float` behält dagegen nur etwa 15 signifikante Stellen, daher verliert dieselbe Potenz als float an Genauigkeit:
```python
print(3.0 ** 100)  # 5.153775207320113e+47
```
Da `str()` mit jedem `int` funktioniert, ist eine schnelle Methode, die Ziffern einer Zahl zu zählen, die Länge ihres Textes zu messen.

---

Du kannst den erwarteten Typ einer Variable, eines Parameters oder eines Rückgabewerts als **Type Hint** schreiben: ein Doppelpunkt nach dem Namen bei Variablen und Parametern, ein Pfeil `->` vor dem Doppelpunkt beim Rückgabewert:
```python
count: int = 3

def greet(name: str) -> str:
    return "Hi " + name
```
Hints sind **Dokumentation** für Menschen und für Tools wie Editoren: Python prüft sie **nicht**. Dieser Code läuft ohne Beanstandung und gibt `hello` aus:
```python
count: int = "hello"
print(count)
```
Hints machen die beabsichtigten Typen klar, aber der Wert entscheidet weiterhin über den echten Typ.

---

Umwandlungen können kombiniert werden. `int("3.7")` schlägt fehl, aber `float("3.7")` funktioniert, und `int()` eines `float` verwirft den Dezimalteil:
```python
number = float("3.7")   # 3.7
print(int(number))      # 3
```
`bool()` folgt den Wahrheitsregeln: `bool("")` ist `False`, und beachte, dass `bool("False")` `True` ist, weil es eine nicht-leere Zeichenkette ist.

---

Text von außen ist immer eine Zeichenkette (`str`), und dein Programm muss herausfinden, welchen Typ sie wirklich enthält.
Ein gängiger Ansatz ist, zuerst die **strengste** Umwandlung zu versuchen und zur nächsten zurückzufallen, wenn sie einen `ValueError` auslöst:
```python
try:
    value = int(text)
except ValueError:
    value = float(text)
```
Wenn du ein zweites `try` im `except`-Block verschachtelst, kannst du ein weiteres Mal zurückfallen, um zum Beispiel den Text unverändert zu behalten.
