अब तक तुमने जो भी Dart लिखा है, वह एक **isolate** के अंदर चलता है: अपनी मेमोरी और अपना इवेंट लूप वाला एक थ्रेड। एक प्रोग्राम एक isolate से शुरू होता है, जिसे *main* isolate कहते हैं, और और अधिक शुरू कर सकता है।

isolate को ख़ास बनाने वाली बात यह है कि वे **कुछ भी साझा नहीं करते**। दो isolate कभी एक ही ऑब्जेक्ट नहीं देखते, इसलिए न लॉकिंग होती है, न डेटा रेस, और न आधा-अपडेट हुआ कोई मान। वे एक-दूसरे से केवल संदेशों की **प्रतियाँ** भेजकर बात करते हैं।

दूसरे isolate का उपयोग करने का सबसे छोटा तरीका **`Isolate.run`** है। यह एक फ़ंक्शन लेता है, उसे बिल्कुल नए isolate पर चलाता है, और तुम्हें उसके नतीजे के साथ एक `Future` देता है:

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate` `dart:isolate` लाइब्रेरी में रहता है, इसलिए फ़ाइल को `import 'dart:isolate';` से शुरू होना ही चाहिए। जब तक नया isolate गणना करता है, main isolate ख़ाली रहता है: यह असली **समानांतरवाद (parallelism)** है, काम दूसरे प्रोसेसर कोर पर होता है।

---

`Isolate.run` को दिया गया फ़ंक्शन अपने आस-पास के वेरिएबलों को **कैप्चर (capture)** कर सकता है। वे मान फ़ंक्शन के साथ नए isolate में कॉपी हो जाते हैं, इसलिए गणना अपने कॉलर पर निर्भर हो सकती है:

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run` फ़ंक्शन के लौटाए हुए मान का एक `Future` लौटाता है, इसलिए `triple` उसे सीधे लौटा सकता है: जब तुम future को बस आगे पहुँचाते हो तब `async` और `await` की ज़रूरत नहीं होती।

काम को दूसरे isolate पर ले जाने का मक़सद यह है कि लंबी गणनाएँ अब main isolate को जमा नहीं देतीं। एक सेकंड चलने वाला लूप main isolate पर चलने पर सब कुछ रोक देता है; `Isolate.run` के अंदर वह कहीं और चलता है और main isolate अपने इवेंट्स सँभालता रहता है।

---

isolate के बीच केवल **डेटा** कॉपी होता है; **कोड** नहीं। प्रोग्राम का हर isolate प्रोग्राम के सभी टॉप-लेवल फ़ंक्शन और क्लास पहले से देख सकता है, इसलिए `Isolate.run` को दी गई गणना उन्हें आज़ादी से कॉल कर सकती है:

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

सफ़र करता है केवल कैप्चर किया गया `text` जाते समय और नतीजे वाला `int` आते समय, हर एक एक प्रति। पैटर्न हमेशा वही है: भारी फ़ंक्शन को वहीं रहने दो, और **कॉल** को `Isolate.run` में लपेटो।

---

`await` और `Isolate.run` दो अलग समस्याएँ हल करते हैं, और उन्हें अलग रखना ज़रूरी है।

`await` तुम्हें एक ही isolate पर **कॉन्करेंसी (concurrency)** देता है: जब एक फ़ंक्शन टाइमर या सर्वर का इंतज़ार करता है, तब isolate बाक़ी लंबित कोड चलाता है। कुछ भी एक ही क्षण पर नहीं चलता, isolate बस ख़ाली बैठना बंद कर देता है। इंतज़ार के लिए यही सही औज़ार है।

`Isolate.run` तुम्हें **समानांतरवाद (parallelism)** देता है: दूसरे प्रोसेसर कोर पर एक दूसरा isolate, पहले के साथ उसी क्षण अपना कोड चलाता हुआ। गणना के लिए यही सही औज़ार है।

```dart
await Future.delayed(const Duration(seconds: 1)); // इंतज़ार: कोई कोर व्यस्त नहीं है
await Isolate.run(() => hugeCalculation());       // गणना हो रही है: दूसरा कोर व्यस्त है
```

धीमी गणना का await करना कोई मदद नहीं करता: `await bigSum()` अब भी `bigSum` को मौजूदा isolate पर ही चलाता है और आख़िरी पंक्ति तक उसे रोके रखता है। वह काम केवल दूसरा isolate ही दूर ले जाता है।

---

`Isolate.run` एक अकेले नतीजे के लिए शॉर्टकट है। जब तुम ऐसा isolate चाहते हो जो चलता रहे और एक से अधिक बार जवाब दे, तो उसे ख़ुद **`Isolate.spawn`** से शुरू करो और उसे जवाब देने का एक तरीका दो।

वह तरीका पोर्ट्स की एक जोड़ी है। एक **`ReceivePort`** एक मेलबॉक्स है: तुम उसे अपनी तरफ़ बनाते हो और आने वाले संदेश पढ़ते हो। उसका **`sendPort`** उस मेलबॉक्स का पता है, और जवाब देने के लिए दूसरे isolate को बस उसी की ज़रूरत होती है।

```dart
import 'dart:isolate';

void sayHello(SendPort port) {
  port.send('hi');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(sayHello, receivePort.sendPort);
  final message = await receivePort.first;
  print(message); // hi
}
```

`Isolate.spawn` चलाने वाला फ़ंक्शन और उसे दिया जाने वाला एक अकेला संदेश लेता है, यहाँ वह `SendPort` है। दूसरी तरफ़, `send` मेलबॉक्स में एक मान डालता है, और `await receivePort.first` पहले संदेश का इंतज़ार करके पोर्ट बंद कर देता है।

---

`Isolate.spawn` को दिया गया फ़ंक्शन **entry point** कहलाता है। वह एक टॉप-लेवल (या static) फ़ंक्शन होना चाहिए जो ठीक एक पैरामीटर ले: वह संदेश जिसे `Isolate.spawn` उसे देता है।

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

`ReceivePort` में आने वाले संदेशों का static प्रकार `dynamic` होता है, क्योंकि कोई भी मान भेजा गया हो सकता है। जब तुम्हें पता हो कि दूसरा isolate क्या भेजता है, तो उसे कास्ट करो:

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

स्पॉन किया गया isolate हमेशा वही चार क़दम चलता है: मेलबॉक्स खोलो, वर्कर को उसके पते के साथ स्पॉन करो, जवाब का इंतज़ार करो, उसका उपयोग करो।

```dart
import 'dart:isolate';

void worker(SendPort port) {
  port.send('done');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(worker, receivePort.sendPort);
  print(await receivePort.first);
}
```

`Isolate.spawn` के आगे वाला `await` isolate के *शुरू होने* का इंतज़ार करता है, उसके काम के पूरा होने का नहीं: नतीजा बाद में पोर्ट के ज़रिए आता है।

---

`Isolate.spawn` entry point को ठीक **एक** संदेश देता है, और वर्कर को आम तौर पर जवाब देने के लिए एक `SendPort` और काम करने के लिए कुछ डेटा, दोनों चाहिए होते हैं। आम तरकीब यह है कि सब कुछ एक `List` में बाँधो और दूसरी तरफ़ खोलो:

```dart
void multiply(List<Object> message) {
  final port = message[0] as SendPort;
  final value = message[1] as int;
  port.send(value * 2);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(multiply, <Object>[receivePort.sendPort, 21]);
  print(await receivePort.first); // 42
}
```

सूची जाते समय कॉपी हो जाती है, इसलिए वर्कर अपने ही मान पढ़ता है। एक `SendPort` उन चंद चीज़ों में से एक है जो कॉपी नहीं होती बल्कि साझा की जाती हैं: वह उस isolate के मेलबॉक्स की ओर इशारा करता रहता है जिसने उसे बनाया, और यही वजह है कि उसे वापसी के पते की तरह इस्तेमाल किया जा सकता है।

---

`first` एक संदेश पढ़ता है और मेलबॉक्स बंद कर देता है। एक `ReceivePort` एक **`Stream`** भी है, इसलिए कई संदेश पढ़ने के लिए तुम उस पर `await for` से लूप चलाते हो।

लूप अपने आप कभी ख़त्म नहीं होता: पोर्ट खुला रहता है और ऐसे संदेश का इंतज़ार करता रहता है जो शायद कभी न आए। इसलिए वर्कर आख़िरी मान एक संकेत की तरह भेजता है, अक्सर `null`, और लिसनर उस पर **`close()`** बुलाकर प्रतिक्रिया देता है, जो स्ट्रीम और लूप को ख़त्म कर देता है:

```dart
import 'dart:isolate';

void countdown(SendPort port) {
  port.send(3);
  port.send(2);
  port.send(1);
  port.send(null);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(countdown, receivePort.sendPort);
  await for (final message in receivePort) {
    if (message == null) {
      receivePort.close();
    } else {
      print(message);
    }
  }
  print('done');
}
```

---

संदेशों की पूरी शृंखला इकट्ठा करना एक ही विधि चलाता है: लूप से पहले ख़ाली सूची, हर असली संदेश पर एक `add`, और स्ट्रीम ख़त्म करने वाले संकेत पर `close()`। पोर्ट बंद होते ही `await for` समाप्त हो जाता है और फ़ंक्शन लौट सकता है:

```dart
Future<List<int>> collect(ReceivePort port) async {
  final values = <int>[];
  await for (final message in port) {
    if (message == null) {
      port.close();
    } else {
      values.add(message as int);
    }
  }
  return values;
}
```

संदेश उसी क्रम में रहते हैं जिस क्रम में वे भेजे गए थे, इसलिए तुम्हारी बनाई सूची दूसरे isolate के काम को क़दम-दर-क़दम दर्शाती है।

---

एक खुला `ReceivePort` लंबित काम गिना जाता है: जब तक वह मौजूद है, उसका मालिक isolate जीवित रहने का कारण रखता है और उसका इवेंट लूप संदेश का इंतज़ार करता रहता है। कमांड लाइन प्रोग्राम में खुले पोर्ट वाला main isolate बस **कभी बाहर निकलता ही नहीं**, और तुम्हें उसे हाथ से रोकना पड़ता है।

इसलिए पोर्ट बंद करना काम का एक हिस्सा है, कोई ऑप्टिमाइज़ेशन नहीं:

- `await port.first` एक संदेश के बाद उसे तुम्हारे लिए बंद कर देता है
- `port.close()` उसे साफ़-साफ़ बंद करता है, जो `await for` लूप के बाद तुम्हें चाहिए

`Isolate.run` में इस बही-खाते की कोई झंझट नहीं: वह पोर्ट बनाता है, उन्हें बंद करता है और isolate को तुम्हारे लिए बंद कर देता है। जब एक नतीजा ही चाहिए हो तो उसे ही चुनो।

---

एक isolate के अंदर फेंका गया अपवाद दूसरे पर छलांग नहीं लगा सकता: दोनों के स्टैक अलग होते हैं। `Isolate.run` वह खाई तुम्हारे लिए पाट देता है: वह त्रुटि पकड़ता है, उसे वापस कॉपी करता है और लौटाए गए future को उसी के साथ विफल कर देता है। तुम्हारी तरफ़ वह इसलिए एक साधारण एसिंक्रोनस त्रुटि है, जिसे `await` के चारों ओर `try`/`catch` से पकड़ा जाता है:

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

`try` के अंदर वाला `await` मायने रखता है, बिल्कुल किसी और future की तरह: उसके बिना future `try` ब्लॉक को अधूरा छोड़कर निकल जाता और `catch` कभी न चलता।

`Isolate.spawn` के साथ ऐसा कोई पुल नहीं है। बिना पकड़ी गई त्रुटि स्पॉन किए गए isolate को चुपचाप मार देती है और जनक ऐसे संदेश का इंतज़ार करता रहता है जो कभी नहीं आएगा, जो `Isolate.run` को पहले चुनने की एक और वजह है।

---

`Isolate.run` से लौटने वाली त्रुटि दूसरी तरफ़ फेंकी गई त्रुटि की एक **प्रति** होती है, इसलिए सामान्य जाँचें अब भी चलती हैं: `catch (e)` तुम्हें ऑब्जेक्ट देता है, और `e is FormatException` बताता है कि वह किस तरह की विफलता थी।

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

जिस पर तुम भरोसा नहीं कर सकते, वह है तुम्हारे अपने isolate की ओर इशारा करता स्टैक ट्रेस: त्रुटि सफ़र करती है, स्टैक नहीं।

---

सब जोड़ो तो एक `Isolate.run` प्रोग्राम साधारण क्रमिक कोड जैसा पढ़ा जाता है: कॉल से पहले वाली पंक्ति main isolate पर चलती है, गणना कहीं और चलती है, और `await` के बाद वाली पंक्ति नतीजे के साथ वापस main isolate पर चलती है।

```dart
import 'dart:isolate';

int twice(int n) => n * 2;

Future<void> main() async {
  print('start');
  final result = await Isolate.run(() => twice(4));
  print(result);
}
// start
// 8
```

---

चूँकि isolate कोई मेमोरी साझा नहीं करते, हर संदेश पार करते समय **कॉपी** हो जाता है। संख्याएँ, बूलियन, स्ट्रिंग्स, `null`, सूचियाँ, मैप और ज़्यादातर साधारण ऑब्जेक्ट वह सफ़र कर सकते हैं; चंद चीज़ें बिल्कुल कॉपी नहीं हो सकतीं, जैसे एक खुला सॉकेट, और उसे भेजने की कोशिश एक `ArgumentError` फेंकती है।

इसका नतीजा वह नियम है जो isolate को सुरक्षित बनाता है: भेजने के बाद दोनों तरफ़ **दो स्वतंत्र ऑब्जेक्ट** रहते हैं। जो भी एक isolate अपनी प्रति के साथ करे, वह दूसरे को दिखता नहीं।

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // कॉपी बढ़ती है
print(numbers);                           // [1, 2, 3]
```

`SendPort` उस नियम का अपवाद है जो नियम को सिद्ध करता है: वह कॉपी किए जाने की बजाय साझा किया जाता है, ठीक इसलिए कि वह असली मेलबॉक्स की ओर इशारा करता रहे।

---

हर `Isolate.run` अपना अलग isolate शुरू करता है, इसलिए कई सचमुच एक ही क्षण पर चलते हैं, मशीन में जितने कोर हों उतनों पर। पैटर्न वही है जो तुम futures से पहले से जानते हो: पहले हर गणना शुरू करो, फिर सबका इंतज़ार `Future.wait` से करो, जो नतीजों को इनपुट के क्रम में रखता है।

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

एक isolate शुरू करना मुफ़्त नहीं है: उसकी कीमत मेमोरी और कुछ मिलीसेकंड है। एक लंबी गणना को चंद isolate में बाँटना फ़ायदे का सौदा है, हज़ार तुच्छ जोड़ हज़ार isolate को भेजना नहीं।
