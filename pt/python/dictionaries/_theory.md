**Dicionários** são semelhantes a listas e tuplas, mas você acessa os valores procurando por uma *chave* em vez de um índice.
Uma chave pode ser qualquer string ou número.
Dicionários são delimitados por chaves, assim:
```python
d = {"key1": 1, "key2": 2, "key3": 3}
```
Este é um dicionário chamado `d` com três *pares chave-valor*.
A chave `key1` aponta para o valor `1`, `key2` para `2`, e assim por diante.

---

Acessar valores de um dicionario por chave e igual a acessar valores de uma lista por indice:
```python
user['age']
# obtem o valor de age do dicionario user
```

---

Assim como listas, dicionários são _mutáveis_.
Isso significa que eles podem ser alterados após serem criados.
Uma vantagem disso é que podemos adicionar novos _pares chave/valor_ ao dicionário após ele ser criado, assim:
```python
dict_name[new_key_name] = new_value
```

---

O comprimento `len()` de um dicionário é o número de _pares chave-valor_ que ele possui.
Cada par conta apenas uma vez, mesmo que o valor seja uma lista. (Isso mesmo: você também pode colocar listas dentro de dicionários!)

---

Como dicionários são mutáveis, eles podem ser alterados de várias maneiras. Itens podem ser removidos de um dicionário com o comando `del`:
```python
del dict_name[key_name]
```
irá remover a chave `key_name` e seu valor associado do dicionário.

---

E se quisermos listar todas as chaves do dicionario?
Bem, existe o metodo `keys()`.

---

E se quisermos listar todos os valores do dicionario?
Bem, existe o metodo `values()`.

---

Assim como nas listas, podemos percorrer os elementos de um dicionário usando as palavras-chave `for..in`
Para obter tanto a chave quanto o valor no loop, podemos usar o método `items()`:
```python
for key, value in dict_name:
    print(key, value)
```

---

Também podemos usar a palavra-chave `in` que usamos com loops para verificar se um dicionário contém uma determinada __chave__

---

Para __adicionar__ ou __alterar__ valores em um dicionário, também podemos usar o método `update()` com os _pares chave-valor_ que queremos adicionar entre chaves

---

E se quisermos __remover__ um valor de um dicionario?
Existe o metodo `pop()`:
```python
dict_name.pop("key_name")
```
