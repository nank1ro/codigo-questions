---
language: python
exerciseType: 1
difficulty: 2
title: Checksum de Luhn
---

# --description--

O algoritmo de Luhn é um checksum simples usado para validar números de identificação, como números de cartão de crédito.

Antes de verificar um número, remova todos os espaços da string. A string só é válida se o que restar tiver mais de um caractere e se a string original contiver nada além de dígitos e espaços.

Para fazer a verificação, comece pelo dígito mais à direita e avance para a esquerda, dobrando cada segundo dígito. Quando a duplicação produzir um número maior que 9, subtraia 9 dele. Em seguida, some todos os dígitos: o número só é válido se a soma for divisível por 10.

Por exemplo, `"059"` resulta em `0`, depois `5` dobrado é `10`, que se torna `1`, e depois `9`. A soma deles é `10`, que é divisível por 10, então o número é válido.

# --instructions--

Escreva uma função `is_valid` que recebe uma string e retorna `True` quando o número é válido, `False` caso contrário.

- `"4539 3195 0343 6467"` passa no checksum, então o resultado é `True`.
- `"8273 1232 7352 0569"` falha no checksum, então o resultado é `False`.
- `"0"` tem apenas um caractere, então o resultado é `False`.
- `"055-444-285"` contém um caractere que não é um dígito nem um espaço, então o resultado é `False`.

Exemplo de chamada de função:
```python
print(is_valid("095 245 88"))
# prints True
```

# --seed--

```python
def is_valid(value):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Um único dígito não é válido.

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

Um único dígito com um espaço à esquerda não é válido.

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

O número `"059"` é válido.

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

O número `"59"` é válido.

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

O número `"055 444 285"` é válido.

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

O número `"055 444 286"` não é válido.

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

O número `"8273 1232 7352 0569"` não é válido.

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

O número `"4539 3195 0343 6467"` é válido.

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

O número `"1 2345 6789 1234 5678 9012"` não é válido.

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

O número `"095 245 88"` é válido.

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

Uma letra torna o número inválido.

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

Travessões tornam o número inválido.

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

Um caractere de pontuação torna o número inválido.

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

Símbolos tornam o número inválido.

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

Uma string vazia não é válida.

```python
    def test_an_empty_string_is_not_valid(self):
        self.assertEqual(is_valid(""), False, "--err-t15--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_valid(value):
    total = 0
    count = 0
    for char in reversed(value):
        if char == ' ':
            continue
        if char < '0' or char > '9':
            return False
        digit = int(char)
        if count % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        count += 1
    return count > 1 and total % 10 == 0
```
