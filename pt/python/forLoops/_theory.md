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

Em um loop `for` podemos especificar quantas vezes queremos que nosso loop seja executado com a função `range()`

---

Adicionar um número como `5` dentro da função `range()` significa que ela irá iterar sobre o bloco de código 5 vezes, de `0` até `4`

---

A variável chamada `i` é a variável contadora.
Podemos dar a ela o nome que quisermos.
Ela conta em qual repetição do loop estamos atualmente

---

A função `range()` retorna uma sequência de números, começando em 0 por padrão, incrementando de 1 em 1 (por padrão), e parando antes de um número especificado.
Esta é a sintaxe da função:
```python
range(start, stop, step)
```
`start` e `step` são opcionais, enquanto `stop` é obrigatório
