Uma tarefa muito comum é construir uma nova lista a partir de uma já existente.
Com um loop `for` e `append()`, isso leva algumas linhas:
```python
nums = [1, 2, 3]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6]
```
O Python oferece uma forma mais curta para exatamente essa tarefa: a **list comprehension**, que constrói a lista inteira em uma única expressão:
```python
doubled = [n * 2 for n in nums]
```
A sintaxe é `[expressão for item in iterável]`: a parte do `for` percorre os itens, e a expressão à esquerda é avaliada para cada um deles.
O resultado é uma lista totalmente nova, exatamente igual à construída com o loop.

---

A expressão à esquerda pode ser qualquer coisa que produza um valor: um cálculo, uma chamada de função, uma chamada de método.
A variável do loop pode ter qualquer nome que você quiser, e ela existe apenas dentro dos colchetes:
```python
prices = [10, 20]
with_tax = [price * 1.2 for price in prices]
print(with_tax)  # [12.0, 24.0]
```

---

Uma comprehension também pode **filtrar** os itens.
Adicione uma condição `if` depois da parte `for`: apenas os itens para os quais a condição é `True` acabam na nova lista:
```python
nums = [5, 12, 8, 20]
big = [n for n in nums if n > 10]
print(big)  # [12, 20]
```
Isso é o mesmo que um loop com um `if` dentro, e substitui o `filter()` com uma lambda de forma mais legível.

---

A condição de filtro pode ser qualquer expressão que resulte em um booleano, incluindo chamadas de função como `len()`:
```python
words = ["a", "bee", "cat"]
short = [w for w in words if len(w) < 3]
print(short)  # ['a']
```

---

O iterável não precisa ser uma lista: qualquer coisa sobre a qual você possa fazer um loop funciona, e o `range()` é um dos favoritos.
É a forma mais rápida de construir uma lista de números:
```python
squares = [n * n for n in range(4)]
print(squares)  # [0, 1, 4, 9]
```
Lembre-se de que `range(start, stop)` exclui `stop`.

---

Comprehensions são ótimas para **transformar strings**.
Chame um método de string em cada item, ou construa uma nova string com uma f-string:
```python
names = ["ana", "bob"]
greetings = [f"Hi {name.capitalize()}" for name in names]
print(greetings)  # ['Hi Ana', 'Hi Bob']
```

---

Dentro de uma comprehension você pode usar qualquer variável definida antes dela, por exemplo como o limite de um `range()`.

---

Às vezes você não quer descartar itens, mas escolher **um valor diferente** para alguns deles.
Use uma expressão condicional `a if condição else b` como a expressão, à esquerda do `for`:
```python
nums = [3, -1, 4]
signs = ["+" if n > 0 else "-" for n in nums]
print(signs)  # ['+', '-', '+']
```
Note a posição: o `if-else` vem **antes** do `for` e sempre produz um valor, enquanto o filtro `if` vem **depois** do `for` e não tem `else`.

---

As duas condições podem ser combinadas na mesma comprehension: um `if-else` para escolher o valor, e um filtro `if` no final para pular alguns itens.
```python
nums = [1, 2, 3, 4]
result = ["big" if n > 2 else "small" for n in nums if n != 3]
print(result)  # ['small', 'small', 'big']
```

---

As duas posições do `if` são fáceis de confundir, então mantenha-as separadas:
```python
values = [n if n > 0 else 0 for n in nums]  # if-else antes do for: escolhe um valor, else obrigatório
positives = [n for n in nums if n > 0]      # if depois do for: filtra, else não permitido
```
Colocar um `else` depois do filtro `if` é um erro de sintaxe.

---

Uma comprehension pode ter **mais de um `for`**.
Eles funcionam como loops aninhados: o primeiro `for` é o loop externo, o segundo é o interno.
```python
pairs = [a + b for a in ["x", "y"] for b in ["1", "2"]]
print(pairs)  # ['x1', 'x2', 'y1', 'y2']
```

---

O `for` interno pode usar a variável do externo.
Esta é a forma clássica de **achatar** uma lista de listas em uma única lista:
```python
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```
A função `sum()` então soma todos os números de uma lista.

---

Você também pode fazer um loop sobre um **dicionário**.
Com `.items()`, a parte do `for` desempacota cada par em duas variáveis, uma chave e um valor:
```python
ages = {"ana": 31, "bob": 25}
lines = [f"{name} is {age}" for name, age in ages.items()]
print(lines)  # ['ana is 31', 'bob is 25']
```

---

A mesma ideia funciona para dicionários: uma **dict comprehension** usa chaves e uma expressão `key: value`:
```python
names = ["ana", "bob"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'ana': 3, 'bob': 3}
```

---

Chaves **sem** a parte `key: value` geram uma **set comprehension**.
Um set é uma coleção não ordenada que mantém apenas valores únicos, então as duplicatas desaparecem automaticamente:
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)  # {1, 2, 3}
```

---

**Quando você deve usar uma comprehension?**
É perfeita quando o resultado é uma lista (ou dict, ou set) e a lógica cabe em uma única linha legível: uma transformação simples, um filtro opcional.
Se você precisar de várias instruções, mais de dois `for` aninhados, ou a linha ficar difícil de ler, escreva um loop `for` normal em vez disso: o código será mais longo, mas mais claro.
Uma comprehension também substitui a maioria dos usos de `map()` e `filter()` com lambdas:
```python
doubled = list(map(lambda n: n * 2, nums))
doubled = [n * 2 for n in nums]  # same result, easier to read
```
