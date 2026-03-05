**Dictionaries** sind ähnlich wie Listen und Tupel, aber du greifst auf Werte zu, indem du einen *Schlüssel* anstelle eines Index suchst.
Ein Schlüssel kann ein beliebiger String oder eine beliebige Zahl sein.
Dictionaries sind in geschwungenen Klammern eingeschlossen, wie folgt:
```python
d = {"key1": 1, "key2": 2, "key3": 3}
```
Dies ist ein Dictionary mit dem Namen `d` mit drei *Schlüssel-Wert-Paaren*.
Der Schlüssel `key1` verweist auf den Wert `1`, `key2` auf `2` und so weiter.

---

Der Zugriff auf Dictionary-Werte nach Schlüssel ist genau wie der Zugriff auf Listenwerte nach Index:
```python
user['age']
# gets the age value from the user dictionary
```

---

Wie Listen sind Dictionaries _mutable_.
Das bedeutet, sie können nach ihrer Erstellung geändert werden.
Ein Vorteil davon ist, dass wir neue _Schlüssel-Wert-Paare_ zum Dictionary nach seiner Erstellung hinzufügen können, wie folgt:
```python
dict_name[new_key_name] = new_value
```

---

Die Länge `len()` eines Dictionary ist die Anzahl der _Schlüssel-Wert-Paare_, die es hat.
Jedes Paar zählt nur einmal, auch wenn der Wert eine Liste ist. (Richtig: du kannst auch Listen in Dictionaries einfügen!)

---

Da Dictionaries mutable sind, können sie auf viele Arten geändert werden. Elemente können mit dem `del`-Befehl aus einem Dictionary entfernt werden:
```python
del dict_name[key_name]
```
entfernt den Schlüssel `key_name` und seinen zugehörigen Wert aus dem Dictionary.

---

Was ist, wenn wir alle Schlüssel des Dictionary auflisten möchten?
Nun, da ist die Methode `keys()`.

---

Was ist, wenn wir alle Werte des Dictionary auflisten möchten?
Nun, da ist die Methode `values()`.

---

Wie bei Listen können wir mit den Schlüsselwörtern `for..in` zwischen Dictionary-Elementen schleifen
Um sowohl den Schlüssel als auch den Wert in der Schleife zu erhalten, können wir die Methode `items()` verwenden:
```python
for key, value in dict_name:
    print(key, value)
```

---

Wir können auch das Schlüsselwort `in`, das wir in Schleifen verwendet haben, verwenden, um zu bestimmen, ob ein Dictionary einen bestimmten __Schlüssel__ enthält

---

Um Werte zu einem Dictionary zu __hinzufügen__ oder zu __ändern__, können wir auch die Methode `update()` mit den _Schlüssel-Wert-Paaren_, die wir hinzufügen möchten, in Klammern verwenden

---

Was ist, wenn wir einen Wert aus einem Dictionary __entfernen__ möchten?
Es gibt die Methode `pop()`:
```python
dict_name.pop("key_name")
```
