**Dictionaries** arrays और tuples के समान हैं, लेकिन आप index के बजाय *key* का उपयोग करके values तक पहुँचते हैं।
एक key कोई भी string या number हो सकती है।
Dictionaries को square brackets में लिखा जाता है, इस प्रकार:
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
यह `dictionaryName` नामक एक dictionary है जिसमें तीन *key-value pairs* हैं।
key `key1` value `1` की ओर इंगित करती है, `key2` `2` की ओर, और इसी तरह।

---

key द्वारा dictionary values तक पहुँचना बिल्कुल वैसा ही है जैसे index द्वारा array values तक पहुँचना:
```swift
// gets the age value from the user dictionary
user['age']
```

---

Arrays की तरह, Dictionaries _mutable_ होती हैं।
इसका मतलब है कि उन्हें बनाने के बाद बदला जा सकता है (यदि उन्हें constant घोषित नहीं किया गया है)।
इसका एक फायदा यह है कि हम dictionary बनाने के बाद उसमें नए _key/value pairs_ जोड़ सकते हैं, इस प्रकार:
```swift
dictName[newKeyName] = newValue
```

---

एक dictionary की लंबाई `count` उसमें मौजूद _key-value pairs_ की संख्या होती है।
प्रत्येक pair केवल एक बार गिना जाता है, भले ही value एक array हो। (हाँ, सही सुना: आप dictionaries के अंदर arrays भी रख सकते हैं!)

---

चूँकि dictionaries mutable हैं, उन्हें कई तरीकों से बदला जा सकता है। `removeValue(forKey:)` method से dictionary से items हटाए जा सकते हैं:
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed value, if the key exists
}
```
यह dictionary से key `keyName` और उससे जुड़ी value को हटा देगा।

---

क्या होगा अगर हम dictionary की सभी keys की सूची बनाना चाहें?
इसके लिए `keys` property है।

---

क्या होगा अगर हम dictionary की सभी values की सूची बनाना चाहें?
इसके लिए `values` property है।

---

Arrays की तरह, हम `for..in` keywords का उपयोग करके dictionary elements के बीच loop कर सकते हैं।
loop में key और value दोनों प्राप्त करने के लिए हमें कोई property निर्दिष्ट करने की आवश्यकता नहीं है:
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

हम arrays के साथ उपयोग की गई `isEmpty` property का उपयोग यह निर्धारित करने के लिए भी कर सकते हैं कि dictionary खाली है या नहीं

---

dictionary में values __जोड़ने__ या __बदलने__ के लिए, हम `updateValue(_:forKey:)` method का भी उपयोग कर सकते हैं

---

पहले हमने देखा कि `removeValue()` method से dictionary से _key-value pair_ कैसे हटाया जाता है।
हम key को `nil` value assign करके भी एक element हटा सकते हैं
```swift
dictName[keyName] = nil
// keyName has been removed from the dictionary dictName
```
