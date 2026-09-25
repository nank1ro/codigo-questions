---
language: dart
exerciseType: 1
difficulty: 2
title: Codificación por longitud de serie
---

# --description--

La codificación por longitud de serie es uno de los trucos de compresión más antiguos que existen: en lugar de escribir el mismo carácter una y otra vez, escribes cuántas veces se repite y luego el propio carácter.

Una máquina de fax que escanea una página casi en blanco se encuentra con largas tiras de píxeles idénticos, así que una fila de doce `W` viaja por la línea como el mucho más corto `12W`. Cuando un carácter aparece solo una vez no hay nada que ganar contándolo, así que se copia tal cual.

# --instructions--

Escribe una función `encodeRun` que reciba una cadena `text` y devuelva su forma codificada por longitud de serie.

Cada serie del mismo carácter repetido dos o más veces se convierte en la longitud de la serie escrita en decimal, seguida de ese carácter. Una serie de longitud uno se copia como el único carácter, sin ningún número delante.

Ejemplos:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- El texto contiene solo letras mayúsculas de la `A` a la `Z` y espacios.
- Una serie de más de nueve caracteres usa su conteo decimal completo, así que doce `W` se convierten en `12W` y nunca en `9W3W`.
- Los espacios son caracteres ordinarios: se cuentan y se codifican exactamente igual que las letras.
- La cadena vacía se codifica como la cadena vacía.

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

La cadena vacía se codifica como la cadena vacía

```dart
  test('test1', () {
    expect(encodeRun(''), '', reason: '--err-t1--');
  });
```

Un solo carácter se copia tal cual

```dart
  test('test2', () {
    expect(encodeRun('A'), 'A', reason: '--err-t2--');
  });
```

Una cadena sin repeticiones pasa sin cambios

```dart
  test('test3', () {
    expect(encodeRun('ABCDE'), 'ABCDE', reason: '--err-t3--');
  });
```

Una serie de dos se convierte en el conteo seguido del carácter

```dart
  test('test4', () {
    expect(encodeRun('AA'), '2A', reason: '--err-t4--');
  });
```

El ejemplo mixto "AABCCCDEEEE" se convierte en "2AB3CD4E"

```dart
  test('test5', () {
    expect(encodeRun('AABCCCDEEEE'), '2AB3CD4E', reason: '--err-t5--');
  });
```

Una serie de doce usa su conteo decimal completo, así que el resultado empieza con "12W"

```dart
  test('test6', () {
    expect(encodeRun('WWWWWWWWWWWWBWW'), '12WB2W', reason: '--err-t6--');
  });
```

Las series de espacios se codifican igual que las series de letras

```dart
  test('test7', () {
    expect(encodeRun('  HI  '), '2 HI2 ', reason: '--err-t7--');
  });
```

Una serie de diez se escribe como "10A", nunca como dos series más cortas

```dart
  test('test8', () {
    expect(encodeRun('AAAAAAAAAA'), '10A', reason: '--err-t8--');
  });
```

Los caracteres sueltos que se alternan se copian todos tal cual

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
