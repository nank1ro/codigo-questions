एक **क्लास** ऑब्जेक्ट बनाने का एक खाका होती है। Kotlin में, आप `class` कीवर्ड के बाद क्लास के नाम से एक क्लास घोषित करते हैं।

एक क्लास में **प्रॉपर्टी** (डेटा) और **मेथड** (व्यवहार) हो सकते हैं। कंस्ट्रक्टर में सीधे प्रॉपर्टी घोषित करने के लिए, `val` या `var` उपसर्ग का उपयोग करें:

```kotlin
class Dog(val name: String)
```

यह एक `name` प्रॉपर्टी के साथ एक `Dog` क्लास बनाता है। आप क्लास को एक फ़ंक्शन की तरह कॉल करके एक इंस्टेंस बनाते हैं:

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

क्लासेस में उनके **प्राथमिक कंस्ट्रक्टर** में कई प्रॉपर्टी हो सकती हैं। प्रत्येक प्रॉपर्टी को कंस्ट्रक्टर पैरामीटर सूची में सीधे `val` (केवल-पठनीय) या `var` (परिवर्तनीय) के साथ घोषित किया जाता है:

```kotlin
class Person(val name: String, var age: Int)
```

`val` कीवर्ड `name` को निर्माण के बाद केवल-पठनीय बनाता है, जबकि `var` `age` को परिवर्तनीय बनाता है — आप इसे बाद में बदल सकते हैं:

```kotlin
val p = Person("Alice", 30)
p.age = 31  // अनुमत है क्योंकि age var है
```

---

**`init` ब्लॉक** प्राथमिक कंस्ट्रक्टर के तुरंत बाद चलता है। इसका उपयोग ऑब्जेक्ट बनाते समय सत्यापन या सेटअप लॉजिक करने के लिए किया जाता है:

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "त्रिज्या धनात्मक होनी चाहिए" }
    }
}
```

आप `init` के अंदर अतिरिक्त प्रॉपर्टी भी इनिशियलाइज़ कर सकते हैं:

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

क्लासेस में **मेथड** हो सकते हैं — ऐसे फ़ंक्शन जो क्लास से संबंधित होते हैं और उसकी प्रॉपर्टी पर काम करते हैं:

```kotlin
class Counter(var count: Int) {
    fun increment() {
        count++
    }
    fun value(): Int {
        return count
    }
}
```

मेथड को इंस्टेंस पर डॉट नोटेशन का उपयोग करके कॉल किया जाता है:

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

एक **`data class`** डेटा संग्रहीत करने के लिए डिज़ाइन की गई एक विशेष क्लास है। Kotlin स्वचालित रूप से आपके लिए `equals()`, `hashCode()`, `toString()` और `copy()` उत्पन्न करता है:

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)           // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

`copy()` फ़ंक्शन कुछ प्रॉपर्टी बदलकर एक नया इंस्टेंस बनाता है:

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
