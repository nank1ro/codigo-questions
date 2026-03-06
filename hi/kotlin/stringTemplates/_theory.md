String _template_ एक String उत्पन्न करने का प्रोग्रामेटिक तरीका है।
Kotlin में हम दो या अधिक strings को एक साथ प्रदर्शित करने के लिए `+` चिह्न (concatenation) का उपयोग कर सकते हैं, जैसे:
```kotlin
println("Hello " + "Kotlin!")
// prints "Hello Kotlin!"
```

---

लेकिन `+` चिह्न का उपयोग करके एक संख्या जैसे '10' को एक string जैसे ` "friends"` में जोड़ने पर त्रुटि आती है क्योंकि वे अलग-अलग प्रकार के मान हैं

---

String templates हमें बिना किसी त्रुटि के, एक string में संख्या जोड़ने जैसे expressions प्रदर्शित करने की अनुमति देते हैं।
`${}` के अंदर एक expression रखने से वह evaluate होता है।
लौटाया गया मान String में बदल दिया जाता है और परिणामी String में डाला जाता है

---

यदि आप किसी identifier नाम के पहले $ लगाते हैं, तो String template उस identifier की सामग्री को String में डाल देगा

---

यदि `$` चिह्न के बाद जो आता है वह एक प्रोग्राम identifier के रूप में पहचाना नहीं जा सकता, तो कुछ विशेष नहीं होता

---

हम डॉलर चिह्नों के बाद variables भी डाल सकते हैं ताकि उनका मान दिखाया जा सके

---

हम string templates के अंदर जितनी बार चाहें उतनी बार मान डालने के लिए curly brackets का उपयोग कर सकते हैं

---

`${}` के अंदर हम conditions भी रख सकते हैं, उदाहरण के लिए:
```kotlin
println("${if (true) "Correct" else "Wrong"}")
// prints Correct
```

---

String templates का सबसे अच्छा उपयोग print statements में होता है, लेकिन हम उन्हें सामान्य strings की तरह variables में भी store कर सकते हैं।
