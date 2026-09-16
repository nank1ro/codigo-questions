---
language: python
exerciseType: 1
difficulty: 2
title: Cifrado César
---

# --description--

Julio César protegía sus cartas privadas con uno de los trucos más antiguos de la criptografía: reemplazaba cada letra de un mensaje por la letra que está un número fijo de posiciones más adelante en el alfabeto. Con un desplazamiento de 3, la `a` se convierte en `d`, la `b` se convierte en `e` y la `c` se convierte en `f`.

El alfabeto se comporta como un círculo, así que las letras del final vuelven al principio: con un desplazamiento de 3, la `x` se convierte en `a`, la `y` se convierte en `b` y la `z` se convierte en `c`.

Todo lo que no sea una letra, como un espacio, una coma, un signo de exclamación o un dígito, atraviesa el cifrado sin modificarse.

# --instructions--

Escribe una función `caesar_cipher` que reciba un mensaje `text` y un número entero `shift`, y devuelva el mensaje codificado.

Ejemplos:
```
caesar_cipher("hello", 3) ➞ "khoor"
caesar_cipher("xyz", 3) ➞ "abc"
caesar_cipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- El mensaje siempre está en minúsculas, así que nunca tienes que lidiar con letras mayúsculas.
- Los caracteres que no son letras conservan su lugar y su valor.
- El desplazamiento nunca es negativo. Un desplazamiento de `0` deja el mensaje sin cambios, y lo mismo ocurre con un desplazamiento de `26`.

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

Un desplazamiento de 3 convierte "hello" en "khoor"

```python
    def test1(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor", "--err-t1--")
```

El final del alfabeto da la vuelta, así que "xyz" se convierte en "abc"

```python
    def test2(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc", "--err-t2--")
```

Un desplazamiento de 0 deja el mensaje sin cambios

```python
    def test3(self):
        self.assertEqual(caesar_cipher("abc", 0), "abc", "--err-t3--")
```

Un desplazamiento de 26 es una vuelta completa al alfabeto, así que el mensaje queda sin cambios

```python
    def test4(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc", "--err-t4--")
```

Los signos de puntuación y los espacios pasan sin cambios

```python
    def test5(self):
        self.assertEqual(caesar_cipher("codigo, rocks!", 5), "htinlt, wthpx!", "--err-t5--")
```

Un mensaje vacío sigue estando vacío

```python
    def test6(self):
        self.assertEqual(caesar_cipher("", 4), "", "--err-t6--")
```

Los espacios entre letras sueltas se conservan

```python
    def test7(self):
        self.assertEqual(caesar_cipher("a b c", 1), "b c d", "--err-t7--")
```

Los dígitos no se desplazan, ni siquiera con un desplazamiento de 25

```python
    def test8(self):
        self.assertEqual(caesar_cipher("abc 123!", 25), "zab 123!", "--err-t8--")
```

Un desplazamiento de 13 codifica una frase completa

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
