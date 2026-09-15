---
language: dart
exerciseType: 1
difficulty: 2
title: Suma kontrolna Luhna
---

# --description--

Algorytm Luhna to prosta suma kontrolna służąca do sprawdzania poprawności numerów identyfikacyjnych, takich jak numery kart kredytowych.

Przed sprawdzeniem numeru usuń wszystkie spacje z ciągu znaków. Ciąg znaków jest poprawny tylko wtedy, gdy to, co zostało, jest dłuższe niż jeden znak, a oryginalny ciąg znaków zawiera wyłącznie cyfry i spacje.

Aby wykonać sprawdzenie, zacznij od skrajnie prawej cyfry i przesuwaj się w lewo, podwajając co drugą cyfrę. Gdy podwojenie da liczbę większą niż 9, odejmij od niej 9. Następnie zsumuj wszystkie cyfry: numer jest poprawny tylko wtedy, gdy suma jest podzielna przez 10.

Na przykład `"059"` daje `0`, potem podwojone `5` to `10`, które staje się `1`, a następnie `9`. Ich suma wynosi `10`, czyli liczbę podzielną przez 10, więc numer jest poprawny.

# --instructions--

Napisz funkcję `isValid`, która przyjmuje ciąg znaków i zwraca `true`, gdy numer jest poprawny, a `false` w przeciwnym razie.

- `"4539 3195 0343 6467"` przechodzi sumę kontrolną, więc wynik to `true`.
- `"8273 1232 7352 0569"` nie przechodzi sumy kontrolnej, więc wynik to `false`.
- `"0"` ma długość tylko jednego znaku, więc wynik to `false`.
- `"055-444-285"` zawiera znak, który nie jest cyfrą ani spacją, więc wynik to `false`.

Przykład wywołania funkcji:
```dart
print(isValid("095 245 88"));
// wypisuje true
```

# --seed--

```dart
bool isValid(String value) {
  
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

Pojedyncza cyfra nie jest poprawna.

```dart
  test('test1', () {
    expect(isValid("0"), false, reason: '--err-t1--');
  });
```

Pojedyncza cyfra ze spacją na początku nie jest poprawna.

```dart
  test('test2', () {
    expect(isValid(" 0"), false, reason: '--err-t2--');
  });
```

Numer `"059"` jest poprawny.

```dart
  test('test3', () {
    expect(isValid("059"), true, reason: '--err-t3--');
  });
```

Numer `"59"` jest poprawny.

```dart
  test('test4', () {
    expect(isValid("59"), true, reason: '--err-t4--');
  });
```

Numer `"055 444 285"` jest poprawny.

```dart
  test('test5', () {
    expect(isValid("055 444 285"), true, reason: '--err-t5--');
  });
```

Numer `"055 444 286"` nie jest poprawny.

```dart
  test('test6', () {
    expect(isValid("055 444 286"), false, reason: '--err-t6--');
  });
```

Numer `"8273 1232 7352 0569"` nie jest poprawny.

```dart
  test('test7', () {
    expect(isValid("8273 1232 7352 0569"), false, reason: '--err-t7--');
  });
```

Numer `"4539 3195 0343 6467"` jest poprawny.

```dart
  test('test8', () {
    expect(isValid("4539 3195 0343 6467"), true, reason: '--err-t8--');
  });
```

Numer `"1 2345 6789 1234 5678 9012"` nie jest poprawny.

```dart
  test('test9', () {
    expect(isValid("1 2345 6789 1234 5678 9012"), false, reason: '--err-t9--');
  });
```

Numer `"095 245 88"` jest poprawny.

```dart
  test('test10', () {
    expect(isValid("095 245 88"), true, reason: '--err-t10--');
  });
```

Litera powoduje, że numer jest niepoprawny.

```dart
  test('test11', () {
    expect(isValid("055a 444 285"), false, reason: '--err-t11--');
  });
```

Myślniki powodują, że numer jest niepoprawny.

```dart
  test('test12', () {
    expect(isValid("055-444-285"), false, reason: '--err-t12--');
  });
```

Znak interpunkcyjny powoduje, że numer jest niepoprawny.

```dart
  test('test13', () {
    expect(isValid(":9"), false, reason: '--err-t13--');
  });
```

Symbole powodują, że numer jest niepoprawny.

```dart
  test('test14', () {
    expect(isValid("055# 444\$ 285"), false, reason: '--err-t14--');
  });
```

Pusty ciąg znaków nie jest poprawny.

```dart
  test('test15', () {
    expect(isValid(""), false, reason: '--err-t15--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isValid(String value) {
  var sum = 0;
  var count = 0;
  for (var i = value.length - 1; i >= 0; i--) {
    final code = value.codeUnitAt(i);
    if (code == 32) {
      continue;
    }
    if (code < 48 || code > 57) {
      return false;
    }
    var digit = code - 48;
    if (count % 2 == 1) {
      digit *= 2;
      if (digit > 9) {
        digit -= 9;
      }
    }
    sum += digit;
    count++;
  }
  return count > 1 && sum % 10 == 0;
}
```
