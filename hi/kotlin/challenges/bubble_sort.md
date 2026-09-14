---
language: kotlin
exerciseType: 1
difficulty: 2
title: बबल सॉर्ट
---

# --description--

बबल सॉर्ट सबसे सरल सॉर्टिंग एल्गोरिदम में से एक है। यह एक सूची से गुज़रता है और आसन्न तत्वों के हर जोड़े की तुलना करता है, और जब भी वे गलत क्रम में होते हैं तो उन्हें आपस में बदल देता है। हर पूरे चक्र के बाद सबसे बड़ा शेष मान "बुलबुले" की तरह अपनी अंतिम जगह पर पहुँच जाता है, और जैसे ही कोई चक्र बिना एक भी अदला-बदली के पूरा होता है, सूची क्रमबद्ध हो जाती है।

# --instructions--

`bubbleSort` नाम का एक फ़ंक्शन लिखें जो एक `List<Int>` लेता है और उन्हीं मानों के साथ एक **नई** सूची आरोही क्रम में क्रमबद्ध करके लौटाता है। पास की गई सूची में बदलाव नहीं होना चाहिए।

आपको बबल सॉर्ट एल्गोरिदम स्वयं लागू करना होगा, आसन्न तत्वों की तुलना करके और उन्हें आपस में बदलकर। मानक लाइब्रेरी के किसी सॉर्टिंग फ़ंक्शन का उपयोग न करें।

आपका फ़ंक्शन एक खाली सरणी, एक ही तत्व वाली सरणी, पहले से क्रमबद्ध सरणी, दोहराए गए मानों और ऋणात्मक संख्याओं के साथ भी काम करना चाहिए।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(bubbleSort(listOf(3, 1, 2)))
// prints [1, 2, 3]
```

# --seed--

```kotlin
fun bubbleSort(arr: List<Int>): List<Int> {
    
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

एक खाली सरणी को एक खाली सरणी लौटानी चाहिए

```kotlin
    tryCatch(bubbleSort(listOf<Int>()) == listOf<Int>())
```

एक ही तत्व वाली सरणी वैसी ही रहनी चाहिए

```kotlin
    tryCatch(bubbleSort(listOf<Int>(42)) == listOf<Int>(42))
```

पहले से क्रमबद्ध सरणी उसी क्रम में रहनी चाहिए

```kotlin
    tryCatch(bubbleSort(listOf<Int>(1, 2, 3, 4, 5)) == listOf<Int>(1, 2, 3, 4, 5))
```

उल्टे क्रम में क्रमबद्ध सरणी को आरोही क्रम में बदलना चाहिए

```kotlin
    tryCatch(bubbleSort(listOf<Int>(5, 4, 3, 2, 1)) == listOf<Int>(1, 2, 3, 4, 5))
```

दोहराए गए सभी मान बने रहने चाहिए

```kotlin
    tryCatch(bubbleSort(listOf<Int>(3, 1, 3, 2, 1)) == listOf<Int>(1, 1, 2, 3, 3))
```

ऋणात्मक संख्याओं को धनात्मक संख्याओं से पहले क्रमबद्ध होना चाहिए

```kotlin
    tryCatch(bubbleSort(listOf<Int>(-5, 3, -1, 0, -9)) == listOf<Int>(-9, -5, -1, 0, 3))
```

एक लंबी मिश्रित सरणी आरोही क्रम में क्रमबद्ध होनी चाहिए

```kotlin
    tryCatch(bubbleSort(listOf<Int>(9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6)) == listOf<Int>(-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14))
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
fun bubbleSort(arr: List<Int>): List<Int> {
    val result = arr.toMutableList()
    var end = result.size
    var swapped = true
    while (swapped) {
        swapped = false
        for (i in 1 until end) {
            if (result[i - 1] > result[i]) {
                val temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end--
    }
    return result
}
```
