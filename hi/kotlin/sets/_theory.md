`Set` एक डेटा टाइप है जिसका उपयोग आप विभिन्न जानकारियों के संग्रह को एक क्रम में एकल वेरिएबल नाम के तहत संग्रहीत करने के लिए कर सकते हैं।
`List` से मुख्य अंतर यह है कि `Set` प्रत्येक मान का केवल एक तत्व की अनुमति देता है।

`List` की तरह, `Set` एक या कई प्रकार के कई मान संग्रहीत करता है और इन मानों को अलग करने के लिए **indexes** का उपयोग करता है।
आप इस रूप में एक expression के साथ set में आइटम असाइन कर सकते हैं:
```kotlin
val setName = setOf<itemsType>(item1, item2)
```
`itemsType` set के अंदर आइटम्स के प्रकार को दर्शाता है, उदाहरण के लिए, यह `Int`, `String`, `Any` हो सकता है...

---

`Set` __अद्वितीय__ आइटम्स का एक संग्रह है जिसमें कोई विशिष्ट क्रम नहीं होता।

```kotlin
val numbers = setOf(1, 1, 2) // [1]
println(numbers)
// prints [1, 2]
```

__[1]__ पर हम संख्या __1__ को दो बार शामिल करके एक set बनाने की कोशिश कर रहे हैं, लेकिन जैसा कि आप देख सकते हैं, प्रत्येक तत्व अद्वितीय होना चाहिए और दूसरा __1__ स्वचालित रूप से हटा दिया जाता है।

---

Kotlin में दो प्रकार के `Set` हैं:

- `Set` को बनाने के बाद संशोधित नहीं किया जा सकता।
- `MutableSet` को बनाने के बाद संशोधित किया जा सकता है, यानी आप इसके तत्वों को जोड़, हटा या अपडेट कर सकते हैं।

```kotlin
val numbers = setOf(1, 2, 3)
numbers.add(4) // [1]
```
__[1]__ एक Error देता है क्योंकि `Set` _केवल-पठनीय_ हैं।

एक संशोधन योग्य set बनाने के लिए `mutableSetOf` कीवर्ड का उपयोग करें
```kotlin
val numbers = mutableSetOf(1, 2, 3)
numbers.add(4)
println(numbers)
// prints [1, 2, 3, 4]
```

---

सबसे सामान्य `Set` गतिविधि `in` या `contains()` का उपयोग करके सदस्यता की जांच करना है

```kotlin
val numbers = setOf(1, 2, 3)
println(2 in numbers) // prints true
println(numbers.contains(5)) // prints false
```

जैसा कि आप ऊपर देख सकते हैं, `in` और `contains` एक `Bool` लौटाते हैं जो बताता है कि पास किया गया तत्व set में मौजूद है या नहीं

---

`Set` में तत्वों का क्रम महत्वपूर्ण नहीं है।
वास्तव में यदि आप समान तत्वों वाले लेकिन अलग क्रम में दो `Set` की तुलना करें तो आपको पता चलेगा कि वे बराबर हैं।

---

`Set` पर आप कई ऑपरेशन कर सकते हैं जैसे union, intersection, difference और subset की जांच।

```kotlin
val firstNumbers = setOf(1, 2, 3)
val lastNumbers = setOf(3, 4, 5)
val union = firstNumbers.union(lastNumbers) // [1, 2, 3, 4, 5]
val intersection = firstNumbers intersect lastNumbers // [3]
val difference = firstNumbers subtract lastNumbers // [1, 2]
val subset = firstNumbers.containsAll(lastNumbers) // false
```

---

`Set` को `List` में बदलने के लिए हम `toList()` फ़ंक्शन का उपयोग कर सकते हैं
