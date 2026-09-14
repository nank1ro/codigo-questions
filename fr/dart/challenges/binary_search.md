---
language: dart
exerciseType: 1
difficulty: 2
title: Recherche binaire
---

# --description--

La recherche binaire trouve une valeur dans une collection **triée** en divisant à plusieurs reprises la plage de recherche par deux : regarde l'élément du milieu et, si ce n'est pas celui que tu cherches, continue dans la moitié gauche lorsque la valeur cherchée est plus petite ou dans la moitié droite lorsqu'elle est plus grande.

Comme chaque étape écarte la moitié des éléments restants, la recherche binaire atteint la réponse en quelques comparaisons même sur de très grandes collections, alors que vérifier les éléments un par un coûterait autant d'étapes qu'il y a d'éléments.

# --instructions--

Écris une fonction `binarySearch` qui prend une liste d'entiers triée par ordre croissant et un entier cherché, et renvoie l'index de la valeur cherchée dans la liste, ou `-1` lorsque la valeur n'est pas présente.

La liste ne contient jamais de doublons, l'index est donc toujours unique. La liste peut aussi être vide. Ta fonction doit utiliser la recherche binaire, en divisant la plage de recherche par deux à chaque étape, et non un parcours linéaire.

Exemple d'appel de fonction :
```dart
print(binarySearch([1, 3, 5, 7], 5));
// prints 2
```

# --seed--

```dart
int binarySearch() {

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

Rechercher dans une liste vide doit renvoyer -1

```dart
  test('test1', () {
    expect(binarySearch([], 7), -1, reason: '--err-t1--');
  });
```

Rechercher 5 dans `[5]` doit renvoyer 0

```dart
  test('test2', () {
    expect(binarySearch([5], 5), 0, reason: '--err-t2--');
  });
```

Rechercher 9 dans `[5]` doit renvoyer -1

```dart
  test('test3', () {
    expect(binarySearch([5], 9), -1, reason: '--err-t3--');
  });
```

Le premier élément -9 de la liste de 12 éléments doit être trouvé à l'index 0

```dart
  test('test4', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, reason: '--err-t4--');
  });
```

Le dernier élément 78 de la liste de 12 éléments doit être trouvé à l'index 11

```dart
  test('test5', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, reason: '--err-t5--');
  });
```

L'élément 15 doit être trouvé à l'index 6

```dart
  test('test6', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, reason: '--err-t6--');
  });
```

L'élément 22 doit être trouvé à l'index 7

```dart
  test('test7', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, reason: '--err-t7--');
  });
```

La valeur 12, qui se situe entre 11 et 15, doit renvoyer -1

```dart
  test('test8', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, reason: '--err-t8--');
  });
```

Une valeur cherchée plus petite que tous les éléments doit renvoyer -1

```dart
  test('test9', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, reason: '--err-t9--');
  });
```

Une valeur cherchée plus grande que tous les éléments doit renvoyer -1

```dart
  test('test10', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100), -1, reason: '--err-t10--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int binarySearch(List<int> arr, int target) {
  var low = 0;
  var high = arr.length - 1;
  while (low <= high) {
    final mid = low + (high - low) ~/ 2;
    if (arr[mid] == target) {
      return mid;
    }
    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return -1;
}
```
