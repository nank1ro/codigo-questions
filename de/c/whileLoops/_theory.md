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
Offensichtlich würden wir bei langen Anweisungen viel Zeit damit verbringen, den Code zu schreiben, aber zum Glück können wir Schleifen verwenden.
Lernen wir die `while` Schleife kennen und erhalten die gleiche Ausgabe wie oben.
```c
int count = 2;
while (count <= 5) {
    printf("%d seconds\n", count);
    count++;
}
```
Also haben wir eine Variable `count` erstellt und `2` als Anfangswert zugewiesen.
Dann haben wir die `while` Anweisung verwendet, die den Codeblock ausführt, solange die Bedingung `count <= 5` `true` ist.
Innerhalb des Codeblocks sollten wir **NICHT** vergessen, die Zeile `count++;` hinzuzufügen.
Sie erhöht den `count` Wert, sonst wird unsere Schleife unendlich

---

To control the times a `while` loop repeats, we start with a variable set to a number.
We call this variable a counter variable

---

Then, we use a comparison in the condition to compare the `counter` variable to a number.

---

Inside the block of code, in order to stop the `while` loop, we increment the `counter` variable.

---

The order you write code affects the output.
