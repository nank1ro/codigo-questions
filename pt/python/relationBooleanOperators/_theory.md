Vamos comecar com o operador relacional **igual** `==`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se duas expressoes sao iguais, por exemplo:
```python
>>> 2 == 2
True
>>> 2 == 3
False
```

---

Vamos continuar com o operador relacional **diferente** `!=`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se duas expressoes **NAO** sao iguais, por exemplo:
```python
>>> 2 != 2
False
>>> 2 != 3
True
```
Ele e exatamente o oposto do operador *igual*

---

Vamos continuar com o operador relacional **maior que** `>`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se uma expressao e maior que a outra, por exemplo:
```python
>>> 2 > 2
False
>>> 3 > 2
True
```

---

Vamos continuar com o operador relacional **menor que** `<`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se uma expressao e menor que a outra, por exemplo:
```python
>>> 2 < 2
False
>>> 2 < 3
True
```

---

Vamos continuar com o operador relacional **maior ou igual** `>=`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se uma expressao e maior ou igual a outra, por exemplo:
```python
>>> 2 >= 2
True
>>> 3 >= 2
True
>>> 3 >= 4
False
```

---

Vamos continuar com o operador relacional **menor ou igual** `<=`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se uma expressao e menor ou igual a outra, por exemplo:
```python
>>> 2 <= 2
True
>>> 3 <= 2
False
>>> 3 <= 4
True
```

---

Agora vamos ver os operadores **Booleanos**, comecando pelo primeiro chamado `and`.
Ele retorna o primeiro operando que e avaliado como *False* ou o ultimo se todos forem *True*.
```python
>>> 2 == 2 and 2 == 3
False
>>> 1 == 1 and 1 == 1.0
True
```

---

Vamos continuar com o operador booleano **or**.
Ele retorna o primeiro operando que e avaliado como *True* ou o ultimo se todos forem *False*.
```python
>>> 2 == 2 or 2 == 3
True
>>> 1 == 2 or 1 == 3
False
```

---

Vamos finalizar com o operador booleano **not**.
Ele retorna um booleano que e o inverso do estado logico de uma expressao.
```python
>>> not True
False
>>> not False
True
>>> not 2 == 2
False
```
