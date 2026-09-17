In Swift an error is a **value**, not a crash. Any type can act as one by conforming to the `Error` protocol, and an enum is the usual choice because the cases name exactly what can go wrong:
```swift
enum LoginError: Error {
    case wrongPassword
}
```
A function that can fail is marked `throws`, and it reports the failure with `throw`:
```swift
func login(_ password: String) throws {
    if password != "swift" {
        throw LoginError.wrongPassword
    }
    print("welcome")
}
```
Calling such a function needs `try`, and the call has to live inside a `do` block followed by a `catch` block that says what to do when it fails:
```swift
do {
    try login("hunter2")
} catch {
    print("login failed")
}
// login failed
```
When `throw` runs, the rest of the `do` block is skipped and `catch` takes over. Nothing crashes: the program carries on after the `catch`.

---

A throwing function can still return a value. The `throws` keyword goes between the parameter list and the return arrow:
```swift
func square(_ n: Int) throws -> Int {
    if n < 0 {
        throw SquareError.negative
    }
    return n * n
}
```
Reading it out loud: *square takes an `Int`, may throw, and returns an `Int`*.

At the call site the value only exists when nothing was thrown, so the assignment lives inside the `do` block:
```swift
do {
    let result = try square(4)
    print(result) // 16
} catch {
    print("failed")
}
```
The `try` is not optional decoration: the compiler refuses the call without it, so a reader always sees which lines can fail.

---

A bare `catch` handles every error the same way. Most of the time you want to react to one particular failure, so a `catch` can carry a **pattern**: the case it is willing to handle.
```swift
do {
    try check("")
} catch ValidationError.empty {
    print("the text is empty")
} catch {
    print("something else")
}
```
Swift tries the `catch` clauses from top to bottom and runs the first one whose pattern matches.

The last `catch` has no pattern on purpose. A patterned `catch` only covers the case it names, and Swift insists that every error is handled somewhere, so a `do` block that lists patterns needs a final pattern-less `catch` to sweep up the rest.

---

Order matters. Swift compares the thrown value with each `catch` pattern in the order they are written and stops at the first match, so a pattern-less `catch` placed first would swallow everything below it. Keep the specific cases at the top and the catch-all at the bottom.

An error that matches none of the patterns is not ignored: it lands in the final pattern-less `catch`.

---

An error case can carry data. Give the case **associated values** and the `throw` fills them in, so the handler learns not only *what* failed but *by how much*:
```swift
enum ValidationError: Error {
    case tooShort(minimum: Int)
}

throw ValidationError.tooShort(minimum: 8)
```
The matching `catch` binds those values with `let`:
```swift
} catch ValidationError.tooShort(let minimum) {
    print("needs at least \(minimum) characters")
}
```
The name after `let` is yours to choose; it is a new constant available inside that `catch` block only. This is how an error carries a useful message without you having to paste numbers into strings at the point where the failure happens.

---

One enum usually holds every way a single job can fail, one case per reason:
```swift
enum FormError: Error {
    case empty
    case tooLong
}
```
Writing one `catch` per case gets repetitive. Instead, catch the whole type at once and `switch` over the value:
```swift
} catch let error as FormError {
    switch error {
    case .empty: print("empty")
    case .tooLong: print("too long")
    }
} catch {
    print("unknown")
}
```
`catch let error as FormError` means *catch anything that is a `FormError`, and call it `error`*. Inside the block `error` has the enum type, so `switch` sees the cases and checks that you covered them all. The final pattern-less `catch` is still required, because some other type of error could reach this `do` block.

---

A validator reads best when the rejections come first and the real work is left unindented at the bottom. `guard` is built for that: it states the condition that must hold, and its `else` block runs when it does not.
```swift
func priceFor(_ quantity: Int) throws -> Int {
    guard quantity > 0 else {
        throw OrderError.notPositive
    }
    return quantity * 3
}
```
The `else` block of a `guard` has to leave the current scope, and `throw` is one of the ways to do that, next to `return`, `break` and `continue`. Several `guard`s stacked at the top of a function read like a list of the rules the input has to satisfy.

---

Sometimes you do not care *why* something failed, only that it did. `try?` turns a throwing call into an **optional**: the value when it succeeds, `nil` when it throws.
```swift
enum ParseError: Error {
    case notANumber
}

func toInt(_ text: String) throws -> Int {
    guard let value = Int(text) else {
        throw ParseError.notANumber
    }
    return value
}

if let number = try? toInt("42") {
    print(number) // 42
}
```
No `do`, no `catch`: the failure is folded into the optional you already know how to unwrap. The price is that the error value is thrown away, so reach for `try?` only when there is genuinely nothing to report.

---

Because `try?` produces an optional, the nil-coalescing operator `??` finishes the job by supplying a fallback:
```swift
let port = (try? readPort(text)) ?? 8080
```
The parentheses matter. `try?` would otherwise try to cover the whole expression including the `??`, and the compiler asks you to be explicit about where the failing call ends.

Read the line as one sentence: *use the port we managed to read, otherwise 8080*. Two lines of `do`/`catch` collapse into one when the recovery really is just a default value.

---

There is a third form: `try!`. It tells the compiler *this call cannot fail*, so no `do`, no `catch` and no optional. If it does fail anyway, the program stops immediately.
```swift
let pattern = try! Regex("[0-9]+")
```
That is the shape where `try!` is defensible: the argument is a literal written by you, in your own source, and if it is wrong the program is broken and should stop during your first test run.

Anything that arrives at runtime — a line typed by a user, a file, a network response — can be wrong in ways you cannot see while writing the code, and `try!` on it turns a recoverable failure into a crash in front of the user. Use `do`/`catch` or `try?` there.

---

When a function throws, everything after the `throw` is skipped — including the line that was supposed to close the file or release the lock. `defer` solves that: it registers a block now and runs it when the current scope ends, whichever way it ends.
```swift
func load() throws {
    print("open")
    defer { print("close") }
    throw FileError.missing
}
```
The call prints `open`, then `close`, and only then does the error travel on to the caller. Had the function returned normally, `close` would still have printed — that is the point. Put the cleanup right next to the setup and stop worrying about which exit the code takes.

---

A scope can register more than one `defer`. They run in **reverse** order: the last one registered is the first one to run.

That is not an arbitrary rule. Cleanups usually undo a setup that happened in order — open the file, then lock it — and undoing has to go the other way round: unlock, then close. Reverse order makes each `defer` the mirror image of the line above it.

---

A function that takes a closure has a problem: it cannot know whether the closure it is handed will throw. Marking the function `throws` would force every caller to write `try`, even the ones passing a harmless closure. `rethrows` says *I throw only if the closure you gave me throws*:
```swift
func applyTwice(_ value: Int, _ transform: (Int) throws -> Int) rethrows -> Int {
    return try transform(transform(value))
}
```
Inside the body you still write `try`, because the call really might fail. At the call site the compiler looks at the closure you passed:
```swift
let doubled = applyTwice(3, { (n: Int) -> Int in n * 2 }) // no try needed
```
The standard library uses this everywhere — `map`, `filter` and `sorted(by:)` are all `rethrows` — which is why you never write `try` in front of an ordinary `map`.

---

A `do` block is not limited to one error type. Each step can fail in its own way, and each failure gets its own `catch`:
```swift
do {
    let text = try load(false)
    let value = try parse(text)
    print(value)
} catch NetworkError.offline {
    print("offline")
} catch ParseError.badFormat {
    print("bad format")
} catch {
    print("unknown")
}
```
The first `try` that throws ends the block, so the later steps never run — the value simply never existed. That is what makes this shape readable: the happy path stays in one straight line at the top, and every way it can go wrong is listed underneath.

---

Where the `do` block sits decides how much work a single failure costs. Put it **inside** the loop and each item gets its own attempt, so one bad value is skipped and the rest still run:
```swift
for age in [4, -1, 7] {
    do {
        print(try label(age))
    } catch {
        print("skipped")
    }
}
```
Wrapping the whole loop in one `do` instead would stop at the first error and never reach `7`. Neither is wrong — it is the difference between *one bad item* and *give up*.

---

Everything in this chapter answers one question: who deals with the failure?

A throwing function refuses to answer it. It names what went wrong — a case of an `Error` enum, carrying whatever the handler will need — and hands the decision upwards. The caller then picks a tool: `do`/`catch` to react case by case, `try?` and `??` to fall back on a default, `defer` to clean up on the way out either way.

That split is the whole point. The function that detects the problem rarely knows what should happen next, and the code that knows rarely wants to repeat the check.
