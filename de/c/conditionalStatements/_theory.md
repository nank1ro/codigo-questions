Die Entscheidungsfindung ist erforderlich, wenn wir Code nur ausführen möchten, wenn eine bestimmte Bedingung erfüllt ist.
Nehmen wir an, wir möchten nur draußen spielen, wenn das Wetter schön ist.
In der Programmierung können wir eine boolesche Variable `nice_weather` speichern und die Aktion, draußen zu spielen, mit `if` ausführen, wenn diese Variable `true` ist, wie folgt:
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```

---

Lass uns mit dem vorherigen Beispiel fortfahren.
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```
Wir haben gesehen, dass die `if`-Anweisung den Codeblock nur ausführt, wenn die Bedingung `true` ist.
Ein weiterer wichtiger Punkt sind die **geschwungenen Klammern** `{}`, die einen Codeblock angeben.

---

Wir haben gerade gesehen, wie man einen Codeblock ausführt, wenn eine Bedingung eintritt. Jetzt schauen wir uns an, wie man einen anderen Codeblock ausführt, wenn die erste Bedingung fehlschlägt.
Wir spielen draußen, wenn das Wetter schön ist; ansonsten bleiben wir zu Hause.
In C können wir die `else`-Anweisung verwenden, wie folgt:
```c
bool nice_weather = false;
if (nice_weather) {
    // play outside
} else {
    // stay home
}
```

---

Nehmen wir an, wir haben eine weitere Bedingung zu prüfen, wie in diesem Beispiel:
```c
int num = 3;
if (num == 2) {
    printf("the number is 2\n");
} else if (num == 3) {
    printf("the number is 3\n");
} else {
    printf("do something else\n");
}
```
und die Ausgabe dieses Codes ist `the number is 3`.
Zunächst prüfen wir, ob die Zahl gleich 2 ist, was falsch ist.
Also fahren wir mit der zweiten Anweisung fort und prüfen, ob `num` gleich 3 ist. Da dies wahr ist, führen wir den folgenden Codeblock aus, indem wir `the number is 3` ausgeben.

---

Wir können so viele `else if`-Anweisungen hinzufügen, wie wir möchten. Es gibt keine Grenzen.
```c
int num = 4;
if (num == 2) {
    printf("the number is 2");
} else if (num == 3) {
    printf("the number is 3");
} else if (num == 4) {
    printf("the number is 4");
} else if (num == 5) {
    printf("the number is 5");
} else if (num == 6) {
    printf("the number is 6");
}
```
und die Ausgabe dieses Codes ist `the number is 4`.

---

Wir können auch eine bedingte Anweisung (`if`, `else if` oder `else`) in einer anderen bedingten Anweisung verschachteln, um eine komplexere Struktur zu schaffen.
```c
int num = 4;
if (num < 3) {
    printf("the number is lower than 3\n");
} else {
    if (num == 3) {
        printf("the number is 3\n");
  } else if (num == 4) {
        printf("the number is 4\n");
  } else {
        printf("the number is greather than 4\n");
  }
}
```
und die Ausgabe dieses Codes ist `the number is 4`.
