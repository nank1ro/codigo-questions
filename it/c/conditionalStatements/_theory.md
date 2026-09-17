Il processo decisionale e' necessario quando vogliamo eseguire il codice solo se una certa condizione viene soddisfatta.
Supponiamo di voler giocare all'aperto solo se il tempo e' bello.
In programmazione, possiamo salvare una variabile booleana `bel_tempo` ed eseguire l'azione di giocare fuori **solo** se (`if`) questa variabile e' `True`, come:
```c
bool bel_tempo = true;
if (bel_tempo) {
    // giocare fuori
}
```

---

Continuiamo con l'esempio precedente.
```c
bool bel_tempo = true;
if (bel_tempo) {
    // giocare fuori
}
```
Abbiamo visto che l'istruzione `if` esegue il blocco di codice solo se la condizione e' `true`.
Un'altra cosa importante da considerare e' rappresentata dalle **parantesi graffe** che indica l'inizio di un blocco di codice.

---

Abbiamo appena visto come eseguire un blocco di codice se si verifica una condizione, ora vediamo come eseguire un altro blocco di codice se la prima condizione fallisce.
Andiamo a giocare fuori se il tempo e' bello, altrimenti restiamo a casa.
In C possiamo usare l'istruzione `else`, come:
```c
bool bel_tempo = false;
if (bel_tempo) {
    // giocare fuori
} else {
    // restare a casa
}
```

---

Supponiamo di avere un'altra condizione da verificare, come in questo esempio:
```c
int num = 3;
if (num == 2) {
    printf("il numero è 2\n");
} else if (num == 3) {
    printf("il numero è 3\n");
} else {
    printf("fai qualcos'altro\n");
}
```
e l'output di questo codice è `il numero è 3`.
Prima di tutto, verifichiamo se il numero è uguale a 2, questo è falso.
Passiamo quindi alla seconda istruzione e verifichiamo se `num` è uguale a 3, essendo vero eseguiamo il seguente blocco di codice stampando `il numero è 3`.

---

Possiamo aggiungere tutte le istruzioni `else if` che vogliamo, non ci sono limiti
```c
int num = 4;
if (num == 2) {
    printf("il numero è 2");
} else if (num == 3) {
    printf("il numero è 3");
} else if (num == 4) {
    printf("il numero è 4");
} else if (num == 5) {
    printf("il numero è 5");
} else if (num == 6) {
    printf("il numero è 6");
}
```
e l'output del codice è `il numero è 4`.

---

Possiamo anche nidificare un'istruzione condizionale (`if`, `else if` o `else`) all'interno di un'altra istruzione condizionale, per creare una struttura piu' complessa.
```c
int num = 4;
if (num < 3) {
    printf("il numero è minore di 3\n");
} else {
    if (num == 3) {
        printf("il numero è 3\n");
    } else if (num == 4) {
        printf("il numero è 4\n");
    } else {
        printf("il numero è maggiore di 4\n");
    }
}
```
e l'output del codice è `il numero è 4`.

---

È il momento di mettere in pratica la sintassi dell'istruzione `if`: la parola chiave, una condizione tra parentesi e un blocco di codice racchiuso tra parentesi graffe.
```c
if (condition) {
    // viene eseguito se la condizione è vera
}
```

---

I letterali booleani di C sono `true` e `false`: minuscoli, senza virgolette, e definiti da `<stdbool.h>` invece di essere integrati nel linguaggio. Scrivere `True` non compila come condizione — funziona solo la forma minuscola, e quando vale `true` il blocco viene eseguito.

---

C non ha un test booleano separato: una condizione è vera ogni volta che il suo valore è diverso da zero. `false` definito da `<stdbool.h>` è semplicemente `0`, quindi un blocco protetto da esso non viene mai eseguito.

---

Un'istruzione `if` in C è composta da tre parti: la parola chiave `if`, una condizione tra parentesi e un blocco tra parentesi graffe. Le parentesi sono obbligatorie — sono il modo in cui il compilatore capisce dove finisce la condizione.

---

Ogni istruzione condizionale inizia con una parola chiave che dice al compilatore che occorre verificare una condizione prima di decidere cosa eseguire successivamente.

---

Una condizione letterale `true` è sempre vera, quindi il blocco viene eseguito e il suo `printf` viene eseguito esattamente come scritto.

---

Una condizione letterale `false` non è mai vera, quindi il blocco viene saltato completamente e nulla al suo interno viene eseguito.

---

Le condizioni sono i valori che un'istruzione `if` controlla: quando una condizione è `true` il blocco viene eseguito, quando è `false` viene saltato.

---

La parentesi graffa di apertura può stare sulla stessa riga della condizione oppure sulla riga successiva. C ignora l'a capo, quindi entrambi gli stili compilano esattamente nello stesso programma.

---

Le parentesi attorno a una condizione fanno parte della sintassi dell'`if` in C, non sono un raggruppamento opzionale: `if true { ... }` non compila.

---

Una `"false"` tra virgolette è una stringa, non un booleano — e una stringa in una condizione è un indirizzo non nullo, che conta come vero. Solo il `false` senza virgolette impedisce l'esecuzione del blocco.

---

Gli spazi tra le parti di una riga `if` sono liberi in C: `if(true){` e `if (true) {` sono la stessa istruzione per il compilatore, quindi conta solo l'ordine delle parti.

---

Un blocco di codice non è limitato a una sola istruzione. Ogni istruzione tra le parentesi graffe viene eseguita, una dopo l'altra, nell'ordine in cui è scritta.

---

Una variabile booleana può essere usata direttamente come condizione, senza bisogno di confronti. Poiché `online` contiene già `true`, scrivere semplicemente `if (online)` è sufficiente per eseguire il blocco.

---

Una variabile `bool` funziona come condizione perché `if` guarda solo il valore che contiene in quel momento. Con `false` in `online`, `if (online)` si comporta esattamente come `if (false)`.

---

Solo il codice tra le parentesi graffe di un'istruzione `if` è condizionale. Tutto ciò che è scritto dopo la parentesi graffa di chiusura viene eseguito incondizionatamente, indipendentemente dalla condizione.

---

Non c'è un limite fisso al numero di istruzioni che un blocco di codice può contenere — una riga o cento, vengono eseguite tutte insieme quando la condizione è `true`.

---

Leggere una variabile booleana come condizione funziona proprio come un letterale: poiché `online` contiene `true`, il blocco viene eseguito e il suo `printf` viene eseguito.

---

Quando invece `online` contiene `false`, la condizione è falsa, quindi il blocco viene saltato completamente e non viene stampato nulla all'interno di quelle parentesi graffe.
