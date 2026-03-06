---
language: dart
exerciseType: 1
difficulty: 1
title: जोड़
---

# --description--

दो पूर्णांक `num1` और `num2` दिए गए हैं, इन दो संख्याओं को जोड़ने के लिए एक प्रोग्राम लिखें

# --instructions--

एक फ़ंक्शन लिखें जो दो संख्याओं का योग लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(addition(1, 2));
// prints 3
```

# --seed--

```dart
int addition() {
  
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

1 और 3 का योग 4 के बराबर होना चाहिए

```dart
  test('test1', () {
    expect(addition(1, 3), 4, reason: '--err-t1--');
  });
```

200 और 210 का योग 410 के बराबर होना चाहिए

```dart
  test('test2', () {
    expect(addition(200, 210), 410, reason: '--err-t2--');
  });
```

15 और 35 का योग 50 के बराबर होना चाहिए

```dart
  test('test3', () {
    expect(addition(15, 35), 50, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int addition(int num1, int num2) {
  return num1 + num2;
}
```
