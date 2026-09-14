---
language: python
exerciseType: 1
difficulty: 2
title: Ordenação por bolha
---

# --description--

A ordenação por bolha é um dos algoritmos de ordenação mais simples. Ela percorre uma lista e compara cada par de elementos adjacentes, trocando-os sempre que estão na ordem errada. Depois de cada passagem completa, o maior valor restante "borbulhou" até a sua posição final, e a lista está ordenada assim que uma passagem termina sem uma única troca.

# --instructions--

Escreva uma função chamada `bubble_sort` que receba uma lista de números inteiros e devolva uma **nova** lista com os mesmos valores ordenados em ordem crescente. A lista passada não deve ser modificada.

Você deve implementar o algoritmo de ordenação por bolha por conta própria, comparando e trocando elementos adjacentes. Não use uma função de ordenação da biblioteca padrão.

A sua função também deve funcionar com um array vazio, um array com um único elemento, um array já ordenado, valores repetidos e números negativos.

Exemplo de chamada de função:
```python
print(bubble_sort([3, 1, 2]))
# prints [1, 2, 3]
```

# --seed--

```python
def bubble_sort(arr):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Um array vazio deve devolver um array vazio

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

Um array com um único elemento deve permanecer igual

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

Um array já ordenado deve manter a mesma ordem

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

Um array ordenado ao contrário deve ser colocado em ordem crescente

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

Todos os valores repetidos devem ser mantidos

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

Os números negativos devem ser ordenados antes dos positivos

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

Um array misto mais longo deve ser ordenado em ordem crescente

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

O array passado não deve ser modificado

```python
    def test_8(self):
        original = [3, 1, 2]
        bubble_sort(original)
        self.assertEqual(original, [3, 1, 2], "--err-t8--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def bubble_sort(arr):
    result = list(arr)
    end = len(result)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, end):
            if result[i - 1] > result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]
                swapped = True
        end -= 1
    return result
```
