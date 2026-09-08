**Operatory porównania** porównują dwie wartości i dają wynik: `1`, gdy porównanie jest prawdziwe, i `0`, gdy nie jest.
Operator **równości** `==` sprawdza, czy dwie wartości są takie same, a operator **różności** `!=` sprawdza, czy się różnią:
```c
int a = 7, b = 3;
printf("%d\n", a == b);
// wypisuje "0"
printf("%d\n", a != b);
// wypisuje "1"
```
Uważaj: `==` (dwa znaki) porównuje, a pojedyncze `=` przypisuje wartość.

---

Pozostałe operatory porównania sprawdzają kolejność dwóch wartości:
- `<` mniejsze niż, `>` większe niż
- `<=` mniejsze lub równe, `>=` większe lub równe
```c
printf("%d\n", 3 < 5);  // wypisuje "1"
printf("%d\n", 5 >= 6); // wypisuje "0"
```
Funkcja może zwrócić wynik porównania bezpośrednio, ponieważ jest to zwykły `int`:
```c
int is_big(int n) {
    return n > 100;
}
```

---

W C wynik porównania nie jest specjalnym typem: to `int`, którego wartość wynosi dokładnie `1` (prawda) lub `0` (fałsz).
Oznacza to, że możesz przechować go w zmiennej typu `int` jak każdą inną liczbę:
```c
int n = 42;
int big = n > 100; // big wynosi 0
```
W wyniku nie pojawia się słowo `true`/`false`: `printf("%d", 2 == 2)` wypisuje `1`.

---

**Operatory logiczne** łączą porównania. Operator **i** `&&` daje `1` tylko wtedy, gdy obie strony są prawdziwe:
```c
int age = 25;
printf("%d\n", age >= 18 && age < 65); // wypisuje "1"
```
Nie łącz porównań tak jak w matematyce: `1 <= x <= 10` jest obliczane jako `(1 <= x) <= 10`, co porównuje `0` lub `1` z `10` i zawsze daje prawdę.
Zawsze zapisuj oba porównania osobno i łącz je za pomocą `&&`.

---

Operator **lub** `||` daje `1`, gdy przynajmniej jedna strona jest prawdziwa, i `0` tylko wtedy, gdy obie strony są fałszywe:
```c
int day = 1;
printf("%d\n", day == 1 || day == 7); // wypisuje "1"
```
Każda strona musi być pełnym porównaniem: `day == 6 || 7` nie oznacza "6 lub 7" (dowiesz się dlaczego później).

---

Operator **negacji** `!` odwraca wynik: `!1` to `0`, a `!0` to `1`.
Jest umieszczany przed wyrażeniem, więc użyj nawiasów, aby zanegować całe porównanie:
```c
int n = 5;
printf("%d\n", !(n > 3)); // wypisuje "0"
```
Bez nawiasów `!n > 3` najpierw obliczyłoby `!n`, a potem porównałoby to z `3`.

---

Operatory logiczne działają nie tylko na `0` i `1`: w C **każda wartość różna od zera liczy się jako prawda**, a tylko `0` liczy się jako fałsz.
Dlatego `5 && 1` to `1`, `0 || -3` to `1`, a `!` zamienia każdą wartość różną od zera na `0`:
```c
printf("%d\n", !7); // wypisuje "0"
printf("%d\n", !0); // wypisuje "1"
```
Dlatego `day == 6 || 7` jest zawsze prawdziwe: samo `7` jest już wartością prawdziwą.

---

`&&` i `||` używają **oceny skróconej (short-circuit)**: przerywają obliczenia, gdy tylko wynik jest już znany.
- w przypadku `&&`, jeśli lewa strona to `0`, prawa strona nigdy nie jest obliczana
- w przypadku `||`, jeśli lewa strona jest prawdziwa, prawa strona nigdy nie jest obliczana

Dzięki temu możesz zabezpieczyć niebezpieczną operację, umieszczając warunek po jej lewej stronie:
```c
int safe = divisor != 0 && value / divisor > 2;
```
Gdy `divisor` wynosi `0`, dzielenie nigdy nie jest wykonywane.

---

Ocena skrócona pomija także wywołania funkcji: w `0 && check()` funkcja `check` nigdy nie zostaje wywołana, więc żaden jej efekt uboczny (np. aktualizacja licznika) nie zachodzi.

---

Operatory mają **pierwszeństwo**, które decyduje, co jest obliczane najpierw:
1. najpierw stosowane jest `!`
2. potem porównania relacyjne `<`, `>`, `<=`, `>=`
3. potem porównania równości `==`, `!=`
4. potem `&&`
5. potem `||`

Dlatego `a > 0 && a < 10` nie potrzebuje nawiasów: oba porównania są obliczane przed `&&`.
A `x == 1 || y == 2 && z == 3` oznacza `x == 1 || (y == 2 && z == 3)`, ponieważ `&&` wiąże silniej niż `||`.

---

`char` to mała liczba całkowita, więc znaki można porównywać tymi samymi operatorami.
Porównuj z literałem znakowym w pojedynczych cudzysłowach:
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // wypisuje "1"
```
Podwójne cudzysłowy utworzyłyby string, którego nie można porównać w ten sposób.

---

Ponieważ znaki są liczbami, `<` i `>` porównują ich kody, a kolejne znaki, takie jak `'a'`, `'b'`, `'c'` lub `'0'`, `'1'`, `'2'`, mają kolejne kody.
Sprawdzanie zakresu na znakach działa więc dokładnie tak samo jak na liczbach:
```c
int is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Klasyczny błąd w C to napisanie `=` zamiast zamierzonego `==`. Kod nadal się kompiluje, ponieważ przypisanie jest wyrażeniem, którego wartością jest przypisana wartość:
```c
int x = 5;
if (x = 0) { ... } // przypisuje 0 do x, warunek to 0 (fałsz)
if (x = 3) { ... } // przypisuje 3 do x, warunek to 3 (prawda)
```
Większość kompilatorów ostrzega przed tym, więc czytaj ostrzeżenia, gdy warunek zachowuje się dziwnie.

---

Warunek `if` to po prostu wyrażenie, które jest traktowane jako prawdziwe, gdy jest różne od zera, więc porównania i operatory logiczne pasują tu naturalnie:
```c
if (n < 0) {
    printf("negative\n");
} else if (n == 0) {
    printf("zero\n");
}
```
Możesz też najpierw zapisać wynik w zmiennej i sprawdzić ją: `int ok = n > 0; if (ok) { ... }`.

---

Pętla `while` działa dopóki jej warunek jest różny od zera, więc to porównanie decyduje, kiedy się zatrzyma:
```c
int i = 0;
while (i < 3) {
    printf("%d\n", i);
    i++;
}
// wypisuje 0, 1, 2
```
Wybór między `<` a `<=` decyduje o tym, czy ostatnia wartość zostanie uwzględniona.

---

Od C99 nagłówek `stdbool.h` udostępnia typ `bool` oraz stałe `true` (`1`) i `false` (`0`):
```c
#include <stdbool.h>

bool ready = true;
bool done = count == 10;
```
`bool` w środku wciąż jest liczbą całkowitą: wypisanie go za pomocą `%d` pokazuje `1` lub `0`, i działa on z `&&`, `||` i `!` tak jak każdy wynik porównania.
Użycie `bool` sprawia, że intencja funkcji jest jaśniejsza niż zwracanie zwykłego `int`.

---

Parametr typu `bool` może być użyty bezpośrednio jako operand `&&` lub `||`, bez porównywania go z `true`: napisz `age >= 18 && citizen`, a nie `citizen == true`.

---

Gdy warunek łączy `&&` i `||`, dodaj nawiasy wokół każdej grupy, nawet jeśli pierwszeństwo operatorów i tak zadziałałoby poprawnie: dzięki temu reguła jest czytelna na pierwszy rzut oka.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
