---
language: swift
exerciseType: 1
difficulty: 1
title: बारिश की बूंदें
---

# --description--

आपका कार्य एक संख्या को एक स्ट्रिंग में बदलना है जिसमें कुछ संभावित गुणनखंडों के अनुरूप बारिश की बूंदों की आवाज़ें हों।
एक गुणनखंड वह संख्या है जो किसी अन्य संख्या को बिना शेषफल के पूर्णतः विभाजित करती है।
यह जांचने का सबसे सरल तरीका कि कोई संख्या किसी अन्य की गुणनखंड है या नहीं, मॉड्यूलो ऑपरेशन का उपयोग करना है।
बारिश की बूंदों के नियम यह हैं कि यदि दी गई संख्या:

- 3 गुणनखंड है, तो परिणाम में 'Pling' जोड़ें।
- 5 गुणनखंड है, तो परिणाम में 'Plang' जोड़ें।
- 7 गुणनखंड है, तो परिणाम में 'Plong' जोड़ें।
- 3, 5, या 7 में से कोई भी गुणनखंड नहीं है, तो परिणाम संख्या के अंक होने चाहिए।

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

- 28 में 7 गुणनखंड है, लेकिन 3 या 5 नहीं, इसलिए परिणाम `"Plong"` होगा।
- 30 में 3 और 5 दोनों गुणनखंड हैं, लेकिन 7 नहीं, इसलिए परिणाम `"PlingPlang"` होगा।
- 34 में 3, 5, या 7 में से कोई गुणनखंड नहीं है, इसलिए परिणाम `"34"` होगा।

> संकेत: `_` (अंडरस्कोर) के साथ आर्गुमेंट लेबल हटाएं

फ़ंक्शन कॉल का उदाहरण:
```swift
print(raindrops(28))
// prints "Plong"
```

# --seed--

```swift
func raindrops() {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

1 के लिए ध्वनि "1" है

```swift
    func test1() {
        XCTAssertEqual("1", raindrops(1), "--err-t1--")
    }
```

3 के लिए ध्वनि "Pling" है

```swift
    func test3() {
        XCTAssertEqual("Pling", raindrops(3), "--err-t2--")
    }
```

5 के लिए ध्वनि "Plang" है

```swift
    func test5() {
        XCTAssertEqual("Plang", raindrops(5), "--err-t3--")
    }
```

7 के लिए ध्वनि "Plong" है

```swift
    func test7() {
        XCTAssertEqual("Plong", raindrops(7), "--err-t4--")
    }
```

6 के लिए ध्वनि "Pling" है

```swift
    func test6() {
        XCTAssertEqual("Pling", raindrops(6), "--err-t5--")
    }
```

8 के लिए ध्वनि "8" है

```swift
    func test8() {
        XCTAssertEqual("8", raindrops(8), "--err-t6--")
    }
```

9 के लिए ध्वनि "Pling" है

```swift
    func test9() {
        XCTAssertEqual("Pling", raindrops(9), "--err-t7--")
    }
```

10 के लिए ध्वनि "Plang" है

```swift
    func test10() {
        XCTAssertEqual("Plang", raindrops(10), "--err-t8--")
    }
```

14 के लिए ध्वनि "Plong" है

```swift
    func test14() {
        XCTAssertEqual("Plong", raindrops(14), "--err-t9--")
    }
```

15 के लिए ध्वनि "PlingPlang" है

```swift
    func test15() {
        XCTAssertEqual("PlingPlang", raindrops(15), "--err-t10--")
    }
```

21 के लिए ध्वनि "PlingPlong" है

```swift
    func test21() {
        XCTAssertEqual("PlingPlong", raindrops(21), "--err-t11--")
    }
```

25 के लिए ध्वनि "Plang" है

```swift
    func test25() {
        XCTAssertEqual("Plang", raindrops(25), "--err-t12--")
    }
```

27 के लिए ध्वनि "Pling" है

```swift
    func test27() {
        XCTAssertEqual("Pling", raindrops(27), "--err-t13--")
    }
```

35 के लिए ध्वनि "PlangPlong" है

```swift
    func test35() {
        XCTAssertEqual("PlangPlong", raindrops(35), "--err-t14--")
    }
```

49 के लिए ध्वनि "Plong" है

```swift
    func test49() {
        XCTAssertEqual("Plong", raindrops(49), "--err-t15--")
    }
```

52 के लिए ध्वनि "52" है

```swift
    func test52() {
        XCTAssertEqual("52", raindrops(52), "--err-t16--")
    }
```

105 के लिए ध्वनि "PlingPlangPlong" है

```swift
    func test105() {
        XCTAssertEqual("PlingPlangPlong", raindrops(105), "--err-t17--")
    }
```

3125 के लिए ध्वनि "Plang" है

```swift
    func test3125() {
        XCTAssertEqual("Plang", raindrops(3125), "--err-t18--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test3", test3),
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
            ("test9", test9),
            ("test10", test10),
            ("test14", test14),
            ("test15", test15),
            ("test21", test21),
            ("test25", test25),
            ("test27", test27),
            ("test35", test35),
            ("test49", test49),
            ("test52", test52),
            ("test105", test105),
            ("test3125", test3125),
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func raindrops(_ num: Int) -> String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


