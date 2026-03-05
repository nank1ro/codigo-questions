Listen sind ein Datentyp, mit dem Sie eine Sammlung verschiedener Informationen als Sequenz unter einem einzelnen Variablennamen speichern können.
Eine Liste speichert mehrere Werte beliebigen Typs und verwendet **Indizes**, um diese Werte zu unterscheiden.
Sie können Elemente einer Liste mit einem Ausdruck der folgenden Form zuweisen:
```python
list_name = [item1, item2]
```

---

Sie können auf ein einzelnes Element der Liste über seinen Index zugreifen.
Ein Index ist wie eine Adresse, die die Position des Elements in der Liste angibt.
Der Index wird direkt nach dem Listennamen in Klammern angezeigt, wie folgt:
```python
list_name[index]
```

Listenindizes beginnen mit `0`, **nicht** `1`! Sie greifen auf das erste Element einer Liste wie folgt zu: `list_name[0]`.
Das zweite Element einer Liste ist am Index 1: `list_name[1]`.

---

Ein Listenindex verhält sich wie jeder andere Variablenname! Er kann zum Zugreifen und zum Zuweisen von Werten verwendet werden.
Sie haben gesehen, wie Sie auf einen Listenindex wie folgt zugreifen:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] # Gets the value "Jeremiah"
```
So funktioniert eine Zuordnung:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] = "Jordan"
names[0] # Gets the new value "Jordan"
```

---

Wie Strings haben auch Listen eine **Länge**.
Die Länge einer Liste ist die Anzahl der Elemente, die sie enthält

---

Eine Liste muss keine feste Länge haben.
Sie können jederzeit Elemente am Ende einer Liste hinzufügen!
Um ein Element zu einer Liste hinzuzufügen, verwenden wir das Schlüsselwort `append`:
```python
>>> letters = ["a", "b"]
>>> letters.append("c")
>>> print(letters)
['a', 'b', 'c']
```

---

Manchmal möchten Sie nur auf einen Teil einer Liste zugreifen.
Betrachten Sie den folgenden Code:
```python
>>> numbers = [1, 2, 3, 4]
>>> slice = numbers[1:3]
>>> print(slice)
[2, 3]
```
Zuerst erstellen wir eine Liste namens `numbers`.
Dann extrahieren wir einen Abschnitt der Liste und speichern ihn in der Slice-Liste.
Dies tun wir, indem wir die Indizes definieren, die wir nach dem Listennamen einschließen möchten: `numbers[1:3]`.
In Python schließen wir bei der Angabe eines Listenabschnitts auf diese Weise das Element mit dem ersten Index `1` ein, schließen aber das Element mit dem zweiten Index `3` aus.

---

Sie können einen String genau wie eine Liste aufteilen! Tatsächlich können Sie Strings als Listen von Zeichen betrachten: jedes Zeichen ist ein nachfolgendes Element in der Liste, beginnend mit Index `0`.
```python
list_name[:2]
# Grabs the first two items
list_name[3:]
# Grabs the fourth through last items
```
Wenn Ihr Listenschnitt das erste oder letzte Element einer Liste (oder eines Strings) enthält, muss der Index für dieses Element nicht angegeben werden.

---

Listenelemente können von beliebigem Typ sein:
```python
list_name = ["one", 2, True]
```
Tatsächlich haben wir oben der Reihe nach einen String, eine Ganzzahl und einen booleschen Wert.
Aber wir können auch Listen mit Listen haben!

---

Manchmal müssen Sie nach einem Element in einer Liste suchen.
In Python können wir die Methode `index()` verwenden:
```python
>>> names = ["Trevor", "Zac", "Glenn"]
>>> print(names.index("Zac"))
1
```
Der Code oben gibt den ersten Index aus, der den String `"Zac"` enthält, in diesem Fall `1`.
Wir können auch Elemente an einem bestimmten Index in eine Liste einfügen, indem wir die Methode `insert()` verwenden:
```python
>>> names.insert(1, "Ali")
>>> print(names)
['Trevor', 'Ali', 'Zac', 'Glenn']
```
Der Code oben fügt `"Ali"` am Index `1` ein, wodurch alles nach diesem Index um 1 nach unten verschoben wird

---

In Python können wir auf sehr einfache Weise durch eine Liste iterieren, indem wir die Schlüsselwörter `for..in` verwenden:
```python
>>> numbers = [1, 2, 3]
>>> for num in numbers:
>>>     print(num)
1
2
3
```
Ein Variablenname folgt dem Schlüsselwort `for`, dem wird der Wert jedes Listenelements nacheinander zugewiesen.

---

**Tupel** sind wie Listen, aber viel schneller.
Die Werte eines Tupels können jedoch nicht geändert werden.
Wir verwenden Tupel normalerweise für **schreibgeschützte** Daten, die während der Programmausführung konstant bleiben.
Um ein Tupel zu erstellen, verwenden wir die runden Klammern `()`

---

Es kann vorkommen, dass wir unser Tupel in eine Liste konvertieren möchten.
Um dies zu tun, können wir die Funktion `list()` verwenden

---

Gleichermaßen können wir eine Liste in ein Tupel konvertieren
