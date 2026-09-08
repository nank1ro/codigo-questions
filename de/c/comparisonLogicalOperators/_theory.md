**Vergleichsoperatoren** vergleichen zwei Werte und liefern ein Ergebnis: `1`, wenn der Vergleich zutrifft, und `0`, wenn nicht.
Der **Gleich**-Operator `==` prüft, ob zwei Werte identisch sind, der **Ungleich**-Operator `!=` prüft, ob sie sich unterscheiden:
```c
int a = 7, b = 3;
printf("%d\n", a == b);
// gibt "0" aus
printf("%d\n", a != b);
// gibt "1" aus
```
Achtung: `==` (zwei Zeichen) vergleicht, während ein einzelnes `=` einen Wert zuweist.

---

Die anderen Vergleichsoperatoren prüfen die Reihenfolge zweier Werte:
- `<` kleiner als, `>` größer als
- `<=` kleiner oder gleich, `>=` größer oder gleich
```c
printf("%d\n", 3 < 5);  // gibt "1" aus
printf("%d\n", 5 >= 6); // gibt "0" aus
```
Eine Funktion kann einen Vergleich direkt zurückgeben, da das Ergebnis ein einfacher `int` ist:
```c
int is_big(int n) {
    return n > 100;
}
```

---

In C ist das Ergebnis eines Vergleichs kein besonderer Typ: Es ist ein `int`, dessen Wert genau `1` (wahr) oder `0` (falsch) ist.
Das bedeutet, du kannst es wie jede andere Zahl in einer `int`-Variable speichern:
```c
int n = 42;
int big = n > 100; // big ist 0
```
Es gibt kein Wort `true`/`false` in der Ausgabe: `printf("%d", 2 == 2)` gibt `1` aus.

---

**Logische Operatoren** verknüpfen Vergleiche. Der **Und**-Operator `&&` liefert `1` nur, wenn beide Seiten wahr sind:
```c
int age = 25;
printf("%d\n", age >= 18 && age < 65); // gibt "1" aus
```
Verkette Vergleiche nicht wie in der Mathematik: `1 <= x <= 10` wird als `(1 <= x) <= 10` ausgewertet, was eine `0` oder `1` mit `10` vergleicht und immer wahr ist.
Schreibe die beiden Vergleiche immer explizit und verbinde sie mit `&&`.

---

Der **Oder**-Operator `||` liefert `1`, wenn mindestens eine Seite wahr ist, und `0` nur, wenn beide Seiten falsch sind:
```c
int day = 1;
printf("%d\n", day == 1 || day == 7); // gibt "1" aus
```
Jede Seite muss ein vollständiger Vergleich sein: `day == 6 || 7` bedeutet nicht "6 oder 7" (du wirst später sehen, warum).

---

Der **Nicht**-Operator `!` kehrt ein Ergebnis um: `!1` ist `0` und `!0` ist `1`.
Er steht vor dem Ausdruck, verwende also Klammern, um einen ganzen Vergleich zu negieren:
```c
int n = 5;
printf("%d\n", !(n > 3)); // gibt "0" aus
```
Ohne die Klammern würde `!n > 3` zuerst `!n` berechnen und das Ergebnis dann mit `3` vergleichen.

---

Logische Operatoren funktionieren nicht nur mit `0` und `1`: In C zählt **jeder Wert ungleich null als wahr**, und nur `0` zählt als falsch.
Daher ist `5 && 1` gleich `1`, `0 || -3` ist `1`, und `!` verwandelt jeden Wert ungleich null in `0`:
```c
printf("%d\n", !7); // gibt "0" aus
printf("%d\n", !0); // gibt "1" aus
```
Deshalb ist `day == 6 || 7` immer wahr: `7` allein ist bereits ein wahrer Wert.

---

`&&` und `||` verwenden **Kurzschlussauswertung**: Sie stoppen, sobald das Ergebnis feststeht.
- bei `&&` wird die rechte Seite nie ausgewertet, wenn die linke Seite `0` ist
- bei `||` wird die rechte Seite nie ausgewertet, wenn die linke Seite wahr ist

Dadurch kannst du eine gefährliche Operation mit einer links davor platzierten Prüfung absichern:
```c
int safe = divisor != 0 && value / divisor > 2;
```
Wenn `divisor` `0` ist, wird die Division nie ausgeführt.

---

Kurzschlussauswertung überspringt auch Funktionsaufrufe: In `0 && check()` wird die Funktion `check` nie aufgerufen, sodass ein etwaiger Seiteneffekt (wie das Aktualisieren eines Zählers) nicht eintritt.

---

Operatoren haben eine **Rangfolge**, die bestimmt, was zuerst berechnet wird:
1. `!` wird zuerst angewendet
2. dann die relationalen Vergleiche `<`, `>`, `<=`, `>=`
3. dann die Gleichheitsvergleiche `==`, `!=`
4. dann `&&`
5. dann `||`

Daher benötigt `a > 0 && a < 10` keine Klammern: Beide Vergleiche werden vor `&&` berechnet.
Und `x == 1 || y == 2 && z == 3` bedeutet `x == 1 || (y == 2 && z == 3)`, weil `&&` stärker bindet als `||`.

---

Ein `char` ist eine kleine Ganzzahl, daher können Zeichen mit denselben Operatoren verglichen werden.
Vergleiche mit einem Zeichenliteral in einfachen Anführungszeichen:
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // gibt "1" aus
```
Doppelte Anführungszeichen würden einen String erzeugen, der sich so nicht vergleichen lässt.

---

Da Zeichen Zahlen sind, vergleichen `<` und `>` ihre Codes, und aufeinanderfolgende Zeichen wie `'a'`, `'b'`, `'c'` oder `'0'`, `'1'`, `'2'` haben aufeinanderfolgende Codes.
Eine Bereichsprüfung bei Zeichen funktioniert daher genau wie bei Zahlen:
```c
int is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Ein klassischer C-Fehler ist es, `=` statt `==` zu schreiben. Der Code kompiliert trotzdem, weil eine Zuweisung ein Ausdruck ist, dessen Wert der zugewiesene Wert ist:
```c
int x = 5;
if (x = 0) { ... } // weist x den Wert 0 zu, die Bedingung ist 0 (falsch)
if (x = 3) { ... } // weist x den Wert 3 zu, die Bedingung ist 3 (wahr)
```
Die meisten Compiler warnen davor, also lies die Warnungen, wenn sich eine Bedingung merkwürdig verhält.

---

Die Bedingung eines `if` ist einfach ein Ausdruck, der als wahr gilt, wenn er ungleich null ist, daher passen Vergleiche und logische Operatoren natürlich hinein:
```c
if (n < 0) {
    printf("negative\n");
} else if (n == 0) {
    printf("zero\n");
}
```
Du kannst das Ergebnis auch zuerst speichern und die Variable testen: `int ok = n > 0; if (ok) { ... }`.

---

Eine `while`-Schleife läuft weiter, solange ihre Bedingung ungleich null ist, daher entscheidet ein Vergleich, wann sie stoppt:
```c
int i = 0;
while (i < 3) {
    printf("%d\n", i);
    i++;
}
// gibt 0, 1, 2 aus
```
Die Wahl zwischen `<` und `<=` entscheidet, ob der letzte Wert eingeschlossen wird.

---

Seit C99 stellt der Header `stdbool.h` den Typ `bool` und die Konstanten `true` (`1`) und `false` (`0`) bereit:
```c
#include <stdbool.h>

bool ready = true;
bool done = count == 10;
```
Ein `bool` ist im Kern immer noch eine Ganzzahl: Die Ausgabe mit `%d` zeigt `1` oder `0`, und er funktioniert mit `&&`, `||` und `!` wie jedes Vergleichsergebnis.
Die Verwendung von `bool` macht die Absicht einer Funktion klarer, als einfach einen `int` zurückzugeben.

---

Ein `bool`-Parameter kann direkt als Operand von `&&` oder `||` verwendet werden, ohne ihn mit `true` zu vergleichen: schreibe `age >= 18 && citizen`, nicht `citizen == true`.

---

Wenn eine Bedingung `&&` und `||` mischt, setze Klammern um jede Gruppe, auch wenn die Rangfolge bereits das Richtige tun würde: Das macht die Regel auf einen Blick lesbar.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
