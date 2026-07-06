---
language: dart
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

13195 के अभाज्य गुणनखंड 5, 7, 13 और 29 हैं।

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो `number` का सबसे बड़ा अभाज्य गुणनखंड लौटाता है।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(largestPrimeFactor(13195));
// prints 29
```

# --seed--

```dart
int largestPrimeFactor(int number) {

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

2 का सबसे बड़ा अभाज्य गुणनखंड 2 के बराबर होना चाहिए

```dart
  test('test1', () {
    expect(largestPrimeFactor(2), 2, reason: '--err-t1--');
  });
```

3 का सबसे बड़ा अभाज्य गुणनखंड 3 के बराबर होना चाहिए

```dart
  test('test2', () {
    expect(largestPrimeFactor(3), 3, reason: '--err-t2--');
  });
```

13195 का सबसे बड़ा अभाज्य गुणनखंड 29 के बराबर होना चाहिए

```dart
  test('test3', () {
    expect(largestPrimeFactor(13195), 29, reason: '--err-t3--');
  });
```

600851475143 का सबसे बड़ा अभाज्य गुणनखंड 6857 के बराबर होना चाहिए

```dart
  test('test4', () {
    expect(largestPrimeFactor(600851475143), 6857, reason: '--err-t4--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int largestPrimeFactor(int number) {
  int largest = 1;
  int n = number;
  int factor = 2;
  while (factor * factor <= n) {
    while (n % factor == 0) {
      largest = factor;
      n ~/= factor;
    }
    factor++;
  }
  if (n > 1) {
    largest = n;
  }
  return largest;
}
```
