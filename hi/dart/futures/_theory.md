कुछ ऑपरेशन समय लेते हैं: फ़ाइल पढ़ना, सर्वर को कॉल करना, टाइमर का इंतज़ार करना। Dart उनके चलते समय प्रोग्राम को रोकता नहीं है। इसके बजाय, ऐसा फ़ंक्शन एक **`Future<T>`** लौटाता है: यह वादा कि `T` प्रकार का एक मान **बाद में** उपलब्ध होगा।

सबसे सरल future वह है जिसके पास पहले से उसका मान है, जिसे `Future.value` से बनाया जाता है:

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

किसी future से मान निकालने के लिए तुम उसे **`await`** करते हो। `await` मौजूदा फ़ंक्शन को तब तक रोक देता है जब तक future पूरा नहीं हो जाता, फिर तुम्हें सादा मान देता है। यह केवल **`async`** से चिह्नित फ़ंक्शन के अंदर ही मान्य है, इसलिए `main` बन जाता है `Future<void> main() async`:

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

`await` के बिना, `n` स्वयं `Future` होता, और `print(n)` संख्या के बजाय `Instance of 'Future<int>'` दिखाता।

---

किसी फ़ंक्शन को `async` चिह्नित करने से दो चीज़ें होती हैं: बॉडी के अंदर `await` की अनुमति मिलती है, और फ़ंक्शन **एक `Future` लौटाने** लगता है। तुम `return` से जो देते हो वही मान बनता है जिसके साथ future पूरा होता है, इसलिए घोषित रिटर्न प्रकार `Future<T>` होता है, भले ही बॉडी सादा `T` लौटाती हो:

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

यहाँ तुम्हें `Future.value` की ज़रूरत नहीं है: `async` कीवर्ड लौटाए गए मान को तुम्हारे लिए लपेट देता है।

---

`Future.value` तुरंत पूरा हो जाता है। समय लेने वाले काम की नकल करने के लिए **`Future.delayed`** का उपयोग करो: यह एक `Duration` और एक फ़ंक्शन लेता है, उस अवधि तक प्रतीक्षा करता है, फिर फ़ंक्शन जो लौटाए उसके साथ पूरा होता है:

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` को `seconds`, `milliseconds` या `minutes` जैसे नामित पैरामीटर से बनाया जाता है। किसी `async` फ़ंक्शन के अंदर तुम केवल रुकने के लिए, बिना किसी मान के, अकेली देरी का भी await कर सकते हो:

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

दोनों शैलियाँ आम हैं; दूसरी सामान्य क्रमिक कोड की तरह पढ़ी जाती है।

---

future के दोनों पहलू दिमाग में साफ़ रखो:

- एक `async` फ़ंक्शन `Future<T>` **घोषित** करता है और सादा `T` **लौटाता** है: लपेटना अपने आप होता है
- जो कॉलर किसी `Future<T>` का `await` करता है वह सादा `T` **पाता** है: खोलना अपने आप होता है

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

`int count() async` लिखना गलत है: एक `async` फ़ंक्शन को `Future` (या `void`) रिटर्न प्रकार घोषित करना ही होगा।

---

future का उपयोग करने का एकमात्र तरीका `await` नहीं है। तुम **`then`** के साथ एक **कॉलबैक** भी दर्ज कर सकते हो: future पूरा होते ही तुम्हारा दिया हुआ फ़ंक्शन उस मान के साथ बुलाया जाता है। `await` के विपरीत, `then` मौजूदा फ़ंक्शन को रोकता **नहीं** है, इसलिए उसके बाद वाला कोड पहले चलता है:

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

`Future.value` से बना future भी अपना मान तभी देता है जब मौजूदा कोड समाप्त हो चुका हो, इसीलिए `waiting` पहले छपता है। `then` किसी भी फ़ंक्शन में काम करता है, चाहे वह `async` हो या न हो।

---

किसी `async` फ़ंक्शन के अंदर, `await` तुम्हें एसिंक्रोनस चरणों को सामान्य क्रमिक कोड की तरह लिखने देता है। हर `await` अपने future की प्रतीक्षा करता है, और अगली पंक्ति तभी चलती है जब मान आ चुका हो:

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` को सीधे किसी अभिव्यक्ति के भीतर भी इस्तेमाल किया जा सकता है: `return await width() * await height();` वही परिणाम देता है।

---

जब कोई फ़ंक्शन `await` पर पहुँचता है, तो वह उसी पंक्ति पर **रुक** जाता है और बाकी प्रोग्राम चलता रहता है। `await` के बाद वाली पंक्तियाँ तभी चलती हैं जब future पूरा हो जाए। इसलिए किसी `async` फ़ंक्शन को ऊपर से नीचे पढ़ना तुम्हें उसके प्रभावों का सटीक क्रम बता देता है:

```dart
Future<int> load() async {
  await Future.delayed(const Duration(milliseconds: 5));
  return 7;
}

Future<void> main() async {
  print('loading');
  final n = await load();
  print('value: $n');
  print('done');
}
// loading
// value: 7
// done
```

---

कोई future **त्रुटि** के साथ भी पूरा हो सकता है। जब कोई `async` फ़ंक्शन थ्रो करता है, तो अपवाद तुरंत बाहर नहीं निकलता: वह लौटाए गए future की त्रुटि बन जाता है। जो उस future का `await` करता है उसे त्रुटि `await` पर थ्रो होती दिखती है, इसलिए उसे सामान्य `try`/`catch` से संभाला जा सकता है:

```dart
Future<int> parseLater(String s) async {
  await Future.delayed(const Duration(milliseconds: 5));
  return int.parse(s); // throws FormatException for 'abc'
}

Future<int> orZero(String s) async {
  try {
    return await parseLater(s);
  } catch (e) {
    return 0;
  }
}
```

`try` के अंदर का `await` ज़रूरी है: `return parseLater(s);` future को **बिना प्रतीक्षा किए** कॉलर को सौंप देता, इसलिए त्रुटि तब आती जब `try` ब्लॉक पहले ही समाप्त हो चुका होता और `catch` कभी नहीं चलता।

---

त्रुटियाँ कॉल स्टैक से नहीं, future के साथ यात्रा करती हैं। थ्रो करने वाले `async` फ़ंक्शन को कॉल करना अपने आप कभी कॉलर को क्रैश नहीं करता: त्रुटि लौटाए गए future में रखी जाती है और बाद में उसी जगह सामने आती है जहाँ future का await किया जाता है। इसलिए `try`/`catch` को **`await`** के चारों ओर होना चाहिए, उस कॉल के नहीं जिसने future बनाया।

यदि विफल future का कोई कभी await या हैंडल नहीं करता, तो Dart एक *unhandled exception* की सूचना देता है और कमांड-लाइन प्रोग्राम में त्रुटि के साथ बाहर निकल जाता है।

---

कॉलबैक के साथ, त्रुटियाँ **`catchError`** से संभाली जाती हैं, जो `then` की जोड़ीदार है। दोनों एक नया future लौटाते हैं, इसलिए उन्हें आमतौर पर श्रृंखला में जोड़ा जाता है: future सफल हो तो `then` को मान मिलता है, विफल हो तो `catchError` को त्रुटि मिलती है, और दोनों में से केवल एक ही कॉलबैक चलता है:

```dart
Future<String> download() async {
  throw StateError('no network');
}

void main() {
  download()
      .then((data) => print('data: $data'))
      .catchError((e) => print('error: $e'));
  print('requested');
}
// requested
// error: Bad state: no network
```

`then` के बाद रखा गया `catchError` `then` कॉलबैक के अंदर थ्रो हुई त्रुटियाँ भी पकड़ता है। `then` की तरह ही, श्रृंखला के बाद वाला कोड पहले चलता है, क्योंकि कॉलबैक तभी बुलाए जाते हैं जब मौजूदा कोड समाप्त हो चुका हो।

---

जब कई future एक-दूसरे पर निर्भर नहीं होते, तो उन सबको **`Future.wait`** को सौंप दो: यह एक `List<Future<T>>` लेता है, उन्हें एक ही समय पर चलने देता है, और एक अकेला `Future<List<T>>` लौटाता है जो तब पूरा होता है जब **सभी** समाप्त हो जाएँ। परिणाम इनपुट सूची का क्रम बनाए रखते हैं, चाहे कोई भी future पहले समाप्त हुआ हो:

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` में `25` मिलीसेकंड लगते हैं, क्योंकि `fast()` तभी बुलाया जाता है जब `slow()` पूरा हो चुका हो; `await Future.wait([slow(), fast()])` में लगभग `20` लगते हैं, यानी सबसे लंबे वाले की अवधि।

---

`Future.wait` "कई चीज़ें लोड करो, फिर आगे बढ़ो" के लिए औज़ार है। सामान्य ढाँचा यह है: future की सूची बनाओ, उस पर `await Future.wait` करो, फिर मिली हुई सूची का उपयोग करो:

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` पहले पूरा होता है, पर सूची फिर भी कॉल के क्रम का पालन करती है: पहले `stock()`, दूसरा `orders()`।

---

दो future को एक ही समय पर चलाने के लिए तुम्हें `Future.wait` की ज़रूरत नहीं है। कोई `async` फ़ंक्शन **बुलाए** जाते ही अपने पहले `await` तक चलने लगता है; जो future तुम्हें वापस मिलता है वह पहले से चल रहा काम है। इसलिए तरकीब यह है: **पहले बुलाओ, बाद में await करो**:

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

`return await words() / await pages();` से तुलना करो, जहाँ `pages()` तभी बुलाया जाता है जब `words()` पूरा हो चुका हो: परिणाम वही, समय दोगुना। जब भी दूसरी कॉल को पहली के परिणाम की ज़रूरत न हो, समवर्ती रूप को प्राथमिकता दो।

---

कोई त्रुटि हर उस `await` से होकर **फैलती** है जो उसे नहीं पकड़ता। यदि `load()` विफल होता है, तो `loadTwice()` के अंदर `await load()` थ्रो करता है; चूँकि `loadTwice` में `try`/`catch` नहीं है, उसका अपना future भी उसी त्रुटि के साथ विफल हो जाता है; और इसी तरह श्रृंखला में ऊपर तक, जब तक कोई `await` किसी `try`/`catch` में लिपटा न मिले:

```dart
Future<int> load() async {
  throw StateError('offline');
}

Future<int> loadTwice() async {
  final n = await load();   // throws here, loadTwice fails too
  return n * 2;             // never runs
}

Future<void> main() async {
  try {
    print(await loadTwice());
  } catch (e) {
    print('failed: $e');    // failed: Bad state: offline
  }
}
```

यह वैसा ही है जैसे अपवाद सिंक्रोनस कॉल से होकर फैलते हैं: तुम उन्हें एक ही बार संभालते हो, उस स्तर पर जो जानता है कि क्या करना है।

---

`Future.wait` भी यही नियम मानता है: यदि **कोई भी** future विफल होता है, तो संयुक्त future उसी त्रुटि के साथ पूरा होता है और `await Future.wait(...)` थ्रो करता है। तुम्हें सफल मानों की आंशिक सूची कभी नहीं मिलती। बाकी को बचाने के लिए, `Future.wait` को देने से पहले हर अलग future के अंदर ही त्रुटि संभालो, उदाहरण के लिए `catchError` से।

```dart
Future<int> ok() => Future.value(1);
Future<int> bad() async => throw StateError('nope');

Future<void> main() async {
  try {
    await Future.wait([ok(), bad()]);
  } catch (e) {
    print('failed: $e'); // failed: Bad state: nope
  }
}
```

---

चूँकि `await` future की त्रुटियों को सामान्य अपवादों में बदल देता है, `try`/`catch` के सभी सामान्य पैटर्न एसिंक्रोनस कोड पर भी लागू होते हैं, दोबारा कोशिश करने वाले लूप सहित। किसी `catch` ब्लॉक के अंदर **`rethrow`** उसी त्रुटि को फिर से थ्रो करता है, और इसी तरह तुम आख़िरी कोशिश के बाद हार मानते हो:

```dart
Future<String> onceThenGiveUp(Future<String> Function() task) async {
  try {
    return await task();
  } catch (e) {
    print('first attempt failed');
    rethrow; // the caller sees the original error
  }
}
```

`Future<String> Function() task` जैसा फ़ंक्शन-प्रकार का पैरामीटर स्वयं **फ़ंक्शन** पाता है, कोई future नहीं: `task()` की हर कॉल एक नई कोशिश शुरू करती है।
