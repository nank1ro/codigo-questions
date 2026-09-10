Vergleichsoperatoren vergleichen zwei Werte und geben einen **Boolean** zurück, `True` oder `False`: `==` gleich, `!=` ungleich, `<` kleiner als, `>` größer als, `<=` kleiner als oder gleich, `>=` größer als oder gleich:
```python
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age < 18)   # False
print(age >= 18)  # True
```
Das Ergebnis kann in einer Variablen gespeichert oder direkt ausgegeben werden. Ein einzelnes `=` ist eine Zuweisung, kein Vergleich.

---

Vergleichsoperatoren sind nicht auf Zahlen beschränkt. Zeichenketten werden Zeichen für Zeichen über ihre Codepunkte verglichen, sodass `"apple" < "banana"` `True` ist und, weil jeder Großbuchstabe vor den Kleinbuchstaben kommt, `"Zoo" < "apple"` ebenfalls `True` ist. Listen und Tupel werden auf die gleiche Weise Element für Element verglichen:
```python
print("cat" < "dog")       # True
print([1, 2, 3] < [1, 3])  # True
print((1, 2) == (1, 2))    # True
```
Ein Vergleich ist ein Ausdruck, sodass eine Funktion `return a < b` direkt zurückgeben kann, statt ihn in ein `if` zu verpacken.

---

Vergleiche können **verkettet** werden: `1 < x < 10` prüft, ob `x` größer als `1` **und** kleiner als `10` ist, genau wie `1 < x and x < 10`, aber `x` wird nur einmal ausgewertet:
```python
x = 5
print(1 < x < 10)   # True
print(1 < x <= 5)   # True
print(10 < x < 20)  # False
```
Beliebige Vergleichsoperatoren können verkettet werden, und jeder gilt für seine beiden Nachbarn: `a < b == c` bedeutet `a < b and b == c`. Eine Kette als Bereich zu lesen, `low < x < high`, ist der häufigste Anwendungsfall.

---

Logische Operatoren kombinieren Booleans. `and` ist `True`, nur wenn beide Seiten `True` sind, `or`, wenn mindestens eine Seite es ist, und `not` kehrt einen einzelnen Wert um:
```python
age = 20
member = False
print(age >= 18 and member)  # False
print(age >= 18 or member)   # True
print(not member)            # True
```
Vergleiche binden stärker als logische Operatoren, daher braucht `age >= 18 and member` keine Klammern. Klammern braucht man, um ein `or` innerhalb eines `and` zu gruppieren: `a and (b or c)`.

---

Wenn `not`, `and` und `or` in einem Ausdruck vorkommen, wendet Python zuerst `not` an, dann `and`, dann `or`. `a or b and c` bedeutet also `a or (b and c)`, und `not a == b` bedeutet `not (a == b)`:
```python
x = 6
print(x == 6 or x < 10 and x > 100)  # True: x == 6 or (False)
print(not x == 6)                    # False
```
Wenn eine andere Gruppierung gemeint ist, füge Klammern hinzu; sie machen den Ausdruck auch leichter lesbar.

---

Jeder Wert hat einen **Wahrheitswert**. `bool(value)` gibt `False` für `0`, `0.0`, `None`, die leere Zeichenkette `""` und leere Container wie `[]`, `{}` und `set()` zurück; jeder andere Wert ist truthy, einschließlich `"0"` und `[0]`:
```python
print(bool(0), bool(""), bool(None))   # False False False
print(bool(42), bool("0"), bool([0]))  # True True True
```
`if`, `while`, `and`, `or` und `not` verwenden diese Regel, sodass `if items:` prüft, ob die Liste nicht leer ist, und `not name` prüft, ob die Zeichenkette leer ist; es ist nicht nötig, `len(items) > 0` oder `name == ""` zu schreiben.

---

Weil `if value:` den Wahrheitswert bereits anwendet, ist ein Vergleich mit `== True` oder `== False` unnötig und kann sogar falsch sein: `2 == True` ist `False`, obwohl `2` truthy ist. Prüfe den Wert selbst:
```python
values = [0, 1, "", "a", None, [], [0]]
for value in values:
    if value:
        print(value)  # 1, a, [0]
```

---

`and` und `or` geben nicht immer `True` oder `False` zurück: Sie geben einen ihrer **Operanden** zurück. `a and b` gibt `a` zurück, wenn es falsy ist, sonst `b`; `a or b` gibt `a` zurück, wenn es truthy ist, sonst `b`:
```python
print(0 and "x")       # 0
print(3 and "x")       # x
print("" or "none")    # none
print("hi" or "none")  # hi
```
Das Ergebnis ist genau dann truthy oder falsy, wenn der ganze Ausdruck es ist, weshalb `if a and b:` weiterhin funktioniert. Ein häufiger Anwendungsfall ist ein Standardwert: `name = user_input or "guest"`.

---

Logische Operatoren **schließen kurz**: `and` stoppt, sobald ein Operand falsy ist, und `or`, sobald einer truthy ist, weil das Ergebnis bereits bekannt ist. Die verbleibenden Operanden werden nie ausgewertet, sind es Funktionsaufrufe, werden sie also nicht ausgeführt:
```python
def check(n):
    print("checking", n)
    return n > 0

check(-1) and check(5)  # prints only "checking -1"
check(2) or check(-3)   # prints only "checking 2"
```

---

`==` vergleicht **Werte**; `is` vergleicht **Identität**, das heißt, ob beide Namen auf dasselbe Objekt verweisen. Zwei gleiche, separat erzeugte Listen sind `==`, aber nicht `is`:
```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # True False True
```
`is` ist für Singletons wie `None`, `True` und `False` gedacht: Schreibe `value is None` oder `value is not None`, niemals `value == None`, weil eine Klasse `==` definieren kann, um Beliebiges zurückzugeben. `is` mit Zahlen oder Zeichenketten zu verwenden ist unzuverlässig, und Python warnt davor.

---

Kurzschlussauswertung ist eine sichere Möglichkeit, eine Operation abzusichern (**Guard**), die bei manchen Werten fehlschlagen würde. In `word is not None and len(word) < 4` wird `len(word)` nur ausgeführt, wenn `word` nicht `None` ist, daher löst der Aufruf nie einen Fehler aus. Der Guard muss zuerst kommen:
```python
def is_short(word):
    return word is not None and len(word) < 4

print(is_short(None))   # False
print(is_short("cat"))  # True
```
Denke daran, dass `and` einen Operanden zurückgibt: `word and len(word) < 4` ergibt `None` für `None` und `""` für die leere Zeichenkette, nicht `False`. Wenn ein Boolean verlangt ist, sichere mit einem echten Vergleich ab.

---

Der `in`-Operator prüft die **Zugehörigkeit**: ob ein Element in einer Liste, einem Tupel oder einem Set ist, ob eine Teilzeichenkette in einer Zeichenkette ist oder ob ein Schlüssel in einem Wörterbuch ist. `not in` ist seine Negation:
```python
fruits = ["apple", "pear"]
print("pear" in fruits)          # True
print("kiwi" not in fruits)      # True
print("ex" in "text")            # True
print("age" in {"name": "Ada"})  # False, only keys are checked
```
Beide geben einen Boolean zurück und lesen sich wie Englisch, was sie zur bevorzugten Art macht, Zugehörigkeit zu prüfen, statt eine Schleife zu schreiben.
