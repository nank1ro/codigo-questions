Para controlar as vezes que um loop `while` se repete, começamos com uma variável definida como um número.
Chamamos essa variável de variável contadora

---

Muitas vezes na programação, precisamos repetir um bloco de código, por exemplo:
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
Obviamente, para declarações longas gastaríamos muito tempo escrevendo o código, mas felizmente podemos usar loops.
Vamos aprender o loop `while`, obtendo a mesma saída acima.
```python
count = 2
while (count <= 5):
    print(f"{count} seconds")
    count += 1
```
Então criamos uma variável `count` atribuindo `2`, o valor inicial.
Então usamos a declaração `while` que executará o bloco de código até que a condição `count <= 5` seja `True`.
Dentro do bloco de código, **NÃO** devemos esquecer de adicionar a linha `count += 1`.
Ela incrementa o valor de `count`, caso contrário, nosso loop será infinito

---

Então, usamos uma comparação na condição para comparar a variável `counter` com um número.
