---
language: python
exerciseType: 1
title: 100 doors
difficulty: 1
---
# --description--
Existem 100 portas em uma fila que estão todas inicialmente fechadas.
Você faz 100 passagens pelas portas.
Na primeira vez, visite cada porta e 'alterne' a porta (se a porta estiver fechada, abra-a; se estiver aberta, feche-a).
Na segunda vez, visite apenas cada 2ª porta (ou seja, porta #2, #4, #6, ...) e alterne-a.
Na terceira vez, visite cada 3ª porta (ou seja, porta #3, #6, #9, ...), etc., até que você visite apenas a 100ª porta.
# --instructions--
Implemente uma função para determinar o estado das portas após a última passagem.
Retorne o resultado final em um vetor, com apenas o número da porta incluído no vetor se ela estiver aberta.
> O método deve ser capaz de trabalhar com um número variável de portas.
# --seed--
```python
def get_final_opened_doors(num_doors):
    pass
```


# --before-asserts--
```python
import unittest
class CodigoTests(unittest.TestCase):
```



# --asserts--
Dado 100 portas, retorne a lista correta de portas abertas
```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_final_opened_doors(100), solution, "--err-t1--")
```
Dado 10 portas, retorne a lista correta de portas abertas
```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(get_final_opened_doors(10), solution, "--err-t2--")
```
Dado 950 portas, retorne a lista correta de portas abertas
```python
    def test_3(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        self.assertEqual(get_final_opened_doors(950), solution, "--err-t3--")
```







# --after-asserts--
```python
if __name__ == "__main__":
    unittest.main()
```


# --solutions--
```python
def get_final_opened_doors(num_doors):
    open_doors = []
    i = 1;
    while (i**2) <= num_doors:
        open_doors.append(i**2)
        i += 1
    return open_doors
```

