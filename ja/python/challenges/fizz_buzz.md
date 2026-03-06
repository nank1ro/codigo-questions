---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

数値を引数として受け取り、`"Fizz"`、`"Buzz"`、または`"FizzBuzz"`を返す関数を作成してください。

# --instructions--

- 数が`3`の倍数の場合、出力は`"Fizz"`にしてください
- 数が`5`の倍数の場合、出力は`"Buzz"`にしてください
- 数が`3`と`5`の両方の倍数の場合、出力は`"FizzBuzz"`にしてください
- 数が`3`でも`5`の倍数でもない場合、以下の例のように数値そのものを出力してください
- 出力は`3`または`5`の倍数でなくても、常に文字列でなければなりません

例：
```python
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
```

# --seed--

```python
def fizz_buzz():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

数`3`は`"Fizz"`に等しくなければなりません

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

数`5`は`"Buzz"`に等しくなければなりません

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

数`15`は`"FizzBuzz"`に等しくなければなりません

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

数`10`は`"Buzz"`に等しくなければなりません

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

数`98`は`"98"`に等しくなければなりません

```python
    def test5(self):
        self.assertEqual(fizz_buzz(98), "98", "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)
```
