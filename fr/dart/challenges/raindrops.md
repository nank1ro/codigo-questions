---
language: dart
exerciseType: 1
difficulty: 1
title: Gouttes de pluie
---

# --description--

Votre tâche est de convertir un nombre en une chaîne qui contient des sons de gouttes de pluie correspondant à certains facteurs potentiels.
Un facteur est un nombre qui divise uniformément un autre nombre, sans laisser de reste.
Le moyen le plus simple de tester si un nombre est un facteur d'un autre est d'utiliser l'opération modulo.
Les règles des gouttes de pluie sont que si un nombre donné :

- a 3 comme facteur, ajoutez 'Pling' au résultat.
- a 5 comme facteur, ajoutez 'Plang' au résultat.
- a 7 comme facteur, ajoutez 'Plong' au résultat.
- n'a pas 3, 5 ou 7 comme facteur, le résultat doit être les chiffres du nombre.

# --instructions--

Écrivez une fonction qui retourne la chaîne correcte, exemples :

- 28 a 7 comme facteur, mais pas 3 ou 5, donc le résultat serait `"Plong"`.
- 30 a à la fois 3 et 5 comme facteurs, mais pas 7, donc le résultat serait `"PlingPlang"`.
- 34 n'est pas factorisé par 3, 5 ou 7, donc le résultat serait `"34"`.

Exemple d'appel de fonction :
```dart
print(raindrops(28))
// prints "Plong"
```

# --seed--

```dart
String raindrops() {

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

Le son pour 1 est "1"

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

Le son pour 3 est "Pling"

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

Le son pour 5 est "Plang"

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

Le son pour 7 est "Plong"

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

Le son pour 6 est "Pling"

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

Le son pour 8 est "8"

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

Le son pour 9 est "Pling"

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

Le son pour 10 est "Plang"

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

Le son pour 14 est "Plong"

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

Le son pour 15 est "PlingPlang"

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

Le son pour 21 est "PlingPlong"

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

Le son pour 25 est "Plang"

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

Le son pour 27 est "Pling"

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

Le son pour 35 est "PlangPlong"

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

Le son pour 49 est "Plong"

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

Le son pour 52 est "52"

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

Le son pour 105 est "PlingPlangPlong"

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

Le son pour 3125 est "Plang"

```dart
  test('test18', () {
    expect(raindrops(3125), "Plang", reason: '--err-t18--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String raindrops(int number) {
  var result = "";
  if (number % 3 == 0) {
    result += "Pling";
  }
  if (number % 5 == 0) {
    result += "Plang";
  }
  if (number % 7 == 0) {
    result += "Plong";
  }
  if (result.isEmpty) {
    result = number.toString();
  }
  return result;
}
```
