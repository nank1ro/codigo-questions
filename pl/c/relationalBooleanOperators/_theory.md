**Operatory relacyjne** porównują dwie wartości. Wynik nie jest specjalnym typem: to `int`, którego wartość wynosi `1`, gdy porównanie jest spełnione, i `0`, gdy nie jest. C ma ich sześć:
```c
printf("%d\n", 5 == 5); // equal: prints "1"
printf("%d\n", 5 != 5); // not equal: prints "0"
printf("%d\n", 3 < 5);  // less than: prints "1"
printf("%d\n", 3 > 5);  // greater than: prints "0"
printf("%d\n", 5 <= 5); // less than or equal: prints "1"
printf("%d\n", 4 >= 5); // greater than or equal: prints "0"
```
Ponieważ wynik jest typu `int`, jest wypisywany za pomocą `%d` i może być przechowany w zmiennej typu `int` jak każda inna liczba.

---

Funkcja może zwrócić porównanie bezpośrednio: wywołujący otrzymuje `1` lub `0`.
```c
int is_big(int n) {
    return n > 100;
}

printf("%d\n", is_big(250)); // prints "1"
```
Wybór między `>` a `>=` (lub `<` a `<=`) decyduje, czy wartość graniczna się liczy: `n >= 100` daje `1` dla `100`, a `n > 100` daje `0`.

---

Najczęstszym błędem w C jest napisanie `=` tam, gdzie chodziło o `==`. Pojedynczy `=` to **przypisanie**, a w C przypisanie jest wyrażeniem, którego wartością jest przypisywana wartość:
```c
int x = 3;
printf("%d\n", x == 7); // compares: prints "0", x is still 3
printf("%d\n", x = 7);  // assigns: prints "7", x is now 7
```
Kod z `=` nadal się kompiluje, więc warunek zapisany jako `if (x = 0)` po cichu ustawia `x` na `0` zamiast go sprawdzać. Większość kompilatorów wypisuje przy tym ostrzeżenie: przeczytaj je.

---

**Operatory logiczne** łączą warunki. Operator **koniunkcji** (and) `&&` daje `1` tylko wtedy, gdy obie strony są prawdziwe, a operator **alternatywy** (or) `||` daje `1`, gdy co najmniej jedna strona jest prawdziwa:
```c
int t = 25;
printf("%d\n", t > 20 && t < 30); // prints "1"
printf("%d\n", t < 20 || t > 30); // prints "0"
```
W C **każda niezerowa wartość liczy się jako prawda**, a tylko `0` liczy się jako fałsz, więc `5 && 1` to `1`, a `0 || -3` to `1`. Wynik `&&` i `||` to zawsze dokładnie `1` lub `0`.

---

Zmienna przechowująca `0` lub wartość niezerową może sama w sobie pełnić rolę warunku: samo `holiday` oznacza „holiday jest niezerowe”, nie ma potrzeby pisania `holiday != 0`.
```c
int is_open(int weekday, int holiday) {
    return weekday && !holiday;
}
```
Operator **negacji** (not) `!` odwraca warunek: `!0` to `1`, a `!` zastosowane do dowolnej niezerowej wartości daje `0`.

---

Ponieważ `!` zamienia dowolną niezerową wartość na `0`, a `0` na `1`, zastosowanie go dwukrotnie normalizuje wartość do dokładnie `0` lub `1`: `!!42` to `1`, a `!!0` to `0`.
```c
int count = 3;
printf("%d %d\n", !count, !!count); // prints "0 1"
```
Jest to przydatne, gdy funkcja zwraca dowolną niezerową liczbę, a ty chcesz otrzymać czyste `1`.

---

Od C99 nagłówek `stdbool.h` dostarcza typ `bool` oraz stałe `true` (czyli `1`) i `false` (czyli `0`):
```c
#include <stdbool.h>

bool open = true;
bool full = 3 > 5;
printf("%d %d\n", open, full); // prints "1 0"
```
Typ `bool` pod spodem nadal jest liczbą całkowitą: jest wypisywany za pomocą `%d` i działa z `&&`, `||` oraz `!` dokładnie jak wynik porównania. Po prostu lepiej oddaje intencje niż zwykły `int`.

---

Funkcja odpowiadająca na pytanie tak/nie powinna zwracać `bool`. Parametr typu `bool` to już gotowy warunek, więc używaj go bezpośrednio jako operandu `&&` lub `||`: pisz `age >= 18 && citizen`, a nie `citizen == true`.
```c
bool can_enter(int age, bool member) {
    return age >= 16 && member;
}
```
W tych zadaniach `stdbool.h` jest już dołączone nad twoim kodem.

---

`&&` i `||` stosują **ocenę skróconą (short-circuit)**: przerywają obliczenia, gdy tylko wynik jest już znany.
- przy `&&`, jeśli lewa strona to `0`, prawa strona nigdy nie jest obliczana
- przy `||`, jeśli lewa strona jest niezerowa, prawa strona nigdy nie jest obliczana

Dzięki temu sprawdzenie po lewej stronie chroni niebezpieczną operację po prawej:
```c
int ok = count != 0 && total / count > 2;
```
Gdy `count` wynosi `0`, dzielenie nigdy nie jest wykonywane, więc program nie ulega awarii.

---

Ocena skrócona pomija również wywołania funkcji. W `1 || check()` funkcja `check` nigdy nie jest wywoływana, więc żaden jej efekt uboczny, na przykład aktualizacja licznika, nie zachodzi.
```c
int calls = 0;

int check() {
    calls++;
    return 1;
}
```
Miej to na uwadze, gdy funkcja po prawej stronie `&&` lub `||` robi coś, na czym twoja logika polega.

---

Operatory mają **pierwszeństwo**, które decyduje, co jest obliczane najpierw:
1. najpierw stosowane jest `!`
2. następnie porównania relacyjne `<`, `>`, `<=`, `>=`
3. następnie porównania równości `==`, `!=`
4. następnie `&&`
5. następnie `||`

Zatem `a > 0 && a < 10` nie potrzebuje nawiasów, a `a && b || c` znaczy `(a && b) || c`, ponieważ `&&` wiąże mocniej niż `||`. Używaj nawiasów, aby wymusić inne grupowanie albo po prostu, aby intencja była czytelna.

---

`char` to mała liczba całkowita, więc znaki porównuje się tymi samymi operatorami. Porównuj z literałem znakowym w pojedynczych cudzysłowach: `"a"` w podwójnych cudzysłowach to ciąg znaków, którego nie da się w ten sposób porównywać.
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // prints "1"
```
Kolejne znaki, takie jak `'0'`, `'1'`, ... `'9'` czy `'a'`, `'b'`, ... `'z'`, mają kolejne kody, więc sprawdzenie zakresu na znakach działa dokładnie tak samo jak na liczbach:
```c
bool is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Nie łącz porównań w łańcuch jak w matematyce. `1 <= x <= 10` się kompiluje, ale jest obliczane jako `(1 <= x) <= 10`: pierwsze porównanie daje `0` lub `1`, a to jest następnie porównywane z `10`, więc całe wyrażenie ma zawsze wartość `1`.
```c
int x = 20;
printf("%d\n", 1 <= x <= 10);       // prints "1" (wrong!)
printf("%d\n", 1 <= x && x <= 10);  // prints "0"
```
Zawsze pisz oba porównania jawnie i łącz je za pomocą `&&`.

---

Gdy warunek miesza `&&` i `||`, grupuj każdą część nawiasami, nawet gdy pierwszeństwo samo dałoby właściwy wynik: reguła staje się czytelna na pierwszy rzut oka.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
Operator reszty `%` naturalnie łączy się z `==`: `n % 4 == 0` to `1`, gdy `n` jest podzielne przez `4`.
