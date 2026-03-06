---
language: swift
exerciseType: 1
difficulty: 3
title: लीप वर्ष
---

# --description--

एक कैलेंडर वर्ष में ठीक 365.25 दिन होते हैं। लेकिन, अंततः, यह भ्रम पैदा करेगा क्योंकि मनुष्य सामान्यतः 1 की सटीक विभाज्यता से गिनते हैं, दशमलव बिंदुओं से नहीं। इसलिए, इससे बचने के लिए, हर चार वर्ष के चक्र में सभी 0.25 दिनों को जोड़कर उस वर्ष को 366 दिन (29 फरवरी को एक अतिरिक्त दिन के रूप में शामिल करते हुए) देने और इसे __लीप वर्ष__ कहने का निर्णय लिया गया। चार वर्ष के चक्र में अन्य तीन वर्षों में केवल 365 दिन होंगे और वे __लीप वर्ष नहीं होंगे__।

# --instructions--

इस चुनौती में हम इसे एक नए स्तर पर ले जाएंगे, जहां आपको `Date` क्लास, `switch` स्टेटमेंट, __if ब्लॉक__, __if-else ब्लॉक__ या __टर्नरी ऑपरेशन__ (`x ? a : b`) और न ही लॉजिकल ऑपरेटर __AND__ (`&&`) और __OR__ (`||`) के उपयोग के बिना यह निर्धारित करना है कि यह लीप वर्ष है या नहीं, __NOT__ (`!`) ऑपरेटर को छोड़कर।

यदि लीप वर्ष है तो `true` लौटाएं, अन्यथा `false`।

फ़ंक्शन कॉल का उदाहरण:
```swift
print(leapYear(2000))
// prints true
```

# --seed--

```swift
func leapYear(_ year: Int) -> Bool {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

`Date`, `switch`, `if`, `else`, `&&`, `||` या `?` का उपयोग अनुमत नहीं है।

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

वर्ष `2016` एक लीप वर्ष है।

```swift
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

वर्ष `1996` एक लीप वर्ष है।

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

वर्ष `1600` एक लीप वर्ष है।

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

वर्ष `2020` एक लीप वर्ष है।

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

वर्ष `2000` एक लीप वर्ष है।

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

वर्ष `2008` एक लीप वर्ष है।

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

वर्ष `1521` लीप वर्ष नहीं है।

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

वर्ष `1800` लीप वर्ष नहीं है।

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

वर्ष `2007` लीप वर्ष नहीं है।

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

वर्ष `2002` लीप वर्ष नहीं है।

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

वर्ष `1979` लीप वर्ष नहीं है।

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

वर्ष `2006` लीप वर्ष नहीं है।

```swift
    func test12() {
        XCTAssertEqual(leapYear(2006), false, "--err-t12--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test2", test2),
            ("test3", test3),
            ("test4", test4),
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
            ("test9", test9),
            ("test10", test10),
            ("test11", test11),
            ("test12", test12), 
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func leapYear(_ year: Int) -> Bool {
    var yr = year
    while yr % 100 == 0 {
        yr = yr / 100
    }
    return yr % 4 == 0
}
```
