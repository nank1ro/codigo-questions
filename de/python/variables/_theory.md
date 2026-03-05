Variablen sind Container zum Speichern von Datenwerten.
Jede Variable in Python ist ein Objekt und im Gegensatz zu anderen Programmiersprachen hat Python keinen Befehl zum Deklarieren einer Variable.
Um eine Variable zu erstellen, müssen wir ihr einen **Namen** geben, wobei zu beachten ist, dass er keine Leerzeichen enthalten darf.
Eine Variable wird in dem Moment erstellt, in dem Sie ihr zum ersten Mal einen Wert zuweisen.
Ein Beispiel für die Erstellung einer Variable namens `x` ist:
```python
x = 1
```
Auf diese Weise haben wir der Variable namens `x` den Wert `1` zugewiesen.
Wenn wir die Variable `x` drucken, erhalten wir die Zahl `1` zurück:
```python
>>> print(x)
1
```

---

Variablen werden so genannt, weil sich der Wert, den sie speichern, ändern kann.
Wir können `x` aktualisieren, indem wir `=` verwenden und ihm einen neuen Wert geben.
```python
>>> x = 1
>>> print(x)
1
>>> x = 2
>>> print(x)
2
```

---

Wir können auch Variablen die Werte anderer Variablen geben. Hier können wir der Variable `y` den Wert von `x` geben
```python
>>> x = 5
>>> y = x
>>> print(y)
5
```

---

Wenn wir eine Variable aktualisieren, vergisst sie ihren vorherigen Wert. Hier können wir die Variable `x` zweimal anzeigen und sehen, wie ihr Wert aktualisiert wird.
```python
>>> x = 5
>>> print(x)
5
>>> x = 10
>>> print(x)
10
```

---

String-Variablen können mit einfachen oder doppelten Anführungszeichen deklariert werden:
```python
>>> x = "May"
>>> x = 'May'
```
Beide sind dasselbe.

---

Wenn wir einen Variablennamen mit mehreren Wörtern haben, verwenden wir **snake case**.
Das bedeutet, dass wir `_` verwenden, um die zusätzlichen Wörter zu verbinden.
