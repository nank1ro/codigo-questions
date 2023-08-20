---
language: dart
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

In un anno solare ci sono esattamente 365.25 giorni. Ma questo poteva portare confusione perché gli esseri umani normalmente contano in base all'esatta divisibilità di 1 e non con i punti decimali. Quindi, per evitare quest'ultimo problema, si decise di sommare tutti gli 0.25 giorni ogni ciclo di quattro anni e dare a quell'anno 366 giorni (includendo il 29 febbraio come giorno intercalare) e chiamarlo __anno bisestile__. Gli altri tre anni del ciclo quadriennale contengono solo 365 giorni e non sono __anni bisestili__.

# --instructions--

In questa sfida ci spingeremo ad un nuovo livello, in cui dovremo determinare se si tratta di un anno bisestile o meno senza l'uso della classe `DateTime`, delle dichiarazioni `switch`, dei blocchi __if__, __if-else__ o delle __operazioni ausiliarie__ (`x ? a : b`) né degli operatori logici __AND__ (`&&`) e __OR__ (`||`) con l'eccezione dell'operatore __NOT__ (`!`).

Restituisci `true` se è un anno bisestile, `false` altrimenti.

Esempio di chiamata di funzione:
```dart
print(leapYear(2000));
// stampa true
```

# --seed--

```dart
bool leapYear(int year) {
  
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

L'uso di `DateTime`, `switch`, `if`, `else`, `&&`, `||` o `?` non è consentito.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

L'anno `2016` è bisestile.

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

L'anno `1996` è bisestile.

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

L'anno `1600` è bisestile.

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

L'anno `2020` è bisestile.

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

L'anno `2000` è bisestile.

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

L'anno `2008` è bisestile.

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

L'anno `1521` non è bisestile.

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

L'anno `1800` non è bisestile.

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

L'anno `2007` non è bisestile.

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

L'anno `2002` non è bisestile.

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

L'anno `1979` non è bisestile.

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

L'anno `2006` non è bisestile.

```dart
  test('test12', () {
    expect(leapYear(2006), false, reason: '--err-t12--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool leapYear(int year) {
  return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0));
}
```
