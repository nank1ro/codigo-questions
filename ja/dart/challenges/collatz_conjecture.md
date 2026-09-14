---
language: dart
exerciseType: 1
difficulty: 1
title: コラッツの予想
---

# --description--

コラッツの予想は、任意の正の整数`n`から始めて、1つの単純な規則を繰り返します。`n`が偶数ならそれを半分にし、`n`が奇数なら`3n + 1`で置き換えます。いずれ数列は1に到達します。

例えば、16から始めると数列は`16 -> 8 -> 4 -> 2 -> 1`となり、4ステップかかります。

これが常に起こると証明した人はまだいませんが、これまでテストされたすべての数で成り立っています。

# --instructions--

正の整数`n`を受け取り、1に到達するまでに必要なステップ数を返す関数`collatzSteps`を書いてください。

`collatzSteps(1)`は0になります。1はすでに数列の終わりだからです。`collatzSteps(12)`は9、`collatzSteps(27)`は111です。

関数呼び出しの例：
```dart
print(collatzSteps(16));
// prints 4
```

# --seed--

```dart
int collatzSteps(int n) {

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

`collatzSteps(1)`は、1がすでに数列の終わりであるため、0を返すべきです。

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)`は1を返すべきです。

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)`は8を返すべきです。

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)`は16を返すべきです。

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)`は4を返すべきです。

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)`は9を返すべきです。

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)`は111を返すべきです。

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)`は118を返すべきです。

```dart
    test('test8', () {
      expect(collatzSteps(97), 118, reason: '--err-t8--');
    });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int collatzSteps(int n) {
  int value = n;
  int steps = 0;
  while (value != 1) {
    value = value % 2 == 0 ? value ~/ 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
