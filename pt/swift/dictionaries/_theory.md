**Dicionários** são semelhantes a arrays e tuplas, mas você acessa valores procurando por uma *chave* em vez de um índice.
Uma chave pode ser qualquer string ou número.
Dicionários são delimitados por colchetes, assim:
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
Este é um dicionário chamado `dictionaryName` com três *pares chave-valor*.
A chave `key1` aponta para o valor `1`, `key2` para `2`, e assim por diante.

---

Acessar valores de um dicionário pela chave é igual a acessar valores de um array pelo índice:
```swift
// gets the age value from the user dictionary
user['age']
```

---

Assim como Arrays, Dicionários são _mutáveis_.
Isso significa que eles podem ser alterados após serem criados (se não forem declarados como constantes).
Uma vantagem disso é que podemos adicionar novos _pares chave/valor_ ao dicionário após ele ser criado, assim:
```swift
dictName[newKeyName] = newValue
```

---

O comprimento `count` de um dicionário é o número de _pares chave-valor_ que ele possui.
Cada par conta apenas uma vez, mesmo que o valor seja um array. (Isso mesmo: você também pode colocar arrays dentro de dicionários!)

---

Como dicionários são mutáveis, eles podem ser alterados de várias formas. Itens podem ser removidos de um dicionário com o método `removeValue(forKey:)`:
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed value, if the key exists
}
```
irá remover a chave `keyName` e seu valor associado do dicionário.

---

E se quisermos listar todas as chaves do dicionário?
Bem, existe a propriedade `keys`.

---

E se quisermos listar todos os valores do dicionário?
Bem, existe a propriedade `values`.

---

Assim como em arrays, podemos percorrer os elementos de um dicionário usando as palavras-chave `for..in`.
Para obter tanto a chave quanto o valor no loop, não precisamos especificar nenhuma propriedade:
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

Também podemos usar a propriedade `isEmpty` que usamos com arrays para verificar se um dicionário está vazio

---

Para __adicionar__ ou __alterar__ valores em um dicionário, também podemos usar o método `updateValue(_:forKey:)`

---

Anteriormente vimos como remover um _par chave-valor_ do dicionário com o método `removeValue()`.
Também podemos remover um elemento atribuindo à chave o valor `nil`
```swift
dictName[keyName] = nil
// keyName has been removed from the dictionary dictName
```
