---
language: python
exerciseType: 1
difficulty: 2
title: Сортировка пузырьком
---

# --description--

Сортировка пузырьком — один из самых простых алгоритмов сортировки. Он проходит по списку и сравнивает каждую пару соседних элементов, меняя их местами всякий раз, когда они стоят в неправильном порядке. После каждого полного прохода наибольшее из оставшихся значений «всплывает» на своё окончательное место, а список считается отсортированным, как только проход завершается без единого обмена.

# --instructions--

Напишите функцию с именем `bubble_sort`, которая принимает список целых чисел и возвращает **новый** список с теми же значениями, отсортированными по возрастанию. Переданный список изменять нельзя.

Вы должны сами реализовать алгоритм сортировки пузырьком, сравнивая и меняя местами соседние элементы. Не используйте функцию сортировки из стандартной библиотеки.

Ваша функция также должна работать с пустым массивом, массивом из одного элемента, уже отсортированным массивом, повторяющимися значениями и отрицательными числами.

Пример вызова функции:
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

Пустой массив должен вернуть пустой массив

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

Массив из одного элемента должен остаться прежним

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

Уже отсортированный массив должен сохранить тот же порядок

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

Массив, отсортированный в обратном порядке, должен быть упорядочен по возрастанию

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

Все повторяющиеся значения должны сохраниться

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

Отрицательные числа должны быть отсортированы перед положительными

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

Более длинный смешанный массив должен быть отсортирован по возрастанию

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

Переданный массив изменять нельзя

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
