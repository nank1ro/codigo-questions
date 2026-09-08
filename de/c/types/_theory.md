C ist eine **statisch typisierte** Sprache: Jede Variable wird mit einem Typ deklariert, der bestimmt, was sie speichern kann und wie viel Speicher sie belegt.
Die drei am häufigsten verwendeten Typen sind:
- `int` für ganze Zahlen, wie `30` oder `-4`
- `double` für Zahlen mit Dezimalteil, wie `1.75`
- `char` für ein einzelnes Zeichen, in einfachen Anführungszeichen geschrieben wie `'A'`

Jeder Typ hat seinen eigenen `printf` **Formatbezeichner**: `%d` gibt einen `int` aus, `%f` gibt einen `double` aus (standardmäßig mit sechs Dezimalstellen) und `%c` gibt ein `char` aus:
```c
int age = 30;
double height = 1.75;
char initial = 'A';
printf("%d %f %c\n", age, height, initial);
// gibt "30 1.750000 A" aus
```
Den falschen Bezeichner für einen Typ zu verwenden gibt Datenmüll aus, also müssen sie immer zusammenpassen.

---

C hat zwei Gleitkommatypen: `float` (einfache Genauigkeit, etwa 7 signifikante Stellen) und `double` (doppelte Genauigkeit, etwa 15 signifikante Stellen).
Ein Dezimalliteral wie `1.75` ist ein `double`; um ein `float`-Literal zu schreiben, fügst du das Suffix `f` hinzu, wie in `1.75f`.
Bevorzuge `double`, außer wenn Speicher knapp ist: Es ist die Standardwahl und genauer.
```c
double pi = 3.14159;
float ratio = 0.5f;
```
Eine Funktion, die ein Dezimalergebnis zurückgibt, sollte `double` als Rückgabetyp deklarieren, und `double`-Parameter akzeptieren sowohl ganze als auch dezimale Argumente:
```c
double half(double x) {
    return x / 2;
}
```

---

`%f` gibt sechs Dezimalstellen aus, was selten das ist, was du willst. Setze eine Genauigkeit zwischen `%` und `f`, um festzulegen, wie viele Dezimalstellen angezeigt werden: `%.2f` gibt zwei Dezimalstellen aus, `%.1f` eine, und der Wert wird dabei **gerundet**, nicht abgeschnitten:
```c
double price = 9.987;
printf("%.2f\n", price); // gibt "9.99" aus
printf("%.1f\n", price); // gibt "10.0" aus
```
Ein `float` wird mit denselben Bezeichnern wie ein `double` ausgegeben: Wenn er an `printf` übergeben wird, wird er automatisch in `double` umgewandelt.

---

Das Ergebnis von `/` hängt von den Typen seiner Operanden ab.
Wenn **beide** Operanden ganze Zahlen sind, ist das Ergebnis eine ganze Zahl und der Dezimalteil wird verworfen: `7 / 2` ist `3`, nicht `3.5`.
Wenn **mindestens einer** der Operanden ein Gleitkommawert ist, behält die Division die Dezimalstellen: `7 / 2.0` ist `3.5`.
```c
printf("%d\n", 7 / 2);     // gibt "3" aus
printf("%f\n", 7 / 2.0);   // gibt "3.500000" aus
```
Das Literal als `2.0` statt `2` zu schreiben ist der einfachste Weg, eine Gleitkommadivision zu erzwingen.

---

C konvertiert **implizit** zwischen numerischen Typen, wenn ein Wert einer Variable eines anderen Typs zugewiesen wird.
- ein in einem `double` gespeicherter `int` wird verlustfrei erweitert: `double d = 3;` macht `d` gleich `3.0`
- ein in einem `int` gespeicherter `double` wird **abgeschnitten**: `int n = 3.99;` macht `n` gleich `3` (Compiler warnen davor meist)

Die Umwandlung erfolgt erst im Moment der Zuweisung. Der Ausdruck auf der rechten Seite wird zuerst mit seinen eigenen Typen berechnet:
```c
double d = 7 / 2;
```
Hier ist `7 / 2` eine Ganzzahldivision, die `3` ergibt, und erst danach wird `3` in `3.0` umgewandelt.

---

Wenn die implizite Umwandlung nicht das ist, was du willst, oder du sie sichtbar machen willst, verwende eine **explizite Umwandlung (Cast)**: Schreibe den Zieltyp in Klammern vor den Wert.
```c
double x = 3.99;
int n = (int) x;   // n ist 3
```
Das Umwandeln eines Gleitkommawerts in `int` **schneidet in Richtung Null ab**: `(int) 3.99` ist `3` und `(int) -2.5` ist `-2`, es findet keine Rundung statt.
Der Cast gilt nur für den Wert direkt danach, also castet `(int) x * 2` zuerst `x` und multipliziert danach.

---

Ein Cast ist der Standardweg, um aus zwei `int`-Variablen eine Gleitkommadivision zu erhalten: caste **einen Operanden** vor der Division in `double`.
```c
int total = 7, count = 2;
double avg = (double) total / count; // 3.5
```
Stattdessen das gesamte Ergebnis zu casten, wie in `(double) (total / count)`, ist ein häufiger Fehler: Die Ganzzahldivision hat bereits stattgefunden und die Dezimalstellen sind verloren.

---

Ein `char` ist eigentlich eine kleine Ganzzahl: Er speichert den **ASCII-Code** des Zeichens.
`'A'` ist `65`, `'a'` ist `97` und `'0'` ist `48`, und aufeinanderfolgende Zeichen haben aufeinanderfolgende Codes.
Deshalb kannst du mit Zeichen rechnen:
- `'a' + 1` ist `98`, der Code von `'b'`
- `'7' - '0'` ist `55 - 48`, also die Zahl `7`

Derselbe Wert kann mit `%c` als Zeichen oder mit `%d` als Zahl ausgegeben werden:
```c
char c = 'A';
printf("%c %d\n", c, c); // gibt "A 65" aus
```

---

Groß- und Kleinbuchstaben liegen in der ASCII-Tabelle `32` Positionen auseinander: `'A'` ist `65` und `'a'` ist `97`.
Das Abziehen von `32` von einem Kleinbuchstaben ergibt daher dessen Großbuchstaben-Version, und das Ergebnis kann wieder in einem `char` gespeichert werden:
```c
char upper = 'g' - 32; // 'G'
```

---

`int` ist nicht der einzige Ganzzahltyp. Modifikatoren ändern seine Größe und seinen Bereich:
- `short` verwendet weniger Speicher und hat einen kleineren Bereich (üblicherweise -32768 bis 32767)
- `long` hat einen größeren Bereich (auf 64-Bit-Systemen etwa ±9 Trillionen)
- `unsigned` entfernt das Vorzeichen: `unsigned int` reicht von `0` bis etwa 4 Milliarden, kann aber nie negativ sein

Ein Literal, das `long` sein muss, erhält das Suffix `L`, eines, das `unsigned` sein muss, das Suffix `U`, und jeder Typ hat seinen eigenen Bezeichner:
```c
long population = 8000000000L;
unsigned int count = 40U;
printf("%ld %u\n", population, count); // gibt "8000000000 40" aus
```
`%ld` gibt einen `long` aus, `%u` einen `unsigned int` und `%lu` einen `unsigned long`. Ein einfacher `int` fasst auf den meisten Systemen Werte bis etwa 2 Milliarden, daher passt `5000000000` nicht hinein.

---

Der `sizeof`-Operator gibt an, wie viele **Bytes** ein Typ oder eine Variable belegt. Sein Ergebnis hat den Typ `size_t`, der mit `%zu` ausgegeben wird:
```c
printf("%zu\n", sizeof(int));  // gibt auf den meisten Systemen "4" aus
```
Der Standard garantiert nur, dass `sizeof(char)` gleich `1` ist und dass `short <= int <= long` gilt, aber auf einem typischen 64-Bit-System sind die Größen: `char` 1, `short` 2, `int` 4, `long` 8, `float` 4, `double` 8.
`sizeof` wird oft verwendet, um zu prüfen, wie viel Speicher eine Variable belegt, ohne die Zahl fest im Code zu verankern.

---

Jeder Ganzzahltyp hat einen begrenzten Bereich, und der Header `limits.h` gibt diesen Grenzen einen Namen: `INT_MAX` und `INT_MIN` für `int`, `LONG_MAX` für `long`, `UINT_MAX` für `unsigned int` und so weiter.
```c
#include <limits.h>

printf("%d\n", INT_MAX); // gibt auf den meisten Systemen "2147483647" aus
```
`INT_MAX` bei einem vorzeichenbehafteten Typ zu überschreiten ist **undefiniertes Verhalten**: Das Programm kann überlaufen, abstürzen oder irgendetwas anderes tun. Prüfe, bevor du rechnest:
```c
if (a <= INT_MAX - b) { /* a + b ist sicher */ }
```
Beachte, dass die Prüfung subtrahiert statt addiert, weil `a + b` selbst bereits überlaufen könnte.

---

Anders als bei vorzeichenbehafteten Typen ist **unsigned**-Arithmetik außerhalb des Bereichs wohldefiniert: Der Wert **läuft über** wie ein Kilometerzähler.
`1` zu `UINT_MAX` zu addieren ergibt `0`, und `1` von `0` zu subtrahieren ergibt `UINT_MAX` (`4294967295`, wenn `unsigned int` 32 Bit hat):
```c
unsigned int n = UINT_MAX;
n = n + 1;
printf("%u\n", n); // gibt "0" aus
```
Deshalb stoppt eine Schleife, die eine `unsigned`-Variable herunterzählt „bis sie negativ ist", nie: Ein unsigned-Wert liegt niemals unter `0`.

---

Seit C99 stellt der Header `stdbool.h` den Typ `bool` mit den Konstanten `true` (`1`) und `false` (`0`) bereit.
Ein `bool` ist ein Ganzzahltyp mit nur zwei Werten, daher ergibt die Umwandlung einer beliebigen Zahl in `bool` für jeden Wert ungleich null `true` und für `0` `false`. Das unterscheidet sich von der Umwandlung in `int`:
```c
#include <stdbool.h>

bool b = 0.5;  // true, weil 0.5 nicht null ist
int n = 0.5;   // 0, weil die Dezimalstellen abgeschnitten werden
```
Vergleiche wie `x != 0` liefern bereits ein `bool`-kompatibles Ergebnis, und eine Funktion, die `bool` zurückgibt, dokumentiert, dass sie eine Ja/Nein-Frage beantwortet.

---

Eine arithmetische Operation wird im Typ ihrer Operanden ausgeführt, **nicht** im Typ der Variable, die das Ergebnis erhält.
`long big = n * n;` mit einem `int` `n` multipliziert also zwei `int`-Werte, läuft über, wenn das Produkt zu groß ist, und speichert erst dann das (bereits falsche) Ergebnis im `long`.
Caste einen Operanden **vor** der Operation, um im breiteren Typ zu rechnen:
```c
int n = 100000;
long big = (long) n * n; // 10000000000, berechnet als long
```
Dieselbe Regel erklärt, warum `(double) total / count` funktioniert: Der Cast ändert den Typ des Operanden, und die Division folgt entsprechend.

---

Alles zusammengefügt: Wähle den Typ entsprechend der Art des Wertes, passe jeden `printf`-Bezeichner zu seinem Argumenttyp, und caste, wenn eine Berechnung in einem anderen Typ als dem seiner Operanden erfolgen muss.
