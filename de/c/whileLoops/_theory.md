Oft in der Programmierung müssen wir einen Codeblock wiederholen, zum Beispiel:
```c
printf("2 seconds\n");
printf("3 seconds\n");
printf("4 seconds\n");
printf("5 seconds\n");
```
Dies erzeugt die folgende Ausgabe:
```c
2 seconds
3 seconds
4 seconds
5 seconds
```
Offensichtlich würden wir für lange Anweisungen viel Zeit damit verbringen, den Code zu schreiben, aber glücklicherweise können wir Schleifen verwenden.
Lernen wir die `while`-Schleife kennen und erhalten wir die gleiche Ausgabe wie oben.
```c
int count = 2;
while (count <= 5) {
    printf("%d seconds\n", count);
    count++;
}
```
Wir haben also eine Variable `count` mit dem Anfangswert `2` erstellt.
Dann haben wir die `while`-Anweisung verwendet, die den Codeblock ausführt, bis die Bedingung `count <= 5` `true` ist.
Innerhalb des Codeblocks sollten wir **NICHT** vergessen, die Zeile `count++;` hinzuzufügen.
Sie erhöht den `count`-Wert, ansonsten wird unsere Schleife unendlich

---

Um zu steuern, wie oft eine `while`-Schleife wiederholt wird, beginnen wir mit einer Variablen, die auf eine Zahl eingestellt ist.
Wir nennen diese Variable eine Zählervariable

---

Dann verwenden wir einen Vergleich in der Bedingung, um die Variable `counter` mit einer Zahl zu vergleichen.

---

Innerhalb des Codeblocks erhöhen wir die Variable `counter`, um die `while`-Schleife zu beenden.

---

Die Reihenfolge, in der Sie Code schreiben, beeinflusst die Ausgabe.
