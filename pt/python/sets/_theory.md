Um **conjunto** é uma coleção de elementos **únicos**: o mesmo valor pode aparecer apenas uma vez, não importa quantas vezes você o escreva.
Um conjunto também é **não ordenado**: não existe primeiro nem último elemento, então você não pode ler um elemento por índice.
Conjuntos são ideais quando você só se importa com *quais* valores estão presentes, não com quantas vezes ou em que posição.
Você cria um conjunto escrevendo seus elementos entre chaves `{...}`:
```python
colors = {"red", "blue", "red"}
print(len(colors))  # 2
```
A duplicata `"red"` é descartada, então `len()` conta apenas os elementos distintos.

---

A função embutida `set()` constrói um conjunto a partir de qualquer coleção, por exemplo uma lista ou uma string.
Como um conjunto mantém cada valor apenas uma vez, esta é a forma clássica de **remover duplicatas**:
```python
nums = [1, 2, 2, 3]
unique = set(nums)
print(len(unique))  # 3
```
Para verificar se um valor está presente, use o operador `in`, que retorna `True` ou `False`:
```python
print(2 in unique)  # True
print(9 in unique)  # False
```
Verificações de pertencimento em um conjunto são muito rápidas, mesmo com milhares de elementos.

---

Existe uma armadilha ao criar um **conjunto vazio**.
Chaves também são a sintaxe de dicionários, então `{}` cria um **dicionário** vazio, não um conjunto:
```python
empty = {}
print(type(empty))  # <class 'dict'>
```
Para obter um conjunto vazio, você deve chamar `set()` sem argumentos:
```python
empty = set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
```

---

Conjuntos são **mutáveis**: você pode adicionar e remover elementos depois de criá-los.
`add(value)` insere um valor; adicionar um que já está presente não muda nada:
```python
letters = {"a", "b"}
letters.add("c")
letters.add("a")
print(len(letters))  # 3
```
Existem duas formas de remover um elemento:
- `remove(value)` o exclui, mas gera um `KeyError` se o valor não estiver no conjunto
- `discard(value)` o exclui se estiver presente e **não faz nada** caso contrário, sem erro
```python
letters.remove("a")
letters.discard("z")  # "z" não está lá, mas nenhum erro
letters.remove("z")   # KeyError: 'z'
```

---

`pop()` remove **um elemento arbitrário** do conjunto e o retorna.
Como um conjunto não tem ordem, você não pode escolher qual elemento é removido; chamar `pop()` em um conjunto vazio gera um `KeyError`:
```python
tickets = {101, 102, 103}
picked = tickets.pop()
print(len(tickets))  # 2
```
`clear()` remove **todos** os elementos, deixando um conjunto vazio:
```python
tickets.clear()
print(len(tickets))  # 0
```

---

Você pode percorrer um conjunto com `for`, exatamente como uma lista:
```python
for color in {"red", "blue"}:
    print(color)
```
Como um conjunto não é ordenado, os elementos podem sair em **qualquer ordem**, e essa ordem pode até mudar entre execuções.
Quando você precisa de uma ordem previsível, passe o conjunto para `sorted()`, que retorna uma **lista** ordenada de seus elementos:
```python
for color in sorted({"red", "blue"}):
    print(color)  # blue, then red
```

---

A **união** de dois conjuntos é um novo conjunto com os elementos de **ambos**, sem duplicatas.
Use o operador `|` ou o método `union()`:
```python
a = {1, 2}
b = {2, 3}
print(a | b)        # {1, 2, 3}
print(a.union(b))   # {1, 2, 3}
```
Nem `a` nem `b` são modificados: operações de conjunto sempre retornam um novo conjunto.

---

A **interseção** de dois conjuntos contém apenas os elementos presentes em **ambos**.
Use o operador `&` ou o método `intersection()`:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)               # {2, 3}
print(a.intersection(b))   # {2, 3}
```
Se os conjuntos não têm nada em comum, o resultado é um conjunto vazio.

---

A **diferença** `a - b` contém os elementos de `a` que **não** estão em `b`.
A ordem importa: `a - b` e `b - a` costumam ser diferentes:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}
print(b - a)  # {4}
```
A **diferença simétrica** `a ^ b` contém os elementos que estão em **exatamente um** dos dois conjuntos:
```python
print(a ^ b)  # {1, 4}
```
As formas em método são `difference()` e `symmetric_difference()`.

---

Operadores e métodos não são perfeitamente equivalentes.
Os operadores `|`, `&`, `-` e `^` funcionam apenas quando **ambos** os operandos são conjuntos.
Os métodos `union()`, `intersection()`, `difference()` e `symmetric_difference()` aceitam **qualquer iterável**, como uma lista ou uma string:
```python
a = {1, 2}
print(a.union([2, 3]))  # {1, 2, 3}
print(a | [2, 3])       # TypeError: unsupported operand type(s) for |: 'set' and 'list'
```

---

Conjuntos também podem ser **comparados** entre si.
`a.issubset(b)`, ou `a <= b`, é `True` quando todo elemento de `a` também está em `b`.
`a.issuperset(b)`, ou `a >= b`, é `True` quando `a` contém todo elemento de `b`.
`a.isdisjoint(b)` é `True` quando os dois conjuntos não têm **nenhum** elemento em comum:
```python
small = {1, 2}
big = {1, 2, 3}
print(small <= big)              # True
print(big.issuperset(small))     # True
print(small.isdisjoint({8, 9}))  # True
```

---

Um conjunto só pode conter elementos **hasheáveis**, ou seja, valores que não podem mudar: números, strings, `True`/`False` e **tuplas**.
Tentar adicionar uma lista, um dicionário ou outro conjunto gera um `TypeError`:
```python
points = set()
points.add((1, 2))  # ok, a tuple
points.add([1, 2])  # TypeError: unhashable type: 'list'
```
Conjuntos de tuplas são úteis para acompanhar pares únicos, como coordenadas ou registros (name, age):
```python
visits = [(1, 2), (1, 2), (3, 4)]
print(len(set(visits)))  # 2
```

---

Um **frozenset** é um conjunto **imutável**: uma vez criado, você não pode adicionar ou remover elementos.
Crie-o com `frozenset()` a partir de qualquer coleção:
```python
days = frozenset(["sat", "sun"])
print("sat" in days)  # True
days.add("mon")       # AttributeError: 'frozenset' object has no attribute 'add'
```
Imprimir um frozenset mostra seu tipo ao redor dos elementos, como `frozenset({'sat', 'sun'})`.
Como não pode mudar, um frozenset é hasheável: ao contrário de um conjunto normal, ele pode ser elemento de outro conjunto ou chave de dicionário.
Todas as operações somente leitura (`in`, `len()`, `|`, `&`, `-`, `^`, comparações) funcionam normalmente.

---

Uma **compreensão de conjunto** constrói um conjunto em uma única expressão, com a mesma sintaxe de uma list comprehension, mas com chaves:
```python
nums = [1, 2, 2, 3]
squares = {n * n for n in nums}
print(squares)  # {1, 4, 9}
```
Um `if` opcional filtra os elementos, e duplicatas produzidas pela expressão são descartadas automaticamente:
```python
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

---

Operações de conjunto também podem modificar um conjunto **no lugar**, em vez de retornar um novo.
`update(iterable)` adiciona todos os elementos de qualquer coleção, como `add()`, mas para vários valores de uma vez:
```python
inventory = {"sword"}
inventory.update(["potion", "map"])
print(len(inventory))  # 3
```
Os operadores compostos também funcionam no lugar: `|=` adiciona os elementos de outro conjunto, `&=` mantém apenas os comuns, `-=` remove os elementos de outro conjunto:
```python
inventory -= {"map"}
print(sorted(inventory))  # ['potion', 'sword']
```

---

Dois conjuntos são **iguais** quando contêm os mesmos elementos, seja qual for a ordem em que foram escritos:
```python
print({1, 2, 3} == {3, 1, 2})  # True
```
Comparar o tamanho de uma coleção com o tamanho de seu conjunto é uma forma rápida de detectar duplicatas: se o conjunto for **menor**, algum valor apareceu mais de uma vez:
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)) < len(emails))  # True
```
O método de lista `count(value)` diz quantas vezes um valor aparece, o que ajuda a descobrir *quais* valores estão duplicados.
