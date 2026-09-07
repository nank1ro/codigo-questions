A function is a block of code that performs a specific task and can be reused throughout your program.
In Kotlin, you define a function using the `fun` keyword, followed by the function name and parentheses:
```kotlin
fun greet() {
    println("Hello!")
}
```
To call (execute) a function, use its name followed by parentheses:
```kotlin
greet() // prints Hello!
```
A function that does not return a value implicitly returns `Unit`.

---

Functions can return a value. You specify the return type after the parentheses using a colon:
```kotlin
fun getNumber(): Int {
    return 42
}
```
The `return` keyword sends a value back to the caller:
```kotlin
var result = getNumber()
println(result) // prints 42
```
The return type must match the type of the value you return.

---

Functions can accept parameters, which are inputs you pass when calling the function.
Parameters are declared inside the parentheses with a name and type:
```kotlin
fun greet(name: String) {
    println("Hello, $name!")
}
```
You pass arguments when calling the function:
```kotlin
greet("Alice") // prints Hello, Alice!
```
Parameters let you write reusable code that works with different values.

---

Kotlin supports default parameter values. If a caller doesn't provide an argument, the default value is used:
```kotlin
fun greet(name: String = "World") {
    println("Hello, $name!")
}
greet()         // prints Hello, World!
greet("Alice")  // prints Hello, Alice!
```
Default values make parameters optional, reducing the need for overloaded functions.

---

When a function body consists of a single expression, you can use the single-expression syntax with `=`:
```kotlin
fun square(n: Int): Int = n * n
```
This is more concise than the block body form. Kotlin can often infer the return type, so you can also write:
```kotlin
fun square(n: Int) = n * n
```
Single-expression functions are a common Kotlin idiom for simple computations.

---

Functions can return `Boolean` values, which is useful for checking conditions:
```kotlin
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
println(isEven(4)) // prints true
println(isEven(7)) // prints false
```
A `Boolean` function returns either `true` or `false`.

---

Functions can have multiple parameters of different types:
```kotlin
fun introduce(name: String, age: Int): String {
    return "My name is $name and I am $age years old."
}
println(introduce("Bob", 30))
// prints My name is Bob and I am 30 years old.
```
Named arguments let you pass values in any order using the parameter name:
```kotlin
println(introduce(age = 30, name = "Bob"))
```

---

A basic function in Kotlin uses the `fun` keyword followed by a name and parentheses:
```kotlin
fun sayBye() {
    println("Bye!")
}
```

---

To declare a return type for a function, add a colon and the type after the parentheses:
```kotlin
fun getName(): String {
    return "Alice"
}
```

---

A function parameter is declared with a name, a colon, and a type:
```kotlin
fun greet(name: String) {
    println("Hi, $name!")
}
```

---

A single-expression function uses `=` instead of a block body:
```kotlin
fun triple(n: Int) = n * 3
```
This is shorthand for:
```kotlin
fun triple(n: Int): Int {
    return n * 3
}
```
