---
language: dart
exerciseType: 1
difficulty: 2
title: シーザー暗号
---

# --description--

ユリウス・カエサルは、暗号術の中でも最も古い手法の1つを使って、自分の私的な手紙を守っていました。その手法とは、メッセージのすべての文字を、アルファベットに沿って固定された数だけ先にある文字に置き換えるというものです。シフトが3の場合、`a`は`d`に、`b`は`e`に、`c`は`f`になります。

アルファベットは円のように振る舞うため、終わりの文字は先頭へ折り返します。シフトが3の場合、`x`は`a`に、`y`は`b`に、`z`は`c`になります。

スペース、カンマ、感嘆符、数字など、英字以外のものはすべて、暗号を通しても変更されずにそのまま通過します。

# --instructions--

メッセージ`text`と整数`shift`を受け取り、エンコードされたメッセージを返す関数`caesarCipher`を書いてください。

例：
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- メッセージは常に小文字なので、大文字を扱う必要はありません。
- 英字以外の文字は、その位置と値を保ちます。
- シフトが負になることはありません。シフト`0`ではメッセージはそのままになり、シフト`26`でも同じです。

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

シフト3で"hello"は"khoor"になります。

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

アルファベットの終わりが折り返されるため、"xyz"は"abc"になります。

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

シフト0ではメッセージは変わりません。

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

シフト26はアルファベットのちょうど1周なので、メッセージは変わりません。

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

句読点とスペースは変更されずに通過します。

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

空のメッセージは空のままです。

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

文字と文字の間のスペースはそのまま保持されます。

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

数字は、シフト25であっても置き換えられません。

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

シフト13で文全体がエンコードされます。

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
