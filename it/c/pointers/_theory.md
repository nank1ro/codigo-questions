Ogni variabile vive da qualche parte in memoria, e quel luogo ha un numero chiamato **indirizzo**. L'operatore `&`, che si legge "address of" (indirizzo di), restituisce l'indirizzo di una variabile:
```c
int x = 42;
printf("%p\n", &x); // prints something like 0x7ffd5c3e9a4c
```
Lo specificatore `%p` stampa un indirizzo; il numero esatto cambia da un'esecuzione all'altra, quindi i programmi non vi si affidano mai.
Un indirizzo viene memorizzato in una variabile **puntatore**. Un puntatore si dichiara con il tipo a cui punta seguito da `*`:
```c
int *p = &x; // p is a pointer to int, and it holds the address of x
```
Si dice che `p` **punta a** `x`. Due puntatori sono uguali quando contengono lo stesso indirizzo, quindi `p == &x` è vero.

---

Un puntatore da solo è soltanto un indirizzo. Per leggere il valore memorizzato in quell'indirizzo si **dereferenzia** il puntatore con l'operatore `*`:
```c
int x = 42;
int *p = &x;
printf("%d\n", *p); // prints "42"
```
`*p` significa "il valore a cui `p` punta", ed è un `int` come `x` stessa. Lo stesso simbolo `*` ha due ruoli: in una dichiarazione `int *p` dice "questo è un puntatore", in un'espressione `*p` segue il puntatore fino al valore.

---

Un puntatore dereferenziato può anche essere **assegnato**. Scrivere su `*p` memorizza il nuovo valore nell'indirizzo contenuto in `p`, quindi la variabile a cui punta cambia:
```c
int x = 5;
int *p = &x;
*p = 10;
printf("%d\n", x); // prints "10"
```
`x` e `*p` sono due nomi per la stessa memoria. Assegnare a `p` senza il `*` cambierebbe invece **quale indirizzo** contiene il puntatore, non il valore memorizzato lì.

---

Un puntatore che non punta ancora a nulla deve contenere `NULL`, una costante speciale definita in `stdio.h` e `stddef.h` che significa "nessun indirizzo":
```c
int *p = NULL;
```
Dereferenziare un puntatore `NULL` è un errore a runtime che fa terminare il programma, quindi un puntatore che può essere `NULL` viene controllato prima dell'uso:
```c
if (p != NULL) {
    printf("%d\n", *p);
}
```
Poiché `NULL` è zero, `if (p)` è una scorciatoia comune per `if (p != NULL)`. Un puntatore dichiarato senza inizializzatore contiene spazzatura, non `NULL`, quindi inizializza sempre i puntatori.

---

Un puntatore può puntare a qualsiasi tipo: `double *`, `char *`, `bool *` e così via. Il tipo nella dichiarazione dice al compilatore quanti byte leggere quando il puntatore viene dereferenziato e cosa significano:
```c
double price = 9.5;
double *p = &price;
*p = *p * 2; // price is now 19.0
```
Un puntatore deve corrispondere al tipo della variabile a cui punta; `int *p = &price;` viene rifiutato dal compilatore. `NULL` è l'unico valore compatibile con un puntatore di qualsiasi tipo.

---

Un puntatore a `char` funziona come qualsiasi altro puntatore: contiene l'indirizzo di un singolo carattere, e `*p` legge o scrive quel carattere:
```c
char grade = 'B';
char *p = &grade;
*p = 'A';
printf("%c\n", grade); // prints "A"
```
Leggere attraverso un puntatore e scrivere attraverso di esso possono essere liberamente mescolati: `*p = *p + 1` trasforma `'A'` in `'B'`.

---

Un puntatore memorizza un indirizzo, e ogni indirizzo ha la stessa dimensione su una data macchina, indipendentemente dal tipo di dato memorizzato lì. La `sizeof` di un puntatore è quindi la stessa per `char *`, `int *` e `double *`: `8` byte su un sistema a 64 bit, `4` su uno a 32 bit:
```c
printf("%zu\n", sizeof(int *));  // prints "8" on 64-bit
printf("%zu\n", sizeof(double)); // prints "8"
printf("%zu\n", sizeof(char));   // prints "1"
```
Non confondere la dimensione del puntatore con la dimensione di ciò a cui punta: `sizeof(p)` è la dimensione dell'indirizzo, `sizeof(*p)` è la dimensione del valore.

---

Un nome di array usato in un'espressione fornisce l'indirizzo del suo **primo elemento**, quindi può essere assegnato direttamente a un puntatore:
```c
int numbers[3] = {10, 20, 30};
int *p = numbers; // same as &numbers[0]
```
Aggiungere un intero a un puntatore lo sposta in avanti di quel numero di **elementi**, non di byte: `p + 1` è l'indirizzo di `numbers[1]`, e `*(p + 1)` è `20`. Il compilatore scala il passo in base alla dimensione del tipo.
L'indicizzazione funziona anche sui puntatori: `p[i]` è definito come `*(p + i)`, quindi `p[2]` è `30`. Questo si chiama **aritmetica dei puntatori**.

---

Poiché `p + 1` è l'elemento successivo, `p++` sposta un puntatore all'elemento successivo in posizione. Un ciclo può percorrere un array avanzando un puntatore invece di un indice:
```c
int *p = values;
for (int i = 0; i < 3; i++) {
    printf("%d\n", *p);
    p++;
}
```
A ogni giro stampa l'elemento a cui `p` punta, poi sposta `p` in avanti di un elemento.

---

Quando un array viene passato a una funzione esso **decade** in un puntatore al suo primo elemento. È per questo che i parametri `int values[]` e `int *values` significano esattamente la stessa cosa, e perché la funzione non può conoscere da sola la lunghezza: riceve soltanto un indirizzo.
I puntatori nello stesso array possono essere confrontati e sottratti. `end - start` è il numero di elementi tra essi, e un ciclo può far avanzare un puntatore da un indirizzo a un altro:
```c
for (int *p = start; p < end; p++) {
    printf("%d\n", *p);
}
```
Passare `numbers` e `numbers + 3` descrive i primi tre elementi senza un parametro di dimensione separato.

---

Gli argomenti delle funzioni sono passati **per valore**: la funzione riceve una copia, e assegnare a un parametro non cambia mai la variabile di chi ha chiamato. Per permettere a una funzione di cambiare una variabile, passane l'indirizzo e dereferenzia il puntatore al suo interno:
```c
void reset(int *p) {
    *p = 0;
}

int counter = 7;
reset(&counter); // counter is now 0
```
L'esempio classico è lo scambio di due variabili, che richiede una copia temporanea di un valore mentre l'altro viene sovrascritto.

---

Una funzione può fare `return` di un solo valore. Per restituirne di più, riceve puntatori a variabili appartenenti a chi la chiama e scrive i risultati attraverso di essi. Tali parametri si chiamano **parametri di output**:
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
Chi chiama dichiara le variabili, passa i loro indirizzi e le ritrova riempite dopo la chiamata. Molte funzioni standard usano questo schema, ed è per questo che `scanf("%d", &n)` richiede il `&`.

---

Un puntatore a una struct raggiunge i membri con la freccia `->`, e l'indirizzo di una struct memorizzata in un array si prende con `&items[i]`. Una funzione può anche **restituire** un puntatore, per esempio all'elemento che ha trovato:
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
Chi chiama poi legge i membri attraverso il puntatore restituito con `->`, dopo aver verificato che non sia `NULL`. Restituire un puntatore evita di copiare la struct e permette a chi chiama di modificare l'elemento originale.

---

`const` può proteggere il valore o il puntatore, a seconda di dove viene scritto:
```c
const int *p = &a; // pointer to const: *p cannot be changed, p can point elsewhere
int *const q = &a; // const pointer: q always points to a, but *q can be changed
```
Si legge la dichiarazione da destra a sinistra: `p` è un puntatore a un `int` costante; `q` è un puntatore costante a un `int`. Un puntatore a const è il modo usuale per promettere che una funzione fa solo **lettura** di ciò che riceve, come in `int sum(const int *values, int size)`. Una variabile normale può essere passata; la promessa limita solo ciò che la funzione può fare.

---

Un puntatore è una variabile, quindi ha un indirizzo tutto suo, e quell'indirizzo può essere memorizzato in un **puntatore a puntatore**, dichiarato con due asterischi:
```c
int x = 7;
int *p = &x;
int **pp = &p;
```
`*pp` è `p`, l'indirizzo di `x`, e `**pp` segue entrambi i passi fino a raggiungere `7`. I puntatori a puntatori permettono a una funzione di cambiare quale indirizzo contiene un puntatore: riceve `&p` e assegna a `*pp`.

---

Mettendo tutto insieme: una funzione che percorre un array con un puntatore, conserva un puntatore al miglior elemento visto finora e lo restituisce, oppure `NULL` quando non c'è nulla da restituire:
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
Chi chiama confronta il risultato con `NULL` prima di dereferenziarlo, e può usare `result - values` per recuperare l'indice dell'elemento.
