---
language: dart
exerciseType: 1
difficulty: 1
title: 둘이서 하나
---

# --description--

이름이 주어지면 다음 메시지가 포함된 문자열을 반환합니다:
`One for X, one for me.`
여기서 `X`는 주어진 이름입니다.
그러나 이름이 없으면 다음 문자열을 반환합니다:
`One for you, one for me.`

# --instructions--

올바른 문자열을 반환하는 함수를 작성하십시오. 예시:

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**: `James`
**output**: `One for James, one for me.`

**input**: `Martha`
**output**: `One for Martha, one for me.`

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

이름이 주어지지 않은 경우

```dart
  test('test1', () {
    expect(twoForOne(), "One for you, one for me.", reason: '--err-t1--');
  });
```

"James"를 이름으로 전달합니다

```dart
  test('test2', () {
    expect(twoForOne(name: "James"), "One for James, one for me.", reason: '--err-t2--');
  });
```

"Martha"를 이름으로 전달합니다

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


