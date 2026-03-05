Python ist eine objektorientierte Programmiersprache, was bedeutet, dass sie mit Programmierkonstrukten manipuliert, die als Objekte bezeichnet werden.
Man kann sich ein Objekt als eine einzelne Datenstruktur vorstellen, die sowohl Daten als auch Funktionen enthält; die Funktionen eines Objekts werden seine Methoden genannt.
Zum Beispiel, wenn du aufgerufen wird:
```python
dict_name.items()
```
Python prüft, ob `my_dict` eine `items()`-Methode hat (die alle Wörterbücher haben) und führt diese Methode aus, wenn sie sie findet.

---

Eine grundlegende Klasse besteht nur aus dem `class`-Schlüsselwort und dem Namen der Klasse, zum Beispiel:
```python
class ClassName:
    pass
```

---

Lassen Sie uns `pass` durch etwas anderes ersetzen.
Die Methode `__init__()` ist erforderlich für Klassen, und sie wird verwendet, um die Objekte, die sie erstellt, zu __initialisieren__.
`__init__()` nimmt immer mindestens ein Argument, `self`, an, das sich auf das zu erstellende Objekt bezieht.
Man kann sich `__init__()` als die Methode vorstellen, die jedes von der Klasse erstellte Objekt startet.

---

Natürlich kann die `__init__()`-Methode mehr Parameter als `self` verwenden

---

Das erste Argument `__init__()` wird verwendet, um sich auf das Instanzobjekt zu beziehen, und nach Konvention wird dieses Argument `self` genannt.
Wenn du zusätzliche Argumente hinzufügst (zum Beispiel ein `gender` und `legs` für dein Tier), wird das Setzen jedes dieser auf `self.gender` und `self.legs` im Body von `__init__()` dazu führen, dass, wenn du ein Instanzobjekt deiner `Animal`-Klasse erstellst, du jeder Instanz ein Geschlecht und Beine geben musst, und diese werden mit der besonderen Instanz verbunden, die du erstellst

---

Das Definieren einer Klasse erstellt kein Objekt.
Um das zu tun, müssen wir eine __Instanz__ einer Klasse erstellen

---

Wenn eine Klasse ihre eigenen Funktionen hat, werden diese Funktionen __Methoden__ genannt. Du hast bereits eine solche Methode gesehen: `__init__()`.
Aber du kannst auch deine eigenen Methoden definieren!
