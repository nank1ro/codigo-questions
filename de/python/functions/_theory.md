Du hast vielleicht schon überlegt, wie du ein Stück Code wiederverwenden könntest, nur mit einigen anderen Werten.
Anstatt den ganzen Code neu zu schreiben, ist es viel sauberer, eine Funktion zu definieren, die dann wiederholt verwendet werden kann.
In Python verwenden wir das Schlüsselwort `def` gefolgt vom Namen der Funktion:
```python
def say_hi():
    print("Hello!")
```

---

Die Klammern in der __Funktionsdefinition__ müssen nicht leer sein.
Darin können wir Parameter angeben

---

Manchmal möchten wir, dass eine Funktion einen Wert __zurückgibt__.
Nun ja, es gibt das Schlüsselwort `return`

---

In Funktionen können wir einen _optionalen Kommentar_ hinzufügen, der erklärt, was die Funktion tut:
```python
"""
Prints 'Hello World' to the console.
"""
```
