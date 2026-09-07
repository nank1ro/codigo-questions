---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Se elenchiamo tutti i numeri naturali inferiori a 10 che sono multipli di 3 o 5, otteniamo 3, 5, 6 e 9. La somma di questi multipli è 23.

# --instructions--

Scrivi una funzione che calcola la somma di tutti i multipli di 3 o 5 inferiori al numero dato.

Esempio di chiamata alla funzione:
```swift
print(multiplesOf3And5(10))
// prints 23
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
func multiplesOf3And5(_ number: Int) -> Int {

}
```

# --asserts--

La somma dei multipli di 3 o 5 inferiori a 10 deve essere uguale a 23

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

La somma dei multipli di 3 o 5 inferiori a 1000 deve essere uguale a 233168

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

La somma dei multipli di 3 o 5 inferiori a 6987 deve essere uguale a 11390208

```swift
tryCatch(multiplesOf3And5(6987) == 11390208)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func multiplesOf3And5(_ number: Int) -> Int {
    var sum = 0
    for i in 1..<number {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i
        }
    }
    return sum
}
```
