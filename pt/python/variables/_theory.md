Variaveis sao conteineres para armazenar valores de dados.
Cada variavel em Python e um objeto e, ao contrario de outras linguagens de programacao, Python nao tem comando para declarar uma variavel.
Para criar uma variavel, precisamos dar a ela um **nome** mantendo em mente que ela nao deve conter espacos.
Uma variavel e criada no momento em que voce atribui um valor a ela pela primeira vez.
Um exemplo de criacao de uma variavel chamada `x` e:
```python
x = 1
```
Desta forma, atribuimos o valor `1` a variavel chamada `x`.
Se imprimirmos a variavel `x`, recebemos de volta o numero `1`:
```python
>>> print(x)
1
```

---

Variaveis sao chamadas assim porque o valor que elas armazenam pode mudar.
Podemos atualizar `x` usando `=` e dando a ela um novo valor.
```python
>>> x = 1
>>> print(x)
1
>>> x = 2
>>> print(x)
2
```

---

Tambem podemos dar as variaveis os valores de outras variaveis. Aqui, podemos dar a variavel `y` o valor de `x`
```python
>>> x = 5
>>> y = x
>>> print(y)
5
```

---

Quando atualizamos uma variavel, ela esquece seu valor anterior. Aqui podemos exibir a variavel `x` duas vezes e ver como seu valor atualiza.
```python
>>> x = 5
>>> print(x)
5
>>> x = 10
>>> print(x)
10
```

---

Variaveis de string podem ser declaradas usando aspas simples ou aspas duplas:
```python
>>> x = "May"
>>> x = 'May'
```
Ambos sao a mesma coisa.

---

Se quisermos um nome de variavel com varias palavras, usamos **snake case**.
Isso significa usar `_` para conectar as palavras adicionais.
