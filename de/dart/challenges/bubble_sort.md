---
language: dart
exerciseType: 1
difficulty: 2
title: Bubblesort
---

# --description--

Bubblesort ist einer der einfachsten Sortieralgorithmen. Er durchläuft eine Liste und vergleicht jedes Paar benachbarter Elemente, wobei er sie vertauscht, sobald sie in der falschen Reihenfolge stehen. Nach jedem vollständigen Durchlauf ist der größte verbleibende Wert an seine endgültige Position „aufgestiegen“, und die Liste ist sortiert, sobald ein Durchlauf ohne einen einzigen Tausch endet.

# --instructions--

Schreiben Sie eine Funktion namens `bubbleSort`, die eine `List<int>` entgegennimmt und eine **neue** Liste mit denselben Werten in aufsteigender Reihenfolge zurückgibt. Die übergebene Liste darf nicht verändert werden.

Sie müssen den Bubblesort-Algorithmus selbst implementieren, indem Sie benachbarte Elemente vergleichen und vertauschen. Verwenden Sie keine Sortierfunktion aus der Standardbibliothek.

Ihre Funktion muss auch mit einem leeren Array, einem Array mit einem einzigen Element, einem bereits sortierten Array, wiederholten Werten und negativen Zahlen funktionieren.

Beispiel eines Funktionsaufrufs:
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

Ein leeres Array muss ein leeres Array zurückgeben

```dart
    test("test1", () {
      expect(bubbleSort([]), [], reason: "--err-t1--");
    });
```

Ein Array mit einem einzigen Element muss gleich bleiben

```dart
    test("test2", () {
      expect(bubbleSort([42]), [42], reason: "--err-t2--");
    });
```

Ein bereits sortiertes Array muss in derselben Reihenfolge bleiben

```dart
    test("test3", () {
      expect(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], reason: "--err-t3--");
    });
```

Ein absteigend sortiertes Array muss in aufsteigende Reihenfolge gebracht werden

```dart
    test("test4", () {
      expect(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], reason: "--err-t4--");
    });
```

Wiederholte Werte müssen alle erhalten bleiben

```dart
    test("test5", () {
      expect(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], reason: "--err-t5--");
    });
```

Negative Zahlen müssen vor den positiven sortiert werden

```dart
    test("test6", () {
      expect(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], reason: "--err-t6--");
    });
```

Ein längeres gemischtes Array muss in aufsteigender Reihenfolge sortiert werden

```dart
    test("test7", () {
      expect(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], reason: "--err-t7--");
    });
```

Die übergebene Liste darf nicht verändert werden

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
