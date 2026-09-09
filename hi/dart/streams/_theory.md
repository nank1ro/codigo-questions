`Future` एक **अकेला** मान दर्शाता है जो बाद में आता है। **Stream** मानों का एक **क्रम** दर्शाता है जो समय के साथ आते हैं: कीबोर्ड के दबाव, फ़ाइल के टुकड़े, सर्वर से आने वाले संदेश। हर मान को **इवेंट** कहा जाता है, और आख़िरी इवेंट के बाद स्ट्रीम **समाप्त** हो जाती है।

स्ट्रीम बनाने का सबसे आसान तरीका `Stream.fromIterable` है, जो किसी लिस्ट का हर एलिमेंट एक के बाद एक भेजती है:

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

इवेंट्स को एक-एक करके उपयोग करने के लिए तुम **`await for`** लूप का इस्तेमाल करते हो। `await` की तरह, यह केवल `async` से चिह्नित फ़ंक्शन के अंदर ही मान्य है, इसलिए `main` बन जाता है `Future<void> main() async`। लूप का बॉडी हर इवेंट पर एक बार चलता है और स्ट्रीम समाप्त होने पर लूप ख़त्म हो जाता है:

```dart
Future<void> main() async {
  final names = Stream.fromIterable(['Ada', 'Linus']);
  await for (final name in names) {
    print(name);
  }
  // Ada
  // Linus
}
```

यहाँ सामान्य `for` लूप काम नहीं करता: `Stream` कोई `Iterable` नहीं है, उसके मान एक साथ उपलब्ध नहीं होते।

---

`Stream.fromIterable` को सारे मान पहले से चाहिए। मानों को एक-एक करके **उत्पन्न** करने के लिए एक **असिंक्रोनस जनरेटर** लिखो: ऐसा फ़ंक्शन जिसका बॉडी `async*` से चिह्नित हो और जिसका रिटर्न टाइप `Stream<T>` हो। उसके अंदर `yield` स्ट्रीम को एक इवेंट भेजता है:

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

जब तुम `countTo(3)` कॉल करते हो तब बॉडी नहीं चलता: वह आलस्य से चलता है, जैसे-जैसे सुनने वाला मान माँगता है, और बॉडी ख़त्म होने पर स्ट्रीम समाप्त हो जाती है।

हर इवेंट को एक `List` में इकट्ठा करने के लिए `toList()` कॉल करो। यह `Future<List<T>>` लौटाता है, इसलिए तुम इसे `await` करते हो:

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

`await for` लूप प्रिंट करने से ज़्यादा कर सकता है: यह लूप से पहले घोषित किसी वेरिएबल को अपडेट कर सकता है। जो फ़ंक्शन किसी स्ट्रीम का उपयोग करके कोई परिणाम निकालता है उसे `async` से चिह्नित होना चाहिए, और वह उस परिणाम का `Future` लौटाता है:

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

फ़ंक्शन `return` तक तभी पहुँचता है जब स्ट्रीम समाप्त हो जाती है, इसलिए कॉल करने वाले को अंतिम मान तब मिलता है जब वह उस future का इंतज़ार करता है:

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

हर स्ट्रीम आख़िरकार ख़त्म होती है। `async*` जनरेटर के लिए स्ट्रीम तभी **समाप्त** हो जाती है जब फ़ंक्शन का बॉडी ख़त्म होता है, चाहे वह अंत तक पहुँचा हो या किसी `return` पर रुका हो। समाप्त स्ट्रीम पर `await for` लूप बाहर निकल जाता है, और `toList()` का कोई भी future पूरा हो जाता है।

स्ट्रीम दोबारा शुरू नहीं होती और अपने मान दोहराती नहीं: एक बार समाप्त होने के बाद वह समाप्त ही रहती है।

---

`await for` मौजूदा फ़ंक्शन को तब तक रोक देता है जब तक स्ट्रीम समाप्त न हो जाए। जब तुम **बिना इंतज़ार किए** इवेंट्स पर प्रतिक्रिया देना चाहते हो, तो `listen` कॉल करो और एक कॉलबैक पास करो: वह हर इवेंट पर एक बार बुलाया जाता है, और `listen` के बाद का कोड तुरंत चलता है।

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen` एक नामित पैरामीटर `onDone` भी स्वीकार करता है, यानी बिना आर्ग्युमेंट वाला एक फ़ंक्शन जो स्ट्रीम ख़त्म होने पर बुलाया जाता है:

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

एक `async*` जनरेटर `yield*` (yield-star) से **किसी दूसरी स्ट्रीम के हर इवेंट** को आगे भेज सकता है। यह उस `await for` लूप जैसा है जो हर मान yield करता है, बस एक ही पंक्ति में:

```dart
Stream<int> ones() async* {
  yield 1;
  yield 1;
}

Stream<int> sequence() async* {
  yield 0;
  yield* ones();
  yield 2;
}
// sequence() emits 0, 1, 1, 2
```

भीतरी स्ट्रीम समाप्त होते ही बाहरी स्ट्रीम अपने `yield` के साथ आगे बढ़ती है।

---

`Iterable` की तरह, `Stream` के पास भी ऐसे मेथड हैं जो किसी मौजूदा स्ट्रीम से एक **नई स्ट्रीम** बनाते हैं:

- `map` हर इवेंट को बदलता है
- `where` केवल उन इवेंट्स को रखता है जो शर्त पूरी करते हैं
- `take` दी गई संख्या के इवेंट्स के बाद रुक जाता है

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

ये मेथड **आलसी** हैं: जब तक कोई परिणामी स्ट्रीम को नहीं सुनता, कुछ नहीं चलता। इन्हें चेन किया जा सकता है, और स्रोत स्ट्रीम कभी नहीं बदलती।

---

चूँकि `where`, `map` और `take` सभी एक स्ट्रीम लौटाते हैं, तुम इन्हें चेन कर सकते हो और परिणाम को लिस्ट के रूप में पाने के लिए `toList()` से ख़त्म कर सकते हो। केवल आख़िरी `toList()` को `await` चाहिए, क्योंकि वही एकमात्र कॉल है जो `Future` लौटाती है:

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

`toList()` के अलावा, स्ट्रीम के पास और भी मेथड हैं जो उसके सारे इवेंट्स **उपयोग** करके एक ही `Future` लौटाते हैं:

- `first` और `last` पहले या आख़िरी इवेंट के साथ पूरे होते हैं
- `length` इवेंट्स की संख्या के साथ पूरा होता है
- `join(separator)` सारे इवेंट्स को एक `String` में जोड़कर पूरा होता है
- `reduce(combine)` इवेंट्स को दो-दो करके एक मान में मिलाता है

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce` अब तक के परिणाम और अगले इवेंट के साथ `combine` को बुलाता है। यदि स्ट्रीम खाली हो तो यह अपवाद फेंकता है, इसलिए इसका उपयोग तभी करो जब कम से कम एक इवेंट की गारंटी हो।

---

`Stream` के मेथड दो समूहों में बँटते हैं:

- **रूपांतरण** करने वाले मेथड जैसे `map`, `where`, `take` और `skip` एक **नई `Stream`** लौटाते हैं और आलसी होते हैं: जब तक नई स्ट्रीम सुनी न जाए, कोई इवेंट प्रोसेस नहीं होता
- **उपयोग** करने वाले मेथड जैसे `toList`, `reduce`, `join`, `first`, `last` और `length` स्ट्रीम को सुनते हैं और अंतिम परिणाम के साथ एक **`Future`** लौटाते हैं

इसलिए एक चेन में शून्य या अधिक रूपांतरण कॉल होते हैं और उसके बाद अधिकतम एक उपयोग कॉल।

---

जनरेटर एक ही फ़ंक्शन के अंदर से इवेंट्स बनाते हैं। जब इवेंट्स **कहीं और** से आते हैं (किसी बटन से, किसी नेटवर्क कॉलबैक से, किसी दूसरे ऑब्जेक्ट से) तो तुम्हें एक **`StreamController`** चाहिए। यह `dart:async` लाइब्रेरी में रहता है, इसलिए फ़ाइल की शुरुआत `import 'dart:async';` से होनी चाहिए।

कंट्रोलर एक स्ट्रीम का मालिक होता है और तुम्हें उसमें इवेंट्स डालने देता है:

```dart
import 'dart:async';

Stream<int> dice() {
  final controller = StreamController<int>();
  controller.add(4);
  controller.add(2);
  controller.close();
  return controller.stream;
}
```

- `add(value)` एक इवेंट भेजता है
- `close()` स्ट्रीम को ख़त्म करता है; इसे भूलने का मतलब है कि सुनने वाले हमेशा इंतज़ार करते रहेंगे
- `stream` वह `Stream` है जिसे सुनने वाले उपयोग करते हैं

किसी के सुनने से पहले जोड़े गए इवेंट्स एक बफ़र में रखे जाते हैं, इसलिए ऊपर वाला कोड सुरक्षित है: बाद में आने वाले सुनने वाले को भी `4` और `2` मिलते हैं।

---

`StreamController` अक्सर एक ही जगह बनाया और उपयोग किया जाता है: `listen` से `controller.stream` की सदस्यता लो, फिर `add` से इवेंट्स जोड़ो और `close` से कंट्रोलर बंद करो। चूँकि `listen` इंतज़ार नहीं करता, इवेंट्स मौजूदा कोड ख़त्म होने के बाद पहुँचाए जाते हैं, लेकिन हमेशा उसी क्रम में जिसमें वे जोड़े गए थे:

```dart
import 'dart:async';

void main() {
  final controller = StreamController<int>();
  controller.stream.listen((n) => print('got $n'));
  controller.add(1);
  controller.add(2);
  controller.close();
}
// got 1
// got 2
```

---

अब तक देखी गई स्ट्रीम्स **सिंगल-सब्सक्रिप्शन** हैं: वे ठीक एक सुनने वाले की अनुमति देती हैं। `listen`, `await for` या किसी भी उपयोग करने वाले मेथड को दूसरी बार बुलाने पर `StateError` फेंका जाता है ("Stream has already been listened to")।

किसी स्ट्रीम को कई सुनने वालों के बीच साझा करने के लिए उसे `asBroadcastStream()` से **ब्रॉडकास्ट** स्ट्रीम में बदलो:

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

ब्रॉडकास्ट स्ट्रीम बफ़र नहीं करती: सुनने वाले को केवल वही इवेंट्स मिलते हैं जो उसकी सदस्यता के **बाद** भेजे जाते हैं। उदाहरण में दोनों सुनने वाले पहले `await` से पहले सदस्यता लेते हैं, इसलिए दोनों को हर इवेंट मिलता है।

---

कंट्रोलर नामित कंस्ट्रक्टर `StreamController<T>.broadcast()` से सीधे एक ब्रॉडकास्ट स्ट्रीम बना सकता है। उसकी `stream` कितने भी सुनने वालों को स्वीकार करती है, और हर इवेंट उन सबको उसी क्रम में पहुँचाया जाता है जिस क्रम में उन्होंने सदस्यता ली:

```dart
import 'dart:async';

void main() {
  final controller = StreamController<String>.broadcast();
  controller.stream.listen((msg) => print('first: $msg'));
  controller.stream.listen((msg) => print('second: $msg'));
  controller.add('hi');
  controller.close();
}
// first: hi
// second: hi
```

हर ब्रॉडकास्ट स्ट्रीम की तरह यह भी बफ़र नहीं करती: किसी सुनने वाले की सदस्यता से पहले जोड़े गए इवेंट्स उसके लिए खो जाते हैं।

---

स्ट्रीम मानों के साथ-साथ **त्रुटियाँ** भी ले जा सकती है। `async*` जनरेटर के अंदर `throw` एक त्रुटि इवेंट भेजता है और स्ट्रीम को ख़त्म कर देता है; `StreamController` `addError` से ऐसी इवेंट भेज सकता है।

उपयोग करने वाले पक्ष पर, `await for` लूप त्रुटि को वहीं दोबारा फेंकता है जहाँ लूप है, इसलिए तुम उसे लूप के चारों ओर सामान्य `try`/`catch` से सँभालते हो:

```dart
Stream<int> risky() async* {
  yield 1;
  throw StateError('sensor offline');
}

Future<void> main() async {
  try {
    await for (final n in risky()) {
      print(n);
    }
  } catch (e) {
    print('caught: $e');
  }
}
// 1
// caught: Bad state: sensor offline
```

`listen` के साथ इसके बजाय एक `onError` कॉलबैक पास करो: `stream.listen(print, onError: (e) => print('caught: $e'));`
