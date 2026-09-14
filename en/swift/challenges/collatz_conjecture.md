---
language: swift
exerciseType: 1
difficulty: 1
title: Collatz conjecture
---

# --description--

The Collatz conjecture starts from any positive integer `n` and repeats one simple rule: if `n` is even, halve it; if `n` is odd, replace it with `3n + 1`. Sooner or later the sequence reaches 1.

For example, starting from 16 the sequence is `16 -> 8 -> 4 -> 2 -> 1`, so it takes 4 steps.

Nobody has ever proved that this always happens, but it holds for every number ever tested.

# --instructions--

Write a function `collatzSteps` that takes a positive integer `n` and returns the number of steps needed to reach 1.

`collatzSteps(1)` is 0, because 1 is already the end of the sequence. `collatzSteps(12)` is 9, and `collatzSteps(27)` is 111.

Example of function call:
```swift
print(collatzSteps(16))
// prints 4
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func collatzSteps(_ n: Int) -> Int {

}
```

# --asserts--

`collatzSteps(1)` should return 0, because 1 is already the end of the sequence.

```swift
tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` should return 1.

```swift
tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` should return 8.

```swift
tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` should return 16.

```swift
tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` should return 4.

```swift
tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` should return 9.

```swift
tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` should return 111.

```swift
tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` should return 118.

```swift
tryCatch(collatzSteps(97) == 118)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func collatzSteps(_ n: Int) -> Int {
    var value = n
    var steps = 0
    while value != 1 {
        value = value % 2 == 0 ? value / 2 : 3 * value + 1
        steps += 1
    }
    return steps
}
```
