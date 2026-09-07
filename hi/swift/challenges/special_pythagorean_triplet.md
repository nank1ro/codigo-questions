---
language: swift
exerciseType: 1
difficulty: 2
title: विशेष पाइथागोरियन त्रिक
---

# --description--

एक पाइथागोरियन त्रिक तीन प्राकृत संख्याओं a < b < c का समुच्चय है, जिसके लिए a² + b² = c² होता है। ठीक एक पाइथागोरियन त्रिक मौजूद है जिसके लिए a + b + c = 1000 होता है। गुणनफल a × b × c ज्ञात करें।

# --instructions--

एक फ़ंक्शन लिखें जो उस पाइथागोरियन त्रिक का गुणनफल a × b × c ज्ञात करे जहाँ a + b + c = n हो।

फ़ंक्शन कॉल का उदाहरण:
```swift
print(specialPythagoreanTriplet(12))
// prints 60
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
func specialPythagoreanTriplet(_ n: Int) -> Int {

}
```

# --asserts--

a + b + c = 12 वाले पाइथागोरियन त्रिक का गुणनफल 60 होना चाहिए

```swift
tryCatch(specialPythagoreanTriplet(12) == 60)
```

a + b + c = 1000 वाले पाइथागोरियन त्रिक का गुणनफल 31875000 होना चाहिए

```swift
tryCatch(specialPythagoreanTriplet(1000) == 31875000)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func specialPythagoreanTriplet(_ n: Int) -> Int {
    for a in 1..<n {
        for b in (a + 1)..<n {
            let c = n - a - b
            if c > b && a * a + b * b == c * c {
                return a * b * c
            }
        }
    }
    return -1
}
```
