---
language: swift
exerciseType: 1
difficulty: 2
title: अभाज्य संख्याओं का योग
---

# --description--

10 से कम अभाज्य संख्याओं का योग 2 + 3 + 5 + 7 = 17 है।

# --instructions--

एक फ़ंक्शन लिखें जो दी गई संख्या से कम सभी अभाज्य संख्याओं का योग ज्ञात करे।

फ़ंक्शन कॉल का उदाहरण:
```swift
print(primeSummation(10))
// prints 17
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
func primeSummation(_ n: Int) -> Int {

}
```

# --asserts--

10 से कम सभी अभाज्य संख्याओं का योग 17 होना चाहिए

```swift
tryCatch(primeSummation(10) == 17)
```

1000 से कम सभी अभाज्य संख्याओं का योग 76127 होना चाहिए

```swift
tryCatch(primeSummation(1000) == 76127)
```

100000 से कम सभी अभाज्य संख्याओं का योग 454396537 होना चाहिए

```swift
tryCatch(primeSummation(100000) == 454396537)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func primeSummation(_ n: Int) -> Int {
    var sieve = [Bool](repeating: true, count: n)
    if n > 0 { sieve[0] = false }
    if n > 1 { sieve[1] = false }
    var i = 2
    while i * i < n {
        if sieve[i] {
            var j = i * i
            while j < n {
                sieve[j] = false
                j += i
            }
        }
        i += 1
    }
    return sieve.indices.filter { sieve[$0] }.reduce(0, +)
}
```
