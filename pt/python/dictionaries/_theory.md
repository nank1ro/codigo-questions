**Dicionários** são similares a listas e tuplas, mas você acessa valores procurando uma *chave* em vez de um índice.
Uma chave pode ser qualquer string ou número.
Dicionários são delimitados por chaves, como:
```python
d = {"key1": 1, "key2": 2, "key3": 3}
```
Este é um dicionário chamado `d` com três *pares chave-valor*.
A chave `key1` aponta para o valor `1`, `key2` para `2`, e assim por diante.

---

Acessar valores de dicionário por chave é como acessar valores de lista por índice:
```python
user['age']
# obtém o valor age do dicionário user
```

---

Como Listas, Dicionários são _mutáveis_.
Isso significa que eles podem ser alterados após serem criados.
Uma vantagem disso é que podemos adicionar novos _pares chave/valor_ ao dicionário após sua criação, como:
```python
dict_name[new_key_name] = new_value
```

---

O comprimento `len()` de um dicionário é o número de _pares chave-valor_ que ele possui.
Cada par conta apenas uma vez, mesmo que o valor seja uma lista. (Isso mesmo: você também pode colocar listas dentro de dicionários!)

---

Porque dicionários são mutáveis, eles podem ser alterados de muitas maneiras. Itens podem ser removidos de um dicionário com o comando `del`:
```python
del dict_name[key_name]
```
irá remover a chave `key_name` e seu valor associado do dicionário.

---

E se quisermos listar todas as chaves do dicionário?
Bem, existe o método `keys()`.

---

E se quisermos listar todos os valores do dicionário?
Bem, existe o método `values()`.

---

Assim como para listas, podemos iterar entre elementos do dicionário usando as palavras-chave `for..in`
Para obter tanto a chave quanto o valor no loop, podemos usar o método `items()`:
```python
for key, value in dict_name:
    print(key, value)
```

---

Também podemos usar a palavra-chave `in` que usamos com loops para determinar se um dicionário contém certa __chave__

---

Para __adicionar__ ou __alterar__ valores a um dicionário, também podemos usar o método `update()` com os _pares chave-valor_ que queremos adicionar entre chaves

---

E se quisermos __remover__ um valor de um dicionário?
Existe o método `pop()`:
```python
dict_name.pop("key_name")
```
