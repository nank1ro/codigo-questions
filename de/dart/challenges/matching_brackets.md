---
language: dart
exerciseType: 1
difficulty: 3
title: Passende Klammern
---

# --description--

Text, der Code, Formeln oder Markup enthält, ist voller Klammern, und jede öffnende Klammer braucht eine schließende derselben Art. Ein String ist ausgeglichen, wenn sich seine Klammern paarweise entsprechen und wie die Schichten einer Zwiebel verschachteln: `{[()]}` ist ausgeglichen, `{[(])}` dagegen nicht, weil das runde Paar vor dem eckigen Paar geschlossen wird, in dem es liegt.

Hier zählen drei Paare: runde `()`, eckige `[]` und geschweifte `{}`. Jedes andere Zeichen im String wird ignoriert. Eine schließende Klammer muss die zuletzt geöffnete Klammer schließen, die noch offen ist, und wenn der String endet, darf keine Klammer offen geblieben sein.

# --instructions--

Schreiben Sie eine Funktion `isBalanced`, die einen String entgegennimmt und `true` zurückgibt, wenn alle darin enthaltenen Klammern übereinstimmen und korrekt verschachtelt sind, und andernfalls `false`.

Beispiele:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Ein leerer String ist ausgeglichen.
- Zeichen, die keine Klammern sind, werden ignoriert.
- Eine schließende Klammer muss zu der zuletzt geöffneten Klammer passen, die noch offen ist.
- Wenn der String endet, darf keine Klammer offen geblieben sein.

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

Ein leerer String ist ausgeglichen

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

Ein einzelnes Paar runder Klammern ist ausgeglichen

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

Die drei Arten von Paaren, ineinander verschachtelt, sind ausgeglichen

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

Klammern, die mit anderem Text vermischt sind, sind weiterhin ausgeglichen

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

Nebeneinander stehende Paare sind ausgeglichen

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

Ein String ohne jegliche Klammern ist ausgeglichen

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

Ein überkreuztes Paar ist nicht ausgeglichen

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

Eine öffnende Klammer, die nie geschlossen wird, ist nicht ausgeglichen

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

Eine schließende Klammer vor jeder öffnenden ist nicht ausgeglichen

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

Überkreuzte Paare tiefer im String sind nicht ausgeglichen

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

Eine am Ende übrig gebliebene schließende Klammer ist nicht ausgeglichen

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
