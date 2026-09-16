---
language: python
exerciseType: 1
difficulty: 2
title: Caesar-Verschlüsselung
---

# --description--

Julius Caesar schützte seine privaten Briefe mit einem der ältesten Tricks der Kryptografie: Er ersetzte jeden Buchstaben einer Nachricht durch den Buchstaben, der eine feste Anzahl von Stellen weiter hinten im Alphabet steht. Bei einer Verschiebung von 3 wird `a` zu `d`, `b` zu `e` und `c` zu `f`.

Das Alphabet verhält sich wie ein Kreis, daher laufen die Buchstaben am Ende wieder zum Anfang zurück: Bei einer Verschiebung von 3 wird `x` zu `a`, `y` zu `b` und `z` zu `c`.

Alles, was kein Buchstabe ist, etwa ein Leerzeichen, ein Komma, ein Ausrufezeichen oder eine Ziffer, durchläuft die Verschlüsselung unverändert.

# --instructions--

Schreiben Sie eine Funktion `caesar_cipher`, die eine Nachricht `text` und eine ganze Zahl `shift` entgegennimmt und die verschlüsselte Nachricht zurückgibt.

Beispiele:
```
caesar_cipher("hello", 3) ➞ "khoor"
caesar_cipher("xyz", 3) ➞ "abc"
caesar_cipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Die Nachricht besteht immer aus Kleinbuchstaben, Sie müssen sich also nie um Großbuchstaben kümmern.
- Zeichen, die keine Buchstaben sind, behalten ihren Platz und ihren Wert.
- Die Verschiebung ist nie negativ. Eine Verschiebung von `0` lässt die Nachricht unverändert, und eine Verschiebung von `26` ebenfalls.

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

Eine Verschiebung von 3 macht aus "hello" "khoor"

```python
    def test1(self):
        self.assertEqual(caesar_cipher("hello", 3), "khoor", "--err-t1--")
```

Die Buchstaben am Ende des Alphabets laufen zum Anfang zurück, daher wird "xyz" zu "abc"

```python
    def test2(self):
        self.assertEqual(caesar_cipher("xyz", 3), "abc", "--err-t2--")
```

Eine Verschiebung von 0 lässt die Nachricht unverändert

```python
    def test3(self):
        self.assertEqual(caesar_cipher("abc", 0), "abc", "--err-t3--")
```

Eine Verschiebung von 26 ist eine volle Runde durch das Alphabet, daher bleibt die Nachricht unverändert

```python
    def test4(self):
        self.assertEqual(caesar_cipher("abc", 26), "abc", "--err-t4--")
```

Satzzeichen und Leerzeichen werden unverändert durchgereicht

```python
    def test5(self):
        self.assertEqual(caesar_cipher("codigo, rocks!", 5), "htinlt, wthpx!", "--err-t5--")
```

Eine leere Nachricht bleibt leer

```python
    def test6(self):
        self.assertEqual(caesar_cipher("", 4), "", "--err-t6--")
```

Leerzeichen zwischen einzelnen Buchstaben bleiben erhalten

```python
    def test7(self):
        self.assertEqual(caesar_cipher("a b c", 1), "b c d", "--err-t7--")
```

Ziffern werden nicht verschoben, auch nicht bei einer Verschiebung von 25

```python
    def test8(self):
        self.assertEqual(caesar_cipher("abc 123!", 25), "zab 123!", "--err-t8--")
```

Eine Verschiebung von 13 verschlüsselt einen ganzen Satz

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
