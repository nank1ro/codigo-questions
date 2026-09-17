Vamos começar com o operador relacional **igual** `==`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se duas expressões são iguais, por exemplo:
```python
>>> 2 == 2
True
>>> 2 == 3
False
```

---

Vamos continuar com o operador relacional **diferente** `!=`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se duas expressões **NÃO** são iguais, por exemplo:
```python
>>> 2 != 2
False
>>> 2 != 3
True
```
Ele é exatamente o oposto do operador *igual*

---

Vamos continuar com o operador relacional **maior que** `>`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se uma expressão é maior que a outra, por exemplo:
```python
>>> 2 > 2
False
>>> 3 > 2
True
```

---

Vamos continuar com o operador relacional **menor que** `<`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se uma expressão é menor que a outra, por exemplo:
```python
>>> 2 < 2
False
>>> 2 < 3
True
```

---

Vamos continuar com o operador relacional **maior ou igual** `>=`.
Ele retorna um **Booleano** (`True` ou `False`) indicando se uma expressão é maior ou igual a outra, por exemplo:
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
Ele retorna um **Booleano** (`True` ou `False`) indicando se uma expressão é menor ou igual a outra, por exemplo:
```python
>>> 2 <= 2
True
>>> 3 <= 2
False
>>> 3 <= 4
True
```

---

Agora vamos ver os operadores **Booleanos**, começando pelo primeiro chamado `and`.
Ele retorna o primeiro operando que é avaliado como *False* ou o último se todos forem *True*.
```python
>>> 2 == 2 and 2 == 3
False
>>> 1 == 1 and 1 == 1.0
True
```

---

Vamos continuar com o operador booleano **or**.
Ele retorna o primeiro operando que é avaliado como *True* ou o último se todos forem *False*.
```python
>>> 2 == 2 or 2 == 3
True
>>> 1 == 2 or 1 == 3
False
```

---

Vamos finalizar com o operador booleano **not**.
Ele retorna um booleano que é o inverso do estado lógico de uma expressão.
```python
>>> not True
False
>>> not False
True
>>> not 2 == 2
False
```
