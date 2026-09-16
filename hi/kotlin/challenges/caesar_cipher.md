---
language: kotlin
exerciseType: 1
difficulty: 2
title: सीज़र सिफर
---

# --description--

जूलियस सीज़र ने क्रिप्टोग्राफी की सबसे पुरानी तरकीबों में से एक से अपनी निजी चिट्ठियों को सुरक्षित रखा था: वे किसी संदेश के हर अक्षर को वर्णमाला में एक निश्चित संख्या में आगे स्थित अक्षर से बदल देते थे। 3 के शिफ्ट पर `a`, `d` बन जाता है, `b`, `e` बन जाता है और `c`, `f` बन जाता है।

वर्णमाला एक वृत्त जैसा व्यवहार करती है, इसलिए अंत के अक्षर घूमकर वापस शुरुआत पर पहुँच जाते हैं: 3 के शिफ्ट पर `x`, `a` बन जाता है, `y`, `b` बन जाता है और `z`, `c` बन जाता है।

जो कुछ भी अक्षर नहीं है, जैसे रिक्त स्थान, अल्पविराम, विस्मयादिबोधक चिह्न या अंक, वह सिफर से बिना बदले गुज़र जाता है।

# --instructions--

एक फ़ंक्शन `caesarCipher` लिखें जो एक संदेश `text` और एक पूर्ण संख्या `shift` लेता है, और एन्कोड किया हुआ संदेश लौटाता है।

उदाहरण:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- संदेश हमेशा लोअरकेस में होता है, इसलिए आपको कभी भी अपरकेस अक्षरों से निपटना नहीं पड़ेगा।
- जो वर्ण अक्षर नहीं हैं, वे अपनी जगह और अपना मान बनाए रखते हैं।
- शिफ्ट कभी ऋणात्मक नहीं होता। `0` का शिफ्ट संदेश को अपरिवर्तित छोड़ देता है, और `26` का शिफ्ट भी ऐसा ही करता है।

# --seed--

```kotlin
fun caesarCipher(text: String, shift: Int): String {
    
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

3 का शिफ्ट "hello" को "khoor" में बदल देता है

```kotlin
    tryCatch(caesarCipher("hello", 3) == "khoor")
```

वर्णमाला का अंत घूमकर शुरुआत पर वापस आ जाता है, इसलिए "xyz", "abc" बन जाता है

```kotlin
    tryCatch(caesarCipher("xyz", 3) == "abc")
```

0 का शिफ्ट संदेश को अपरिवर्तित छोड़ देता है

```kotlin
    tryCatch(caesarCipher("abc", 0) == "abc")
```

26 का शिफ्ट वर्णमाला का एक पूरा चक्र है, इसलिए संदेश अपरिवर्तित रहता है

```kotlin
    tryCatch(caesarCipher("abc", 26) == "abc")
```

विराम चिह्न और रिक्त स्थान बिना बदले गुज़र जाते हैं

```kotlin
    tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

खाली संदेश खाली ही रहता है

```kotlin
    tryCatch(caesarCipher("", 4) == "")
```

अक्षरों के बीच के रिक्त स्थान बने रहते हैं

```kotlin
    tryCatch(caesarCipher("a b c", 1) == "b c d")
```

25 के शिफ्ट पर भी अंक शिफ्ट नहीं होते

```kotlin
    tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

13 का शिफ्ट एक पूरे वाक्य को एन्कोड कर देता है

```kotlin
    tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt")
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
fun caesarCipher(text: String, shift: Int): String {
    val result = StringBuilder()

    for (char in text) {
        if (char in 'a'..'z') {
            result.append('a' + (char - 'a' + shift) % 26)
        } else {
            result.append(char)
        }
    }

    return result.toString()
}
```
