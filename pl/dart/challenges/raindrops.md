---
language: dart
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Twoim zadaniem jest zamiana liczby na ciąg znaków zawierający dźwięki deszczu odpowiadające pewnym potencjalnym dzielnikam.
Dzielnik to liczba, która dzieli inną liczbę bez reszty.
Najprostszym sposobem sprawdzenia, czy liczba jest dzielnikiem innej, jest użycie operacji modulo.
Zasady gry Raindrops: jeśli podana liczba:

- ma 3 jako dzielnik, dodaj 'Pling' do wyniku.
- ma 5 jako dzielnik, dodaj 'Plang' do wyniku.
- ma 7 jako dzielnik, dodaj 'Plong' do wyniku.
- nie ma żadnego z 3, 5 ani 7 jako dzielnika, wynikiem powinny być cyfry tej liczby.

# --instructions--

Napisz funkcję, która zwraca poprawny ciąg znaków, przykłady:

- 28 ma 7 jako dzielnik, ale nie 3 ani 5, więc wynikiem byłoby `"Plong"`.
- 30 ma zarówno 3, jak i 5 jako dzielniki, ale nie 7, więc wynikiem byłoby `"PlingPlang"`.
- 34 nie jest podzielne przez 3, 5 ani 7, więc wynikiem byłoby `"34"`.

Przykład wywołania funkcji:
```dart
print(raindrops(28))
// prints "Plong"
```

# --seed--

```dart
String raindrops() {

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

Dźwięk dla 1 to "1"

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

Dźwięk dla 3 to "Pling"

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

Dźwięk dla 5 to "Plang"

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

Dźwięk dla 7 to "Plong"

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

Dźwięk dla 6 to "Pling"

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

Dźwięk dla 8 to "8"

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

Dźwięk dla 9 to "Pling"

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

Dźwięk dla 10 to "Plang"

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

Dźwięk dla 14 to "Plong"

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

Dźwięk dla 15 to "PlingPlang"

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

Dźwięk dla 21 to "PlingPlong"

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

Dźwięk dla 25 to "Plang"

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

Dźwięk dla 27 to "Pling"

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

Dźwięk dla 35 to "PlangPlong"

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

Dźwięk dla 49 to "Plong"

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

Dźwięk dla 52 to "52"

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

Dźwięk dla 105 to "PlingPlangPlong"

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

Dźwięk dla 3125 to "Plang"

```dart
  test('test18', () {
    expect(raindrops(3125), "Plang", reason: '--err-t18--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String raindrops(int number) {
  var result = "";
  if (number % 3 == 0) {
    result += "Pling";
  }
  if (number % 5 == 0) {
    result += "Plang";
  }
  if (number % 7 == 0) {
    result += "Plong";
  }
  if (result.isEmpty) {
    result = number.toString();
  }
  return result;
}
```
