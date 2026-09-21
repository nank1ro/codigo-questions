---
language: dart
exerciseType: 1
difficulty: 3
title: Corchetes coincidentes
---

# --description--

El texto que contiene código, matemáticas o marcado está lleno de corchetes, y cada corchete de apertura necesita uno de cierre de la misma clase. Una cadena está equilibrada cuando sus corchetes se emparejan y se anidan como las capas de una cebolla: `{[()]}` está equilibrada, mientras que `{[(])}` no lo está, porque el par redondo se cierra antes que el par cuadrado dentro del cual se encuentra.

Aquí cuentan tres pares: paréntesis `()`, corchetes `[]` y llaves `{}`. Todos los demás caracteres de la cadena se ignoran. Un corchete de cierre debe cerrar el último corchete que se haya abierto y que aún siga abierto, y cuando la cadena termina no debe quedar ningún corchete abierto.

# --instructions--

Escribe una función `isBalanced` que tome una cadena y devuelva `true` cuando todos los corchetes que contiene estén emparejados y anidados correctamente, y `false` en caso contrario.

Ejemplos:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Una cadena vacía está equilibrada.
- Los caracteres que no son corchetes se ignoran.
- Un corchete de cierre debe corresponder al último corchete que se haya abierto y que aún siga abierto.
- No debe quedar ningún corchete abierto cuando la cadena termina.

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

Una cadena vacía está equilibrada

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

Un solo par de paréntesis está equilibrado

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

Los tres tipos de pares anidados unos dentro de otros están equilibrados

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

Los corchetes mezclados con otro texto siguen estando equilibrados

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

Los pares colocados uno al lado del otro están equilibrados

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

Una cadena sin ningún corchete está equilibrada

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

Un par cruzado no está equilibrado

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

Un corchete de apertura que nunca se cierra no está equilibrado

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

Un corchete de cierre antes de cualquier corchete de apertura no está equilibrado

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

Los pares cruzados en lo profundo de la cadena no están equilibrados

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

Un corchete de cierre que sobra al final no está equilibrado

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
