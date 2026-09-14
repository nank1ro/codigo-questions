---
language: dart
exerciseType: 1
difficulty: 1
title: Панграмма
---

# --description--

Панграмма — это предложение, в котором каждая буква английского алфавита используется хотя бы один раз. Самый известный пример — "the quick brown fox jumps over the lazy dog", в котором все 26 букв умещаются в девять коротких слов.

Проверка не учитывает регистр, поэтому `A` и `a` считаются одной и той же буквой. Цифры, знаки препинания и пробелы игнорируются: они не являются буквами, но и не являются причиной отклонить предложение.

# --instructions--

Напишите функцию `isPangram`, которая принимает предложение и возвращает `true`, если предложение является панграммой, и `false` в противном случае.

Примеры:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Пустое предложение не является панграммой.
- Считаются только 26 букв от `a` до `z`.

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

Пустое предложение не является панграммой

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

Классическое предложение "the quick brown fox jumps over the lazy dog" является панграммой

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

Предложение, в котором отсутствует буква `x`, не является панграммой

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

Предложение "the five boxing wizards jump quickly" является панграммой

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

Подчёркивания игнорируются, поэтому предложение остаётся панграммой

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

Цифры игнорируются, поэтому предложение остаётся панграммой

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

Цифры не заменяют буквы `e`, `i` и `t`

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

Предложение в верхнем регистре тоже является панграммой

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

Смешения регистров одной и той же половины алфавита недостаточно

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
