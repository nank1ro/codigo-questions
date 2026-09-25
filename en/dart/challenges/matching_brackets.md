---
language: dart
exerciseType: 1
difficulty: 3
title: Matching brackets
---

# --description--

Text that carries code, maths or markup is full of brackets, and every opening bracket needs a closing one of the same kind. A string is balanced when its brackets pair up and nest like the layers of an onion: `{[()]}` is balanced, while `{[(])}` is not, because the round pair is closed before the square pair it sits inside.

Three pairs count here: round `()`, square `[]` and curly `{}`. Every other character in the string is ignored. A closing bracket must close the most recently opened bracket that is still open, and when the string ends no bracket may be left open.

# --instructions--

Write a function `isBalanced` that takes a string and returns `true` when all the brackets in it are matched and properly nested, and `false` otherwise.

Examples:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- An empty string is balanced.
- Characters that are not brackets are ignored.
- A closing bracket must match the most recently opened bracket that is still open.
- No bracket may be left open when the string ends.

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

An empty string is balanced

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

A single pair of round brackets is balanced

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

The three kinds of pair nested inside each other are balanced

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

Brackets mixed with other text are still balanced

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

Pairs placed side by side are balanced

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

A string without any brackets is balanced

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

A crossed pair is not balanced

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

An opening bracket that is never closed is not balanced

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

A closing bracket before any opening one is not balanced

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

Crossed pairs deeper in the string are not balanced

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

A closing bracket left over at the end is not balanced

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
