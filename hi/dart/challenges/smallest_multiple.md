---
language: dart
exerciseType: 1
difficulty: 2
title: Smallest multiple
---

# --description--

2520 सबसे छोटी संख्या है जिसे 1 से 10 तक की प्रत्येक संख्या से बिना शेष के विभाजित किया जा सकता है।

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो सबसे छोटी धनात्मक संख्या लौटाता है जो 1 से `n` तक की सभी संख्याओं से पूरी तरह विभाज्य हो।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(smallestMultiple(10));
// prints 2520
```

# --seed--

```dart
int smallestMultiple(int n) {

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

1 से 5 तक का सबसे छोटा गुणज 60 के बराबर होना चाहिए

```dart
  test('test1', () {
    expect(smallestMultiple(5), 60, reason: '--err-t1--');
  });
```

1 से 10 तक का सबसे छोटा गुणज 2520 के बराबर होना चाहिए

```dart
  test('test2', () {
    expect(smallestMultiple(10), 2520, reason: '--err-t2--');
  });
```

1 से 20 तक का सबसे छोटा गुणज 232792560 के बराबर होना चाहिए

```dart
  test('test3', () {
    expect(smallestMultiple(20), 232792560, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int _gcd(int a, int b) => b == 0 ? a : _gcd(b, a % b);

int _lcm(int a, int b) => a ~/ _gcd(a, b) * b;

int smallestMultiple(int n) {
  int result = 1;
  for (int i = 2; i <= n; i++) {
    result = _lcm(result, i);
  }
  return result;
}
```
