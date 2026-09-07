---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Каждый новый член последовательности Фибоначчи получается сложением двух предыдущих членов. Начиная с 1 и 2, первые 10 членов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Рассматривая члены последовательности Фибоначчи, значения которых не превышают заданного числа, найдите сумму членов с чётными значениями.

# --instructions--

Напишите функцию, которая возвращает сумму всех чётных чисел Фибоначчи до заданного предела включительно.

Пример вызова функции:
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

Сумма чётных чисел Фибоначчи до 8 должна быть равна 10

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

Сумма чётных чисел Фибоначчи до 10 должна быть равна 10

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

Сумма чётных чисел Фибоначчи до 34 должна быть равна 44

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

Сумма чётных чисел Фибоначчи до 1000 должна быть равна 798

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

Сумма чётных чисел Фибоначчи до 4000000 должна быть равна 4613732

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
