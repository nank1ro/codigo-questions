Un'**enumerazione** (`enum`) assegna dei nomi a un insieme di costanti intere correlate, così puoi scrivere `RED` invece di un numero nudo.
La dichiari con la parola chiave `enum`, un nome e l'elenco delle costanti tra parentesi graffe:
```c
enum Color { RED, GREEN, BLUE };
```
Ogni costante è un intero: se non specifichi altrimenti, la prima è `0` e ogni successiva è la precedente più uno, quindi `RED` è `0`, `GREEN` è `1` e `BLUE` è `2`.
Poiché sono numeri interi, le stampi con `%d`:
```c
printf("%d\n", GREEN);
// prints "1"
```

---

La numerazione continua automaticamente per tutte le costanti che elenchi: la quarta costante è `3`, la quinta è `4` e così via.
I nomi vengono di solito scritti in maiuscolo, come le altre costanti, e devono essere univoci in tutto il programma: due enumerazioni non possono condividere il nome di una costante.

---

Puoi anche assegnare a una costante un valore esplicito con `=`; le costanti successive continuano a contare a partire da quel valore:
```c
enum Month { JAN = 1, FEB, MAR }; // FEB is 2, MAR is 3
```
I valori espliciti non devono essere consecutivi né crescenti: `enum Status { OK = 200, NOT_FOUND = 404 };` è perfettamente valido.

---

Un'enumerazione è anche un tipo: puoi dichiarare una variabile di quel tipo scrivendo `enum` seguito dal nome dell'enumerazione, e assegnarle una delle sue costanti:
```c
enum Color favorite = GREEN;
```
Poiché le costanti sono numeri interi, confronti le variabili di tipo enumerazione con gli operatori consueti:
```c
if (favorite == GREEN) {
    printf("Green it is\n");
}
```

---

Un'enumerazione può essere il tipo di un parametro di funzione, esattamente come `int`:
```c
int is_weekend(enum Day day) {
    return day == SAT || day == SUN;
}
```
All'interno della funzione, uno `switch` è il modo naturale di gestire ogni costante, perché le costanti di un'enumerazione possono essere usate direttamente come etichette `case`:
```c
switch (day) {
    case SAT: return 1;
    case SUN: return 1;
    default: return 0;
}
```

---

Quando ogni caso di uno `switch` gestisce una costante, ricordati il `break` dopo ciascuno, altrimenti l'esecuzione prosegue nel caso successivo.
Un caso `default` non è necessario se copri tutte le costanti dell'enumerazione.

---

Anche una funzione può restituire un'enumerazione; basta usare il tipo enumerato come tipo di ritorno e restituire una delle sue costanti:
```c
enum Grade grade_for(int score) {
    if (score >= 60) {
        return PASS;
    }
    return FAIL;
}
```
Restituire una costante con nome è molto più chiaro per chi chiama la funzione rispetto a restituire un semplice `0` o `1`.

---

Scrivere `enum Color` ogni volta è prolisso. Con `typedef` dai all'enumerazione un nome di tipo breve, e l'enumerazione stessa può restare anonima:
```c
typedef enum { RED, GREEN, BLUE } Color;

Color favorite = BLUE;
```
Il nuovo nome `Color` viene usato da solo, senza la parola chiave `enum` davanti.

---

Una costante di enumerazione viene convertita automaticamente in `int`, quindi `int n = BLUE;` è valido e memorizza `2`.
Il percorso inverso si fa con un **cast**, scrivendo il tipo enumerato tra parentesi prima dell'intero:
```c
enum Color c = (enum Color)1; // c is GREEN
```
C non verifica che il numero corrisponda a una costante: `(enum Color)7` compila anche se nessuna costante vale `7`, quindi valida gli interi prima di convertirli.

---

Un'operazione aritmetica su un valore di enumerazione produce un semplice `int`: `GREEN + 1` è `2`, non `BLUE`.
Per salvare di nuovo il risultato in una variabile di enumerazione o restituirlo da una funzione, convertilo nel tipo enumerato:
```c
enum Color after_green = (enum Color)(GREEN + 1); // BLUE
```
Combinato con l'operatore resto `%`, questo ti permette di ciclare tra le costanti e tornare alla prima.

---

Un trucco comune è aggiungere una costante extra alla fine dell'enumerazione, di solito chiamata `COUNT`: poiché la numerazione parte da `0`, il suo valore corrisponde esattamente al numero di costanti reali che la precedono.
```c
enum Day { MON, TUE, WED, DAY_COUNT }; // DAY_COUNT is 3
```
Questa sentinella ti permette di scorrere tutte le costanti senza codificare il numero, e resta corretta quando aggiungi costanti prima di essa:
```c
for (int d = MON; d < DAY_COUNT; d++) {
    printf("%d\n", d);
}
```

---

La sentinella `COUNT` è anche la dimensione perfetta per un array con una casella per costante, e le costanti diventano indici leggibili al suo interno:
```c
enum Fruit { APPLE, BANANA, CHERRY, FRUIT_COUNT };

int stock[FRUIT_COUNT] = {10, 4, 7};
printf("%d\n", stock[BANANA]); // prints "4"
```
Un ciclo da `0` a `FRUIT_COUNT` visita ogni casella, e l'indice del ciclo può essere riconvertito in `enum Fruit` quando serve restituirlo.

---

C non offre alcun modo integrato per ottenere il nome di una costante di enumerazione: `printf("%d\n", SUMMER)` stampa `2`, non `Summer`. La soluzione abituale è una piccola funzione con uno `switch` che restituisce la stringa corrispondente a ogni costante.

---

I valori di enumerazione possono essere memorizzati in array come qualsiasi altro intero: `enum Fruit basket[] = {APPLE, APPLE, CHERRY};` contiene tre frutti, e ogni elemento può essere confrontato con una costante.
