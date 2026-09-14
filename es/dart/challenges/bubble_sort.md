---
language: dart
exerciseType: 1
difficulty: 2
title: Ordenamiento burbuja
---

# --description--

El ordenamiento burbuja es uno de los algoritmos de ordenación más simples. Recorre una lista y compara cada par de elementos adyacentes, intercambiándolos siempre que están en el orden incorrecto. Después de cada pasada completa, el valor más grande que queda ha "burbujeado" hasta su posición final, y la lista está ordenada en cuanto una pasada termina sin un solo intercambio.

# --instructions--

Escribe una función llamada `bubbleSort` que reciba una `List<int>` y devuelva una **nueva** lista con los mismos valores ordenados en orden ascendente. La lista que se pasa no debe ser modificada.

Debes implementar el algoritmo de ordenamiento burbuja tú mismo, comparando e intercambiando elementos adyacentes. No uses una función de ordenación de la biblioteca estándar.

Tu función también debe funcionar con un array vacío, un array con un solo elemento, un array que ya está ordenado, valores repetidos y números negativos.

Ejemplo de llamada de función:
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

Un array vacío debe devolver un array vacío

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

Un array con un solo elemento debe quedar igual

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

Un array ya ordenado debe mantener el mismo orden

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

Un array ordenado a la inversa debe convertirse en orden ascendente

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

Todos los valores repetidos deben conservarse

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

Los números negativos deben ordenarse antes que los positivos

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

Un array mixto más largo debe ordenarse en orden ascendente

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

La lista que se pasa no debe ser modificada

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
