---
language: python
exerciseType: 1
title: 100扇门
difficulty: 1
---

# --description--

一排有100扇门，初始状态全部关闭。
你经过这些门100次。
第一次经过时，访问每扇门并"切换"门的状态（如果门是关闭的，就打开它；如果是打开的，就关闭它）。
第二次，只访问每第2扇门（即第2、4、6...扇门）并切换状态。
第三次，访问每第3扇门（即第3、6、9...扇门），以此类推，直到你只访问第100扇门。

# --instructions--

实现一个函数来确定最后一次经过后门的状态。
将最终结果以数组形式返回，只有打开的门的编号才包含在数组中。
> 该方法必须能够处理可变数量的门。

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

给定100扇门，返回正确的打开门列表

```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_final_opened_doors(100), solution, "--err-t1--")
```

给定10扇门，返回正确的打开门列表

```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(get_final_opened_doors(10), solution, "--err-t2--")
```

给定950扇门，返回正确的打开门列表

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
