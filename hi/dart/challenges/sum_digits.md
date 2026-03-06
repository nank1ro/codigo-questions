---
language: dart
exerciseType: 1
difficulty: 1
title: अंकों का योग
---

# --description--

आपको एक पूर्णांक `N` दिया गया है।
N के सभी अंकों का योग गणना करने के लिए एक प्रोग्राम लिखें

# --instructions--

`N` के अंकों का योग लौटाएं।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(sumDigits(28))
// prints 10
```

# --seed--

```dart
int sumDigits() {

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

12345 के अंकों का योग 15 है

```dart
  test('test1', () {
    expect(sumDigits(12345), 15, reason: '--err-t1--');
  });
```

57253 के अंकों का योग 22 है

```dart
  test('test2', () {
    expect(sumDigits(57253), 22, reason: '--err-t2--');
  });
```

122 के अंकों का योग 5 है

```dart
  test('test3', () {
    expect(sumDigits(122), 5, reason: '--err-t3--');
  });
```

91979997 के अंकों का योग 60 है

```dart
  test('test4', () {
    expect(sumDigits(91979997), 60, reason: '--err-t4--');
  });
```

2147483647 के अंकों का योग 46 है

```dart
  test('test5', () {
    expect(sumDigits(2147483647), 46, reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumDigits(int number) {
  var n = number;
  var result = 0;
  while (n > 0) {
    result += n % 10;
    n = n ~/ 10;
  }
  return result;
}
```

