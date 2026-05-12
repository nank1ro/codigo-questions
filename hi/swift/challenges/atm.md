---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

जेम्स ATM से N डॉलर निकालना चाहता है।
कैश मशीन लेनदेन तभी स्वीकार करेगी जब N 5 का गुणज हो, और जेम्स के खाते में निकासी लेनदेन करने के लिए पर्याप्त नकदी हो (बैंक शुल्क सहित)।
प्रत्येक सफल निकासी के लिए बैंक `0.50$` शुल्क लेता है।
एक प्रयास किए गए लेनदेन के बाद जेम्स के खाते की शेष राशि की गणना करें।
इनपुट निम्नलिखित क्रम में हैं:
1. जेम्स जितनी नकदी निकालना चाहता है वह निम्नलिखित सीमा में है: `0 < N <= 2000`।
2. जेम्स की प्रारंभिक शेष राशि दो अंकों की सटीकता के साथ दी गई है और निम्नलिखित सीमा में है: `0 < B <= 2000`।

# --instructions--

प्रयास किए गए लेनदेन के बाद खाते की शेष राशि लौटाएं, जो दो अंकों की सटीकता वाली संख्या के रूप में दी गई हो।
यदि खाते में लेनदेन पूरा करने के लिए पर्याप्त धन नहीं है, तो वर्तमान बैंक शेष राशि लौटाएं।

> संकेत: `_` (अंडरस्कोर) के साथ आर्गुमेंट लेबल हटाएं

फ़ंक्शन कॉल का उदाहरण:
```swift
print(accountBalance(10, 20))
// prints 9,5
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
func accountBalance() -> Double {
    return
}
```

# --asserts--

एक सफल लेनदेन करें

```swift
do {
    let expected: Double = 69.50
    tryCatch(accountBalance(50, 120.00) == expected)
}
```

अपर्याप्त धनराशि

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(200, 120.00) == expected)
}
```

अस्वीकृत लेनदेन, अमान्य राशि

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(22, 120.00) == expected)
}
```

सारा पैसा सफलतापूर्वक निकालें

```swift
do {
    let expected: Double = 0.00
    tryCatch(accountBalance(95, 95.50) == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func accountBalance(_ withdraw: Double,_ balance: Double) -> Double {
    let isMultipleOf5 = withdraw.truncatingRemainder(dividingBy: 5) == 0;
    let isAmountAvailable = balance >= (withdraw + 0.50)
    if isMultipleOf5 && isAmountAvailable {
        return balance - withdraw - 0.50
    }
    return balance
}
```
