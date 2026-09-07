एक **class** ऑब्जेक्ट बनाने के लिए एक ब्लूप्रिंट है। Dart में, आप `class` कीवर्ड के बाद क्लास का नाम और घुंडी कोष्ठकों (curly braces) की एक जोड़ी लिखकर एक क्लास परिभाषित करते हैं:

```dart
class Animal {
  // fields and methods go here
}
```

परंपरा के अनुसार, क्लास के नाम **PascalCase** का उपयोग करते हैं (हर शब्द बड़े अक्षर से शुरू होता है)।

---

एक क्लास में **इंस्टेंस वेरिएबल** (जिन्हें फ़ील्ड भी कहा जाता है) हो सकते हैं जो हर ऑब्जेक्ट के लिए डेटा रखते हैं। आप इन्हें क्लास बॉडी के अंदर घोषित करते हैं और हर एक को एक शुरुआती मान देते हैं:

```dart
class Animal {
  String name = '';
  int age = 0;
}
```

इस क्लास से बनाया गया हर ऑब्जेक्ट अपना खुद का `name` और `age` रखेगा।

---

एक **constructor** एक विशेष मेथड है जो किसी क्लास से ऑब्जेक्ट बनाते (इंस्टेंशिएट करते) समय चलता है। कंस्ट्रक्टर का नाम क्लास के नाम जैसा ही होता है:

```dart
class Animal {
  String name;

  Animal(this.name);
}
```

`this.name` के रूप में लिखा गया पैरामीटर, कंस्ट्रक्टर को दिए गए मान को सीधे नए ऑब्जेक्ट की `name` फ़ील्ड में संग्रहीत कर देता है। इस तरह सेट की गई फ़ील्ड को शुरुआती मान की आवश्यकता नहीं होती।

आप `new` कीवर्ड (Dart में वैकल्पिक) या सिर्फ क्लास के नाम का उपयोग करके एक ऑब्जेक्ट बनाते हैं:

```dart
var dog = Animal('Rex');
```

---

पिछले अभ्यास में देखा गया `this.x` पैरामीटर एक संक्षिप्त रूप है। लंबे रूप में, कंस्ट्रक्टर बॉडी के अंदर हर पैरामीटर को उसकी फ़ील्ड में असाइन किया जाता है (`this.x` फ़ील्ड है, `x` पैरामीटर है):

```dart
class Point {
  int x = 0;
  int y = 0;

  Point(int x, int y) {
    this.x = x;
    this.y = y;
  }
}
```

वही क्लास इस तरह भी लिखी जा सकती है:

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

इस छोटे रूप को **initializing formals** कहा जाता है।

---

एक **method** क्लास के अंदर परिभाषित एक फ़ंक्शन है। मेथड किसी ऑब्जेक्ट के व्यवहार का वर्णन करते हैं:

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name makes a sound.');
  }
}
```

आप डॉट नोटेशन का उपयोग करके किसी ऑब्जेक्ट पर मेथड कॉल करते हैं: `dog.speak()`।

---

`this` क्लास के **वर्तमान इंस्टेंस** को संदर्भित करता है, यानी वह ऑब्जेक्ट जिस पर मेथड कॉल किया गया था। किसी मेथड के अंदर आप इसका उपयोग ऑब्जेक्ट की अपनी फ़ील्ड तक पहुँचने के लिए कर सकते हैं:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double diameter() {
    return this.radius * 2;
  }
}
```

यहाँ `this.radius`, उस circle की `radius` फ़ील्ड पढ़ता है जिस पर `diameter()` कॉल किया गया था। जब उसी नाम का कोई और वेरिएबल नहीं होता, तो `this.` को छोड़ा जा सकता है: `radius * 2` भी वैसे ही काम करता है।

---

Dart **named constructors** को सपोर्ट करता है, जो आपको ऑब्जेक्ट बनाने के अतिरिक्त तरीके परिभाषित करने देते हैं। Named constructors को `ClassName.constructorName` के रूप में लिखा जाता है:

```dart
class Point {
  double x;
  double y;

  Point(this.x, this.y);

  Point.origin()
      : x = 0,
        y = 0;
}
```

कोलन के बाद वाला भाग **initializer list** है: यह कंस्ट्रक्टर बॉडी चलने से पहले फ़ील्ड को असाइन करता है। इसके बाद आप origin पर एक ऑब्जेक्ट इस तरह बना सकते हैं: `var p = Point.origin();`

---

एक **getter** एक विशेष मेथड है जो किसी गणना किए गए या private मान को पढ़ता है और property access जैसा दिखता है। इसे आप `get` कीवर्ड से परिभाषित करते हैं:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

आप getter को फ़ील्ड की तरह एक्सेस करते हैं: `circle.area` (बिना कोष्ठक के)।

एरो `=> expr`, केवल एक मान लौटाने वाली बॉडी `{ return expr; }` का संक्षिप्त रूप है। यह getters के साथ-साथ किसी भी फ़ंक्शन या मेथड के लिए भी काम करता है:

```dart
double half(double n) => n / 2;
```

---

एक **setter** एक विशेष मेथड है जो आपको validation लॉजिक चलाते हुए एक मान असाइन करने देता है। इसे आप `set` कीवर्ड से परिभाषित करते हैं:

```dart
class Temperature {
  double _celsius = 0;

  double get celsius => _celsius;

  set celsius(double value) {
    if (value < -273.15) throw ArgumentError('Too cold!');
    _celsius = value;
  }
}
```

फ़ील्ड के नाम के आगे अक्सर `_` लगाया जाता है ताकि उसे private दिखाया जा सके।

---

**Inheritance** एक क्लास (**subclass**) को दूसरी क्लास (**superclass**) को extend करने और उसकी फ़ील्ड व मेथड्स को फिर से उपयोग करने देता है। इसके लिए `extends` कीवर्ड का उपयोग करें:

```dart
class Animal {
  String name = 'animal';

  void speak() {
    print('$name makes a sound.');
  }
}

class Dog extends Animal {
  void fetch() {
    print('$name fetches the ball.');
  }
}
```

`Dog`, `Animal` से `name` और `speak()` को इनहेरिट करता है और अपना खुद का मेथड `fetch()` जोड़ता है। जिस क्लास में कोई कंस्ट्रक्टर घोषित नहीं किया जाता, उसे बिना पैरामीटर वाला एक डिफ़ॉल्ट कंस्ट्रक्टर मिल जाता है, इसलिए आप `var dog = Dog();` लिख सकते हैं और फिर `dog.speak()` और `dog.fetch()` दोनों को कॉल कर सकते हैं।

---

जब किसी subclass के कंस्ट्रक्टर को superclass के कंस्ट्रक्टर को कॉल करना हो, तो **initializer list** में `super` कीवर्ड का उपयोग करें:

```dart
class Vehicle {
  String brand;
  Vehicle(this.brand);
}

class Car extends Vehicle {
  int doors;
  Car(String brand, this.doors) : super(brand);
}
```

`super(brand)`, `brand` आर्गुमेंट को `Vehicle` के कंस्ट्रक्टर तक आगे भेज देता है।

---

**Method overriding** एक subclass को superclass में पहले से मौजूद किसी मेथड का अपना खुद का implementation देने देता है। इसके लिए `@override` एनोटेशन का उपयोग करें:

```dart
class Shape {
  double area() => 0;
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

`@override` एनोटेशन Dart (और अन्य डेवलपर्स) को बताता है कि आप जानबूझकर superclass के मेथड को बदल रहे हैं।

---

एक **abstract class** एक ऐसी क्लास है जिसे सीधे इंस्टेंशिएट नहीं किया जा सकता। इसका उपयोग एक ऐसे आधार के रूप में किया जाता है जो एक contract परिभाषित करता है — यानी वे मेथड जिन्हें subclasses को implement करना ही होगा। आप बॉडी को छोड़कर abstract मेथड्स दिखाते हैं:

```dart
abstract class Shape {
  double area(); // abstract method — no body
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

`Shape()` को सीधे इंस्टेंशिएट करने की कोशिश करने पर एरर आता है।

---

**Static members** किसी खास इंस्टेंस के बजाय क्लास से ही जुड़े होते हैं। आप इन्हें `static` कीवर्ड से घोषित करते हैं और क्लास पर सीधे एक्सेस करते हैं:

```dart
class MathHelper {
  static const double pi = 3.14159;

  static double circleArea(double r) => pi * r * r;
}

void main() {
  // access without creating an object:
  print(MathHelper.pi);
  print(MathHelper.circleArea(5));
}
```

Static फ़ील्ड और मेथड सभी इंस्टेंस के बीच साझा होते हैं।

---

एक **factory constructor**, `factory` कीवर्ड का उपयोग करता है और आपको ऑब्जेक्ट बनाने पर नियंत्रण देता है — उदाहरण के लिए, एक कैश्ड इंस्टेंस या subtype लौटाना:

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

`Logger()` की हर कॉल एक ही इंस्टेंस लौटाती है (singleton pattern)।
