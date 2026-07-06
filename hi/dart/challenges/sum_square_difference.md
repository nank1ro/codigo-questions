---
language: dart
exerciseType: 1
difficulty: 1
title: Sum square difference
---

# --description--

पहले दस प्राकृतिक संख्याओं के वर्गों का योग 1² + 2² + ... + 10² = 385 है।

पहले दस प्राकृतिक संख्याओं के योग का वर्ग (1 + 2 + ... + 10)² = 55² = 3025 है।

1 से 10 तक के वर्गों के योग और योग के वर्ग के बीच का अंतर 3025 − 385 = 2640 है।

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो पहले `n` प्राकृतिक संख्याओं के योग के वर्ग और वर्गों के योग के बीच का अंतर लौटाता है।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(sumSquareDifference(10));
// prints 2640
```

# --seed--

```dart
int sumSquareDifference(int n) {

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

n=10 के लिए योग-वर्ग अंतर 2640 के बराबर होना चाहिए

```dart
  test('test1', () {
    expect(sumSquareDifference(10), 2640, reason: '--err-t1--');
  });
```

n=20 के लिए योग-वर्ग अंतर 41230 के बराबर होना चाहिए

```dart
  test('test2', () {
    expect(sumSquareDifference(20), 41230, reason: '--err-t2--');
  });
```

n=100 के लिए योग-वर्ग अंतर 25164150 के बराबर होना चाहिए

```dart
  test('test3', () {
    expect(sumSquareDifference(100), 25164150, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumSquareDifference(int n) {
  int sumOfSquares = 0;
  int sum = 0;
  for (int i = 1; i <= n; i++) {
    sumOfSquares += i * i;
    sum += i;
  }
  return sum * sum - sumOfSquares;
}
```
