Le liste sono un tipo di dati che si può utilizzare per memorizzare una collezione di informazioni diverse come una sequenza sotto un'unica variabile.
Una lista memorizza valori multipli di qualsiasi tipo e utilizza gli **indici** per distinguere questi valori.
E' possibile assegnare gli elementi ad una lista con un'espressione della forma:
```kotlin
val nomeLista = listOf<tipoElementi>(elemento1, elemento2)
```
`tipoElementi` sta ad indicare il tipo degli elementi all'interno della lista, per esempio, può essere  `Int`, `String`, `Any`...

---

Una lista è una collezione di elementi con uno specifico ordine.
Ci sono due tipi di liste in Kotlin:

- Una `List` non può essere modificata dopo essere stata creata.
- Una `Mutable list` (lista mutabile) può essere modificata dopo essere stata creata, quindi possiamo aggiungere, rimuovere o aggiornare i suoi elementi.

```kotlin
val numeri = listOf(1, 3, 5)
numeri.add(7) // [1]
```
__[1]__ genera un Errore in quanto il tipo `List` è in _sola-lettura_.

Per creare una lista modificabile dobbiamo usare la parola chiave `mutableListOf`
```kotlin
val numeri = mutableListOf(1, 3, 5)
numeri.add(7)
println(numeri)
// stampa [1, 3, 5, 7]
```

---

È possibile accedere ad un singolo valore della lista tramite il suo indice.
Un indice è come un indirizzo che identifica il posto dell'elemento nella lista.
L'indice si inserisce direttamente dopo il nome della lista, tra le parentesi, in questo modo:
```kotlin
nomeLista[index]
```
Gli indici delle liste iniziano con `0`, **non** `1`! Per ottenere il primo valore della lista usiamo: `nomeLista[0]` oppure `nomeLista.get(0)` o ancora `nomeLista.first()`.
Il secondo elemento della lista si trova all'indice __1__: `nomeLista[1]`.

---

L'indice è in realtà un offset dal primo elemento. Per esempio, quando si scrive `list[2]` non si chiede il secondo elemento della lista, ma l'elemento che si trova a 2 posizioni di distanza dal primo elemento. Quindi `list[0]` è il primo elemento (offset zero), `list[1]` è il secondo elemento (offset 1), `list[2]` è il terzo elemento (offset 2) e così via.

L'indice di una lista può essere usato sia per accedere che per assegnare valori.
Abbiamo già visto come accedere a un indice di lista in questo modo:
```kotlin
val nomi = mutableListOf("Maria", "Michele", "Ivan", "Noemi"]
// stampa il valore "Maria"
println(nomi[0])
```
Ecco invece come funziona un'assegnazione:
```kotlin
val nomi = mutableListOf("Maria", "Michele", "Ivan", "Noemi")
// Assegna il nuovo valore "Jordan"
nomi[0] = "Jordan"
// Stmpa il valore "Jordan"
println(nomi[0])
```

---

Proprio come le stringhe, le liste hanno una __lunghezza__ ottenuta con il getter `size`.
La lunghezza di una lista e' il numero di elementi che contiene

---

Un'altra utile operazione utile delle liste è il metodo `contains` che permette di sapere se un elemento è presente nella lista.
Per esempio, se hai una lista di nomi, puoi usare il metodo `contains` per capire se il nome è presente nella lista
```kotlin
val nomi = listOf("Tommaso", "Donald", "Scarlett")
println(nomi.contains("Scarlett"))
// stampa true
```

---

Una lista mutabile non ha una lunghezza fissa.
Puoi aggiungere elementi al fondo della lista ogni volta che vuoi!
Per aggiungere un elemento ad una lista mutabile usiamo la funzione `add` o il shortcut `+=`:
```kotlin
val lettere = mutableListOf("a", "b")
lettere.add("c")
println(lettere)
// stampa [a, b, c]
```

---

Come abbiamo visto nel precedente esempio, possiamo aggiungere gli elementi uno ad uno usando la funzione `add`.
Ma se volessimo aggiungere tutti gli elementi di un'altra lista possiamo semplicemente usare la funzione `addAll`, oppure il shortcut `+=`:
```kotlin
val lettere = mutableListOf("a", "b")
val nuoveLettere = listOf("c", "d", "e") 
lettere.addAll(nuoveLettere)
println(lettere)
// stampa [a, b, c, d, e]
```

---

A volte si vuole accedere solo a una parte di una lista.
Considera il seguente codice:
```kotlin
val numeri = listOf(1, 2, 3, 4) // [1]
val fetta = numeri.slice(1..2) // [2]
println(fetta)
// stampa [2, 3]
```

__[1]__: per prima cosa abbiamo creato una lista in _sola-lettura_ chiamata `numeri`.
__[2]__: successivamente, abbiamo preso un sottoinsieme usando la funzione `slice` ed abbiamo salvato il valore nella variabile `fetta`.
In Kotlin possiamo includere l'indice finale usando `..`, mentre possiamo escluderlo usando `until`.

---

Gli elementi della lista possono essere di qualsiasi tipo, se specifichiamo il tipo `Any`:
```kotlin
var nomeLista: List<Any> = listOf("uno", 2, true)
```

Difatti, qui sopra abbiamo, in ordine, una `String`, un `Integer` ed un `Boolean`.
Potremmo anche avere liste di liste.

---

A volte è necessario cercare un elemento in una lista.
In Kotlin possiamo usare il metodo `indexOfFirst`:
```kotlin
val nomi = mutableListOf("Trevor", "Zac", "Glenn")
println(nomi.indexOfFirst { it == "Zac"})
// stampa 1
```

Il metodo `indexOfFirst` prende una funzione __predicato__ che verrà valutata per ogni elemento della lista finchè non è `true`, restituendo l'_indice_ dell'elemento.
Il codice di sopra stampa il primo indice della lista che corrisponde alla stringa `Zac`, in questo caso `1`.

Possiamo anche inserire elementi all'interno di una lista modificabile ad un indice specifico, utilizzando il metodo `add(index, element)`:

```kotlin
nomi.add(1, "Ali")
// stampa [Trevor, Ali, Zac, Glenn]
```
Questo codice inserisce `"Ali"` all'indice `1`, muovendo tutto ciò che è successivo a questo indice in giù di 1.

---

In Kotlin possiamo far scorrere una lista in un ciclo in un modo molto semplice usando le parole chiave `for..in`:
```kotlin
val numeri = listOf(1, 2, 3)
for (num in numeri) {
    println(num)
}
// stampa 1, 2, 3 
```
Un nome di variabile segue la parola chiave `for`, ad essa verrà assegnato il valore di ogni elemento della lista a turno.
