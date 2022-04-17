Il processo decisionale e' necessario quando vogliamo eseguire il codice solo se una certa condizione viene soddisfatta.
Supponiamo di voler giocare all'aperto solo se il tempo e' bello.
In programmazione, possiamo salvare una variabile booleana `belTempo` ed eseguire l'azione di giocare fuori **solo** se (`if`) questa variabile e' `true`, come:
```kotlin
var belTempo = true
if (belTempo) {
    // gioca fuori
}
```

---

Continuiamo con l'esempio precedente.
```kotlin
var belTempo = true
if (belTempo) {
    // gioca fuori
}
```
Abbiamo visto che l'istruzione `if` esegue il blocco di codice solo se la condizione e' `true`.
Un'altra cosa importante da considerare e' rappresentata dalle **parentesi graffe** `{}` che indicano un blocco di codice.

---

Abbiamo appena visto come eseguire un blocco di codice se si verifica una condizione, ora vediamo come eseguire un altro blocco di codice se la prima condizione fallisce.
Andiamo a giocare fuori se il tempo e' bello, altrimenti restiamo a casa.
In Kotlin possiamo usare l'istruzione `else`, come:
```kotlin
var belTempo = true
if (belTempo) {
    // gioca fuori
} else {
    // resta a casa
}
```

---

Supponiamo di avere un'altra condizione da verificare, come in questo esempio:
```kotlin
var num = 3
if (num == 2) {
    println("il numero è 2")
} else if (num == 3) {
    println("il numero è 3")
} else {
    println("fai qualcos'altro")
}
```
e l'output di questo codice e' `il numero e' 3`.
Prima di tutto, verifichiamo se il numero e' uguale a 2, questo e' falso.
Passiamo quindi alla seconda istruzione e verifichiamo se `num` e' uguale a 3, essendo vero eseguiamo il seguente blocco di codice stampando `il numero e' 3`.

---

Possiamo aggiungere tutte le istruzioni `else if` che vogliamo, non ci sono limiti
```kotlin
var num = 4
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else if (num == 4) {
    println("the number is 4")
} else if (num == 5) {
    println("the number is 5")
} else if (num == 6) {
    println("the number is 6")
}
```
e l'output del codice e' `il numero e' 4`

---

Possiamo anche nidificare un'istruzione condizionale (`if`, `else if` o `else`) all'interno di un'altra istruzione condizionale, per creare una struttura piu' complessa.
```kotlin
var num = 4
if (num < 3) {
    println("il numero è minore di 3")
} else {
    if (num == 3) {
        println("il numero è 3")
    } else if (num == 4) {
        println("il numero è 4")
    } else {
        println("il numero è maggiore di 4")
    }
}
```
e l'output del codice e' `il numero e' 4`.

---

L'_operatore elvis_ `a ?: b` utilizza `a` se esso contiene un valore, altrimenti restituisce un valore di default `b` se `a` e' uguale a `null`.
L'espressione `a` deve essere sempre di tipo opzionale.
L'espressione `b` deve avere lo stesso tipo salvato all'interno di `a`
L'operatore elvis è una scorciatoia per il codice seguente:
```kotlin
if (a != null) a else b
```
