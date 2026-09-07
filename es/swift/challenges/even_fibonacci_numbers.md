---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Cada nuevo término de la sucesión de Fibonacci se genera sumando los dos términos anteriores. Comenzando con 1 y 2, los primeros 10 términos serán: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Considerando los términos de la sucesión de Fibonacci cuyos valores no superan el número dado, encuentra la suma de los términos de valor par.

# --instructions--

Escribe una función que devuelva la suma de todos los números de Fibonacci de valor par hasta el límite dado, inclusive.

Ejemplo de llamada a la función:
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

La suma de los números de Fibonacci pares hasta 8 debe ser igual a 10

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

La suma de los números de Fibonacci pares hasta 10 debe ser igual a 10

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

La suma de los números de Fibonacci pares hasta 34 debe ser igual a 44

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

La suma de los números de Fibonacci pares hasta 1000 debe ser igual a 798

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

La suma de los números de Fibonacci pares hasta 4000000 debe ser igual a 4613732

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
