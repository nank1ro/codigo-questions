Każda zmienna znajduje się gdzieś w pamięci, a to miejsce ma numer zwany jej **adresem**. Operator `&`, czytany „adres", podaje adres zmiennej:
```c
int x = 42;
printf("%p\n", &x); // prints something like 0x7ffd5c3e9a4c
```
Specyfikator `%p` wypisuje adres; dokładna liczba zmienia się z uruchomienia na uruchomienie, więc programy nigdy nie polegają na jej wartości.
Adres jest przechowywany w zmiennej będącej **wskaźnikiem**. Wskaźnik deklaruje się, podając typ, na który wskazuje, a po nim `*`:
```c
int *p = &x; // p is a pointer to int, and it holds the address of x
```
Mówi się teraz, że `p` **wskazuje na** `x`. Dwa wskaźniki są równe, gdy przechowują ten sam adres, więc `p == &x` jest prawdą.

---

Sam wskaźnik to tylko adres. Aby odczytać wartość zapisaną pod tym adresem, **wyłuskujesz** wskaźnik operatorem `*`:
```c
int x = 42;
int *p = &x;
printf("%d\n", *p); // prints "42"
```
`*p` znaczy „wartość, na którą wskazuje `p`", i jest to `int`, podobnie jak samo `x`. Ten sam symbol `*` pełni dwie role: w deklaracji `int *p` oznacza „to jest wskaźnik", a w wyrażeniu `*p` prowadzi wskaźnikiem do wartości.

---

Do wyłuskanego wskaźnika można też **przypisywać** wartość. Zapis do `*p` zapisuje nową wartość pod adresem przechowywanym przez `p`, więc zmienna, na którą wskazuje, się zmienia:
```c
int x = 5;
int *p = &x;
*p = 10;
printf("%d\n", x); // prints "10"
```
`x` i `*p` to dwie nazwy tej samej pamięci. Przypisanie do `p` bez `*` zmieniłoby zamiast tego **adres**, który przechowuje wskaźnik, a nie wartość zapisaną pod nim.

---

Wskaźnik, który jeszcze na nic nie wskazuje, powinien przechowywać `NULL` — specjalną stałą zdefiniowaną w `stdio.h` i `stddef.h`, która znaczy „brak adresu":
```c
int *p = NULL;
```
Wyłuskanie wskaźnika `NULL` to błąd wykonania, który powoduje awarię programu, więc wskaźnik, który może być `NULL`, sprawdza się przed użyciem:
```c
if (p != NULL) {
    printf("%d\n", *p);
}
```
Ponieważ `NULL` to zero, `if (p)` to częsty skrót od `if (p != NULL)`. Wskaźnik zadeklarowany bez inicjalizatora przechowuje śmieciowe wartości, a nie `NULL`, więc zawsze inicjalizuj wskaźniki.

---

Wskaźnik może wskazywać na dowolny typ: `double *`, `char *`, `bool *` i tak dalej. Typ w deklaracji mówi kompilatorowi, ile bajtów odczytać przy wyłuskaniu wskaźnika i co one znaczą:
```c
double price = 9.5;
double *p = &price;
*p = *p * 2; // price is now 19.0
```
Wskaźnik musi pasować do typu zmiennej, na którą wskazuje; `int *p = &price;` zostaje odrzucony przez kompilator. `NULL` to jedyna wartość, która pasuje do wskaźnika dowolnego typu.

---

Wskaźnik na `char` działa jak każdy inny wskaźnik: przechowuje adres pojedynczego znaku, a `*p` odczytuje lub zapisuje ten znak:
```c
char grade = 'B';
char *p = &grade;
*p = 'A';
printf("%c\n", grade); // prints "A"
```
Odczyt przez wskaźnik i zapis przez niego można dowolnie łączyć: `*p = *p + 1` zamienia `'A'` na `'B'`.

---

Wskaźnik przechowuje adres, a każdy adres ma ten sam rozmiar na danej maszynie, niezależnie od typu przechowywanego pod nim. `sizeof` wskaźnika jest więc takie samo dla `char *`, `int *` i `double *`: `8` bajtów w systemie 64-bitowym, `4` w 32-bitowym:
```c
printf("%zu\n", sizeof(int *));  // prints "8" on 64-bit
printf("%zu\n", sizeof(double)); // prints "8"
printf("%zu\n", sizeof(char));   // prints "1"
```
Nie myl rozmiaru wskaźnika z rozmiarem tego, na co wskazuje: `sizeof(p)` to rozmiar adresu, a `sizeof(*p)` to rozmiar wartości.

---

Nazwa tablicy użyta w wyrażeniu daje adres jej **pierwszego elementu**, więc można ją przypisać bezpośrednio do wskaźnika:
```c
int numbers[3] = {10, 20, 30};
int *p = numbers; // same as &numbers[0]
```
Dodanie liczby całkowitej do wskaźnika przesuwa go do przodu o tyle **elementów**, nie bajtów: `p + 1` to adres `numbers[1]`, a `*(p + 1)` to `20`. Kompilator skaluje krok o rozmiar typu.
Indeksowanie działa też na wskaźnikach: `p[i]` jest zdefiniowane jako `*(p + i)`, więc `p[2]` to `30`. Nazywa się to **arytmetyką wskaźników**.

---

Skoro `p + 1` to następny element, `p++` przesuwa wskaźnik do następnego elementu w miejscu. Pętla może przechodzić po tablicy, przesuwając wskaźnik zamiast indeksu:
```c
int *p = values;
for (int i = 0; i < 3; i++) {
    printf("%d\n", *p);
    p++;
}
```
W każdym obrocie wypisywany jest element, na który wskazuje `p`, po czym `p` przesuwa się o jeden element do przodu.

---

Gdy tablica jest przekazywana do funkcji, **rozpada się** (decay) na wskaźnik do jej pierwszego elementu. Dlatego parametry `int values[]` i `int *values` oznaczają dokładnie to samo i dlatego funkcja nie może sama poznać długości: otrzymuje tylko adres.
Wskaźniki na tę samą tablicę można porównywać i odejmować. `end - start` to liczba elementów między nimi, a pętla może prowadzić wskaźnik od jednego adresu do drugiego:
```c
for (int *p = start; p < end; p++) {
    printf("%d\n", *p);
}
```
Przekazanie `numbers` i `numbers + 3` opisuje pierwsze trzy elementy bez osobnego parametru rozmiaru.

---

Argumenty funkcji są przekazywane **przez wartość**: funkcja otrzymuje kopię, a przypisanie do parametru nigdy nie zmienia zmiennej wywołującego. Aby funkcja mogła zmienić zmienną, przekaż adres zmiennej i wyłuskaj wskaźnik wewnątrz funkcji:
```c
void reset(int *p) {
    *p = 0;
}

int counter = 7;
reset(&counter); // counter is now 0
```
Klasycznym przykładem jest zamiana dwóch zmiennych, która wymaga tymczasowej kopii jednej wartości, podczas gdy druga jest nadpisywana.

---

Funkcja może zwrócić przez `return` tylko jedną wartość. Aby zwrócić więcej, przyjmuje wskaźniki na zmienne należące do wywołującego i zapisuje przez nie wyniki. Takie parametry nazywa się **parametrami wyjściowymi**:
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
min_max(4, 9, &lo, &hi); // lo is 4, hi is 9
```
Wywołujący deklaruje zmienne, przekazuje ich adresy i po wywołaniu znajduje je wypełnione. Wiele funkcji standardowych używa tego wzorca, dlatego `scanf("%d", &n)` potrzebuje `&`.

---

Wskaźnik na strukturę sięga pól strzałką `->`, a adres struktury zapisanej w tablicy pobiera się przez `&items[i]`. Funkcja może też **zwracać** wskaźnik, na przykład do znalezionego elementu:
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
Wywołujący odczytuje potem pola przez zwrócony wskaźnik za pomocą `->`, po sprawdzeniu, że nie jest to `NULL`. Zwracanie wskaźnika unika kopiowania struktury i pozwala wywołującemu zmodyfikować oryginalny element.

---

`const` może chronić wartość albo wskaźnik, zależnie od tego, gdzie zostało zapisane:
```c
const int *p = &a; // pointer to const: *p cannot be changed, p can point elsewhere
int *const q = &a; // const pointer: q always points to a, but *q can be changed
```
Czytaj deklarację od prawej do lewej: `p` to wskaźnik na stałą typu `int`; `q` to stały wskaźnik na `int`. Wskaźnik na stałą to zwykły sposób obiecania, że funkcja tylko **odczytuje** to, co otrzymuje, jak w `int sum(const int *values, int size)`. Można jej przekazać zwykłą zmienną; obietnica ogranicza tylko to, co funkcja może zrobić.

---

Wskaźnik jest zmienną, więc ma też własny adres, a ten adres można przechować w **wskaźniku do wskaźnika**, deklarowanym z dwiema gwiazdkami:
```c
int x = 7;
int *p = &x;
int **pp = &p;
```
`*pp` to `p`, czyli adres `x`, a `**pp` przechodzi oba kroki, aby dotrzeć do `7`. Wskaźniki do wskaźników pozwalają funkcji zmienić adres przechowywany przez wskaźnik: otrzymuje `&p` i przypisuje do `*pp`.

---

Połączenie wszystkiego razem: funkcja, która przechodzi po tablicy wskaźnikiem, przechowuje wskaźnik na najlepszy dotychczasowy element i zwraca go, albo `NULL`, gdy nie ma czego zwrócić:
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
Wywołujący porównuje wynik z `NULL` przed jego wyłuskaniem i może użyć `result - values`, aby odzyskać indeks elementu.
