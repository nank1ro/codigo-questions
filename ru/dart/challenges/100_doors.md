---
language: dart
exerciseType: 1
difficulty: 1
title: 100 дверей
---

# --description--

В ряду стоят 100 дверей, все изначально закрыты.
Вы совершаете 100 проходов мимо дверей.
В первый раз посещаете каждую дверь и переключаете её (если дверь закрыта, откройте её; если открыта, закройте).
Во второй раз посещаете только каждую 2-ю дверь (т.е. дверь №2, №4, №6, ...) и переключаете её.
В третий раз посещаете каждую 3-ю дверь (т.е. дверь №3, №6, №9, ...) и так далее, пока не посетите только 100-ю дверь.

# --instructions--

Реализуйте функцию для определения состояния дверей после последнего прохода.
Верните конечный результат в массиве, включив в массив только номер двери, если она открыта.
> Метод должен работать с переменным количеством дверей.

# --seed--

```dart
import 'dart:math';

List<int> getFinalOpenedDoors(numDoors: Int) {
    
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

Для 100 дверей вернуть правильный список открытых дверей

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

Для 10 дверей вернуть правильный список открытых дверей

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

Для 950 дверей вернуть правильный список открытых дверей

```dart
    test("test3", () {
      const solution3 = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900];
      expect(getFinalOpenedDoors(950), solution3, reason: "--err-t3--");
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
import 'dart:math';

int square(int number) => pow(number.toDouble(), 2.0).toInt();

List<int> getFinalOpenedDoors(int numDoors) {
    final openDoors = <int>[];
    var i = 1;
    while (square(i) <= numDoors) {
        openDoors.add(square(i));
        i += 1;
    }
    return openDoors;
}
```
