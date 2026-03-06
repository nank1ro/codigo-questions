---
language: dart
exerciseType: 1
difficulty: 3
title: रोमन अंक परिवर्तक
---

# --description--

एक फ़ंक्शन बनाएं जो एक धनात्मक पूर्णांक को अपने पैरामीटर के रूप में लेता है और उस पूर्णांक के रोमन अंक प्रतिनिधित्व वाली एक स्ट्रिंग लौटाता है। आधुनिक रोमन अंक प्रत्येक अंक को अलग-अलग व्यक्त करके लिखे जाते हैं, सबसे बाएं अंक से शुरू करते हुए और शून्य मान वाले किसी भी अंक को छोड़ते हुए।

# --instructions--

उदाहरण:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- सभी रोमन अंक अपरकेस में लौटाए जाने चाहिए।
- इस संकेतन में प्रदर्शित की जा सकने वाली सबसे बड़ी संख्या 3,999 है।

# --seed--

```dart
String convertToRoman(int n) {
  
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

संख्या `2` `II` के बराबर होनी चाहिए

```dart
  test('test1', () {
    expect(convertToRoman(2), 'II', reason: '--err-t1--');
  });
```

संख्या `12` `XII` के बराबर होनी चाहिए

```dart
  test('test2', () {
    expect(convertToRoman(12), 'XII', reason: '--err-t2--');
  });
```

संख्या `16` `XVI` के बराबर होनी चाहिए

```dart
  test('test3', () {
    expect(convertToRoman(16), 'XVI', reason: '--err-t3--');
  });
```

संख्या `44` `XLIV` के बराबर होनी चाहिए

```dart
  test('test4', () {
    expect(convertToRoman(44), 'XLIV', reason: '--err-t4--');
  });
```

संख्या `68` `LXVIII` के बराबर होनी चाहिए

```dart
  test('test5', () {
    expect(convertToRoman(68), 'LXVIII', reason: '--err-t5--');
  });
```

संख्या `400` `CD` के बराबर होनी चाहिए

```dart
  test('test6', () {
    expect(convertToRoman(400), 'CD', reason: '--err-t6--');
  });
```

संख्या `798` `DCCXCVIII` के बराबर होनी चाहिए

```dart
  test('test7', () {
    expect(convertToRoman(798), 'DCCXCVIII', reason: '--err-t7--');
  });
```

संख्या `1000` `M` के बराबर होनी चाहिए

```dart
  test('test8', () {
    expect(convertToRoman(1000), 'M', reason: '--err-t8--');
  });
```

संख्या `3999` `MMMCMXCIX` के बराबर होनी चाहिए

```dart
  test('test9', () {
    expect(convertToRoman(3999), 'MMMCMXCIX', reason: '--err-t9--');
  });
```

संख्या `649` `DCXLIX` के बराबर होनी चाहिए

```dart
  test('test10', () {
    expect(convertToRoman(649), 'DCXLIX', reason: '--err-t10--');
  });
```

संख्या `1666` `MDCLXVI` के बराबर होनी चाहिए

```dart
  test('test11', () {
    expect(convertToRoman(1666), 'MDCLXVI', reason: '--err-t11--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String convertToRoman(int n) {
  var result = "";

  final values = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
  ];

  for (var i = 0; i < values.length; i++) {
    final value = values[i].$1;
    final letter = values[i].$2;

    while (n >= value) {
      result += letter;
      n -= value;
    }
  }
}
```
