---
language: swift
exerciseType: 1
difficulty: 1
title: Функция Аккермана
---

# --description--

Функция Аккермана — это классический пример рекурсивной функции, примечательной тем, что она не является примитивно рекурсивной. Она очень быстро растёт в значении, как и размер её дерева вызовов.

Функция Аккермана обычно определяется следующим образом:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Её аргументы никогда не бывают отрицательными, и она всегда завершается

# --instructions--

Напишите функцию, которая возвращает значение функции Аккермана.

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
func ack(_ m: Int, _ n: Int) -> Int {
    
}
```

# --asserts--

`ack(0, 0)` должен вернуть 1.

```swift
tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` должен вернуть 3.

```swift
tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` должен вернуть 13.

```swift
tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` должен вернуть 61.

```swift
tryCatch(ack(3, 3) == 61)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func ack(_ m: Int, _ n: Int) -> Int {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
