---
language: dart
exerciseType: 1
difficulty: 1
title: Dois por um
---

# --description--

Dado um nome, retorne uma string com a mensagem:
`One for X, one for me.`
Onde `X` é o nome fornecido.
No entanto, se o nome estiver ausente, retorne a string:
`One for you, one for me.`

# --instructions--

Escreva uma função que retorne a string correta, exemplos:

**entrada**: `Walter`
**saída**: `One for Walter, one for me.`

**entrada**: `James`
**saída**: `One for James, one for me.`

**entrada**: `Martha`
**saída**: `One for Martha, one for me.`

# --seed--

```dart
String twoForOne() {
  
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

Nenhum nome fornecido

```dart
  test('test1', () {
    expect(twoForOne(), "One for you, one for me.", reason: '--err-t1--');
  });
```

Passar "James" como nome

```dart
  test('test2', () {
    expect(twoForOne(name: "James"), "One for James, one for me.", reason: '--err-t2--');
  });
```

Passar "Martha" como nome

```dart
  test('test3', () {
    expect(twoForOne(name: "Martha"), "One for Martha, one for me.", reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String twoForOne({String? name}) {
  if (name != null) {
    return "One for $name, one for me.";
  }
  return "One for you, one for me.";
}
```


