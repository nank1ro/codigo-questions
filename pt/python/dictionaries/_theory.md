**Dicionarios** sao semelhantes a listas e tuplas, mas voce acessa os valores procurando por uma *chave* em vez de um indice.
Uma chave pode ser qualquer string ou numero.
Dicionarios sao delimitados por chaves, assim:
```python
d = {"key1": 1, "key2": 2, "key3": 3}
```
Este e um dicionario chamado `d` com tres *pares chave-valor*.
A chave `key1` aponta para o valor `1`, `key2` para `2`, e assim por diante.

---

Acessar valores de um dicionario por chave e igual a acessar valores de uma lista por indice:
```python
user['age']
# obtem o valor de age do dicionario user
```

---

Assim como listas, dicionarios sao _mutaveis_.
Isso significa que eles podem ser alterados apos serem criados.
Uma vantagem disso e que podemos adicionar novos _pares chave/valor_ ao dicionario apos ele ser criado, assim:
```python
dict_name[new_key_name] = new_value
```

---

O comprimento `len()` de um dicionario e o numero de _pares chave-valor_ que ele possui.
Cada par conta apenas uma vez, mesmo que o valor seja uma lista. (Isso mesmo: voce tambem pode colocar listas dentro de dicionarios!)

---

Como dicionarios sao mutaveis, eles podem ser alterados de varias maneiras. Itens podem ser removidos de um dicionario com o comando `del`:
```python
del dict_name[key_name]
```
ira remover a chave `key_name` e seu valor associado do dicionario.

---

E se quisermos listar todas as chaves do dicionario?
Bem, existe o metodo `keys()`.

---

E se quisermos listar todos os valores do dicionario?
Bem, existe o metodo `values()`.

---

Assim como nas listas, podemos percorrer os elementos de um dicionario usando as palavras-chave `for..in`
Para obter tanto a chave quanto o valor no loop, podemos usar o metodo `items()`:
```python
for key, value in dict_name:
    print(key, value)
```

---

Tambem podemos usar a palavra-chave `in` que usamos com loops para verificar se um dicionario contem uma determinada __chave__

---

Para __adicionar__ ou __alterar__ valores em um dicionario, tambem podemos usar o metodo `update()` com os _pares chave-valor_ que queremos adicionar entre chaves

---

E se quisermos __remover__ um valor de um dicionario?
Existe o metodo `pop()`:
```python
dict_name.pop("key_name")
```
