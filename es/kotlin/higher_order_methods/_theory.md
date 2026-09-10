Un **método de orden superior** es un método que toma una función como argumento. Las colecciones de Kotlin ofrecen muchos, y la función que pasas suele ser una **lambda**: una pequeña función anónima escrita entre llaves.
`map` es el más común: llama a la lambda sobre cada elemento y devuelve una **nueva lista** con los resultados, dejando la original intacta:
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6]
println(numbers) // [1, 2, 3]
```
Cuando la lambda tiene un solo parámetro no hace falta declararlo: Kotlin lo llama `it`. La lambda se escribe después del nombre del método, fuera de los paréntesis, que pueden omitirse cuando la lambda es el único argumento. Esta es la sintaxis de **trailing lambda** y se usa en todos los ejercicios de este tema.

---

`filter` toma una lambda que devuelve un `Boolean`, llamada **predicado**, y devuelve una nueva lista solo con los elementos para los que el predicado es `true`:
```kotlin
val numbers = listOf(4, -2, 7, 0)
println(numbers.filter { it > 0 }) // [4, 7]
```
En lugar de `it` puedes darle un nombre al parámetro, seguido de una flecha `->`. Un parámetro con nombre hace más legibles las lambdas largas, y es obligatorio cuando una lambda está anidada dentro de otra, porque el `it` interior oculta el elemento exterior:
```kotlin
val minLength = 4
val words = listOf("fig", "banana", "kiwi")
println(words.filter { word -> word.length >= minLength }) // [banana, kiwi]
```

---

`forEach` ejecuta la lambda una vez por cada elemento y no devuelve nada. Es la alternativa de orden superior al bucle `for`, y se usa para efectos secundarios como imprimir:
```kotlin
listOf("a", "b").forEach { println(it) }
```
`forEachIndexed` también te da la posición de cada elemento. Su lambda tiene **dos** parámetros, así que deben tener nombre: `it` solo existe para lambdas con exactamente un parámetro.
```kotlin
listOf("a", "b").forEachIndexed { index, letter ->
    println("$index: $letter") // 0: a, luego 1: b
}
```

---

`reduce` combina todos los elementos en un único valor. Su lambda toma dos parámetros: el **acumulador** (el resultado hasta ese momento) y el siguiente elemento. Empieza con el primer elemento como acumulador y ejecuta la lambda para cada elemento restante:
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n }) // 10
```
`reduce` lanza una excepción con una lista vacía, porque no hay un primer elemento del que partir. `fold` lo soluciona: pasas el **valor inicial** del acumulador como argumento, y la lambda se ejecuta para cada elemento, incluido el primero:
```kotlin
println(numbers.fold(0) { acc, n -> acc + n })   // 10
println(listOf<Int>().fold(0) { acc, n -> acc + n }) // 0
```
Con `fold` el acumulador puede incluso tener un tipo distinto al de los elementos, como construir un `String` a partir de una lista de números.

---

Algunos métodos de orden superior responden a una pregunta sobre la colección en lugar de construir una nueva. Todos toman un predicado:
- `any` devuelve `true` si **al menos un** elemento lo cumple
- `all` devuelve `true` si **todos** los elementos lo cumplen
- `none` devuelve `true` si **ningún** elemento lo cumple
- `count` devuelve **cuántos** elementos lo cumplen
```kotlin
val numbers = listOf(1, 2, 3)
println(numbers.any { it > 2 })   // true
println(numbers.all { it > 2 })   // false
println(numbers.none { it > 2 })  // false
println(numbers.count { it > 1 }) // 2
```
Con una lista vacía `any` devuelve `false`, mientras que `all` y `none` devuelven `true`: no hay ningún elemento que rompa la regla.

---

Los métodos de agregación convierten toda una colección en un solo valor:
- `sum()` suma una lista de números, mientras que `sumOf` suma el valor que la lambda calcula para cada elemento
- `maxByOrNull` y `minByOrNull` devuelven el **elemento** para el que la lambda da el valor más grande o más pequeño, o `null` con una lista vacía
```kotlin
val words = listOf("fig", "banana", "kiwi")
println(words.sumOf { it.length })      // 13
println(words.minByOrNull { it.length }) // fig
println(listOf(1, 2, 3).sum())           // 6
```
Fíjate en la diferencia con `maxOf { it.length }`, que devuelve el **valor** más grande (`6`) en lugar del elemento que lo produjo.

---

`sortedBy` devuelve una nueva lista ordenada según el valor que la lambda calcula para cada elemento, de menor a mayor. `sortedByDescending` ordena de mayor a menor. Cuando lo que quieres comparar son los propios elementos, `sorted()` y `sortedDescending()` no necesitan lambda:
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })            // [fig, kiwi, banana]
println(words.sortedByDescending { it.length })  // [banana, kiwi, fig]
println(words.sorted())                          // [banana, fig, kiwi]
```
La ordenación es **estable**: los elementos con la misma clave mantienen su orden relativo original. La lista original nunca se modifica.

---

`take(n)` devuelve una nueva lista con los primeros `n` elementos, y `drop(n)` devuelve una nueva lista **sin** los primeros `n` elementos. Ninguno de los dos toma una lambda, pero a menudo se encadenan después de un método que sí la toma:
```kotlin
val numbers = listOf(5, 3, 8, 1)
println(numbers.take(2))                    // [5, 3]
println(numbers.drop(2))                    // [8, 1]
println(numbers.sortedDescending().take(2)) // [8, 5]
```
`takeWhile` y `dropWhile` son las versiones con predicado: toman o descartan elementos desde el principio **mientras** el predicado sea `true`, y se detienen en el primer elemento que no lo cumple:
```kotlin
println(numbers.takeWhile { it > 2 }) // [5, 3, 8]
```

---

`groupBy` divide una colección en un `Map`: la lambda calcula la **clave** de cada elemento, y cada clave queda asociada a la lista de los elementos que la produjeron, en su orden original:
```kotlin
val words = listOf("fig", "kiwi", "pear")
val byLength = words.groupBy { it.length }
println(byLength)    // {3=[fig], 4=[kiwi, pear]}
println(byLength[4]) // [kiwi, pear]
```
El resultado tiene tipo `Map<K, List<T>>`, donde `K` es el tipo devuelto por la lambda y `T` es el tipo de los elementos. Las claves aparecen en el orden en que se encuentran por primera vez.

---

Cuando la lambda devuelve una **lista** para cada elemento, `map` produce una lista de listas. `flatMap` hace lo mismo pero luego une todas esas listas en una sola lista plana:
```kotlin
val numbers = listOf(1, 2)
println(numbers.map { listOf(it, -it) })     // [[1, -1], [2, -2]]
println(numbers.flatMap { listOf(it, -it) }) // [1, -1, 2, -2]
```
El orden se conserva: primero van todos los valores producidos por el primer elemento, luego los del segundo, y así sucesivamente. Si ya tienes una lista de listas, `flatten()` las une sin lambda.

---

`zip` empareja los elementos de dos listas posición por posición. Sin lambda devuelve una lista de valores `Pair`, cuyas mitades se leen con `.first` y `.second`; con una lambda, los dos elementos de cada posición se le pasan y los resultados se recogen en una lista:
```kotlin
val names = listOf("Ann", "Bob")
val ages = listOf(31, 25)
println(names.zip(ages))                            // [(Ann, 31), (Bob, 25)]
println(names.zip(ages) { name, age -> "$name:$age" }) // [Ann:31, Bob:25]
```
El resultado es tan largo como la **más corta** de las dos listas: los elementos sobrantes de la más larga se ignoran.

---

La forma de la lambda debe coincidir con lo que el método espera:
- los métodos que trabajan con un elemento a la vez (`map`, `filter`, `sortedBy`, `groupBy`...) toman una lambda de **un parámetro**, donde `it` está disponible
- `reduce`, `fold`, `forEachIndexed` y `zip` con lambda pasan **dos** valores, así que los parámetros deben nombrarse explícitamente con `a, b ->`
```kotlin
val numbers = listOf(1, 2, 3)
numbers.map { it * 2 }                  // ok: un parámetro, it está disponible
numbers.reduce { acc, n -> acc + n }    // ok: dos parámetros, con nombre
numbers.reduce { it + 1 }               // error: it no existe con dos parámetros
```
Nombrar los parámetros siempre está permitido, incluso con uno solo: `numbers.map { n -> n * 2 }`.

---

Los métodos de orden superior se pueden **encadenar**: cada uno devuelve una nueva colección sobre la que trabaja el siguiente, así que todo un cálculo se lee como una tubería de izquierda a derecha:
```kotlin
val words = listOf("kiwi", "fig", "banana", "date")
println(words.filter { it.length == 4 }.map { it.uppercase() }.sorted()) // [DATE, KIWI]
```
Los mapas también tienen métodos de orden superior. `mapValues` conserva las claves y sustituye cada valor por el resultado de la lambda, que recibe la **entrada** con `.key` y `.value`:
```kotlin
val byLength = words.groupBy { it.length }      // {4=[kiwi, date], 3=[fig], 6=[banana]}
println(byLength.mapValues { it.value.size })   // {4=2, 3=1, 6=1}
```

---

En una cadena, el tipo de `it` cambia en cada paso: después de `filter` sobre una `List<String>` sigues teniendo cadenas, pero después de `map { it.length }` tienes una `List<Int>`, así que la siguiente lambda ve números.
```kotlin
val words = listOf("kiwi", "fig")
println(words.map { it.length }.filter { it > 3 }) // [4]
```
Cada paso devuelve una lista **nueva** y nunca toca la anterior, así que una cadena se puede dividir en valores intermedios con nombre sin cambiar el resultado.

---

Una lambda puede contener otra llamada de orden superior. Dentro de la lambda interior, `it` se refiere al elemento **interior** y oculta el exterior, así que dale un nombre explícito al parámetro exterior para mantener ambos accesibles:
```kotlin
val sales = listOf("north" to 120, "south" to 80, "north" to 30)
val byRegion = sales.groupBy { it.first }
val totals = byRegion.mapValues { entry -> entry.value.sumOf { it.second } }
println(totals) // {north=150, south=80}
```
`"north" to 120` crea un `Pair`. Aquí la lambda exterior trabaja sobre una entrada del mapa, mientras que la interior trabaja sobre los pares de la lista de esa entrada.

---

Un `Map` se puede procesar como una lista de entradas: `filter` y `map` funcionan directamente sobre el mapa y reciben cada entrada con `.key` y `.value`. `filter` sobre un mapa devuelve un mapa, mientras que `map` devuelve una lista. Los métodos de ordenación como `sortedBy` no están definidos sobre un mapa: pasa antes por `scores.entries`, que es una colección de las entradas:
```kotlin
val scores = mapOf("Ann" to 90, "Bob" to 72)
println(scores.filter { it.value > 80 })              // {Ann=90}
println(scores.entries.sortedBy { it.value }.map { it.key }) // [Bob, Ann]
```
`scores.entries` es el conjunto de todas las entradas; `scores.keys` y `scores.values` dan solo uno de los dos lados.
