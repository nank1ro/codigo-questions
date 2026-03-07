---
language: dart
exerciseType: 1
difficulty: 1
title: Два по цене одного
---

# --description--

Дано имя, верните строку с сообщением:
`One for X, one for me.`
Где `X` — это данное имя.
Однако, если имя отсутствует, верните строку:
`One for you, one for me.`

# --instructions--

Напишите функцию, которая возвращает правильную строку, примеры:

**ввод**: `Walter`
**вывод**: `One for Walter, one for me.`

**ввод**: `James`
**вывод**: `One for James, one for me.`

**ввод**: `Martha`
**вывод**: `One for Martha, one for me.`

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

Имя не указано

```dart
  test('test1', () {
    expect(twoForOne(), "One for you, one for me.", reason: '--err-t1--');
  });
```

Передать "James" в качестве имени

```dart
  test('test2', () {
    expect(twoForOne(name: "James"), "One for James, one for me.", reason: '--err-t2--');
  });
```

Передать "Martha" в качестве имени

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


