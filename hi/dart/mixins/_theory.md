एक क्लास केवल एक ही सुपरक्लास को `extend` कर सकती है, लेकिन अक्सर एक ही व्यवहार ऐसी क्लासों को भी चाहिए होता है जिनका आपस में और कोई संबंध नहीं होता। एक **मिक्सिन** व्यवहार का एक पुन: प्रयोज्य टुकड़ा है, जिसे जितनी चाहें उतनी क्लासें अपना सकती हैं।

आप इसे **`mixin`** कीवर्ड से घोषित करते हैं, और कोई क्लास उसे **`with`** कीवर्ड से अपनाती है:

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` अपनी तरफ से कोई सदस्य घोषित नहीं करती, फिर भी हर `Fish` के पास `swim` होता है, क्योंकि मिक्सिन के सदस्य क्लास के सदस्य बन जाते हैं। एक मिक्सिन का उपयोग जितनी चाहें उतनी क्लासें कर सकती हैं, चाहे वे संबंधित हों या नहीं।

---

मिक्सिन की बॉडी क्लास की बॉडी जैसी दिखती है: मेथड, गेटर और फ़ील्ड, बिल्कुल उसी तरह लिखे जाते हैं। अंतर घोषणा के साथ आप क्या कर सकते हैं, इसमें है।

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

मिक्सिन का नाम एक **टाइप** भी है, इसलिए `Server() is Timestamped` का मान `true` होता है और एक वेरिएबल को `Timestamped t = Server();` की तरह घोषित किया जा सकता है। अब दो असंबंधित क्लासें एक ही इम्प्लीमेंटेशन साझा करती हैं, बिना एक-दूसरे को इनहेरिट किए।

---

मिक्सिन केवल मेथडों तक सीमित नहीं है: वह **फ़ील्ड** भी घोषित कर सकता है, और मिक्सिन का उपयोग करने वाली हर क्लास के हर ऑब्जेक्ट को उनकी अपनी एक प्रति मिलती है।

```dart
mixin Counter {
  int count = 0;

  void increment() {
    count++;
  }
}

class Clicker with Counter {}

void main() {
  final a = Clicker();
  final b = Clicker();
  a.increment();
  a.increment();
  print(a.count); // 2
  print(b.count); // 0, b has its own count
}
```

यही मिक्सिन को एक इंटरफ़ेस से अधिक बनाता है: वह डेटा और उस पर काम करने वाला कोड, दोनों साथ लाता है।

---

एक `mixin` घोषणा एक क्लास **नहीं** है। वह केवल दूसरी क्लासों में मिक्स किए जाने के लिए होती है, इसलिए उसका अपना कोई कंस्ट्रक्टर नहीं होता और उसे इंस्टेंटिएट या एक्सटेंड नहीं किया जा सकता:

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

नाम फिर भी एक टाइप की तरह काम करता है, इसलिए `Team() is Scored` और `Scored s = Team();` दोनों ठीक हैं। मिक्सिन का कोई कंस्ट्रक्टर नहीं होता, इसलिए एक non-nullable फ़ील्ड को घोषणा की जगह पर ही इनिशियलाइज़ करना ज़रूरी है (या उसे `late` चिह्नित करना होता है), जैसे ऊपर `int score = 0;` है।

---

एक मिक्सिन कोई सदस्य **बिना बॉडी के** भी घोषित कर सकता है। ऐसा सदस्य ऐब्स्ट्रैक्ट होता है: मिक्सिन उसका उपयोग करता है, और मिक्सिन को अपनाने वाली क्लास को उसे सप्लाई करना होता है।

```dart
mixin Greeting {
  String get name;                       // no body: the class provides it

  String greet() => 'Hello, $name!';
}

class Person with Greeting {
  @override
  final String name;

  Person(this.name);
}

void main() {
  print(Person('Ada').greet()); // Hello, Ada!
}
```

व्यवहार मिक्सिन लाता है, डेटा क्लास लाती है। क्लास में एक फ़ील्ड, जैसे `final String name;`, उसी नाम के ऐब्स्ट्रैक्ट गेटर को संतुष्ट करने के लिए पर्याप्त है।

---

सब कुछ जोड़ते हुए, मिक्सिन का उपयोग करने वाले प्रोग्राम के तीन भाग होते हैं: `mixin` घोषणा, एक या अधिक क्लासें जो उसे `with` से अपनाती हैं, और साझा सदस्य को कॉल करने वाला कोड।

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

Dart में टॉप-लेवल घोषणाएँ किसी भी क्रम में लिखी जा सकती हैं, लेकिन फ़ाइल को ऊपर से नीचे पढ़ना तब आसान होता है जब मिक्सिन उसका उपयोग करने वाली क्लासों से पहले आता है।

---

एक क्लास **एक साथ कई मिक्सिन** का उपयोग कर सकती है, जिन्हें `with` के बाद सूचीबद्ध किया जाता है और कॉमा से अलग किया जाता है। Dart उन्हें **बाएँ से दाएँ** लागू करता है, हर एक को पिछले के ऊपर रखते हुए, इसलिए जब दो मिक्सिन एक ही सदस्य घोषित करते हैं तो सूची में **अंतिम** वाला जीतता है:

```dart
mixin A {
  String who() => 'A';
}

mixin B {
  String who() => 'B';
}

class First with A, B {}
class Second with B, A {}

void main() {
  print(First().who());  // B, the last mixin in the list
  print(Second().who()); // A, the last mixin in the list
}
```

इस स्टैकिंग को **लीनियराइज़ेशन** कहा जाता है: `with A, B` यह चेन बनाता है `Object` → `A` → `B` → क्लास स्वयं।

---

चूँकि अंतिम मिक्सिन जीतता है, `with` सूची का क्रम क्लास के अर्थ का हिस्सा है, केवल स्टाइल की बात नहीं। उसे दोबारा क्रमित करने से बदल जाता है कि ऑब्जेक्ट किस इम्प्लीमेंटेशन पर आख़िरकार पहुँचता है:

```dart
mixin Plain {
  String format(String text) => text;
}

mixin Starred {
  String format(String text) => '*$text*';
}

class Fancy with Plain, Starred {}  // format comes from Starred
class Simple with Starred, Plain {} // format comes from Plain
```

सदस्य जिन्हें केवल एक मिक्सिन घोषित करता है, वे कभी प्रतिस्पर्धा में नहीं होते: वे किसी भी क्रम में उपलब्ध रहते हैं। `with X, Y` को इस तरह पढ़ें: "`X` से शुरू करें, फिर `Y` को उसे ओवरराइड करने दें"।

---

मिक्सिन और `extends` साथ काम करते हैं। एक क्लास के पास एक सुपरक्लास **और** मिक्सिन की एक सूची हो सकती है, और मिक्सिन हमेशा सुपरक्लास के **ऊपर** लागू किए जाते हैं:

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

यहाँ चेन है `Object` → `Document` → `Timestamped` → `Report`। कोई सदस्य चेन के अंत से शुरू करके खोजा जाता है, इसलिए `Report().header()` को पहले `Timestamped` का वर्शन मिलता है। एक ही सदस्य को सुपरक्लास में और मिक्सिन में घोषित करना पूरी तरह वैध है: इसी तरह एक मिक्सिन इनहेरिट किए गए व्यवहार को बदलता या उसमें लपेटता है।

---

क्लास बॉडी चेन के बिल्कुल अंत में होती है, इसलिए क्लास में घोषित कोई सदस्य उसके किसी भी मिक्सिन से आए उसी सदस्य को **ओवरराइड** कर देता है। ओवरराइड के अंदर, **`super`** मिक्सिन द्वारा दिए गए वर्शन तक पहुँचता है:

```dart
mixin Polite {
  String greet() => 'Hello';
}

class Host with Polite {
  @override
  String greet() => '${super.greet()}, welcome!';
}

class Guest with Polite {}

void main() {
  print(Host().greet());  // Hello, welcome!
  print(Guest().greet()); // Hello
}
```

मिक्सिन स्वयं अछूता रहता है: `Guest` को अब भी मूल `greet` मिलता है। `super.greet()` ही है जो `Host` को साझा व्यवहार की प्रति बनाने के बजाय उस पर निर्माण करने देता है।

---

कुछ व्यवहार केवल एक विशेष क्लास के ऊपर ही मायने रखता है, और अपना काम करने के लिए उस क्लास के सदस्यों की ज़रूरत होती है। **`on`** क्लॉज यह आवश्यकता बताता है:

```dart
class Animal {
  String get name => 'animal';
}

mixin Noisy on Animal {
  String shout() => '${name.toUpperCase()}!';
}

class Dog extends Animal with Noisy {
  @override
  String get name => 'dog';
}

void main() {
  print(Dog().shout()); // DOG!
}
```

`on Animal` दो काम करता है: वह मिक्सिन को `Animal` के सदस्यों का उपयोग करने देता है, जैसे ऊपर `name`, और वह यह भी सीमित करता है कि मिक्सिन का उपयोग कौन कर सकता है। `class Rock with Noisy {}` एक कंपाइल-टाइम त्रुटि है, क्योंकि `Rock` एक `Animal` नहीं है।

---

`on` क्लॉज वाला मिक्सिन अपने सुपरक्लास के सदस्यों को अपना हुआ पढ़ता है, और यही उसे किसी मौजूदा टाइप को सजाने वाले व्यवहार के लिए एक अच्छी जगह बनाता है:

```dart
class Shape {
  String get kind => 'shape';
}

mixin Printable on Shape {
  void show() {
    print('a $kind');
  }
}

class Square extends Shape with Printable {
  @override
  String get kind => 'square';
}
```

`Square` `kind` को ओवरराइड करती है, और `show` ओवरराइड को स्वतः उठा लेता है: मिक्सिन हमेशा सदस्य को असली ऑब्जेक्ट पर कॉल करता है।

---

जब मिक्सिन के पास एक `on` क्लॉज होता है, तो वह उस टाइप के किसी सदस्य को **ओवरराइड** कर सकता है और चेन में अपने नीचे वाले वर्शन तक पहुँचने के लिए **`super`** कॉल कर सकता है:

```dart
class Logger {
  String log(String message) => message;
}

mixin Timestamped on Logger {
  @override
  String log(String message) => '[12:00] ${super.log(message)}';
}

class AppLogger extends Logger with Timestamped {}

void main() {
  print(AppLogger().log('started')); // [12:00] started
}
```

`super.log` मिक्सिन का अपना `log` नहीं है, वह उसके नीचे वाला है, इसलिए अनंत पुनरावृत्ति नहीं होती। कई ऐसे मिक्सिन को `with A, B` से स्टैक करें और हर एक पिछले को लपेटता है: कॉल पहले **अंतिम** मिक्सिन में आती है और नीचे सुपरक्लास तक जाती है।

---

एक `mixin` घोषणा को इंस्टेंटिएट या एक्सटेंड नहीं किया जा सकता, और एक साधारण `class` को `with` के बाद उपयोग नहीं किया जा सकता। जब आपको एक ऐसी घोषणा चाहिए जो **दोनों** तरह से काम करे, तो लिखें **`mixin class`**:

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

एक `mixin class` उस लचीलेपन की कीमत दो प्रतिबंधों से चुकाता है: उसे `Object` को एक्सटेंड करना ही होगा, इसलिए उसका अपना `extends` क्लॉज नहीं हो सकता, और उसे कंस्ट्रक्टर घोषित नहीं करना चाहिए, क्योंकि मिक्सिन कभी कोई कंस्ट्रक्टर नहीं चलाता।

---

मिक्सिन, इनहेरिटेंस और इंटरफ़ेस तीन अलग-अलग समस्याएँ हल करते हैं:

- **`extends`** किसी क्लास को एक सुपरक्लास देता है, एक "किसी प्रकार का है" संबंध के लिए। स्लॉट केवल एक है, इसलिए वह सबसे मज़बूत संबंध को मिलना चाहिए।
- **`with`** वह व्यवहार जोड़ता है जिसकी ज़रूरत कई असंबंधित क्लासों को होती है। इसकी कोई सीमा नहीं है, और इम्प्लीमेंटेशन साझा होता है, कॉपी नहीं।
- **`implements`** सदस्यों का एक सेट वादा करता है लेकिन **कोई** इम्प्लीमेंटेशन नहीं लाता: हर क्लास को बॉडी स्वयं लिखनी होती है।

मिक्सिन चाहने का एक साफ संकेत है ऐसी मेथड जिसे आप वरना उन क्लासों में कॉपी करते जिनका कोई स्वाभाविक साझा पैरेंट नहीं है, जैसे `Duck`, `Plane` और `Kite` सबको एक ही `fly` चाहिए।

---

स्टैक किए गए मिक्सिन ही हैं जिनसे छोटे, स्वतंत्र नियम एक क्लास में जुड़ते हैं। हर मिक्सिन उसी सदस्य को ओवरराइड करता है, अपना हिस्सा करता है, और काम आगे सौंपने के लिए `super` कॉल करता है। चूँकि कॉल पहले **अंतिम** मिक्सिन में आती है, `with` सूची का क्रम तय करता है कि कौन सा नियम किससे पहले चलेगा:

```dart
class Account {
  int balance = 0;

  void deposit(int amount) {
    balance += amount;
  }
}

mixin Doubled on Account {
  @override
  void deposit(int amount) {
    super.deposit(amount * 2);
  }
}
```

`class A extends Account with Doubled {}` हर जमा को दोगुना कर देता है। `Doubled` के बाद एक दूसरा मिक्सिन जोड़ें और जमा सबसे पहले उसे मिलेगी, `Doubled` तक पहुँचने से पहले।
