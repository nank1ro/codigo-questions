---
language: python
exerciseType: 1
difficulty: 2
title: 冒泡排序
---

# --description--

冒泡排序是最简单的排序算法之一。它遍历一个列表，比较每一对相邻的元素，只要它们的顺序不对就交换它们。每完成一轮完整的遍历，剩下的最大值就会“冒泡”到它的最终位置；一旦某一轮遍历没有发生任何交换，列表就已经排好序了。

# --instructions--

编写一个名为 `bubble_sort` 的函数，它接收一个整数列表，并返回一个包含相同值且按升序排序的**新**列表。传入的列表不能被修改。

你必须自己实现冒泡排序算法，比较并交换相邻的元素。不要使用标准库中的排序函数。

你的函数还必须能处理空数组、只有一个元素的数组、已经排好序的数组、重复的值和负数。

函数调用示例：
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

空数组必须返回空数组

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

只有一个元素的数组必须保持不变

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

已经排好序的数组必须保持相同的顺序

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

逆序排列的数组必须变成升序

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

所有重复的值都必须保留

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

负数必须排在正数之前

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

更长的混合数组必须按升序排序

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

传入的数组不能被修改

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
