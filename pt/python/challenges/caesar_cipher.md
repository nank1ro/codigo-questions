---
language: python
exerciseType: 1
difficulty: 2
title: Cifra de César
---

# --description--

Júlio César protegia as suas cartas particulares com um dos truques mais antigos da criptografia: ele substituía cada letra de uma mensagem pela letra que está um número fixo de posições à frente no alfabeto. Com um deslocamento de 3, `a` vira `d`, `b` vira `e` e `c` vira `f`.

O alfabeto funciona como um círculo, então as letras no final voltam para o começo: com um deslocamento de 3, `x` vira `a`, `y` vira `b` e `z` vira `c`.

Qualquer coisa que não seja uma letra, como um espaço, uma vírgula, um ponto de exclamação ou um dígito, atravessa a cifra sem sofrer alterações.

# --instructions--

Escreva uma função `caesar_cipher` que receba uma mensagem `text` e um número inteiro `shift`, e retorne a mensagem codificada.

Exemplos:
```
caesar_cipher("hello", 3) ➞ "khoor"
caesar_cipher("xyz", 3) ➞ "abc"
caesar_cipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- A mensagem está sempre em minúsculas, então você nunca precisa lidar com letras maiúsculas.
- Os caracteres que não são letras mantêm o seu lugar e o seu valor.
- O deslocamento nunca é negativo. Um deslocamento de `0` deixa a mensagem inalterada, e o mesmo acontece com um deslocamento de `26`.

# --seed--

```python
def caesar_cipher(text, shift):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Um deslocamento de 3 transforma "hello" em "khoor"

```python
    def test1(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor", "--err-t1--")
```

O final do alfabeto dá a volta, então "xyz" vira "abc"

```python
    def test2(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc", "--err-t2--")
```

Um deslocamento de 0 deixa a mensagem inalterada

```python
    def test3(self):
        self.assertEqual(caesar_cipher("abc", 0), "abc", "--err-t3--")
```

Um deslocamento de 26 é uma volta completa no alfabeto, então a mensagem fica inalterada

```python
    def test4(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc", "--err-t4--")
```

A pontuação e os espaços passam sem sofrer alterações

```python
    def test5(self):
        self.assertEqual(caesar_cipher("codigo, rocks!", 5), "htinlt, wthpx!", "--err-t5--")
```

Uma mensagem vazia continua vazia

```python
    def test6(self):
        self.assertEqual(caesar_cipher("", 4), "", "--err-t6--")
```

Os espaços entre letras isoladas são preservados

```python
    def test7(self):
        self.assertEqual(caesar_cipher("a b c", 1), "b c d", "--err-t7--")
```

Os dígitos não são deslocados, mesmo com um deslocamento de 25

```python
    def test8(self):
        self.assertEqual(caesar_cipher("abc 123!", 25), "zab 123!", "--err-t8--")
```

Um deslocamento de 13 codifica uma frase inteira

```python
    def test9(self):
        self.assertEqual(caesar_cipher("the quick brown fox jumps over the lazy dog", 13), "gur dhvpx oebja sbk whzcf bire gur ynml qbt", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if "a" <= char <= "z":
            result += chr(ord("a") + (ord(char) - ord("a") + shift) % 26)
        else:
            result += char

    return result
```
