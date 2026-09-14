---
language: dart
exerciseType: 1
difficulty: 2
title: Luhn checksum
---

# --description--

Der Luhn-Algorithmus ist eine einfache Prüfsumme, die zur Überprüfung von Identifikationsnummern wie Kreditkartennummern verwendet wird.

Bevor Sie eine Zahl überprüfen, entfernen Sie alle Leerzeichen aus dem String. Der String ist nur gültig, wenn der übrig gebliebene Teil länger als ein Zeichen ist und der ursprüngliche String nichts außer Ziffern und Leerzeichen enthält.

Um die Überprüfung durchzuführen, beginnen Sie bei der äußersten rechten Ziffer und bewegen Sie sich nach links, wobei Sie jede zweite Ziffer verdoppeln. Wenn das Verdoppeln eine Zahl größer als 9 ergibt, subtrahieren Sie 9 davon. Addieren Sie dann alle Ziffern: Die Zahl ist nur gültig, wenn die Summe durch 10 teilbar ist.

Zum Beispiel ergibt `"059"` `0`, dann ergibt `5` verdoppelt `10`, was zu `1` wird, dann `9`. Ihre Summe ist `10`, was durch 10 teilbar ist, also ist die Zahl gültig.

# --instructions--

Schreiben Sie eine Funktion `isValid`, die einen String entgegennimmt und `true` zurückgibt, wenn die Zahl gültig ist, andernfalls `false`.

- `"4539 3195 0343 6467"` besteht die Prüfsumme, also ist das Ergebnis `true`.
- `"8273 1232 7352 0569"` besteht die Prüfsumme nicht, also ist das Ergebnis `false`.
- `"0"` ist nur ein Zeichen lang, also ist das Ergebnis `false`.
- `"055-444-285"` enthält ein Zeichen, das weder eine Ziffer noch ein Leerzeichen ist, also ist das Ergebnis `false`.

Beispiel eines Funktionsaufrufs:
```dart
print(isValid("095 245 88"));
// prints true
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

Eine einzelne Ziffer ist nicht gültig.

```dart
  test('test1', () {
    expect(isValid("0"), false, reason: '--err-t1--');
  });
```

Eine einzelne Ziffer mit einem führenden Leerzeichen ist nicht gültig.

```dart
  test('test2', () {
    expect(isValid(" 0"), false, reason: '--err-t2--');
  });
```

Die Zahl `"059"` ist gültig.

```dart
  test('test3', () {
    expect(isValid("059"), true, reason: '--err-t3--');
  });
```

Die Zahl `"59"` ist gültig.

```dart
  test('test4', () {
    expect(isValid("59"), true, reason: '--err-t4--');
  });
```

Die Zahl `"055 444 285"` ist gültig.

```dart
  test('test5', () {
    expect(isValid("055 444 285"), true, reason: '--err-t5--');
  });
```

Die Zahl `"055 444 286"` ist not gültig.

```dart
  test('test6', () {
    expect(isValid("055 444 286"), false, reason: '--err-t6--');
  });
```

Die Zahl `"8273 1232 7352 0569"` ist not gültig.

```dart
  test('test7', () {
    expect(isValid("8273 1232 7352 0569"), false, reason: '--err-t7--');
  });
```

Die Zahl `"4539 3195 0343 6467"` ist gültig.

```dart
  test('test8', () {
    expect(isValid("4539 3195 0343 6467"), true, reason: '--err-t8--');
  });
```

Die Zahl `"1 2345 6789 1234 5678 9012"` ist not gültig.

```dart
  test('test9', () {
    expect(isValid("1 2345 6789 1234 5678 9012"), false, reason: '--err-t9--');
  });
```

Die Zahl `"095 245 88"` ist gültig.

```dart
  test('test10', () {
    expect(isValid("095 245 88"), true, reason: '--err-t10--');
  });
```

Ein Buchstabe macht die Zahl ungültig.

```dart
  test('test11', () {
    expect(isValid("055a 444 285"), false, reason: '--err-t11--');
  });
```

Bindestriche machen die Zahl ungültig.

```dart
  test('test12', () {
    expect(isValid("055-444-285"), false, reason: '--err-t12--');
  });
```

Ein Satzeichen macht die Zahl ungültig.

```dart
  test('test13', () {
    expect(isValid(":9"), false, reason: '--err-t13--');
  });
```

Symbole machen die Zahl ungültig.

```dart
  test('test14', () {
    expect(isValid("055# 444\$ 285"), false, reason: '--err-t14--');
  });
```

Ein leerer String ist nicht gültig.

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
