---
language: dart
exerciseType: 1
difficulty: 2
title: Cifrario di Cesare
---

# --description--

Giulio Cesare proteggeva le sue lettere private con uno dei trucchi più antichi della crittografia: sostituiva ogni lettera di un messaggio con la lettera che si trova un numero fisso di posizioni più avanti nell'alfabeto. Con uno spostamento di 3, `a` diventa `d`, `b` diventa `e` e `c` diventa `f`.

L'alfabeto si comporta come un cerchio, quindi le lettere della fine tornano all'inizio: con uno spostamento di 3, `x` diventa `a`, `y` diventa `b` e `z` diventa `c`.

Tutto ciò che non è una lettera, come uno spazio, una virgola, un punto esclamativo o una cifra, attraversa il cifrario senza subire modifiche.

# --instructions--

Scrivi una funzione `caesarCipher` che riceve un messaggio `text` e un numero intero `shift`, e restituisce il messaggio codificato.

Esempi:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Il messaggio è sempre in minuscolo, quindi non dovrai mai occuparti delle lettere maiuscole.
- I caratteri che non sono lettere mantengono la loro posizione e il loro valore.
- Lo spostamento non è mai negativo. Uno spostamento di `0` lascia il messaggio invariato, e così anche uno spostamento di `26`.

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

Uno spostamento di 3 trasforma "hello" in "khoor"

```dart
  test('test1', () {
    expect(caesarCipher('hello', 3), 'khoor', reason: '--err-t1--');
  });
```

La fine dell'alfabeto ricomincia da capo, quindi "xyz" diventa "abc"

```dart
  test('test2', () {
    expect(caesarCipher('xyz', 3), 'abc', reason: '--err-t2--');
  });
```

Uno spostamento di 0 lascia il messaggio invariato

```dart
  test('test3', () {
    expect(caesarCipher('abc', 0), 'abc', reason: '--err-t3--');
  });
```

Uno spostamento di 26 è un giro completo dell'alfabeto, quindi il messaggio resta invariato

```dart
  test('test4', () {
    expect(caesarCipher('abc', 26), 'abc', reason: '--err-t4--');
  });
```

Punteggiatura e spazi passano invariati

```dart
  test('test5', () {
    expect(caesarCipher('codigo, rocks!', 5), 'htinlt, wthpx!', reason: '--err-t5--');
  });
```

Un messaggio vuoto resta vuoto

```dart
  test('test6', () {
    expect(caesarCipher('', 4), '', reason: '--err-t6--');
  });
```

Gli spazi tra singole lettere vengono preservati

```dart
  test('test7', () {
    expect(caesarCipher('a b c', 1), 'b c d', reason: '--err-t7--');
  });
```

Le cifre non vengono spostate, nemmeno con uno spostamento di 25

```dart
  test('test8', () {
    expect(caesarCipher('abc 123!', 25), 'zab 123!', reason: '--err-t8--');
  });
```

Uno spostamento di 13 codifica una frase intera

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
