Il processo decisionale e' necessario quando vogliamo eseguire il codice solo se una certa condizione viene soddisfatta.
Supponiamo di voler giocare all'aperto solo se il tempo e' bello.
In programmazione, possiamo salvare una variabile booleana `belTempo` ed eseguire l'azione di giocare fuori **solo** se (`if`) questa variabile e' `true`, come:
```javascript
var belTempo = true;
if (belTempo) {
    // gioca fuori
}
```

---

Continuiamo con l'esempio precedente.
```javascript
var belTempo = true;
if (belTempo) {
    // gioca fuori
}
```
Abbiamo visto che l'istruzione `if` esegue il blocco di codice solo se la condizione e' `true`.
Un'altra cosa importante da considerare e' rappresentata dalle **parentesi graffe** `{}` che indicano un blocco di codice.

---

Abbiamo appena visto come eseguire un blocco di codice se si verifica una condizione, ora vediamo come eseguire un altro blocco di codice se la prima condizione fallisce.
Andiamo a giocare fuori se il tempo e' bello, altrimenti restiamo a casa.
In JavaScript possiamo usare l'istruzione `else`, come:
```javascript
var belTempo = true;
if (belTempo) {
    // gioca fuori
} else {
    // resta a casa
}
```

---

Supponiamo di avere un'altra condizione da verificare, come in questo esempio:
```javascript
var num = 3;
if (num == 2) {
    console.log("il numero è 2");
} else if (num == 3) {
    console.log("il numero è 3");
} else {
    console.log("fai qualcos'altro");
}
```
e l'output di questo codice e' `il numero e' 3`.
Prima di tutto, verifichiamo se il numero e' uguale a 2, questo e' falso.
Passiamo quindi alla seconda istruzione e verifichiamo se `num` e' uguale a 3, essendo vero eseguiamo il seguente blocco di codice stampando `il numero e' 3`.

---

Possiamo aggiungere tutte le istruzioni `elif` che vogliamo, non ci sono limiti
```javascript
var num = 4;
if (num == 2) {
    console.log("il numero è 2");
} else if (num == 3) {
    console.log("il numero è 3");
} else if (num == 4) {
    console.log("il numero è 4");
} else if (num == 5) {
    console.log("il numero è 5");
} else if (num == 6) {
    console.log("il numero è 6");
}
```
e l'output del codice e' `il numero e' 4`

---

Possiamo anche nidificare un'istruzione condizionale (`if`, `elif` o `else`) all'interno di un'altra istruzione condizionale, per creare una struttura piu' complessa.
```javascript
var num = 4;
if (num < 3) {
    console.log("il numero è minore di 3");
} else {
    if (num == 3) {
        console.log("il numero è 3");
    } else if (num == 4) {
        console.log("il numero è 4");
    } else {
        console.log("il numero è maggiore di 4");
    }
}
```
e l'output del codice e' `il numero e' 4`.

---

L'operatore ternario è un operatore condizionale speciale costituito da tre parti, e prende la forma di `domanda ? risposta1 : risposta2`.
È una scorciatoia che permette di valutare una delle due espressioni in base al fatto che la `domanda` sia vera o falsa.
Se `domanda` è vera, valuta `risposta1` e ne restituisce il suo valore; altrimenti, valuta `risposta2` e ne restituisce il suo valore.
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// stampa 10
```
The shortand code for the above code is:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// stampa 10
```
`c` viene impostato uguale ad `a`, perchè la condizione `a < b` è vera

---

L'operatore _nil-coalescing_ `a ?? b` utilizza `a` se esso contiene un valore, altrimenti restituisce un valore di default `b` se `a` e' uguale a `nil`.
L'espressione `a` deve essere sempre di tipo opzionale.
L'espressione `b' deve avere lo stesso tipo salvato all'interno di `a`
L'operatore nil-coalescing e' una scorciatoia per il codice seguente:
```javascript
a != nil ? a! : b;
```

---

`if` è la parola chiave che introduce un'istruzione condizionale in JavaScript. Qui non esiste la parola chiave `elif` — una seconda condizione viene introdotta con `else if`, scritto come due parole separate.

---

I letterali booleani di JavaScript sono minuscoli: `true` e `false`, non `True`/`False`, e nemmeno le stringhe `"true"`/`"false"`.

---

Per impedire l'esecuzione di un blocco di codice, la condizione tra parentesi deve valutare a `false`.

---

Lo spazio tra `if` e le sue parentesi è puramente estetico: `if(true)` e `if (true)` sono la stessa istruzione per JavaScript.

---

Le parentesi graffe sono ciò che raggruppa più istruzioni in un unico blocco. Senza di esse un `if` controlla solo la singola istruzione che lo segue, quindi `if (true) console.log("Hello!");` è JavaScript valido.

---

La condizione viene valutata una sola volta, prima che il blocco inizi. JavaScript non la riesamina mentre le istruzioni tra le parentesi graffe sono in esecuzione.

---

Una condizione `false` salta completamente il blocco, e il programma continua dalla prima istruzione dopo la parentesi graffa di chiusura.

---

Una condizione non deve essere per forza un booleano: JavaScript converte qualunque cosa trovi in uno, quindi `if (1)` esegue il suo blocco e `if (0)` no. Un letterale `true` non richiede alcuna conversione.

---

Un blocco di codice non è limitato a una singola riga — ogni istruzione all'interno delle parentesi graffe viene eseguita, in ordine, quando la condizione è `true`.
```javascript
if (true) {
    console.log("First line");
    console.log("Second line");
}
```
e l'output è `First line` seguito da `Second line`.

---

Le istruzioni all'interno di un blocco vengono eseguite una dopo l'altra, dall'alto verso il basso, quindi due chiamate a `console.log` nello stesso blocco stampano su due righe separate.

---

Indentare le istruzioni all'interno di un blocco è solo una convenzione di leggibilità. JavaScript usa le parentesi graffe, mai l'indentazione, per decidere cosa appartiene al blocco.

---

Istruzioni come `if`, `else if` ed `else`, che eseguono o saltano il codice a seconda che una condizione sia `true` o `false`, sono chiamate **istruzioni condizionali**.

---

Una variabile booleana, anche una costruita con una negazione `!` come `isAfternoon`, può essere usata direttamente come condizione di un `if`, senza bisogno di confronti.

---

La condizione di un'istruzione `if` va sempre dentro le parentesi `()`, poste subito dopo la parola chiave `if` e prima della parentesi graffa di apertura.

---

Un blocco può contenere un numero qualsiasi di istruzioni, e può anche non contenerne nessuna: `if (true) {}` è JavaScript valido che semplicemente non fa nulla.

---

Il blocco di codice di un'istruzione `if` è l'insieme delle istruzioni all'interno delle parentesi graffe `{ }`, la parte che viene effettivamente eseguita quando la condizione è `true`.
