---
language: python
exerciseType: 1
difficulty: 2
title: Двоичный поиск
---

# --description--

Двоичный поиск находит значение внутри **отсортированной** коллекции, многократно деля диапазон поиска пополам: посмотрите на элемент в середине, и если это не тот, который вам нужен, продолжайте в левой половине, когда искомое значение меньше, или в правой половине, когда оно больше.

Поскольку каждый шаг отбрасывает половину оставшихся элементов, двоичный поиск приходит к ответу за считанные сравнения даже на очень больших коллекциях, тогда как проверка элементов по одному стоила бы столько шагов, сколько есть элементов.

# --instructions--

Напишите функцию `binary_search`, которая принимает список целых чисел, отсортированный по возрастанию, и искомое целое число, и возвращает индекс искомого числа в списке или `-1`, если числа в списке нет.

Список никогда не содержит дубликатов, поэтому индекс всегда уникален. Список также может быть пустым. Ваша функция должна использовать двоичный поиск, деля диапазон поиска пополам на каждом шаге, а не линейный перебор.

Пример вызова функции:
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

Поиск в пустом списке должен вернуть -1

```python
    def test1(self):
        self.assertEqual(binary_search([], 7), -1, "--err-t1--")
```

Поиск 5 в `[5]` должен вернуть 0

```python
    def test2(self):
        self.assertEqual(binary_search([5], 5), 0, "--err-t2--")
```

Поиск 9 в `[5]` должен вернуть -1

```python
    def test3(self):
        self.assertEqual(binary_search([5], 9), -1, "--err-t3--")
```

Первый элемент -9 списка из 12 элементов должен быть найден по индексу 0

```python
    def test4(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, "--err-t4--")
```

Последний элемент 78 списка из 12 элементов должен быть найден по индексу 11

```python
    def test5(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, "--err-t5--")
```

Элемент 15 должен быть найден по индексу 6

```python
    def test6(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, "--err-t6--")
```

Элемент 22 должен быть найден по индексу 7

```python
    def test7(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, "--err-t7--")
```

Значение 12, которое находится между 11 и 15, должно вернуть -1

```python
    def test8(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, "--err-t8--")
```

Искомое значение меньше всех элементов должно вернуть -1

```python
    def test9(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, "--err-t9--")
```

Искомое значение больше всех элементов должно вернуть -1

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
