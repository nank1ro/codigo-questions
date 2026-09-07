---
language: dart
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

피보나치 수열의 각 새로운 항은 이전 두 항을 더해서 생성됩니다. 1과 2로 시작하면 처음 10항은 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...입니다.

# --instructions--

`n`을 초과하지 않는 피보나치 수열의 모든 짝수 항의 합을 반환하는 함수를 작성하세요.

함수 호출 예시:
```dart
print(fibonacciEvenSum(8));
// prints 10
```

# --seed--

```dart
int fibonacciEvenSum(int n) {

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

8을 초과하지 않는 짝수 피보나치 항의 합은 10과 같아야 한다

```dart
  test('test1', () {
    expect(fibonacciEvenSum(8), 10, reason: '--err-t1--');
  });
```

10을 초과하지 않는 짝수 피보나치 항의 합은 10과 같아야 한다

```dart
  test('test2', () {
    expect(fibonacciEvenSum(10), 10, reason: '--err-t2--');
  });
```

34를 초과하지 않는 짝수 피보나치 항의 합은 44와 같아야 한다

```dart
  test('test3', () {
    expect(fibonacciEvenSum(34), 44, reason: '--err-t3--');
  });
```

1000을 초과하지 않는 짝수 피보나치 항의 합은 798과 같아야 한다

```dart
  test('test4', () {
    expect(fibonacciEvenSum(1000), 798, reason: '--err-t4--');
  });
```

4000000을 초과하지 않는 짝수 피보나치 항의 합은 4613732와 같아야 한다

```dart
  test('test5', () {
    expect(fibonacciEvenSum(4000000), 4613732, reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int fibonacciEvenSum(int n) {
  int sum = 0;
  int a = 1, b = 2;
  while (a <= n) {
    if (a % 2 == 0) {
      sum += a;
    }
    int temp = a + b;
    a = b;
    b = temp;
  }
  return sum;
}
```
