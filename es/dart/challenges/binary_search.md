---
language: dart
exerciseType: 1
difficulty: 2
title: Búsqueda binaria
---

# --description--

La búsqueda binaria encuentra un valor dentro de una colección **ordenada** dividiendo repetidamente por la mitad el rango de búsqueda: mira el elemento del medio y, si no es el que buscas, continúa en la mitad izquierda cuando el valor buscado es menor o en la mitad derecha cuando es mayor.

Como cada paso descarta la mitad de los elementos restantes, la búsqueda binaria llega a la respuesta en unas pocas comparaciones incluso en colecciones muy grandes, mientras que comprobar los elementos uno por uno costaría tantos pasos como elementos haya.

# --instructions--

Escribe una función `binarySearch` que recibe una lista de números enteros ordenada de forma ascendente y un número entero buscado, y devuelve el índice del valor buscado dentro de la lista, o `-1` cuando el valor no está presente.

La lista nunca contiene duplicados, por lo que el índice siempre es único. La lista también puede estar vacía. Tu función debe usar búsqueda binaria, dividiendo el rango de búsqueda por la mitad en cada paso, no un recorrido lineal.

Ejemplo de llamada de función:
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

Buscar en una lista vacía debe devolver -1

```dart
  test('test1', () {
    expect(binarySearch([], 7), -1, reason: '--err-t1--');
  });
```

Buscar 5 en `[5]` debe devolver 0

```dart
  test('test2', () {
    expect(binarySearch([5], 5), 0, reason: '--err-t2--');
  });
```

Buscar 9 en `[5]` debe devolver -1

```dart
  test('test3', () {
    expect(binarySearch([5], 9), -1, reason: '--err-t3--');
  });
```

El primer elemento -9 de la lista de 12 elementos debe encontrarse en el índice 0

```dart
  test('test4', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, reason: '--err-t4--');
  });
```

El último elemento 78 de la lista de 12 elementos debe encontrarse en el índice 11

```dart
  test('test5', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, reason: '--err-t5--');
  });
```

El elemento 15 debe encontrarse en el índice 6

```dart
  test('test6', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, reason: '--err-t6--');
  });
```

El elemento 22 debe encontrarse en el índice 7

```dart
  test('test7', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, reason: '--err-t7--');
  });
```

El valor 12, que está entre 11 y 15, debe devolver -1

```dart
  test('test8', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, reason: '--err-t8--');
  });
```

Un valor buscado menor que todos los elementos debe devolver -1

```dart
  test('test9', () {
    expect(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, reason: '--err-t9--');
  });
```

Un valor buscado mayor que todos los elementos debe devolver -1

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
