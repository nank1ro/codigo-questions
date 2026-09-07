---
language: swift
exerciseType: 1
difficulty: 2
title: सबसे बड़ा पैलिंड्रोम गुणनफल
---

# --description--

एक पैलिंड्रोम संख्या दोनों दिशाओं से समान पढ़ी जाती है। दो 2-अंकीय संख्याओं के गुणनफल से बनने वाला सबसे बड़ा पैलिंड्रोम 9009 = 91 × 99 है।

# --instructions--

एक फ़ंक्शन लिखें जो दो n-अंकीय संख्याओं के गुणनफल से बनने वाला सबसे बड़ा पैलिंड्रोम ज्ञात करे।

फ़ंक्शन कॉल का उदाहरण:
```swift
print(largestPalindromeProduct(2))
// prints 9009
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
func largestPalindromeProduct(_ n: Int) -> Int {

}
```

# --asserts--

दो 2-अंकीय संख्याओं का सबसे बड़ा पैलिंड्रोम गुणनफल 9009 होना चाहिए

```swift
tryCatch(largestPalindromeProduct(2) == 9009)
```

दो 3-अंकीय संख्याओं का सबसे बड़ा पैलिंड्रोम गुणनफल 906609 होना चाहिए

```swift
tryCatch(largestPalindromeProduct(3) == 906609)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func largestPalindromeProduct(_ n: Int) -> Int {
    func isPalindrome(_ num: Int) -> Bool {
        let s = String(num)
        return s == String(s.reversed())
    }
    let upper = Int(pow(10.0, Double(n))) - 1
    let lower = Int(pow(10.0, Double(n - 1)))
    var largest = 0
    for i in stride(from: upper, through: lower, by: -1) {
        if i * upper < largest { break }
        for j in stride(from: i, through: lower, by: -1) {
            let product = i * j
            if product < largest { break }
            if isPalindrome(product) {
                largest = product
            }
        }
    }
    return largest
}
```
