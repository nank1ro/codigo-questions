---
language: dart
exerciseType: 1
difficulty: 2
title: Luhn checksum
---

# --description--

L'algorithme de Luhn est une somme de contrôle simple utilisée pour valider des numéros d'identification, tels que les numéros de carte bancaire.

Avant de vérifier un numéro, supprimez tous les espaces de la chaîne. La chaîne est valide uniquement si ce qui reste contient plus d'un caractère et si la chaîne d'origine ne contient rien d'autre que des chiffres et des espaces.

Pour effectuer la vérification, partez du chiffre le plus à droite et progressez vers la gauche en doublant un chiffre sur deux. Lorsque le doublement produit un nombre supérieur à 9, soustrayez-lui 9. Additionnez ensuite tous les chiffres : le numéro est valide uniquement si la somme est divisible par 10.

Par exemple, `"059"` donne `0`, puis `5` doublé donne `10`, qui devient `1`, puis `9`. Leur somme est `10`, qui est divisible par 10, donc le numéro est valide.

# --instructions--

Écrivez une fonction `isValid` qui prend une chaîne et retourne `true` lorsque le numéro est valide, `false` sinon.

- `"4539 3195 0343 6467"` passe la somme de contrôle, donc le résultat est `true`.
- `"8273 1232 7352 0569"` échoue à la somme de contrôle, donc le résultat est `false`.
- `"0"` ne contient qu'un seul caractère, donc le résultat est `false`.
- `"055-444-285"` contient un caractère qui n'est ni un chiffre ni un espace, donc le résultat est `false`.

Exemple d'appel de fonction :
```dart
print(isValid("095 245 88"));
// prints true
```

# --seed--

```dart
bool isValid(String value) {
  
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

Un chiffre seul n'est pas valide.

```dart
  test('test1', () {
    expect(isValid("0"), false, reason: '--err-t1--');
  });
```

Un chiffre seul avec un espace au début n'est pas valide.

```dart
  test('test2', () {
    expect(isValid(" 0"), false, reason: '--err-t2--');
  });
```

Le numéro `"059"` est valide.

```dart
  test('test3', () {
    expect(isValid("059"), true, reason: '--err-t3--');
  });
```

Le numéro `"59"` est valide.

```dart
  test('test4', () {
    expect(isValid("59"), true, reason: '--err-t4--');
  });
```

Le numéro `"055 444 285"` est valide.

```dart
  test('test5', () {
    expect(isValid("055 444 285"), true, reason: '--err-t5--');
  });
```

Le numéro `"055 444 286"` n'est pas valide.

```dart
  test('test6', () {
    expect(isValid("055 444 286"), false, reason: '--err-t6--');
  });
```

Le numéro `"8273 1232 7352 0569"` n'est pas valide.

```dart
  test('test7', () {
    expect(isValid("8273 1232 7352 0569"), false, reason: '--err-t7--');
  });
```

Le numéro `"4539 3195 0343 6467"` est valide.

```dart
  test('test8', () {
    expect(isValid("4539 3195 0343 6467"), true, reason: '--err-t8--');
  });
```

Le numéro `"1 2345 6789 1234 5678 9012"` n'est pas valide.

```dart
  test('test9', () {
    expect(isValid("1 2345 6789 1234 5678 9012"), false, reason: '--err-t9--');
  });
```

Le numéro `"095 245 88"` est valide.

```dart
  test('test10', () {
    expect(isValid("095 245 88"), true, reason: '--err-t10--');
  });
```

Une lettre rend le numéro invalide.

```dart
  test('test11', () {
    expect(isValid("055a 444 285"), false, reason: '--err-t11--');
  });
```

Les tirets rendent le numéro invalide.

```dart
  test('test12', () {
    expect(isValid("055-444-285"), false, reason: '--err-t12--');
  });
```

Un caractère de ponctuation rend le numéro invalide.

```dart
  test('test13', () {
    expect(isValid(":9"), false, reason: '--err-t13--');
  });
```

Les symboles rendent le numéro invalide.

```dart
  test('test14', () {
    expect(isValid("055# 444\$ 285"), false, reason: '--err-t14--');
  });
```

Une chaîne vide n'est pas valide.

```dart
  test('test15', () {
    expect(isValid(""), false, reason: '--err-t15--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isValid(String value) {
  var sum = 0;
  var count = 0;
  for (var i = value.length - 1; i >= 0; i--) {
    final code = value.codeUnitAt(i);
    if (code == 32) {
      continue;
    }
    if (code < 48 || code > 57) {
      return false;
    }
    var digit = code - 48;
    if (count % 2 == 1) {
      digit *= 2;
      if (digit > 9) {
        digit -= 9;
      }
    }
    sum += digit;
    count++;
  }
  return count > 1 && sum % 10 == 0;
}
```
