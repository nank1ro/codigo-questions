---
language: python
exerciseType: 1
difficulty: 2
title: Bubblesort
---

# --description--

Bubblesort ist einer der einfachsten Sortieralgorithmen. Er durchläuft eine Liste und vergleicht jedes Paar benachbarter Elemente, wobei er sie vertauscht, sobald sie in der falschen Reihenfolge stehen. Nach jedem vollständigen Durchlauf ist der größte verbleibende Wert an seine endgültige Position „aufgestiegen“, und die Liste ist sortiert, sobald ein Durchlauf ohne einen einzigen Tausch endet.

# --instructions--

Schreiben Sie eine Funktion namens `bubble_sort`, die eine Liste von ganzen Zahlen entgegennimmt und eine **neue** Liste mit denselben Werten in aufsteigender Reihenfolge zurückgibt. Die übergebene Liste darf nicht verändert werden.

Sie müssen den Bubblesort-Algorithmus selbst implementieren, indem Sie benachbarte Elemente vergleichen und vertauschen. Verwenden Sie keine Sortierfunktion aus der Standardbibliothek.

Ihre Funktion muss auch mit einem leeren Array, einem Array mit einem einzigen Element, einem bereits sortierten Array, wiederholten Werten und negativen Zahlen funktionieren.

Beispiel eines Funktionsaufrufs:
```python
print(bubble_sort([3, 1, 2]))
# gibt [1, 2, 3] aus
```

# --seed--

```python
def bubble_sort(arr):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Ein leeres Array muss ein leeres Array zurückgeben

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

Ein Array mit einem einzigen Element muss gleich bleiben

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

Ein bereits sortiertes Array muss in derselben Reihenfolge bleiben

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

Ein absteigend sortiertes Array muss in aufsteigende Reihenfolge gebracht werden

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

Wiederholte Werte müssen alle erhalten bleiben

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

Negative Zahlen müssen vor den positiven sortiert werden

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

Ein längeres gemischtes Array muss in aufsteigender Reihenfolge sortiert werden

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

Das übergebene Array darf nicht verändert werden

```python
    def test_8(self):
        original = [3, 1, 2]
        bubble_sort(original)
        self.assertEqual(original, [3, 1, 2], "--err-t8--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def bubble_sort(arr):
    result = list(arr)
    end = len(result)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, end):
            if result[i - 1] > result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]
                swapped = True
        end -= 1
    return result
```
