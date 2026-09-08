C è un linguaggio a **tipizzazione statica**: ogni variabile viene dichiarata con un tipo che determina cosa può memorizzare e quanta memoria occupa.
I tre tipi che userai più spesso sono:
- `int` per i numeri interi, come `30` o `-4`
- `double` per i numeri con parte decimale, come `1.75`
- `char` per un singolo carattere, scritto tra apici singoli come `'A'`

Ogni tipo ha il proprio **specificatore di formato** di `printf`: `%d` stampa un `int`, `%f` stampa un `double` (con sei decimali di default) e `%c` stampa un `char`:
```c
int age = 30;
double height = 1.75;
char initial = 'A';
printf("%d %f %c\n", age, height, initial);
// stampa "30 1.750000 A"
```
Usare lo specificatore sbagliato per un tipo stampa dati senza senso, quindi falli sempre corrispondere.

---

C ha due tipi in virgola mobile: `float` (precisione singola, circa 7 cifre significative) e `double` (precisione doppia, circa 15 cifre significative).
Un letterale decimale come `1.75` è un `double`; per scrivere un letterale `float` aggiungi il suffisso `f`, come in `1.75f`.
Preferisci `double` a meno che la memoria non sia limitata: è il tipo predefinito ed è più preciso.
```c
double pi = 3.14159;
float ratio = 0.5f;
```
Una funzione che restituisce un risultato decimale dovrebbe dichiarare `double` come tipo di ritorno, e i parametri `double` accettano sia argomenti interi che decimali:
```c
double half(double x) {
    return x / 2;
}
```

---

`%f` stampa sei decimali, che raramente è ciò che vuoi. Metti una precisione tra `%` e `f` per scegliere quanti decimali mostrare: `%.2f` stampa due decimali, `%.1f` ne stampa uno, e il valore viene **arrotondato**, non troncato:
```c
double price = 9.987;
printf("%.2f\n", price); // stampa "9.99"
printf("%.1f\n", price); // stampa "10.0"
```
Un `float` viene stampato con gli stessi specificatori di un `double`: quando viene passato a `printf` viene convertito automaticamente in `double`.

---

Il risultato di `/` dipende dai tipi dei suoi operandi.
Quando **entrambi** gli operandi sono interi, il risultato è un intero e la parte decimale viene scartata: `7 / 2` è `3`, non `3.5`.
Quando **almeno uno** degli operandi è un valore in virgola mobile, la divisione mantiene i decimali: `7 / 2.0` è `3.5`.
```c
printf("%d\n", 7 / 2);     // stampa "3"
printf("%f\n", 7 / 2.0);   // stampa "3.500000"
```
Scrivere il letterale come `2.0` invece di `2` è il modo più semplice per forzare una divisione in virgola mobile.

---

C converte tra tipi numerici in modo **implicito** quando un valore viene assegnato a una variabile di tipo diverso.
- un `int` memorizzato in un `double` viene esteso senza perdita: `double d = 3;` rende `d` uguale a `3.0`
- un `double` memorizzato in un `int` viene **troncato**: `int n = 3.99;` rende `n` uguale a `3` (i compilatori di solito avvisano di questo)

La conversione avviene solo nel momento dell'assegnazione. L'espressione a destra viene calcolata prima, con i propri tipi:
```c
double d = 7 / 2;
```
Qui `7 / 2` è una divisione intera che dà `3`, e solo dopo `3` viene convertito in `3.0`.

---

Quando la conversione implicita non è quello che vuoi, o vuoi renderla visibile, usa un **cast esplicito**: scrivi il tipo di destinazione tra parentesi prima del valore.
```c
double x = 3.99;
int n = (int) x;   // n è 3
```
Convertire un valore in virgola mobile in `int` **tronca verso lo zero**: `(int) 3.99` è `3` e `(int) -2.5` è `-2`, non avviene alcun arrotondamento.
Il cast si applica solo al valore immediatamente successivo, quindi `(int) x * 2` converte prima `x` e poi moltiplica.

---

Un cast è il modo standard per ottenere una divisione in virgola mobile da due variabili `int`: converti **un operando** in `double` prima di dividere.
```c
int total = 7, count = 2;
double avg = (double) total / count; // 3.5
```
Convertire invece l'intero risultato, come in `(double) (total / count)`, è un errore comune: la divisione intera è già avvenuta e i decimali sono andati persi.

---

Un `char` è in realtà un piccolo intero: memorizza il **codice ASCII** del carattere.
`'A'` è `65`, `'a'` è `97` e `'0'` è `48`, e caratteri consecutivi hanno codici consecutivi.
Per questo puoi fare aritmetica sui caratteri:
- `'a' + 1` è `98`, il codice di `'b'`
- `'7' - '0'` è `55 - 48`, cioè il numero `7`

Lo stesso valore può essere stampato come carattere con `%c` o come numero con `%d`:
```c
char c = 'A';
printf("%c %d\n", c, c); // stampa "A 65"
```

---

Le lettere maiuscole e minuscole distano `32` posizioni nella tabella ASCII: `'A'` è `65` e `'a'` è `97`.
Sottraendo `32` da una lettera minuscola si ottiene quindi la sua versione maiuscola, e il risultato può essere memorizzato di nuovo in un `char`:
```c
char upper = 'g' - 32; // 'G'
```

---

`int` non è l'unico tipo intero. I modificatori ne cambiano dimensione e intervallo:
- `short` usa meno memoria e ha un intervallo più piccolo (di solito da -32768 a 32767)
- `long` ha un intervallo più grande (su sistemi a 64 bit circa ±9 trilioni)
- `unsigned` rimuove il segno: `unsigned int` va da `0` a circa 4 miliardi, ma non può mai essere negativo

Un letterale che deve essere `long` prende il suffisso `L`, uno `unsigned` il suffisso `U`, e ogni tipo ha il proprio specificatore:
```c
long population = 8000000000L;
unsigned int count = 40U;
printf("%ld %u\n", population, count); // stampa "8000000000 40"
```
`%ld` stampa un `long`, `%u` un `unsigned int` e `%lu` un `unsigned long`. Un normale `int`, sulla maggior parte dei sistemi, contiene valori fino a circa 2 miliardi, quindi `5000000000` non ci sta.

---

L'operatore `sizeof` indica quanti **byte** occupa un tipo o una variabile. Il suo risultato ha tipo `size_t`, che viene stampato con `%zu`:
```c
printf("%zu\n", sizeof(int));  // stampa "4" sulla maggior parte dei sistemi
```
Lo standard garantisce solo che `sizeof(char)` sia `1` e che `short <= int <= long`, ma su un tipico sistema a 64 bit le dimensioni sono: `char` 1, `short` 2, `int` 4, `long` 8, `float` 4, `double` 8.
`sizeof` viene spesso usato per controllare quanta memoria occupa una variabile senza scrivere il numero direttamente nel codice.

---

Ogni tipo intero ha un intervallo limitato, e l'header `limits.h` dà un nome a questi limiti: `INT_MAX` e `INT_MIN` per `int`, `LONG_MAX` per `long`, `UINT_MAX` per `unsigned int`, e così via.
```c
#include <limits.h>

printf("%d\n", INT_MAX); // stampa "2147483647" sulla maggior parte dei sistemi
```
Superare `INT_MAX` con un tipo con segno è **comportamento indefinito**: il programma può andare in overflow, andare in crash, o fare qualsiasi altra cosa. Controlla prima di calcolare:
```c
if (a <= INT_MAX - b) { /* a + b è sicuro */ }
```
Nota che il controllo sottrae invece di sommare, perché `a + b` stesso potrebbe già andare in overflow.

---

A differenza dei tipi con segno, l'aritmetica **unsigned** è ben definita quando esce dall'intervallo: il valore **si azzera e riparte** come un contachilometri.
Aggiungere `1` a `UINT_MAX` dà `0`, e sottrarre `1` da `0` dà `UINT_MAX` (`4294967295` quando `unsigned int` ha 32 bit):
```c
unsigned int n = UINT_MAX;
n = n + 1;
printf("%u\n", n); // stampa "0"
```
Per questo un ciclo che conta alla rovescia una variabile `unsigned` "finché non è negativa" non si ferma mai: un valore unsigned non è mai inferiore a `0`.

---

Dalla versione C99, l'header `stdbool.h` fornisce il tipo `bool` con le costanti `true` (`1`) e `false` (`0`).
Un `bool` è un tipo intero con solo due valori, quindi convertire qualsiasi numero in `bool` dà `true` per ogni valore diverso da zero e `false` per `0`. Questo è diverso dalla conversione in `int`:
```c
#include <stdbool.h>

bool b = 0.5;  // true, perché 0.5 non è zero
int n = 0.5;   // 0, perché i decimali vengono troncati
```
Confronti come `x != 0` producono già un risultato compatibile con `bool`, e una funzione che restituisce `bool` documenta che risponde a una domanda sì/no.

---

Un'operazione aritmetica viene eseguita nel tipo dei suoi operandi, **non** nel tipo della variabile che riceve il risultato.
Quindi `long big = n * n;` con un `n` di tipo `int` moltiplica due valori `int`, va in overflow se il prodotto è troppo grande, e solo dopo memorizza il risultato (già sbagliato) nel `long`.
Converti un operando **prima** dell'operazione per calcolare nel tipo più ampio:
```c
int n = 100000;
long big = (long) n * n; // 10000000000, calcolato come long
```
La stessa regola spiega perché `(double) total / count` funziona: il cast cambia il tipo dell'operando, e la divisione lo segue.

---

Mettendo insieme tutto: scegli il tipo in base al tipo di valore, fai corrispondere ogni specificatore di `printf` al tipo del suo argomento, e usa un cast quando un calcolo deve avvenire in un tipo diverso da quello dei suoi operandi.
