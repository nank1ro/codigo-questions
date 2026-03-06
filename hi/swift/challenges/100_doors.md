---
language: swift
exerciseType: 1
difficulty: 1
title: 100 दरवाज़े
---

# --description--

एक कतार में 100 दरवाज़े हैं जो शुरू में सभी बंद हैं।
आप दरवाज़ों से 100 बार गुज़रते हैं।
पहली बार, हर दरवाज़े पर जाएं और दरवाज़े को 'टॉगल' करें (यदि दरवाज़ा बंद है, तो खोलें; यदि खुला है, तो बंद करें)।
दूसरी बार, केवल हर दूसरे दरवाज़े पर जाएं (यानी, दरवाज़ा #2, #4, #6, ...) और उसे टॉगल करें।
तीसरी बार, हर तीसरे दरवाज़े पर जाएं (यानी, दरवाज़ा #3, #6, #9, ...), आदि, जब तक आप केवल 100वें दरवाज़े पर न जाएं।

# --instructions--

अंतिम पास के बाद दरवाज़ों की स्थिति निर्धारित करने के लिए एक फ़ंक्शन लागू करें।
अंतिम परिणाम एक ऐरे में लौटाएं, जिसमें केवल उस दरवाज़े का नंबर शामिल हो जो खुला है।
> विधि को दरवाज़ों की परिवर्तनीय संख्या के साथ काम करने में सक्षम होना चाहिए।

# --seed--

```swift
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

100 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```swift
    func test1() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        XCTAssertEqual(getFinalOpenedDoors(100), solution, "--err-t1--")
    }
```

10 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```swift
    func test2() {
        let solution = [1, 4, 9]
        XCTAssertEqual(getFinalOpenedDoors(16), solution, "--err-t2--")
    }
```

950 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```swift
    func test3() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        XCTAssertEqual(getFinalOpenedDoors(950), solution, "--err-t3--")
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
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func square(_ num: Int) -> Int {
    return Int(pow(Double(num), Double(2)))
}

func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    var openDoors: [Int] = []
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.append(square(i))
        i += 1
    }
    return openDoors
}
```
