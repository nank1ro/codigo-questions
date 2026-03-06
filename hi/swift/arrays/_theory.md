Arrays एक डेटा टाइप है जिसका उपयोग आप विभिन्न जानकारियों के संग्रह को एक क्रम में एक ही वेरिएबल नाम के अंतर्गत संग्रहीत करने के लिए कर सकते हैं।
एक array एक या एकाधिक प्रकार के कई मान संग्रहीत करता है और इन मानों को अलग करने के लिए **indexes** का उपयोग करता है।
आप निम्नलिखित अभिव्यक्ति के रूप में एक array में आइटम असाइन कर सकते हैं:
```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType` array के अंदर आइटम्स के प्रकार को दर्शाता है, उदाहरण के लिए, यह `Int`, `String`, `Any` हो सकता है...

---

आप array के किसी व्यक्तिगत आइटम को उसके index से एक्सेस कर सकते हैं।
एक index एक पते की तरह है जो array में आइटम की स्थिति को पहचानता है।
index array के नाम के ठीक बाद, कोष्ठकों के बीच इस प्रकार दिखाई देता है:
```swift
arrayName[index]
```

Array indices `0` से शुरू होते हैं, `1` से **नहीं**! आप array के पहले आइटम को इस प्रकार एक्सेस करते हैं: `arrayName[0]`।
Array में दूसरा आइटम index 1 पर होता है: `arrayName[1]`।

---

एक array index किसी अन्य वेरिएबल नाम की तरह व्यवहार करता है।
इसका उपयोग मान एक्सेस करने के साथ-साथ असाइन करने के लिए भी किया जा सकता है।
आपने देखा कि array index को इस प्रकार एक्सेस किया जाता है:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
print(names[0])
```
इस प्रकार असाइनमेंट काम करता है:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
print(names[0])
```

---

स्ट्रिंग्स की तरह, arrays की एक **लंबाई** `count` होती है।
एक array की लंबाई उसमें मौजूद आइटम्स की संख्या होती है

---

एक array की लंबाई निश्चित होना जरूरी नहीं है।
आप जब चाहें array के अंत में आइटम जोड़ सकते हैं!
Array में आइटम जोड़ने के लिए हम `append` फंक्शन का उपयोग करते हैं:
```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// Prints ["a", "b", "c"]
```

---

कभी-कभी, आप array का केवल एक हिस्सा एक्सेस करना चाहते हैं।
निम्नलिखित कोड पर विचार करें:
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// prints [2, 3]
```
पहले, हम `numbers` नामक एक array बनाते हैं।
फिर, हम array का एक उपखंड लेते हैं और इसे slice array में संग्रहीत करते हैं।
हम array के नाम के बाद शामिल करने वाले indices को परिभाषित करके ऐसा करते हैं: `numbers[1...2]`।
Swift में हम `...` का उपयोग करके अंतिम index को शामिल कर सकते हैं, लेकिन हम `..<` का उपयोग करके अंतिम index को बाहर भी कर सकते हैं

---

Swift में हम array को जैसे चाहें स्लाइस कर सकते हैं!
```swift
// Grabs the first two items
listName[..<2]
// Grabs the fourth through last items
listName[3...]
```
यदि आपके array स्लाइस में array का पहला या अंतिम आइटम शामिल है, तो उस आइटम के लिए index शामिल करने की आवश्यकता नहीं है

---

यदि हम `Any` प्रकार निर्दिष्ट करें तो array के तत्व किसी भी प्रकार के हो सकते हैं:
```swift
var arrayName: [Any] = ["one", 2, true]
```
वास्तव में, ऊपर हमारे पास क्रम में एक स्ट्रिंग, एक पूर्णांक और एक बूलियन है।
लेकिन हमारे पास arrays के अंदर arrays भी हो सकते हैं!

---

कभी-कभी आपको array में किसी आइटम को खोजने की आवश्यकता होती है।
Swift में हम `firstIndex()` मेथड का उपयोग कर सकते हैं:
```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// prints 1
```
ऊपर का कोड पहले index को प्रिंट करता है जिसमें स्ट्रिंग `"Zac"` है, इस मामले में `1`।
हम `insert()` मेथड का उपयोग करके किसी विशिष्ट index पर array में आइटम भी डाल सकते हैं:
```swift
names.insert("Ali", at: 1)
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
ऊपर का कोड index `1` पर `"Ali"` डालता है, जो इस index के बाद सब कुछ 1 से नीचे खिसका देता है

---

Swift में हम `for..in` कीवर्ड्स का उपयोग करके बहुत सरल तरीके से array में लूप कर सकते हैं:
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// prints 1, 2, 3
```
`for` कीवर्ड के बाद एक वेरिएबल नाम आता है, इसे बारी-बारी से प्रत्येक array आइटम का मान असाइन किया जाएगा।

---

**Tuples** arrays की तरह हैं लेकिन आप तत्वों को नाम दे सकते हैं और उन नामों का उपयोग उन्हें संदर्भित करने के लिए कर सकते हैं
Tuple बनाने के लिए हम गोल कोष्ठक `()` का उपयोग करते हैं
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
