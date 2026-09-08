`String` दोहरे उद्धरण चिह्नों के बीच लिखा गया वर्णों का एक क्रम है।
`length` प्रॉपर्टी बताती है कि स्ट्रिंग में कितने वर्ण हैं, स्पेस सहित:
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

स्ट्रिंग के हर वर्ण का एक **इंडेक्स** होता है, जो पहले वर्ण के लिए `0` से शुरू होता है।
आप वर्ग कोष्ठक या `get` फंक्शन का उपयोग करके एक वर्ण पढ़ सकते हैं, और परिणाम एक `Char` होता है:
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
आखिरी वर्ण इंडेक्स `length - 1` पर होता है। `first()` और `last()` फंक्शन सुविधाजनक शॉर्टकट हैं:
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()` स्ट्रिंग के हर अक्षर को अपरकेस में बदलकर उसकी एक कॉपी लौटाता है, `lowercase()` इसका उल्टा करता है।
मूल स्ट्रिंग में कोई बदलाव नहीं होता:
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

किसी स्ट्रिंग में कोई खास टेक्स्ट है या नहीं, यह जांचने के लिए `contains`, `startsWith` और `endsWith` का उपयोग किया जाता है। ये सभी एक `Boolean` लौटाते हैं:
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
यह जांच केस-सेंसिटिव होती है, जब तक कि आप `ignoreCase = true` पास न करें:
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf` वह इंडेक्स लौटाता है जहाँ कोई टेक्स्ट **पहली बार** दिखाई देता है, या अगर वह बिल्कुल भी नहीं दिखता तो `-1` लौटाता है।
`lastIndexOf` इसके बजाय अंत से खोजता है:
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring` किसी स्ट्रिंग का एक हिस्सा निकालता है। दो आर्गुमेंट के साथ, यह शुरुआती इंडेक्स से लेकर अंतिम इंडेक्स तक के वर्ण लेता है, लेकिन अंतिम इंडेक्स को **शामिल नहीं करता**।
एक आर्गुमेंट के साथ, यह उस इंडेक्स से अंत तक सब कुछ लेता है:
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
`indexOf` और `substring` को मिलाकर आप किसी मार्कर के आसपास स्ट्रिंग को काट सकते हैं:
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split` किसी सेपरेटर के आधार पर स्ट्रिंग को टुकड़ों की एक `List` में तोड़ता है, जबकि `joinToString` इसका उल्टा करता है: यह किसी कलेक्शन के तत्वों को आपके चुने हुए सेपरेटर के साथ एक स्ट्रिंग में जोड़ देता है:
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

चूँकि `split` एक `List` लौटाता है, आप इसके तत्वों पर किसी भी अन्य लिस्ट की तरह लूप चला सकते हैं:
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// prints a, then b
```

---

यूज़र इनपुट में अक्सर अतिरिक्त स्पेस होते हैं। `trim()` शुरुआत और अंत के स्पेस हटाकर स्ट्रिंग लौटाता है, जबकि `trimStart()` और `trimEnd()` केवल एक तरफ के स्पेस हटाते हैं:
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()` `""` के लिए `true` होता है, जबकि `isBlank()` केवल स्पेस से बनी स्ट्रिंग्स के लिए भी `true` होता है:
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)` एक कॉपी लौटाता है जिसमें `old` की **हर** मौजूदगी को `new` से बदल दिया जाता है:
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)` स्ट्रिंग को `n` बार जोड़कर लौटाता है:
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)` स्ट्रिंग के `width` वर्णों तक पहुँचने तक शुरुआत में `char` जोड़ता है; `padEnd` उन्हें अंत में जोड़ता है।
अगर स्ट्रिंग पहले से ही पर्याप्त लंबी है, तो वह बिना बदले लौटा दी जाती है:
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
संख्याएँ स्ट्रिंग नहीं होतीं: पहले `toString()` को कॉल करें, जैसे `42.toString().padStart(4, '0')` में।
