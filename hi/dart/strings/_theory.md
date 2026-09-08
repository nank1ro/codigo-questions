**String** टेक्स्ट का एक टुकड़ा है: उद्धरण चिह्नों में लिपटे वर्णों का एक क्रम। Dart में आप सिंगल कोट्स `'...'` या डबल कोट्स `"..."` का उपयोग कर सकते हैं, दोनों बिल्कुल एक जैसे काम करते हैं:

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

एक तरह के कोट को चुनने से आप टेक्स्ट के अंदर बिना किसी एस्केपिंग के दूसरी तरह के कोट का उपयोग कर सकते हैं:

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

अगर आपको अंदर वही कोट चाहिए, तो उसे बैकस्लैश से एस्केप करें: `'It\'s sunny'`।

---

दो स्ट्रिंग्स को `+` ऑपरेटर से जोड़कर एक नई स्ट्रिंग बनाई जा सकती है, इसे **कॉन्कैटिनेशन** (concatenation) कहा जाता है:

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dart बिना किसी ऑपरेटर के, एक-दूसरे के बगल में लिखी गई दो स्ट्रिंग **लिटरल** को भी जोड़ देता है। यह लंबे टेक्स्ट को कई पंक्तियों में बांटने के लिए सुविधाजनक है:

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

`+` से केवल स्ट्रिंग्स को ही जोड़ा जा सकता है: `'Age: ' + 30` एक कंपाइल एरर है, क्योंकि `30` एक `int` है।

---

स्ट्रिंग्स को जोड़ने के बजाय, आप **इंटरपोलेशन** (interpolation) की मदद से वैल्यू को सीधे स्ट्रिंग में डाल सकते हैं। किसी वेरिएबल का मान डालने के लिए `$name` लिखें, और किसी भी एक्सप्रेशन का परिणाम डालने के लिए `${expression}` लिखें:

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

इंटरपोलेशन किसी भी प्रकार के साथ काम करता है: संख्याएं, बूलियन और सूचियां अपने आप टेक्स्ट में बदल जाती हैं, इसलिए `age` एक `int` होने के बावजूद `'Age: $age'` लिखना ठीक है।

---

हर स्ट्रिंग को अपनी `.length` प्रॉपर्टी के माध्यम से पता होता है कि उसमें कितने वर्ण हैं। स्पेस और विराम चिह्न भी वर्णों के रूप में गिने जाते हैं:

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

आप स्क्वायर ब्रैकेट और उसके **इंडेक्स** (`0` से शुरू होकर) का उपयोग करके एक ही वर्ण पढ़ सकते हैं। परिणाम एक-वर्ण वाला `String` होता है:

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

स्ट्रिंग की सीमा के बाहर का इंडेक्स (जैसे `word[5]`) पढ़ने पर एक एरर आता है।

---

Dart में स्ट्रिंग्स **इम्यूटेबल** होती हैं: एक बार बन जाने के बाद, एक स्ट्रिंग कभी नहीं बदलती। `.toUpperCase()` और `.toLowerCase()` जैसे मेथड मूल स्ट्रिंग को नहीं बदलते, वे **एक नई स्ट्रिंग लौटाते हैं**:

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

अगर आप चाहते हैं कि वेरिएबल में नया मान रहे, तो परिणाम को वापस असाइन करें: `word = word.toUpperCase();`।

---

यूज़र द्वारा टाइप किए गए टेक्स्ट में अक्सर आगे-पीछे अतिरिक्त स्पेस होते हैं। `.trim()` मेथड स्ट्रिंग की एक कॉपी लौटाता है जिसमें शुरुआती और आखिरी व्हाइटस्पेस (स्पेस, टैब और न्यूलाइन) हटा दिए गए हों। `.trimLeft()` और `.trimRight()` केवल एक तरफ से हटाते हैं:

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

`.substring(start, end)` मेथड इंडेक्स `start` से इंडेक्स `end` तक (`end` को **शामिल किए बिना**) स्ट्रिंग का हिस्सा लौटाता है। अगर आप `end` छोड़ देते हैं, तो यह स्ट्रिंग के अंत तक सब कुछ लेता है:

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

स्ट्रिंग के अंदर खोजने के लिए कई मेथड मौजूद हैं:

- `.contains(other)` `true` लौटाता है अगर `other` स्ट्रिंग में कहीं भी मौजूद हो
- `.startsWith(other)` और `.endsWith(other)` शुरुआत और अंत की जांच करते हैं
- `.indexOf(other)` पहली बार आने की इंडेक्स लौटाता है, या न मिलने पर `-1` लौटाता है

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

ये सभी केस-सेंसिटिव हैं: `'Dart'.contains('dart')` `false` है।

---

`.replaceAll(from, to)` मेथड एक नई स्ट्रिंग लौटाता है जिसमें `from` की **हर** occurrence को `to` से बदल दिया गया हो। `.replaceFirst(from, to)` केवल पहली occurrence को बदलता है:

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

`.split(separator)` मेथड सेपरेटर के हर occurrence पर काटकर एक स्ट्रिंग को `List<String>` में बदल देता है। इसका उल्टा `.join(separator)` है, जो सूचियों (lists) का एक मेथड है और तत्वों को एक स्ट्रिंग में जोड़ देता है:

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

खाली सेपरेटर के साथ `.split('')` कॉल करने पर आपको हर एक वर्ण वाली एक सूची मिलती है।
