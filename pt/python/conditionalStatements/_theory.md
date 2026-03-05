A tomada de decisao e necessaria quando queremos executar um codigo apenas se uma determinada condicao for satisfeita.
Vamos supor que queremos brincar la fora apenas se o tempo estiver bom.
Em programacao, podemos salvar uma variavel booleana `nice_weather` e executar a acao de brincar la fora `if` (se) essa variavel for `True`, assim:
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
Vimos que a instrucao `if` executa o bloco de codigo apenas se a condicao for `True`.
Outra coisa importante a considerar e representada pelos **dois pontos** `:` e pela **indentacao**, que indicam o inicio de um bloco de codigo.
Indentacao refere-se aos espacos no inicio de uma linha de codigo.
Enquanto em outras linguagens de programacao a indentacao no codigo serve apenas para legibilidade, a indentacao em Python e essencial.
Voce pode usar seu numero favorito de espacos (2, 4, 6, 8), sendo que o preferido e 4.
Aqui no app, sugerimos usar a tecla **TAB** para indentar suas linhas de codigo

---

Acabamos de ver como executar um bloco de codigo se uma condicao ocorrer, agora vamos ver como executar outro bloco de codigo se a primeira condicao falhar.
Vamos brincar la fora se o tempo estiver bom; caso contrario, ficamos em casa.
Em Python podemos usar a instrucao `else`, assim:
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
Primeiro, vamos verificar se o numero e igual a 2, isso e falso.
Entao vamos passar para a segunda instrucao e verificar se `num` e igual a 3, sendo verdadeiro executamos o bloco de codigo seguinte imprimindo `the number is 3`

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
