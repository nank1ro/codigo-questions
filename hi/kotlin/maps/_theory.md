`Map` **key-value जोड़ों** को संग्रहीत करता है: हर मान को इंडेक्स के बजाय उसकी key से खोजा जाता है।
map के अंदर keys अद्वितीय होती हैं, जबकि मान दोहराए जा सकते हैं।

आप `mapOf` से एक read-only map बनाते हैं, `to` इनफ़िक्स फ़ंक्शन का उपयोग करके हर key को उसके मान के साथ जोड़ते हुए:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// prints {Italy=Rome, France=Paris}
```
यहाँ `"Italy"` और `"France"` keys हैं, और `"Rome"` तथा `"Paris"` उनके मान हैं।

---

किसी मान को पढ़ने के लिए आप square brackets या `get` फ़ंक्शन का उपयोग करके map को उसकी key से इंडेक्स करते हैं:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

अगर key मौजूद नहीं है तो परिणाम `null` होता है, इसलिए `ages["Alice"]` का टाइप `Int` नहीं बल्कि `Int?` है:
```kotlin
println(ages["Zoe"]) // null
```

---

जब कोई key गायब हो सकती है, तो `getOrDefault` आपको `null` की जगह उपयोग करने के लिए मान चुनने देता है:
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
पहला argument key है, दूसरा वह डिफ़ॉल्ट मान है जो key न मिलने पर लौटाया जाता है।

---

`mapOf` से बनाया गया map read-only होता है। entries जोड़ने या बदलने के लिए `mutableMapOf` का उपयोग करें, जो एक `MutableMap` लौटाता है:
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adds a new entry
ages["Alice"] = 31 // updates the existing one
println(ages)
// prints {Alice=31, Bob=25}
```
`map[key] = value` से असाइन करने पर, अगर key नई है तो जोड़ा जुड़ जाता है, और अगर key पहले से मौजूद है तो मान बदल जाता है। आप वही काम करने वाले `ages.put("Bob", 25)` को भी कॉल कर सकते हैं।

---

`remove(key)` एक `MutableMap` से entry हटा देता है। अगर key मौजूद नहीं है तो कुछ नहीं होता।
`size` प्रॉपर्टी बताती है कि map में कितनी entries हैं:
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

कोई key मौजूद है या नहीं यह जांचने के लिए `containsKey` या `in` ऑपरेटर का उपयोग करें; कोई मान मौजूद है या नहीं यह जांचने के लिए `containsValue` का उपयोग करें:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

`keys` प्रॉपर्टी map की सभी keys को एक `Set` के रूप में लौटाती है, और `values` सभी मानों को एक collection के रूप में लौटाता है:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
दोनों उसी क्रम को बनाए रखते हैं जिसमें entries डाली गई थीं।

---

आप `for` से map पर लूप चला सकते हैं, हर entry को उसकी key और मान में विभाजित करते हुए:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// prints
// Alice is 30
// Bob is 25
```
कोष्ठक `(name, age)` हर entry को दो वेरिएबल्स में बाँट देते हैं। entries उसी क्रम में देखी जाती हैं जिसमें उन्हें डाला गया था।
