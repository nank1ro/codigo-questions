---
language: dart
exerciseType: 1
difficulty: 2
title: Sortowanie bąbelkowe
---

# --description--

Sortowanie bąbelkowe to jeden z najprostszych algorytmów sortowania. Przechodzi przez listę i porównuje każdą parę sąsiednich elementów, zamieniając je miejscami zawsze, gdy są w złej kolejności. Po każdym pełnym przejściu największa z pozostałych wartości „wypływa” na swoje ostateczne miejsce, a lista jest posortowana, gdy tylko przejście zakończy się bez ani jednej zamiany.

# --instructions--

Napisz funkcję o nazwie `bubbleSort`, która przyjmuje `List<int>` i zwraca **nową** listę z tymi samymi wartościami posortowanymi w kolejności rosnącej. Przekazana lista nie może zostać zmodyfikowana.

Musisz samodzielnie zaimplementować algorytm sortowania bąbelkowego, porównując i zamieniając sąsiednie elementy. Nie używaj funkcji sortującej z biblioteki standardowej.

Twoja funkcja musi działać również dla pustej tablicy, tablicy z jednym elementem, tablicy już posortowanej, powtarzających się wartości i liczb ujemnych.

Przykład wywołania funkcji:
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

Pusta tablica musi zwrócić pustą tablicę

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

Tablica z jednym elementem musi pozostać taka sama

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

Już posortowana tablica musi zachować tę samą kolejność

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

Tablica posortowana odwrotnie musi zostać uporządkowana rosnąco

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

Wszystkie powtarzające się wartości muszą zostać zachowane

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

Liczby ujemne muszą zostać posortowane przed dodatnimi

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

Dłuższa mieszana tablica musi zostać posortowana rosnąco

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

Przekazana lista nie może zostać zmodyfikowana

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
