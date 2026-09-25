---
language: dart
exerciseType: 1
difficulty: 3
title: Pasujące nawiasy
---

# --description--

Tekst zawierający kod, zapis matematyczny czy znaczniki jest pełen nawiasów, a każdy nawias otwierający potrzebuje nawiasu zamykającego tego samego rodzaju. Ciąg znaków jest zrównoważony, gdy jego nawiasy tworzą pary i zagnieżdżają się jak warstwy cebuli: `{[()]}` jest zrównoważony, natomiast `{[(])}` już nie, ponieważ para okrągła zostaje zamknięta przed parą kwadratową, wewnątrz której się znajduje.

Liczą się tutaj trzy pary: okrągła `()`, kwadratowa `[]` i klamrowa `{}`. Każdy inny znak w ciągu jest ignorowany. Nawias zamykający musi zamykać ostatnio otwarty nawias, który wciąż jest otwarty, a gdy ciąg się kończy, żaden nawias nie może pozostać otwarty.

# --instructions--

Napisz funkcję `isBalanced`, która przyjmuje ciąg znaków i zwraca `true`, gdy wszystkie zawarte w niej nawiasy są sparowane i poprawnie zagnieżdżone, a w przeciwnym razie zwraca `false`.

Przykłady:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Pusty ciąg znaków jest zrównoważony.
- Znaki, które nie są nawiasami, są ignorowane.
- Nawias zamykający musi pasować do ostatnio otwartego nawiasu, który wciąż jest otwarty.
- Żaden nawias nie może pozostać otwarty, gdy ciąg znaków się kończy.

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

Pusty ciąg znaków jest zrównoważony

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

Pojedyncza para nawiasów okrągłych jest zrównoważona

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

Trzy rodzaje par zagnieżdżone jeden w drugim są zrównoważone

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

Nawiasy przeplatane innym tekstem nadal są zrównoważone

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

Pary ustawione obok siebie są zrównoważone

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

Ciąg znaków bez żadnych nawiasów jest zrównoważony

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

Skrzyżowana para nawiasów nie jest zrównoważona

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

Nawias otwierający, który nigdy nie zostaje zamknięty, nie jest zrównoważony

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

Nawias zamykający pojawiający się przed jakimkolwiek nawiasem otwierającym nie jest zrównoważony

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

Skrzyżowane pary głębiej w ciągu znaków nie są zrównoważone

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

Nawias zamykający pozostawiony na końcu nie jest zrównoważony

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
