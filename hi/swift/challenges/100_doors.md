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
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --asserts--

100 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    tryCatch(getFinalOpenedDoors(100) == solution)
}
```

10 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```swift
do {
    let solution = [1, 4, 9]
    tryCatch(getFinalOpenedDoors(10) == solution)
}
```

950 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
    tryCatch(getFinalOpenedDoors(950) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
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
