Adicionar um número como `5`, dentro da função `range()` significa que ela irá percorrer o bloco de código 5 vezes, de `0` até `4`

---

Sabemos como repetir código usando um loop `while`.
Como este programa que repete instruções para exibir `hello`
```python
counter = 0

while counter < 5:
    print("hello")
    counter += 1
```
Mas podemos fazer o mesmo com loops `for`:
```python
for i in range(5):
    print("hello")
```

---

A variável chamada `i` é a variável contadora.
Podemos dar a ela o nome que quisermos.
Ela conta em qual repetição do loop estamos atualmente

---

Em um loop `for` podemos especificar quantas vezes queremos que nosso loop seja executado com a função `range()`
