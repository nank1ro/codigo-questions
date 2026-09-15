---
language: dart
exerciseType: 1
difficulty: 2
title: Сортировка пузырьком
---

# --description--

Сортировка пузырьком — один из самых простых алгоритмов сортировки. Он проходит по списку и сравнивает каждую пару соседних элементов, меняя их местами всякий раз, когда они стоят в неправильном порядке. После каждого полного прохода наибольшее из оставшихся значений «всплывает» на своё окончательное место, а список считается отсортированным, как только проход завершается без единого обмена.

# --instructions--

Напишите функцию с именем `bubbleSort`, которая принимает `List<int>` и возвращает **новый** список с теми же значениями, отсортированными по возрастанию. Переданный список изменять нельзя.

Вы должны сами реализовать алгоритм сортировки пузырьком, сравнивая и меняя местами соседние элементы. Не используйте функцию сортировки из стандартной библиотеки.

Ваша функция также должна работать с пустым массивом, массивом из одного элемента, уже отсортированным массивом, повторяющимися значениями и отрицательными числами.

Пример вызова функции:
```dart
print(bubbleSort([3, 1, 2]));
// выводит [1, 2, 3]
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

Пустой массив должен вернуть пустой массив

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

Массив из одного элемента должен остаться прежним

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

Уже отсортированный массив должен сохранить тот же порядок

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

Массив, отсортированный в обратном порядке, должен быть упорядочен по возрастанию

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

Все повторяющиеся значения должны сохраниться

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

Отрицательные числа должны быть отсортированы перед положительными

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

Более длинный смешанный массив должен быть отсортирован по возрастанию

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

Переданный список изменять нельзя

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
