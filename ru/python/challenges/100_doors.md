---
language: python
exerciseType: 1
title: 100 дверей
difficulty: 1
---

# --description--

В ряду стоят 100 дверей, все изначально закрыты.
Вы совершаете 100 проходов мимо дверей.
В первый раз вы посещаете каждую дверь и переключаете её (если дверь закрыта — открываете; если открыта — закрываете).
Во второй раз вы посещаете только каждую 2-ю дверь (т.е. дверь №2, №4, №6, ...) и переключаете её.
В третий раз вы посещаете каждую 3-ю дверь (т.е. дверь №3, №6, №9, ...) и т.д., пока не посетите только 100-ю дверь.

# --instructions--

Реализуйте функцию для определения состояния дверей после последнего прохода.
Верните итоговый результат в виде массива, включив в него только номера открытых дверей.
> Метод должен работать с переменным количеством дверей.

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

Для 100 дверей вернуть правильный список открытых дверей

```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_final_opened_doors(100), solution, "--err-t1--")
```

Для 10 дверей вернуть правильный список открытых дверей

```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(get_final_opened_doors(10), solution, "--err-t2--")
```

Для 950 дверей вернуть правильный список открытых дверей

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
