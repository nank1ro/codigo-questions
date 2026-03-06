---
language: python
exerciseType: 1
title: 100のドア
difficulty: 1
---

# --description--

一列に並んだ100枚のドアがあり、最初はすべて閉まっています。
100回ドアの前を通ります。
1回目は、すべてのドアを訪れてドアを「切り替え」ます（ドアが閉まっていれば開け、開いていれば閉めます）。
2回目は、2番目ごとのドアだけを訪れ（つまり、ドア#2、#4、#6、...）、切り替えます。
3回目は、3番目ごとのドアを訪れ（つまり、ドア#3、#6、#9、...）、以降同様に100番目のドアだけを訪れるまで続けます。

# --instructions--

最後の通過後のドアの状態を判定する関数を実装してください。
開いているドアの番号のみを含む配列で最終結果を返してください。
> このメソッドは、可変数のドアに対応できなければなりません。

# --seed--

```python
def get_final_opened_doors(num_doors):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

100枚のドアが与えられた場合、開いているドアの正しいリストを返す

```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_final_opened_doors(100), solution, "--err-t1--")
```

10枚のドアが与えられた場合、開いているドアの正しいリストを返す

```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(get_final_opened_doors(10), solution, "--err-t2--")
```

950枚のドアが与えられた場合、開いているドアの正しいリストを返す

```python
    def test_3(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        self.assertEqual(get_final_opened_doors(950), solution, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def get_final_opened_doors(num_doors):
    open_doors = []
    i = 1;
    while (i**2) <= num_doors:
        open_doors.append(i**2)
        i += 1
    return open_doors
```
