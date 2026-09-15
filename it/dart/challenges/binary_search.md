---
language: dart
exerciseType: 1
difficulty: 2
title: Ricerca binaria
---

# --description--

La ricerca binaria trova un valore all'interno di una collezione **ordinata** dimezzando ripetutamente l'intervallo di ricerca: guarda l'elemento centrale e, se non è quello che cerchi, continua nella metà sinistra quando il valore cercato è più piccolo o nella metà destra quando è più grande.

Poiché ogni passo scarta metà degli elementi rimanenti, la ricerca binaria arriva alla risposta in poche comparazioni anche su collezioni molto grandi, mentre controllare gli elementi uno per uno costerebbe tanti passi quanti sono gli elementi.

# --instructions--

Scrivi una funzione `binarySearch` che riceve una lista di numeri interi ordinata in modo crescente e un numero intero cercato, e restituisce l'indice del valore cercato all'interno della lista, oppure `-1` quando il valore non è presente.

La lista non contiene mai duplicati, quindi l'indice è sempre unico. La lista può anche essere vuota. La tua funzione deve usare la ricerca binaria, dimezzando l'intervallo di ricerca a ogni passo, non una scansione lineare.

Esempio di chiamata di funzione:
```dart
print(binarySearch([1, 3, 5, 7], 5));
// stampa 2
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

La ricerca in una lista vuota deve restituire -1

```dart
  test('test1', () {
    expect(binarySearch([], 7), -1, reason: '--err-t1--');
  });
```

La ricerca di 5 in `[5]` deve restituire 0

```dart
  test('test2', () {
    expect(binarySearch([5], 5), 0, reason: '--err-t2--');
  });
```

La ricerca di 9 in `[5]` deve restituire -1

```dart
  test('test3', () {
    expect(binarySearch([5], 9), -1, reason: '--err-t3--');
  });
```

Il primo elemento -9 della lista di 12 elementi deve essere trovato all'indice 0

```dart
  test('test4', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, reason: '--err-t4--');
  });
```

L'ultimo elemento 78 della lista di 12 elementi deve essere trovato all'indice 11

```dart
  test('test5', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, reason: '--err-t5--');
  });
```

L'elemento 15 deve essere trovato all'indice 6

```dart
  test('test6', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, reason: '--err-t6--');
  });
```

L'elemento 22 deve essere trovato all'indice 7

```dart
  test('test7', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, reason: '--err-t7--');
  });
```

Il valore 12, che si trova tra 11 e 15, deve restituire -1

```dart
  test('test8', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, reason: '--err-t8--');
  });
```

Un valore cercato più piccolo di ogni elemento deve restituire -1

```dart
  test('test9', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, reason: '--err-t9--');
  });
```

Un valore cercato più grande di ogni elemento deve restituire -1

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
