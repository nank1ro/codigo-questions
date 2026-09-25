---
language: python
exerciseType: 1
difficulty: 3
title: Passende Klammern
---

# --description--

Text, der Code, Formeln oder Markup enthält, ist voller Klammern, und jede öffnende Klammer braucht eine schließende derselben Art. Ein String ist ausgeglichen, wenn sich seine Klammern paarweise entsprechen und wie die Schichten einer Zwiebel verschachteln: `{[()]}` ist ausgeglichen, `{[(])}` dagegen nicht, weil das runde Paar vor dem eckigen Paar geschlossen wird, in dem es liegt.

Hier zählen drei Paare: runde `()`, eckige `[]` und geschweifte `{}`. Jedes andere Zeichen im String wird ignoriert. Eine schließende Klammer muss die zuletzt geöffnete Klammer schließen, die noch offen ist, und wenn der String endet, darf keine Klammer offen geblieben sein.

# --instructions--

Schreiben Sie eine Funktion `is_balanced`, die einen String entgegennimmt und `True` zurückgibt, wenn alle darin enthaltenen Klammern übereinstimmen und korrekt verschachtelt sind, und andernfalls `False`.

Beispiele:
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- Ein leerer String ist ausgeglichen.
- Zeichen, die keine Klammern sind, werden ignoriert.
- Eine schließende Klammer muss zu der zuletzt geöffneten Klammer passen, die noch offen ist.
- Wenn der String endet, darf keine Klammer offen geblieben sein.

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

Ein leerer String ist ausgeglichen

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

Ein einzelnes Paar runder Klammern ist ausgeglichen

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

Die drei Arten von Paaren, ineinander verschachtelt, sind ausgeglichen

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

Klammern, die mit anderem Text vermischt sind, sind weiterhin ausgeglichen

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

Nebeneinander stehende Paare sind ausgeglichen

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

Ein String ohne jegliche Klammern ist ausgeglichen

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

Ein überkreuztes Paar ist nicht ausgeglichen

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

Eine öffnende Klammer, die nie geschlossen wird, ist nicht ausgeglichen

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

Eine schließende Klammer vor jeder öffnenden ist nicht ausgeglichen

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

Überkreuzte Paare tiefer im String sind nicht ausgeglichen

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

Eine am Ende übrig gebliebene schließende Klammer ist nicht ausgeglichen

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
