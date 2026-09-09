A **higher-order function** is a function that takes another function as argument, returns one, or both. You already met `map`, `filter`, `reduce` and `sorted(by:)`: they take a closure and apply it to the elements of a collection. Swift has many more of them, and knowing them lets you replace long loops with a single readable line.
`compactMap` works like `map`, but the closure returns an optional and the `nil` results are dropped:
```swift
let words = ["3", "seven", "12"]
let numbers = words.compactMap { Int($0) }
print(numbers) // [3, 12]
```
`Int("seven")` is `nil`, so that element disappears and the result is a `[Int]`, not a `[Int?]`.

---

`flatMap` is for closures that return an **array**: instead of building an array of arrays, it joins all the returned arrays into one flat result:
```swift
let teams = [["Ann", "Bob"], ["Cid"]]
print(teams.map { $0 })     // [["Ann", "Bob"], ["Cid"]]
print(teams.flatMap { $0 }) // ["Ann", "Bob", "Cid"]
```
The closure can also transform each inner array before it is flattened, for example `teams.flatMap { $0.reversed() }` gives `["Bob", "Ann", "Cid"]`.

---

The three `map` variants differ only in what the closure returns:
- `map`: any value, one result per element
- `compactMap`: an optional, the `nil` results are dropped
- `flatMap`: an array, all the results are joined into one array

The closure passed to `flatMap` can itself call `map` on the inner array, nesting one transformation inside the other:
```swift
let matrix = [[1, 2], [3]]
print(matrix.flatMap { row in row.map { $0 + 1 } }) // [2, 3, 4]
```

---

`reduce` builds a new accumulated value at every step, which is wasteful when the result is an array or a dictionary. `reduce(into:)` gives the closure the accumulator as an `inout` parameter, so it can be modified in place with no `return`:
```swift
let words = ["a", "b", "a"]
let counts = words.reduce(into: [String: Int]()) { result, word in
    result[word, default: 0] += 1
}
print(counts["a"]!) // 2
```
`[String: Int]()` creates an empty dictionary, and `result[word, default: 0]` reads the current count or `0` when the key is missing.

---

Some higher-order functions answer a question about the collection instead of transforming it. They all take a closure that returns a `Bool`:
- `first(where:)` returns the first element that satisfies the closure, or `nil` if there is none
- `contains(where:)` returns `true` if at least one element satisfies it
- `allSatisfy` returns `true` if every element satisfies it

```swift
let nums = [4, 9, 16]
print(nums.first(where: { $0 > 5 }))  // Optional(9)
print(nums.contains(where: { $0 > 5 })) // true
print(nums.allSatisfy { $0 > 5 })       // false
```
Unlike `filter`, `first(where:)` stops at the first match and doesn't build a new array.

---

`contains(where:)` and `allSatisfy` replace the common pattern of a loop with a flag variable. Both stop as soon as the answer is known: `contains(where:)` at the first match, `allSatisfy` at the first element that fails.
```swift
let ages = [15, 22, 40]
let anyMinor = ages.contains { $0 < 18 }  // true
let allAdults = ages.allSatisfy { $0 >= 18 } // false
```
`contains { ... }` is the trailing closure form of `contains(where:)`, not to be confused with `contains(_:)`, which looks for a specific value.

---

Higher-order functions work on any array, including arrays of your own structs. Chaining `filter` and then `map` is the usual way to select some elements and extract a value from each:
```swift
struct Book {
    var title: String
    var pages: Int
}
let books = [Book(title: "Dune", pages: 412), Book(title: "Haiku", pages: 40)]
let long = books.filter { $0.pages > 100 }.map { $0.title }
print(long) // ["Dune"]
```
Doing it in the opposite order, `map` then `filter`, would lose the `pages` property before the check could use it.

---

When a closure only reads one property, you can pass a **key path** instead: `\.name` means "the `name` property of the element", and `map(\.name)` is the same as `map { $0.name }`.
Sorting by a property uses the usual two-argument closure, comparing that property on both elements:
```swift
struct City {
    var name: String
    var population: Int
}
let cities = [City(name: "Oslo", population: 700), City(name: "Rome", population: 2800)]
let byPopulation = cities.sorted { $0.population > $1.population }
print(byPopulation.map(\.name)) // ["Rome", "Oslo"]
```

---

To sort by **more than one criterion**, compare the first property and fall back to the second one only when the first values are equal:
```swift
let sorted = people.sorted {
    if $0.age != $1.age {
        return $0.age < $1.age
    }
    return $0.name < $1.name
}
```
Here people are ordered by age, and people with the same age are ordered by name. The closure must return `true` only when the first element should come before the second, so the equal case falls through to the next comparison.

---

`enumerated()` turns an array into a sequence of `(offset, element)` pairs, so a closure can use the position of each element together with its value:
```swift
let steps = ["mix", "bake"]
let numbered = steps.enumerated().map { pair in
    "\(pair.offset + 1). \(pair.element)"
}
print(numbered) // ["1. mix", "2. bake"]
```
Because each pair is a tuple, the closure can also destructure it: `.map { (i, step) in "\(i + 1). \(step)" }`.

---

`zip` pairs up the elements of two sequences position by position, producing a sequence of tuples. It stops at the end of the shorter one:
```swift
let names = ["Ann", "Bob"]
let ages = [31, 27, 99]
let pairs = zip(names, ages).map { "\($0) is \($1)" }
print(pairs) // ["Ann is 31", "Bob is 27"]
```
Inside the closure `$0` is the element from the first sequence and `$1` the one from the second. `zip` is a free function, not a method: you write `zip(a, b)`, not `a.zip(b)`.

---

`forEach` is the higher-order twin of the `for-in` loop: it calls the closure once per element, in order. The difference is in how you leave the loop. In a `for-in` you can `break` out or `continue`; inside a `forEach` closure `break` and `continue` are not allowed, and `return` only ends the **current call** of the closure, then the next element is processed as usual:
```swift
[1, 2, 3].forEach { n in
    if n == 2 { return }
    print(n)
}
// prints 1 and 3
```
Use `forEach` for a short side effect on every element, and `for-in` when you need to stop early.

---

`Dictionary(grouping:by:)` splits a collection into a dictionary of arrays. The closure computes the **key** of each element, and all the elements with the same key end up in the same array:
```swift
let words = ["apple", "bee", "avocado"]
let byInitial = Dictionary(grouping: words, by: { $0.first! })
print(byInitial["a"]!) // ["apple", "avocado"]
```
`mapValues` transforms every value of a dictionary while keeping the keys, so it is the natural next step after grouping:
```swift
let sizes = byInitial.mapValues { $0.count }
print(sizes["a"]!) // 2
```

---

`prefix(while:)` takes elements from the start **as long as** the closure returns `true`, and stops at the first element that fails, even if later elements would pass again. `drop(while:)` is its complement: it skips that same starting run and returns everything else:
```swift
let temps = [12, 15, 21, 14]
print(temps.prefix { $0 < 20 }) // [12, 15]
print(temps.drop { $0 < 20 })   // [21, 14]
```
Both return an `ArraySlice`, a view on the original array that prints like an array and can be turned into one with `Array(...)`.

---

You can write your own higher-order functions. A function that takes a closure and **returns a new closure** built from it is a common pattern: the returned closure captures the original one, so the parameter must be `@escaping`.
For example, `negate` turns a predicate into its opposite, ready to be passed to `filter`:
```swift
func negate(_ predicate: @escaping (Int) -> Bool) -> (Int) -> Bool {
    return { !predicate($0) }
}
let isEven: (Int) -> Bool = { $0 % 2 == 0 }
print([1, 2, 3, 4].filter(negate(isEven))) // [1, 3]
```
Note that `filter(negate(isEven))` passes the closure as a normal argument, without trailing closure syntax.

---

`map` and `filter` on an array are **eager**: each one processes the whole array and builds a new one before the next step runs. On a large collection, or when you only need the first result, that is wasted work.
The `lazy` property returns a view whose operations run only when an element is actually requested, one element at a time through the whole chain:
```swift
let firstBig = (1...1000).lazy.map { $0 * $0 }.first { $0 > 50 }
print(firstBig!) // 64
```
Here only `1, 2, ..., 8` are squared: `first(where:)` asks for elements until one satisfies the condition, and the chain stops there. Without `lazy`, `map` would square all 1000 numbers first.
