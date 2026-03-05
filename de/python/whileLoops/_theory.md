Oft müssen wir in der Programmierung einen Codeblock wiederholen, zum Beispiel:
```python
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
Dies erzeugt die folgende Ausgabe:
```python
2 seconds
3 seconds
4 seconds
5 seconds
```
Offensichtlich würden wir bei langen Anweisungen viel Zeit damit verbringen, den Code zu schreiben, aber glücklicherweise können wir Schleifen verwenden.
Lassen Sie uns die `while`-Schleife erlernen und die gleiche Ausgabe wie oben erhalten.
```python
count = 2
while (count <= 5):
    print(f"{count} seconds")
    count += 1
```
Wir haben eine Variable `count` erstellt und `2`, den Anfangswert, zugewiesen.
Dann haben wir die `while`-Anweisung verwendet, die den Codeblock ausführt, bis die Bedingung `count <= 5` `True` ist.
Im Codeblock sollten wir die Zeile `count += 1` nicht vergessen.
Sie erhöht den Wert von `count`, andernfalls wird unsere Schleife unendlich sein

---

Um zu kontrollieren, wie oft eine `while`-Schleife wiederholt wird, beginnen wir mit einer Variablen, die auf eine Zahl gesetzt ist.
Wir nennen diese Variable eine Zählervariable

---

Dann verwenden wir einen Vergleich in der Bedingung, um die Variable `counter` mit einer Zahl zu vergleichen.

---

Im Codeblock erhöhen wir die Variable `counter`, um die `while`-Schleife zu stoppen.

---

Die Reihenfolge, in der Sie Code schreiben, beeinflusst die Ausgabe.
