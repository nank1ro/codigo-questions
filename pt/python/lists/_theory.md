Listas são um tipo de dado que você pode usar para armazenar uma coleção de diferentes informações como uma sequência sob um único nome de variável.
Uma lista armazena múltiplos valores de qualquer tipo e usa **índices** para distinguir esses valores.
Você pode atribuir itens a uma lista com uma expressão da seguinte forma:
```python
list_name = [item1, item2]
```

---

Você pode acessar um item individual da lista pelo seu índice.
Um índice é como um endereço que identifica a posição do item na lista.
O índice aparece diretamente após o nome da lista, entre colchetes, assim:
```python
list_name[index]
```

Os índices de lista começam com `0`, **não** com `1`! Você acessa o primeiro item de uma lista assim: `list_name[0]`.
O segundo item de uma lista está no índice 1: `list_name[1]`.

---

Um índice de lista se comporta como qualquer outro nome de variável! Ele pode ser usado tanto para acessar quanto para atribuir valores.
Você viu como acessar um índice de lista assim:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] # Obtém o valor "Jeremiah"
```
É assim que uma atribuição funciona:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] = "Jordan"
names[0] # Obtém o novo valor "Jordan"
```

---

Assim como strings, listas tem um **comprimento**.
O comprimento de uma lista e o numero de itens que ela contem

---

Uma lista não precisa ter um comprimento fixo.
Você pode adicionar itens ao final de uma lista a qualquer momento!
Para adicionar um item a uma lista usamos a palavra-chave `append`:
```python
>>> letters = ["a", "b"]
>>> letters.append("c")
>>> print(letters)
['a', 'b', 'c']
```

---

Às vezes, você só quer acessar uma parte de uma lista.
Considere o seguinte código:
```python
>>> numbers = [1, 2, 3, 4]
>>> slice = numbers[1:3]
>>> print(slice)
[2, 3]
```
Primeiro, criamos uma lista chamada `numbers`.
Depois, pegamos uma subseção da lista e a armazenamos na lista slice.
Fazemos isso definindo os índices que queremos incluir após o nome da lista: `numbers[1:3]`.
Em Python, quando especificamos uma parte de uma lista dessa forma, incluímos o elemento com o primeiro índice, `1`, mas excluímos o elemento com o segundo índice, `3`.

---

Você pode fatiar uma string exatamente como uma lista! Na verdade, você pode pensar em strings como listas de caracteres: cada caractere é um item sequencial na lista, começando pelo índice `0`.
```python
list_name[:2]
# Pega os dois primeiros itens
list_name[3:]
# Pega do quarto item até o último
```
Se o seu fatiamento de lista incluir o primeiro ou o último item de uma lista (ou de uma string), o índice desse item não precisa ser incluído.

---

Os elementos de uma lista podem ser de qualquer tipo:
```python
list_name = ["one", 2, True]
```
Na verdade, acima temos, em ordem, uma string, um inteiro e um booleano.
Mas também podemos ter listas dentro de listas!

---

Às vezes você precisa procurar um item em uma lista.
Em Python podemos usar o método `index()`:
```python
>>> names = ["Trevor", "Zac", "Glenn"]
>>> print(names.index("Zac"))
1
```
O código acima imprime o primeiro índice que contém a string `"Zac"`, `1` neste caso.
Também podemos inserir itens em uma lista em um índice específico, usando o método `insert()`:
```python
>>> names.insert(1, "Ali")
>>> print(names)
['Trevor', 'Ali', 'Zac', 'Glenn']
```
O código acima insere `"Ali"` no índice `1`, o que move tudo, após esse índice, uma posição para baixo

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
Um nome de variável segue a palavra-chave `for`, ele receberá o valor de cada item da lista por vez.

---

**Tuplas** são como listas, mas são muito mais rápidas.
Porém, os valores de uma tupla não podem ser alterados.
Costumamos usar tuplas para dados **somente leitura** que permanecem constantes enquanto o programa está em execução.
Para criar uma tupla usamos os parênteses `()`

---

Pode haver momentos em que queremos converter nossa tupla em uma lista.
Para fazer isso, podemos usar a funcao `list()`

---

Da mesma forma, podemos converter uma lista em uma tupla
