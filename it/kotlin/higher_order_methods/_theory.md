Un **metodo di ordine superiore** è un metodo che prende una funzione come argomento. Le collezioni di Kotlin ne offrono molti, e la funzione che passi è di solito una **lambda**: una piccola funzione anonima scritta tra parentesi graffe.
`map` è il più comune: chiama la lambda su ogni elemento e restituisce una **nuova lista** con i risultati, lasciando intatta l'originale:
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6]
println(numbers) // [1, 2, 3]
```
Quando la lambda ha un solo parametro non devi dichiararlo: Kotlin lo chiama `it`. La lambda si scrive dopo il nome del metodo, fuori dalle parentesi tonde, che possono essere omesse quando la lambda è l'unico argomento. Questa è la sintassi della **trailing lambda** ed è usata in ogni esercizio di questo argomento.

---

`filter` prende una lambda che restituisce un `Boolean`, chiamata **predicato**, e restituisce una nuova lista con i soli elementi per cui il predicato è `true`:
```kotlin
val numbers = listOf(4, -2, 7, 0)
println(numbers.filter { it > 0 }) // [4, 7]
```
Invece di `it` puoi dare un nome al parametro, seguito da una freccia `->`. Un parametro con un nome rende più leggibili le lambda lunghe, ed è obbligatorio quando una lambda è annidata dentro un'altra, perché l'`it` interno nasconde l'elemento esterno:
```kotlin
val minLength = 4
val words = listOf("fig", "banana", "kiwi")
println(words.filter { word -> word.length >= minLength }) // [banana, kiwi]
```

---

`forEach` esegue la lambda una volta per ogni elemento e non restituisce nulla. È l'alternativa di ordine superiore al ciclo `for`, e si usa per effetti collaterali come stampare:
```kotlin
listOf("a", "b").forEach { println(it) }
```
`forEachIndexed` ti dà anche la posizione di ogni elemento. La sua lambda ha **due** parametri, quindi devono avere un nome: `it` esiste solo per le lambda con esattamente un parametro.
```kotlin
listOf("a", "b").forEachIndexed { index, letter ->
    println("$index: $letter") // 0: a, poi 1: b
}
```

---

`reduce` combina tutti gli elementi in un singolo valore. La sua lambda prende due parametri: l'**accumulatore** (il risultato fino a quel punto) e l'elemento successivo. Parte dal primo elemento come accumulatore ed esegue la lambda per ogni elemento rimanente:
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n }) // 10
```
`reduce` lancia un'eccezione su una lista vuota, perché non c'è un primo elemento da cui partire. `fold` risolve il problema: passi il **valore iniziale** dell'accumulatore come argomento, e la lambda viene eseguita per ogni elemento, incluso il primo:
```kotlin
println(numbers.fold(0) { acc, n -> acc + n })   // 10
println(listOf<Int>().fold(0) { acc, n -> acc + n }) // 0
```
Con `fold` l'accumulatore può anche avere un tipo diverso dagli elementi, come costruire una `String` a partire da una lista di numeri.

---

Alcuni metodi di ordine superiore rispondono a una domanda sulla collezione invece di costruirne una nuova. Prendono tutti un predicato:
- `any` restituisce `true` se **almeno un** elemento lo soddisfa
- `all` restituisce `true` se **ogni** elemento lo soddisfa
- `none` restituisce `true` se **nessun** elemento lo soddisfa
- `count` restituisce **quanti** elementi lo soddisfano
```kotlin
val numbers = listOf(1, 2, 3)
println(numbers.any { it > 2 })   // true
println(numbers.all { it > 2 })   // false
println(numbers.none { it > 2 })  // false
println(numbers.count { it > 1 }) // 2
```
Su una lista vuota `any` restituisce `false`, mentre `all` e `none` restituiscono `true`: non c'è nessun elemento che infrange la regola.

---

I metodi di aggregazione trasformano un'intera collezione in un solo valore:
- `sum()` somma una lista di numeri, mentre `sumOf` somma il valore che la lambda calcola per ogni elemento
- `maxByOrNull` e `minByOrNull` restituiscono l'**elemento** per cui la lambda dà il valore più grande o più piccolo, oppure `null` su una lista vuota
```kotlin
val words = listOf("fig", "banana", "kiwi")
println(words.sumOf { it.length })      // 13
println(words.minByOrNull { it.length }) // fig
println(listOf(1, 2, 3).sum())           // 6
```
Nota la differenza con `maxOf { it.length }`, che restituisce il **valore** più grande (`6`) invece dell'elemento che lo ha prodotto.

---

`sortedBy` restituisce una nuova lista ordinata in base al valore che la lambda calcola per ogni elemento, dal più piccolo in su. `sortedByDescending` ordina dal più grande in giù. Quando sono gli elementi stessi a dover essere confrontati, `sorted()` e `sortedDescending()` non hanno bisogno di una lambda:
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })            // [fig, kiwi, banana]
println(words.sortedByDescending { it.length })  // [banana, kiwi, fig]
println(words.sorted())                          // [banana, fig, kiwi]
```
L'ordinamento è **stabile**: gli elementi con la stessa chiave mantengono il loro ordine relativo originale. La lista originale non viene mai modificata.

---

`take(n)` restituisce una nuova lista con i primi `n` elementi, e `drop(n)` restituisce una nuova lista **senza** i primi `n` elementi. Nessuno dei due prende una lambda, ma vengono spesso concatenati dopo un metodo che la prende:
```kotlin
val numbers = listOf(5, 3, 8, 1)
println(numbers.take(2))                    // [5, 3]
println(numbers.drop(2))                    // [8, 1]
println(numbers.sortedDescending().take(2)) // [8, 5]
```
`takeWhile` e `dropWhile` sono le versioni con un predicato: prendono o scartano gli elementi dall'inizio **finché** il predicato è `true`, e si fermano al primo elemento che non lo soddisfa:
```kotlin
println(numbers.takeWhile { it > 2 }) // [5, 3, 8]
```

---

`groupBy` divide una collezione in una `Map`: la lambda calcola la **chiave** di ogni elemento, e ogni chiave è associata alla lista degli elementi che l'hanno prodotta, nel loro ordine originale:
```kotlin
val words = listOf("fig", "kiwi", "pear")
val byLength = words.groupBy { it.length }
println(byLength)    // {3=[fig], 4=[kiwi, pear]}
println(byLength[4]) // [kiwi, pear]
```
Il risultato ha tipo `Map<K, List<T>>`, dove `K` è il tipo restituito dalla lambda e `T` è il tipo degli elementi. Le chiavi compaiono nell'ordine in cui vengono incontrate per la prima volta.

---

Quando la lambda restituisce una **lista** per ogni elemento, `map` produce una lista di liste. `flatMap` fa lo stesso ma poi unisce tutte quelle liste in una sola lista piatta:
```kotlin
val numbers = listOf(1, 2)
println(numbers.map { listOf(it, -it) })     // [[1, -1], [2, -2]]
println(numbers.flatMap { listOf(it, -it) }) // [1, -1, 2, -2]
```
L'ordine viene mantenuto: vengono prima tutti i valori prodotti dal primo elemento, poi quelli del secondo, e così via. Se hai già una lista di liste, `flatten()` le unisce senza una lambda.

---

`zip` accoppia gli elementi di due liste posizione per posizione. Senza una lambda restituisce una lista di valori `Pair`, le cui metà si leggono con `.first` e `.second`; con una lambda, i due elementi di ogni posizione le vengono passati e i risultati vengono raccolti in una lista:
```kotlin
val names = listOf("Ann", "Bob")
val ages = listOf(31, 25)
println(names.zip(ages))                            // [(Ann, 31), (Bob, 25)]
println(names.zip(ages) { name, age -> "$name:$age" }) // [Ann:31, Bob:25]
```
Il risultato è lungo quanto la **più corta** delle due liste: gli elementi in più della più lunga vengono ignorati.

---

La forma della lambda deve corrispondere a quello che il metodo si aspetta:
- i metodi che lavorano su un elemento alla volta (`map`, `filter`, `sortedBy`, `groupBy`...) prendono una lambda con **un parametro**, dove `it` è disponibile
- `reduce`, `fold`, `forEachIndexed` e `zip` con una lambda passano **due** valori, quindi i parametri devono avere un nome esplicito con `a, b ->`
```kotlin
val numbers = listOf(1, 2, 3)
numbers.map { it * 2 }                  // ok: un parametro, it è disponibile
numbers.reduce { acc, n -> acc + n }    // ok: due parametri, con un nome
numbers.reduce { it + 1 }               // errore: it non esiste con due parametri
```
Dare un nome ai parametri è sempre permesso, anche con uno solo: `numbers.map { n -> n * 2 }`.

---

I metodi di ordine superiore possono essere **concatenati**: ognuno restituisce una nuova collezione su cui lavora il successivo, così un intero calcolo si legge come una pipeline da sinistra a destra:
```kotlin
val words = listOf("kiwi", "fig", "banana", "date")
println(words.filter { it.length == 4 }.map { it.uppercase() }.sorted()) // [DATE, KIWI]
```
Anche le mappe hanno metodi di ordine superiore. `mapValues` mantiene le chiavi e sostituisce ogni valore con il risultato della lambda, che riceve l'**entry** con `.key` e `.value`:
```kotlin
val byLength = words.groupBy { it.length }      // {4=[kiwi, date], 3=[fig], 6=[banana]}
println(byLength.mapValues { it.value.size })   // {4=2, 3=1, 6=1}
```

---

In una catena, il tipo di `it` cambia a ogni passo: dopo `filter` su una `List<String>` hai ancora delle stringhe, ma dopo `map { it.length }` hai una `List<Int>`, quindi la lambda successiva vede dei numeri.
```kotlin
val words = listOf("kiwi", "fig")
println(words.map { it.length }.filter { it > 3 }) // [4]
```
Ogni passo restituisce una **nuova** lista e non tocca mai la precedente, quindi una catena può essere spezzata in valori intermedi con un nome senza cambiare il risultato.

---

Una lambda può contenere un'altra chiamata di ordine superiore. Dentro la lambda interna, `it` si riferisce all'elemento **interno** e nasconde quello esterno, quindi dai un nome esplicito al parametro esterno per tenerli raggiungibili entrambi:
```kotlin
val sales = listOf("north" to 120, "south" to 80, "north" to 30)
val byRegion = sales.groupBy { it.first }
val totals = byRegion.mapValues { entry -> entry.value.sumOf { it.second } }
println(totals) // {north=150, south=80}
```
`"north" to 120` crea un `Pair`. Qui la lambda esterna lavora su una entry della mappa, mentre quella interna lavora sulle coppie della lista di quella entry.

---

Una `Map` può essere elaborata come una lista di entry: `filter` e `map` funzionano direttamente sulla mappa e ricevono ogni entry con `.key` e `.value`. `filter` su una mappa restituisce una mappa, mentre `map` restituisce una lista. I metodi di ordinamento come `sortedBy` non sono definiti su una mappa: passa prima da `scores.entries`, che è una collezione delle entry:
```kotlin
val scores = mapOf("Ann" to 90, "Bob" to 72)
println(scores.filter { it.value > 80 })              // {Ann=90}
println(scores.entries.sortedBy { it.value }.map { it.key }) // [Bob, Ann]
```
`scores.entries` è l'insieme di tutte le entry; `scores.keys` e `scores.values` danno solo una delle due parti.
