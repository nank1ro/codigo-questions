---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

毕达哥拉斯三元组是满足 a < b < c 且 a² + b² = c² 的三个自然数的集合。

例如，3² + 4² = 9 + 16 = 25 = 5²。恰好存在一个满足 a + b + c = 1000 的毕达哥拉斯三元组。

# --instructions--

编写一个函数，找出 a + b + c 等于 `n` 的毕达哥拉斯三元组，并返回乘积 a × b × c。

函数调用示例：
```dart
print(specialPythagoreanTriplet(12));
// prints 60
```

# --seed--

```dart
int specialPythagoreanTriplet(int n) {

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

满足a+b+c=12的毕达哥拉斯三元组的乘积必须等于60

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

满足a+b+c=1000的毕达哥拉斯三元组的乘积必须等于31875000

```dart
  test('test2', () {
    expect(specialPythagoreanTriplet(1000), 31875000, reason: '--err-t2--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int specialPythagoreanTriplet(int n) {
  for (int a = 1; a < n; a++) {
    for (int b = a + 1; b < n - a; b++) {
      int c = n - a - b;
      if (c > b && a * a + b * b == c * c) {
        return a * b * c;
      }
    }
  }
  return -1;
}
```
