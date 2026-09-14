---
language: python
exerciseType: 1
difficulty: 2
title: Busca binária
---

# --description--

A busca binária encontra um valor dentro de uma coleção **ordenada** dividindo o intervalo de busca pela metade repetidamente: olhe o elemento no meio e, se não for o que você procura, continue na metade esquerda quando o alvo for menor ou na metade direita quando o alvo for maior.

Como cada etapa descarta metade dos elementos restantes, a busca binária chega à resposta em poucas comparações, mesmo em coleções muito grandes, enquanto verificar os elementos um por um custaria tantos passos quanto o número de elementos.

# --instructions--

Escreva uma função `binary_search` que recebe uma lista de inteiros ordenada em ordem crescente e um inteiro alvo, e retorna o índice do alvo dentro da lista, ou `-1` quando o alvo não está presente.

A lista nunca contém duplicatas, então o índice é sempre único. A lista também pode estar vazia. Sua função deve usar busca binária, dividindo o intervalo de busca pela metade a cada passo, e não uma varredura linear.

Exemplo de chamada da função:
```python
print(binary_search([1, 3, 5, 7], 5))
# prints 2
```

# --seed--

```python
def binary_search(arr, target):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

A busca em uma lista vazia deve retornar -1

```python
    def test1(self):
        self.assertEqual(binary_search([], 7), -1, "--err-t1--")
```

A busca por 5 em `[5]` deve retornar 0

```python
    def test2(self):
        self.assertEqual(binary_search([5], 5), 0, "--err-t2--")
```

A busca por 9 em `[5]` deve retornar -1

```python
    def test3(self):
        self.assertEqual(binary_search([5], 9), -1, "--err-t3--")
```

O primeiro elemento -9 da lista de 12 elementos deve ser encontrado no índice 0

```python
    def test4(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, "--err-t4--")
```

O último elemento 78 da lista de 12 elementos deve ser encontrado no índice 11

```python
    def test5(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, "--err-t5--")
```

O elemento 15 deve ser encontrado no índice 6

```python
    def test6(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, "--err-t6--")
```

O elemento 22 deve ser encontrado no índice 7

```python
    def test7(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, "--err-t7--")
```

O valor 12, que está entre 11 e 15, deve retornar -1

```python
    def test8(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, "--err-t8--")
```

Um alvo menor que todos os elementos deve retornar -1

```python
    def test9(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, "--err-t9--")
```

Um alvo maior que todos os elementos deve retornar -1

```python
    def test10(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100), -1, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
