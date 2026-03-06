---
language: dart
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

数値を引数として受け取り、`"Fizz"`、`"Buzz"`、または`"FizzBuzz"`を返す関数を作成してください。

# --instructions--

- 数値が`3`の倍数の場合、出力は`"Fizz"`になります。
- 与えられた数値が`5`の倍数の場合、出力は`"Buzz"`になります。
- 与えられた数値が`3`と`5`の両方の倍数の場合、出力は`"FizzBuzz"`になります。
- 数値が`3`にも`5`にも倍数でない場合、以下の例に示すように数値そのものを出力します。
- 出力は`3`や`5`の倍数でない場合でも、常に文字列である必要があります。

例：
```dart
fizz_buzz(3); // ➞ "Fizz"
fizz_buzz(5); // ➞ "Buzz"
fizz_buzz(15); // ➞ "FizzBuzz"
fizz_buzz(4); // ➞ "4"
```

# --seed--

```dart
String fizzBuzz() {
  
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

数値`3`は`"Fizz"`に等しくなければならない

```dart
  test('test1', () {
    expect(fizzBuzz(3), 'Fizz', reason: '--err-t1--');
  });
```

数値`5`は`"Buzz"`に等しくなければならない

```dart
  test('test2', () {
    expect(fizzBuzz(5), 'Buzz', reason: '--err-t2--');
  });
```

数値`15`は`"FizzBuzz"`に等しくなければならない

```dart
  test('test3', () {
    expect(fizzBuzz(15), 'FizzBuzz', reason: '--err-t3--');
  });
```

数値`10`は`"Buzz"`に等しくなければならない

```dart
  test('test4', () {
    expect(fizzBuzz(10), 'Buzz', reason: '--err-t4--');
  });
```

数値`98`は`"98"`に等しくなければならない

```dart
  test('test5', () {
    expect(fizzBuzz(98), '98', reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String fizzBuzz(int number) {
  if (number % 3 == 0 && number % 5 == 0) {
    return 'FizzBuzz';
  }
  if (number % 3 == 0) {
    return 'Fizz';
  }
  if (number % 5 == 0) {
    return 'Buzz';
  }
  return number.toString();
}
```
