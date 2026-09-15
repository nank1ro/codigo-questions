---
language: dart
exerciseType: 1
difficulty: 2
title: Wyszukiwanie binarne
---

# --description--

Wyszukiwanie binarne znajduje wartość w **posortowanej** kolekcji poprzez wielokrotne dzielenie zakresu wyszukiwania na połowy: spójrz na element znajdujący się w środku, a jeśli nie jest to ten, którego szukasz, kontynuuj w lewej połowie, gdy szukana wartość jest mniejsza, lub w prawej połowie, gdy jest większa.

Ponieważ każdy krok odrzuca połowę pozostałych elementów, wyszukiwanie binarne dociera do odpowiedzi w kilku porównaniach, nawet dla bardzo dużych kolekcji, podczas gdy sprawdzanie elementów pojedynczo kosztowałoby tyle kroków, ile jest elementów.

# --instructions--

Napisz funkcję `binarySearch`, która przyjmuje listę liczb całkowitych posortowaną rosnąco oraz liczbę całkowitą będącą szukaną wartością, i zwraca indeks tej wartości na liście lub `-1`, gdy nie ma jej na liście.

Lista nigdy nie zawiera duplikatów, więc indeks jest zawsze unikalny. Lista może być również pusta. Twoja funkcja musi korzystać z wyszukiwania binarnego, dzieląc zakres wyszukiwania na połowy w każdym kroku, a nie z liniowego przeglądania elementów.

Przykład wywołania funkcji:
```dart
print(binarySearch([1, 3, 5, 7], 5));
// wypisuje 2
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

Wyszukiwanie w pustej liście musi zwrócić -1

```dart
  test('test1', () {
    expect(binarySearch([], 7), -1, reason: '--err-t1--');
  });
```

Wyszukiwanie 5 w `[5]` musi zwrócić 0

```dart
  test('test2', () {
    expect(binarySearch([5], 5), 0, reason: '--err-t2--');
  });
```

Wyszukiwanie 9 w `[5]` musi zwrócić -1

```dart
  test('test3', () {
    expect(binarySearch([5], 9), -1, reason: '--err-t3--');
  });
```

Pierwszy element -9 12-elementowej listy musi zostać znaleziony pod indeksem 0

```dart
  test('test4', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, reason: '--err-t4--');
  });
```

Ostatni element 78 12-elementowej listy musi zostać znaleziony pod indeksem 11

```dart
  test('test5', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, reason: '--err-t5--');
  });
```

Element 15 musi zostać znaleziony pod indeksem 6

```dart
  test('test6', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, reason: '--err-t6--');
  });
```

Element 22 musi zostać znaleziony pod indeksem 7

```dart
  test('test7', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, reason: '--err-t7--');
  });
```

Wartość 12, która leży między 11 a 15, musi zwrócić -1

```dart
  test('test8', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, reason: '--err-t8--');
  });
```

Szukana wartość mniejsza niż każdy element musi zwrócić -1

```dart
  test('test9', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, reason: '--err-t9--');
  });
```

Szukana wartość większa niż każdy element musi zwrócić -1

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
