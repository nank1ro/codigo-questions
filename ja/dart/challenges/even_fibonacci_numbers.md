---
language: dart
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

フィボナッチ数列の各新しい項は、前の 2 つの項を足すことで生成されます。1 と 2 から始めると、最初の 10 項は次のようになります: 1、2、3、5、8、13、21、34、55、89、...

# --instructions--

`n` を超えないフィボナッチ数列のすべての偶数項の合計を返す関数を書いてください。

関数呼び出しの例:
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

8 を超えない偶数フィボナッチ項の合計は 10 と等しくなければならない

```dart
  test('test1', () {
    expect(fibonacciEvenSum(8), 10, reason: '--err-t1--');
  });
```

10 を超えない偶数フィボナッチ項の合計は 10 と等しくなければならない

```dart
  test('test2', () {
    expect(fibonacciEvenSum(10), 10, reason: '--err-t2--');
  });
```

34 を超えない偶数フィボナッチ項の合計は 44 と等しくなければならない

```dart
  test('test3', () {
    expect(fibonacciEvenSum(34), 44, reason: '--err-t3--');
  });
```

1000 を超えない偶数フィボナッチ項の合計は 798 と等しくなければならない

```dart
  test('test4', () {
    expect(fibonacciEvenSum(1000), 798, reason: '--err-t4--');
  });
```

4000000 を超えない偶数フィボナッチ項の合計は 4613732 と等しくなければならない

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
