---
language: python
exerciseType: 1
difficulty: 2
title: Anagramm
---

# --description--

Zwei Wörter sind Anagramme, wenn eines eine Umordnung des anderen ist: Sie verwenden exakt dieselben Buchstaben, jeden Buchstaben gleich oft, nur in einer anderen Reihenfolge. `listen` und `silent` sind Anagramme, und ebenso `stone` und `tones`.

Ein Wort ist nie ein Anagramm von sich selbst. Wenn die beiden Wörter exakt gleich sind, wurde nichts umgeordnet, daher ist die Antwort `False`. Beide Wörter sind in Kleinbuchstaben gegeben und enthalten nur die Buchstaben von `a` bis `z`.

# --instructions--

Schreiben Sie eine Funktion `is_anagram`, die zwei Wörter, `first` und `second`, entgegennimmt und `True` zurückgibt, wenn sie Anagramme voneinander sind, und andernfalls `False`.

Beispiele:
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- Zwei identische Wörter sind keine Anagramme.
- Wörter unterschiedlicher Länge sind nie Anagramme.
- Jeder Buchstabe muss in beiden Wörtern gleich oft vorkommen.

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

Die Wörter "listen" und "silent" sind Anagramme

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

Die Wörter "stone" und "tones" sind Anagramme

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

Ein Wort ist kein Anagramm von sich selbst

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

Wörter unterschiedlicher Länge sind keine Anagramme

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

Dieselben Buchstaben in unterschiedlicher Anzahl sind kein Anagramm

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

Die Wörter "anagram" und "nagaram" sind Anagramme

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

Zwei Wörter derselben Länge mit unterschiedlichen Buchstaben sind keine Anagramme

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

Zwei leere Wörter sind identisch, daher sind sie keine Anagramme

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

Zwei unterschiedliche einzelne Buchstaben sind keine Anagramme

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

Die Wörter "evil" und "vile" sind Anagramme

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
