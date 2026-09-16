---
language: dart
exerciseType: 1
difficulty: 2
title: 카이사르 암호
---

# --description--

율리우스 카이사르는 암호학에서 가장 오래된 기법 중 하나로 자신의 개인 편지를 보호했습니다. 그는 메시지의 모든 글자를 알파벳에서 고정된 칸수만큼 뒤에 있는 글자로 바꿨습니다. 이동 거리가 3이면 `a`는 `d`가 되고, `b`는 `e`가 되며, `c`는 `f`가 됩니다.

알파벳은 원처럼 동작하기 때문에 끝에 있는 글자는 다시 처음으로 돌아갑니다. 이동 거리가 3이면 `x`는 `a`가 되고, `y`는 `b`가 되며, `z`는 `c`가 됩니다.

공백, 쉼표, 느낌표, 숫자처럼 글자가 아닌 것들은 이 암호를 거쳐도 그대로 남습니다.

# --instructions--

메시지 `text`와 정수 `shift`를 받아 암호화된 메시지를 반환하는 함수 `caesarCipher`를 작성하세요.

예시:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- 메시지는 항상 소문자이므로 대문자를 다룰 필요는 없습니다.
- 글자가 아닌 문자는 자리와 값을 그대로 유지합니다.
- 이동 거리는 절대 음수가 아닙니다. 이동 거리가 `0`이면 메시지는 바뀌지 않으며, `26`이어도 마찬가지입니다.

# --seed--

```dart
String caesarCipher(String text, int shift) {
  
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

이동 거리가 3이면 "hello"는 "khoor"가 됩니다

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

알파벳의 끝은 처음으로 돌아가므로 "xyz"는 "abc"가 됩니다

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

이동 거리가 0이면 메시지는 바뀌지 않습니다

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

이동 거리가 26이면 알파벳을 한 바퀴 도는 것이므로 메시지는 바뀌지 않습니다

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

문장 부호와 공백은 바뀌지 않고 그대로 통과합니다

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

빈 메시지는 빈 상태로 남습니다

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

글자 사이의 공백은 그대로 유지됩니다

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

이동 거리가 25여도 숫자는 이동하지 않습니다

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

이동 거리가 13이면 문장 전체가 암호화됩니다

```dart
  test('test9', () {
    expect(caesarCipher('the quick brown fox jumps over the lazy dog', 13), 'gur dhvpx oebja sbk whzcf bire gur ynml qbt', reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String caesarCipher(String text, int shift) {
  final a = 'a'.codeUnitAt(0);
  final z = 'z'.codeUnitAt(0);
  final encoded = <int>[];

  for (final code in text.codeUnits) {
    if (code >= a && code <= z) {
      encoded.add(a + (code - a + shift) % 26);
    } else {
      encoded.add(code);
    }
  }

  return String.fromCharCodes(encoded);
}
```
