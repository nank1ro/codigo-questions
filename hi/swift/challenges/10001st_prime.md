---
language: swift
exerciseType: 1
difficulty: 1
title: 10001वाँ अभाज्य
---

# --description--

पहली छह अभाज्य संख्याओं 2, 3, 5, 7, 11 और 13 को सूचीबद्ध करने पर हम देख सकते हैं कि छठी अभाज्य संख्या 13 है।

# --instructions--

एक फ़ंक्शन लिखें जो n-वाँ अभाज्य संख्या लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```swift
print(nthPrime(6))
// prints 13
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
func nthPrime(_ n: Int) -> Int {

}
```

# --asserts--

छठी अभाज्य संख्या 13 होनी चाहिए

```swift
tryCatch(nthPrime(6) == 13)
```

10वीं अभाज्य संख्या 29 होनी चाहिए

```swift
tryCatch(nthPrime(10) == 29)
```

1000वीं अभाज्य संख्या 7919 होनी चाहिए

```swift
tryCatch(nthPrime(1000) == 7919)
```

10001वीं अभाज्य संख्या 104743 होनी चाहिए

```swift
tryCatch(nthPrime(10001) == 104743)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func nthPrime(_ n: Int) -> Int {
    func isPrime(_ num: Int) -> Bool {
        if num < 2 { return false }
        if num == 2 { return true }
        if num % 2 == 0 { return false }
        var i = 3
        while i * i <= num {
            if num % i == 0 { return false }
            i += 2
        }
        return true
    }
    var count = 0
    var candidate = 1
    while count < n {
        candidate += 1
        if isPrime(candidate) {
            count += 1
        }
    }
    return candidate
}
```
