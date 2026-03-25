एक **क्लास** ऑब्जेक्ट बनाने का एक खाका है। यह संबंधित डेटा (फ़ील्ड) और व्यवहार (मेथड) को एक साथ समूहित करती है।

Dart में, आप `class` कीवर्ड के बाद क्लास का नाम (परंपरा के अनुसार, PascalCase) लिखकर क्लास घोषित करते हैं:

```dart
class Car {
  String brand = 'Toyota';
}
```

आप इस प्रकार क्लास का एक **इंस्टेंस** (ऑब्जेक्ट) बनाते हैं:

```dart
final car = Car();
print(car.brand); // Toyota
```

---

एक **कंस्ट्रक्टर** एक विशेष मेथड है जो तब चलता है जब आप किसी क्लास का इंस्टेंस बनाते हैं। इसका उपयोग ऑब्जेक्ट के फ़ील्ड को आरंभ करने के लिए किया जाता है।

Dart में, सबसे सरल कंस्ट्रक्टर पैरामीटर को सीधे फ़ील्ड में असाइन करने के लिए **शॉर्टहैंड** `this.fieldName` का उपयोग करता है:

```dart
class Car {
  String brand;
  Car(this.brand);
}

void main() {
  final car = Car('Toyota');
  print(car.brand); // Toyota
}
```

---

एक **मेथड** किसी क्लास के अंदर परिभाषित एक फंक्शन है। मेथड किसी ऑब्जेक्ट के व्यवहार का वर्णन करते हैं।

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double area() {
    return 3.14 * radius * radius;
  }
}

void main() {
  final c = Circle(5);
  print(c.area()); // 78.5
}
```

मेथड ऑब्जेक्ट के अपने फ़ील्ड को सीधे नाम से (या `this.fieldName` के माध्यम से) एक्सेस कर सकते हैं।

---

एक **गेटर** एक विशेष मेथड है जो एक्सेस करने पर किसी प्रॉपर्टी जैसा दिखता है। इसे परिभाषित करने के लिए `get` कीवर्ड का उपयोग करें:

```dart
class Circle {
  double radius;
  Circle(this.radius);

  double get area => 3.14 * radius * radius;
}

void main() {
  final c = Circle(5);
  print(c.area); // फ़ील्ड की तरह एक्सेस किया जाता है, मेथड कॉल की तरह नहीं
}
```

गेटर फ़ील्ड से प्राप्त गणना किए गए मानों के लिए उपयोगी होते हैं।

---

**इनहेरिटेंस** किसी क्लास को दूसरी क्लास के फ़ील्ड और मेथड का पुनः उपयोग करने देती है। सबक्लास (चाइल्ड क्लास) बनाने के लिए `extends` कीवर्ड का उपयोग करें:

```dart
class Animal {
  String name;
  Animal(this.name);

  void speak() {
    print('...');
  }
}

class Cat extends Animal {
  Cat(String name) : super(name);

  @override
  void speak() {
    print('Meow');
  }
}
```

चाइल्ड क्लास पैरेंट कंस्ट्रक्टर को `super(...)` से कॉल करती है। `@override` एनोटेशन दर्शाता है कि मेथड पैरेंट के संस्करण को प्रतिस्थापित करता है।
