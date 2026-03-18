---
language: dart
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

回文数とは、前から読んでも後ろから読んでも同じになる数です。2 桁の数字 2 つの積で作られる最大の回文数は 9009 = 91 × 99 です。

# --instructions--

`n` 桁の数字 2 つの積で作られる最大の回文数を返す関数を書いてください。

関数呼び出しの例:
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

2 桁の数字 2 つの最大回文積は 9009 と等しくなければならない

```dart
  test('test1', () {
    expect(largestPalindromeProduct(2), 9009, reason: '--err-t1--');
  });
```

3 桁の数字 2 つの最大回文積は 906609 と等しくなければならない

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
