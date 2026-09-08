Ein **Set** ist eine Sammlung **eindeutiger** Elemente: Derselbe Wert kann nur einmal vorkommen, egal wie oft du ihn schreibst.
Ein Set ist außerdem **ungeordnet**: es gibt kein erstes oder letztes Element, daher kannst du kein Element über einen Index lesen.
Sets sind ideal, wenn dich nur interessiert, *welche* Werte vorhanden sind, nicht wie oft oder an welcher Position.
Du erstellst ein Set, indem du seine Elemente zwischen geschweiften Klammern `{...}` schreibst:
```python
colors = {"red", "blue", "red"}
print(len(colors))  # 2
```
Das doppelte `"red"` wird verworfen, sodass `len()` nur die unterschiedlichen Elemente zählt.

---

Die eingebaute Funktion `set()` erstellt ein Set aus einer beliebigen Sammlung, zum Beispiel einer Liste oder einer Zeichenkette.
Da ein Set jeden Wert nur einmal behält, ist dies die klassische Methode, um **Duplikate zu entfernen**:
```python
nums = [1, 2, 2, 3]
unique = set(nums)
print(len(unique))  # 3
```
Um zu prüfen, ob ein Wert vorhanden ist, verwendest du den `in`-Operator, der `True` oder `False` zurückgibt:
```python
print(2 in unique)  # True
print(9 in unique)  # False
```
Mitgliedschaftsprüfungen bei einem Set sind sehr schnell, selbst bei Tausenden von Elementen.

---

Beim Erstellen eines **leeren Sets** lauert eine Falle.
Geschweifte Klammern sind auch die Syntax von Dictionaries, daher erstellt `{}` ein leeres **Dictionary**, kein Set:
```python
empty = {}
print(type(empty))  # <class 'dict'>
```
Um ein leeres Set zu erhalten, musst du `set()` ohne Argumente aufrufen:
```python
empty = set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
```

---

Sets sind **mutable**: Du kannst nach dem Erstellen Elemente hinzufügen und entfernen.
`add(value)` fügt einen Wert ein; das Hinzufügen eines bereits vorhandenen Werts ändert nichts:
```python
letters = {"a", "b"}
letters.add("c")
letters.add("a")
print(len(letters))  # 3
```
Es gibt zwei Möglichkeiten, ein Element zu entfernen:
- `remove(value)` löscht es, löst aber einen `KeyError` aus, wenn der Wert nicht im Set ist
- `discard(value)` löscht es, falls vorhanden, und tut **nichts**, wenn nicht, ohne Fehler
```python
letters.remove("a")
letters.discard("z")  # "z" ist nicht vorhanden, aber kein Fehler
letters.remove("z")   # KeyError: 'z'
```

---

`pop()` entfernt **ein beliebiges Element** aus dem Set und gibt es zurück.
Da ein Set keine Reihenfolge hat, kannst du nicht wählen, welches Element entfernt wird; der Aufruf von `pop()` bei einem leeren Set löst einen `KeyError` aus:
```python
tickets = {101, 102, 103}
picked = tickets.pop()
print(len(tickets))  # 2
```
`clear()` entfernt **alle** Elemente und hinterlässt ein leeres Set:
```python
tickets.clear()
print(len(tickets))  # 0
```

---

Du kannst mit `for` über ein Set iterieren, genau wie über eine Liste:
```python
for color in {"red", "blue"}:
    print(color)
```
Da ein Set ungeordnet ist, können die Elemente in **beliebiger Reihenfolge** erscheinen, und diese Reihenfolge kann sich sogar zwischen verschiedenen Durchläufen ändern.
Wenn du eine vorhersehbare Reihenfolge brauchst, übergib das Set an `sorted()`, das eine sortierte **Liste** seiner Elemente zurückgibt:
```python
for color in sorted({"red", "blue"}):
    print(color)  # blue, then red
```

---

Die **Vereinigung** zweier Sets ist ein neues Set mit den Elementen **beider**, ohne Duplikate.
Verwende den `|`-Operator oder die Methode `union()`:
```python
a = {1, 2}
b = {2, 3}
print(a | b)        # {1, 2, 3}
print(a.union(b))   # {1, 2, 3}
```
Weder `a` noch `b` wird verändert: Mengenoperationen geben immer ein neues Set zurück.

---

Die **Schnittmenge** zweier Sets enthält nur die Elemente, die in **beiden** vorhanden sind.
Verwende den `&`-Operator oder die Methode `intersection()`:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)               # {2, 3}
print(a.intersection(b))   # {2, 3}
```
Wenn die Sets nichts gemeinsam haben, ist das Ergebnis ein leeres Set.

---

Die **Differenz** `a - b` enthält die Elemente von `a`, die **nicht** in `b` sind.
Die Reihenfolge spielt eine Rolle: `a - b` und `b - a` sind meist unterschiedlich:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}
print(b - a)  # {4}
```
Die **symmetrische Differenz** `a ^ b` enthält die Elemente, die in **genau einem** der beiden Sets sind:
```python
print(a ^ b)  # {1, 4}
```
Die Methodenformen sind `difference()` und `symmetric_difference()`.

---

Operatoren und Methoden sind nicht perfekt gleichwertig.
Die Operatoren `|`, `&`, `-` und `^` funktionieren nur, wenn **beide** Operanden Sets sind.
Die Methoden `union()`, `intersection()`, `difference()` und `symmetric_difference()` akzeptieren **jedes Iterable**, wie eine Liste oder eine Zeichenkette:
```python
a = {1, 2}
print(a.union([2, 3]))  # {1, 2, 3}
print(a | [2, 3])       # TypeError: unsupported operand type(s) for |: 'set' and 'list'
```

---

Sets können auch miteinander **verglichen** werden.
`a.issubset(b)`, oder `a <= b`, ist `True`, wenn jedes Element von `a` auch in `b` ist.
`a.issuperset(b)`, oder `a >= b`, ist `True`, wenn `a` jedes Element von `b` enthält.
`a.isdisjoint(b)` ist `True`, wenn die beiden Sets **kein** gemeinsames Element haben:
```python
small = {1, 2}
big = {1, 2, 3}
print(small <= big)              # True
print(big.issuperset(small))     # True
print(small.isdisjoint({8, 9}))  # True
```

---

Ein Set kann nur **hashbare** Elemente enthalten, also Werte, die sich nicht ändern können: Zahlen, Zeichenketten, `True`/`False` und **Tupel**.
Der Versuch, eine Liste, ein Dictionary oder ein anderes Set hinzuzufügen, löst einen `TypeError` aus:
```python
points = set()
points.add((1, 2))  # ok, ein Tupel
points.add([1, 2])  # TypeError: unhashable type: 'list'
```
Sets aus Tupeln eignen sich gut, um eindeutige Paare zu verfolgen, wie Koordinaten oder (Name, Alter)-Datensätze:
```python
visits = [(1, 2), (1, 2), (3, 4)]
print(len(set(visits)))  # 2
```

---

Ein **frozenset** ist ein **unveränderliches** Set: einmal erstellt, kannst du keine Elemente hinzufügen oder entfernen.
Erstelle es mit `frozenset()` aus einer beliebigen Sammlung:
```python
days = frozenset(["sat", "sun"])
print("sat" in days)  # True
days.add("mon")       # AttributeError: 'frozenset' object has no attribute 'add'
```
Beim Ausgeben eines frozenset wird sein Typ um die Elemente herum angezeigt, wie `frozenset({'sat', 'sun'})`.
Da es sich nicht ändern kann, ist ein frozenset hashbar: im Gegensatz zu einem normalen Set kann es Element eines anderen Sets oder ein Dictionary-Schlüssel sein.
Alle schreibgeschützten Operationen (`in`, `len()`, `|`, `&`, `-`, `^`, Vergleiche) funktionieren wie gewohnt.

---

Eine **Set Comprehension** erstellt ein Set in einem einzigen Ausdruck, mit derselben Syntax wie eine List Comprehension, aber mit geschweiften Klammern:
```python
nums = [1, 2, 2, 3]
squares = {n * n for n in nums}
print(squares)  # {1, 4, 9}
```
Ein optionales `if` filtert die Elemente, und vom Ausdruck erzeugte Duplikate werden automatisch verworfen:
```python
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

---

Mengenoperationen können ein Set auch **direkt** verändern, statt ein neues zurückzugeben.
`update(iterable)` fügt jedes Element einer beliebigen Sammlung hinzu, wie `add()`, aber für viele Werte auf einmal:
```python
inventory = {"sword"}
inventory.update(["potion", "map"])
print(len(inventory))  # 3
```
Die erweiterten Operatoren funktionieren auch direkt: `|=` fügt die Elemente eines anderen Sets hinzu, `&=` behält nur die gemeinsamen, `-=` entfernt die Elemente eines anderen Sets:
```python
inventory -= {"map"}
print(sorted(inventory))  # ['potion', 'sword']
```

---

Zwei Sets sind **gleich**, wenn sie dieselben Elemente enthalten, unabhängig von der Reihenfolge, in der sie geschrieben wurden:
```python
print({1, 2, 3} == {3, 1, 2})  # True
```
Der Vergleich der Länge einer Sammlung mit der Länge ihres Sets ist eine schnelle Methode, um Duplikate zu erkennen: Wenn das Set **kleiner** ist, kam ein Wert mehr als einmal vor:
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)) < len(emails))  # True
```
Die Listenmethode `count(value)` sagt dir, wie oft ein Wert vorkommt, was hilft herauszufinden, *welche* Werte doppelt sind.
