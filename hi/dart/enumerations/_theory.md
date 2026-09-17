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

---

Dart 2.17 से एक enum, क्लास की तरह ही, **fields** और एक **constructor** घोषित कर सकता है। इसे *enhanced enum* कहा जाता है। हर value फिर अपने खुद के आर्ग्युमेंट्स constructor को पास करती है:

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);
}

print(Planet.mars.moons); // 2
```

तीन नियमों पर ध्यान दें: values की लिस्ट **सेमीकोलन** `;` पर समाप्त होती है, fields ज़रूर `final` होने चाहिए, और constructor ज़रूर `const` होना चाहिए।

---

एक enhanced enum **methods** और **getters** भी घोषित कर सकता है। उनके अंदर, `this` वर्तमान value होती है, इसलिए आप सीधे इसकी `name`, `index` और fields का उपयोग कर सकते हैं:

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);

  bool get hasMoons => moons > 0;

  String describe() => '$name has $moons moon(s)';
}

print(Planet.earth.hasMoons);   // true
print(Planet.mars.describe()); // mars has 2 moon(s)
```

बिना fields वाला enum भी methods घोषित कर सकता है: उस स्थिति में values की लिस्ट `;` पर समाप्त होती है और उसके बाद members आते हैं।

---

`String` से वापस enum value पर जाने के लिए, `values` लिस्ट पर `byName` कॉल करें। यह वह value लौटाता है जिसका `name` बिल्कुल मेल खाता है:

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

अगर उस नाम की कोई value नहीं है, तो `byName` एक `ArgumentError` फेंकता है। जब स्ट्रिंग यूज़र इनपुट से आती है, तो `asNameMap()` एक ज़्यादा सुरक्षित विकल्प है: यह नामों से values तक का एक `Map<String, Direction>` लौटाता है, इसलिए किसी अज्ञात नाम को खोजने पर एरर की बजाय `null` मिलता है:

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

enum values शानदार **map keys** बनती हैं: ये यूनिक होती हैं, इन्हें compare करना आसान होता है, और कंपाइलर यह सुनिश्चित करता है कि आप केवल वास्तविक values का ही उपयोग करें। enum को key type के रूप में उपयोग करते हुए map घोषित करें और `[]` से values खोजें:

```dart
enum Direction { north, south, east, west }

Map<Direction, String> arrows = {
  Direction.north: '^',
  Direction.south: 'v',
  Direction.east: '>',
  Direction.west: '<',
};

print(arrows[Direction.east]); // >
```

किसी भी map की तरह, key न मिलने पर लुकअप `null` लौटाता है, इसलिए एक फ़ॉलबैक देने के लिए `??` का उपयोग करें।

---

एक enum `implements` कीवर्ड से एक **interface को implement** कर सकता है। फिर enum, interface द्वारा घोषित हर member को उपलब्ध कराने का वादा करता है, और उसकी values का उपयोग वहाँ किया जा सकता है जहाँ भी वह interface type अपेक्षित हो:

```dart
abstract class Describable {
  String describe();
}

enum Animal implements Describable {
  dog,
  cat;

  @override
  String describe() => 'I am a $name';
}

Describable pet = Animal.cat;
print(pet.describe()); // I am a cat
```

interface में घोषित किया गया getter, या तो एक getter से या उसी नाम की एक `final` field से implement किया जा सकता है।
