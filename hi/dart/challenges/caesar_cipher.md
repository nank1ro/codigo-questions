---
language: dart
exerciseType: 1
difficulty: 2
title: सीज़र सिफर
---

# --description--

जूलियस सीज़र ने क्रिप्टोग्राफी की सबसे पुरानी तरकीबों में से एक से अपनी निजी चिट्ठियों को सुरक्षित रखा था: वे किसी संदेश के हर अक्षर को वर्णमाला में एक निश्चित संख्या में आगे स्थित अक्षर से बदल देते थे। 3 के शिफ्ट पर `a`, `d` बन जाता है, `b`, `e` बन जाता है और `c`, `f` बन जाता है।

वर्णमाला एक वृत्त जैसा व्यवहार करती है, इसलिए अंत के अक्षर घूमकर वापस शुरुआत पर पहुँच जाते हैं: 3 के शिफ्ट पर `x`, `a` बन जाता है, `y`, `b` बन जाता है और `z`, `c` बन जाता है।

जो कुछ भी अक्षर नहीं है, जैसे रिक्त स्थान, अल्पविराम, विस्मयादिबोधक चिह्न या अंक, वह सिफर से बिना बदले गुज़र जाता है।

# --instructions--

एक फ़ंक्शन `caesarCipher` लिखें जो एक संदेश `text` और एक पूर्ण संख्या `shift` लेता है, और एन्कोड किया हुआ संदेश लौटाता है।

उदाहरण:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- संदेश हमेशा लोअरकेस में होता है, इसलिए आपको कभी भी अपरकेस अक्षरों से निपटना नहीं पड़ेगा।
- जो वर्ण अक्षर नहीं हैं, वे अपनी जगह और अपना मान बनाए रखते हैं।
- शिफ्ट कभी ऋणात्मक नहीं होता। `0` का शिफ्ट संदेश को अपरिवर्तित छोड़ देता है, और `26` का शिफ्ट भी ऐसा ही करता है।

# --seed--

```dart
String caesarCipher(String text, int shift) {
  
}
```

# --before-asserts--

```dart
import 'package:dart_runner/main.dart';
import 'package:test/test.dart';

void main() {
  group('MainTest -', () {
```

# --asserts--

3 का शिफ्ट "hello" को "khoor" में बदल देता है

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

वर्णमाला का अंत घूमकर शुरुआत पर वापस आ जाता है, इसलिए "xyz", "abc" बन जाता है

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

0 का शिफ्ट संदेश को अपरिवर्तित छोड़ देता है

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

26 का शिफ्ट वर्णमाला का एक पूरा चक्र है, इसलिए संदेश अपरिवर्तित रहता है

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

विराम चिह्न और रिक्त स्थान बिना बदले गुज़र जाते हैं

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

खाली संदेश खाली ही रहता है

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

अक्षरों के बीच के रिक्त स्थान बने रहते हैं

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

25 के शिफ्ट पर भी अंक शिफ्ट नहीं होते

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

13 का शिफ्ट एक पूरे वाक्य को एन्कोड कर देता है

```dart
  test('test9', () {
    expect(caesarCipher('the quick brown fox jumps over the lazy dog', 13), 'gur dhvpx oebja sbk whzcf bire gur ynml qbt', reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String caesarCipher(String text, int shift) {
  final a = 'a'.codeUnitAt(0);
  final z = 'z'.codeUnitAt(0);
  final encoded = <int>[];

  for (final code in text.codeUnits) {
    if (code >= a && code <= z) {
      encoded.add(a + (code - a + shift) % 26);
    } else {
      encoded.add(code);
    }
  }

  return String.fromCharCodes(encoded);
}
```
