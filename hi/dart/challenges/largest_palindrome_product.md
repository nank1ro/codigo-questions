---
language: dart
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

एक पैलिंड्रोम संख्या दोनों दिशाओं में एक समान पढ़ी जाती है। दो 2-अंकीय संख्याओं के गुणनफल से बनने वाला सबसे बड़ा पैलिंड्रोम 9009 = 91 × 99 है।

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो दो `n`-अंकीय संख्याओं के गुणनफल से बनने वाला सबसे बड़ा पैलिंड्रोम लौटाता है।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(largestPalindromeProduct(2));
// prints 9009
```

# --seed--

```dart
int largestPalindromeProduct(int n) {

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

दो 2-अंकीय संख्याओं का सबसे बड़ा पैलिंड्रोम गुणनफल 9009 के बराबर होना चाहिए

```dart
  test('test1', () {
    expect(largestPalindromeProduct(2), 9009, reason: '--err-t1--');
  });
```

दो 3-अंकीय संख्याओं का सबसे बड़ा पैलिंड्रोम गुणनफल 906609 के बराबर होना चाहिए

```dart
  test('test2', () {
    expect(largestPalindromeProduct(3), 906609, reason: '--err-t2--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool _isPalindrome(int n) {
  String s = n.toString();
  return s == s.split('').reversed.join();
}

int largestPalindromeProduct(int n) {
  int upper = 1;
  for (int i = 0; i < n; i++) upper *= 10;
  int lower = upper ~/ 10;

  int largest = 0;
  for (int i = upper - 1; i >= lower; i--) {
    if (i * i < largest) break;
    for (int j = i; j >= lower; j--) {
      int product = i * j;
      if (product < largest) break;
      if (_isPalindrome(product)) {
        largest = product;
      }
    }
  }
  return largest;
}
```
