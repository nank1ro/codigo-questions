---
language: swift
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

Wenn wir alle natürlichen Zahlen unter 10 auflisten, die Vielfache von 3 oder 5 sind, erhalten wir 3, 5, 6 und 9. Die Summe dieser Vielfachen beträgt 23.

# --instructions--

Schreibe eine Funktion, die die Summe aller Vielfachen von 3 oder 5 unterhalb der gegebenen Zahl berechnet.

Beispiel eines Funktionsaufrufs:
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

Die Summe der Vielfachen von 3 oder 5 unter 10 muss 23 ergeben

```swift
tryCatch(multiplesOf3And5(10) == 23)
```

Die Summe der Vielfachen von 3 oder 5 unter 1000 muss 233168 ergeben

```swift
tryCatch(multiplesOf3And5(1000) == 233168)
```

Die Summe der Vielfachen von 3 oder 5 unter 6987 muss 11390208 ergeben

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
