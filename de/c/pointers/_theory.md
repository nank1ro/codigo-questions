Jede Variable lebt irgendwo im Speicher, und dieser Ort hat eine Nummer, die seine **Adresse** genannt wird. Der Operator `&`, gelesen als „address of“ (Adresse von), liefert die Adresse einer Variable:
```c
int x = 42;
printf("%p\n", &x); // gibt etwas wie 0x7ffd5c3e9a4c aus
```
Der `%p`-Spezifizierer gibt eine Adresse aus; die genaue Zahl ändert sich von einem Lauf zum nächsten, daher verlassen sich Programme nie darauf.
Eine Adresse wird in einer **Zeiger**-Variable gespeichert. Ein Zeiger wird mit dem Typ deklariert, auf den er zeigt, gefolgt von `*`:
```c
int *p = &x; // p ist ein Zeiger auf int und speichert die Adresse von x
```
Man sagt nun, `p` **zeigt auf** `x`. Zwei Zeiger sind gleich, wenn sie dieselbe Adresse speichern, daher ist `p == &x` wahr.

---

Ein Zeiger allein ist nur eine Adresse. Um den Wert zu lesen, der an dieser Adresse gespeichert ist, **dereferenzierst** du den Zeiger mit dem Operator `*`:
```c
int x = 42;
int *p = &x;
printf("%d\n", *p); // gibt "42" aus
```
`*p` bedeutet „der Wert, auf den `p` zeigt“, und er ist ein `int` wie `x` selbst. Dasselbe Symbol `*` hat zwei Rollen: In einer Deklaration `int *p` sagt es „das ist ein Zeiger“, in einem Ausdruck `*p` folgt es dem Zeiger zum Wert.

---

Ein dereferenzierter Zeiger kann auch **beschrieben** werden. Das Schreiben in `*p` speichert den neuen Wert an der Adresse, die `p` hält, sodass sich die Variable ändert, auf die er zeigt:
```c
int x = 5;
int *p = &x;
*p = 10;
printf("%d\n", x); // gibt "10" aus
```
`x` und `*p` sind zwei Namen für denselben Speicher. Eine Zuweisung an `p` ohne das `*` würde stattdessen ändern, **welche Adresse** der Zeiger hält, nicht den dort gespeicherten Wert.

---

Ein Zeiger, der noch auf nichts zeigt, sollte `NULL` halten, eine besondere Konstante, die in `stdio.h` und `stddef.h` definiert ist und „keine Adresse“ bedeutet:
```c
int *p = NULL;
```
Das Dereferenzieren eines `NULL`-Zeigers ist ein Laufzeitfehler, der das Programm abstürzen lässt, daher wird ein Zeiger, der `NULL` sein kann, vor der Verwendung geprüft:
```c
if (p != NULL) {
    printf("%d\n", *p);
}
```
Da `NULL` null ist, ist `if (p)` eine gängige Kurzform für `if (p != NULL)`. Ein Zeiger, der ohne Initialisierer deklariert wird, hält Müll, nicht `NULL`, daher initialisiere Zeiger immer.

---

Ein Zeiger kann auf jeden Typ zeigen: `double *`, `char *`, `bool *` und so weiter. Der Typ in der Deklaration sagt dem Compiler, wie viele Bytes er beim Dereferenzieren des Zeigers lesen soll und was sie bedeuten:
```c
double price = 9.5;
double *p = &price;
*p = *p * 2; // price ist jetzt 19.0
```
Ein Zeiger muss zum Typ der Variable passen, auf die er zeigt; `int *p = &price;` wird vom Compiler abgelehnt. `NULL` ist der einzige Wert, der zu einem Zeiger jedes Typs passt.

---

Ein Zeiger auf `char` funktioniert wie jeder andere Zeiger: Er hält die Adresse eines einzelnen Zeichens, und `*p` liest oder schreibt dieses Zeichen:
```c
char grade = 'B';
char *p = &grade;
*p = 'A';
printf("%c\n", grade); // gibt "A" aus
```
Lesen über einen Zeiger und Schreiben durch ihn lassen sich frei kombinieren: `*p = *p + 1` macht aus `'A'` ein `'B'`.

---

Ein Zeiger speichert eine Adresse, und jede Adresse hat auf einer gegebenen Maschine dieselbe Größe, egal welcher Typ dort gespeichert ist. `sizeof` eines Zeigers ist daher für `char *`, `int *` und `double *` gleich: `8` Bytes auf einem 64-Bit-System, `4` auf einem 32-Bit-System:
```c
printf("%zu\n", sizeof(int *));  // gibt "8" auf 64-Bit aus
printf("%zu\n", sizeof(double)); // gibt "8" aus
printf("%zu\n", sizeof(char));   // gibt "1" aus
```
Verwechsle nicht die Größe des Zeigers mit der Größe des Objekts, auf das er zeigt: `sizeof(p)` ist die Größe der Adresse, `sizeof(*p)` die Größe des Werts.

---

Ein in einem Ausdruck verwendeteter Array-Name liefert die Adresse seines **ersten Elements**, daher kann er direkt einem Zeiger zugewiesen werden:
```c
int numbers[3] = {10, 20, 30};
int *p = numbers; // dasselbe wie &numbers[0]
```
Addiert man eine Ganzzahl zu einem Zeiger, rückt er um so viele **Elemente** weiter, nicht um so viele Bytes: `p + 1` ist die Adresse von `numbers[1]`, und `*(p + 1)` ist `20`. Der Compiler skaliert den Schritt auf die Größe des Typs.
Indizierung funktioniert auch auf Zeigern: `p[i]` ist definiert als `*(p + i)`, daher ist `p[2]` gleich `30`. Das nennt man **Zeigerarithmetik**.

---

Da `p + 1` das nächste Element ist, rückt `p++` einen Zeiger an Ort und Stelle zum nächsten Element weiter. Eine Schleife kann ein Array durchlaufen, indem sie einen Zeiger statt eines Indexes weiterbewegt:
```c
int *p = values;
for (int i = 0; i < 3; i++) {
    printf("%d\n", *p);
    p++;
}
```
Jeder Durchlauf gibt das Element aus, auf das `p` zeigt, und bewegt `p` dann ein Element vorwärts.

---

Wird ein Array an eine Funktion übergeben, **zerfällt** es zu einem Zeiger auf sein erstes Element. Deshalb bedeuten die Parameter `int values[]` und `int *values` genau dasselbe, und deshalb kann die Funktion die Länge nicht von selbst wissen: Sie erhält nur eine Adresse.
Zeiger in dasselbe Array lassen sich vergleichen und voneinander subtrahieren. `end - start` ist die Anzahl der Elemente zwischen ihnen, und eine Schleife kann einen Zeiger von einer Adresse zur anderen laufen lassen:
```c
for (int *p = start; p < end; p++) {
    printf("%d\n", *p);
}
```
Die Übergabe von `numbers` und `numbers + 3` beschreibt die ersten drei Elemente ohne einen separaten Größenparameter.

---

Funktionsargumente werden **als Wert übergeben** (by value): Die Funktion erhält eine Kopie, und eine Zuweisung an einen Parameter ändert nie die Variable des Aufrufers. Damit eine Funktion eine Variable ändern kann, übergibst du die Adresse der Variable und dereferenzierst den Zeiger innerhalb der Funktion:
```c
void reset(int *p) {
    *p = 0;
}

int counter = 7;
reset(&counter); // counter ist jetzt 0
```
Das klassische Beispiel ist das Vertauschen zweier Variablen, das eine temporäre Kopie des einen Werts benötigt, während der andere überschrieben wird.

---

Eine Funktion kann nur einen Wert `return`en. Um mehr zurückzugeben, nimmt sie Zeiger auf Variablen des Aufrufers entgegen und schreibt die Ergebnisse durch sie hindurch. Solche Parameter heißen **Ausgabeparameter**:
```c
void min_max(int a, int b, int *min, int *max) {
    *min = a;
    *max = b;
    if (a > b) {
        *min = b;
        *max = a;
    }
}

int lo, hi;
min_max(4, 9, &lo, &hi); // lo ist 4, hi ist 9
```
Der Aufrufer deklariert die Variablen, übergibt ihre Adressen und findet sie nach dem Aufruf ausgefüllt vor. Viele Standardfunktionen verwenden dieses Muster, weshalb `scanf("%d", &n)` das `&` benötigt.

---

Ein Zeiger auf ein struct erreicht die Member mit dem Pfeil `->`, und die Adresse eines in einem Array gespeicherten structs wird mit `&items[i]` genommen. Eine Funktion kann auch einen Zeiger **zurückgeben**, zum Beispiel auf das gefundene Element:
```c
Player *first_active(Player players[], int size) {
    for (int i = 0; i < size; i++) {
        if (players[i].active) {
            return &players[i];
        }
    }
    return NULL;
}
```
Der Aufrufer liest Member dann über den zurückgegebenen Zeiger mit `->`, nachdem er geprüft hat, dass dieser nicht `NULL` ist. Das Zurückgeben eines Zeigers vermeidet das Kopieren des structs und erlaubt dem Aufrufer, das ursprüngliche Element zu ändern.

---

`const` kann entweder den Wert oder den Zeiger schützen, je nachdem, wo es geschrieben steht:
```c
const int *p = &a; // Zeiger auf const: *p kann nicht geändert werden, p kann woandershin zeigen
int *const q = &a; // const-Zeiger: q zeigt immer auf a, aber *q kann geändert werden
```
Lies die Deklaration von rechts nach links: `p` ist ein Zeiger auf ein konstantes `int`; `q` ist ein konstanter Zeiger auf ein `int`. Ein Zeiger auf const ist die übliche Art zu versprechen, dass eine Funktion nur **liest**, was sie erhält, wie in `int sum(const int *values, int size)`. Eine normale Variable kann ihr übergeben werden; das Versprechen schränkt nur ein, was die Funktion tun darf.

---

Ein Zeiger ist eine Variable, daher hat er eine eigene Adresse, und diese Adresse kann in einem **Zeiger auf Zeiger** gespeichert werden, der mit zwei Sternen deklariert wird:
```c
int x = 7;
int *p = &x;
int **pp = &p;
```
`*pp` ist `p`, die Adresse von `x`, und `**pp` folgt beiden Schritten und erreicht `7`. Zeiger auf Zeiger ermöglichen es einer Funktion zu ändern, welche Adresse ein Zeiger hält: Sie empfängt `&p` und weist `*pp` zu.

---

Setzen wir alles zusammen: eine Funktion, die ein Array mit einem Zeiger durchläuft, einen Zeiger auf das bisher beste Element behält und ihn zurückgibt, oder `NULL`, wenn es nichts zurückzugeben gibt:
```c
int *first_negative(int *values, int size) {
    for (int *p = values; p < values + size; p++) {
        if (*p < 0) {
            return p;
        }
    }
    return NULL;
}
```
Der Aufrufer vergleicht das Ergebnis mit `NULL`, bevor er es dereferenziert, und kann mit `result - values` den Index des Elements zurückgewinnen.
