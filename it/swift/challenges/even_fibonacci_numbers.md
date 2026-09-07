---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Ogni nuovo termine della sequenza di Fibonacci viene generato sommando i due termini precedenti. Partendo da 1 e 2, i primi 10 termini sono: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Considerando i termini della sequenza di Fibonacci i cui valori non superano il numero dato, trova la somma dei termini di valore pari.

# --instructions--

Scrivi una funzione che restituisce la somma di tutti i numeri di Fibonacci pari fino al limite dato incluso.

Esempio di chiamata alla funzione:
```swift
print(fibonacciEvenSum(8))
// prints 10
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
func fibonacciEvenSum(_ n: Int) -> Int {

}
```

# --asserts--

La somma dei numeri di Fibonacci pari fino a 8 deve essere uguale a 10

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

La somma dei numeri di Fibonacci pari fino a 10 deve essere uguale a 10

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

La somma dei numeri di Fibonacci pari fino a 34 deve essere uguale a 44

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

La somma dei numeri di Fibonacci pari fino a 1000 deve essere uguale a 798

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

La somma dei numeri di Fibonacci pari fino a 4000000 deve essere uguale a 4613732

```swift
tryCatch(fibonacciEvenSum(4000000) == 4613732)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func fibonacciEvenSum(_ n: Int) -> Int {
    var sum = 0
    var a = 1
    var b = 2
    while a <= n {
        if a % 2 == 0 {
            sum += a
        }
        let temp = a + b
        a = b
        b = temp
    }
    return sum
}
```
