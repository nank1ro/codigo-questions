---
language: dart
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Палиндромное число читается одинаково в обоих направлениях. Наибольший палиндром, являющийся произведением двух 2-значных чисел, — это 9009 = 91 × 99.

# --instructions--

Напишите функцию, которая возвращает наибольший палиндром, являющийся произведением двух `n`-значных чисел.

Пример вызова функции:
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

Наибольшее палиндромное произведение двух 2-значных чисел должно быть равно 9009

```dart
  test('test1', () {
    expect(largestPalindromeProduct(2), 9009, reason: '--err-t1--');
  });
```

Наибольшее палиндромное произведение двух 3-значных чисел должно быть равно 906609

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
