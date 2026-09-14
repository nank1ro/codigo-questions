---
language: dart
exerciseType: 1
difficulty: 2
title: Binäre Suche
---

# --description--

Die binäre Suche findet einen Wert in einer **sortierten** Sammlung, indem sie den Suchbereich wiederholt halbiert: Sieh dir das Element in der Mitte an, und wenn es nicht das gesuchte ist, mach in der linken Hälfte weiter, wenn der gesuchte Wert kleiner ist, oder in der rechten Hälfte, wenn er größer ist.

Da jeder Schritt die Hälfte der verbleibenden Elemente verwirft, erreicht die binäre Suche die Antwort selbst bei sehr großen Sammlungen mit einer Handvoll Vergleichen, während das Prüfen der Elemente eines nach dem anderen so viele Schritte kosten würde, wie es Elemente gibt.

# --instructions--

Schreibe eine Funktion `binarySearch`, die eine aufsteigend sortierte Liste von ganzen Zahlen und eine gesuchte ganze Zahl entgegennimmt und den Index der gesuchten Zahl in der Liste zurückgibt oder `-1`, wenn die Zahl nicht vorhanden ist.

Die Liste enthält niemals Duplikate, der Index ist also immer eindeutig. Die Liste kann auch leer sein. Deine Funktion muss die binäre Suche verwenden und den Suchbereich bei jedem Schritt halbieren, statt linear zu suchen.

Beispiel für einen Funktionsaufruf:
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

Die Suche in einer leeren Liste muss -1 zurückgeben

```dart
  test('test1', () {
    expect(binarySearch([], 7), -1, reason: '--err-t1--');
  });
```

Die Suche nach 5 in `[5]` muss 0 zurückgeben

```dart
  test('test2', () {
    expect(binarySearch([5], 5), 0, reason: '--err-t2--');
  });
```

Die Suche nach 9 in `[5]` muss -1 zurückgeben

```dart
  test('test3', () {
    expect(binarySearch([5], 9), -1, reason: '--err-t3--');
  });
```

Das erste Element -9 der 12-elementigen Liste muss am Index 0 gefunden werden

```dart
  test('test4', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, reason: '--err-t4--');
  });
```

Das letzte Element 78 der 12-elementigen Liste muss am Index 11 gefunden werden

```dart
  test('test5', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, reason: '--err-t5--');
  });
```

Das Element 15 muss am Index 6 gefunden werden

```dart
  test('test6', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, reason: '--err-t6--');
  });
```

Das Element 22 muss am Index 7 gefunden werden

```dart
  test('test7', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, reason: '--err-t7--');
  });
```

Der Wert 12, der zwischen 11 und 15 liegt, muss -1 zurückgeben

```dart
  test('test8', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, reason: '--err-t8--');
  });
```

Ein gesuchter Wert, der kleiner als jedes Element ist, muss -1 zurückgeben

```dart
  test('test9', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, reason: '--err-t9--');
  });
```

Ein gesuchter Wert, der größer als jedes Element ist, muss -1 zurückgeben

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
