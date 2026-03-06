---
language: dart
exerciseType: 1
difficulty: 1
title: अंकगणितीय माध्य
---

# --description--

एक संख्यात्मक वेक्टर का _अंकगणितीय औसत_ ज्ञात करने के लिए `mean` नामक एक फ़ंक्शन लिखें।

# --instructions--

एक फ़ंक्शन लिखें जो एक संख्यात्मक वेक्टर का माध्य लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(mean([1, 2, 3]));
// prints 2.0
```

# --seed--

```dart
num mean() {
  
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

`[1, 2, 3, 4, 5, 6, 7]` का माध्य 4.0 के बराबर होना चाहिए

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

`[4, 5, 6]` का माध्य 5.0 के बराबर होना चाहिए

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

`[12, 34, 56, 78]` का माध्य 45.0 के बराबर होना चाहिए

```dart
  test('test3', () {
    expect(mean([12, 34, 56, 78]), 45.0, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
num mean(List<num> numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
