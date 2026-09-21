---
language: dart
exerciseType: 1
difficulty: 2
title: Codifica run-length
---

# --description--

La codifica run-length è uno dei trucchi di compressione più antichi che esistano: invece di scrivere più e più volte lo stesso carattere, scrivi quante volte si ripete e poi il carattere stesso.

Un fax che scansiona una pagina quasi tutta bianca incontra lunghe distese di pixel identici, così una riga di dodici `W` viaggia lungo la linea come la ben più corta `12W`. Quando un carattere compare una sola volta, contarlo non porta nessun vantaggio, quindi viene copiato da solo.

# --instructions--

Scrivi una funzione `encodeRun` che riceve una stringa `text` e restituisce la sua forma codificata run-length.

Ogni sequenza dello stesso carattere ripetuto due o più volte diventa la lunghezza della sequenza scritta in decimale, seguita da quel carattere. Una sequenza di lunghezza uno viene copiata come singolo carattere, senza nessun numero davanti.

Esempi:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Il testo contiene solo lettere maiuscole dalla `A` alla `Z` e spazi.
- Una sequenza più lunga di nove caratteri usa il suo conteggio decimale completo, quindi dodici `W` diventano `12W` e mai `9W3W`.
- Gli spazi sono caratteri normali: vengono contati e codificati esattamente come le lettere.
- La stringa vuota si codifica nella stringa vuota.

# --seed--

```dart
String encodeRun(String text) {
  
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

La stringa vuota si codifica nella stringa vuota

```dart
  test('test1', () {
    expect(encodeRun(''), '', reason: '--err-t1--');
  });
```

Un singolo carattere viene copiato così com'è

```dart
  test('test2', () {
    expect(encodeRun('A'), 'A', reason: '--err-t2--');
  });
```

Una stringa senza ripetizioni attraversa il processo invariata

```dart
  test('test3', () {
    expect(encodeRun('ABCDE'), 'ABCDE', reason: '--err-t3--');
  });
```

Una sequenza di due diventa il conteggio seguito dal carattere

```dart
  test('test4', () {
    expect(encodeRun('AA'), '2A', reason: '--err-t4--');
  });
```

L'esempio misto "AABCCCDEEEE" diventa "2AB3CD4E"

```dart
  test('test5', () {
    expect(encodeRun('AABCCCDEEEE'), '2AB3CD4E', reason: '--err-t5--');
  });
```

Una sequenza di dodici usa il suo conteggio decimale completo, quindi il risultato inizia con "12W"

```dart
  test('test6', () {
    expect(encodeRun('WWWWWWWWWWWWBWW'), '12WB2W', reason: '--err-t6--');
  });
```

Le sequenze di spazi vengono codificate esattamente come le sequenze di lettere

```dart
  test('test7', () {
    expect(encodeRun('  HI  '), '2 HI2 ', reason: '--err-t7--');
  });
```

Una sequenza di dieci viene scritta come "10A", mai come due sequenze più corte

```dart
  test('test8', () {
    expect(encodeRun('AAAAAAAAAA'), '10A', reason: '--err-t8--');
  });
```

I caratteri singoli che si alternano vengono tutti copiati così come sono

```dart
  test('test9', () {
    expect(encodeRun('ABABAB'), 'ABABAB', reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String encodeRun(String text) {
  final result = StringBuffer();
  var i = 0;

  while (i < text.length) {
    var run = 1;
    while (i + run < text.length && text[i + run] == text[i]) {
      run++;
    }
    if (run > 1) {
      result.write(run);
    }
    result.write(text[i]);
    i += run;
  }

  return result.toString();
}
```
