Un **array** memorizza un numero fisso di valori dello stesso tipo sotto un unico nome di variabile.
Ne crei uno con `arrayOf`, leggi un elemento con le parentesi quadre e un **indice** che parte da `0`, e ottieni il numero di elementi con `size`:
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
L'ultimo elemento si trova all'indice `size - 1`.

---

`arrayOf(1, 2, 3)` crea un `Array<Int>` in cui ogni elemento è un oggetto boxed.
Per i tipi primitivi Kotlin offre tipi dedicati e più efficienti come `IntArray`, `DoubleArray` e `BooleanArray`:
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
Puoi anche costruire un array di una data dimensione con una lambda di **inizializzazione** che riceve ogni indice, oppure un `IntArray` riempito di zeri:
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

Ogni array ha due proprietà utili per lavorare con gli indici:
- `indices` è l'intervallo di indici validi, da `0` all'ultimo
- `lastIndex` è l'indice dell'ultimo elemento, cioè `size - 1`
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

Anche quando un array è dichiarato con `val`, i suoi **elementi** possono essere sostituiti assegnando un valore a un indice:
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
Per visitare ogni elemento puoi usare un ciclo `for` o `forEach`:
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
Nota che `n` e `it` sono copie in sola lettura dei valori e non possono essere riassegnate, quindi per modificare gli elementi ti serve il loro indice.

---

Per verificare se un array contiene un valore usa `in` o `contains`, entrambi restituiscono un `Boolean`.
`indexOf` restituisce l'indice della prima occorrenza, oppure `-1` quando il valore non è presente:
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

Stampare un array direttamente non mostra i suoi elementi, stampa qualcosa come `[Ljava.lang.String;@1b6d3586`.
Usa `joinToString` per costruire una stringa leggibile, eventualmente con un separatore personalizzato (quello predefinito è `", "`), oppure `contentToString` per ottenere gli elementi tra parentesi quadre:
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

Gli array possono essere ordinati **sul posto** oppure copiati in una nuova collezione ordinata:
- `sort()` e `sortDescending()` riordinano l'array stesso e non restituiscono nulla
- `reverse()` inverte l'ordine dell'array stesso
- `sorted()`, `sortedDescending()` e `reversed()` lasciano l'array invariato e restituiscono una nuova `List`
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

Gli array numerici dispongono di funzioni di aggregazione:
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()` e `min()` lanciano un'eccezione su un array vuoto, usa `maxOrNull()` e `minOrNull()` quando l'array potrebbe essere vuoto.

---

La differenza principale tra un array e una `MutableList` è che un array ha una **dimensione fissa**: una volta creato puoi sostituirne gli elementi, ma non puoi mai aggiungerne o rimuoverne uno, non esiste una funzione `add`.
Espressioni come `nums + 4` non fanno crescere `nums`, ma costruiscono un array completamente nuovo:
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
Preferisci una `MutableList` quando il numero di elementi cambia nel tempo, e un array quando è noto in anticipo o quando ti serve la performance dei tipi primitivi.

---

Gli array supportano le stesse funzioni di trasformazione delle liste. `filter` mantiene gli elementi che soddisfano una condizione e `map` trasforma ogni elemento.
Entrambe restituiscono una nuova `List`, non un array:
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
Dato che il risultato è una lista, stamparla direttamente ne mostra gli elementi.

---

Quando ti servono sia l'indice sia il valore durante un ciclo, usa `withIndex()` e destruttura ogni coppia, oppure `forEachIndexed`:
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

Array e liste si convertono facilmente l'uno nell'altra:
- `toList()` e `toMutableList()` copiano un array in una lista
- `toTypedArray()` copia una lista in un `Array<T>`
- `toIntArray()` copia una lista di `Int` in un `IntArray`
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
Ogni conversione crea una **copia**, quindi modificare il risultato non influisce sull'originale.

---

A differenza delle liste, due array con gli stessi elementi **non** sono uguali con `==`: gli array vengono confrontati per riferimento, quindi `==` è `true` solo per lo stesso identico oggetto array.
Per confrontare i contenuti usa `contentEquals`:
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

Poiché gli array hanno una dimensione fissa, prendere una parte di uno significa creare un nuovo array:
- `copyOf()` copia l'intero array, `copyOf(n)` copia i primi `n` elementi
- `copyOfRange(from, to)` copia gli elementi dall'indice `from` fino a `to` **escluso**
- `sliceArray(range)` copia gli elementi agli indici dell'intervallo, entrambi gli estremi inclusi
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
