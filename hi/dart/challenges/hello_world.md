---
language: dart
exerciseType: 1
difficulty: 1
title: हैलो वर्ल्ड!
---

# --description--

__"Hello, World!"__ एक नई भाषा या वातावरण में प्रोग्रामिंग शुरू करने के लिए पारंपरिक पहला प्रोग्राम है।

# --instructions--

एक फ़ंक्शन लिखें जो स्ट्रिंग "Hello, World!" लौटाए।

# --seed--

```dart
String hello() {

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

फ़ंक्शन को "Hello, World!" लौटाना चाहिए।

```dart
  const expected = "Hello, World!";
  test('test1', () {
    expect(hello(), expected, reason: '--err-t1--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String hello() {
  return "Hello, World!";
}
```

