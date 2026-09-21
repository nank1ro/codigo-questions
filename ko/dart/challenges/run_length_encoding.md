---
language: dart
exerciseType: 1
difficulty: 2
title: 런 렝스 인코딩
---

# --description--

런 렝스 인코딩은 가장 오래된 압축 기법 중 하나입니다: 같은 문자를 계속 반복해서 쓰는 대신, 몇 번 반복되는지를 먼저 쓰고 그다음에 문자 자신을 씁니다.

거의 빈 페이지를 스캔하는 팩스 기계는 길게 이어지는 동일한 픽셀을 만나므로, 열두 개의 `W`가 이룬 한 행은 훨씬 짧은 `12W`로 전송됩니다. 문자가 한 번만 나타나면 개수를 세서 얻는 것이 없으므로 문자 하나만 그대로 복사됩니다.

# --instructions--

문자열 `text`를 받아 런 렝스 인코딩된 형태를 반환하는 함수 `encodeRun`을(를) 작성하세요.

같은 문자가 두 번 이상 반복되는 모든 런은 런의 길이를 십진수로 쓴 것 뒤에 그 문자를 붙인 형태가 됩니다. 길이가 1인 런은 앞에 숫자 없이 문자 하나만 그대로 복사됩니다.

예시:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- 텍스트에는 `A`부터 `Z`까지의 대문자와 공백만 포함됩니다.
- 아홉 글자보다 긴 런은 전체 십진수 개수를 사용하므로, 열두 개의 `W`는 `12W`가 되며 절대 `9W3W`가 되지 않습니다.
- 공백도 일반 문자입니다. 공백은 글자와 똑같이 개수를 세고 인코딩합니다.
- 빈 문자열은 빈 문자열로 인코딩됩니다.

# --seed--

```dart
String encodeRun(String text) {
  
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

빈 문자열은 빈 문자열로 인코딩됩니다

```dart
  test('test1', () {
    expect(encodeRun(''), '', reason: '--err-t1--');
  });
```

문자 하나는 그대로 자기 자신으로 복사됩니다

```dart
  test('test2', () {
    expect(encodeRun('A'), 'A', reason: '--err-t2--');
  });
```

반복이 없는 문자열은 아무 변화 없이 그대로 통과합니다

```dart
  test('test3', () {
    expect(encodeRun('ABCDE'), 'ABCDE', reason: '--err-t3--');
  });
```

길이가 2인 런은 개수 뒤에 문자를 붙인 형태가 됩니다

```dart
  test('test4', () {
    expect(encodeRun('AA'), '2A', reason: '--err-t4--');
  });
```

뒤섞인 예시 "AABCCCDEEEE"는 "2AB3CD4E"가 됩니다

```dart
  test('test5', () {
    expect(encodeRun('AABCCCDEEEE'), '2AB3CD4E', reason: '--err-t5--');
  });
```

길이가 12인 런은 전체 십진수 개수를 사용하므로 결과는 "12W"로 시작합니다

```dart
  test('test6', () {
    expect(encodeRun('WWWWWWWWWWWWBWW'), '12WB2W', reason: '--err-t6--');
  });
```

공백의 런도 글자의 런과 똑같이 인코딩됩니다

```dart
  test('test7', () {
    expect(encodeRun('  HI  '), '2 HI2 ', reason: '--err-t7--');
  });
```

길이가 10인 런은 "10A"로 쓰이며 두 개의 더 짧은 런으로 쓰이지 않습니다

```dart
  test('test8', () {
    expect(encodeRun('AAAAAAAAAA'), '10A', reason: '--err-t8--');
  });
```

번갈아 나타나는 문자들은 하나하나 모두 그대로 자기 자신으로 복사됩니다

```dart
  test('test9', () {
    expect(encodeRun('ABABAB'), 'ABABAB', reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String encodeRun(String text) {
  final result = StringBuffer();
  var i = 0;

  while (i < text.length) {
    var run = 1;
    while (i + run < text.length && text[i + run] == text[i]) {
      run++;
    }
    if (run > 1) {
      result.write(run);
    }
    result.write(text[i]);
    i += run;
  }

  return result.toString();
}
```
