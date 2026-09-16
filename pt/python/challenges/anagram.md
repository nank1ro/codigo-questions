---
language: python
exerciseType: 1
difficulty: 2
title: Anagrama
---

# --description--

Duas palavras são anagramas quando uma é um rearranjo da outra: elas usam exatamente as mesmas letras, cada letra o mesmo número de vezes, apenas em uma ordem diferente. `listen` e `silent` são anagramas, assim como `stone` e `tones`.

Uma palavra nunca é um anagrama de si mesma. Se as duas palavras forem exatamente iguais, nada foi rearranjado, então a resposta é `False`. Ambas as palavras são dadas em minúsculas e contêm apenas as letras de `a` a `z`.

# --instructions--

Escreva uma função `is_anagram` que recebe duas palavras, `first` e `second`, e retorna `True` quando elas são anagramas uma da outra e `False` caso contrário.

Exemplos:
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- Duas palavras idênticas não são anagramas.
- Palavras de tamanhos diferentes nunca são anagramas.
- Cada letra deve aparecer o mesmo número de vezes nas duas palavras.

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

As palavras "listen" e "silent" são anagramas

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

As palavras "stone" e "tones" são anagramas

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

Uma palavra não é um anagrama de si mesma

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

Palavras de tamanhos diferentes não são anagramas

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

As mesmas letras em quantidades diferentes não formam um anagrama

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

As palavras "anagram" e "nagaram" são anagramas

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

Duas palavras do mesmo tamanho com letras diferentes não são anagramas

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

Duas palavras vazias são idênticas, então não são anagramas

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

Duas letras únicas diferentes não são anagramas

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

As palavras "evil" e "vile" são anagramas

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
