As listas sao um tipo de dado que voce pode usar para armazenar uma colecao de diferentes informacoes como uma sequencia sob um unico nome de variavel.
Uma lista armazena varios valores de qualquer tipo e usa **indices** para distinguir esses valores.
Voce pode atribuir itens a uma lista com uma expressao do seguinte formato:
```python
list_name = [item1, item2]
```

---

Voce pode acessar um item individual da lista pelo seu indice.
Um indice e como um endereco que identifica o lugar do item na lista.
O indice aparece diretamente apos o nome da lista, entre colchetes, assim:
```python
list_name[index]
```

Os indices da lista comecam com `0`, **nao** com `1`! Voce acessa o primeiro item de uma lista assim: `list_name[0]`.
O segundo item de uma lista esta no indice 1: `list_name[1]`.

---

Uma lista nao precisa ter um tamanho fixo.
Voce pode adicionar itens ao final de uma lista quando quiser!
Para adicionar um item a uma lista usamos a palavra-chave `append`:
```python
>>> letters = ["a", "b"]
>>> letters.append("c")
>>> print(letters)
['a', 'b', 'c']
```

---

Assim como strings, listas tem um **tamanho** (length).
O tamanho de uma lista e o numero de itens que ela contem

---

Um indice de lista se comporta como qualquer outro nome de variavel! Ele pode ser usado tanto para acessar quanto para atribuir valores.
Voce viu como acessar um indice de lista assim:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] # Obtem o valor "Jeremiah"
```
Assim funciona uma atribuicao:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] = "Jordan"
names[0] # Obtem o novo valor "Jordan"
```

---

As vezes, voce quer acessar apenas uma parte de uma lista.
Considere o seguinte codigo:
```python
>>> numbers = [1, 2, 3, 4]
>>> slice = numbers[1:3]
>>> print(slice)
[2, 3]
```
Primeiro, criamos uma lista chamada `numbers`.
Entao, pegamos uma subsecao da lista e a armazenamos na lista slice.
Fazemos isso definindo os indices que queremos incluir apos o nome da lista: `numbers[1:3]`.
Em Python, quando especificamos uma parte de uma lista desta maneira, incluímos o elemento com o primeiro indice, `1`, mas excluímos o elemento com o segundo indice, `3`.

---

As vezes voce precisa procurar um item em uma lista.
Em Python podemos usar o metodo `index()`:
```python
>>> names = ["Trevor", "Zac", "Glenn"]
>>> print(names.index("Zac"))
1
```
O codigo acima imprime o primeiro indice que contem a string `"Zac"`, `1` neste caso.
Tambem podemos inserir itens em uma lista em um indice especifico, usando o metodo `insert()`:
```python
>>> names.insert(1, "Ali")
>>> print(names)
['Trevor', 'Ali', 'Zac', 'Glenn']
```
O codigo acima insere `"Ali"` no indice `1`, que move tudo, apos este indice, para baixo em 1

---

Os elementos da lista podem ser de qualquer tipo:
```python
list_name = ["one", 2, True]
```
Na verdade, acima temos, em ordem, uma string, um inteiro e um booleano.
Mas tambem podemos ter listas com listas!

---

Voce pode fatiar uma string exatamente como uma lista! De fato, voce pode pensar em strings como listas de caracteres: cada caractere e um item sequencial na lista, comecando do indice `0`.
```python
list_name[:2]
# Pega os primeiros dois itens
list_name[3:]
# Pega do quarto ao ultimo item
```
Se o seu fatiamento de lista incluir o primeiro ou ultimo item de uma lista (ou uma string), o indice desse item nao precisa ser incluido.

---

In Python we can loop through a list in a very simple way using the `for..in` keywords:
```python
>>> numbers = [1, 2, 3]
>>> for num in numbers:
>>>     print(num)
1
2
3
```
A variable name follows the `for` keyword, it will be assigned the value of each list item in turn.

---

**Tuplas** sao como listas mas sao muito mais rapidas.
No entanto, os valores das tuplas nao podem ser alterados.
Tendemos a usar tuplas para dados **apenas de leitura** que permanecem constantes enquanto o programa esta em execucao.
Para criar uma tupla usamos os parenteses `()`

---

Da mesma forma, podemos converter uma lista em uma tupla
