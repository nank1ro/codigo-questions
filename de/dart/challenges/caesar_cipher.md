---
language: dart
exerciseType: 1
difficulty: 2
title: Caesar-Verschlüsselung
---

# --description--

Julius Caesar schützte seine privaten Briefe mit einem der ältesten Tricks der Kryptografie: Er ersetzte jeden Buchstaben einer Nachricht durch den Buchstaben, der eine feste Anzahl von Stellen weiter hinten im Alphabet steht. Bei einer Verschiebung von 3 wird `a` zu `d`, `b` zu `e` und `c` zu `f`.

Das Alphabet verhält sich wie ein Kreis, daher laufen die Buchstaben am Ende wieder zum Anfang zurück: Bei einer Verschiebung von 3 wird `x` zu `a`, `y` zu `b` und `z` zu `c`.

Alles, was kein Buchstabe ist, etwa ein Leerzeichen, ein Komma, ein Ausrufezeichen oder eine Ziffer, durchläuft die Verschlüsselung unverändert.

# --instructions--

Schreiben Sie eine Funktion `caesarCipher`, die eine Nachricht `text` und eine ganze Zahl `shift` entgegennimmt und die verschlüsselte Nachricht zurückgibt.

Beispiele:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Die Nachricht besteht immer aus Kleinbuchstaben, Sie müssen sich also nie um Großbuchstaben kümmern.
- Zeichen, die keine Buchstaben sind, behalten ihren Platz und ihren Wert.
- Die Verschiebung ist nie negativ. Eine Verschiebung von `0` lässt die Nachricht unverändert, und eine Verschiebung von `26` ebenfalls.

# --seed--

```dart
String caesarCipher(String text, int shift) {
  
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

Eine Verschiebung von 3 macht aus "hello" "khoor"

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

Die Buchstaben am Ende des Alphabets laufen zum Anfang zurück, daher wird "xyz" zu "abc"

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

Eine Verschiebung von 0 lässt die Nachricht unverändert

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

Eine Verschiebung von 26 ist eine volle Runde durch das Alphabet, daher bleibt die Nachricht unverändert

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

Satzzeichen und Leerzeichen werden unverändert durchgereicht

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

Eine leere Nachricht bleibt leer

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

Leerzeichen zwischen einzelnen Buchstaben bleiben erhalten

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

Ziffern werden nicht verschoben, auch nicht bei einer Verschiebung von 25

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

Eine Verschiebung von 13 verschlüsselt einen ganzen Satz

```dart
  test('test9', () {
    expect(caesarCipher('the quick brown fox jumps over the lazy dog', 13), 'gur dhvpx oebja sbk whzcf bire gur ynml qbt', reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String caesarCipher(String text, int shift) {
  final a = 'a'.codeUnitAt(0);
  final z = 'z'.codeUnitAt(0);
  final encoded = <int>[];

  for (final code in text.codeUnits) {
    if (code >= a && code <= z) {
      encoded.add(a + (code - a + shift) % 26);
    } else {
      encoded.add(code);
    }
  }

  return String.fromCharCodes(encoded);
}
```
