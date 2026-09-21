---
language: dart
exerciseType: 1
difficulty: 3
title: 括弧の対応
---

# --description--

コードや数式、マークアップを含むテキストには括弧が数多く登場し、開き括弧にはどれも同じ種類の閉じ括弧が必要です。括弧が対をなして玉ねぎの層のように入れ子になっていくとき、その文字列はバランスが取れています。`{[()]}` はバランスが取れていますが、`{[(])}` はバランスが取れていません。丸括弧の組が、その丸括弧が内側に収まっている角括弧の組よりも先に閉じられているからです。

ここで数えるのは、丸括弧 `()`、角括弧 `[]`、波括弧 `{}` の3組です。文字列内のそれ以外の文字はすべて無視されます。閉じ括弧は、まだ開いている括弧の中で最も新しく開かれた括弧を閉じなければならず、文字列が終わるときに開いたままの括弧が残っていてはいけません。

# --instructions--

文字列を受け取り、その中のすべての括弧が対応して正しく入れ子になっていれば `true` を、そうでなければ `false` を返す関数 `isBalanced` を書いてください。

例:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- 空の文字列はバランスが取れています。
- 括弧以外の文字は無視されます。
- 閉じ括弧は、まだ開いている括弧の中で最も新しく開かれた括弧と対応しなければなりません。
- 文字列が終わるとき、開いたままの括弧が残っていてはいけません。

# --seed--

```dart
bool isBalanced(String text) {
  
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

空の文字列はバランスが取れている

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

丸括弧1組だけの文字列はバランスが取れている

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

3種類の組が互いに入れ子になった文字列はバランスが取れている

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

括弧が他のテキストと混ざっていてもバランスが取れている

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

組が横に並んでいてもバランスが取れている

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

括弧をまったく含まない文字列はバランスが取れている

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

交差した組はバランスが取れていない

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

閉じられないままの開き括弧はバランスが取れていない

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

開き括弧より先に来る閉じ括弧はバランスが取れていない

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

文字列の奥で交差した組はバランスが取れていない

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

最後に余った閉じ括弧はバランスが取れていない

```dart
  test('test11', () {
    expect(isBalanced('())'), false, reason: '--err-t11--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isBalanced(String text) {
  const pairs = {')': '(', ']': '[', '}': '{'};
  final stack = <String>[];

  for (final char in text.split('')) {
    if (char == '(' || char == '[' || char == '{') {
      stack.add(char);
    } else if (pairs.containsKey(char)) {
      if (stack.isEmpty || stack.removeLast() != pairs[char]) {
        return false;
      }
    }
  }

  return stack.isEmpty;
}
```
