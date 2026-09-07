---
language: swift
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Una terna pitagorica è un insieme di tre numeri naturali, a < b < c, per i quali a² + b² = c². Esiste esattamente una terna pitagorica per la quale a + b + c = 1000. Trova il prodotto a × b × c.

# --instructions--

Scrivi una funzione che trova il prodotto a × b × c della terna pitagorica dove a + b + c = n.

Esempio di chiamata alla funzione:
```swift
print(specialPythagoreanTriplet(12))
// prints 60
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
func specialPythagoreanTriplet(_ n: Int) -> Int {

}
```

# --asserts--

Il prodotto della terna pitagorica con a + b + c = 12 deve essere uguale a 60

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

Il prodotto della terna pitagorica con a + b + c = 1000 deve essere uguale a 31875000

```swift
tryCatch(specialPythagoreanTriplet(1000) == 31875000)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {
    for a in 1..<n {
        for b in (a + 1)..<n {
            let c = n - a - b
            if c > b && a * a + b * b == c * c {
                return a * b * c
            }
        }
    }
    return -1
}
```
