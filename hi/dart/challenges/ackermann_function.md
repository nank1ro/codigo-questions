---
language: dart
exerciseType: 1
difficulty: 1
title: एकरमैन फ़ंक्शन
---

# --description--

एकरमैन फ़ंक्शन एक रिकर्सिव फ़ंक्शन का एक उत्कृष्ट उदाहरण है, जो विशेष रूप से इसलिए उल्लेखनीय है क्योंकि यह एक प्रिमिटिव रिकर्सिव फ़ंक्शन नहीं है। इसका मान बहुत तेज़ी से बढ़ता है, जैसा कि इसके कॉल ट्री का आकार भी बढ़ता है।

एकरमैन फ़ंक्शन को आमतौर पर इस प्रकार परिभाषित किया जाता है:

![ackermann_function](https://bit.ly/3z9u4zh)

इसके तर्क कभी ऋणात्मक नहीं होते और यह हमेशा समाप्त होता है

# --instructions--

एक फ़ंक्शन लिखें जो एकरमैन फ़ंक्शन का मान लौटाए।

# --seed--

```dart
int ack(int m, int n) {
    
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

`ack(0, 0)` को 1 लौटाना चाहिए।

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)` को 3 लौटाना चाहिए।

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)` को 13 लौटाना चाहिए।

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)` को 61 लौटाना चाहिए।

```dart
    test('test4', () {
      expect(ack(3, 3), 61, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int ack(int m, int n) {
  if (m == 0) return n + 1;
  return ack(
    m - 1,
    (n == 0) ? 1 : ack(m, n - 1),
  );
}
```
