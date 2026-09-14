---
language: python
exerciseType: 1
difficulty: 1
title: Pangrama
---

# --description--

Um pangrama é uma frase que usa cada letra do alfabeto inglês pelo menos uma vez. O exemplo mais conhecido é "the quick brown fox jumps over the lazy dog", que reúne todas as 26 letras em nove palavras curtas.

A verificação não diferencia maiúsculas de minúsculas, então `A` e `a` contam como a mesma letra. Dígitos, pontuação e espaços são ignorados: não são letras, mas também não são motivo para rejeitar uma frase.

# --instructions--

Escreva uma função `is_pangram` que recebe uma frase e retorna `True` se a frase for um pangrama e `False` caso contrário.

Exemplos:
```
is_pangram("the quick brown fox jumps over the lazy dog") ➞ True
is_pangram("the five boxing wizards jump quickly") ➞ True
is_pangram("a quick movement of the enemy will jeopardize five gunboats") ➞ False
```

- Uma frase vazia não é um pangrama.
- Apenas as 26 letras de `a` a `z` contam.

# --seed--

```python
def is_pangram(sentence):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Uma frase vazia não é um pangrama

```python
    def test1(self):
        self.assertEqual(is_pangram(""), False, "--err-t1--")
```

A frase clássica "the quick brown fox jumps over the lazy dog" é um pangrama

```python
    def test2(self):
        self.assertEqual(is_pangram("the quick brown fox jumps over the lazy dog"), True, "--err-t2--")
```

Uma frase sem a letra `x` não é um pangrama

```python
    def test3(self):
        self.assertEqual(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), False, "--err-t3--")
```

A frase "the five boxing wizards jump quickly" é um pangrama

```python
    def test4(self):
        self.assertEqual(is_pangram("the five boxing wizards jump quickly"), True, "--err-t4--")
```

Sublinhados são ignorados, então a frase ainda é um pangrama

```python
    def test5(self):
        self.assertEqual(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True, "--err-t5--")
```

Dígitos são ignorados, então a frase ainda é um pangrama

```python
    def test6(self):
        self.assertEqual(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True, "--err-t6--")
```

Dígitos não substituem as letras `e`, `i` e `t`

```python
    def test7(self):
        self.assertEqual(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False, "--err-t7--")
```

Uma frase em maiúsculas também é um pangrama

```python
    def test8(self):
        self.assertEqual(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), True, "--err-t8--")
```

Misturar maiúsculas e minúsculas da mesma metade do alfabeto não é suficiente

```python
    def test9(self):
        self.assertEqual(is_pangram("abcdefghijklm ABCDEFGHIJKLM"), False, "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_pangram(sentence):
    letters = set()

    for char in sentence.lower():
        if "a" <= char <= "z":
            letters.add(char)

    return len(letters) == 26
```
