---
language: dart
exerciseType: 1
difficulty: 1
title: 数字の合計
---

# --description--

整数`N`が与えられます。
Nのすべての桁の合計を計算するプログラムを書いてください。

# --instructions--

`N`の各桁の合計を返してください。

関数呼び出しの例：
```dart
print(sumDigits(28))
// prints 10
```

# --seed--

```dart
int sumDigits() {

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

12345の各桁の合計は15

```dart
  test('test1', () {
    expect(sumDigits(12345), 15, reason: '--err-t1--');
  });
```

57253の各桁の合計は22

```dart
  test('test2', () {
    expect(sumDigits(57253), 22, reason: '--err-t2--');
  });
```

122の各桁の合計は5

```dart
  test('test3', () {
    expect(sumDigits(122), 5, reason: '--err-t3--');
  });
```

91979997の各桁の合計は60

```dart
  test('test4', () {
    expect(sumDigits(91979997), 60, reason: '--err-t4--');
  });
```

2147483647の各桁の合計は46

```dart
  test('test5', () {
    expect(sumDigits(2147483647), 46, reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int sumDigits(int number) {
  var n = number;
  var result = 0;
  while (n > 0) {
    result += n % 10;
    n = n ~/ 10;
  }
  return result;
}
```

