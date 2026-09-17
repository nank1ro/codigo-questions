Die Entscheidungsfindung ist erforderlich, wenn wir Code nur ausführen möchten, wenn eine bestimmte Bedingung erfüllt ist.
Nehmen wir an, wir möchten nur draußen spielen, wenn das Wetter schön ist.
In der Programmierung können wir eine boolesche Variable `nice_weather` speichern und die Aktion, draußen zu spielen, mit `if` ausführen, wenn diese Variable `true` ist, wie folgt:
```c
bool nice_weather = true;
if (nice_weather) {
    // draußen spielen
}
```

---

Lass uns mit dem vorherigen Beispiel fortfahren.
```c
bool nice_weather = true;
if (nice_weather) {
    // draußen spielen
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
    // draußen spielen
} else {
    // zu Hause bleiben
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

---

Zeit, die Syntax der `if`-Anweisung in die Praxis umzusetzen: das Schlüsselwort, eine Bedingung in Klammern und ein Codeblock, der in geschwungene Klammern eingeschlossen ist.
```c
if (condition) {
    // wird ausgeführt, wenn die Bedingung wahr ist
}
```

---

Die booleschen Literale in C sind `true` und `false`: kleingeschrieben, ohne Anführungszeichen, und definiert durch `<stdbool.h>`, statt fest in die Sprache eingebaut zu sein. `True` lässt sich als Bedingung nicht kompilieren — nur die kleingeschriebene Form funktioniert, und wenn sie `true` ist, wird der Block ausgeführt.

---

C kennt keinen eigenen booleschen Test: Eine Bedingung ist wahr, sobald ihr Wert etwas anderes als null ist. `false` aus `<stdbool.h>` ist schlicht `0`, weshalb ein davon abhängiger Block nie ausgeführt wird.

---

Eine `if`-Anweisung in C besteht aus drei Teilen: dem Schlüsselwort `if`, einer Bedingung in Klammern und einem Block in geschwungenen Klammern. Die Klammern sind erforderlich — an ihnen erkennt der Compiler, wo die Bedingung endet.

---

Jede bedingte Anweisung beginnt mit einem Schlüsselwort, das dem Compiler mitteilt, dass eine Bedingung geprüft werden muss, bevor entschieden wird, was als Nächstes ausgeführt wird.

---

Eine `true`-Bedingung ist immer wahr, also wird der Block ausgeführt und sein `printf` läuft genau so ab, wie geschrieben.

---

Eine `false`-Bedingung ist nie wahr, also wird der Block vollständig übersprungen und nichts darin wird ausgeführt.

---

Bedingungen sind die Werte, die eine `if`-Anweisung prüft: Ist eine Bedingung `true`, wird der Block ausgeführt, ist sie `false`, wird er übersprungen.

---

Die öffnende geschwungene Klammer kann in derselben Zeile wie die Bedingung stehen oder in der Zeile darunter. C ignoriert den Zeilenumbruch, sodass beide Stile zu genau demselben Programm kompiliert werden.

---

Die Klammern um eine Bedingung sind Teil der `if`-Syntax von C, keine optionale Gruppierung: `if true { ... }` lässt sich nicht kompilieren.

---

Ein in Anführungszeichen gesetztes `"false"` ist eine Zeichenkette, kein boolescher Wert — und eine Zeichenkette ist in einer Bedingung eine von null verschiedene Adresse, was als wahr zählt. Nur das nicht in Anführungszeichen gesetzte `false` verhindert, dass der Block ausgeführt wird.

---

Der Abstand zwischen den Teilen einer `if`-Zeile ist in C frei wählbar: `if(true){` und `if (true) {` sind für den Compiler dieselbe Anweisung, es zählt also nur die Reihenfolge der Teile.

---

Ein Codeblock ist nicht auf eine Anweisung beschränkt. Jede Anweisung zwischen den geschwungenen Klammern wird der Reihe nach ausgeführt, in der Reihenfolge, in der sie geschrieben ist.

---

Eine boolesche Variable kann direkt als Bedingung verwendet werden, ohne dass ein Vergleich nötig ist. Da `online` bereits `true` enthält, reicht `if (online)` allein aus, um den Block auszuführen.

---

Eine `bool`-Variable funktioniert als Bedingung, weil `if` nur den Wert betrachtet, der in diesem Moment darin gespeichert ist. Mit `false` in `online` verhält sich `if (online)` genau wie `if (false)`.

---

Nur der Code zwischen den geschwungenen Klammern einer `if`-Anweisung ist bedingt. Alles, was nach der schließenden Klammer steht, wird unbedingt ausgeführt, unabhängig davon, wie die Bedingung war.

---

Es gibt keine feste Grenze dafür, wie viele Anweisungen ein Codeblock enthalten kann — eine Zeile oder hundert, sie werden alle zusammen ausgeführt, wenn die Bedingung `true` ist.

---

Eine boolesche Variable als Bedingung zu lesen, funktioniert genau wie ein Literal: Da `online` `true` enthält, wird der Block ausgeführt und sein `printf` läuft.

---

Enthält `online` stattdessen `false`, ist die Bedingung falsch, also wird der Block vollständig übersprungen und nichts innerhalb dieser geschwungenen Klammern wird ausgegeben.
