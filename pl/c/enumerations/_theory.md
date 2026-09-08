**Wyliczenie** (`enum`) nadaje nazwy zbiorowi powiązanych stałych całkowitych, dzięki czemu możesz napisać `RED` zamiast samej liczby.
Deklarujesz je za pomocą słowa kluczowego `enum`, nazwy i listy stałych w nawiasach klamrowych:
```c
enum Color { RED, GREEN, BLUE };
```
Każda stała jest liczbą całkowitą: jeśli nie powiesz inaczej, pierwsza ma wartość `0`, a każda kolejna to poprzednia plus jeden, więc `RED` to `0`, `GREEN` to `1`, a `BLUE` to `2`.
Ponieważ są to liczby całkowite, wypisujesz je za pomocą `%d`:
```c
printf("%d\n", GREEN);
// prints "1"
```

---

Numeracja jest kontynuowana automatycznie dla dowolnej liczby wymienionych stałych: czwarta stała to `3`, piąta to `4` i tak dalej.
Nazwy zwykle pisze się wielkimi literami, tak jak inne stałe, i muszą być unikalne w całym programie: dwa wyliczenia nie mogą mieć wspólnej nazwy stałej.

---

Możesz też nadać stałej jawną wartość za pomocą `=`; stałe po niej dalej liczą od tej wartości:
```c
enum Month { JAN = 1, FEB, MAR }; // FEB is 2, MAR is 3
```
Jawne wartości nie muszą być kolejne ani rosnące: `enum Status { OK = 200, NOT_FOUND = 404 };` jest całkowicie poprawne.

---

Wyliczenie jest też typem: możesz zadeklarować zmienną tego typu, pisząc `enum`, a następnie nazwę wyliczenia, i przypisać jej jedną z jego stałych:
```c
enum Color favorite = GREEN;
```
Ponieważ stałe są liczbami całkowitymi, zmienne typu enum porównuje się zwykłymi operatorami:
```c
if (favorite == GREEN) {
    printf("Green it is\n");
}
```

---

Wyliczenie może być typem parametru funkcji, dokładnie tak jak `int`:
```c
int is_weekend(enum Day day) {
    return day == SAT || day == SUN;
}
```
Wewnątrz funkcji naturalnym sposobem obsługi każdej stałej jest `switch`, ponieważ stałe enum można używać bezpośrednio jako etykiety `case`:
```c
switch (day) {
    case SAT: return 1;
    case SUN: return 1;
    default: return 0;
}
```

---

Gdy każdy przypadek `switch` obsługuje jedną stałą, pamiętaj o `break` po każdym z nich, w przeciwnym razie wykonanie przechodzi do kolejnego przypadku.
Przypadek `default` nie jest wymagany, jeśli obsłużysz wszystkie stałe wyliczenia.

---

Funkcja może też zwracać wyliczenie; wystarczy użyć typu enum jako typu zwracanego i zwrócić jedną z jego stałych:
```c
enum Grade grade_for(int score) {
    if (score >= 60) {
        return PASS;
    }
    return FAIL;
}
```
Zwrócenie nazwanej stałej jest dla wywołującego znacznie czytelniejsze niż zwrócenie samego `0` lub `1`.

---

Pisanie `enum Color` za każdym razem jest rozwlekłe. Za pomocą `typedef` nadajesz wyliczeniu krótką nazwę typu, a samo wyliczenie może pozostać anonimowe:
```c
typedef enum { RED, GREEN, BLUE } Color;

Color favorite = BLUE;
```
Nowa nazwa `Color` jest używana samodzielnie, bez poprzedzającego jej słowa kluczowego `enum`.

---

Stała enum jest automatycznie konwertowana na `int`, więc `int n = BLUE;` jest poprawne i zapisuje `2`.
Odwrotną drogę wykonuje się za pomocą **rzutowania**, wpisując typ enum w nawiasach przed liczbą całkowitą:
```c
enum Color c = (enum Color)1; // c is GREEN
```
C nie sprawdza, czy liczba odpowiada jakiejś stałej: `(enum Color)7` się kompiluje, mimo że żadna stała nie ma wartości `7`, więc zweryfikuj liczby całkowite przed ich konwersją.

---

Arytmetyka na wartości enum daje zwykły `int`: `GREEN + 1` to `2`, a nie `BLUE`.
Aby zapisać wynik z powrotem do zmiennej enum lub zwrócić go z funkcji, zrzutuj go na typ enum:
```c
enum Color after_green = (enum Color)(GREEN + 1); // BLUE
```
W połączeniu z operatorem reszty `%` pozwala to cyklicznie przechodzić przez stałe i wracać do pierwszej.

---

Częstą sztuczką jest dodanie jednej dodatkowej stałej na końcu wyliczenia, zwykle nazwanej `COUNT`: ponieważ numeracja zaczyna się od `0`, jej wartość to dokładnie liczba właściwych stałych przed nią.
```c
enum Day { MON, TUE, WED, DAY_COUNT }; // DAY_COUNT is 3
```
Ten wartownik pozwala przejść pętlą przez wszystkie stałe bez wpisywania liczby na sztywno, i pozostaje poprawny, gdy dodasz stałe przed nim:
```c
for (int d = MON; d < DAY_COUNT; d++) {
    printf("%d\n", d);
}
```

---

Wartownik `COUNT` ma też idealny rozmiar dla tablicy z jednym miejscem na stałą, a stałe stają się czytelnymi indeksami do niej:
```c
enum Fruit { APPLE, BANANA, CHERRY, FRUIT_COUNT };

int stock[FRUIT_COUNT] = {10, 4, 7};
printf("%d\n", stock[BANANA]); // prints "4"
```
Pętla od `0` do `FRUIT_COUNT` odwiedza każde miejsce, a indeks pętli można zrzutować z powrotem na `enum Fruit`, gdy trzeba go zwrócić.

---

C nie udostępnia wbudowanego sposobu na pobranie nazwy stałej wyliczeniowej: `printf("%d\n", SUMMER)` wypisuje `2`, a nie `Summer`. Zwykłym rozwiązaniem jest mała funkcja z instrukcją `switch`, która zwraca odpowiedni napis dla każdej stałej.

---

Wartości enum można przechowywać w tablicach tak jak każdą inną liczbę całkowitą: `enum Fruit basket[] = {APPLE, APPLE, CHERRY};` przechowuje trzy owoce, a każdy element można porównać ze stałą.
