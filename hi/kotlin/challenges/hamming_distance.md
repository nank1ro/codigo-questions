---
language: kotlin
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

# --seed--

```kotlin
fun hammingDistance(left: String, right: String): Int {
    
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

दो खाली स्ट्रैंड कहीं भिन्न नहीं होते

```kotlin
    tryCatch(hammingDistance("", "") == 0)
```

दो समान एकल-न्यूक्लियोटाइड स्ट्रैंड में कोई अंतर नहीं होता

```kotlin
    tryCatch(hammingDistance("A", "A") == 0)
```

दो भिन्न एकल-न्यूक्लियोटाइड स्ट्रैंड एक स्थान पर भिन्न होते हैं

```kotlin
    tryCatch(hammingDistance("A", "G") == 1)
```

दो छोटे स्ट्रैंड जो हर स्थान पर भिन्न होते हैं

```kotlin
    tryCatch(hammingDistance("AG", "CT") == 2)
```

दो छोटे स्ट्रैंड जो केवल पहले स्थान पर भिन्न होते हैं

```kotlin
    tryCatch(hammingDistance("AT", "CT") == 1)
```

स्ट्रैंडों के बीच में एक भिन्न न्यूक्लियोटाइड

```kotlin
    tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

अलग-अलग स्थानों पर समान न्यूक्लियोटाइड भी अंतर में गिने जाते हैं

```kotlin
    tryCatch(hammingDistance("TAG", "GAT") == 2)
```

चार अंतरों वाले स्ट्रैंडों का एक लंबा जोड़ा

```kotlin
    tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

एक स्ट्रैंड को एक स्थान खिसकाने पर लगभग हर स्थान भिन्न हो जाता है

```kotlin
    tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

विवरण वाले दोनों स्ट्रैंड की दूरी सात है

```kotlin
    tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun hammingDistance(left: String, right: String): Int {
    var distance = 0

    for (i in left.indices) {
        if (left[i] != right[i]) {
            distance++
        }
    }

    return distance
}
```
