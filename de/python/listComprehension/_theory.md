Eine sehr häufige Aufgabe ist es, aus einer bestehenden Liste eine neue zu erstellen.
Mit einer `for`-Schleife und `append()` braucht man dafür ein paar Zeilen:
```python
nums = [1, 2, 3]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6]
```
Python bietet dafür eine kürzere Form: die **List Comprehension**, die die gesamte Liste in einem einzigen Ausdruck erstellt:
```python
doubled = [n * 2 for n in nums]
```
Die Syntax lautet `[Ausdruck for Element in Iterable]`: der `for`-Teil durchläuft die Elemente, und der Ausdruck auf der linken Seite wird für jedes davon ausgewertet.
Das Ergebnis ist eine brandneue Liste, genau dieselbe wie die mit der Schleife erstellte.

---

Der Ausdruck auf der linken Seite kann alles sein, was einen Wert erzeugt: eine Berechnung, ein Funktionsaufruf, ein Methodenaufruf.
Die Schleifenvariable kann einen beliebigen Namen haben und existiert nur innerhalb der eckigen Klammern:
```python
prices = [10, 20]
with_tax = [price * 1.2 for price in prices]
print(with_tax)  # [12.0, 24.0]
```

---

Eine Comprehension kann die Elemente auch **filtern**.
Füge nach dem `for`-Teil eine `if`-Bedingung hinzu: nur die Elemente, für die die Bedingung `True` ist, landen in der neuen Liste:
```python
nums = [5, 12, 8, 20]
big = [n for n in nums if n > 10]
print(big)  # [12, 20]
```
Das ist dasselbe wie eine Schleife mit einem `if` darin, und es ersetzt `filter()` mit einer lambda auf lesbarere Weise.

---

Die Filterbedingung kann jeder Ausdruck sein, der einen Wahrheitswert liefert, einschließlich Funktionsaufrufen wie `len()`:
```python
words = ["a", "bee", "cat"]
short = [w for w in words if len(w) < 3]
print(short)  # ['a']
```

---

Das Iterable muss keine Liste sein: alles, worüber man iterieren kann, funktioniert, und `range()` ist ein Favorit.
Es ist der schnellste Weg, eine Liste von Zahlen zu erstellen:
```python
squares = [n * n for n in range(4)]
print(squares)  # [0, 1, 4, 9]
```
Denke daran, dass `range(start, stop)` `stop` ausschließt.

---

Comprehensions eignen sich hervorragend zum **Transformieren von Strings**.
Rufe eine String-Methode auf jedem Element auf, oder baue einen neuen String mit einem f-String:
```python
names = ["ana", "bob"]
greetings = [f"Hi {name.capitalize()}" for name in names]
print(greetings)  # ['Hi Ana', 'Hi Bob']
```

---

Innerhalb einer Comprehension kannst du jede zuvor definierte Variable verwenden, zum Beispiel als Grenzwert eines `range()`.

---

Manchmal möchtest du keine Elemente verwerfen, sondern für einige von ihnen **einen anderen Wert** wählen.
Verwende einen bedingten Ausdruck `a if bedingung else b` als Ausdruck links vom `for`:
```python
nums = [3, -1, 4]
signs = ["+" if n > 0 else "-" for n in nums]
print(signs)  # ['+', '-', '+']
```
Beachte die Position: das `if-else` steht **vor** dem `for` und erzeugt immer einen Wert, während das Filter-`if` **nach** dem `for` steht und kein `else` hat.

---

Die beiden Bedingungen können in derselben Comprehension kombiniert werden: ein `if-else`, um den Wert zu wählen, und ein Filter-`if` am Ende, um einige Elemente zu überspringen.
```python
nums = [1, 2, 3, 4]
result = ["big" if n > 2 else "small" for n in nums if n != 3]
print(result)  # ['small', 'small', 'big']
```

---

Die beiden Positionen von `if` werden leicht verwechselt, halte sie also auseinander:
```python
values = [n if n > 0 else 0 for n in nums]  # if-else vor dem for: wählt einen Wert, else erforderlich
positives = [n for n in nums if n > 0]      # if nach dem for: filtert, kein else erlaubt
```
Ein `else` nach dem Filter-`if` ist ein Syntaxfehler.

---

Eine Comprehension kann **mehr als ein `for`** haben.
Sie funktionieren wie verschachtelte Schleifen: das erste `for` ist die äußere Schleife, das zweite die innere.
```python
pairs = [a + b for a in ["x", "y"] for b in ["1", "2"]]
print(pairs)  # ['x1', 'x2', 'y1', 'y2']
```

---

Das innere `for` kann die Variable des äußeren verwenden.
Das ist der klassische Weg, eine Liste von Listen zu einer einzigen Liste zu **flatten**:
```python
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```
Die Funktion `sum()` addiert dann alle Zahlen einer Liste.

---

Du kannst auch über ein **Dictionary** iterieren.
Mit `.items()` entpackt der `for`-Teil jedes Paar in zwei Variablen, einen Schlüssel und einen Wert:
```python
ages = {"ana": 31, "bob": 25}
lines = [f"{name} is {age}" for name, age in ages.items()]
print(lines)  # ['ana is 31', 'bob is 25']
```

---

Dieselbe Idee funktioniert auch für Dictionaries: eine **Dict Comprehension** verwendet geschweifte Klammern und einen `key: value`-Ausdruck:
```python
names = ["ana", "bob"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'ana': 3, 'bob': 3}
```

---

Geschweifte Klammern **ohne** den `key: value`-Teil ergeben eine **Set Comprehension**.
Ein Set ist eine ungeordnete Sammlung, die nur eindeutige Werte behält, sodass Duplikate automatisch verschwinden:
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)  # {1, 2, 3}
```

---

**Wann solltest du eine Comprehension verwenden?**
Sie ist perfekt, wenn das Ergebnis eine Liste (oder ein Dict oder Set) ist und die Logik in eine lesbare Zeile passt: eine einfache Transformation, ein optionaler Filter.
Wenn du mehrere Anweisungen, mehr als zwei verschachtelte `for`, oder eine schwer lesbare Zeile brauchst, schreibe stattdessen eine einfache `for`-Schleife: der Code wird länger, aber klarer.
Eine Comprehension ersetzt außerdem die meisten Verwendungen von `map()` und `filter()` mit lambdas:
```python
doubled = list(map(lambda n: n * 2, nums))
doubled = [n * 2 for n in nums]  # same result, easier to read
```
