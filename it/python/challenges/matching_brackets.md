---
language: python
exerciseType: 1
difficulty: 3
title: Parentesi bilanciate
---

# --description--

Il testo che contiene codice, formule matematiche o markup è pieno di parentesi, e ogni parentesi aperta ha bisogno di una chiusa dello stesso tipo. Una stringa è bilanciata quando le sue parentesi si accoppiano e si annidano come gli strati di una cipolla: `{[()]}` è bilanciata, mentre `{[(])}` non lo è, perché la coppia tonda viene chiusa prima della coppia quadrata al cui interno si trova.

Qui contano tre coppie: le tonde `()`, le quadre `[]` e le graffe `{}`. Ogni altro carattere della stringa viene ignorato. Una parentesi chiusa deve chiudere la parentesi aperta più di recente che risulta ancora aperta, e quando la stringa termina nessuna parentesi può rimanere aperta.

# --instructions--

Scrivi una funzione `is_balanced` che prende una stringa e restituisce `True` quando tutte le parentesi in essa contenute sono accoppiate e correttamente annidate, e `False` altrimenti.

Esempi:
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- Una stringa vuota è bilanciata.
- I caratteri che non sono parentesi vengono ignorati.
- Una parentesi chiusa deve corrispondere alla parentesi aperta più di recente che risulta ancora aperta.
- Nessuna parentesi può rimanere aperta quando la stringa termina.

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

Una stringa vuota è bilanciata

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

Una singola coppia di parentesi tonde è bilanciata

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

I tre tipi di coppia annidati l'uno dentro l'altro sono bilanciati

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

Parentesi mescolate ad altro testo restano comunque bilanciate

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

Coppie poste una accanto all'altra sono bilanciate

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

Una stringa senza alcuna parentesi è bilanciata

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

Una coppia incrociata non è bilanciata

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

Una parentesi aperta che non viene mai chiusa non è bilanciata

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

Una parentesi chiusa prima di qualsiasi parentesi aperta non è bilanciata

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

Coppie incrociate più in profondità nella stringa non sono bilanciate

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

Una parentesi chiusa lasciata alla fine non è bilanciata

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
