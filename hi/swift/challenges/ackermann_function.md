---
language: swift
exerciseType: 1
difficulty: 1
title: एकरमन फलन
---

# --description--

एकरमन फलन एक पुनरावर्ती फलन (recursive function) का एक उत्कृष्ट उदाहरण है, जो विशेष रूप से इसलिए उल्लेखनीय है क्योंकि यह एक आदिम पुनरावर्ती फलन (primitive recursive function) नहीं है। इसका मान बहुत तेज़ी से बढ़ता है, और इसके कॉल ट्री का आकार भी।

एकरमन फलन को आमतौर पर इस प्रकार परिभाषित किया जाता है:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

इसके आर्गुमेंट कभी ऋणात्मक नहीं होते और यह हमेशा समाप्त होता है

# --instructions--

एक फ़ंक्शन लिखें जो एकरमन फलन का मान लौटाए।

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

`ack(0, 0)` को 1 लौटाना चाहिए।

```swift
tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` को 3 लौटाना चाहिए।

```swift
tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` को 13 लौटाना चाहिए।

```swift
tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` को 61 लौटाना चाहिए।

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
