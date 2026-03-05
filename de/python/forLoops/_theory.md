Wir wissen, wie man Code mit einer `while`-Schleife wiederholt.
Wie dieses Programm Anweisungen wiederholt, um `hello` anzuzeigen
```python
counter = 0

while counter < 5:
    print("hello")
    counter += 1
```
Aber wir können das Gleiche mit `for`-Schleifen tun:
```python
for i in range(5):
    print("hello")
```

---

In einer `for`-Schleife können wir mit der `range()`-Funktion angeben, wie oft unsere Schleife ausgeführt werden soll

---

Das Hinzufügen einer Zahl wie `5` in der `range()`-Funktion bedeutet, dass die Schleife 5 Mal über den Codeblock durchlaufen wird, von `0` bis `4`

---

Die Variable `i` ist die Zählervariable.
Wir können ihr den Namen geben, den wir möchten.
Sie zählt, bei welcher Wiederholung der Schleife wir uns befinden

---

Die `range()`-Funktion gibt eine Zahlenfolge zurück, beginnend standardmäßig bei 0, erhöht sich um 1 (standardmäßig) und stoppt vor einer angegebenen Zahl.
Dies ist die Syntax der Funktion:
```python
range(start, stop, step)
```
`start` und `step` sind optional, während `stop` erforderlich ist
