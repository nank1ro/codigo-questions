I `Set` sono un tipo di dato che si può utilizzare per memorizzare una collezione di informazioni diverse come una sequenza sotto un'unica variabile.
La differenza principale con le `List`e è che un `Set` consente solo elementi unici.
È possibile assegnare gli elementi ad un set con un'espressione della forma:
```kotlin
val nomeSet = setOf<tipoElementi>(elemento1, elemento2)
```
`tipoElementi` sta ad indicare il tipo degli elementi all'interno della lista, per esempio, può essere  `Int`, `String`, `Any`...

---

Un `Set` è una collezione di elementi __unici__

```kotlin
val numeri = setOf(1, 1, 2) // [1]
println(numeri)
// stampa [1, 2]
```

Al punto __[1]__ stiamo provando a creare un set con il numero __1__ presente due volte ma come puoi vedere ogni elemento deve essere unico quindi il secondo __1__ viene scartato automanticamente.

---

Ci sono due tipo di `Set` in Kotlin:

- Un `Set` non può essere modificato dopo essere stato creato
- Un `MutableSet` (set mutabile) può essere modificato dopo essere stato creato, quindi possiamo aggiungere, rimuovere o aggiornare i suoi elementi.

```kotlin
val numeri = setOf(1, 2, 3)
numeri.add(4) // [1]
```
__[1]__ genera un Errore in quanto il tipo `Set` è in _sola-lettura_.

Per creare un set modificabile dobbiamo usare la parola chiave `mutableSetOf`

```kotlin
val numeri = mutableSetOf(1, 2, 3)
numeri.add(4)
println(numeri)
// stampa [1, 2, 3, 4]
```

---

L'attività più comune che possiamo fare con i `Set` è testare l'appartenza di un elemento usando `in` oppure `contains()`

```kotlin
val numeri = setOf(1, 2, 3)
println(2 in numeri) // stampa true
println(numeri.contains(5)) // stampa false
```

Come puoi vedere sopra `in` e `contains` restituiscono un `Bool`eano che indica se l'elemento che gli passi è presente nel set

---

L'ordine degli elementi in un `Set` non è importante.
Difatti se provi a compare due `Set` con gli stessi elementi ma in ordine diverso otterrai che sono uguali

---

Con i `Set` puoi eseguire diverse operazioni come l'unione, l'intersezione, la differenza ed il sottoinsieme.

```kotlin
val numeri1 = setOf(1, 2, 3)
val numeri2 = setOf(3, 4, 5)
val unione = numeri1.union(numeri2) // [1, 2, 3, 4, 5]
val intersezione = numeri1 intersect numeri2 // [3]
val differenza = numeri1 subtract numeri2 // [1, 2]
val sottoinsieme = numeri1.containsAll(numeri2) // false
```

---

Per convertire un `Set` in una `List`a possiamo usare la funzione `toList()`
