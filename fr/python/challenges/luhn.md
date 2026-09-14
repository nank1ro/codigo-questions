---
language: python
exerciseType: 1
difficulty: 2
title: Luhn checksum
---

# --description--

L'algorithme de Luhn est une somme de contrôle simple utilisée pour valider des numéros d'identification, tels que les numéros de carte bancaire.

Avant de vérifier un numéro, supprimez tous les espaces de la chaîne. La chaîne est valide uniquement si ce qui reste contient plus d'un caractère et si la chaîne d'origine ne contient rien d'autre que des chiffres et des espaces.

Pour effectuer la vérification, partez du chiffre le plus à droite et progressez vers la gauche en doublant un chiffre sur deux. Lorsque le doublement produit un nombre supérieur à 9, soustrayez-lui 9. Additionnez ensuite tous les chiffres : le numéro est valide uniquement si la somme est divisible par 10.

Par exemple, `"059"` donne `0`, puis `5` doublé donne `10`, qui devient `1`, puis `9`. Leur somme est `10`, qui est divisible par 10, donc le numéro est valide.

# --instructions--

Écrivez une fonction `is_valid` qui prend une chaîne et retourne `True` lorsque le numéro est valide, `False` sinon.

- `"4539 3195 0343 6467"` passe la somme de contrôle, donc le résultat est `True`.
- `"8273 1232 7352 0569"` échoue à la somme de contrôle, donc le résultat est `False`.
- `"0"` ne contient qu'un seul caractère, donc le résultat est `False`.
- `"055-444-285"` contient un caractère qui n'est ni un chiffre ni un espace, donc le résultat est `False`.

Exemple d'appel de fonction :
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

Un chiffre seul n'est pas valide.

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

Un chiffre seul avec un espace au début n'est pas valide.

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

Le numéro `"059"` est valide.

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

Le numéro `"59"` est valide.

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

Le numéro `"055 444 285"` est valide.

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

Le numéro `"055 444 286"` n'est pas valide.

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

Le numéro `"8273 1232 7352 0569"` n'est pas valide.

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

Le numéro `"4539 3195 0343 6467"` est valide.

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

Le numéro `"1 2345 6789 1234 5678 9012"` n'est pas valide.

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

Le numéro `"095 245 88"` est valide.

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

Une lettre rend le numéro invalide.

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

Les tirets rendent le numéro invalide.

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

Un caractère de ponctuation rend le numéro invalide.

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

Les symboles rendent le numéro invalide.

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

Une chaîne vide n'est pas valide.

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
