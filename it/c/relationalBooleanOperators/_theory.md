Gli **operatori relazionali** confrontano due valori. Il risultato non è un tipo speciale: è un `int` che vale `1` quando il confronto è vero e `0` quando non lo è. C ne ha sei:
```c
printf("%d\n", 5 == 5); // equal: prints "1"
printf("%d\n", 5 != 5); // not equal: prints "0"
printf("%d\n", 3 < 5);  // less than: prints "1"
printf("%d\n", 3 > 5);  // greater than: prints "0"
printf("%d\n", 5 <= 5); // less than or equal: prints "1"
printf("%d\n", 4 >= 5); // greater than or equal: prints "0"
```
Poiché il risultato è un `int`, viene stampato con `%d` e può essere memorizzato in una variabile `int` come qualsiasi altro numero.

---

Una funzione può restituire direttamente un confronto: il chiamante riceve `1` o `0`.
```c
int is_big(int n) {
    return n > 100;
}

printf("%d\n", is_big(250)); // prints "1"
```
Scegliere tra `>` e `>=` (oppure `<` e `<=`) decide se il valore limite conta: `n >= 100` vale `1` per `100`, `n > 100` vale `0`.

---

L'errore più comune in C è scrivere `=` dove si intendeva `==`. Un singolo `=` è un'**assegnazione**, e in C un'assegnazione è un'espressione il cui valore è il valore assegnato:
```c
int x = 3;
printf("%d\n", x == 7); // compares: prints "0", x is still 3
printf("%d\n", x = 7);  // assigns: prints "7", x is now 7
```
Il codice con `=` compila comunque, quindi una condizione scritta come `if (x = 0)` imposta silenziosamente `x` a `0` invece di verificarlo. La maggior parte dei compilatori stampa un avviso per questo: leggilo.

---

Gli **operatori logici** combinano condizioni. L'operatore **and** `&&` dà `1` solo quando entrambi i lati sono veri, l'operatore **or** `||` dà `1` quando almeno un lato è vero:
```c
int t = 25;
printf("%d\n", t > 20 && t < 30); // prints "1"
printf("%d\n", t < 20 || t > 30); // prints "0"
```
In C **qualsiasi valore diverso da zero conta come vero** e solo `0` conta come falso, quindi `5 && 1` vale `1` e `0 || -3` vale `1`. Il risultato di `&&` e `||` è sempre esattamente `1` o `0`.

---

Una variabile che contiene `0` o un valore diverso da zero può essere usata da sola come condizione: `holiday` da solo significa "holiday è diverso da zero", non serve scrivere `holiday != 0`.
```c
int is_open(int weekday, int holiday) {
    return weekday && !holiday;
}
```
L'operatore **not** `!` inverte una condizione: `!0` vale `1` e `!` di qualsiasi valore diverso da zero vale `0`.

---

Poiché `!` trasforma qualsiasi valore diverso da zero in `0` e `0` in `1`, applicarlo due volte normalizza un valore esattamente a `0` o `1`: `!!42` vale `1`, `!!0` vale `0`.
```c
int count = 3;
printf("%d %d\n", !count, !!count); // prints "0 1"
```
Questo è utile quando una funzione restituisce un numero arbitrario diverso da zero e vuoi un `1` pulito.

---

Dal C99 l'header `stdbool.h` fornisce il tipo `bool` e le costanti `true` (che vale `1`) e `false` (che vale `0`):
```c
#include <stdbool.h>

bool open = true;
bool full = 3 > 5;
printf("%d %d\n", open, full); // prints "1 0"
```
Un `bool` è comunque un intero sotto il cofano: viene stampato con `%d` e funziona con `&&`, `||` e `!` esattamente come il risultato di un confronto. Rende solo l'intento più chiaro di un semplice `int`.

---

Una funzione che risponde a una domanda sì/no dovrebbe restituire `bool`. Un parametro `bool` è già una condizione, quindi usalo direttamente come operando di `&&` o `||`: scrivi `age >= 18 && citizen`, non `citizen == true`.
```c
bool can_enter(int age, bool member) {
    return age >= 16 && member;
}
```
`stdbool.h` è già incluso sopra il tuo codice in questi esercizi.

---

`&&` e `||` usano la **valutazione a corto circuito**: si fermano appena il risultato è noto.
- con `&&`, se il lato sinistro è `0` il lato destro non viene mai valutato
- con `||`, se il lato sinistro è diverso da zero il lato destro non viene mai valutato

Questo permette a un controllo a sinistra di proteggere un'operazione pericolosa a destra:
```c
int ok = count != 0 && total / count > 2;
```
Quando `count` è `0`, la divisione non viene mai eseguita, quindi il programma non va in crash.

---

La valutazione a corto circuito salta anche le chiamate di funzione. In `1 || check()` la funzione `check` non viene mai chiamata, quindi qualsiasi suo effetto collaterale, come aggiornare un contatore, non avviene.
```c
int calls = 0;

int check() {
    calls++;
    return 1;
}
```
Tienilo a mente quando una funzione sul lato destro di `&&` o `||` fa qualcosa su cui fai affidamento.

---

Gli operatori hanno una **precedenza** che decide cosa viene calcolato per primo:
1. `!` viene applicato per primo
2. poi i confronti relazionali `<`, `>`, `<=`, `>=`
3. poi i confronti di uguaglianza `==`, `!=`
4. poi `&&`
5. poi `||`

Quindi `a > 0 && a < 10` non ha bisogno di parentesi, e `a && b || c` significa `(a && b) || c` perché `&&` lega più strettamente di `||`. Usa le parentesi per forzare un raggruppamento diverso o semplicemente per rendere l'intento leggibile.

---

Un `char` è un piccolo intero, quindi i caratteri si confrontano con gli stessi operatori. Confronta con un letterale di carattere tra apici singoli: `"a"` con doppi apici è una stringa, che non può essere confrontata in questo modo.
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // prints "1"
```
Caratteri consecutivi come `'0'`, `'1'`, ... `'9'` oppure `'a'`, `'b'`, ... `'z'` hanno codici consecutivi, quindi un controllo di intervallo sui caratteri funziona esattamente come uno sui numeri:
```c
bool is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Non concatenare i confronti come in matematica. `1 <= x <= 10` compila, ma viene valutato come `(1 <= x) <= 10`: il primo confronto dà `0` o `1`, e quello viene poi confrontato con `10`, quindi l'intera espressione vale sempre `1`.
```c
int x = 20;
printf("%d\n", 1 <= x <= 10);       // prints "1" (wrong!)
printf("%d\n", 1 <= x && x <= 10);  // prints "0"
```
Scrivi sempre entrambi i confronti esplicitamente e uniscili con `&&`.

---

Quando una condizione mescola `&&` e `||`, raggruppa ogni parte con le parentesi anche quando la precedenza farebbe già la cosa giusta: la regola diventa leggibile a colpo d'occhio.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
L'operatore resto `%` si abbina naturalmente con `==`: `n % 4 == 0` vale `1` quando `n` è divisibile per `4`.
