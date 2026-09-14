---
language: dart
exerciseType: 1
difficulty: 1
title: 팬그램
---

# --description--

팬그램은 영어 알파벳의 모든 문자를 적어도 한 번씩 사용하는 문장입니다. 가장 잘 알려진 예는 "the quick brown fox jumps over the lazy dog"이며, 26개의 문자를 모두 아홉 개의 짧은 단어에 담고 있습니다.

이 검사는 대소문자를 구분하지 않으므로 `A`와 `a`는 같은 문자로 셉니다. 숫자, 문장 부호, 공백은 무시됩니다. 이들은 문자가 아니지만, 문장을 거부할 이유도 되지 않습니다.

# --instructions--

문장을 받아 그 문장이 팬그램이면 `true`를, 그렇지 않으면 `false`를 반환하는 함수 `isPangram`를 작성하세요.

예시:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- 빈 문장은 팬그램이 아닙니다.
- `a`부터 `z`까지의 26개 문자만 셉니다.

# --seed--

```dart
bool isPangram(String sentence) {
  
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

빈 문장은 팬그램이 아니다

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

고전적인 문장 "the quick brown fox jumps over the lazy dog"는 팬그램이다

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

문자 `x`가 빠진 문장은 팬그램이 아니다

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

문장 "the five boxing wizards jump quickly"는 팬그램이다

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

밑줄은 무시되므로 그 문장은 여전히 팬그램이다

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

숫자는 무시되므로 그 문장은 여전히 팬그램이다

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

숫자는 문자 `e`, `i`, `t`를 대신하지 않는다

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

대문자로 된 문장도 팬그램이다

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

알파벳의 같은 절반의 대소문자를 섞는 것만으로는 충분하지 않다

```dart
  test('test9', () {
    expect(isPangram('abcdefghijklm ABCDEFGHIJKLM'), false, reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isPangram(String sentence) {
  final letters = <String>{};

  for (final char in sentence.toLowerCase().split('')) {
    if (char.compareTo('a') >= 0 && char.compareTo('z') <= 0) {
      letters.add(char);
    }
  }

  return letters.length == 26;
}
```
