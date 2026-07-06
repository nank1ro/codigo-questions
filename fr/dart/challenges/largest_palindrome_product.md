---
language: dart
exerciseType: 1
difficulty: 2
title: Largest palindrome product
---

# --description--

Un nombre palindromique se lit de la même façon dans les deux sens. Le plus grand palindrome formé par le produit de deux nombres à 2 chiffres est 9009 = 91 × 99.

# --instructions--

Écris une fonction qui retourne le plus grand palindrome formé par le produit de deux nombres à `n` chiffres.

Exemple d'appel de fonction :
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

Le plus grand produit palindromique de deux nombres à 2 chiffres doit être égal à 9009

```dart
  test('test1', () {
    expect(largestPalindromeProduct(2), 9009, reason: '--err-t1--');
  });
```

Le plus grand produit palindromique de deux nombres à 3 chiffres doit être égal à 906609

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
