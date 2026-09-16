---
language: swift
exerciseType: 1
difficulty: 1
title: हैमिंग दूरी
---

# --description--

DNA को न्यूक्लियोटाइडों के स्ट्रैंड के रूप में लिखा जाता है, जिनमें से प्रत्येक एक अक्षर होता है: `A`, `C`, `G` या `T`। जब समान लंबाई के दो स्ट्रैंड साथ-साथ पंक्तिबद्ध किए जाते हैं, तो कुछ स्थानों पर एक ही न्यूक्लियोटाइड होता है और कुछ स्थानों पर अलग-अलग।

जिन स्थानों पर दोनों स्ट्रैंड भिन्न होते हैं, उनकी संख्या हैमिंग दूरी कहलाती है, और जीववैज्ञानिक इसका उपयोग यह मापने के लिए करते हैं कि दो स्ट्रैंड कितनी दूर अलग हो गए हैं। `GAGCCTACTAACGGGAT` को `CATCGTAATGACGGCCT` के साथ पंक्तिबद्ध करने पर 7 स्थान भिन्न मिलते हैं, इसलिए उनकी हैमिंग दूरी 7 होती है।

# --instructions--

`hammingDistance` नाम का एक फ़ंक्शन लिखें जो समान लंबाई के दो DNA स्ट्रैंड लेता है और उन स्थानों की संख्या लौटाता है जहाँ वे भिन्न होते हैं।

उदाहरण:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- दोनों स्ट्रैंड हमेशा समान लंबाई के होते हैं, इसलिए आपको कभी अलग-अलग लंबाई वाले स्ट्रैंड संभालने की ज़रूरत नहीं है।
- दो खाली स्ट्रैंड कहीं भिन्न नहीं होते, इसलिए उनकी दूरी 0 होती है।

> संकेत: `_` (अंडरस्कोर) का उपयोग करके आर्ग्युमेंट लेबल छोड़ दें

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
func hammingDistance(_ left: String, _ right: String) -> Int {
    
}
```

# --asserts--

दो खाली स्ट्रैंड कहीं भिन्न नहीं होते

```swift
tryCatch(hammingDistance("", "") == 0)
```

दो समान एकल-न्यूक्लियोटाइड स्ट्रैंड में कोई अंतर नहीं होता

```swift
tryCatch(hammingDistance("A", "A") == 0)
```

दो भिन्न एकल-न्यूक्लियोटाइड स्ट्रैंड एक स्थान पर भिन्न होते हैं

```swift
tryCatch(hammingDistance("A", "G") == 1)
```

दो छोटे स्ट्रैंड जो हर स्थान पर भिन्न होते हैं

```swift
tryCatch(hammingDistance("AG", "CT") == 2)
```

दो छोटे स्ट्रैंड जो केवल पहले स्थान पर भिन्न होते हैं

```swift
tryCatch(hammingDistance("AT", "CT") == 1)
```

स्ट्रैंडों के बीच में एक भिन्न न्यूक्लियोटाइड

```swift
tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

अलग-अलग स्थानों पर समान न्यूक्लियोटाइड भी अंतर में गिने जाते हैं

```swift
tryCatch(hammingDistance("TAG", "GAT") == 2)
```

चार अंतरों वाले स्ट्रैंडों का एक लंबा जोड़ा

```swift
tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

एक स्ट्रैंड को एक स्थान खिसकाने पर लगभग हर स्थान भिन्न हो जाता है

```swift
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

विवरण वाले दोनों स्ट्रैंड की दूरी सात है

```swift
tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func hammingDistance(_ left: String, _ right: String) -> Int {
    var distance = 0

    for (leftNucleotide, rightNucleotide) in zip(left, right) {
        if leftNucleotide != rightNucleotide {
            distance += 1
        }
    }

    return distance
}
```
