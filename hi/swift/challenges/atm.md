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

# --seed--

```swift
func accountBalance() -> Double {
    return
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

एक सफल लेनदेन करें

```swift
    func testSuccessfulTransaction() {
        let expected: Double = 69.50
        XCTAssertEqual(accountBalance(50, 120.00), expected, "--err-t1--")
    }
```

अपर्याप्त धनराशि

```swift
    func testInsufficientFunds() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(200, 120.00), expected, "--err-t2--")
    }
```

अस्वीकृत लेनदेन, अमान्य राशि

```swift
    func testNotMultipleOf5() {
        let expected: Double = 120.00
        XCTAssertEqual(accountBalance(22, 120.00), expected, "--err-t3--")
    }
```

सारा पैसा सफलतापूर्वक निकालें

```swift
    func testWithdrawAll() {
        let expected: Double = 0.00
        XCTAssertEqual(accountBalance(95, 95.50), expected, "--err-t4--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("testSuccessfulTransaction", testSuccessfulTransaction),
            ("testInsufficientFunds", testInsufficientFunds),
            ("testNotMultipleOf5", testNotMultipleOf5),
            ("testWithdrawAll", testWithdrawAll),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
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
