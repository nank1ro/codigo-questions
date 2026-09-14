---
language: python
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

Un pangramma è una frase che usa almeno una volta ogni lettera dell'alfabeto inglese. L'esempio più noto è "the quick brown fox jumps over the lazy dog", che fa stare tutte e 26 le lettere in nove parole brevi.

Il controllo non distingue tra maiuscole e minuscole, quindi `A` e `a` contano come la stessa lettera. Cifre, punteggiatura e spazi vengono ignorati: non sono lettere, ma non sono nemmeno un motivo per rifiutare una frase.

# --instructions--

Scrivi una funzione `is_pangram` che prende una frase e restituisce `True` se la frase è un pangramma e `False` altrimenti.

Esempi:
```
is_pangram("the quick brown fox jumps over the lazy dog") ➞ True
is_pangram("the five boxing wizards jump quickly") ➞ True
is_pangram("a quick movement of the enemy will jeopardize five gunboats") ➞ False
```

- Una frase vuota non è un pangramma.
- Contano solo le 26 lettere dalla `a` alla `z`.

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

Una frase vuota non è un pangramma

```python
    def test1(self):
        self.assertEqual(is_pangram(""), False, "--err-t1--")
```

La frase classica "the quick brown fox jumps over the lazy dog" è un pangramma

```python
    def test2(self):
        self.assertEqual(is_pangram("the quick brown fox jumps over the lazy dog"), True, "--err-t2--")
```

Una frase a cui manca la lettera `x` non è un pangramma

```python
    def test3(self):
        self.assertEqual(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), False, "--err-t3--")
```

La frase "the five boxing wizards jump quickly" è un pangramma

```python
    def test4(self):
        self.assertEqual(is_pangram("the five boxing wizards jump quickly"), True, "--err-t4--")
```

I trattini bassi vengono ignorati, quindi la frase resta un pangramma

```python
    def test5(self):
        self.assertEqual(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True, "--err-t5--")
```

Le cifre vengono ignorate, quindi la frase resta un pangramma

```python
    def test6(self):
        self.assertEqual(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True, "--err-t6--")
```

Le cifre non sostituiscono le lettere `e`, `i` e `t`

```python
    def test7(self):
        self.assertEqual(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False, "--err-t7--")
```

Anche una frase in maiuscolo è un pangramma

```python
    def test8(self):
        self.assertEqual(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), True, "--err-t8--")
```

Mescolare maiuscole e minuscole della stessa metà dell'alfabeto non basta

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
