---
language: dart
exerciseType: 1
difficulty: 1
title: 算術平均
---

# --description--

数値ベクトルの_算術平均_を求める`mean`という関数を書いてください。

# --instructions--

数値ベクトルの平均を返す関数を書いてください。

関数呼び出しの例：
```dart
print(mean([1, 2, 3]));
// prints 2.0
```

# --seed--

```dart
num mean() {
  
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

`[1, 2, 3, 4, 5, 6, 7]`の平均は4.0に等しくなければならない

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

`[4, 5, 6]`の平均は5.0に等しくなければならない

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

`[12, 34, 56, 78]`の平均は45.0に等しくなければならない

```dart
  test('test3', () {
    expect(mean([12, 34, 56, 78]), 45.0, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
num mean(List<num> numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
