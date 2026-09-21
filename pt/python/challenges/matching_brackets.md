---
language: python
exerciseType: 1
difficulty: 3
title: Colchetes correspondentes
---

# --description--

Textos que contêm código, matemática ou marcação estão cheios de colchetes, e todo colchete de abertura precisa de um colchete de fechamento do mesmo tipo. Uma string está balanceada quando seus colchetes formam pares e se aninham como as camadas de uma cebola: `{[()]}` está balanceada, enquanto `{[(])}` não está, porque o par redondo é fechado antes do par de colchetes dentro do qual ele está.

Três pares contam aqui: parênteses `()`, colchetes `[]` e chaves `{}`. Todos os outros caracteres da string são ignorados. Um colchete de fechamento deve fechar o colchete aberto mais recentemente que ainda esteja aberto, e quando a string termina nenhum colchete pode ficar aberto.

# --instructions--

Escreva uma função `is_balanced` que recebe uma string e retorna `True` quando todos os colchetes nela estão correspondidos e corretamente aninhados, e `False` caso contrário.

Exemplos:
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- Uma string vazia está balanceada.
- Caracteres que não são colchetes são ignorados.
- Um colchete de fechamento deve corresponder ao colchete aberto mais recentemente que ainda esteja aberto.
- Nenhum colchete pode ficar aberto quando a string termina.

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

Uma string vazia está balanceada

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

Um único par de parênteses está balanceado

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

Os três tipos de par aninhados uns dentro dos outros estão balanceados

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

Colchetes misturados com outro texto ainda estão balanceados

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

Pares colocados lado a lado estão balanceados

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

Uma string sem nenhum colchete está balanceada

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

Um par cruzado não está balanceado

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

Um colchete de abertura que nunca é fechado não está balanceado

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

Um colchete de fechamento antes de qualquer colchete de abertura não está balanceado

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

Pares cruzados mais no fundo da string não estão balanceados

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

Um colchete de fechamento que sobra no final não está balanceado

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
