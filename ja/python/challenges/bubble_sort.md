---
language: python
exerciseType: 1
difficulty: 2
title: バブルソート
---

# --description--

バブルソートは最も単純なソートアルゴリズムの一つです。リストを順に見ていき、隣り合う要素のペアを比較し、順序が間違っているたびにそれらを交換します。完全な走査が終わるたびに残りの中で最大の値が最終的な位置まで「浮かび上がり」、一度も交換が起きずに走査が終わった時点でリストはソートされています。

# --instructions--

整数のリストを受け取り、同じ値を昇順にソートした**新しい**リストを返す`bubble_sort`という関数を書いてください。渡されたリストを変更してはいけません。

バブルソートのアルゴリズムは自分で実装し、隣り合う要素を比較して交換してください。標準ライブラリのソート関数は使わないでください。

関数は空の配列、要素が1つだけの配列、すでにソート済みの配列、重複した値、負の数でも動作しなければなりません。

関数呼び出しの例:
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

空の配列は空の配列を返さなければなりません

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

要素が1つだけの配列はそのままでなければなりません

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

すでにソート済みの配列は同じ順序のままでなければなりません

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

逆順にソートされた配列は昇順に並べ替えられなければなりません

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

重複した値はすべて保持されなければなりません

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

負の数は正の数より前にソートされなければなりません

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

より長い混在した配列は昇順にソートされなければなりません

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

渡された配列を変更してはいけません

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
