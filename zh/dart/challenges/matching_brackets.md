---
language: dart
exerciseType: 1
difficulty: 3
title: 括号匹配
---

# --description--

包含代码、数学式或标记的文本中充满了括号，每个开括号都需要一个同类型的闭括号。当字符串中的括号两两配对，并像洋葱的层层外皮一样嵌套时，它就是平衡的：`{[()]}` 是平衡的，而 `{[(])}` 则不是，因为圆括号对在包含它的方括号对之前就闭合了。

这里有三对括号：圆括号 `()`、方括号 `[]` 和花括号 `{}`。字符串中的其他所有字符都会被忽略。闭括号必须闭合最近一个仍处于打开状态的括号，并且在字符串结束时不能有任何括号保持打开。

# --instructions--

编写一个函数 `isBalanced`，它接收一个字符串，当其中的所有括号都配对且正确嵌套时返回 `true`，否则返回 `false`。

示例：
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- 空字符串是平衡的。
- 不是括号的字符会被忽略。
- 闭括号必须与最近一个仍处于打开状态的括号配对。
- 字符串结束时不能有任何括号保持打开。

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

空字符串是平衡的

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

单独的一对圆括号是平衡的

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

三种括号对彼此嵌套是平衡的

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

括号与其他文本混在一起时依然是平衡的

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

并排摆放的括号对是平衡的

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

不含任何括号的字符串是平衡的

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

交叉的括号对不是平衡的

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

从未被闭合的开括号不是平衡的

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

出现在任何开括号之前的闭括号不是平衡的

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

字符串更深处的交叉括号对不是平衡的

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

结尾遗留的闭括号不是平衡的

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
