---
language: python
exerciseType: 1
difficulty: 2
title: Anagrama
---

# --description--

Dos palabras son anagramas cuando una es una reordenación de la otra: usan exactamente las mismas letras, cada letra el mismo número de veces, solo que en un orden diferente. `listen` y `silent` son anagramas, y también lo son `stone` y `tones`.

Una palabra nunca es un anagrama de sí misma. Si las dos palabras son exactamente iguales, no se ha reordenado nada, así que la respuesta es `False`. Ambas palabras se dan en minúsculas y contienen solo las letras de la `a` a la `z`.

# --instructions--

Escribe una función `is_anagram` que reciba dos palabras, `first` y `second`, y devuelva `True` cuando sean anagramas la una de la otra y `False` en caso contrario.

Ejemplos:
```
is_anagram("listen", "silent") ➞ True
is_anagram("stone", "tones") ➞ True
is_anagram("stone", "stone") ➞ False
is_anagram("abc", "abcd") ➞ False
is_anagram("aab", "abb") ➞ False
```

- Dos palabras idénticas no son anagramas.
- Palabras de longitudes diferentes nunca son anagramas.
- Cada letra debe aparecer el mismo número de veces en ambas palabras.

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

Las palabras "listen" y "silent" son anagramas

```python
    def test1(self):
        self.assertEqual(is_anagram("listen", "silent"), True, "--err-t1--")
```

Las palabras "stone" y "tones" son anagramas

```python
    def test2(self):
        self.assertEqual(is_anagram("stone", "tones"), True, "--err-t2--")
```

Una palabra no es un anagrama de sí misma

```python
    def test3(self):
        self.assertEqual(is_anagram("stone", "stone"), False, "--err-t3--")
```

Palabras de longitudes diferentes no son anagramas

```python
    def test4(self):
        self.assertEqual(is_anagram("abc", "abcd"), False, "--err-t4--")
```

Las mismas letras en cantidades diferentes no forman un anagrama

```python
    def test5(self):
        self.assertEqual(is_anagram("aab", "abb"), False, "--err-t5--")
```

Las palabras "anagram" y "nagaram" son anagramas

```python
    def test6(self):
        self.assertEqual(is_anagram("anagram", "nagaram"), True, "--err-t6--")
```

Dos palabras de la misma longitud con letras diferentes no son anagramas

```python
    def test7(self):
        self.assertEqual(is_anagram("rat", "car"), False, "--err-t7--")
```

Dos palabras vacías son idénticas, así que no son anagramas

```python
    def test8(self):
        self.assertEqual(is_anagram("", ""), False, "--err-t8--")
```

Dos letras individuales diferentes no son anagramas

```python
    def test9(self):
        self.assertEqual(is_anagram("a", "b"), False, "--err-t9--")
```

Las palabras "evil" y "vile" son anagramas

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
