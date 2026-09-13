Some work does not finish immediately: downloading a file, reading from a database, waiting for a timer. If a program simply stopped and waited, nothing else could happen in the meantime. Swift solves this with **asynchronous functions**.

A function marked **`async`** is allowed to pause in the middle and resume later. The keyword goes after the parameter list, before the arrow:
```swift
func fetchNumber() async -> Int {
    return 42
}
```
Calling it is different too: you must write **`await`** in front of the call. `await` marks the exact point where the program may pause, and gives you the plain value once the function is done:
```swift
let n = await fetchNumber()
print(n)
// prints 42
```
In a Swift script the top level already supports `await`, so you can call asynchronous functions directly, without any extra setup. Forgetting `async` or `await` is a compile error, not a silent bug.

---

An asynchronous function is still an ordinary function: it can take parameters and return a value of any type. Only two things change, the `async` keyword in the signature and the `await` at every call site:
```swift
func price(of quantity: Int) async -> Double {
    return Double(quantity) * 2.5
}

let total = await price(of: 4)
print(total)
// prints 10.0
```
The returned value is a normal `Double`, not a wrapper: once `await` has finished, you work with it exactly as usual.

---

Asynchronous functions are usually built on top of each other. Inside an `async` function you may `await` any other `async` function, and the result is used like any normal value:
```swift
func base() async -> Int {
    return 10
}

func withBonus() async -> Int {
    let value = await base()
    return value + 5
}

print(await withBonus())
// prints 15
```
`await` is only allowed inside an asynchronous context: an `async` function, or the top level of a script. A plain, non-`async` function cannot `await` anything.

---

Work that happens over time often fails: a server is down, a file is missing, the input is wrong. Such a function is marked **`async throws`**, and it is called with **`try await`**:
```swift
enum LoadError: Error {
    case missing
}

func load(_ name: String) async throws -> String {
    if name.isEmpty {
        throw LoadError.missing
    }
    return "file: \(name)"
}
```
To handle the error you wrap the call in a `do` block and catch it:
```swift
do {
    let text = try await load("")
    print(text)
} catch {
    print("could not load")
}
// prints could not load
```
The order of the keywords is fixed: `try` comes first, then `await`.

---

When you do not care *why* the call failed, `try?` is shorter than a `do` block. It turns a throwing call into an **optional**: the value on success, `nil` on failure. Combined with `await` it is written `try? await`:
```swift
let value = try? await parse("42")  // Optional(42)
let broken = try? await parse("x")  // nil
```
Because the result is optional, it fits straight into an `if let`:
```swift
if let value = try? await parse("x") {
    print(value)
} else {
    print("not a number")
}
```
Use `try? await` for a quick fallback, and `do` / `catch` when the error itself matters.

---

Several `await` calls written one after the other run **sequentially**: the second call does not even start until the first one has returned. The code reads top to bottom, exactly like ordinary code:
```swift
func step(_ name: String) async -> String {
    print("start \(name)")
    return "done \(name)"
}

let a = await step("A")
print(a)
let b = await step("B")
print(b)
// start A
// done A
// start B
// done B
```
This is what you want when the second call needs the result of the first. When the calls are independent, waiting for one before starting the other is wasted time, and the next exercises show how to avoid it.

---

To run two independent calls at the same time, declare them with **`async let`**. The work starts immediately, and the program keeps going without waiting:
```swift
async let left = step("A")
async let right = step("B")
```
The value is not there yet, so you cannot use the binding directly: you must `await` it at the point where you finally need it. One `await` in front of the expression covers every `async let` inside it:
```swift
let both = await left + right
```
If each call takes one second, the sequential version needs two seconds while the `async let` version needs about one, because the two calls overlap.

---

When you need the results separately, collect several `async let` bindings into a tuple and `await` the whole tuple at once:
```swift
async let city = fetchCity()
async let country = fetchCountry()
let (a, b) = await (city, country)
```
Both calls were already running; the single `await` waits until the slower of the two is finished. Remember that `async let` only starts the work: an `async let` you never await is cancelled and implicitly awaited when the scope ends.

---

`async let` is tied to the scope where it is written. To start concurrent work and keep a handle on it, use a **`Task`**. The closure passed to `Task { }` runs on its own, and the task can be stored, passed around or returned:
```swift
let job = Task {
    return await double(21)
}
```
The result is read later with **`.value`**, which is awaited:
```swift
print(await job.value)
// prints 42
```
The type of the handle says what it produces and what it can throw: `Task<Int, Never>` is a task that returns an `Int` and never throws. Unlike `async let`, a `Task` can be created from ordinary, non-asynchronous code.

---

`Task.sleep` pauses the current task for a while without blocking anything else. It can be interrupted, so it is a throwing asynchronous call and needs `try await`. The duration is given with helpers such as `.seconds`, `.milliseconds` or `.nanoseconds`:
```swift
func slowGreeting() async throws -> String {
    try await Task.sleep(for: .milliseconds(50))
    return "hello"
}
```
This is the standard way to simulate slow work in an example, instead of a real network call. Note that it does not freeze the program: while one task sleeps, the others keep running.

---

Now the difference between sequential and concurrent is measurable. Suppose `work` sleeps one second before returning:
```swift
func work(_ n: Int) async -> Int {
    try? await Task.sleep(for: .seconds(1))
    return n
}
```
Awaiting the calls one by one takes about **two** seconds, because the second sleep only starts when the first is over:
```swift
let a = await work(1)
let b = await work(2)
```
Starting them with `async let` takes about **one** second, because both sleeps overlap:
```swift
async let a = work(1)
async let b = work(2)
let sum = await a + b
```
Writing `await work(1) + await work(2)` on a single line changes nothing: the two calls are still evaluated one after the other. Concurrency comes from `async let` or from tasks, never from how the line is formatted.

---

`async let` works when you know how many calls there are while writing the code. For a list whose size is only known at run time, use a **task group**.

`withTaskGroup(of:)` opens a group, `addTask` starts one child task per item, and the group is then read with `for await`, which delivers the results as they finish:
```swift
let total = await withTaskGroup(of: Int.self) { group in
    for n in numbers {
        group.addTask {
            return await square(n)
        }
    }
    var sum = 0
    for await value in group {
        sum += value
    }
    return sum
}
```
`of: Int.self` declares what every child task returns. The whole `withTaskGroup` call is one expression, so it needs a single `await` in front of it, and it does not return until every child task is done.

---

A task group hands you results in **completion order**, not in the order the tasks were added. The fastest child task arrives first, so collecting values into an array gives an unpredictable order.

When the order matters there are two fixes. If the values can simply be reordered, sort them at the end:
```swift
return values.sorted()
```
If each result belongs to a position, let every task return a pair `(index, value)` and write it into a prepared array:
```swift
for (index, word) in words.enumerated() {
    group.addTask {
        return (index, await lengthOf(word))
    }
}
var result = Array(repeating: 0, count: words.count)
for await (index, value) in group {
    result[index] = value
}
```
A sum, a maximum or a count needs neither fix, because the order of the values does not change the answer.
