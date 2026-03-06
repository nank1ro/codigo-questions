---
language: dart
exerciseType: 1
difficulty: 1
title: 足し算
---

# --description--

2つの整数`num1`と`num2`が与えられた場合、これら2つの数を足すプログラムを書いてください。

# --instructions--

2つの数の合計を返す関数を書いてください。

関数呼び出しの例：
```dart
print(addition(1, 2));
// prints 3
```

# --seed--

```dart
int addition() {
  
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

1と3の合計は4に等しくなければならない

```dart
  test('test1', () {
    expect(addition(1, 3), 4, reason: '--err-t1--');
  });
```

200と210の合計は410に等しくなければならない

```dart
  test('test2', () {
    expect(addition(200, 210), 410, reason: '--err-t2--');
  });
```

15と35の合計は50に等しくなければならない

```dart
  test('test3', () {
    expect(addition(15, 35), 50, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int addition(int num1, int num2) {
  return num1 + num2;
}
```
