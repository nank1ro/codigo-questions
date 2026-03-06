---
language: python
exerciseType: 1
difficulty: 3
title: 윤년
---

# --description--

달력의 한 해에는 정확히 365.25일이 있습니다. 하지만 결국 이것은 혼란을 야기하게 됩니다. 왜냐하면 인간은 보통 소수점이 아닌 1의 정확한 나눗셈으로 세기 때문입니다. 그래서 이를 피하기 위해, 4년 주기마다 0.25일을 모두 더하여 그 해에 366일을 부여하고 (2월 29일을 윤일로 포함) 이를 __윤년__이라고 부르기로 했습니다. 4년 주기의 나머지 세 해는 365일만 포함하며 __윤년이 아닙니다__.

# --instructions--

이 챌린지에서는 한 단계 더 나아가, `datetime` 클래스, __if 블록__, __if-elif 블록__, __조건식__ (`a if b else c`) 또는 논리 연산자 __AND__ (`and`)와 __OR__ (`or`)를 사용하지 않고 윤년인지 판별해야 합니다. __NOT__ (`not`) 연산자는 예외적으로 사용할 수 있습니다.

윤년이면 `True`를, 그렇지 않으면 `False`를 반환하세요.

함수 호출 예시:
```dart
print(leap_year(2000))
// prints true
```

# --seed--

```python
def leap_year(year):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`month`, `day`, `if`, `else`, `elif`, `and`, `or`의 사용은 허용되지 않습니다.

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

`2016`년은 윤년입니다.

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

`1996`년은 윤년입니다.

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

`1600`년은 윤년입니다.

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

`2020`년은 윤년입니다.

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

`2000`년은 윤년입니다.

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

`2008`년은 윤년입니다.

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

`1521`년은 윤년이 아닙니다.

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

`1800`년은 윤년이 아닙니다.

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

`2007`년은 윤년이 아닙니다.

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

`2002`년은 윤년입니다.

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

`1979`년은 윤년이 아닙니다.

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

`2006`년은 윤년이 아닙니다.

```python
    def test12(self):
        self.assertEqual(leap_year(2006), False, "--err-t12--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def leap_year(year):
    return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0))
```

```python
def leap_year(year):
    while year % 100 == 0:
        year = year // 100
    return year % 4 == 0
```
