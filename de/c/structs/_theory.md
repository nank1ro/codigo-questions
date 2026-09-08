Ein **struct** fasst zusammengehörige Werte unterschiedlicher Typen zu einem einzigen neuen Typ zusammen. Jeder Wert darin heißt **Member**.
Die Deklaration listet die Member zwischen geschweiften Klammern auf und endet mit einem Semikolon; sie erzeugt den Typ `struct Point`, aber noch keine Variable:
```c
struct Point {
    int x;
    int y;
};
```
Eine Variable dieses Typs wird mit `struct Point` deklariert, und ihre Member können **der Reihe nach** mit geschweiften Klammern initialisiert werden, wie bei einem Array:
```c
struct Point p = {3, 4}; // x ist 3, y ist 4
```
Member werden mit dem **Punkt**-Operator `.` gelesen und geschrieben:
```c
printf("%d\n", p.x); // gibt "3" aus
p.y = 10;
```

---

Member der Reihe nach zu initialisieren ist fragil: Kommt ein Member hinzu, verschiebt sich jeder Initialisierer. Seit C99 benennt ein **benannter Initialisierer** (designated initializer) jeden Member mit einem Punkt, in beliebiger Reihenfolge:
```c
struct Point p = {.y = 4, .x = 3};
```
Nicht aufgeführte Member werden auf `0` gesetzt, `{.y = 5}` ergibt also `x` gleich `0`. Das unterscheidet sich von einer Variablen, die ganz ohne Initialisierer deklariert wird, `struct Point q;`, deren Member **zufälligen Müll** enthalten, bis du ihnen etwas zuweist:
```c
struct Point q;
q.x = 1;
q.y = 2;
```

---

Ein struct kann wie jeder andere Wert an eine Funktion übergeben werden. Der Parameter wird mit dem vollständigen Typnamen deklariert, und die Funktion liest die Member mit `.`:
```c
struct Point { int x; int y; };

int sum(struct Point p) {
    return p.x + p.y;
}
```
Das struct muss **vor** der Funktion deklariert werden, die es benutzt, damit der Compiler seine Member bereits kennt.

---

Jedes Mal `struct Point` zu schreiben ist umständlich. Mit `typedef` gibst du dem struct einen kurzen Typnamen, und das struct selbst kann anonym bleiben:
```c
typedef struct {
    double celsius;
} Temperature;

Temperature t = {21.5};
```
Der neue Name `Temperature` wird für sich allein verwendet, ohne das Schlüsselwort `struct` davor. Das ist die häufigste Art, structs in echten Programmen zu deklarieren.

---

Ein Member kann selbst ein struct sein. Eine Strecke besteht zum Beispiel aus zwei Punkten:
```c
typedef struct { int x; int y; } Point;

typedef struct {
    Point start;
    Point end;
} Segment;
```
Das innere struct wird mit einem eigenen Paar geschweifter Klammern initialisiert, und seine Member werden durch Aneinanderreihen des Punkt-Operators erreicht:
```c
Segment s = {{1, 2}, {5, 2}};
printf("%d\n", s.end.x); // gibt "5" aus
```

---

Structs können wie jeder andere Typ in einem Array gespeichert werden. Jedes Element wird mit eigenen geschweiften Klammern initialisiert, und eine Schleife besucht sie eines nach dem anderen: erst indizieren, dann den Punkt verwenden:
```c
Point path[3] = {{0, 0}, {2, 1}, {4, 3}};

for (int i = 0; i < 3; i++) {
    printf("%d\n", path[i].y);
}
```

---

Ein Array von structs wird genauso an eine Funktion übergeben wie ein Array von Zahlen: Der Parameter wird als `Item items[]` geschrieben, und da das Array seine Länge nicht mitführt, wird die Größe separat übergeben:
```c
int count_free(Item items[], int size) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (items[i].price == 0) {
            count++;
        }
    }
    return count;
}
```

---

Wenn ein struct **als Wert** an eine Funktion übergeben wird, erhält die Funktion eine **Kopie**. Ein Member des Parameters zu ändern verändert nur die Kopie, und die Variable des Aufrufers bleibt, wie sie war:
```c
void reset(Point p) {
    p.x = 0; // ändert die Kopie
}
```
Damit eine Funktion das struct des Aufrufers verändern kann, übergib seine **Adresse** mit `&` und deklariere den Parameter als **Zeiger**, `Point *p`. Der Zeiger verweist auf die ursprüngliche Variable statt auf eine Kopie:
```c
void reset(Point *p) { ... }

reset(&origin);
```
Kopieren kostet bei großen structs außerdem Zeit, deshalb sind Zeiger die übliche Wahl, selbst wenn nichts verändert wird.

---

Über einen Zeiger werden die Member mit dem **Pfeil**-Operator `->` statt mit dem Punkt erreicht:
```c
void grow(Box *b) {
    b->size = b->size * 2;
}
```
`b->size` ist eine Kurzform für `(*b).size`: erst dem Zeiger folgen, dann den Member nehmen. Der Punkt funktioniert nur auf einem struct, der Pfeil nur auf einem Zeiger auf ein struct.
Der Aufrufer übergibt die Adresse seiner Variablen mit `&`, und die über den Zeiger vorgenommene Änderung ist nach dem Aufruf sichtbar.

---

Eine Funktion, die einen Zeiger auf ein struct erhält, kann den ursprünglichen Wert direkt aktualisieren. Das ist die übliche Art, "verändernde" Funktionen in C zu schreiben: Der erste Parameter ist das zu ändernde struct, die weiteren sind die anzuwendenden Daten:
```c
void set_number(Player *p, int new_number) {
    p->number = new_number;
}
```
Lesen und Schreiben laufen über denselben Pfeil: `p->score += 10` addiert zum Member des structs, auf das der Zeiger verweist.

---

Eine Funktion kann ein struct auch **zurückgeben**. Baue es in einer lokalen Variablen auf und gib es zurück; der Aufrufer erhält eine Kopie des gesamten Wertes:
```c
Point make_point(int x, int y) {
    Point p = {x, y};
    return p;
}

Point origin = make_point(0, 0);
```
So gibt C mehr als einen Wert aus einer Funktion zurück: indem man sie in ein struct packt.

---

`sizeof` funktioniert auch auf structs und ist der richtige Weg, um zu erfahren, wie viel Speicher eines belegt:
```c
printf("%zu\n", sizeof(Point));
```
Die Größe ist **mindestens** die Summe der Größen der Member. Sie kann größer sein, weil der Compiler ungenutzte **Füllbytes** (Padding) einfügen darf, damit jeder Member an einer für seinen Typ passenden Adresse liegt: `struct { char c; int n; }` belegt üblicherweise `8` Bytes, nicht `5`. Schreibe die Größe eines structs nie fest in den Code; frag `sizeof`.

---

Structs können nicht mit `==` verglichen werden: `a == b` auf zwei structs zu schreiben ist ein **Kompilierfehler**. Vergleiche sie stattdessen **Member für Member** und kombiniere die Ergebnisse mit `&&`:
```c
bool same_size(Rectangle a, Rectangle b) {
    return a.width == b.width && a.height == b.height;
}
```
Dasselbe gilt für `<` und `>`: Du entscheidest, welcher Member die Reihenfolge bestimmt.

---

Ein struct enthält oft Text, gespeichert als `char`-Array-Member mit fester Größe:
```c
typedef struct {
    char name[20];
    int age;
} Person;
```
Einem Array-Member kann nach der Deklaration nichts mit `=` zugewiesen werden: `p.name = "Ann"` kompiliert nicht. Kopiere den Text mit `strcpy` aus `string.h` hinein und übergib den Member als Ziel:
```c
Person p;
strcpy(p.name, "Ann");
p.age = 30;
```
Nur ein Klammer-Initialisierer bei der Deklaration nimmt die Zeichenkette direkt an: `Person p = {"Ann", 30};`.

---

`printf` hat keinen Formatbezeichner für ein ganzes struct. Die übliche Lösung ist eine kleine Funktion, die die Member in einem festen Format ausgibt, damit jeder Teil des Programms den Wert gleich darstellt:
```c
void print_person(Person p) {
    printf("%s (%d)\n", p.name, p.age);
}
```

---

Alles zusammen: Eine Funktion, die einen Zeiger auf ein struct erhält, kann einen Text-Member mit `strcpy` über den Pfeil aktualisieren, denn `item->name` ist das `char`-Array im ursprünglichen struct:
```c
void set_title(Book *book, char *title) {
    strcpy(book->title, title);
}
```
Denk daran, `#include <string.h>` an den Anfang deines Codes zu setzen, um `strcpy` zu verwenden.
