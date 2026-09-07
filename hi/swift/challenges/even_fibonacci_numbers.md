---
language: swift
exerciseType: 1
difficulty: 1
title: सम फिबोनाची संख्याएँ
---

# --description--

फिबोनाची श्रृंखला में प्रत्येक नया पद पिछले दो पदों को जोड़कर बनाया जाता है। 1 और 2 से शुरू करने पर पहले 10 पद इस प्रकार होंगे: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

दी गई संख्या से अधिक न होने वाले फिबोनाची श्रृंखला के पदों पर विचार करते हुए, सम मान वाले पदों का योग ज्ञात करें।

# --instructions--

एक फ़ंक्शन लिखें जो दी गई सीमा तक (सीमा सहित) सभी सम फिबोनाची संख्याओं का योग लौटाए।

फ़ंक्शन कॉल का उदाहरण:
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

8 तक की सम फिबोनाची संख्याओं का योग 10 होना चाहिए

```swift
tryCatch(fibonacciEvenSum(8) == 10)
```

10 तक की सम फिबोनाची संख्याओं का योग 10 होना चाहिए

```swift
tryCatch(fibonacciEvenSum(10) == 10)
```

34 तक की सम फिबोनाची संख्याओं का योग 44 होना चाहिए

```swift
tryCatch(fibonacciEvenSum(34) == 44)
```

1000 तक की सम फिबोनाची संख्याओं का योग 798 होना चाहिए

```swift
tryCatch(fibonacciEvenSum(1000) == 798)
```

4000000 तक की सम फिबोनाची संख्याओं का योग 4613732 होना चाहिए

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
