Manchmal hat eine Variable noch **keinen Wert** zum Speichern: ein Benutzer, der sich nicht angemeldet hat, eine Suche, die nichts gefunden hat, eine Einstellung, die nie gewählt wurde. Python stellt dies mit dem speziellen Wert `None` dar.
`None` ist ein Wert wie jeder andere: Du kannst ihn zuweisen, ausgeben und an Funktionen übergeben. Sein Typ ist `NoneType`, und es gibt genau **einen** `None` im ganzen Programm, sodass jedes `None`, das du schreibst, auf dasselbe Objekt verweist:
```python
winner = None
print(winner)                 # None
print(type(winner).__name__)  # NoneType
print(winner is None)         # True
```
`None` ist nicht `0`, nicht eine leere Zeichenkette und nicht `False`: Es ist ein eigener Wert, der "hier ist nichts" bedeutet.

---

Jeder Funktionsaufruf erzeugt einen Wert, selbst wenn die Funktion scheinbar nichts zurückgibt. Eine Funktion **ohne** `return`-Anweisung oder mit einem bloßen `return` gibt `None` zurück:
```python
def say_hello():
    print("hello")

result = say_hello()
print(result)  # None
```
Deshalb zeigt der Aufruf von `print(my_list.append(3))` `None`: `append` ändert die Liste an Ort und Stelle und gibt nichts zurück.
Eine Funktion, die nur eine Aktion ausführt (Ausgeben, Speichern, Ändern einer Liste), gibt normalerweise `None` zurück, während eine Funktion, die etwas berechnet, es explizit mit `return` zurückgeben muss.

---

Um zu prüfen, ob eine Variable `None` enthält, verwende `is` und `is not`, niemals `==`:
```python
if user is None:
    print("nobody logged in")
if user is not None:
    print("welcome")
```
`==` fragt "sind diese Werte *gleich*?", und jede Klasse kann diese Frage auf ihre eigene Weise beantworten, indem sie die Methode `__eq__` definiert. `is` fragt "sind dies *dasselbe Objekt*?", und nichts kann diese Antwort ändern.
Da es nur ein `None` gibt, ist `is None` immer korrekt und etwas schneller, während `== None` bei Objekten mit einem eigenen `__eq__` eine überraschende Antwort liefern kann.

---

`None` gilt in einer Bedingung als **falsch**, daher ist `if not value:` `True`, wenn `value` `None` ist. Es ist verlockend, das als `None`-Prüfung zu verwenden, aber derselbe Test ist auch für `0`, `""`, `[]` und jeden anderen leeren Wert `True`:
```python
count = 0
if not count:
    print("missing?")   # printed, but 0 is a real value!
```
Wenn "kein Wert" und "leerer Wert" unterschiedlich behandelt werden müssen, prüfe zuerst `is None` und dann den Wahrheitswert:
```python
if count is None:
    print("no count yet")
elif not count:
    print("count is zero")
```
Verwende `if not value:` nur, wenn du `None` und leere Werte wirklich gleich behandeln willst.

---

Ein Parameter kann einen **Standardwert** haben, der verwendet wird, wenn der Aufrufer das Argument weglässt. `None` ist der übliche Standardwert für "nicht angegeben":
```python
def greet(name=None):
    if name is None:
        name = "stranger"
    print("Hello, " + name)

greet()       # Hello, stranger
greet("Ada")  # Hello, Ada
```
Das ist bei Listen und Wörterbüchern wichtig. Ein Standardwert wird **einmal** ausgewertet, wenn die Funktion definiert wird, daher teilt sich `def add(item, items=[])` dieselbe Liste über jeden Aufruf, der `items` weglässt, und die Elemente stapeln sich. Die Lösung ist, als Standardwert `None` zu verwenden und innerhalb der Funktion eine neue Liste zu erstellen:
```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

Das Lesen eines fehlenden Schlüssels aus einem Wörterbuch mit `[]` löst einen `KeyError` aus. Die Methode `get` ist die sichere Alternative: Sie gibt den Wert zurück, wenn der Schlüssel existiert, und `None`, wenn nicht:
```python
ages = {"Ada": 36}
print(ages.get("Ada"))    # 36
print(ages.get("Grace"))  # None
```
`get` akzeptiert ein zweites Argument, den Wert, der **statt** `None` zurückgegeben wird, wenn der Schlüssel fehlt:
```python
print(ages.get("Grace", 0))  # 0
```
Das ist die häufigste Art, wie `None` im alltäglichen Code auftaucht: eine Suche, die nichts gefunden hat.

---

Eine Funktion, die eine Zahl **oder** `None` zurückgibt, sollte das in ihrer Signatur angeben. Ein **Type Hint** ist eine Annotation, die den erwarteten Typ dokumentiert: `name: str` für einen Parameter und `-> int` für den Rückgabewert. Python erzwingt keine Hints, aber Editoren und Leser verlassen sich darauf:
```python
def parse_age(text: str) -> int | None:
    if text.isdigit():
        return int(text)
    return None
```
`int | None` liest sich als "ein `int` oder `None`". Die ältere Schreibweise `Optional[int]` aus dem Modul `typing` bedeutet genau dasselbe, und du wirst ihr in bestehendem Code noch begegnen.
Immer wenn du `| None` in einer Signatur siehst, denke daran, das Ergebnis zu prüfen, bevor du es verwendest.

---

Funktionen, die `None` erhalten können, beginnen oft mit einem **Guard**: einem `if`, das früh zurückkehrt, wenn es nichts zu bearbeiten gibt. Der Rest der Funktion kann dann davon ausgehen, dass der Wert vorhanden ist, ohne alles in einem `else` zu verschachteln:
```python
def shout(text):
    if text is None:
        return None
    return text.upper() + "!"
```
Guards kommen zuerst, in der Reihenfolge, in der die Prüfungen stattfinden müssen: Du kannst `text.split()` nicht aufrufen, bevor du weißt, dass `text` nicht `None` ist.

---

Der Operator `or` gibt nicht `True` oder `False` zurück: Er gibt seinen **linken** Operanden zurück, wenn dieser wahr ist, und sonst seinen **rechten** Operanden. Das liefert eine Einzeiler-Möglichkeit, einen Fallback bereitzustellen:
```python
name = None
print(name or "anonymous")  # anonymous
name = "Ada"
print(name or "anonymous")  # Ada
```
Der Haken ist, dass `or` auf den Wahrheitswert schaut, nicht auf `None`: `0`, `""` und `[]` werden ebenfalls durch den Fallback ersetzt. Verwende `x or fallback` nur, wenn jeder leere Wert ebenfalls zum Fallback werden soll.

---

Wenn `0` oder `""` erhalten bleiben und nur `None` ersetzt werden soll, braucht der Fallback eine explizite `is None`-Prüfung. Die kompakte Form ist der **bedingte Ausdruck**, `a if condition else b`, der zu `a` auswertet, wenn die Bedingung wahr ist, und sonst zu `b`:
```python
timeout = 0
seconds = timeout if timeout is not None else 30
print(seconds)  # 0, not 30
```

---

Eine Liste kann `None` neben echten Werten enthalten, zum Beispiel Messungen, die fehlgeschlagen sind, oder Antworten, die übersprungen wurden. Die meisten Operationen akzeptieren es nicht: `sum([8, None])` löst einen `TypeError` aus.
Filtere die `None`-Werte mit einer List Comprehension heraus, deren Bedingung `is not None` ist:
```python
readings = [3, None, 5]
valid = [r for r in readings if r is not None]
print(valid)  # [3, 5]
```
Stattdessen `if r` zu verwenden, würde auch jede `0` verwerfen, also sei explizit, wenn Null eine gültige Messung ist.

---

Eine Suche gefolgt von einer `None`-Prüfung braucht normalerweise zwei Zeilen: eine zum Speichern des Ergebnisses, eine zum Testen. Der Operator für **Zuweisungsausdrücke** `:=`, mit dem Spitznamen *Walrus*, weist einen Wert **innerhalb** eines Ausdrucks zu, sodass beide Schritte in das `if` passen:
```python
ages = {"Ada": 36}
if (age := ages.get("Ada")) is not None:
    print(age + 1)  # 37
```
Die Klammern sind erforderlich: Ohne sie würde `:=` versuchen, den ganzen Vergleich zuzuweisen. Nach dem `if` bleibt `age` wie jede andere Variable verfügbar.

---

Nicht jedes "nicht gefunden" wird mit `None` gemeldet. Einige ältere Funktionen geben stattdessen einen **Sentinel**-Wert zurück, einen normalen Wert, dem eine besondere Bedeutung gegeben wird. Die Zeichenkettenmethode `find` gibt den Index einer Teilzeichenkette zurück, oder `-1`, wenn sie fehlt:
```python
print("banana".find("n"))  # 2
print("banana".find("x"))  # -1
```
Die Funktion `re.match(pattern, text)` aus dem Modul `re` prüft, ob `text` mit `pattern` beginnt, und gibt ein Match-Objekt zurück, oder `None`, wenn sie nicht übereinstimmt.
`None` ist die sicherere Konvention: `-1` ist ein gültiger Index, daher gibt `text[text.find("x")]` stillschweigend das letzte Zeichen zurück, statt zu scheitern, während die Verwendung von `None` als Index sofort einen Fehler auslöst.

---

`None` kann nicht geordnet werden: `None < 1` löst einen `TypeError` aus, weil Python nicht weiß, ob "nichts" kleiner oder größer als eine Zahl ist.
Das ist wichtig, wenn `None` als Startwert einer Suche verwendet wird, etwa "der bisher beste Wert, falls vorhanden". Jeder Vergleich muss durch eine `is None`-Prüfung geschützt sein, die **zuerst** steht, damit `or` kurzschließt und der Vergleich übersprungen wird, wenn es noch nichts zu vergleichen gibt:
```python
if best is None or value > best:
    best = value
```
Andersherum geschrieben würde `value > best or best is None` in der ersten Iteration mit `None` vergleichen und abstürzen.
