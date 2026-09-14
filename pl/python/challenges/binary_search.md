---
language: python
exerciseType: 1
difficulty: 2
title: Wyszukiwanie binarne
---

# --description--

Wyszukiwanie binarne znajduje wartość w **posortowanej** kolekcji poprzez wielokrotne dzielenie zakresu wyszukiwania na połowy: spójrz na element znajdujący się w środku, a jeśli nie jest to ten, którego szukasz, kontynuuj w lewej połowie, gdy szukana wartość jest mniejsza, lub w prawej połowie, gdy jest większa.

Ponieważ każdy krok odrzuca połowę pozostałych elementów, wyszukiwanie binarne dociera do odpowiedzi w kilku porównaniach, nawet dla bardzo dużych kolekcji, podczas gdy sprawdzanie elementów pojedynczo kosztowałoby tyle kroków, ile jest elementów.

# --instructions--

Napisz funkcję `binary_search`, która przyjmuje listę liczb całkowitych posortowaną rosnąco oraz liczbę całkowitą będącą szukaną wartością, i zwraca indeks tej wartości na liście lub `-1`, gdy nie ma jej na liście.

Lista nigdy nie zawiera duplikatów, więc indeks jest zawsze unikalny. Lista może być również pusta. Twoja funkcja musi korzystać z wyszukiwania binarnego, dzieląc zakres wyszukiwania na połowy w każdym kroku, a nie z liniowego przeglądania elementów.

Przykład wywołania funkcji:
```python
print(binary_search([1, 3, 5, 7], 5))
# prints 2
```

# --seed--

```python
def binary_search(arr, target):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Wyszukiwanie w pustej liście musi zwrócić -1

```python
    def test1(self):
        self.assertEqual(binary_search([], 7), -1, "--err-t1--")
```

Wyszukiwanie 5 w `[5]` musi zwrócić 0

```python
    def test2(self):
        self.assertEqual(binary_search([5], 5), 0, "--err-t2--")
```

Wyszukiwanie 9 w `[5]` musi zwrócić -1

```python
    def test3(self):
        self.assertEqual(binary_search([5], 9), -1, "--err-t3--")
```

Pierwszy element -9 12-elementowej listy musi zostać znaleziony pod indeksem 0

```python
    def test4(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, "--err-t4--")
```

Ostatni element 78 12-elementowej listy musi zostać znaleziony pod indeksem 11

```python
    def test5(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, "--err-t5--")
```

Element 15 musi zostać znaleziony pod indeksem 6

```python
    def test6(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, "--err-t6--")
```

Element 22 musi zostać znaleziony pod indeksem 7

```python
    def test7(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, "--err-t7--")
```

Wartość 12, która leży między 11 a 15, musi zwrócić -1

```python
    def test8(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, "--err-t8--")
```

Szukana wartość mniejsza niż każdy element musi zwrócić -1

```python
    def test9(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, "--err-t9--")
```

Szukana wartość większa niż każdy element musi zwrócić -1

```python
    def test10(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100), -1, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
