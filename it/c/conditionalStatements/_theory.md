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
