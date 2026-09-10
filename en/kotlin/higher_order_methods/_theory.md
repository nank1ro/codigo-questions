A **higher-order method** is a method that takes a function as an argument. Kotlin collections offer many of them, and the function you pass is usually a **lambda**: a small anonymous function written between curly braces.
`map` is the most common one: it calls the lambda on every element and returns a **new list** with the results, leaving the original untouched:
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6]
println(numbers) // [1, 2, 3]
```
When the lambda has a single parameter you don't need to declare it: Kotlin names it `it`. The lambda is written after the method name, outside the parentheses, which can be omitted when the lambda is the only argument. This is the **trailing lambda** syntax and it is used in every exercise of this topic.

---

`filter` takes a lambda that returns a `Boolean`, called a **predicate**, and returns a new list with only the elements for which the predicate is `true`:
```kotlin
val numbers = listOf(4, -2, 7, 0)
println(numbers.filter { it > 0 }) // [4, 7]
```
Instead of `it` you can give the parameter a name, followed by an arrow `->`. A named parameter makes longer lambdas easier to read, and it is required when a lambda is nested inside another one, because the inner `it` hides the outer element:
```kotlin
val minLength = 4
val words = listOf("fig", "banana", "kiwi")
println(words.filter { word -> word.length >= minLength }) // [banana, kiwi]
```

---

`forEach` runs the lambda once for every element and returns nothing. It is the higher-order alternative to a `for` loop, and it is used for side effects like printing:
```kotlin
listOf("a", "b").forEach { println(it) }
```
`forEachIndexed` also gives you the position of each element. Its lambda has **two** parameters, so they must be named: `it` only exists for lambdas with exactly one parameter.
```kotlin
listOf("a", "b").forEachIndexed { index, letter ->
    println("$index: $letter") // 0: a, then 1: b
}
```

---

`reduce` combines all the elements into a single value. Its lambda takes two parameters: the **accumulator** (the result so far) and the next element. It starts with the first element as accumulator and runs the lambda for every remaining element:
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n }) // 10
```
`reduce` throws an exception on an empty list, because there is no first element to start from. `fold` fixes that: you pass the **initial value** of the accumulator as an argument, and the lambda runs for every element, including the first:
```kotlin
println(numbers.fold(0) { acc, n -> acc + n })   // 10
println(listOf<Int>().fold(0) { acc, n -> acc + n }) // 0
```
With `fold` the accumulator can even have a different type from the elements, like building a `String` out of a list of numbers.

---

Some higher-order methods answer a question about the collection instead of building a new one. They all take a predicate:
- `any` returns `true` if **at least one** element satisfies it
- `all` returns `true` if **every** element satisfies it
- `none` returns `true` if **no** element satisfies it
- `count` returns **how many** elements satisfy it
```kotlin
val numbers = listOf(1, 2, 3)
println(numbers.any { it > 2 })   // true
println(numbers.all { it > 2 })   // false
println(numbers.none { it > 2 })  // false
println(numbers.count { it > 1 }) // 2
```
On an empty list `any` returns `false`, while `all` and `none` return `true`: there is no element that breaks the rule.

---

Aggregation methods turn a whole collection into one value:
- `sum()` adds up a list of numbers, while `sumOf` adds up the value the lambda computes for each element
- `maxByOrNull` and `minByOrNull` return the **element** for which the lambda gives the largest or smallest value, or `null` on an empty list
```kotlin
val words = listOf("fig", "banana", "kiwi")
println(words.sumOf { it.length })      // 13
println(words.minByOrNull { it.length }) // fig
println(listOf(1, 2, 3).sum())           // 6
```
Note the difference with `maxOf { it.length }`, which returns the largest **value** (`6`) instead of the element that produced it.

---

`sortedBy` returns a new list ordered by the value the lambda computes for each element, from the smallest up. `sortedByDescending` orders from the largest down. When the elements themselves are what you want to compare, `sorted()` and `sortedDescending()` need no lambda:
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })            // [fig, kiwi, banana]
println(words.sortedByDescending { it.length })  // [banana, kiwi, fig]
println(words.sorted())                          // [banana, fig, kiwi]
```
The sort is **stable**: elements with the same key keep their original relative order. The original list is never modified.

---

`take(n)` returns a new list with the first `n` elements, and `drop(n)` returns a new list **without** the first `n` elements. Neither of them takes a lambda, but they are often chained after a method that does:
```kotlin
val numbers = listOf(5, 3, 8, 1)
println(numbers.take(2))                    // [5, 3]
println(numbers.drop(2))                    // [8, 1]
println(numbers.sortedDescending().take(2)) // [8, 5]
```
`takeWhile` and `dropWhile` are the versions with a predicate: they take or drop elements from the start **as long as** the predicate is `true`, and stop at the first element that fails it:
```kotlin
println(numbers.takeWhile { it > 2 }) // [5, 3, 8]
```

---

`groupBy` splits a collection into a `Map`: the lambda computes the **key** of each element, and every key is mapped to the list of the elements that produced it, in their original order:
```kotlin
val words = listOf("fig", "kiwi", "pear")
val byLength = words.groupBy { it.length }
println(byLength)    // {3=[fig], 4=[kiwi, pear]}
println(byLength[4]) // [kiwi, pear]
```
The result has type `Map<K, List<T>>`, where `K` is the type returned by the lambda and `T` is the type of the elements. Keys appear in the order they are first met.

---

When the lambda returns a **list** for each element, `map` produces a list of lists. `flatMap` does the same but then joins all those lists into a single flat one:
```kotlin
val numbers = listOf(1, 2)
println(numbers.map { listOf(it, -it) })     // [[1, -1], [2, -2]]
println(numbers.flatMap { listOf(it, -it) }) // [1, -1, 2, -2]
```
The order is preserved: all the values produced by the first element come first, then those of the second, and so on. If you already have a list of lists, `flatten()` joins them without a lambda.

---

`zip` pairs up the elements of two lists position by position. Without a lambda it returns a list of `Pair` values, whose halves are read with `.first` and `.second`; with a lambda, the two elements of each position are passed to it and the results are collected in a list:
```kotlin
val names = listOf("Ann", "Bob")
val ages = listOf(31, 25)
println(names.zip(ages))                            // [(Ann, 31), (Bob, 25)]
println(names.zip(ages) { name, age -> "$name:$age" }) // [Ann:31, Bob:25]
```
The result is as long as the **shorter** of the two lists: extra elements of the longer one are ignored.

---

The shape of the lambda must match what the method expects:
- methods that work on one element at a time (`map`, `filter`, `sortedBy`, `groupBy`...) take a **one-parameter** lambda, where `it` is available
- `reduce`, `fold`, `forEachIndexed` and `zip` with a lambda pass **two** values, so the parameters must be named explicitly with `a, b ->`
```kotlin
val numbers = listOf(1, 2, 3)
numbers.map { it * 2 }                  // ok: one parameter, it is available
numbers.reduce { acc, n -> acc + n }    // ok: two parameters, named
numbers.reduce { it + 1 }               // error: it does not exist with two parameters
```
Naming the parameters is always allowed, even with one: `numbers.map { n -> n * 2 }`.

---

Higher-order methods can be **chained**: each one returns a new collection that the next one works on, so a whole computation reads as a pipeline from left to right:
```kotlin
val words = listOf("kiwi", "fig", "banana", "date")
println(words.filter { it.length == 4 }.map { it.uppercase() }.sorted()) // [DATE, KIWI]
```
Maps have higher-order methods too. `mapValues` keeps the keys and replaces every value with the result of the lambda, which receives the **entry** with `.key` and `.value`:
```kotlin
val byLength = words.groupBy { it.length }      // {4=[kiwi, date], 3=[fig], 6=[banana]}
println(byLength.mapValues { it.value.size })   // {4=2, 3=1, 6=1}
```

---

In a chain, the type of `it` changes at every step: after `filter` on a `List<String>` you still have strings, but after `map { it.length }` you have a `List<Int>`, so the next lambda sees numbers.
```kotlin
val words = listOf("kiwi", "fig")
println(words.map { it.length }.filter { it > 3 }) // [4]
```
Every step returns a **new** list and never touches the previous one, so a chain can be split into named intermediate values without changing the result.

---

A lambda can contain another higher-order call. Inside the inner lambda, `it` refers to the **inner** element and hides the outer one, so name the outer parameter explicitly to keep both reachable:
```kotlin
val sales = listOf("north" to 120, "south" to 80, "north" to 30)
val byRegion = sales.groupBy { it.first }
val totals = byRegion.mapValues { entry -> entry.value.sumOf { it.second } }
println(totals) // {north=150, south=80}
```
`"north" to 120` creates a `Pair`. Here the outer lambda works on a map entry, while the inner one works on the pairs of that entry's list.

---

A `Map` can be processed like a list of entries: `filter` and `map` work directly on the map and receive each entry with `.key` and `.value`. `filter` on a map returns a map, while `map` returns a list. Sorting methods such as `sortedBy` are not defined on a map: go through `scores.entries` first, which is a collection of the entries:
```kotlin
val scores = mapOf("Ann" to 90, "Bob" to 72)
println(scores.filter { it.value > 80 })              // {Ann=90}
println(scores.entries.sortedBy { it.value }.map { it.key }) // [Bob, Ann]
```
`scores.entries` is the set of all the entries; `scores.keys` and `scores.values` give only one side.
