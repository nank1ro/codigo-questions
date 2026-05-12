---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

एक फ़ंक्शन बनाएं जो एक संख्या को आर्गुमेंट के रूप में लेता है और `"Fizz"`, `"Buzz"` या `"FizzBuzz"` लौटाता है।

# --instructions--

- यदि संख्या `3` का गुणज है तो आउटपुट `"Fizz"` होना चाहिए
- यदि दी गई संख्या `5` का गुणज है, तो आउटपुट `"Buzz"` होना चाहिए।
- यदि दी गई संख्या `3` और `5` दोनों का गुणज है, तो आउटपुट `"FizzBuzz"` होना चाहिए।
- यदि संख्या `3` या `5` में से किसी का भी गुणज नहीं है, तो संख्या को स्वयं आउटपुट किया जाना चाहिए जैसा कि नीचे दिए गए उदाहरणों में दिखाया गया है।
- आउटपुट हमेशा एक स्ट्रिंग होना चाहिए, भले ही वह `3` या `5` का गुणज न हो।

उदाहरण:
```swift
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
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
func fizzBuzz() {
    
}
```

# --asserts--

संख्या `3` का परिणाम `"Fizz"` होना चाहिए

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

संख्या `5` का परिणाम `"Buzz"` होना चाहिए

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

संख्या `15` का परिणाम `"FizzBuzz"` होना चाहिए

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

संख्या `10` का परिणाम `"Buzz"` होना चाहिए

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

संख्या `98` का परिणाम `"98"` होना चाहिए

```swift
tryCatch(fizzBuzz(98) == "98")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func fizzBuzz(_ number: Int) -> String {
    if number % 3 == 0 && number % 5 == 0 {
        return "FizzBuzz"
    }
    if number % 3 == 0 {
        return "Fizz"
    }
    if number % 5 == 0 {
        return "Buzz"
    }
    return String(number)
}
```
