---
language: swift
exerciseType: 1
difficulty: 1
title: Smallest multiple
---

# --description--

2520 — это наименьшее число, которое делится на каждое из чисел от 1 до 10 без остатка.

# --instructions--

Напишите функцию, которая возвращает наименьшее положительное число, равномерно делящееся на все числа от 1 до n.

Пример вызова функции:
```swift
print(smallestMultiple(10))
// prints 2520
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
func smallestMultiple(_ n: Int) -> Int {

}
```

# --asserts--

Наименьшее кратное от 1 до 5 должно быть равно 60

```swift
tryCatch(smallestMultiple(5) == 60)
```

Наименьшее кратное от 1 до 10 должно быть равно 2520

```swift
tryCatch(smallestMultiple(10) == 2520)
```

Наименьшее кратное от 1 до 20 должно быть равно 232792560

```swift
tryCatch(smallestMultiple(20) == 232792560)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func smallestMultiple(_ n: Int) -> Int {
    func gcd(_ a: Int, _ b: Int) -> Int {
        return b == 0 ? a : gcd(b, a % b)
    }
    func lcm(_ a: Int, _ b: Int) -> Int {
        return a / gcd(a, b) * b
    }
    return (1...n).reduce(1) { lcm($0, $1) }
}
```
