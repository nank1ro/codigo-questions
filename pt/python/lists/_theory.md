Listas sao um tipo de dado que voce pode usar para armazenar uma colecao de diferentes informacoes como uma sequencia sob um unico nome de variavel.
Uma lista armazena multiplos valores de qualquer tipo e usa **indices** para distinguir esses valores.
Voce pode atribuir itens a uma lista com uma expressao da seguinte forma:
```python
list_name = [item1, item2]
```

---

Voce pode acessar um item individual da lista pelo seu indice.
Um indice e como um endereco que identifica a posicao do item na lista.
O indice aparece diretamente apos o nome da lista, entre colchetes, assim:
```python
list_name[index]
```

Os indices de lista comecam com `0`, **nao** com `1`! Voce acessa o primeiro item de uma lista assim: `list_name[0]`.
O segundo item de uma lista esta no indice 1: `list_name[1]`.

---

Um indice de lista se comporta como qualquer outro nome de variavel! Ele pode ser usado tanto para acessar quanto para atribuir valores.
Voce viu como acessar um indice de lista assim:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] # Obtem o valor "Jeremiah"
```
E assim que uma atribuicao funciona:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] = "Jordan"
names[0] # Obtem o novo valor "Jordan"
```

---

Assim como strings, listas tem um **comprimento**.
O comprimento de uma lista e o numero de itens que ela contem

---

Uma lista nao precisa ter um comprimento fixo.
Voce pode adicionar itens ao final de uma lista a qualquer momento!
Para adicionar um item a uma lista usamos a palavra-chave `append`:
```python
>>> letters = ["a", "b"]
>>> letters.append("c")
>>> print(letters)
['a', 'b', 'c']
```

---

As vezes, voce so quer acessar uma parte de uma lista.
Considere o seguinte codigo:
```python
>>> numbers = [1, 2, 3, 4]
>>> slice = numbers[1:3]
>>> print(slice)
[2, 3]
```
Primeiro, criamos uma lista chamada `numbers`.
Depois, pegamos uma subsecao da lista e a armazenamos na lista slice.
Fazemos isso definindo os indices que queremos incluir apos o nome da lista: `numbers[1:3]`.
Em Python, quando especificamos uma parte de uma lista dessa forma, incluimos o elemento com o primeiro indice, `1`, mas excluimos o elemento com o segundo indice, `3`.

---

Voce pode fatiar uma string exatamente como uma lista! Na verdade, voce pode pensar em strings como listas de caracteres: cada caractere e um item sequencial na lista, comecando pelo indice `0`.
```python
list_name[:2]
# Pega os dois primeiros itens
list_name[3:]
# Pega do quarto item ate o ultimo
```
Se o seu fatiamento de lista incluir o primeiro ou o ultimo item de uma lista (ou de uma string), o indice desse item nao precisa ser incluido.

---

Os elementos de uma lista podem ser de qualquer tipo:
```python
list_name = ["one", 2, True]
```
Na verdade, acima temos, em ordem, uma string, um inteiro e um booleano.
Mas tambem podemos ter listas dentro de listas!

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
O codigo acima insere `"Ali"` no indice `1`, o que move tudo, apos esse indice, uma posicao para baixo

---

Em Python podemos percorrer uma lista de forma muito simples usando as palavras-chave `for..in`:
```python
>>> numbers = [1, 2, 3]
>>> for num in numbers:
>>>     print(num)
1
2
3
```
Um nome de variavel segue a palavra-chave `for`, ele recebera o valor de cada item da lista por vez.

---

**Tuplas** sao como listas, mas sao muito mais rapidas.
Porem, os valores de uma tupla nao podem ser alterados.
Costumamos usar tuplas para dados **somente leitura** que permanecem constantes enquanto o programa esta em execucao.
Para criar uma tupla usamos os parenteses `()`

---

Pode haver momentos em que queremos converter nossa tupla em uma lista.
Para fazer isso, podemos usar a funcao `list()`

---

Da mesma forma, podemos converter uma lista em uma tupla
