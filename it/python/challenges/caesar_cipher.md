---
language: python
exerciseType: 1
difficulty: 2
title: Cifrario di Cesare
---

# --description--

Giulio Cesare proteggeva le sue lettere private con uno dei trucchi più antichi della crittografia: sostituiva ogni lettera di un messaggio con la lettera che si trova un numero fisso di posizioni più avanti nell'alfabeto. Con uno spostamento di 3, `a` diventa `d`, `b` diventa `e` e `c` diventa `f`.

L'alfabeto si comporta come un cerchio, quindi le lettere della fine tornano all'inizio: con uno spostamento di 3, `x` diventa `a`, `y` diventa `b` e `z` diventa `c`.

Tutto ciò che non è una lettera, come uno spazio, una virgola, un punto esclamativo o una cifra, attraversa il cifrario senza subire modifiche.

# --instructions--

Scrivi una funzione `caesar_cipher` che riceve un messaggio `text` e un numero intero `shift`, e restituisce il messaggio codificato.

Esempi:
```
caesar_cipher("hello", 3) ➞ "khoor"
caesar_cipher("xyz", 3) ➞ "abc"
caesar_cipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Il messaggio è sempre in minuscolo, quindi non dovrai mai occuparti delle lettere maiuscole.
- I caratteri che non sono lettere mantengono la loro posizione e il loro valore.
- Lo spostamento non è mai negativo. Uno spostamento di `0` lascia il messaggio invariato, e così anche uno spostamento di `26`.

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

Uno spostamento di 3 trasforma "hello" in "khoor"

```python
    def test1(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor", "--err-t1--")
```

La fine dell'alfabeto ricomincia da capo, quindi "xyz" diventa "abc"

```python
    def test2(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc", "--err-t2--")
```

Uno spostamento di 0 lascia il messaggio invariato

```python
    def test3(self):
        self.assertEqual(caesar_cipher("abc", 0), "abc", "--err-t3--")
```

Uno spostamento di 26 è un giro completo dell'alfabeto, quindi il messaggio resta invariato

```python
    def test4(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc", "--err-t4--")
```

Punteggiatura e spazi passano invariati

```python
    def test5(self):
        self.assertEqual(caesar_cipher("codigo, rocks!", 5), "htinlt, wthpx!", "--err-t5--")
```

Un messaggio vuoto resta vuoto

```python
    def test6(self):
        self.assertEqual(caesar_cipher("", 4), "", "--err-t6--")
```

Gli spazi tra singole lettere vengono preservati

```python
    def test7(self):
        self.assertEqual(caesar_cipher("a b c", 1), "b c d", "--err-t7--")
```

Le cifre non vengono spostate, nemmeno con uno spostamento di 25

```python
    def test8(self):
        self.assertEqual(caesar_cipher("abc 123!", 25), "zab 123!", "--err-t8--")
```

Uno spostamento di 13 codifica una frase intera

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
