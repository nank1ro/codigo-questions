एक **enumeration** (या *enum*) संबंधित मानों के समूह के लिए एक सामान्य प्रकार परिभाषित करता है, ताकि आप उन मानों के साथ टाइप-सेफ तरीके से काम कर सकें। Dart में आप इसे `enum` कीवर्ड से घोषित करते हैं, और इसके **values** को कॉमा से अलग करके सूचीबद्ध करते हैं:

```dart
enum Direction { north, south, east, west }
```

परंपरा के अनुसार value के नाम वेरिएबल्स की तरह `lowerCamelCase` में लिखे जाते हैं। प्रत्येक value को enum के नाम के माध्यम से एक्सेस किया जाता है, और उसे प्रिंट करने पर enum और value दोनों दिखते हैं:

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

एक enum को फ़ाइल के **टॉप लेवल** पर घोषित किया जाना चाहिए, कभी भी `main` जैसे किसी फ़ंक्शन के अंदर नहीं।

---

हर enum value में दो built-in properties होती हैं:

- `name` value का नाम एक `String` के रूप में
- `index` घोषणा में उसकी स्थिति है, जो `0` से शुरू होती है

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

हर enum के पास एक constant list भी होती है जिसे `values` कहा जाता है, जो घोषणा के क्रम में उसके सभी values रखती है। आप इसे किसी भी list की तरह index कर सकते हैं, इसकी `length` पढ़ सकते हैं, या `for-in` से इस पर loop चला सकते हैं:

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

चूँकि `values` एक list है, आप इसे उन list methods के साथ जोड़ सकते हैं जिन्हें आप पहले से जानते हैं। उदाहरण के लिए `.name` के साथ `.map()` का उपयोग करके values को strings की list में बदला जा सकता है:

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

`values` पर लूप चलाना किसी enum के हर मान को प्रोसेस करने का सामान्य तरीका है। लूप के अंदर वर्तमान मान किसी भी अन्य ऑब्जेक्ट की तरह व्यवहार करता है, इसलिए आप उसका `index` और `name` पढ़कर उन्हें सीधे स्ट्रिंग इंटरपोलेशन में उपयोग कर सकते हैं:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

हर enum value बिल्कुल एक ही बार मौजूद होती है, इसलिए एक ही value के दो संदर्भ हमेशा बराबर होते हैं। इन्हें `==` और `!=` से compare करें:

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

एक `switch` कथन enum पर branch करने का सामान्य तरीका है, जिसमें हर value के लिए एक `case` होता है:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) {
  switch (direction) {
    case Direction.north:
      return '^';
    case Direction.south:
      return 'v';
    case Direction.east:
      return '>';
    case Direction.west:
      return '<';
  }
}
```

जब cases **हर** value को कवर करते हैं, तो switch *exhaustive* होता है और उसे `default` की ज़रूरत नहीं होती। अगर आप कोई value भूल जाते हैं, तो बग के रनटाइम तक पहुँचने के बजाय कंपाइलर एक एरर देता है।

---

Dart 3 से `switch` का उपयोग एक **expression** के रूप में भी किया जा सकता है जो एक value देता है। हर case को `pattern => value` के रूप में लिखा जाता है और cases को कॉमा से अलग किया जाता है, बिना किसी `case` कीवर्ड या `break` के:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

स्टेटमेंट रूप की तरह ही, enum पर switch expression भी exhaustive होनी चाहिए।
