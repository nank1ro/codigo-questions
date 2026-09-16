---
language: python
exerciseType: 1
difficulty: 2
title: Анаграмма
---

# --description--

Два слова являются анаграммами, когда одно из них является перестановкой другого: они используют ровно одни и те же буквы, и каждая буква встречается одно и то же число раз, просто в другом порядке. `listen` и `silent` — анаграммы, как и `stone` и `tones`.

Слово никогда не является анаграммой самого себя. Если два слова полностью совпадают, ничего не переставлялось, поэтому ответ — `True`. Оба слова заданы в нижнем регистре и содержат только буквы от `a` до `z`.

# --instructions--

Напишите функцию `is_anagram`, которая принимает два слова, `first` и `second`, и возвращает `True`, если они являются анаграммами друг друга, и `False` в противном случае.

Примеры:
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- Два одинаковых слова не являются анаграммами.
- Слова разной длины никогда не являются анаграммами.
- Каждая буква должна встречаться в обоих словах одинаковое число раз.

# --seed--

```python
def is_anagram(first, second):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Слова "listen" и "silent" являются анаграммами

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

Слова "stone" и "tones" являются анаграммами

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

Слово не является анаграммой самого себя

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

Слова разной длины не являются анаграммами

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

Одни и те же буквы в разном количестве не являются анаграммой

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

Слова "anagram" и "nagaram" являются анаграммами

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

Два слова одинаковой длины с разными буквами не являются анаграммами

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

Два пустых слова идентичны, поэтому они не являются анаграммами

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

Две разные одиночные буквы не являются анаграммами

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

Слова "evil" и "vile" являются анаграммами

```python
    def test10(self):
        self.assertEqual(is_anagram("evil", "vile"), True, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_anagram(first, second):
    if first == second:
        return False

    return sorted(first) == sorted(second)
```
