---
language: python
exerciseType: 1
difficulty: 2
title: Binary search
---

# --description--

Binary search finds a value inside a **sorted** collection by repeatedly halving the search range: look at the element in the middle, and if it is not the one you want, continue in the left half when the target is smaller or in the right half when the target is larger.

Because every step throws away half of the remaining elements, binary search reaches the answer in a handful of comparisons even on very large collections, while checking the elements one by one would cost as many steps as there are elements.

# --instructions--

Write a function `binary_search` that takes a list of integers sorted in ascending order and a target integer, and returns the index of the target inside the list, or `-1` when the target is not present.

The list never contains duplicates, so the index is always unique. The list can also be empty. Your function must use binary search, halving the search range at every step, not a linear scan.

Example of function call:
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

Searching in an empty list must return -1

```python
    def test1(self):
        self.assertEqual(binary_search([], 7), -1, "--err-t1--")
```

Searching for 5 in `[5]` must return 0

```python
    def test2(self):
        self.assertEqual(binary_search([5], 5), 0, "--err-t2--")
```

Searching for 9 in `[5]` must return -1

```python
    def test3(self):
        self.assertEqual(binary_search([5], 9), -1, "--err-t3--")
```

The first element -9 of the 12 element list must be found at index 0

```python
    def test4(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, "--err-t4--")
```

The last element 78 of the 12 element list must be found at index 11

```python
    def test5(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, "--err-t5--")
```

The element 15 must be found at index 6

```python
    def test6(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, "--err-t6--")
```

The element 22 must be found at index 7

```python
    def test7(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, "--err-t7--")
```

The value 12, which sits between 11 and 15, must return -1

```python
    def test8(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, "--err-t8--")
```

A target smaller than every element must return -1

```python
    def test9(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, "--err-t9--")
```

A target larger than every element must return -1

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
