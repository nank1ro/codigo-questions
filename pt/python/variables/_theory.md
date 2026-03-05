Variáveis são contêineres para armazenar valores de dados.
Toda variável em Python é um objeto e, diferente de outras linguagens de programação, Python não possui um comando para declarar uma variável.
Para criar uma variável, precisamos dar a ela um **nome**, lembrando que ele não pode conter espaços.
Uma variável é criada no momento em que você atribui um valor a ela pela primeira vez.
Um exemplo de criação de variável chamada `x` é:
```python
x = 1
```
Dessa forma, atribuímos o valor `1` à variável chamada `x`.
Se imprimirmos a variável `x`, obtemos o número `1`:
```python
>>> print(x)
1
```

---

As variáveis são chamadas assim porque o valor que elas armazenam pode mudar.
Podemos atualizar `x` usando `=` e atribuindo um novo valor.
```python
>>> x = 1
>>> print(x)
1
>>> x = 2
>>> print(x)
2
```

---

Também podemos atribuir a variáveis os valores de outras variáveis. Aqui, podemos atribuir à variável `y` o valor de `x`
```python
>>> x = 5
>>> y = x
>>> print(y)
5
```

---

Quando atualizamos uma variável, ela esquece seu valor anterior. Aqui podemos exibir a variável `x` duas vezes e ver como seu valor é atualizado.
```python
>>> x = 5
>>> print(x)
5
>>> x = 10
>>> print(x)
10
```

---

Variáveis do tipo string podem ser declaradas usando aspas simples ou duplas:
```python
>>> x = "May"
>>> x = 'May'
```
Ambas são a mesma coisa.

---

Se quisermos um nome de variável com várias palavras, usamos **snake case**.
Isso significa usar `_` para conectar as palavras adicionais.
