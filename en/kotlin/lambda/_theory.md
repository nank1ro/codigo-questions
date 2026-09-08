A **lambda** is a small function without a name, written directly as an expression between curly braces.
The parameters come first, then an arrow `->`, then the body:
```kotlin
val add = { a: Int, b: Int -> a + b }
```
A lambda is a value like any other: you can store it in a variable and call it later with parentheses, exactly like a function:
```kotlin
println(add(2, 3)) // 5
```
A lambda with no parameters has no arrow at all: `val hello = { println("Hello!") }`.

---

Every lambda has a **function type**, written as the parameter types in parentheses, an arrow, and the return type.
The lambda `{ a: Int, b: Int -> a + b }` has the type `(Int, Int) -> Int`: it takes two `Int` values and returns an `Int`.
When you declare the function type on the variable, the parameter types inside the lambda can be left out because the compiler already knows them:
```kotlin
val add: (Int, Int) -> Int = { a, b -> a + b }
val greet: (String) -> Unit = { name -> println("Hi, $name") }
```
A lambda that returns nothing has the return type `Unit`.

---

The body of a lambda can span several lines. There is no `return` keyword: the value of the **last expression** is what the lambda returns.
```kotlin
val describe: (Int) -> String = { n ->
    val half = n / 2
    "half of $n is $half" // returned
}
println(describe(10)) // half of 10 is 5
```
Because `if` is an expression in Kotlin, it can be the last line and decide the result:
```kotlin
val parity: (Int) -> String = { n -> if (n % 2 == 0) "even" else "odd" }
```

---

When a lambda has exactly **one** parameter you can skip declaring it: Kotlin names it `it` for you.
```kotlin
// val double: (Int) -> Int = { n -> n * 2 }
val double: (Int) -> Int = { it * 2 } // same thing
```
`it` only exists when the parameter is not declared explicitly, and only for single-parameter lambdas.
It keeps short lambdas compact, but for longer bodies a real name is clearer.

---

Lambdas are mostly used as arguments of other functions. Collections offer many functions that take a lambda:
- `forEach` runs the lambda once for every element
- `map` builds a new list with the result of the lambda for every element
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map({ it * 2 }) // [2, 4, 6]
```
When the lambda is the **last** argument, you can move it outside the parentheses; when it is the only argument, the parentheses can be dropped altogether. This is called **trailing lambda** syntax and it is the usual way to write it:
```kotlin
val doubled = numbers.map { it * 2 }
doubled.forEach { println(it) }
```

---

A lambda that returns a `Boolean` is called a **predicate**. Several collection functions take one:
- `filter` keeps only the elements for which the predicate is `true`
- `count` returns how many elements satisfy it
- `any` and `all` tell whether some or every element satisfies it
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)
println(numbers.filter { it % 2 == 0 }) // [2, 4, 6]
println(numbers.count { it > 4 })        // 2
println(numbers.any { it > 5 })          // true
```
Calls can be **chained**: each function returns a new list that the next one works on.
```kotlin
println(numbers.filter { it % 2 == 0 }.map { it * 10 }) // [20, 40, 60]
```

---

Lambdas also drive sorting and aggregation:
- `sortedBy` returns a new list ordered by the value the lambda computes for each element; `sortedByDescending` does the opposite
- `reduce` combines all the elements into one value: the lambda receives the accumulated result so far and the next element
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })          // [fig, kiwi, banana]
println(words.sortedByDescending { it.length }) // [banana, kiwi, fig]

val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n })   // 10
```
`reduce` starts with the first element as `acc`, then runs the lambda for every remaining element.

---

With `reduce` the shape of the result is up to the lambda. Any operation that combines two values works: a sum, a product, keeping the larger of the two.
```kotlin
val numbers = listOf(3, 9, 4)
println(numbers.reduce { acc, n -> if (n > acc) n else acc }) // 9
```
Note that `reduce` throws an exception on an empty list, because there is no first element to start from.

---

A lambda can use the variables declared around it, even after the surrounding code has moved on. This is called a **closure**: the lambda *captures* the variables it needs.
Unlike many other languages, Kotlin lets a lambda **modify** a captured `var`:
```kotlin
var clicks = 0
val onClick = { clicks++ }
onClick()
onClick()
println(clicks) // 2
```
Every call of `onClick` updates the same `clicks` variable that the outer code sees.

---

Since a lambda is a value, a function can **return** one. The return type is a function type:
```kotlin
fun multiplier(factor: Int): (Int) -> Int {
    return { it * factor }
}
val triple = multiplier(3)
println(triple(5)) // 15
```
The returned lambda captures `factor`, so each call of `multiplier` builds a different function.
Functions that take or return other functions are called **higher-order functions**.

---

A returned lambda can capture a `var` declared inside the function. That variable lives on after the function has returned, and only the lambda can reach it: it is private state.
```kotlin
fun makeGreeter(): () -> String {
    var calls = 0
    return { calls++; "hello #$calls" }
}
val greeter = makeGreeter()
println(greeter()) // hello #1
println(greeter()) // hello #2
```
Every call of `makeGreeter()` declares a fresh `calls`, so two greeters count independently.

---

You can write your own higher-order functions: a parameter with a function type accepts any lambda of that shape, and inside the function you call it like a regular function.
```kotlin
fun repeatTwice(text: String, transform: (String) -> String): String {
    return transform(transform(text))
}
println(repeatTwice("a", { it + "!" })) // a!!
println(repeatTwice("a") { it + "!" })  // same, with a trailing lambda
```
Putting the function parameter **last** is what makes the trailing lambda syntax available to the callers.

---

When the function you need already exists, there is no need to wrap it in a lambda: a **function reference** `::name` turns a named function into a value with the matching function type.
```kotlin
fun isEven(n: Int) = n % 2 == 0
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { isEven(it) }) // [2, 4]
println(numbers.filter(::isEven))      // [2, 4], same thing
```
Member functions are referenced through their type, like `String::uppercase`:
```kotlin
println(listOf("a", "b").map(String::uppercase)) // [A, B]
```

---

An **anonymous function** is a function declared with `fun` but without a name. It is another way to create a function value:
```kotlin
val square = fun(x: Int): Int {
    return x * x
}
println(square(4)) // 16
```
Differently from a lambda, it can declare its return type explicitly and it uses `return` to produce the value.
Anonymous functions and lambdas are interchangeable: both can be passed to `map`, `filter` or any function that takes a function type.

---

Higher-order functions can both take and return functions. A classic example is **composition**: building a new function that runs one function and feeds its result into another.
```kotlin
fun andThen(first: (Int) -> Int, second: (Int) -> Int): (Int) -> Int {
    return { n -> second(first(n)) }
}
val addOneThenDouble = andThen({ it + 1 }, { it * 2 })
println(addOneThenDouble(3)) // 8
```
The returned lambda captures both `first` and `second`, so it keeps working long after `andThen` has returned.

---

Some functions take a **lambda with receiver**: inside the lambda, `this` is a specific object, so you can call its members directly without naming it.
`buildString` is a common example: inside its lambda `this` is a `StringBuilder`, so `append` can be called as if it were a local function:
```kotlin
val text = buildString {
    append("Hello")
    append(", ")
    append("world")
}
println(text) // Hello, world
```
`buildString` returns the final string. It is a convenient alternative to concatenating with `+` in a loop.
