---
language: dart
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

Pangram to zdanie, w którym każda litera angielskiego alfabetu występuje co najmniej raz. Najbardziej znanym przykładem jest "the quick brown fox jumps over the lazy dog", które mieści wszystkie 26 liter w dziewięciu krótkich słowach.

Sprawdzenie nie rozróżnia wielkości liter, więc `A` i `a` liczą się jako ta sama litera. Cyfry, znaki interpunkcyjne i spacje są ignorowane: nie są literami, ale nie są też powodem do odrzucenia zdania.

# --instructions--

Napisz funkcję `isPangram`, która przyjmuje zdanie i zwraca `true`, jeśli zdanie jest pangramem, a `false` w przeciwnym razie.

Przykłady:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Puste zdanie nie jest pangramem.
- Liczy się tylko 26 liter od `a` do `z`.

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

Puste zdanie nie jest pangramem

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

Klasyczne zdanie "the quick brown fox jumps over the lazy dog" jest pangramem

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

Zdanie, w którym brakuje litery `x`, nie jest pangramem

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

Zdanie "the five boxing wizards jump quickly" jest pangramem

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

Podkreślenia są ignorowane, więc zdanie nadal jest pangramem

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

Cyfry są ignorowane, więc zdanie nadal jest pangramem

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

Cyfry nie zastępują liter `e`, `i` oraz `t`

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

Zdanie zapisane wielkimi literami też jest pangramem

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

Mieszanie wielkości liter w tej samej połowie alfabetu nie wystarczy

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
