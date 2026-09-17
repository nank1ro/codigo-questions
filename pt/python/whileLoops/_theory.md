Frequentemente na programação, precisamos repetir um bloco de código, por exemplo:
```python
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
Isso produz a seguinte saída:
```python
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviamente, para instruções longas gastaríamos muito tempo escrevendo o código, mas felizmente, podemos usar laços de repetição.
Vamos aprender o laço `while`, obtendo a mesma saída acima.
```python
count = 2
while (count <= 5):
    print(f"{count} seconds")
    count += 1
```
Então criamos uma variável `count` atribuindo `2`, o valor inicial.
Depois usamos a instrução `while` que executará o bloco de código enquanto a condição `count <= 5` for `True`.
Dentro do bloco de código, **NÃO** devemos esquecer de adicionar a linha `count += 1`.
Ela incrementa o valor de `count`, caso contrário, nosso laço será infinito

---

Para controlar quantas vezes um laço `while` se repete, começamos com uma variável definida como um número.
Chamamos essa variável de variável contadora

---

Depois, usamos uma comparacao na condicao para comparar a variavel `counter` com um numero.

---

Dentro do bloco de codigo, para parar o laco `while`, incrementamos a variavel `counter`.

---

A ordem em que voce escreve o codigo afeta a saida.
