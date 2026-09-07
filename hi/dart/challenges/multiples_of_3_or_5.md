---
language: dart
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

यदि हम 10 से नीचे के सभी प्राकृतिक संख्याओं को सूचीबद्ध करें जो 3 या 5 के गुणज हैं, तो हमें 3, 5, 6 और 9 मिलते हैं। इन गुणजों का योग 23 है।

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो `number` से नीचे 3 या 5 के सभी गुणजों का योग लौटाता है।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(multiplesOf3And5(10));
// prints 23
```

# --seed--

```dart
int multiplesOf3And5(int number) {

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

10 से नीचे 3 या 5 के गुणजों का योग 23 के बराबर होना चाहिए

```dart
  test('test1', () {
    expect(multiplesOf3And5(10), 23, reason: '--err-t1--');
  });
```

1000 से नीचे 3 या 5 के गुणजों का योग 233168 के बराबर होना चाहिए

```dart
  test('test2', () {
    expect(multiplesOf3And5(1000), 233168, reason: '--err-t2--');
  });
```

6987 से नीचे 3 या 5 के गुणजों का योग 11390208 के बराबर होना चाहिए

```dart
  test('test3', () {
    expect(multiplesOf3And5(6987), 11390208, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int multiplesOf3And5(int number) {
  int sum = 0;
  for (int i = 1; i < number; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      sum += i;
    }
  }
  return sum;
}
```
