---
language: dart
exerciseType: 1
difficulty: 1
title: 二换一
---

# --description--

给定一个名字，返回包含以下消息的字符串：
`One for X, one for me.`
其中 `X` 是给定的名字。
但是，如果没有提供名字，则返回字符串：
`One for you, one for me.`

# --instructions--

编写一个返回正确字符串的函数，示例：

**输入**: `Walter`
**输出**: `One for Walter, one for me.`

**输入**: `James`
**输出**: `One for James, one for me.`

**输入**: `Martha`
**输出**: `One for Martha, one for me.`

# --seed--

```dart
String twoForOne() {
  
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

未提供名字

```dart
  test('test1', () {
    expect(twoForOne(), "One for you, one for me.", reason: '--err-t1--');
  });
```

传入 "James" 作为名字

```dart
  test('test2', () {
    expect(twoForOne(name: "James"), "One for James, one for me.", reason: '--err-t2--');
  });
```

传入 "Martha" 作为名字

```dart
  test('test3', () {
    expect(twoForOne(name: "Martha"), "One for Martha, one for me.", reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String twoForOne({String? name}) {
  if (name != null) {
    return "One for $name, one for me.";
  }
  return "One for you, one for me.";
}
```


