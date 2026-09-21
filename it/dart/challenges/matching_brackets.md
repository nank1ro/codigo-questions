---
language: dart
exerciseType: 1
difficulty: 3
title: Parentesi bilanciate
---

# --description--

Il testo che contiene codice, formule matematiche o markup è pieno di parentesi, e ogni parentesi aperta ha bisogno di una chiusa dello stesso tipo. Una stringa è bilanciata quando le sue parentesi si accoppiano e si annidano come gli strati di una cipolla: `{[()]}` è bilanciata, mentre `{[(])}` non lo è, perché la coppia tonda viene chiusa prima della coppia quadrata al cui interno si trova.

Qui contano tre coppie: le tonde `()`, le quadre `[]` e le graffe `{}`. Ogni altro carattere della stringa viene ignorato. Una parentesi chiusa deve chiudere la parentesi aperta più di recente che risulta ancora aperta, e quando la stringa termina nessuna parentesi può rimanere aperta.

# --instructions--

Scrivi una funzione `isBalanced` che prende una stringa e restituisce `true` quando tutte le parentesi in essa contenute sono accoppiate e correttamente annidate, e `false` altrimenti.

Esempi:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Una stringa vuota è bilanciata.
- I caratteri che non sono parentesi vengono ignorati.
- Una parentesi chiusa deve corrispondere alla parentesi aperta più di recente che risulta ancora aperta.
- Nessuna parentesi può rimanere aperta quando la stringa termina.

# --seed--

```dart
bool isBalanced(String text) {
  
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

Una stringa vuota è bilanciata

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

Una singola coppia di parentesi tonde è bilanciata

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

I tre tipi di coppia annidati l'uno dentro l'altro sono bilanciati

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

Parentesi mescolate ad altro testo restano comunque bilanciate

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

Coppie poste una accanto all'altra sono bilanciate

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

Una stringa senza alcuna parentesi è bilanciata

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

Una coppia incrociata non è bilanciata

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

Una parentesi aperta che non viene mai chiusa non è bilanciata

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

Una parentesi chiusa prima di qualsiasi parentesi aperta non è bilanciata

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

Coppie incrociate più in profondità nella stringa non sono bilanciate

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

Una parentesi chiusa lasciata alla fine non è bilanciata

```dart
  test('test11', () {
    expect(isBalanced('())'), false, reason: '--err-t11--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isBalanced(String text) {
  const pairs = {')': '(', ']': '[', '}': '{'};
  final stack = <String>[];

  for (final char in text.split('')) {
    if (char == '(' || char == '[' || char == '{') {
      stack.add(char);
    } else if (pairs.containsKey(char)) {
      if (stack.isEmpty || stack.removeLast() != pairs[char]) {
        return false;
      }
    }
  }

  return stack.isEmpty;
}
```
