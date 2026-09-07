---
language: swift
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

斐波那契数列中的每个新项都是由前两项相加得到的。从 1 和 2 开始，前 10 项为：1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

考虑斐波那契数列中值不超过给定数字的项，求其中偶数项的总和。

# --instructions--

编写一个函数，返回所有不超过给定上限的偶数斐波那契数之和（包含上限）。

函数调用示例：
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

不超过 8 的偶数斐波那契数之和必须等于 10

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

不超过 10 的偶数斐波那契数之和必须等于 10

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

不超过 34 的偶数斐波那契数之和必须等于 44

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

不超过 1000 的偶数斐波那契数之和必须等于 798

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

不超过 4000000 的偶数斐波那契数之和必须等于 4613732

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
