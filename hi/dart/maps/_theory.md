एक **मैप** (Map) **की-वैल्यू जोड़ों** (key-value pairs) का एक संग्रह है: हर वैल्यू एक अद्वितीय की के अंतर्गत संग्रहीत होती है, और आप उस की का उपयोग करके वैल्यू को फिर से खोज सकते हैं। मैप को `{}` लिटरल सिंटैक्स से बनाया जाता है, हर जोड़े को `key: value` के रूप में लिखते हुए:

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

टाइप एनोटेशन `Map<String, int>` Dart को बताती है कि हर की एक `String` है और हर वैल्यू एक `int` है। सूचियों की तरह, `var` लिटरल से टाइप का अनुमान लगाता है:

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

किसी वैल्यू को पढ़ने के लिए आप वर्गाकार कोष्ठकों (square brackets) के अंदर की का उपयोग करते हैं, ठीक वैसे ही जैसे सूची में इंडेक्स का उपयोग करते हैं:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

यदि की मैप में नहीं है, तो लुकअप त्रुटि (error) **नहीं** देता: यह `null` लौटाता है। इसी कारण `ages['Ann']` का टाइप `int` नहीं बल्कि `int?` (एक nullable `int`) है:

```dart
print(ages['Zed']); // null
```

---

`map[key] = value` से असाइन करने पर, यदि की मैप में अभी नहीं है तो एक नया जोड़ा **जोड़ा** जाता है, या किसी मौजूदा की के अंतर्गत संग्रहीत वैल्यू **अपडेट** हो जाती है:

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // adds Bob
ages['Ann'] = 31; // updates Ann
print(ages); // {Ann: 31, Bob: 25}
```

नई कीज़ मौजूदा कीज़ के बाद जोड़ी जाती हैं, इसलिए मैप सम्मिलन क्रम (insertion order) को याद रखता है।

---

`.remove(key)` मेथड मैप से एक की और उसकी वैल्यू को हटा देती है। यह हटाई गई वैल्यू लौटाती है, या यदि की मौजूद नहीं थी तो `null` लौटाती है:

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

`.length` प्रॉपर्टी की-वैल्यू जोड़ों की संख्या लौटाती है:

```dart
print(ages.length); // 1
```

---

यह जाँचने के लिए कि किसी मैप में कोई दी गई की है या नहीं, `.containsKey(key)` का उपयोग करें। यह जाँचने के लिए कि क्या कोई जोड़ा दी गई वैल्यू संग्रहीत करता है, `.containsValue(value)` का उपयोग करें। दोनों एक `bool` लौटाते हैं:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

किसी अनुपस्थित की को पढ़ने पर कभी त्रुटि नहीं आती, इसलिए हमेशा ध्यान रखें कि लुकअप आपको `null` दे सकता है। एक सुरक्षित पैटर्न यह है कि `??` ऑपरेटर से एक फ़ॉलबैक दिया जाए:

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

`.keys` प्रॉपर्टी मैप की सभी कीज़ देती है और `.values` सभी वैल्यूज़ देती है, सम्मिलन क्रम में। ये lazy `Iterable` होती हैं, इसलिए जब आपको वास्तविक `List` चाहिए तो `.toList()` कॉल करें:

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```
