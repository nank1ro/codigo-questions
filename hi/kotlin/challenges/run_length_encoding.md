---
language: kotlin
exerciseType: 1
difficulty: 2
title: रन लंबाई एन्कोडिंग
---

# --description--

रन लंबाई एन्कोडिंग संपीड़न की सबसे पुरानी तरकीबों में से एक है: एक ही अक्षर को बार-बार लिखने के बजाय, आप लिख देते हैं कि वह अक्षर कितनी बार दोहराया गया है और फिर उस अक्षर को स्वयं लिख देते हैं।

ज़्यादातर खाली पन्ने को स्कैन करती एक फ़ैक्स मशीन को एक जैसे पिक्सेल के लंबे खिंचाव मिलते हैं, इसलिए बारह `W` की एक पंक्ति लाइन के नीचे बहुत छोटे `12W` के रूप में यात्रा करती है। जब कोई अक्षर केवल एक बार आता है तो उसे गिनने से कुछ हासिल नहीं होता, इसलिए उसे जैसा है वैसा ही अकेले कॉपी कर दिया जाता है।

# --instructions--

एक फ़ंक्शन `encodeRun` लिखें जो एक स्ट्रिंग `text` लेता है और उसका रन लंबाई एन्कोडेड रूप लौटाता है।

एक ही अक्षर के दो या दो से अधिक बार दोहराए जाने वाला हर रन उस रन की दशमलव में लिखी गई लंबाई और उसके बाद वह अक्षर बन जाता है। एक की लंबाई वाला रन केवल उस एक अक्षर के रूप में कॉपी होता है, उसके आगे कोई संख्या नहीं लिखी जाती।

उदाहरण:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- टेक्स्ट में केवल `A` से `Z` तक के अपरकेस अक्षर और रिक्त स्थान होते हैं।
- नौ से लंबा कोई रन अपनी पूरी दशमलव गिनती इस्तेमाल करता है, इसलिए बारह `W`, `12W` बन जाते हैं, कभी भी `9W3W` नहीं।
- रिक्त स्थान साधारण अक्षर हैं: उन्हें भी अक्षरों की तरह ही गिना और एन्कोड किया जाता है।
- खाली स्ट्रिंग का एन्कोडिंग खाली स्ट्रिंग ही होता है।

# --seed--

```kotlin
fun encodeRun(text: String): String {
    
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

खाली स्ट्रिंग का एन्कोडिंग खाली स्ट्रिंग ही होता है

```kotlin
    tryCatch(encodeRun("") == "")
```

एक अकेला अक्षर जैसा है वैसा ही कॉपी हो जाता है

```kotlin
    tryCatch(encodeRun("A") == "A")
```

बिना दोहराव वाली स्ट्रिंग बिना बदले आगे बढ़ जाती है

```kotlin
    tryCatch(encodeRun("ABCDE") == "ABCDE")
```

दो की लंबाई वाला रन गिनती और उसके बाद अक्षर बन जाता है

```kotlin
    tryCatch(encodeRun("AA") == "2A")
```

मिश्रित उदाहरण "AABCCCDEEEE", "2AB3CD4E" बन जाता है

```kotlin
    tryCatch(encodeRun("AABCCCDEEEE") == "2AB3CD4E")
```

बारह की लंबाई वाला रन अपनी पूरी दशमलव गिनती इस्तेमाल करता है, इसलिए परिणाम "12W" से शुरू होता है

```kotlin
    tryCatch(encodeRun("WWWWWWWWWWWWBWW") == "12WB2W")
```

रिक्त स्थानों के रन भी अक्षरों के रनों की तरह ही एन्कोड होते हैं

```kotlin
    tryCatch(encodeRun("  HI  ") == "2 HI2 ")
```

दस की लंबाई वाला रन "10A" लिखा जाता है, कभी भी दो छोटे रनों के रूप में नहीं

```kotlin
    tryCatch(encodeRun("AAAAAAAAAA") == "10A")
```

बारी-बारी से आने वाले अकेले अक्षर सभी जैसे हैं वैसे ही कॉपी होते हैं

```kotlin
    tryCatch(encodeRun("ABABAB") == "ABABAB")
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
fun encodeRun(text: String): String {
    val result = StringBuilder()
    var i = 0

    while (i < text.length) {
        var run = 1
        while (i + run < text.length && text[i + run] == text[i]) {
            run++
        }
        if (run > 1) {
            result.append(run)
        }
        result.append(text[i])
        i += run
    }

    return result.toString()
}
```
