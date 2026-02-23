A tomada de decisao e necessaria quando queremos executar codigo somente se uma determinada condicao for satisfeita.
Vamos supor que queremos brincar fora somente se o clima estiver bom.
Na programacao, podemos salvar uma variavel booleana `nice_weather` e realizar a acao de brincar fora `if` esta variavel for `True`, como:
```python
nice_weather = True
if (nice_weather):
    # play outside
```

---

Vamos continuar com o exemplo anterior.
```python
nice_weather = True
if (nice_weather):
    # play outside
```
Vimos que a instrucao `if` executa o bloco de codigo somente se a condicao for `True`.
Outra coisa importante a considerar e representada pelos **dois pontos** `:` e pelo **recuo**, que indicam o inicio de um bloco de codigo.
O recuo refere-se aos espacos no inicio de uma linha de codigo.
Onde em outras linguagens de programacao o recuo no codigo e apenas para legibilidade, o recuo em Python e essencial.
Voce pode usar seu numero favorito de espacos (2, 4, 6, 8), observando que o preferido e 4.
Aqui no app, sugerimos usar a tecla **TAB** para recuar suas linhas de codigo

---

Acabamos de ver como executar um bloco de codigo se uma condicao ocorre, agora vamos ver como executar outro bloco de codigo se a primeira condicao falhar.
Vamos brincar fora se o clima estiver bom; caso contrario, ficamos em casa.
Em Python podemos usar a instrucao `else`, como:
```python
nice_weather = True
if (nice_weather):
    # play outside
else:
    # stay home
```

---

Vamos supor que temos outra condicao para verificar, como neste exemplo:
```python
num = 3
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
else:
    print("do something else")
```
e a saida deste codigo e `the number is 3`.
Primeiro, vamos verificar se o numero e igual a 2, isto e falso.
Entao vamos passar para a segunda instrucao e verificar se `num` e igual a 3, sendo verdadeiro executamos o seguinte bloco de codigo imprimindo `the number is 3`

---

Podemos adicionar quantas instrucoes `elif` quisermos, nao ha limites
```python
num = 4
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
elif (num == 4):
    print("the number is 4")
elif (num == 5):
    print("the number is 5")
elif (num == 6):
    print("the number is 6")
```
e a saida deste codigo e `the number is 4`.

---

Tambem podemos aninhar uma instrucao condicional (`if`, `elif` ou `else`) dentro de outra instrucao condicional, para criar uma estrutura mais complexa.
```python
num = 4
if (num < 3):
    print("the number is lower than 3")
else:
    if (num == 3):
        print("the number is 3")
    elif (num == 4):
        print("the number is 4")
    else:
        print("the number is greather than 4")
```
e a saida deste codigo e `the number is 4`.
