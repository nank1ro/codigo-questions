Eine **Aufzählung** (`enum`) gibt einer Reihe verwandter Ganzzahlkonstanten Namen, sodass du `RED` statt einer nackten Zahl schreiben kannst.
Du deklarierst sie mit dem Schlüsselwort `enum`, einem Namen und der Liste der Konstanten zwischen geschweiften Klammern:
```c
enum Color { RED, GREEN, BLUE };
```
Jede Konstante ist eine Ganzzahl: Wenn du nichts anderes angibst, ist die erste `0` und jede folgende die vorherige plus eins, also ist `RED` `0`, `GREEN` `1` und `BLUE` `2`.
Da es Ganzzahlen sind, gibst du sie mit `%d` aus:
```c
printf("%d\n", GREEN);
// prints "1"
```

---

Die Nummerierung läuft automatisch für so viele Konstanten weiter, wie du auflistest: Die vierte Konstante ist `3`, die fünfte ist `4` und so weiter.
Die Namen werden üblicherweise in Großbuchstaben geschrieben, wie andere Konstanten auch, und sie müssen im gesamten Programm eindeutig sein: Zwei Aufzählungen können sich keinen Konstantennamen teilen.

---

Du kannst einer Konstante mit `=` auch einen expliziten Wert geben; die darauffolgenden Konstanten zählen ab diesem Wert weiter:
```c
enum Month { JAN = 1, FEB, MAR }; // FEB is 2, MAR is 3
```
Explizite Werte müssen weder aufeinanderfolgend noch aufsteigend sein: `enum Status { OK = 200, NOT_FOUND = 404 };` ist vollkommen gültig.

---

Eine Aufzählung ist auch ein Typ: Du kannst eine Variable dieses Typs deklarieren, indem du `enum` gefolgt vom Namen der Aufzählung schreibst, und ihr eine ihrer Konstanten zuweisen:
```c
enum Color favorite = GREEN;
```
Da die Konstanten Ganzzahlen sind, vergleichst du Aufzählungsvariablen mit den üblichen Operatoren:
```c
if (favorite == GREEN) {
    printf("Green it is\n");
}
```

---

Eine Aufzählung kann der Typ eines Funktionsparameters sein, genau wie `int`:
```c
int is_weekend(enum Day day) {
    return day == SAT || day == SUN;
}
```
Innerhalb der Funktion ist ein `switch` die natürliche Art, jede Konstante zu behandeln, da Aufzählungskonstanten direkt als `case`-Label verwendet werden können:
```c
switch (day) {
    case SAT: return 1;
    case SUN: return 1;
    default: return 0;
}
```

---

Wenn jeder Zweig eines `switch` eine Konstante behandelt, denk an das `break` danach, sonst läuft die Ausführung in den nächsten Zweig durch.
Ein `default`-Zweig ist nicht erforderlich, wenn du jede Konstante der Aufzählung abdeckst.

---

Eine Funktion kann auch eine Aufzählung zurückgeben; verwende einfach den Aufzählungstyp als Rückgabetyp und gib eine ihrer Konstanten zurück:
```c
enum Grade grade_for(int score) {
    if (score >= 60) {
        return PASS;
    }
    return FAIL;
}
```
Eine benannte Konstante zurückzugeben ist für den Aufrufer viel klarer als eine nackte `0` oder `1` zurückzugeben.

---

Jedes Mal `enum Color` zu schreiben ist umständlich. Mit `typedef` gibst du der Aufzählung einen kurzen Typnamen, und die Aufzählung selbst kann anonym bleiben:
```c
typedef enum { RED, GREEN, BLUE } Color;

Color favorite = BLUE;
```
Der neue Name `Color` wird für sich allein verwendet, ohne das Schlüsselwort `enum` davor.

---

Eine Aufzählungskonstante wird automatisch zu `int` konvertiert, also ist `int n = BLUE;` gültig und speichert `2`.
Den umgekehrten Weg erledigt eine **Typumwandlung**, indem du den Aufzählungstyp in Klammern vor die Ganzzahl schreibst:
```c
enum Color c = (enum Color)1; // c is GREEN
```
C prüft nicht, ob die Zahl zu einer Konstante passt: `(enum Color)7` kompiliert, obwohl keine Konstante `7` ist, also validiere Ganzzahlen, bevor du sie umwandelst.

---

Arithmetik mit einem Aufzählungswert ergibt ein einfaches `int`: `GREEN + 1` ist `2`, nicht `BLUE`.
Um das Ergebnis wieder in einer Aufzählungsvariable zu speichern oder aus einer Funktion zurückzugeben, wandle es in den Aufzählungstyp um:
```c
enum Color after_green = (enum Color)(GREEN + 1); // BLUE
```
Zusammen mit dem Restoperator `%` kannst du damit durch die Konstanten zyklen und zur ersten zurückspringen.

---

Ein gängiger Trick ist es, am Ende der Aufzählung eine zusätzliche Konstante hinzuzufügen, meist `COUNT` genannt: Da die Nummerierung bei `0` beginnt, entspricht ihr Wert genau der Anzahl der echten Konstanten davor.
```c
enum Day { MON, TUE, WED, DAY_COUNT }; // DAY_COUNT is 3
```
Dieser Wächterwert erlaubt es dir, über jede Konstante zu iterieren, ohne die Zahl fest zu codieren, und er bleibt korrekt, wenn du davor Konstanten hinzufügst:
```c
for (int d = MON; d < DAY_COUNT; d++) {
    printf("%d\n", d);
}
```

---

Der `COUNT`-Wächterwert ist auch die perfekte Größe für ein Array mit einem Feld pro Konstante, und die Konstanten werden zu lesbaren Indizes darin:
```c
enum Fruit { APPLE, BANANA, CHERRY, FRUIT_COUNT };

int stock[FRUIT_COUNT] = {10, 4, 7};
printf("%d\n", stock[BANANA]); // prints "4"
```
Eine Schleife von `0` bis `FRUIT_COUNT` besucht jedes Feld, und der Schleifenindex kann bei Bedarf zurück in `enum Fruit` umgewandelt werden.

---

C bietet keine eingebaute Möglichkeit, den Namen einer Enum-Konstante zu erhalten: `printf("%d\n", SUMMER)` gibt `2` aus, nicht `Summer`. Die übliche Lösung ist eine kleine Funktion mit einem `switch`, die für jede Konstante die passende Zeichenkette zurückgibt.

---

Aufzählungswerte können wie jede andere Ganzzahl in Arrays gespeichert werden: `enum Fruit basket[] = {APPLE, APPLE, CHERRY};` enthält drei Früchte, und jedes Element kann mit einer Konstante verglichen werden.
