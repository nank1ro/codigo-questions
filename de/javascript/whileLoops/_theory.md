Oft in der Programmierung müssen wir einen Codeblock wiederholen, zum Beispiel:
```javascript
console.log("2 seconds");
console.log("3 seconds");
console.log("4 seconds");
console.log("5 seconds");
```
Dies erzeugt die folgende Ausgabe:
```javascript
2 seconds
3 seconds
4 seconds
5 seconds
```
Offensichtlich würden wir für lange Anweisungen viel Zeit mit dem Schreiben des Codes verbringen, aber glücklicherweise können wir Schleifen verwenden.
Lernen wir die `while`-Schleife und erhalten dieselbe Ausgabe wie oben.
```javascript
var count = 2;
while (count <= 5) {
    console.log(`${count} seconds`);
    count += 1;
}
```
Wir haben also eine Variable `count` mit dem Anfangswert `2` erstellt.
Dann haben wir die `while`-Anweisung verwendet, die den Codeblock ausführt, solange die Bedingung `count <= 5` `true` ist.
Innerhalb des Codeblocks dürfen wir die Zeile `count += 1` nicht vergessen.
Sie erhöht den Wert von `count`, andernfalls wird unsere Schleife unendlich

---

Um zu kontrollieren, wie oft eine `while`-Schleife wiederholt wird, beginnen wir mit einer Variablen, die auf eine Zahl gesetzt ist.
Wir nennen diese Variable eine Zählervariable

---

Dann verwenden wir einen Vergleich in der Bedingung, um die Variable `counter` mit einer Zahl zu vergleichen.

---

Innerhalb des Codeblocks erhöhen wir die Variable `counter`, um die `while`-Schleife zu stoppen.

---

Die Reihenfolge, in der Sie Code schreiben, beeinträchtigt die Ausgabe.

---

In JavaScript haben wir auch die **do-while**-Variation der `while`-Schleife.
Sie führt zuerst einen einzelnen Durchlauf durch den Schleifenblock aus, _bevor_ die Bedingung der Schleife berücksichtigt wird.
Dann wiederholt sie die Schleife, bis die Bedingung `false` ist.
