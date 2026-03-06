Kotlin में एक बुनियादी Boolean टाइप है, जिसे `Boolean` कहा जाता है।
Boolean मानों को तार्किक कहा जाता है, क्योंकि वे केवल true या false हो सकते हैं।
आप Kotlin में किसी भी व्यंजक का मूल्यांकन कर सकते हैं, और दो उत्तरों में से एक प्राप्त कर सकते हैं, `true` या `false`।

---

हम boolean मान `true` को एक वेरिएबल में ठीक उसी तरह स्टोर कर सकते हैं जैसे एक संख्या या एक स्ट्रिंग।

---

`true` का विपरीत मान `false` है

---

Boolean मानों को उनके पहले `!` का उपयोग करके नकारा भी जा सकता है, उदाहरण:
```kotlin
println(!true) // prints false
println(!false) // prints true
```

---

हम `&&` (_and_) और `||` (_or_) का उपयोग करके boolean व्यंजक भी बना सकते हैं:

- `&&` (_and_): केवल तभी true उत्पन्न करता है जब ऑपरेटर के बाईं ओर का Boolean व्यंजक और दाईं ओर का दोनों true हों।
- `||` (_or_): true उत्पन्न करता है यदि ऑपरेटर के बाईं या दाईं ओर का व्यंजक true है, या यदि दोनों true हैं।

```kotlin
println(true && true) // prints true
println(true && false) // prints false
println(false && false) // prints false
println(true || true) // prints true
println(true || false) // prints true
println(false || false) // prints false
```
