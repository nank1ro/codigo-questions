**Struktura** grupuje powiązane wartości różnych typów w jeden nowy typ. Każda wartość wewnątrz niej nazywa się **polem**.
Deklaracja wymienia pola między nawiasami klamrowymi i kończy się średnikiem; tworzy typ `struct Point`, ale jeszcze żadnej zmiennej:
```c
struct Point {
    int x;
    int y;
};
```
Zmienna tego typu jest deklarowana przez `struct Point`, a jej pola można zainicjalizować **w kolejności** za pomocą nawiasów klamrowych, jak w tablicy:
```c
struct Point p = {3, 4}; // x is 3, y is 4
```
Pola odczytuje się i zapisuje operatorem **kropki** `.`:
```c
printf("%d\n", p.x); // prints "3"
p.y = 10;
```

---

Inicjalizowanie pól w kolejności jest kruche: jeśli struktura zyska nowe pole, każdy inicjalizator się przesuwa. Od C99 **inicjalizator oznaczony** nazywa każde pole kropką, w dowolnej kolejności:
```c
struct Point p = {.y = 4, .x = 3};
```
Pola, których nie wymieniono, otrzymują wartość `0`, więc `{.y = 5}` daje `x` równe `0`. To co innego niż zmienna zadeklarowana bez żadnego inicjalizatora, `struct Point q;`, której pola zawierają **śmieciowe wartości**, dopóki im czegoś nie przypiszesz:
```c
struct Point q;
q.x = 1;
q.y = 2;
```

---

Strukturę można przekazać do funkcji jak każdą inną wartość. Parametr deklaruje się z pełną nazwą typu, a funkcja odczytuje pola za pomocą `.`:
```c
struct Point { int x; int y; };

int sum(struct Point p) {
    return p.x + p.y;
}
```
Struktura musi być zadeklarowana **przed** funkcją, która jej używa, aby kompilator znał już jej pola.

---

Pisanie `struct Point` za każdym razem jest uciążliwe. Za pomocą `typedef` nadajesz strukturze krótką nazwę typu, a sama struktura może pozostać anonimowa:
```c
typedef struct {
    double celsius;
} Temperature;

Temperature t = {21.5};
```
Nowej nazwy `Temperature` używa się samodzielnie, bez słowa kluczowego `struct` przed nią. To najczęstszy sposób deklarowania struktur w prawdziwych programach.

---

Polem może być sama struktura. Odcinek na przykład składa się z dwóch punktów:
```c
typedef struct { int x; int y; } Point;

typedef struct {
    Point start;
    Point end;
} Segment;
```
Wewnętrzną strukturę inicjalizuje się jej własną parą nawiasów klamrowych, a jej pola osiąga się przez łączenie operatora kropki:
```c
Segment s = {{1, 2}, {5, 2}};
printf("%d\n", s.end.x); // prints "5"
```

---

Struktury można przechowywać w tablicy jak każdy inny typ. Każdy element inicjalizuje się jego własnymi nawiasami klamrowymi, a pętla odwiedza je jeden po drugim, najpierw indeksując, a potem używając kropki:
```c
Point path[3] = {{0, 0}, {2, 1}, {4, 3}};

for (int i = 0; i < 3; i++) {
    printf("%d\n", path[i].y);
}
```

---

Tablicę struktur przekazuje się do funkcji dokładnie tak samo jak tablicę liczb: parametr zapisuje się jako `Item items[]`, a ponieważ tablica nie niesie swojej długości, rozmiar przekazuje się osobno:
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

Gdy struktura jest przekazywana do funkcji **przez wartość**, funkcja otrzymuje jej **kopię**. Zmiana pola parametru zmienia tylko kopię, a zmienna wywołującego pozostaje taka, jak była:
```c
void reset(Point p) {
    p.x = 0; // changes the copy
}
```
Aby funkcja mogła zmodyfikować strukturę wywołującego, przekaż jej **adres** za pomocą `&` i zadeklaruj parametr jako **wskaźnik**, `Point *p`. Wskaźnik odnosi się do oryginalnej zmiennej, a nie do kopii:
```c
void reset(Point *p) { ... }

reset(&origin);
```
Kopiowanie kosztuje też czas w przypadku dużych struktur, dlatego wskaźniki to zwykły wybór nawet wtedy, gdy nic nie jest modyfikowane.

---

Przez wskaźnik pola osiąga się operatorem **strzałki** `->` zamiast kropki:
```c
void grow(Box *b) {
    b->size = b->size * 2;
}
```
`b->size` to skrót od `(*b).size`: najpierw podążasz za wskaźnikiem, potem bierzesz pole. Kropka działa tylko na strukturze, strzałka tylko na wskaźniku do struktury.
Wywołujący przekazuje adres swojej zmiennej za pomocą `&`, a zmiana dokonana przez wskaźnik jest widoczna po wywołaniu.

---

Funkcja, która otrzymuje wskaźnik do struktury, może zaktualizować oryginalną wartość w miejscu. To standardowy sposób pisania funkcji "modyfikujących" w C, gdzie pierwszy parametr to struktura do zmiany, a pozostałe to dane do zastosowania:
```c
void set_number(Player *p, int new_number) {
    p->number = new_number;
}
```
Odczyt i zapis idą przez tę samą strzałkę: `p->score += 10` dodaje do pola struktury, na którą wskazuje wskaźnik.

---

Funkcja może też **zwracać** strukturę. Zbuduj ją w zmiennej lokalnej i zwróć; wywołujący otrzymuje kopię całej wartości:
```c
Point make_point(int x, int y) {
    Point p = {x, y};
    return p;
}

Point origin = make_point(0, 0);
```
Tak C zwraca z funkcji więcej niż jedną wartość: pakujesz je w strukturę.

---

`sizeof` działa też na strukturach i to właściwy sposób, aby dowiedzieć się, ile pamięci ona zajmuje:
```c
printf("%zu\n", sizeof(Point));
```
Rozmiar jest **co najmniej** sumą rozmiarów pól. Może być większy, ponieważ kompilator może wstawić niewykorzystywane bajty **wypełnienia**, aby każde pole znalazło się pod adresem odpowiednim dla swojego typu: `struct { char c; int n; }` ma zwykle `8` bajtów, a nie `5`. Nigdy nie wpisuj rozmiaru struktury na sztywno; pytaj `sizeof`.

---

Struktur nie można porównywać za pomocą `==`: zapisanie `a == b` dla dwóch struktur to **błąd kompilacji**. Porównuj je zamiast tego **pole po polu**, łącząc wyniki za pomocą `&&`:
```c
bool same_size(Rectangle a, Rectangle b) {
    return a.width == b.width && a.height == b.height;
}
```
To samo dotyczy `<` i `>`: to ty decydujesz, które pole definiuje kolejność.

---

Struktura często przechowuje tekst, zapisany jako pole będące tablicą `char` o stałym rozmiarze:
```c
typedef struct {
    char name[20];
    int age;
} Person;
```
Polu będącemu tablicą nie można przypisać wartości za pomocą `=` po deklaracji: `p.name = "Ann"` się nie skompiluje. Skopiuj do niego tekst za pomocą `strcpy` z `string.h`, przekazując pole jako miejsce docelowe:
```c
Person p;
strcpy(p.name, "Ann");
p.age = 30;
```
Tylko inicjalizator w nawiasach klamrowych przy deklaracji przyjmuje ciąg znaków bezpośrednio: `Person p = {"Ann", 30};`.

---

`printf` nie ma specyfikatora dla całej struktury. Zwykłym rozwiązaniem jest mała funkcja, która wypisuje pola w stałym formacie, dzięki czemu każda część programu pokazuje wartość tak samo:
```c
void print_person(Person p) {
    printf("%s (%d)\n", p.name, p.age);
}
```

---

Łącząc to wszystko: funkcja, która otrzymuje wskaźnik do struktury, może zaktualizować pole tekstowe za pomocą `strcpy` przez strzałkę, ponieważ `item->name` to tablica `char` wewnątrz oryginalnej struktury:
```c
void set_title(Book *book, char *title) {
    strcpy(book->title, title);
}
```
Pamiętaj, aby dodać `#include <string.h>` na początku kodu, żeby używać `strcpy`.
