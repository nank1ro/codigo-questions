Gli **operatori di confronto** confrontano due valori e producono una risposta: `1` quando il confronto è vero e `0` quando non lo è.
L'operatore di **uguaglianza** `==` verifica se due valori sono uguali, l'operatore di **disuguaglianza** `!=` verifica se sono diversi:
```c
int a = 7, b = 3;
printf("%d\n", a == b);
// stampa "0"
printf("%d\n", a != b);
// stampa "1"
```
Attenzione: `==` (due segni) confronta, mentre un singolo `=` assegna un valore.

---

Gli altri operatori di confronto verificano l'ordine tra due valori:
- `<` minore di, `>` maggiore di
- `<=` minore o uguale a, `>=` maggiore o uguale a
```c
printf("%d\n", 3 < 5);  // stampa "1"
printf("%d\n", 5 >= 6); // stampa "0"
```
Una funzione può restituire un confronto direttamente, perché il risultato è un semplice `int`:
```c
int is_big(int n) {
    return n > 100;
}
```

---

In C il risultato di un confronto non è un tipo speciale: è un `int` il cui valore è esattamente `1` (vero) o `0` (falso).
Ciò significa che puoi memorizzarlo in una variabile `int` come qualsiasi altro numero:
```c
int n = 42;
int big = n > 100; // big è 0
```
Non esiste la parola `true`/`false` nell'output: `printf("%d", 2 == 2)` stampa `1`.

---

Gli **operatori logici** combinano confronti. L'operatore **and** `&&` dà `1` solo quando entrambi i lati sono veri:
```c
int age = 25;
printf("%d\n", age >= 18 && age < 65); // stampa "1"
```
Non concatenare i confronti come in matematica: `1 <= x <= 10` viene valutato come `(1 <= x) <= 10`, che confronta uno `0` o `1` con `10` ed è sempre vero.
Scrivi sempre i due confronti in modo esplicito e uniscili con `&&`.

---

L'operatore **or** `||` dà `1` quando almeno un lato è vero, e `0` solo quando entrambi i lati sono falsi:
```c
int day = 1;
printf("%d\n", day == 1 || day == 7); // stampa "1"
```
Ogni lato deve essere un confronto completo: `day == 6 || 7` non significa "6 o 7" (vedrai perché più avanti).

---

L'operatore **not** `!` inverte un risultato: `!1` è `0` e `!0` è `1`.
Si trova davanti all'espressione, quindi usa le parentesi per negare un intero confronto:
```c
int n = 5;
printf("%d\n", !(n > 3)); // stampa "0"
```
Senza le parentesi, `!n > 3` calcolerebbe prima `!n` e poi lo confronterebbe con `3`.

---

Gli operatori logici non funzionano solo con `0` e `1`: in C **qualsiasi valore diverso da zero conta come vero** e solo `0` conta come falso.
Quindi `5 && 1` è `1`, `0 || -3` è `1`, e `!` trasforma qualsiasi valore diverso da zero in `0`:
```c
printf("%d\n", !7); // stampa "0"
printf("%d\n", !0); // stampa "1"
```
Ecco perché `day == 6 || 7` è sempre vero: `7` da solo è già un valore vero.

---

`&&` e `||` usano la **valutazione a corto circuito**: si fermano non appena il risultato è noto.
- con `&&`, se il lato sinistro è `0` il lato destro non viene mai valutato
- con `||`, se il lato sinistro è vero il lato destro non viene mai valutato

Questo permette di proteggere un'operazione pericolosa con un controllo posto alla sua sinistra:
```c
int safe = divisor != 0 && value / divisor > 2;
```
Quando `divisor` è `0`, la divisione non viene mai eseguita.

---

La valutazione a corto circuito salta anche le chiamate di funzione: in `0 && check()` la funzione `check` non viene mai chiamata, quindi qualsiasi effetto collaterale che ha (come aggiornare un contatore) non avviene.

---

Gli operatori hanno una **precedenza** che decide cosa viene calcolato per primo:
1. `!` viene applicato per primo
2. poi i confronti relazionali `<`, `>`, `<=`, `>=`
3. poi i confronti di uguaglianza `==`, `!=`
4. poi `&&`
5. poi `||`

Quindi `a > 0 && a < 10` non ha bisogno di parentesi: entrambi i confronti vengono calcolati prima di `&&`.
E `x == 1 || y == 2 && z == 3` significa `x == 1 || (y == 2 && z == 3)`, perché `&&` lega più stretto di `||`.

---

Un `char` è un piccolo intero, quindi i caratteri possono essere confrontati con gli stessi operatori.
Confronta con un literal di carattere tra apici singoli:
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // stampa "1"
```
Le virgolette doppie creerebbero una stringa, che non può essere confrontata in questo modo.

---

Poiché i caratteri sono numeri, `<` e `>` confrontano i loro codici, e caratteri consecutivi come `'a'`, `'b'`, `'c'` o `'0'`, `'1'`, `'2'` hanno codici consecutivi.
Un controllo di intervallo sui caratteri funziona quindi esattamente come sui numeri:
```c
int is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Un errore classico in C è scrivere `=` al posto di `==`. Il codice compila comunque, perché un'assegnazione è un'espressione il cui valore è il valore assegnato:
```c
int x = 5;
if (x = 0) { ... } // assegna 0 a x, la condizione è 0 (falso)
if (x = 3) { ... } // assegna 3 a x, la condizione è 3 (vero)
```
La maggior parte dei compilatori avverte di questo, quindi leggi gli avvisi quando una condizione si comporta in modo strano.

---

La condizione di un `if` è semplicemente un'espressione trattata come vera quando è diversa da zero, quindi i confronti e gli operatori logici si inseriscono naturalmente:
```c
if (n < 0) {
    printf("negative\n");
} else if (n == 0) {
    printf("zero\n");
}
```
Puoi anche memorizzare prima il risultato e testare la variabile: `int ok = n > 0; if (ok) { ... }`.

---

Un ciclo `while` continua a eseguire finché la sua condizione è diversa da zero, quindi un confronto decide quando si ferma:
```c
int i = 0;
while (i < 3) {
    printf("%d\n", i);
    i++;
}
// stampa 0, 1, 2
```
Scegliere tra `<` e `<=` cambia se l'ultimo valore viene incluso.

---

A partire da C99, l'header `stdbool.h` fornisce il tipo `bool` e le costanti `true` (`1`) e `false` (`0`):
```c
#include <stdbool.h>

bool ready = true;
bool done = count == 10;
```
Un `bool` è comunque un intero sotto il cofano: stamparlo con `%d` mostra `1` o `0`, e funziona con `&&`, `||` e `!` come qualsiasi risultato di confronto.
Usare `bool` rende l'intento di una funzione più chiaro rispetto a restituire un semplice `int`.

---

Un parametro `bool` può essere usato direttamente come operando di `&&` o `||`, senza confrontarlo con `true`: scrivi `age >= 18 && citizen`, non `citizen == true`.

---

Quando una condizione mescola `&&` e `||`, aggiungi le parentesi attorno a ogni gruppo anche quando la precedenza farebbe già la cosa giusta: rende la regola leggibile a colpo d'occhio.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
