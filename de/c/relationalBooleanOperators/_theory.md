**Relationale Operatoren** vergleichen zwei Werte. Das Ergebnis ist kein besonderer Typ: Es ist ein `int`, der `1` ist, wenn der Vergleich zutrifft, und `0`, wenn nicht. C hat sechs davon:
```c
printf("%d\n", 5 == 5); // equal: prints "1"
printf("%d\n", 5 != 5); // not equal: prints "0"
printf("%d\n", 3 < 5);  // less than: prints "1"
printf("%d\n", 3 > 5);  // greater than: prints "0"
printf("%d\n", 5 <= 5); // less than or equal: prints "1"
printf("%d\n", 4 >= 5); // greater than or equal: prints "0"
```
Da das Ergebnis ein `int` ist, wird es mit `%d` ausgegeben und kann wie jede andere Zahl in einer `int`-Variable gespeichert werden.

---

Eine Funktion kann einen Vergleich direkt zurückgeben: Der Aufrufer erhält `1` oder `0`.
```c
int is_big(int n) {
    return n > 100;
}

printf("%d\n", is_big(250)); // prints "1"
```
Die Wahl zwischen `>` und `>=` (oder `<` und `<=`) entscheidet, ob der Grenzwert zählt: `n >= 100` ist `1` für `100`, `n > 100` ist `0`.

---

Der häufigste Fehler in C ist, `=` zu schreiben, wo `==` gemeint ist. Ein einzelnes `=` ist eine **Zuweisung**, und in C ist eine Zuweisung ein Ausdruck, dessen Wert der zugewiesene Wert ist:
```c
int x = 3;
printf("%d\n", x == 7); // compares: prints "0", x is still 3
printf("%d\n", x = 7);  // assigns: prints "7", x is now 7
```
Der Code mit `=` kompiliert trotzdem, sodass eine Bedingung wie `if (x = 0)` stillschweigend `x` auf `0` setzt, statt sie zu prüfen. Die meisten Compiler geben dafür eine Warnung aus: Lies sie.

---

**Logische Operatoren** verknüpfen Bedingungen. Der **Und**-Operator `&&` liefert `1` nur, wenn beide Seiten wahr sind, der **Oder**-Operator `||` liefert `1`, wenn mindestens eine Seite wahr ist:
```c
int t = 25;
printf("%d\n", t > 20 && t < 30); // prints "1"
printf("%d\n", t < 20 || t > 30); // prints "0"
```
In C **gilt jeder Wert ungleich null als wahr** und nur `0` zählt als falsch, daher ist `5 && 1` gleich `1` und `0 || -3` gleich `1`. Das Ergebnis von `&&` und `||` ist immer genau `1` oder `0`.

---

Eine Variable, die `0` oder einen Wert ungleich null enthält, kann allein als Bedingung verwendet werden: `holiday` allein bedeutet „holiday ist ungleich null“, es ist nicht nötig, `holiday != 0` zu schreiben.
```c
int is_open(int weekday, int holiday) {
    return weekday && !holiday;
}
```
Der **Nicht**-Operator `!` kehrt eine Bedingung um: `!0` ist `1` und `!` vor jedem Wert ungleich null ergibt `0`.

---

Da `!` jeden Wert ungleich null in `0` und `0` in `1` umwandelt, normalisiert eine doppelte Anwendung einen Wert auf genau `0` oder `1`: `!!42` ist `1`, `!!0` ist `0`.
```c
int count = 3;
printf("%d %d\n", !count, !!count); // prints "0 1"
```
Das ist praktisch, wenn eine Funktion eine beliebige Zahl ungleich null zurückgibt und man eine saubere `1` möchte.

---

Seit C99 stellt der Header `stdbool.h` den Typ `bool` und die Konstanten `true` (was `1` ist) und `false` (was `0` ist) bereit:
```c
#include <stdbool.h>

bool open = true;
bool full = 3 > 5;
printf("%d %d\n", open, full); // prints "1 0"
```
Ein `bool` ist darunter weiterhin eine Ganzzahl: Er wird mit `%d` ausgegeben und funktioniert mit `&&`, `||` und `!` genau wie ein Vergleichsergebnis. Er macht die Absicht nur klarer als ein einfaches `int`.

---

Eine Funktion, die eine Ja/Nein-Frage beantwortet, sollte `bool` zurückgeben. Ein `bool`-Parameter ist bereits eine Bedingung, verwende ihn also direkt als Operanden von `&&` oder `||`: Schreibe `age >= 18 && citizen`, nicht `citizen == true`.
```c
bool can_enter(int age, bool member) {
    return age >= 16 && member;
}
```
`stdbool.h` ist in diesen Übungen bereits über deinem Code eingebunden.

---

`&&` und `||` verwenden **Kurzschlussauswertung**: Sie stoppen, sobald das Ergebnis feststeht.
- bei `&&` wird die rechte Seite nie ausgewertet, wenn die linke Seite `0` ist
- bei `||` wird die rechte Seite nie ausgewertet, wenn die linke Seite ungleich null ist

So kann eine Prüfung auf der linken Seite eine gefährliche Operation auf der rechten Seite absichern:
```c
int ok = count != 0 && total / count > 2;
```
Wenn `count` `0` ist, wird die Division nie ausgeführt, sodass das Programm nicht abstürzt.

---

Kurzschlussauswertung überspringt auch Funktionsaufrufe. In `1 || check()` wird die Funktion `check` nie aufgerufen, sodass ein etwaiger Seiteneffekt, wie das Aktualisieren eines Zählers, nicht eintritt.
```c
int calls = 0;

int check() {
    calls++;
    return 1;
}
```
Behalte das im Hinterkopf, wenn eine Funktion auf der rechten Seite von `&&` oder `||` etwas tut, auf das du dich verlässt.

---

Operatoren haben eine **Rangfolge**, die bestimmt, was zuerst berechnet wird:
1. `!` wird zuerst angewendet
2. dann die relationalen Vergleiche `<`, `>`, `<=`, `>=`
3. dann die Gleichheitsvergleiche `==`, `!=`
4. dann `&&`
5. dann `||`

Daher benötigt `a > 0 && a < 10` keine Klammern, und `a && b || c` bedeutet `(a && b) || c`, weil `&&` enger bindet als `||`. Verwende Klammern, um eine andere Gruppierung zu erzwingen oder die Absicht einfach lesbar zu machen.

---

Ein `char` ist eine kleine Ganzzahl, daher werden Zeichen mit denselben Operatoren verglichen. Vergleiche mit einem Zeichenliteral in einfachen Anführungszeichen: `"a"` mit doppelten Anführungszeichen ist eine Zeichenkette, die sich so nicht vergleichen lässt.
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // prints "1"
```
Aufeinanderfolgende Zeichen wie `'0'`, `'1'`, ... `'9'` oder `'a'`, `'b'`, ... `'z'` haben aufeinanderfolgende Codes, daher funktioniert eine Bereichsprüfung bei Zeichen genau wie bei Zahlen:
```c
bool is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Verkette Vergleiche nicht wie in der Mathematik. `1 <= x <= 10` kompiliert, wird aber als `(1 <= x) <= 10` ausgewertet: Der erste Vergleich liefert `0` oder `1`, und dieser wird dann mit `10` verglichen, sodass der gesamte Ausdruck immer `1` ist.
```c
int x = 20;
printf("%d\n", 1 <= x <= 10);       // prints "1" (wrong!)
printf("%d\n", 1 <= x && x <= 10);  // prints "0"
```
Schreibe immer beide Vergleiche explizit und verbinde sie mit `&&`.

---

Wenn eine Bedingung `&&` und `||` mischt, setze jeden Teil in Klammern, auch wenn die Rangfolge bereits das Richtige täte: Die Regel ist dann auf einen Blick lesbar.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
Der Restwert-Operator `%` passt natürlich zu `==`: `n % 4 == 0` ist `1`, wenn `n` durch `4` teilbar ist.
