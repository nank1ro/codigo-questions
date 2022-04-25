> I computer sono ideali per compiti ripetitivi.

La forma più elementare di ripetizione usa la parola chiave `while`.
Questa ripete un blocco finché l'_espressione booleana_ di controllo è vera:

```kotlin
while (espressione-booleana) {
  // Codice da ripetere
}
```
L'espressione booleana viene valutata una volta all'inizio del ciclo e
di nuovo prima di ogni ulteriore iterazione attraverso il blocco.

```kotlin
var x = 3
while (x > 0) {
    println(x)
    x--
}
```
Qui abbiamo creato una variabile `x`, assegnandole il valore iniziale __3__.

Poi abbiamo usato l'istruzione `while` che eseguirà il blocco di codice finché la condizione `x > 0` è `true`.

All'interno del blocco di codice, **NON** dobbiamo dimenticare di aggiungere la linea `x--`.
Essa decrementa il valore di `x`, altrimenti il nostro ciclo sarà infinito.

---

Analizziamo questo frammento di codice.
```kotlin
var contatore = 0 // [1]
while (contatore < 100) { // [2]
    contatore += 10 // [3]
    println(contatore)
}
```
- __[1]__: Inizializziamo la variabile `contatore` a __0__.
- __[2]__: L'espressione condizione per il _while_ loop dice: "ripeti le dichiarazioni nel corpo finché il contatore è inferiore a _100_"
- __[3]__: L'operatore `+=` aggiunge _10_ al `contatore` e assegna il resultato al `contatore` in una singola operazione.

L'output del codice di sopra sono i numeri che vanno da _10_ a _100_ inclusi

---

C'è un secondo modo di usare _while_, in congiunzione con la parola chiave `do`.
```kotlin
do {
  // Codice da ripetere
} while (expressione-booleana)
```
Come puoi vedere il `do-while` è abbastanza simile al ciclo `while`, tranne che per una differenza importante:
> Il corpo del ciclo viene eseguito una volta prima che la condizione venga valutata.

In altre parole, il corpo del `do-while` viene sempre eseguito almeno una volta, anche se l'espressione della condizione inizialmente produce `false`.

Al contrario, il corpo di un ciclo `while` non verrà mai eseguito se la condizione produce `false` la prima volta.

---

Il ciclo _while_ supporta le tre espressioni di salto strutturale:
- `break` termina il ciclo più vicino.
- `continue` procede al passo successivo del ciclo più vicino.
- `return` di default ritorna alla funzione più vicina o ad una funzione anonima (_la vedremo più avanti quando parleremo delle funzioni_).

Ecco un esempio dell'uso di `continue` all'interno di un ciclo _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) continue // [1]
  println(i)
}
// stampa 1, 3
```

Come puoi vedere in __[1]__ quando `i` è uguale a _2_, saltiamo e _continuiamo_ al passo successivo. Infatti il numero 2 non viene mai stampato.

---

Ecco un esempio dell'uso di `break` all'interno di un ciclo _while_:
```kotlin
var i = 0
while (i < 3) {
  i++
  if (i == 2) break // [1]
  println(i)
}
// stampa 1
```

Come puoi vedere a __[1]__ quando `i` è uguale a _2_, si _interrompe_ il ciclo. Infatti i numeri 2 e 3 non vengono mai stampati.
