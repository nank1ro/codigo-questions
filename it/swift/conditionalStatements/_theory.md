Il processo decisionale e' necessario quando vogliamo eseguire il codice solo se una certa condizione viene soddisfatta.
Supponiamo di voler giocare all'aperto solo se il tempo e' bello.
In programmazione, possiamo salvare una variabile booleana `belTempo` ed eseguire l'azione di giocare fuori **solo** se (`if`) questa variabile e' `true`, come:
```swift
var belTempo = true
if belTempo {
    // gioca fuori
}
```

---

Continuiamo con l'esempio precedente.
```swift
var belTempo = true
if belTempo {
    // gioca fuori
}
```
Abbiamo visto che l'istruzione `if` esegue il blocco di codice solo se la condizione e' `true`.
Un'altra cosa importante da considerare e' rappresentata dalle **parentesi graffe** `{}` che indicano un blocco di codice.

---

Abbiamo appena visto come eseguire un blocco di codice se si verifica una condizione, ora vediamo come eseguire un altro blocco di codice se la prima condizione fallisce.
Andiamo a giocare fuori se il tempo e' bello, altrimenti restiamo a casa.
In Swift possiamo usare l'istruzione `else`, come:
```swift
var belTempo = true
if belTempo {
    // gioca fuori
} else {
    // resta a casa
}
```

---

Supponiamo di avere un'altra condizione da verificare, come in questo esempio:
```swift
var num = 3
if num == 2 {
    print("il numero e' 2")
} else if num == 3 {
    print("il numero e' 3")
} else {
    print("fai qualcos'altro")
}
```
e l'output di questo codice e' `il numero e' 3`.
Prima di tutto, verifichiamo se il numero e' uguale a 2, questo e' falso.
Passiamo quindi alla seconda istruzione e verifichiamo se `num` e' uguale a 3, essendo vero eseguiamo il seguente blocco di codice stampando `il numero e' 3`.

---

Possiamo aggiungere tutte le istruzioni `elif` che vogliamo, non ci sono limiti
```swift
var num = 4
if (num == 2) {
    print("il numero e' 2")
} else if num == 3 {
    print("il numero e' 3")
} else if (num == 4) {
    print("il numero e' 4")
} else if (num == 5) {
    print("il numero e' 5")
} else if (num == 6) {
    print("il numero e' 6")
}
```
e l'output del codice e' `il numero e' 4`

---

Possiamo anche nidificare un'istruzione condizionale (`if`, `elif` o `else`) all'interno di un'altra istruzione condizionale, per creare una struttura piu' complessa.
```swift
var num = 4
if num < 3 {
    print("il numero e' minore di 3")
} else {
    if num == 3 {
        print("il numero e' 3")
    } else if num == 4 {
        print("il numero e' 4")
    } else {
        print("il numero e' maggiore di 4")
    }
}
```
e l'output del codice e' `il numero e' 4`.

---

L'operatore ternario è un operatore condizionale speciale costituito da tre parti, e prende la forma di `domanda ? risposta1 : risposta2`.
È una scorciatoia che permette di valutare una delle due espressioni in base al fatto che la `domanda` sia vera o falsa.
Se `domanda` è vera, valuta `risposta1` e ne restituisce il suo valore; altrimenti, valuta `risposta2` e ne restituisce il suo valore.
```swift
let a = 10, b = 20, c: Int
if (a < b) {
    c = a
} else {
    c = b
}
print(c)
```
La versione abbreviata del codice di sopra è:
```swift
let a = 10, b = 20, c: Int
c = a < b ? a : b
print(c)
```
`c` viene impostato uguale ad `a`, perchè la condizione `a < b` è vera

---

L'operatore _nil-coalescing_ `a ?? b` utilizza `a` se esso contiene un valore, altrimenti restituisce un valore di default `b` se `a` e' uguale a `nil`.
L'espressione `a` deve essere sempre di tipo opzionale.
L'espressione `b' deve avere lo stesso tipo salvato all'interno di `a`
L'operatore nil-coalescing e' una scorciatoia per il codice seguente:
```swift
a != nil ? a! : b
```
