Oftmals müssen wir in der Programmierung einen Codeblock wiederholen, zum Beispiel:
```swift
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
Dies erzeugt die folgende Ausgabe:
```swift
2 seconds
3 seconds
4 seconds
5 seconds
```
Offensichtlich würden wir bei längeren Anweisungen viel Zeit mit dem Schreiben von Code verbringen, aber glücklicherweise können wir Schleifen verwenden.
Lassen Sie uns die `while` Schleife lernen, um die gleiche Ausgabe wie oben zu erhalten.
```swift
var count = 2
while count <= 5 {
    print("\(count) seconds")
    count += 1
}
```
Wir haben eine Variable `count` mit dem Wert `2` erstellt, das ist der Anfangswert.
Dann haben wir die `while` Anweisung verwendet, die den Codeblock ausführt, bis die Bedingung `count <= 5` `true` ist.
Im Codeblock sollten wir **NICHT** vergessen, die Zeile `count += 1` hinzuzufügen.
Sie erhöht den Wert von `count`, sonst wird unsere Schleife endlos sein.

---

Um zu kontrollieren, wie oft eine `while` Schleife wiederholt wird, beginnen wir mit einer Variable, die auf eine Zahl gesetzt ist.
Wir nennen diese Variable eine Zählervariable.

---

Dann verwenden wir einen Vergleich in der Bedingung, um die `counter` Variable mit einer Zahl zu vergleichen.

---

Im Codeblock erhöhen wir die `counter` Variable, um die `while` Schleife zu stoppen.

---

Die Reihenfolge, in der Sie Code schreiben, beeinflusst die Ausgabe.

---

In Swift haben wir auch die **repeat-while** Variation der `while` Schleife.
Sie führt zunächst einen einzelnen Durchlauf durch den Schleifenblock durch, _bevor_ die Bedingung der Schleife berücksichtigt wird.
Dann wiederholt sie die Schleife, bis die Bedingung `false` ist.
Die __repeat-while__ Schleife in Swift ist analog zu einer __do-while__ Schleife in anderen Sprachen.
