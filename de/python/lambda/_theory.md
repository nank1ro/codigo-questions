Manchmal brauchst du eine winzige Funktion nur ein einziges Mal, zum Beispiel um eine Zahl zu verdoppeln.
Dafür einen ganzen `def`-Block zu schreiben, wirkt umständlich.
Python bietet eine kürzere Form: den **lambda**-Ausdruck, eine _anonyme_ Funktion, die auf einer einzigen Zeile geschrieben wird:
```python
lambda x: x * 2
```
Die Syntax lautet `lambda parameter: ausdruck`.
Eine lambda hat keinen Namen, aber du kannst sie in einer Variablen speichern und wie jede andere Funktion aufrufen:
```python
double = lambda x: x * 2
print(double(4))  # 8
```

---

Beachte, dass der Rumpf der lambda kein `return`-Schlüsselwort hat.
Der Rumpf ist ein **einzelner Ausdruck**, und sein Wert wird automatisch zurückgegeben:
```python
square = lambda n: n * n
print(square(3))  # 9
```

---

Eine lambda kann **mehr als einen Parameter** nehmen.
Trenne sie mit Kommas, genau wie in einer `def`-Funktion:
```python
power = lambda base, exp: base ** exp
print(power(2, 3))  # 8
```

---

Da der Rumpf ein einzelner Ausdruck sein muss, **kann eine lambda keine Anweisungen enthalten**.
Kein `return`, keine `if`-Blöcke, keine Schleifen, keine Zuweisungen:
```python
# SyntaxError
increment = lambda x: return x + 1
```
Wenn du etwas davon brauchst, schreibe stattdessen eine normale `def`-Funktion.

---

lambda-Parameter unterstützen auch **Standardwerte**:
```python
greet = lambda name="World": f"Hello, {name}!"
print(greet())       # Hello, World!
print(greet("Ana"))  # Hello, Ana!
```

---

Du musst eine lambda nicht einmal speichern: du kannst sie **sofort aufrufen**.
Setze die lambda in Klammern und füge dann die Argumente hinzu:
```python
print((lambda x: x + 1)(4))  # 5
```

---

lambdas glänzen wirklich als **Argumente für andere Funktionen**.
`sorted()` akzeptiert einen `key`-Parameter: eine Funktion, die auf jedes Element angewendet wird, und deren Ergebnis die Reihenfolge bestimmt.
Eine lambda passt hier perfekt:
```python
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana']
```

---

Die `key`-lambda kann einen beliebigen Teil eines Elements auswählen.
Bei einer Liste von Listen sortiert `lambda p: p[1]` nach dem zweiten Element jeder inneren Liste.

---

`map()` wendet eine Funktion auf **jedes Element** einer Liste an.
Sie gibt ein spezielles _map-Objekt_ zurück, also setze es in `list()`, um die Werte zu sehen:
```python
nums = [1, 2, 3]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6]
```

---

`filter()` behält nur die Elemente, für die die Funktion `True` zurückgibt:
```python
nums = [5, 12, 8, 20]
big = list(filter(lambda n: n > 10, nums))
print(big)  # [12, 20]
```

---

Ein `map`-Objekt direkt auszugeben zeigt nicht seine Werte: du erhältst etwas wie `<map object at 0x7f2b1c>`.
Erst `list()` (oder eine Schleife) macht daraus die erwarteten Werte.

---

lambdas sind nicht auf eingebaute Funktionen beschränkt: **deine eigenen Funktionen** können eine Funktion als Parameter nehmen und aufrufen.
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 3))  # 30
```

---

Auch `max()` und `min()` akzeptieren eine `key`-Funktion, genau wie `sorted()`:
```python
words = ["hi", "hello", "hey"]
print(max(words, key=lambda w: len(w)))  # hello
```

---

**Wann solltest du `def` bevorzugen?**
Eine lambda ist ideal für eine kurze, einmalig verwendete Funktion, die als Argument übergeben wird.
Wenn die Logik einen Namen, mehrere Zeilen, einen Docstring braucht oder an vielen Stellen wiederverwendet wird, ist eine `def`-Funktion klarer.
Ein letzter Trick: `sorted()` akzeptiert auch `reverse=True`, um zuerst die größten Werte zu erhalten:
```python
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]
```
