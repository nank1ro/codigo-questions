---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Chaque nouveau terme de la suite de Fibonacci est obtenu en ajoutant les deux termes précédents. En commençant par 1 et 2, les 10 premiers termes sont : 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

En considérant les termes de la suite de Fibonacci dont les valeurs ne dépassent pas le nombre donné, trouve la somme des termes de valeur paire.

# --instructions--

Écris une fonction qui retourne la somme de tous les nombres de Fibonacci pairs jusqu'à la limite donnée incluse.

Exemple d'appel de fonction :
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

La somme des nombres de Fibonacci pairs jusqu'à 8 doit être égale à 10

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

La somme des nombres de Fibonacci pairs jusqu'à 10 doit être égale à 10

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

La somme des nombres de Fibonacci pairs jusqu'à 34 doit être égale à 44

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

La somme des nombres de Fibonacci pairs jusqu'à 1000 doit être égale à 798

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

La somme des nombres de Fibonacci pairs jusqu'à 4000000 doit être égale à 4613732

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
