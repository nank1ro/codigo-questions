---
language: python
exerciseType: 1
difficulty: 2
title: Sortowanie bąbelkowe
---

# --description--

Sortowanie bąbelkowe to jeden z najprostszych algorytmów sortowania. Przechodzi przez listę i porównuje każdą parę sąsiednich elementów, zamieniając je miejscami zawsze, gdy są w złej kolejności. Po każdym pełnym przejściu największa z pozostałych wartości „wypływa” na swoje ostateczne miejsce, a lista jest posortowana, gdy tylko przejście zakończy się bez ani jednej zamiany.

# --instructions--

Napisz funkcję o nazwie `bubble_sort`, która przyjmuje listę liczb całkowitych i zwraca **nową** listę z tymi samymi wartościami posortowanymi w kolejności rosnącej. Przekazana lista nie może zostać zmodyfikowana.

Musisz samodzielnie zaimplementować algorytm sortowania bąbelkowego, porównując i zamieniając sąsiednie elementy. Nie używaj funkcji sortującej z biblioteki standardowej.

Twoja funkcja musi działać również dla pustej tablicy, tablicy z jednym elementem, tablicy już posortowanej, powtarzających się wartości i liczb ujemnych.

Przykład wywołania funkcji:
```python
print(bubble_sort([3, 1, 2]))
# wypisuje [1, 2, 3]
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

Pusta tablica musi zwrócić pustą tablicę

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

Tablica z jednym elementem musi pozostać taka sama

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

Już posortowana tablica musi zachować tę samą kolejność

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

Tablica posortowana odwrotnie musi zostać uporządkowana rosnąco

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

Wszystkie powtarzające się wartości muszą zostać zachowane

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

Liczby ujemne muszą zostać posortowane przed dodatnimi

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

Dłuższa mieszana tablica musi zostać posortowana rosnąco

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

Przekazana tablica nie może zostać zmodyfikowana

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
