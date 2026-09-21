---
language: dart
exerciseType: 1
difficulty: 2
title: Zegar
---

# --description--

Zegar 24-godzinny pokazuje porę dnia jako `HH:MM`, zaczynając od `00:00` tuż po północy i kończąc na `23:59`, minutę przed kolejną północą. Obie części są zawsze zapisywane dwiema cyframi, więc dziewięć minut po jedenastej rano to wskazanie `11:09`.

Cały dzień trwa 1440 minut. Gdy zegar przekroczy `23:59`, przewija się na `00:00` i zaczyna dzień od nowa, a przekręcenie go wstecz za `00:00` daje `23:59`.

# --instructions--

Napisz funkcję `clockTime`, która przyjmuje dwie liczby całkowite, `hours` i `minutes`, i zwraca wskazanie zegara 24-godzinnego jako napis `"HH:MM"`, przy czym obie części są uzupełnione do dwóch cyfr.

Przykłady:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Każda z liczb może być ujemna lub większa, niż pozwala prawdziwy zegar.
- Oblicz całkowitą liczbę minut jako `hours * 60 + minutes`, a następnie zawiń tę sumę do zakresu od `0` do `1439`, żeby zegar przewijał się w obu kierunkach.
- `clockTime(24, 0)` to dokładnie jeden dzień, więc wskazanie to `"00:00"`.

# --seed--

```dart
String clockTime(int hours, int minutes) {
  
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

Ósma rano to wskazanie `08:00`

```dart
  test('test1', () {
    expect(clockTime(8, 0), "08:00", reason: '--err-t1--');
  });
```

Pojedyncze cyfry są uzupełniane do dwóch, więc dziewięć minut po jedenastej to wskazanie `11:09`

```dart
  test('test2', () {
    expect(clockTime(11, 9), "11:09", reason: '--err-t2--');
  });
```

Dokładnie jeden pełny dzień godzin przewija się na `00:00`

```dart
  test('test3', () {
    expect(clockTime(24, 0), "00:00", reason: '--err-t3--');
  });
```

Minuty powyżej 60 przenoszą się na godziny

```dart
  test('test4', () {
    expect(clockTime(25, 160), "03:40", reason: '--err-t4--');
  });
```

Ujemna godzina przekręca zegar wstecz za północ

```dart
  test('test5', () {
    expect(clockTime(-1, 15), "23:15", reason: '--err-t5--');
  });
```

Ujemna liczba minut również przekręca zegar wstecz

```dart
  test('test6', () {
    expect(clockTime(0, -90), "22:30", reason: '--err-t6--');
  });
```

Więcej niż cały dzień wstecz nadal przewija zegar

```dart
  test('test7', () {
    expect(clockTime(-25, 0), "23:00", reason: '--err-t7--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String clockTime(int hours, int minutes) {
  // % w Darcie to modulo euklidesowe, więc ujemna suma zostaje od razu
  // zawinięta do przodu do zakresu 0..1439.
  final total = (hours * 60 + minutes) % 1440;

  final hh = (total ~/ 60).toString().padLeft(2, '0');
  final mm = (total % 60).toString().padLeft(2, '0');
  return '$hh:$mm';
}
```
