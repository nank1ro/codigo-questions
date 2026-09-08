A **closure** is a block of code you can pass around and call later, like a function without a name.
The full closure expression syntax puts the parameters and return type inside curly braces, followed by the `in` keyword and the body:
```swift
{ (parameters) -> ReturnType in
    body
}
```
Like any other value, a closure can be stored in a constant and then called using the constant's name:
```swift
let greet = { (name: String) -> String in
    return "Hello, \(name)!"
}
print(greet("Ada")) // Hello, Ada!
```

---

Writing every type inside the closure is often unnecessary. When the constant has an explicit **function type**, Swift infers the parameter and return types, so you only list the parameter names before `in`:
```swift
let triple: (Int) -> Int = { n in
    return n * 3
}
```
The type `(Int) -> Int` reads "a function that takes an `Int` and returns an `Int`".
When the body is a single expression, the `return` keyword can be omitted too, this is called an **implicit return**:
```swift
let triple: (Int) -> Int = { n in n * 3 }
print(triple(4)) // 12
```

---

Swift goes one step further: inside a closure you can refer to the arguments with the **shorthand argument names** `$0`, `$1`, `$2` and so on, without declaring any parameter or the `in` keyword.
`$0` is the first argument, `$1` the second:
```swift
let add: (Int, Int) -> Int = { $0 + $1 }
print(add(2, 3)) // 5
```
The types still come from the annotation `(Int, Int) -> Int`.

---

Since closures are values, a function can accept one as a parameter. The parameter type is just the function type:
```swift
func apply(_ n: Int, _ operation: (Int) -> Int) -> Int {
    return operation(n)
}
print(apply(5, { $0 + 1 })) // 6
```
The function `apply` doesn't know what `operation` does, it only knows it takes an `Int` and returns an `Int`, and calls it like any other function.

---

When a closure is the **last** argument of a function, you can write it after the closing parenthesis of the call. This is the **trailing closure** syntax:
```swift
print(apply(5) { $0 + 1 }) // 6
```
If the closure is the only argument, the parentheses can be dropped entirely:
```swift
func run(_ task: () -> Int) -> Int {
    return task()
}
print(run { 42 }) // 42
```
Both forms call exactly the same function, the trailing syntax is just easier to read when the closure is long.

---

Closures shine with the array methods that take one as argument. `map` calls the closure on every element and returns a new array with the results:
```swift
let nums = [1, 2, 3]
let doubled = nums.map { $0 * 2 }
print(doubled) // [2, 4, 6]
```
The original array is not changed. Because `map` takes a single closure argument, the trailing closure syntax is the usual way to call it.

---

`filter` keeps only the elements for which the closure returns `true`. The closure receives one element and must return a `Bool`:
```swift
let nums = [5, 12, 8, 20]
let big = nums.filter { $0 > 10 }
print(big) // [12, 20]
```
The elements keep their original order, and the result is a new array of the same element type.

---

`reduce` combines all the elements into a single value. It takes an initial value and a closure with two arguments: the value accumulated so far and the current element. The closure returns the new accumulated value:
```swift
let nums = [1, 2, 3, 4]
let product = nums.reduce(1) { $0 * $1 }
print(product) // 24
```
Here `$0` starts as `1`, then becomes `1 * 1`, `1 * 2`, `2 * 3` and finally `6 * 4`.
Because `map`, `filter` and `reduce` all return values, they can be chained: `nums.filter { $0 > 1 }.map { $0 * 10 }`.

---

`sorted(by:)` returns a new sorted array. The closure receives two elements and returns `true` when the first one should come **before** the second:
```swift
let nums = [3, 1, 2]
print(nums.sorted { $0 < $1 }) // [1, 2, 3]
print(nums.sorted { $0 > $1 }) // [3, 2, 1]
```
The closure can compare anything, for example `words.sorted { $0.count < $1.count }` orders strings from the shortest to the longest.
