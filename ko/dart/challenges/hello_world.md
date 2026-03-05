---
language: dart
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__는 새로운 언어나 환경에서 프로그래밍을 시작할 때 전통적으로 작성하는 첫 번째 프로그램입니다.

# --instructions--

"Hello, World!" 문자열을 반환하는 함수를 작성하십시오.

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

함수는 "Hello, World!"를 반환해야 합니다.

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

