---
language: swift
exerciseType: 1
difficulty: 1
title: Números de Fibonacci pares
---

# --description--

Cada novo termo na sequência de Fibonacci é gerado somando os dois termos anteriores. Começando com 1 e 2, os primeiros 10 termos serão: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Considerando os termos da sequência de Fibonacci cujos valores não excedem o número dado, encontre a soma dos termos de valor par.

# --instructions--

Escreva uma função que retorne a soma de todos os números de Fibonacci de valor par até e incluindo o limite dado.

Exemplo de chamada da função:
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

A soma dos números de Fibonacci pares até 8 deve ser igual a 10

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

A soma dos números de Fibonacci pares até 10 deve ser igual a 10

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

A soma dos números de Fibonacci pares até 34 deve ser igual a 44

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

A soma dos números de Fibonacci pares até 1000 deve ser igual a 798

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

A soma dos números de Fibonacci pares até 4000000 deve ser igual a 4613732

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
