---
language: kotlin
exerciseType: 1
difficulty: 3
title: रोमन अंक परिवर्तक
---

# --description--

एक फ़ंक्शन बनाएं जो एक धनात्मक पूर्णांक को अपने पैरामीटर के रूप में लेता है और उस पूर्णांक के रोमन अंक प्रतिनिधित्व वाली एक स्ट्रिंग लौटाता है। आधुनिक रोमन अंक प्रत्येक अंक को अलग-अलग व्यक्त करके लिखे जाते हैं, बाएं सबसे अंक से शुरू करते हुए और शून्य मान वाले किसी भी अंक को छोड़ते हुए।

# --instructions--

उदाहरण:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- सभी रोमन अंक अपरकेस में लौटाए जाने चाहिए।
- इस संकेतन में प्रदर्शित की जा सकने वाली सबसे बड़ी संख्या 3,999 है।

# --seed--

```kotlin
fun convertToRoman(n: Int): String {
    
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

संख्या `2` का मान `II` होना चाहिए

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

संख्या `12` का मान `XII` होना चाहिए

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

संख्या `16` का मान `XVI` होना चाहिए

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

संख्या `44` का मान `XLIV` होना चाहिए

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

संख्या `68` का मान `LXVIII` होना चाहिए

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

संख्या `400` का मान `CD` होना चाहिए

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

संख्या `798` का मान `DCCXCVIII` होना चाहिए

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

संख्या `1000` का मान `M` होना चाहिए

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

संख्या `3999` का मान `MMMCMXCIX` होना चाहिए

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

संख्या `649` का मान `DCXLIX` होना चाहिए

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

संख्या `1666` का मान `MDCLXVI` होना चाहिए

```kotlin
    tryCatch(convertToRoman(1666) == "MDCLXVI")
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
fun convertToRoman(n: Int): String {
    var result = ""
    var number = n

    val values = listOf(
        Pair(1000, "M"),
        Pair(900, "CM"),
        Pair(500, "D"),
        Pair(400, "CD"),
        Pair(100, "C"),
        Pair(90, "XC"),
        Pair(50, "L"),
        Pair(40, "XL"),
        Pair(10, "X"),
        Pair(9, "IX"),
        Pair(5, "V"),
        Pair(4, "IV"),
        Pair(1, "I")
    )

    for (i in values.indices) {
        val value = values[i].first
        val letter = values[i].second

        while (number >= value) {
            result += letter
            number -= value
        }
    }

    return result
}
```
