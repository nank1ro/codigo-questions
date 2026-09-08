एक **ऐरे** एक ही वेरिएबल नाम के तहत समान टाइप के मानों की एक निश्चित संख्या स्टोर करता है।
आप इसे `arrayOf` से बनाते हैं, स्क्वायर ब्रैकेट और `0` से शुरू होने वाले **इंडेक्स** का उपयोग करके एलिमेंट पढ़ते हैं, और `size` से एलिमेंट्स की संख्या प्राप्त करते हैं:
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
अंतिम एलिमेंट इंडेक्स `size - 1` पर होता है।

---

`arrayOf(1, 2, 3)` एक `Array<Int>` बनाता है जिसमें हर एलिमेंट एक बॉक्स्ड ऑब्जेक्ट होता है।
प्रिमिटिव टाइप्स के लिए Kotlin `IntArray`, `DoubleArray` और `BooleanArray` जैसे समर्पित, अधिक कुशल टाइप्स प्रदान करता है:
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
आप हर इंडेक्स प्राप्त करने वाले **init** लैम्ब्डा के साथ दी गई साइज़ का ऐरे बना सकते हैं, या शून्य से भरा `IntArray` बना सकते हैं:
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

हर ऐरे में इंडेक्स के साथ काम करने के लिए दो उपयोगी प्रॉपर्टीज़ होती हैं:
- `indices` वैध इंडेक्स की रेंज है, `0` से लेकर आखिरी तक
- `lastIndex` अंतिम एलिमेंट का इंडेक्स है, यानी `size - 1`
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

भले ही ऐरे `val` से घोषित किया गया हो, इंडेक्स पर वैल्यू असाइन करके उसके **एलिमेंट्स** को बदला जा सकता है:
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
हर एलिमेंट पर जाने के लिए आप `for` लूप या `forEach` का उपयोग कर सकते हैं:
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
ध्यान दें कि `n` और `it` वैल्यू की केवल-पढ़ने-योग्य कॉपी हैं और इन्हें दोबारा असाइन नहीं किया जा सकता, इसलिए एलिमेंट्स को बदलने के लिए आपको उनके इंडेक्स की जरूरत होती है।

---

यह जांचने के लिए कि ऐरे में कोई वैल्यू मौजूद है या नहीं, `in` या `contains` का उपयोग करें, दोनों एक `Boolean` लौटाते हैं।
`indexOf` पहली बार मिलने की जगह का इंडेक्स लौटाता है, या वैल्यू न मिलने पर `-1` लौटाता है:
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

ऐरे को सीधे प्रिंट करने पर उसके एलिमेंट्स नहीं दिखते, बल्कि `[Ljava.lang.String;@1b6d3586` जैसा कुछ प्रिंट होता है।
पढ़ने लायक स्ट्रिंग बनाने के लिए `joinToString` का उपयोग करें, चाहें तो एक कस्टम सेपरेटर के साथ (डिफ़ॉल्ट `", "` है), या स्क्वायर ब्रैकेट के बीच एलिमेंट्स पाने के लिए `contentToString` का उपयोग करें:
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

ऐरे को **इन-प्लेस** सॉर्ट किया जा सकता है, या एक नए सॉर्टेड कलेक्शन में कॉपी किया जा सकता है:
- `sort()` और `sortDescending()` ऐरे को खुद फिर से क्रमबद्ध करते हैं और कुछ नहीं लौटाते
- `reverse()` ऐरे के क्रम को खुद ही उलट देता है
- `sorted()`, `sortedDescending()` और `reversed()` ऐरे को बिना बदले छोड़ देते हैं और एक नई `List` लौटाते हैं
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

न्यूमेरिक ऐरे के साथ एग्रीगेट फ़ंक्शंस भी आते हैं:
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()` और `min()` खाली ऐरे पर एक एक्सेप्शन थ्रो करते हैं, इसलिए जब ऐरे खाली हो सकता है तो `maxOrNull()` और `minOrNull()` का उपयोग करें।

---

ऐरे और `MutableList` के बीच मुख्य अंतर यह है कि ऐरे का **साइज़ फिक्स्ड** होता है: एक बार बनने के बाद आप उसके एलिमेंट्स बदल सकते हैं लेकिन कभी भी किसी को जोड़ या हटा नहीं सकते, यहां `add` जैसा कोई फ़ंक्शन नहीं है।
`nums + 4` जैसे एक्सप्रेशन `nums` को बड़ा नहीं करते, बल्कि एक बिल्कुल नया ऐरे बनाते हैं:
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
जब एलिमेंट्स की संख्या समय के साथ बदलती है तो `MutableList` को प्राथमिकता दें, और जब संख्या पहले से पता हो या आपको प्रिमिटिव परफॉर्मेंस चाहिए तो ऐरे को।

---

ऐरे लिस्ट जैसे ही ट्रांसफॉर्मेशन फ़ंक्शंस सपोर्ट करते हैं। `filter` किसी शर्त से मेल खाने वाले एलिमेंट्स को रखता है और `map` हर एलिमेंट को ट्रांसफॉर्म करता है।
दोनों ऐरे नहीं, बल्कि एक नई `List` लौटाते हैं:
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
चूंकि परिणाम एक लिस्ट होता है, इसलिए इसे सीधे प्रिंट करने पर इसके एलिमेंट्स दिखते हैं।

---

जब लूप के दौरान आपको इंडेक्स और वैल्यू दोनों चाहिए हों, तो `withIndex()` का उपयोग करके हर pair को विभाजित करें, या `forEachIndexed` का उपयोग करें:
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

ऐरे और लिस्ट आसानी से एक-दूसरे में बदले जा सकते हैं:
- `toList()` और `toMutableList()` ऐरे को लिस्ट में कॉपी करते हैं
- `toTypedArray()` लिस्ट को `Array<T>` में कॉपी करता है
- `toIntArray()` `Int` की लिस्ट को `IntArray` में कॉपी करता है
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
हर कन्वर्शन एक **कॉपी** बनाता है, इसलिए परिणाम को बदलने से मूल पर कोई असर नहीं पड़ता।

---

लिस्ट के विपरीत, समान एलिमेंट्स वाले दो ऐरे `==` से **बराबर नहीं** होते: ऐरे की तुलना reference से होती है, इसलिए `==` सिर्फ तभी `true` होगा जब दोनों बिल्कुल एक ही ऐरे ऑब्जेक्ट हों।
कंटेंट की तुलना करने के लिए `contentEquals` का उपयोग करें:
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

चूंकि ऐरे का साइज़ फिक्स्ड होता है, उसका कोई हिस्सा लेने का मतलब है एक नया ऐरे बनाना:
- `copyOf()` पूरे ऐरे को कॉपी करता है, `copyOf(n)` पहले `n` एलिमेंट्स को कॉपी करता है
- `copyOfRange(from, to)` इंडेक्स `from` से `to` तक (`to` को **छोड़कर**) के एलिमेंट्स कॉपी करता है
- `sliceArray(range)` रेंज के दोनों सिरों सहित इंडेक्स के एलिमेंट्स कॉपी करता है
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
