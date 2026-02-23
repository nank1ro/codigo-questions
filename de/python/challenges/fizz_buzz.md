---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

Erstellen Sie eine Funktion, die eine Zahl als Argument entgegennimmt und `"Fizz"`, `"Buzz"` oder `"FizzBuzz"` zurückgibt.

# --instructions--

- Wenn die Zahl ein Vielfaches von `3` ist, sollte die Ausgabe `"Fizz"` sein
- Wenn die angegebene Zahl ein Vielfaches von `5` ist, sollte die Ausgabe `"Buzz"` sein.
- Wenn die angegebene Zahl ein Vielfaches von sowohl `3` als auch `5` ist, sollte die Ausgabe `"FizzBuzz"` sein.
- Wenn die Zahl kein Vielfaches von entweder `3` oder `5` ist, sollte die Zahl allein ausgegeben werden, wie in den Beispielen unten gezeigt.
- Die Ausgabe sollte immer ein String sein, auch wenn sie kein Vielfaches von `3` oder `5` ist.

Beispiele:
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

Die Zahl `3` muss gleich `"Fizz"` sein

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

Die Zahl `5` muss gleich `"Buzz"` sein

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

Die Zahl `15` muss gleich `"FizzBuzz"` sein

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

Die Zahl `10` muss gleich `"Buzz"` sein

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

Die Zahl `98` muss gleich `"98"` sein

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
