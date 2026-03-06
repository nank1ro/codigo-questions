---
language: dart
exerciseType: 1
difficulty: 1
title: アッカーマン関数
---

# --description--

アッカーマン関数は再帰関数の古典的な例であり、特に原始再帰関数ではないことで知られています。その値は非常に急速に増加し、呼び出しツリーのサイズも同様です。

アッカーマン関数は通常、次のように定義されます：

![ackermann_function](https://bit.ly/3z9u4zh)

引数は決して負にならず、常に終了します。

# --instructions--

アッカーマン関数の値を返す関数を書いてください。

# --seed--

```dart
int ack(int m, int n) {
    
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

`ack(0, 0)`は1を返す必要があります。

```dart
    test('test1', () {
      expect(ack(0, 0), 1, reason: '--err-t1--');
    });
```

`ack(1, 1)`は3を返す必要があります。

```dart
    test('test2', () {
      expect(ack(1, 1), 3, reason: '--err-t2--');
    });
```

`ack(2, 5)`は13を返す必要があります。

```dart
    test('test3', () {
      expect(ack(2, 5), 13, reason: '--err-t3--');
    });
```

`ack(3, 3)`は61を返す必要があります。

```dart
    test('test4', () {
      expect(ack(3, 3), 61, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int ack(int m, int n) {
  if (m == 0) return n + 1;
  return ack(
    m - 1,
    (n == 0) ? 1 : ack(m, n - 1),
  );
}
```
