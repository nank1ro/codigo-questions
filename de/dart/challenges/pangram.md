---
language: dart
exerciseType: 1
difficulty: 1
title: Pangramm
---

# --description--

Ein Pangramm ist ein Satz, der jeden Buchstaben des englischen Alphabets mindestens einmal verwendet. Das bekannteste Beispiel ist "the quick brown fox jumps over the lazy dog", das alle 26 Buchstaben in neun kurze Wörter unterbringt.

Die Prüfung unterscheidet nicht zwischen Groß- und Kleinschreibung, daher zählen `A` und `a` als derselbe Buchstabe. Ziffern, Satzzeichen und Leerzeichen werden ignoriert: Sie sind keine Buchstaben, aber sie sind auch kein Grund, einen Satz abzulehnen.

# --instructions--

Schreiben Sie eine Funktion `isPangram`, die einen Satz entgegennimmt und `true` zurückgibt, wenn der Satz ein Pangramm ist, und andernfalls `false`.

Beispiele:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Ein leerer Satz ist kein Pangramm.
- Nur die 26 Buchstaben von `a` bis `z` zählen.

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

Ein leerer Satz ist kein Pangramm

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

Der klassische Satz "the quick brown fox jumps over the lazy dog" ist ein Pangramm

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

Ein Satz, dem der Buchstabe `x` fehlt, ist kein Pangramm

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

Der Satz "the five boxing wizards jump quickly" ist ein Pangramm

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

Unterstriche werden ignoriert, daher ist der Satz weiterhin ein Pangramm

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

Ziffern werden ignoriert, daher ist der Satz weiterhin ein Pangramm

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

Ziffern ersetzen nicht die Buchstaben `e`, `i` und `t`

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

Ein Satz in Großbuchstaben ist ebenfalls ein Pangramm

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

Das Mischen der Groß- und Kleinschreibung derselben Hälfte des Alphabets reicht nicht aus

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
