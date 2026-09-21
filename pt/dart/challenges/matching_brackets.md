---
language: dart
exerciseType: 1
difficulty: 3
title: Colchetes correspondentes
---

# --description--

Textos que contêm código, matemática ou marcação estão cheios de colchetes, e todo colchete de abertura precisa de um colchete de fechamento do mesmo tipo. Uma string está balanceada quando seus colchetes formam pares e se aninham como as camadas de uma cebola: `{[()]}` está balanceada, enquanto `{[(])}` não está, porque o par redondo é fechado antes do par de colchetes dentro do qual ele está.

Três pares contam aqui: parênteses `()`, colchetes `[]` e chaves `{}`. Todos os outros caracteres da string são ignorados. Um colchete de fechamento deve fechar o colchete aberto mais recentemente que ainda esteja aberto, e quando a string termina nenhum colchete pode ficar aberto.

# --instructions--

Escreva uma função `isBalanced` que recebe uma string e retorna `true` quando todos os colchetes nela estão correspondidos e corretamente aninhados, e `false` caso contrário.

Exemplos:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Uma string vazia está balanceada.
- Caracteres que não são colchetes são ignorados.
- Um colchete de fechamento deve corresponder ao colchete aberto mais recentemente que ainda esteja aberto.
- Nenhum colchete pode ficar aberto quando a string termina.

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

Uma string vazia está balanceada

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

Um único par de parênteses está balanceado

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

Os três tipos de par aninhados uns dentro dos outros estão balanceados

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

Colchetes misturados com outro texto ainda estão balanceados

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

Pares colocados lado a lado estão balanceados

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

Uma string sem nenhum colchete está balanceada

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

Um par cruzado não está balanceado

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

Um colchete de abertura que nunca é fechado não está balanceado

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

Um colchete de fechamento antes de qualquer colchete de abertura não está balanceado

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

Pares cruzados mais no fundo da string não estão balanceados

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

Um colchete de fechamento que sobra no final não está balanceado

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
