---
language: swift
exerciseType: 1
difficulty: 1
title: कोलैट्ज़ अनुमान
---

# --description--

कोलैट्ज़ अनुमान किसी भी धनात्मक पूर्णांक `n` से शुरू होकर एक ही सरल नियम दोहराता है: यदि `n` सम है, तो उसे आधा कर दें; यदि `n` विषम है, तो उसे `3n + 1` से बदल दें। कभी न कभी अनुक्रम 1 तक पहुँच जाता है।

उदाहरण के लिए, 16 से शुरू करने पर अनुक्रम `16 -> 8 -> 4 -> 2 -> 1` होता है, इसलिए इसमें 4 चरण लगते हैं।

अब तक किसी ने भी यह सिद्ध नहीं किया है कि ऐसा हमेशा होता है, लेकिन यह अब तक परीक्षण की गई हर संख्या पर लागू होता है।

# --instructions--

`collatzSteps` नाम का एक फ़ंक्शन लिखें जो एक धनात्मक पूर्णांक `n` लेता है और 1 तक पहुँचने के लिए आवश्यक चरणों की संख्या लौटाता है।

`collatzSteps(1)` का मान 0 है, क्योंकि 1 पहले से ही अनुक्रम का अंत है। `collatzSteps(12)` का मान 9 है, और `collatzSteps(27)` का मान 111 है।

फ़ंक्शन कॉल का उदाहरण:
```swift
print(collatzSteps(16))
// 4 प्रिंट करता है
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
func collatzSteps(_ n: Int) -> Int {

}
```

# --asserts--

`collatzSteps(1)` को 0 लौटाना चाहिए, क्योंकि 1 पहले से ही अनुक्रम का अंत है।

```swift
tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` को 1 लौटाना चाहिए।

```swift
tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` को 8 लौटाना चाहिए।

```swift
tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` को 16 लौटाना चाहिए।

```swift
tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` को 4 लौटाना चाहिए।

```swift
tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` को 9 लौटाना चाहिए।

```swift
tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` को 111 लौटाना चाहिए।

```swift
tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` को 118 लौटाना चाहिए।

```swift
tryCatch(collatzSteps(97) == 118)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func collatzSteps(_ n: Int) -> Int {
    var value = n
    var steps = 0
    while value != 1 {
        value = value % 2 == 0 ? value / 2 : 3 * value + 1
        steps += 1
    }
    return steps
}
```
