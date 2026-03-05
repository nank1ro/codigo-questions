**Objetos** são semelhantes a arrays, mas você acessa valores procurando por uma *chave* em vez de um índice.
Uma chave pode ser qualquer string ou número.
Objetos são delimitados por chaves, assim:
```javascript
var objectName = {"key1": 1, "key2": 2, "key3": 3};
```
Este é um dicionário chamado `objectName` com três *pares chave-valor*.
A chave `key1` aponta para o valor `1`, `key2` para `2`, e assim por diante.

---

Acessar valores de um dicionário por chave é como acessar valores de um array por índice:
```javascript
// obtém o valor de age do dicionário user
user['age'];
```

---

Assim como Arrays, Dicionários são _mutáveis_.
Isso significa que eles podem ser alterados após serem criados (se não forem declarados como constantes).
Uma vantagem disso é que podemos adicionar novos _pares chave/valor_ ao dicionário após ele ser criado, assim:
```javascript
dictName[newKeyName] = newValue;
```

---

Como variáveis de dicionários são mutáveis, elas podem ser alteradas de várias formas.
Itens podem ser removidos de um dicionário com a palavra-chave 'delete':
```javascript
delete dictName[keyName];
```
irá remover a chave `keyName` e seu valor associado do dicionário.

---

E se quisermos listar todas as chaves do dicionário?
Bem, existe o método `Object.keys()`.

---

E se quisermos listar todos os valores do dicionário?
Bem, existe o método `Object.values()`.

---

Assim como em arrays, podemos iterar entre os elementos de um dicionário usando o método `Object.entries()`.
```javascript
var user = {"first_name": "John", "last_name": "Hood", "age": 30};
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```
