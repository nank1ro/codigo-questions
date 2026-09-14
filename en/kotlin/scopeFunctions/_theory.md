**Scope functions** run a block of code *inside the context of an object*. They do not add new features to the language: they just make code that works on one object shorter and easier to read. Kotlin has five of them: `let`, `run`, `with`, `apply` and `also`.

They differ on only **two** points: how the object is referenced inside the block, and what the call gives back. We start with `let`: inside its block the object is called `it`, and the call returns the **result of the last expression** of the block.
```kotlin
val word = "kotlin"
val letters = word.let { it.length } // 6
println(letters)
```
Without `let` you would need a temporary variable; with it the object is available under the short name `it` for as long as the block lasts.

---

Because `let` returns the value of its last expression, it is a handy way to **turn a value into something else** without naming an intermediate variable:
```kotlin
val price = 12
val label = price.let { "$it EUR" }
println(label) // 12 EUR
```
Inside the block you can use `it` as many times as you need:
```kotlin
println("kiwi".let { "${it.uppercase()} has ${it.length} letters" })
// KIWI has 4 letters
```

---

`let` becomes really useful after a safe call. `?.let { ... }` runs the block **only** when the value is not `null`, and inside the block `it` is a non-null value, so no extra check is needed:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to ${it.uppercase()}") }
```
When the value is `null` the whole expression is `null` and the block never runs, so the Elvis operator `?:` is the natural partner for supplying a fallback:
```kotlin
fun label(city: String?): String {
    return city?.let { "City: $it" } ?: "No city"
}
```

---

Inside a `let` block you are not forced to call the object `it`: you can give the lambda parameter a name, which keeps the code readable when blocks are nested or when `it` would say nothing useful.
```kotlin
val price: Int? = 12
println(price?.let { amount -> "$amount EUR" }) // 12 EUR
```
The same naming works for every scope function that uses `it`, so for `let` and `also`.

---

`apply` moves on both axes at once: inside its block the object is the receiver `this` (so its members can be used **without any prefix**), and the call returns **the object itself**, not the result of the block.

That combination makes `apply` the tool for **configuring** an object right where you create it:
```kotlin
class Server {
    var host = "localhost"
    var port = 80
}

val server = Server().apply {
    host = "example.com"
    port = 8080
}
println("${server.host}:${server.port}") // example.com:8080
```
`host` and `port` inside the block are `this.host` and `this.port`; because `apply` gives back the configured `Server`, it can be assigned straight away.

---

`apply` is not limited to objects you have just created: it works on any object, and because it gives the object back you can use the whole expression wherever the object is expected.
```kotlin
val box = Box()
box.apply { label = "tools" }        // changes box and returns it
println(listOf(Box().apply { label = "nails" }).size) // 1
```
The block is a normal block of code, so it can hold as many statements as you need.

---

`also` is the mirror image of `apply`: the object is referenced as `it`, and the call returns **the object itself**. Since the block's result is thrown away, `also` is meant for **side effects** such as logging or checking, and it can be dropped in the middle of a chain without changing what the chain produces:
```kotlin
val total = listOf(1, 2, 3)
    .also { println("size: ${it.size}") } // size: 3
    .sum()
println(total) // 6
```
Read it as *"and also do this with it"*: the value keeps flowing to the next step untouched.

---

When the block needs the object as an **argument** of something else, `also` reads better than `apply`: `it` can be handed over directly, while `this` would have to be spelled out.
```kotlin
val names = mutableListOf<String>()
val user = "ada".also { names.add(it) }
println(user)  // ada
println(names) // [ada]
```
The value of the expression is still `"ada"`: `also` only watches it go by.

---

`run` is `let` with the other way of naming the object: inside the block the object is `this`, so its members need no prefix, and the call returns the **result of the last expression**.

It fits when you read several members of the same object to compute one value:
```kotlin
class Rect(val w: Int, val h: Int)

val area = Rect(3, 4).run { w * h }
println(area) // 12
```
Compare it with `apply`, which uses `this` in the very same way but hands back the object instead of the block's result.

---

`with` does the same job as `run`, but it is **not** an extension: the object is passed as the first argument instead of being the receiver of a dot call.
```kotlin
val text = with(StringBuilder()) {
    append("Hello")
    append(", world")
    toString()
}
println(text) // Hello, world
```
Inside the block the object is `this` and the call returns the last expression, exactly like `run`. Prefer `with` when you already have a non-null object and want to group several calls on it; prefer `run` when the object comes out of a chain or may need a safe call (`obj?.run { ... }`).

---

All five scope functions are now on the table, and each one is just a point on the two axes:
- `let` - the object is `it`, returns the result of the block
- `run` - the object is `this`, returns the result of the block
- `with` - the object is `this` (passed as an argument), returns the result of the block
- `apply` - the object is `this`, returns the object
- `also` - the object is `it`, returns the object

Pick the row you need: `it` reads better when you pass the object on to something else, `this` reads better when you touch many of its members; return the block's result when you want a new value, return the object when you want to keep working with it.
