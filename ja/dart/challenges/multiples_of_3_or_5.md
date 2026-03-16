---
language: dart
exerciseType: 1
difficulty: 1
title: Multiples of 3 or 5
---

# --description--

10 未満の自然数のうち、3 または 5 の倍数をすべて列挙すると 3、5、6、9 になります。これらの倍数の合計は 23 です。

# --instructions--

`number` 未満の 3 または 5 のすべての倍数の合計を返す関数を書いてください。

関数呼び出しの例:
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

10 未満の 3 または 5 の倍数の合計は 23 と等しくなければならない

```dart
  test('test1', () {
    expect(multiplesOf3And5(10), 23, reason: '--err-t1--');
  });
```

1000 未満の 3 または 5 の倍数の合計は 233168 と等しくなければならない

```dart
  test('test2', () {
    expect(multiplesOf3And5(1000), 233168, reason: '--err-t2--');
  });
```

6987 未満の 3 または 5 の倍数の合計は 11390208 と等しくなければならない

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
