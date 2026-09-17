A tomada de decisão é necessária quando queremos executar um código apenas se uma determinada condição for satisfeita.
Vamos supor que queremos brincar lá fora apenas se o tempo estiver bom.
Em programação, podemos salvar uma variável booleana `nice_weather` e executar a ação de brincar lá fora `if` (se) essa variável for `True`, assim:
```python
nice_weather = True
if (nice_weather):
    # brincar lá fora
```

---

Vamos continuar com o exemplo anterior.
```python
nice_weather = True
if (nice_weather):
    # brincar lá fora
```
Vimos que a instrução `if` executa o bloco de código apenas se a condição for `True`.
Outra coisa importante a considerar é representada pelos **dois pontos** `:` e pela **indentação**, que indicam o início de um bloco de código.
Indentação refere-se aos espaços no início de uma linha de código.
Enquanto em outras linguagens de programação a indentação no código serve apenas para legibilidade, a indentação em Python é essencial.
Você pode usar seu número favorito de espaços (2, 4, 6, 8), sendo que o preferido é 4.
Aqui no app, sugerimos usar a tecla **TAB** para indentar suas linhas de código

---

Acabamos de ver como executar um bloco de código se uma condição ocorrer, agora vamos ver como executar outro bloco de código se a primeira condição falhar.
Vamos brincar lá fora se o tempo estiver bom; caso contrário, ficamos em casa.
Em Python podemos usar a instrução `else`, assim:
```python
nice_weather = True
if (nice_weather):
    # brincar lá fora
else:
    # ficar em casa
```

---

Vamos supor que temos outra condição para verificar, como neste exemplo:
```python
num = 3
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
else:
    print("do something else")
```
e a saída deste código é `the number is 3`.
Primeiro, vamos verificar se o número é igual a 2, isso é falso.
Então vamos passar para a segunda instrução e verificar se `num` é igual a 3, sendo verdadeiro executamos o bloco de código seguinte imprimindo `the number is 3`

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

Também podemos aninhar uma instrução condicional (`if`, `elif` ou `else`) dentro de outra instrução condicional, para criar uma estrutura mais complexa.
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
e a saída deste código é `the number is 4`.

---

Toda instrução condicional precisa da palavra-chave `if` para introduzi-la. É ela que avisa o Python que o bloco abaixo só é executado quando uma condição é verdadeira.

---

Uma condição não precisa ser uma comparação — um valor booleano como `True` sozinho também funciona, e o bloco é executado sempre que esse valor for `True`.

---

A mesma instrução pode ser feita para pular seu bloco só mudando a condição: sempre que ela resultar em `False`, o Python pula direto o código indentado.

---

Uma linha `if` em Python é formada por três partes: a palavra-chave `if`, uma condição e os dois-pontos que fecham a linha. Tudo o que estiver indentado depois desses dois-pontos é o bloco.

---

Como a condição aqui é `True`, o Python executa a linha indentada abaixo dela e imprime `Hello!`.

---

Uma condição `False` significa que o Python nunca entra no bloco indentado, então nada é impresso.

---

O valor que decide se um bloco é executado é chamado de condição, e ele sempre precisa resultar em um booleano, `True` ou `False`.

---

O bloco abaixo de um `if` nunca pode estar vazio: o Python levanta um `IndentationError` quando nenhuma linha indentada vem depois dos dois-pontos. `pass` é o placeholder mais usado quando ainda não há nada para executar.

---

Os dois-pontos pertencem a linha do `if`, não ao bloco: eles marcam o fim da condição e avisam que as linhas indentadas abaixo fazem parte da instrução.

---

Quando uma condição é `False`, o Python pula todo o bloco indentado e continua na próxima linha que não está indentada sob o `if`.

---

O Python não exige parênteses ao redor de uma condição — `if True:` já é uma instrução completa por si só. Os parênteses aqui são um agrupamento comum, do mesmo tipo usado na aritmética, e não alteram o valor.

---

Um bloco de código pode conter mais de uma linha, e as linhas são executadas na ordem em que foram escritas — uma instrução adicionada acima de outra já existente é impressa primeiro.

---

Uma variável booleana pode ser usada como condição sozinha — não é preciso compará-la com `True` ou `False` antes.

---

Quando a condição é uma variável, o `if` lê o que quer que essa variável guarde naquele momento. Mudar a atribuição acima já é suficiente para desligar o bloco, sem tocar na linha do `if`.

---

As linhas indentadas que pertencem a uma instrução condicional são chamadas de bloco de código — é a indentação que marca que elas fazem parte dele.

---

Uma linha que fica fora da indentação do `if` é executada não importa qual era a condição, já que ela nunca fez parte daquele bloco.

---

Um bloco de código não se limita a uma linha — ele pode ser tão curto ou tão longo quanto a lógica precisar, desde que todas as linhas mantenham a mesma indentação.

---

Com `online` definido como `False`, a condição nunca é verdadeira, então o bloco é pulado e nada é impresso.

---

Apenas o `print` indentado logo depois do `if` pertence ao seu bloco; uma linha escrita com a mesma indentação do próprio `if` não pertence.

---

Uma linha colocada depois do bloco do `if`, mas sem nenhuma indentação extra, não faz mais parte dele — ela é executada sempre, seja qual for a condição.

---

Um bloco pode conter qualquer número de instruções. Elas são executadas de cima para baixo, e cada uma precisa estar indentada no mesmo nível que as outras.

---

Atribuir `True` a variável faz com que a condição que depende dela seja verdadeira, então o bloco abaixo é executado.

---

Atribuir `False`, por outro lado, faz a condição falhar, então o bloco abaixo é completamente pulado.

---

A palavra-chave `if` é o que inicia uma instrução condicional — junto com sua condição, ela decide se o bloco abaixo é executado.

---

`"False"` entre aspas é uma string, não um booleano, e uma string não vazia sempre conta como verdadeira. Somente o `False` puro impede que um bloco seja executado.
```python
print(bool("False"))  # True
```

---

Escolher `True` aqui executa as duas linhas do bloco, não só a primeira — tudo o que está indentado sob o `if` pertence ao mesmo bloco.

---

Os dois-pontos são a única parte de uma linha `if` que não pode faltar: eles fecham a condição e abrem o bloco. Os parênteses ao redor da condição são opcionais em Python, então `if True:` e `if (True):` se comportam de forma idêntica.

---

Instruções como `if`, `elif` e `else`, que executam ou pulam código com base em um valor booleano, são conhecidas coletivamente como instruções condicionais.

---

O operador `not` inverte um valor booleano: `not True` é `False`, e `not False` é `True`.
```python
is_online = False
print(not is_online)  # True
```

---

O `not` cria um novo booleano em vez de modificar o que ele lê, então depois de `is_afternoon = not is_morning` a variável `is_morning` continua com seu valor original.

---

Uma condição sempre fica entre a palavra-chave `if` e os dois-pontos que a seguem, em nenhum outro lugar da linha.

---

Não há um limite rígido para quantas linhas um bloco `if` pode conter — o que importa é que todas as linhas fiquem indentadas no mesmo nível.

---

Um literal booleano funciona perfeitamente bem como condição: `if True:` executa seu bloco sempre. Escrevê-lo como `if (True):` é exatamente a mesma instrução, já que os parênteses ao redor de uma condição são opcionais em Python.

---

O bloco de código de uma instrução `if` é o conjunto de linhas indentadas abaixo dela, separado do resto do programa por essa indentação.

---

Uma condição sempre se reduz a um de dois valores, `True` ou `False` — é isso que faz dela um booleano.
