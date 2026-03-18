---
language: dart
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

회문수는 앞뒤로 읽어도 동일한 숫자입니다. 두 자리 숫자 두 개의 곱으로 만들어지는 가장 큰 회문수는 9009 = 91 × 99입니다.

# --instructions--

`n`자리 숫자 두 개의 곱으로 만들어지는 가장 큰 회문수를 반환하는 함수를 작성하세요.

함수 호출 예시:
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

두 2자리 숫자의 가장 큰 회문 곱은 9009와 같아야 한다

```dart
  test('test1', () {
    expect(largestPalindromeProduct(2), 9009, reason: '--err-t1--');
  });
```

두 3자리 숫자의 가장 큰 회문 곱은 906609와 같아야 한다

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
