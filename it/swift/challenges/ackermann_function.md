---
language: swift
exerciseType: 1
difficulty: 1
title: Funzione di Ackermann
---

# --description--

La funzione Ackermann è un classico esempio di funzione ricorsiva, nota soprattutto perché non è una funzione ricorsiva primitiva. Cresce molto rapidamente in valore, così come la dimensione delle chiamate.

La funzione Ackermann è solitamente definita come segue:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

La funzione termina sempre e i suoi argomenti non sono mai negativi

# --instructions--

Scrivi una funzione che restituisca il valore della funzione Ackermann.

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

`ack(0, 0)` deve restituire 1.

```swift
tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` deve restituire 3.

```swift
tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` deve restituire 13.

```swift
tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` deve restituire 61.

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
