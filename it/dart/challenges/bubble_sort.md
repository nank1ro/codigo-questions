---
language: dart
exerciseType: 1
difficulty: 2
title: Ordinamento a bolle
---

# --description--

L'ordinamento a bolle è uno degli algoritmi di ordinamento più semplici. Percorre una lista e confronta ogni coppia di elementi adiacenti, scambiandoli ogni volta che sono nell'ordine sbagliato. Dopo ogni passata completa il valore più grande rimasto è "salito a galla" fino alla sua posizione finale, e la lista è ordinata non appena una passata si conclude senza un solo scambio.

# --instructions--

Scrivi una funzione chiamata `bubbleSort` che prenda una `List<int>` e restituisca una **nuova** lista con gli stessi valori ordinati in ordine crescente. La lista passata non deve essere modificata.

Devi implementare tu stesso l'algoritmo di ordinamento a bolle, confrontando e scambiando elementi adiacenti. Non usare una funzione di ordinamento della libreria standard.

La tua funzione deve funzionare anche con un array vuoto, un array con un solo elemento, un array già ordinato, valori ripetuti e numeri negativi.

Esempio di chiamata di funzione:
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

Un array vuoto deve restituire un array vuoto

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

Un array con un solo elemento deve rimanere uguale

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

Un array già ordinato deve mantenere lo stesso ordine

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

Un array ordinato al contrario deve essere messo in ordine crescente

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

Tutti i valori ripetuti devono essere mantenuti

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

I numeri negativi devono essere ordinati prima di quelli positivi

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

Un array misto più lungo deve essere ordinato in ordine crescente

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

La lista passata non deve essere modificata

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
