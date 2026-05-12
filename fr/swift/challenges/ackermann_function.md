---
language: swift
exerciseType: 1
difficulty: 1
title: Fonction d'Ackermann
---

# --description--

The Fonction d'Ackermann is a classic example of a recursive function, notable especially because it is not a primitive recursive function. It grows very quickly in value, as does the size of its call tree.

The Fonction d'Ackermann is usually defined as follows:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Ses arguments ne sont jamais négatifs et elle se termine toujours

# --instructions--

Write a function which returns the value of the Fonction d'Ackermann.

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
func ack(_ m: Int, _ n: Int) -> Int {
    
}
```

# --asserts--

`ack(0, 0)` doit retourner 1.

```swift
tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` doit retourner 3.

```swift
tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` doit retourner 13.

```swift
tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` doit retourner 61.

```swift
tryCatch(ack(3, 3) == 61)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
