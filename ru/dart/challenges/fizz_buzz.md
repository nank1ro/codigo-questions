---
language: dart
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Создайте функцию, которая принимает число в качестве аргумента и возвращает `"Fizz"`, `"Buzz"` или `"FizzBuzz"`.

# --instructions--

- Если число кратно `3`, вывод должен быть `"Fizz"`
- Если число кратно `5`, вывод должен быть `"Buzz"`.
- Если число кратно и `3`, и `5`, вывод должен быть `"FizzBuzz"`.
- Если число не кратно ни `3`, ни `5`, число должно быть выведено как есть, как показано в примерах ниже.
- Вывод всегда должен быть строкой, даже если число не кратно `3` или `5`.

Примеры:
```dart
fizz_buzz(3); // ➞ "Fizz"
fizz_buzz(5); // ➞ "Buzz"
fizz_buzz(15); // ➞ "FizzBuzz"
fizz_buzz(4); // ➞ "4"
```

# --seed--

```dart
String fizzBuzz() {
  
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

Число `3` должно быть равно `"Fizz"`

```dart
  test('test1', () {
    expect(fizzBuzz(3), 'Fizz', reason: '--err-t1--');
  });
```

Число `5` должно быть равно `"Buzz"`

```dart
  test('test2', () {
    expect(fizzBuzz(5), 'Buzz', reason: '--err-t2--');
  });
```

Число `15` должно быть равно `"FizzBuzz"`

```dart
  test('test3', () {
    expect(fizzBuzz(15), 'FizzBuzz', reason: '--err-t3--');
  });
```

Число `10` должно быть равно `"Buzz"`

```dart
  test('test4', () {
    expect(fizzBuzz(10), 'Buzz', reason: '--err-t4--');
  });
```

Число `98` должно быть равно `"98"`

```dart
  test('test5', () {
    expect(fizzBuzz(98), '98', reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String fizzBuzz(int number) {
  if (number % 3 == 0 && number % 5 == 0) {
    return 'FizzBuzz';
  }
  if (number % 3 == 0) {
    return 'Fizz';
  }
  if (number % 5 == 0) {
    return 'Buzz';
  }
  return number.toString();
}
```
