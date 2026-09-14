---
language: dart
exerciseType: 1
difficulty: 2
title: Checksum di Luhn
---

# --description--

L'algoritmo di Luhn è un semplice checksum usato per validare numeri identificativi, come i numeri delle carte di credito.

Prima di controllare un numero, rimuovi ogni spazio dalla stringa. La stringa è valida solo se ciò che resta è più lungo di un carattere e la stringa originale non contiene altro che cifre e spazi.

Per eseguire il controllo, parti dalla cifra più a destra e procedi verso sinistra, raddoppiando una cifra su due. Quando il raddoppio produce un numero maggiore di 9, sottrai 9. Poi somma tutte le cifre: il numero è valido solo se la somma è divisibile per 10.

Ad esempio, `"059"` dà `0`, poi `5` raddoppiato è `10` che diventa `1`, poi `9`. La loro somma è `10`, che è divisibile per 10, quindi il numero è valido.

# --instructions--

Scrivi una funzione `isValid` che riceve una stringa e restituisce `true` quando il numero è valido, `false` altrimenti.

- `"4539 3195 0343 6467"` passa il checksum, quindi il risultato è `true`.
- `"8273 1232 7352 0569"` non passa il checksum, quindi il risultato è `false`.
- `"0"` è lungo solo un carattere, quindi il risultato è `false`.
- `"055-444-285"` contiene un carattere che non è una cifra né uno spazio, quindi il risultato è `false`.

Esempio di chiamata di funzione:
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

Una singola cifra non è valida.

```dart
  test('test1', () {
    expect(isValid("0"), false, reason: '--err-t1--');
  });
```

Una singola cifra preceduta da uno spazio non è valida.

```dart
  test('test2', () {
    expect(isValid(" 0"), false, reason: '--err-t2--');
  });
```

Il numero `"059"` è valido.

```dart
  test('test3', () {
    expect(isValid("059"), true, reason: '--err-t3--');
  });
```

Il numero `"59"` è valido.

```dart
  test('test4', () {
    expect(isValid("59"), true, reason: '--err-t4--');
  });
```

Il numero `"055 444 285"` è valido.

```dart
  test('test5', () {
    expect(isValid("055 444 285"), true, reason: '--err-t5--');
  });
```

Il numero `"055 444 286"` non è valido.

```dart
  test('test6', () {
    expect(isValid("055 444 286"), false, reason: '--err-t6--');
  });
```

Il numero `"8273 1232 7352 0569"` non è valido.

```dart
  test('test7', () {
    expect(isValid("8273 1232 7352 0569"), false, reason: '--err-t7--');
  });
```

Il numero `"4539 3195 0343 6467"` è valido.

```dart
  test('test8', () {
    expect(isValid("4539 3195 0343 6467"), true, reason: '--err-t8--');
  });
```

Il numero `"1 2345 6789 1234 5678 9012"` non è valido.

```dart
  test('test9', () {
    expect(isValid("1 2345 6789 1234 5678 9012"), false, reason: '--err-t9--');
  });
```

Il numero `"095 245 88"` è valido.

```dart
  test('test10', () {
    expect(isValid("095 245 88"), true, reason: '--err-t10--');
  });
```

Una lettera rende il numero non valido.

```dart
  test('test11', () {
    expect(isValid("055a 444 285"), false, reason: '--err-t11--');
  });
```

I trattini rendono il numero non valido.

```dart
  test('test12', () {
    expect(isValid("055-444-285"), false, reason: '--err-t12--');
  });
```

Un carattere di punteggiatura rende il numero non valido.

```dart
  test('test13', () {
    expect(isValid(":9"), false, reason: '--err-t13--');
  });
```

I simboli rendono il numero non valido.

```dart
  test('test14', () {
    expect(isValid("055# 444\$ 285"), false, reason: '--err-t14--');
  });
```

Una stringa vuota non è valida.

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
