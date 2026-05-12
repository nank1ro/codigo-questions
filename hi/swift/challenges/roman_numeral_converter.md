---
language: swift
exerciseType: 1
difficulty: 3
title: रोमन अंक परिवर्तक
---

# --description--

एक फ़ंक्शन बनाएं जो एक धनात्मक पूर्णांक को अपने पैरामीटर के रूप में लेता है और उस पूर्णांक के रोमन अंक प्रतिनिधित्व वाली एक स्ट्रिंग लौटाता है। आधुनिक रोमन अंक प्रत्येक अंक को अलग-अलग व्यक्त करके लिखे जाते हैं, सबसे बाएं अंक से शुरू करते हुए और शून्य मान वाले किसी भी अंक को छोड़ते हुए।

# --instructions--

उदाहरण:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- सभी रोमन अंक अपरकेस में लौटाए जाने चाहिए।
- इस संकेतन में प्रदर्शित की जा सकने वाली सबसे बड़ी संख्या 3,999 है।

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
func convertToRoman(_ n: Int) -> String {
    
}
```

# --asserts--

संख्या `2` का मान `II` होना चाहिए

```swift
tryCatch(convertToRoman(2) == "II")
```

संख्या `12` का मान `XII` होना चाहिए

```swift
tryCatch(convertToRoman(12) == "XII")
```

संख्या `16` का मान `XVI` होना चाहिए

```swift
tryCatch(convertToRoman(16) == "XVI")
```

संख्या `44` का मान `XLIV` होना चाहिए

```swift
tryCatch(convertToRoman(44) == "XLIV")
```

संख्या `68` का मान `LXVIII` होना चाहिए

```swift
tryCatch(convertToRoman(68) == "LXVIII")
```

संख्या `400` का मान `CD` होना चाहिए

```swift
tryCatch(convertToRoman(400) == "CD")
```

संख्या `798` का मान `DCCXCVIII` होना चाहिए

```swift
tryCatch(convertToRoman(798) == "DCCXCVIII")
```

संख्या `1000` का मान `M` होना चाहिए

```swift
tryCatch(convertToRoman(1000) == "M")
```

संख्या `3999` का मान `MMMCMXCIX` होना चाहिए

```swift
tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

संख्या `649` का मान `DCXLIX` होना चाहिए

```swift
tryCatch(convertToRoman(649) == "DCXLIX")
```

संख्या `1666` का मान `MDCLXVI` होना चाहिए

```swift
tryCatch(convertToRoman(1666) == "MDCLXVI")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func convertToRoman(_ n: Int) -> String {
  var result = ""
  var number = n
  for (value, letter) in [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
  ] {
    while number >= value {
      result += letter
      number -= value
    }
  }
  return result
}
```
