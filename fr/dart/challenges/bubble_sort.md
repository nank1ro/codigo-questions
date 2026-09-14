---
language: dart
exerciseType: 1
difficulty: 2
title: Tri à bulles
---

# --description--

Le tri à bulles est l'un des algorithmes de tri les plus simples. Il parcourt une liste et compare chaque paire d'éléments adjacents, en les échangeant dès qu'ils sont dans le mauvais ordre. Après chaque passage complet, la plus grande valeur restante a « remonté » jusqu'à sa position finale, et la liste est triée dès qu'un passage se termine sans le moindre échange.

# --instructions--

Écrivez une fonction appelée `bubbleSort` qui prend une `List<int>` et retourne une **nouvelle** liste avec les mêmes valeurs triées par ordre croissant. La liste passée en paramètre ne doit pas être modifiée.

Vous devez implémenter l'algorithme de tri à bulles vous-même, en comparant et en échangeant les éléments adjacents. N'utilisez pas de fonction de tri de la bibliothèque standard.

Votre fonction doit également fonctionner avec un tableau vide, un tableau d'un seul élément, un tableau déjà trié, des valeurs répétées et des nombres négatifs.

Exemple d'appel de fonction :
```dart
print(bubbleSort([3, 1, 2]));
// prints [1, 2, 3]
```

# --seed--

```dart
List<int> bubbleSort(List<int> arr) {
    
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

Un tableau vide doit retourner un tableau vide

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

Un tableau d'un seul élément doit rester identique

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

Un tableau déjà trié doit conserver le même ordre

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

Un tableau trié à l'envers doit être mis en ordre croissant

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

Toutes les valeurs répétées doivent être conservées

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

Les nombres négatifs doivent être triés avant les positifs

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

Un tableau mixte plus long doit être trié par ordre croissant

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

La liste passée en paramètre ne doit pas être modifiée

```dart
    test("test8", () {
      final original = [3, 1, 2];
      bubbleSort(original);
      expect(original, [3, 1, 2], reason: "--err-t8--");
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
List<int> bubbleSort(List<int> arr) {
    final result = List<int>.from(arr);
    var end = result.length;
    var swapped = true;
    while (swapped) {
        swapped = false;
        for (var i = 1; i < end; i++) {
            if (result[i - 1] > result[i]) {
                final temp = result[i - 1];
                result[i - 1] = result[i];
                result[i] = temp;
                swapped = true;
            }
        }
        end--;
    }
    return result;
}
```
