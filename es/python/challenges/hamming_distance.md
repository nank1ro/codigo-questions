---
language: python
exerciseType: 1
difficulty: 1
title: Distancia de Hamming
---

# --description--

El ADN se escribe como una hebra de nucleótidos, cada uno una sola letra: `A`, `C`, `G` o `T`. Cuando dos hebras de la misma longitud se alinean una junto a la otra, algunas posiciones contienen el mismo nucleótido y otras contienen uno diferente.

El número de posiciones en las que las dos hebras difieren se llama distancia de Hamming, y los biólogos la usan para medir cuán lejos han divergido dos hebras. Alinear `GAGCCTACTAACGGGAT` con `CATCGTAATGACGGCCT` da 7 posiciones que difieren, así que su distancia de Hamming es 7.

# --instructions--

Escribe una función `hamming_distance` que reciba dos hebras de ADN de la misma longitud y devuelva el número de posiciones en las que difieren.

Ejemplos:
```
hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hamming_distance("A", "A") ➞ 0
hamming_distance("AG", "CT") ➞ 2
hamming_distance("", "") ➞ 0
```

- Las dos hebras siempre tienen la misma longitud, así que nunca tienes que manejar hebras de longitudes diferentes.
- Dos hebras vacías no difieren en ninguna posición, así que su distancia es 0.

# --seed--

```python
def hamming_distance(left, right):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Dos hebras vacías no difieren en ninguna posición

```python
    def test1(self):
        self.assertEqual(hamming_distance("", ""), 0, "--err-t1--")
```

Dos hebras de un solo nucleótido idénticas no tienen ninguna diferencia

```python
    def test2(self):
        self.assertEqual(hamming_distance("A", "A"), 0, "--err-t2--")
```

Dos hebras de un solo nucleótido diferente difieren en una posición

```python
    def test3(self):
        self.assertEqual(hamming_distance("A", "G"), 1, "--err-t3--")
```

Dos hebras cortas que difieren en todas las posiciones

```python
    def test4(self):
        self.assertEqual(hamming_distance("AG", "CT"), 2, "--err-t4--")
```

Dos hebras cortas que difieren solo en la primera posición

```python
    def test5(self):
        self.assertEqual(hamming_distance("AT", "CT"), 1, "--err-t5--")
```

Un único nucleótido diferente en medio de las hebras

```python
    def test6(self):
        self.assertEqual(hamming_distance("GGACG", "GGTCG"), 1, "--err-t6--")
```

Los mismos nucleótidos en posiciones diferentes siguen contando como diferencias

```python
    def test7(self):
        self.assertEqual(hamming_distance("TAG", "GAT"), 2, "--err-t7--")
```

Un par de hebras más largo con cuatro diferencias

```python
    def test8(self):
        self.assertEqual(hamming_distance("GATACA", "GCATAA"), 4, "--err-t8--")
```

Desplazar una hebra una posición hace que casi todas las posiciones difieran

```python
    def test9(self):
        self.assertEqual(hamming_distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "--err-t9--")
```

Las dos hebras de la descripción tienen una distancia de siete

```python
    def test10(self):
        self.assertEqual(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def hamming_distance(left, right):
    distance = 0

    for left_nucleotide, right_nucleotide in zip(left, right):
        if left_nucleotide != right_nucleotide:
            distance += 1

    return distance
```
