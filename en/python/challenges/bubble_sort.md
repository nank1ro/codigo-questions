---
language: python
exerciseType: 1
difficulty: 2
title: Bubble sort
---

# --description--

Bubble sort is one of the simplest sorting algorithms. It walks through a list and compares each pair of adjacent items, swapping them whenever they are in the wrong order. After each full pass the largest remaining value has "bubbled" up to its final position, and the list is sorted as soon as a pass finishes without a single swap.

# --instructions--

Write a function called `bubble_sort` that takes a list of integers and returns a **new** list with the same values sorted into ascending order. The list that is passed in must not be modified.

You must implement the bubble sort algorithm yourself, comparing and swapping adjacent items. Do not use a sorting function from the standard library.

Your function must also work with an empty array, an array with a single element, an array that is already sorted, repeated values and negative numbers.

Example of function call:
```python
print(bubble_sort([3, 1, 2]))
# prints [1, 2, 3]
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

An empty array must return an empty array

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

An array with a single element must stay the same

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

An already sorted array must stay in the same order

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

A reverse sorted array must be turned into ascending order

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

Repeated values must all be kept

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

Negative numbers must be sorted before the positive ones

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

A longer mixed array must be sorted in ascending order

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

The array that is passed in must not be modified

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
