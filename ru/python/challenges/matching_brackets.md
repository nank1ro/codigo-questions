---
language: python
exerciseType: 1
difficulty: 3
title: Сбалансированные скобки
---

# --description--

Текст, в котором есть код, математика или разметка, полон скобок, и каждой открывающей скобке нужна закрывающая того же вида. Строка сбалансирована, когда её скобки образуют пары и вкладываются друг в друга, как слои луковицы: `{[()]}` сбалансирована, а `{[(])}` — нет, ведь круглая пара закрывается раньше квадратной пары, внутри которой она находится.

Здесь учитываются три пары: круглые `()`, квадратные `[]` и фигурные `{}`. Все остальные символы строки игнорируются. Закрывающая скобка должна закрывать последнюю из ещё открытых скобок, а к концу строки не должно остаться ни одной незакрытой скобки.

# --instructions--

Напишите функцию `is_balanced`, которая принимает строку и возвращает `True`, если все скобки в ней образуют пары и правильно вложены, и `False` в противном случае.

Примеры:
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- Пустая строка сбалансирована.
- Символы, не являющиеся скобками, игнорируются.
- Закрывающая скобка должна соответствовать последней из ещё открытых скобок.
- К концу строки не должно оставаться ни одной открытой скобки.

# --seed--

```python
def is_balanced(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Пустая строка сбалансирована

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

Одна пара круглых скобок сбалансирована

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

Три вида пар, вложенные друг в друга, сбалансированы

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

Скобки вперемешку с другим текстом остаются сбалансированными

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

Пары, стоящие друг за другом, сбалансированы

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

Строка вовсе без скобок сбалансирована

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

Перекрёстная пара не сбалансирована

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

Открывающая скобка, которая никогда не закрывается, не сбалансирована

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

Закрывающая скобка раньше любой открывающей не сбалансирована

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

Перекрёстные пары в глубине строки не сбалансированы

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

Лишняя закрывающая скобка в конце строки не сбалансирована

```python
    def test11(self):
        self.assertEqual(is_balanced("())"), False, "--err-t11--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack
```
