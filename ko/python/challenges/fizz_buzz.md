---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

숫자를 인수로 받아 `"Fizz"`, `"Buzz"` 또는 `"FizzBuzz"`를 반환하는 함수를 만드세요.

# --instructions--

- 숫자가 `3`의 배수이면 출력은 `"Fizz"`여야 합니다
- 주어진 숫자가 `5`의 배수이면 출력은 `"Buzz"`여야 합니다.
- 주어진 숫자가 `3`과 `5` 모두의 배수이면 출력은 `"FizzBuzz"`여야 합니다.
- 숫자가 `3`이나 `5`의 배수가 아니면 아래 예시처럼 숫자 자체를 출력해야 합니다.
- 출력은 `3`이나 `5`의 배수가 아니더라도 항상 문자열이어야 합니다.

예시:
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

숫자 `3`은 `"Fizz"`와 같아야 합니다

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

숫자 `5`는 `"Buzz"`와 같아야 합니다

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

숫자 `15`는 `"FizzBuzz"`와 같아야 합니다

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

숫자 `10`은 `"Buzz"`와 같아야 합니다

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

숫자 `98`은 `"98"`과 같아야 합니다

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
