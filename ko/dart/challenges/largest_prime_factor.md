---
language: dart
exerciseType: 1
difficulty: 2
title: Largest prime factor
---

# --description--

13195의 소인수는 5, 7, 13, 29입니다.

# --instructions--

`number`의 가장 큰 소인수를 반환하는 함수를 작성하세요.

함수 호출 예시:
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

2의 가장 큰 소인수는 2와 같아야 한다

```dart
  test('test1', () {
    expect(largestPrimeFactor(2), 2, reason: '--err-t1--');
  });
```

3의 가장 큰 소인수는 3과 같아야 한다

```dart
  test('test2', () {
    expect(largestPrimeFactor(3), 3, reason: '--err-t2--');
  });
```

13195의 가장 큰 소인수는 29와 같아야 한다

```dart
  test('test3', () {
    expect(largestPrimeFactor(13195), 29, reason: '--err-t3--');
  });
```

600851475143의 가장 큰 소인수는 6857과 같아야 한다

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
