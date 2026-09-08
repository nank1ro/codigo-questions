Una **lambda** è una piccola funzione senza nome, scritta direttamente come espressione tra parentesi graffe.
I parametri vengono prima, poi una freccia `->`, poi il corpo:
```kotlin
val add = { a: Int, b: Int -> a + b }
```
Una lambda è un valore come tutti gli altri: si può memorizzare in una variabile e richiamare in seguito con le parentesi, esattamente come una funzione:
```kotlin
println(add(2, 3)) // 5
```
Una lambda senza parametri non ha proprio una freccia: `val hello = { println("Hello!") }`.

---

Ogni lambda ha un **tipo funzione**, scritto come i tipi dei parametri tra parentesi, una freccia e il tipo di ritorno.
La lambda `{ a: Int, b: Int -> a + b }` ha tipo `(Int, Int) -> Int`: prende due valori `Int` e restituisce un `Int`.
Quando dichiari il tipo funzione sulla variabile, i tipi dei parametri all'interno della lambda possono essere omessi, perché il compilatore li conosce già:
```kotlin
val add: (Int, Int) -> Int = { a, b -> a + b }
val greet: (String) -> Unit = { name -> println("Hi, $name") }
```
Una lambda che non restituisce nulla ha il tipo di ritorno `Unit`.

---

Il corpo di una lambda può occupare più righe. Non esiste la parola chiave `return`: il valore dell'**ultima espressione** è ciò che la lambda restituisce.
```kotlin
val describe: (Int) -> String = { n ->
    val half = n / 2
    "half of $n is $half" // returned
}
println(describe(10)) // half of 10 is 5
```
Poiché `if` è un'espressione in Kotlin, può essere l'ultima riga e decidere il risultato:
```kotlin
val parity: (Int) -> String = { n -> if (n % 2 == 0) "even" else "odd" }
```

---

Quando una lambda ha esattamente **un** parametro puoi evitare di dichiararlo: Kotlin lo chiama `it` per te.
```kotlin
// val double: (Int) -> Int = { n -> n * 2 }
val double: (Int) -> Int = { it * 2 } // same thing
```
`it` esiste solo quando il parametro non è dichiarato esplicitamente, e solo per le lambda con un solo parametro.
Mantiene compatte le lambda brevi, ma per corpi più lunghi un vero nome è più chiaro.

---

Le lambda vengono per lo più usate come argomenti di altre funzioni. Le collezioni offrono molte funzioni che prendono una lambda:
- `forEach` esegue la lambda una volta per ogni elemento
- `map` costruisce una nuova lista con il risultato della lambda per ogni elemento
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map({ it * 2 }) // [2, 4, 6]
```
Quando la lambda è l'**ultimo** argomento, puoi spostarla fuori dalle parentesi; quando è l'unico argomento, le parentesi possono essere del tutto omesse. Questa si chiama sintassi della **trailing lambda** ed è il modo usuale di scriverla:
```kotlin
val doubled = numbers.map { it * 2 }
doubled.forEach { println(it) }
```

---

Una lambda che restituisce un `Boolean` si chiama **predicato**. Diverse funzioni delle collezioni ne accettano uno:
- `filter` mantiene solo gli elementi per cui il predicato è `true`
- `count` restituisce quanti elementi lo soddisfano
- `any` e `all` dicono se alcuni o tutti gli elementi lo soddisfano
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)
println(numbers.filter { it % 2 == 0 }) // [2, 4, 6]
println(numbers.count { it > 4 })        // 2
println(numbers.any { it > 5 })          // true
```
Le chiamate possono essere **incatenate**: ogni funzione restituisce una nuova lista su cui lavora la successiva.
```kotlin
println(numbers.filter { it % 2 == 0 }.map { it * 10 }) // [20, 40, 60]
```

---

Le lambda guidano anche l'ordinamento e l'aggregazione:
- `sortedBy` restituisce una nuova lista ordinata in base al valore che la lambda calcola per ogni elemento; `sortedByDescending` fa l'opposto
- `reduce` combina tutti gli elementi in un solo valore: la lambda riceve il risultato accumulato fino a quel momento e l'elemento successivo
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })          // [fig, kiwi, banana]
println(words.sortedByDescending { it.length }) // [banana, kiwi, fig]

val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n })   // 10
```
`reduce` parte dal primo elemento come `acc`, poi esegue la lambda per ogni elemento rimanente.

---

Con `reduce` la forma del risultato dipende dalla lambda. Qualsiasi operazione che combina due valori va bene: una somma, un prodotto, il mantenimento del maggiore dei due.
```kotlin
val numbers = listOf(3, 9, 4)
println(numbers.reduce { acc, n -> if (n > acc) n else acc }) // 9
```
Nota che `reduce` lancia un'eccezione su una lista vuota, perché non c'è un primo elemento da cui partire.

---

Una lambda può usare le variabili dichiarate attorno a essa, anche dopo che il codice circostante è terminato. Questo si chiama **closure**: la lambda *cattura* le variabili di cui ha bisogno.
A differenza di molti altri linguaggi, Kotlin permette a una lambda di **modificare** una `var` catturata:
```kotlin
var clicks = 0
val onClick = { clicks++ }
onClick()
onClick()
println(clicks) // 2
```
Ogni chiamata di `onClick` aggiorna la stessa variabile `clicks` che il codice esterno vede.

---

Poiché una lambda è un valore, una funzione può **restituirne** una. Il tipo di ritorno è un tipo funzione:
```kotlin
fun multiplier(factor: Int): (Int) -> Int {
    return { it * factor }
}
val triple = multiplier(3)
println(triple(5)) // 15
```
La lambda restituita cattura `factor`, quindi ogni chiamata di `multiplier` costruisce una funzione diversa.
Le funzioni che prendono o restituiscono altre funzioni si chiamano **funzioni di ordine superiore**.

---

Una lambda restituita può catturare una `var` dichiarata all'interno della funzione. Quella variabile continua a vivere dopo che la funzione ha restituito, e solo la lambda può raggiungerla: è uno stato privato.
```kotlin
fun makeGreeter(): () -> String {
    var calls = 0
    return { calls++; "hello #$calls" }
}
val greeter = makeGreeter()
println(greeter()) // hello #1
println(greeter()) // hello #2
```
Ogni chiamata di `makeGreeter()` dichiara una nuova `calls`, quindi due greeter contano indipendentemente.

---

Puoi scrivere le tue funzioni di ordine superiore: un parametro con un tipo funzione accetta qualsiasi lambda di quella forma, e all'interno della funzione la richiami come una funzione normale.
```kotlin
fun repeatTwice(text: String, transform: (String) -> String): String {
    return transform(transform(text))
}
println(repeatTwice("a", { it + "!" })) // a!!
println(repeatTwice("a") { it + "!" })  // same, with a trailing lambda
```
Mettere il parametro funzione **per ultimo** è ciò che rende disponibile ai chiamanti la sintassi della trailing lambda.

---

Quando la funzione di cui hai bisogno esiste già, non c'è bisogno di incapsularla in una lambda: un **riferimento a funzione** `::nome` trasforma una funzione con nome in un valore con il tipo funzione corrispondente.
```kotlin
fun isEven(n: Int) = n % 2 == 0
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { isEven(it) }) // [2, 4]
println(numbers.filter(::isEven))      // [2, 4], same thing
```
Le funzioni membro si referenziano attraverso il loro tipo, come `String::uppercase`:
```kotlin
println(listOf("a", "b").map(String::uppercase)) // [A, B]
```

---

Una **funzione anonima** è una funzione dichiarata con `fun` ma senza nome. È un altro modo per creare un valore funzione:
```kotlin
val square = fun(x: Int): Int {
    return x * x
}
println(square(4)) // 16
```
A differenza di una lambda, può dichiarare esplicitamente il suo tipo di ritorno e usa `return` per produrre il valore.
Le funzioni anonime e le lambda sono intercambiabili: entrambe possono essere passate a `map`, `filter` o a qualsiasi funzione che accetti un tipo funzione.

---

Le funzioni di ordine superiore possono sia prendere che restituire funzioni. Un classico esempio è la **composizione**: costruire una nuova funzione che esegue una funzione e passa il suo risultato a un'altra.
```kotlin
fun andThen(first: (Int) -> Int, second: (Int) -> Int): (Int) -> Int {
    return { n -> second(first(n)) }
}
val addOneThenDouble = andThen({ it + 1 }, { it * 2 })
println(addOneThenDouble(3)) // 8
```
La lambda restituita cattura sia `first` che `second`, quindi continua a funzionare molto tempo dopo che `andThen` ha restituito.

---

Alcune funzioni prendono una **lambda con receiver**: all'interno della lambda, `this` è un oggetto specifico, quindi puoi chiamare i suoi membri direttamente senza nominarlo.
`buildString` è un esempio comune: dentro la sua lambda `this` è un `StringBuilder`, quindi `append` può essere chiamata come se fosse una funzione locale:
```kotlin
val text = buildString {
    append("Hello")
    append(", ")
    append("world")
}
println(text) // Hello, world
```
`buildString` restituisce la stringa finale. È un'alternativa comoda alla concatenazione con `+` in un ciclo.
