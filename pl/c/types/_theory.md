C jest językiem **statycznie typowanym**: każda zmienna jest deklarowana z typem, który decyduje o tym, co może przechowywać i ile zajmuje pamięci.
Trzy typy, których będziesz używać najczęściej, to:
- `int` dla liczb całkowitych, jak `30` czy `-4`
- `double` dla liczb z częścią ułamkową, jak `1.75`
- `char` dla pojedynczego znaku, zapisywanego w apostrofach jak `'A'`

Każdy typ ma swój własny **specyfikator formatu** funkcji `printf`: `%d` wypisuje `int`, `%f` wypisuje `double` (domyślnie z sześcioma miejscami po przecinku), a `%c` wypisuje `char`:
```c
int age = 30;
double height = 1.75;
char initial = 'A';
printf("%d %f %c\n", age, height, initial);
// prints "30 1.750000 A"
```
Użycie złego specyfikatora dla danego typu wypisze śmieci, więc zawsze je dopasowuj.

---

C ma dwa typy zmiennoprzecinkowe: `float` (pojedyncza precyzja, około 7 cyfr znaczących) i `double` (podwójna precyzja, około 15 cyfr znaczących).
Literał dziesiętny taki jak `1.75` jest typu `double`; aby zapisać literał `float`, dodaj przyrostek `f`, jak w `1.75f`.
Preferuj `double`, chyba że pamięć jest ograniczona: jest to typ domyślny i bardziej precyzyjny.
```c
double pi = 3.14159;
float ratio = 0.5f;
```
Funkcja zwracająca wynik dziesiętny powinna deklarować `double` jako typ zwracany, a parametry typu `double` przyjmują zarówno argumenty całkowite, jak i dziesiętne:
```c
double half(double x) {
    return x / 2;
}
```

---

`%f` wypisuje sześć miejsc po przecinku, co rzadko jest tym, czego chcesz. Umieść precyzję między `%` a `f`, aby wybrać liczbę wyświetlanych miejsc dziesiętnych: `%.2f` wypisuje dwa miejsca, `%.1f` wypisuje jedno, a wartość jest **zaokrąglana**, a nie obcinana:
```c
double price = 9.987;
printf("%.2f\n", price); // prints "9.99"
printf("%.1f\n", price); // prints "10.0"
```
`float` jest wypisywany za pomocą tych samych specyfikatorów co `double`: przy przekazaniu do `printf` jest automatycznie konwertowany na `double`.

---

Wynik `/` zależy od typów jego argumentów.
Gdy **oba** argumenty są liczbami całkowitymi, wynik jest liczbą całkowitą, a część ułamkowa jest odrzucana: `7 / 2` to `3`, a nie `3.5`.
Gdy **przynajmniej jeden** argument jest wartością zmiennoprzecinkową, dzielenie zachowuje część ułamkową: `7 / 2.0` to `3.5`.
```c
printf("%d\n", 7 / 2);     // prints "3"
printf("%f\n", 7 / 2.0);   // prints "3.500000"
```
Zapisanie literału jako `2.0` zamiast `2` to najprostszy sposób na wymuszenie dzielenia zmiennoprzecinkowego.

---

C konwertuje między typami liczbowymi **niejawnie**, gdy wartość jest przypisywana do zmiennej innego typu.
- `int` przechowywany w `double` jest rozszerzany bez strat: `double d = 3;` sprawia, że `d` jest równe `3.0`
- `double` przechowywany w `int` jest **obcinany**: `int n = 3.99;` sprawia, że `n` jest równe `3` (kompilatory zwykle ostrzegają o tym)

Konwersja zachodzi tylko w momencie przypisania. Wyrażenie po prawej stronie jest obliczane najpierw, z użyciem swoich własnych typów:
```c
double d = 7 / 2;
```
Tutaj `7 / 2` to dzielenie całkowitoliczbowe, które daje `3`, i dopiero potem `3` jest konwertowane na `3.0`.

---

Gdy niejawna konwersja nie jest tym, czego chcesz, albo chcesz ją uwidocznić, użyj **jawnego rzutowania**: zapisz docelowy typ w nawiasach przed wartością.
```c
double x = 3.99;
int n = (int) x;   // n is 3
```
Rzutowanie wartości zmiennoprzecinkowej na `int` **obcina w kierunku zera**: `(int) 3.99` to `3`, a `(int) -2.5` to `-2`, żadne zaokrąglanie nie zachodzi.
Rzutowanie dotyczy tylko wartości bezpośrednio po nim, więc `(int) x * 2` najpierw rzutuje `x`, a potem mnoży.

---

Rzutowanie to standardowy sposób na uzyskanie dzielenia zmiennoprzecinkowego z dwóch zmiennych `int`: zrzutuj **jeden argument** na `double` przed dzieleniem.
```c
int total = 7, count = 2;
double avg = (double) total / count; // 3.5
```
Rzutowanie całego wyniku, jak w `(double) (total / count)`, to częsty błąd: dzielenie całkowitoliczbowe już się odbyło i część ułamkowa została utracona.

---

`char` to tak naprawdę mała liczba całkowita: przechowuje **kod ASCII** znaku.
`'A'` to `65`, `'a'` to `97`, a `'0'` to `48`, a kolejne znaki mają kolejne kody.
Dlatego można wykonywać arytmetykę na znakach:
- `'a' + 1` to `98`, kod znaku `'b'`
- `'7' - '0'` to `55 - 48`, czyli liczba `7`

Ta sama wartość może być wypisana jako znak za pomocą `%c` lub jako liczba za pomocą `%d`:
```c
char c = 'A';
printf("%c %d\n", c, c); // prints "A 65"
```

---

Wielkie i małe litery są oddalone o `32` pozycje w tabeli ASCII: `'A'` to `65`, a `'a'` to `97`.
Odjęcie `32` od małej litery daje więc jej wielką wersję, a wynik można zapisać z powrotem w `char`:
```c
char upper = 'g' - 32; // 'G'
```

---

`int` nie jest jedynym typem całkowitym. Modyfikatory zmieniają jego rozmiar i zakres:
- `short` zużywa mniej pamięci i ma mniejszy zakres (zwykle od -32768 do 32767)
- `long` ma większy zakres (na systemach 64-bitowych około ±9 trylionów)
- `unsigned` usuwa znak: `unsigned int` przyjmuje wartości od `0` do około 4 miliardów, ale nigdy nie może być ujemny

Literał, który musi być typu `long`, otrzymuje przyrostek `L`, `unsigned` — przyrostek `U`, a każdy typ ma swój własny specyfikator:
```c
long population = 8000000000L;
unsigned int count = 40U;
printf("%ld %u\n", population, count); // prints "8000000000 40"
```
`%ld` wypisuje `long`, `%u` — `unsigned int`, a `%lu` — `unsigned long`. Zwykły `int` na większości systemów przechowuje wartości do około 2 miliardów, więc `5000000000` się w nim nie mieści.

---

Operator `sizeof` mówi, ile **bajtów** zajmuje typ lub zmienna. Jego wynik ma typ `size_t`, który wypisuje się za pomocą `%zu`:
```c
printf("%zu\n", sizeof(int));  // prints "4" on most systems
```
Standard gwarantuje jedynie, że `sizeof(char)` wynosi `1` oraz że `short <= int <= long`, ale na typowym systemie 64-bitowym rozmiary wynoszą: `char` 1, `short` 2, `int` 4, `long` 8, `float` 4, `double` 8.
`sizeof` jest często używany do sprawdzenia, ile pamięci zajmuje zmienna, bez zapisywania tej liczby na sztywno w kodzie.

---

Każdy typ całkowity ma ograniczony zakres, a nagłówek `limits.h` nadaje tym granicom nazwy: `INT_MAX` i `INT_MIN` dla `int`, `LONG_MAX` dla `long`, `UINT_MAX` dla `unsigned int` i tak dalej.
```c
#include <limits.h>

printf("%d\n", INT_MAX); // prints "2147483647" on most systems
```
Przekroczenie `INT_MAX` przy typie ze znakiem to **zachowanie niezdefiniowane**: program może się zawinąć, ulec awarii lub zrobić cokolwiek innego. Sprawdź przed obliczeniem:
```c
if (a <= INT_MAX - b) { /* a + b is safe */ }
```
Zauważ, że sprawdzenie odejmuje zamiast dodawać, ponieważ samo `a + b` mogłoby już spowodować przepełnienie.

---

W przeciwieństwie do typów ze znakiem, arytmetyka **unsigned** jest dobrze zdefiniowana, gdy wykracza poza zakres: wartość **zawija się**, jak licznik przebiegu.
Dodanie `1` do `UINT_MAX` daje `0`, a odjęcie `1` od `0` daje `UINT_MAX` (`4294967295`, gdy `unsigned int` ma 32 bity):
```c
unsigned int n = UINT_MAX;
n = n + 1;
printf("%u\n", n); // prints "0"
```
Dlatego pętla, która zmniejsza zmienną `unsigned` "aż stanie się ujemna", nigdy się nie zatrzymuje: wartość unsigned nigdy nie spada poniżej `0`.

---

Od C99 nagłówek `stdbool.h` udostępnia typ `bool` ze stałymi `true` (`1`) i `false` (`0`).
`bool` to typ całkowity z tylko dwiema wartościami, więc konwersja dowolnej liczby na `bool` daje `true` dla każdej wartości niezerowej i `false` dla `0`. Różni się to od konwersji na `int`:
```c
#include <stdbool.h>

bool b = 0.5;  // true, because 0.5 is not zero
int n = 0.5;   // 0, because the decimals are truncated
```
Porównania takie jak `x != 0` już dają wynik zgodny z `bool`, a funkcja zwracająca `bool` dokumentuje, że odpowiada na pytanie tak/nie.

---

Operacja arytmetyczna jest wykonywana w typie swoich argumentów, **a nie** w typie zmiennej, która otrzymuje wynik.
Tak więc `long big = n * n;` z `n` typu `int` mnoży dwie wartości `int`, powoduje przepełnienie, jeśli iloczyn jest zbyt duży, i dopiero potem zapisuje (już błędny) wynik w `long`.
Zrzutuj jeden argument **przed** operacją, aby obliczenia odbyły się w szerszym typie:
```c
int n = 100000;
long big = (long) n * n; // 10000000000, computed as long
```
Ta sama zasada wyjaśnia, dlaczego działa `(double) total / count`: rzutowanie zmienia typ argumentu, a dzielenie się do niego dostosowuje.

---

Podsumowanie: wybieraj typ na podstawie rodzaju wartości, dopasuj każdy specyfikator `printf` do typu jego argumentu i rzutuj, gdy obliczenie musi odbyć się w innym typie niż typ jego argumentów.
