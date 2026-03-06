निर्णय लेना तब आवश्यक होता है जब हम केवल एक निश्चित शर्त पूरी होने पर ही कोड निष्पादित करना चाहते हैं।
मान लीजिए कि हम बाहर खेलना चाहते हैं केवल तभी जब मौसम अच्छा हो।
प्रोग्रामिंग में, हम एक boolean वेरिएबल `niceWeather` सेव कर सकते हैं और `if` यह वेरिएबल `true` है तो बाहर खेलने की क्रिया कर सकते हैं, जैसे:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```

---

आइए पिछले उदाहरण को जारी रखें।
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```
हमने देखा कि `if` स्टेटमेंट कोड ब्लॉक को केवल तभी निष्पादित करता है जब शर्त `true` हो।
एक और महत्वपूर्ण बात **कर्ली ब्रैकेट्स** `{}` हैं जो एक कोड ब्लॉक को दर्शाते हैं।

---

हमने अभी देखा कि किसी शर्त के पूरा होने पर कोड ब्लॉक कैसे निष्पादित करें, अब देखते हैं कि पहली शर्त विफल होने पर दूसरा कोड ब्लॉक कैसे निष्पादित करें।
अगर मौसम अच्छा है तो हम बाहर खेलने जाते हैं; अन्यथा, हम घर पर रहते हैं।
Kotlin में हम `else` स्टेटमेंट का उपयोग कर सकते हैं, जैसे:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

मान लीजिए कि हमें एक और शर्त की जांच करनी है, जैसे इस उदाहरण में:
```kotlin
var num = 3
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else {
    println("do something else")
}
```
और इस कोड का आउटपुट `the number is 3` है।
सबसे पहले, जांचते हैं कि क्या संख्या 2 के बराबर है, यह false है।
तो दूसरे स्टेटमेंट पर चलते हैं और जांचते हैं कि क्या `num` 3 के बराबर है, यह true होने पर हम `the number is 3` प्रिंट करके कोड ब्लॉक निष्पादित करते हैं

---

हम जितने चाहें उतने `else if` स्टेटमेंट जोड़ सकते हैं, कोई सीमा नहीं है
```kotlin
var num = 4
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else if (num == 4) {
    println("the number is 4")
} else if (num == 5) {
    println("the number is 5")
} else if (num == 6) {
    println("the number is 6")
}
```
और इस कोड का आउटपुट `the number is 4` है।

---

हम एक कंडीशनल स्टेटमेंट (`if`, `else if` या `else`) को दूसरे कंडीशनल स्टेटमेंट के अंदर नेस्ट भी कर सकते हैं, एक अधिक जटिल संरचना बनाने के लिए।
```kotlin
var num = 4
if (num < 3) {
    println("the number is lower than 3")
} else {
    if (num == 3) {
        println("the number is 3")
    } else if (num == 4) {
        println("the number is 4")
    } else {
        println("the number is greather than 4")
    }
}
```
और इस कोड का आउटपुट `the number is 4` है।

---

_एल्विस ऑपरेटर_ `a ?: b` एक ऑप्शनल `a` को अनरैप करता है यदि उसमें कोई मान है, या `a` `null` होने पर डिफ़ॉल्ट मान `b` लौटाता है।
एक्सप्रेशन `a` हमेशा ऑप्शनल टाइप का होता है।
एक्सप्रेशन `b` को a के अंदर संग्रहीत टाइप से मेल खाना चाहिए।
एल्विस ऑपरेटर नीचे दिए गए कोड का संक्षिप्त रूप है:
```kotlin
if (a != null) a else b
```
