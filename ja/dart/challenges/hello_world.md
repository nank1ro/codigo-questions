---
language: dart
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__は、新しい言語や環境でプログラミングを始める際の伝統的な最初のプログラムです。

# --instructions--

文字列"Hello, World!"を返す関数を書いてください。

# --seed--

```dart
String hello() {

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

関数は"Hello, World!"を返す必要があります。

```dart
  const expected = "Hello, World!";
  test('test1', () {
    expect(hello(), expected, reason: '--err-t1--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String hello() {
  return "Hello, World!";
}
```

