---
language: python
exerciseType: 1
difficulty: 1
title: Pangrama
---

# --description--

Un pangrama es una frase que usa cada letra del alfabeto inglés al menos una vez. El ejemplo más conocido es "the quick brown fox jumps over the lazy dog", que encaja las 26 letras en nueve palabras cortas.

La comprobación no distingue entre mayúsculas y minúsculas, por lo que `A` y `a` cuentan como la misma letra. Los dígitos, los signos de puntuación y los espacios se ignoran: no son letras, pero tampoco son motivo para rechazar una frase.

# --instructions--

Escribe una función `is_pangram` que reciba una frase y devuelva `True` si la frase es un pangrama y `False` en caso contrario.

Ejemplos:
```
is_pangram("the quick brown fox jumps over the lazy dog") ➞ True
is_pangram("the five boxing wizards jump quickly") ➞ True
is_pangram("a quick movement of the enemy will jeopardize five gunboats") ➞ False
```

- Una frase vacía no es un pangrama.
- Solo cuentan las 26 letras de la `a` a la `z`.

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

Una frase vacía no es un pangrama

```python
    def test1(self):
        self.assertEqual(is_pangram(""), False, "--err-t1--")
```

La frase clásica "the quick brown fox jumps over the lazy dog" es un pangrama

```python
    def test2(self):
        self.assertEqual(is_pangram("the quick brown fox jumps over the lazy dog"), True, "--err-t2--")
```

Una frase a la que le falta la letra `x` no es un pangrama

```python
    def test3(self):
        self.assertEqual(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), False, "--err-t3--")
```

La frase "the five boxing wizards jump quickly" es un pangrama

```python
    def test4(self):
        self.assertEqual(is_pangram("the five boxing wizards jump quickly"), True, "--err-t4--")
```

Los guiones bajos se ignoran, por lo que la frase sigue siendo un pangrama

```python
    def test5(self):
        self.assertEqual(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True, "--err-t5--")
```

Los dígitos se ignoran, por lo que la frase sigue siendo un pangrama

```python
    def test6(self):
        self.assertEqual(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True, "--err-t6--")
```

Los dígitos no reemplazan a las letras `e`, `i` y `t`

```python
    def test7(self):
        self.assertEqual(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False, "--err-t7--")
```

Una frase en mayúsculas también es un pangrama

```python
    def test8(self):
        self.assertEqual(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), True, "--err-t8--")
```

Mezclar mayúsculas y minúsculas de la misma mitad del alfabeto no es suficiente

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
