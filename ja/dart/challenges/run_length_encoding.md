---
language: dart
exerciseType: 1
difficulty: 2
title: ランレングス符号化
---

# --description--

ランレングス符号化は、圧縮のテクニックの中でも最も古いものの1つです。同じ文字を何度も書き連ねる代わりに、その文字が何回繰り返されるかを書き、その後に文字そのものを書きます。

ほとんどが空白のページをスキャンするファックスは、同じピクセルが長く続く部分に出会います。そのため、`W` が12個並んだ1行は、はるかに短い `12W` となって回線を流れていきます。文字が1度しか現れない場合は、数えても得るものがないため、その文字だけがそのままコピーされます。

# --instructions--

文字列 `text` を受け取り、ランレングス符号化した形式を返す関数 `encodeRun` を書いてください。

同じ文字が2回以上続く連続した並びは、その長さを十進数で書いたものに、その文字を付けた形になります。長さ1の並びは、前に数字を付けずに、その1文字だけがそのままコピーされます。

例:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- テキストには `A` から `Z` までの大文字とスペースだけが含まれます。
- 9文字より長い並びは、十進数の回数をすべて使うため、`W` が12個なら `12W` となり、`9W3W` にはなりません。
- スペースも普通の文字です。文字とまったく同じように数えられ、エンコードされます。
- 空の文字列は空の文字列にエンコードされます。

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

空の文字列は空の文字列にエンコードされる

```dart
  test('test1', () {
    expect(encodeRun(''), '', reason: '--err-t1--');
  });
```

1文字だけの文字はそのままコピーされる

```dart
  test('test2', () {
    expect(encodeRun('A'), 'A', reason: '--err-t2--');
  });
```

繰り返しのない文字列は変化せずにそのまま通る

```dart
  test('test3', () {
    expect(encodeRun('ABCDE'), 'ABCDE', reason: '--err-t3--');
  });
```

長さ2の並びは、回数の後に文字が付いた形になる

```dart
  test('test4', () {
    expect(encodeRun('AA'), '2A', reason: '--err-t4--');
  });
```

並びが混ざった例 "AABCCCDEEEE" は "2AB3CD4E" になる

```dart
  test('test5', () {
    expect(encodeRun('AABCCCDEEEE'), '2AB3CD4E', reason: '--err-t5--');
  });
```

長さ12の並びは十進数の回数をすべて使うため、結果は "12W" で始まる

```dart
  test('test6', () {
    expect(encodeRun('WWWWWWWWWWWWBWW'), '12WB2W', reason: '--err-t6--');
  });
```

スペースの並びも文字の並びと同じようにエンコードされる

```dart
  test('test7', () {
    expect(encodeRun('  HI  '), '2 HI2 ', reason: '--err-t7--');
  });
```

長さ10の並びは "10A" と書かれ、より短い2つの並びに分けられることはない

```dart
  test('test8', () {
    expect(encodeRun('AAAAAAAAAA'), '10A', reason: '--err-t8--');
  });
```

交互に現れる1文字はすべてそのままコピーされる

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
