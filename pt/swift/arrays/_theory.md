Arrays são um tipo de dado que você pode usar para armazenar uma coleção de diferentes informações como uma sequência sob um único nome de variável.
Um array armazena múltiplos valores de um ou vários tipos e usa **índices** para distinguir esses valores.
Você pode atribuir itens a um array com uma expressão da forma:
```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType` representa o tipo dos itens dentro do array, por exemplo, pode ser `Int`, `String`, `Any`...

---

Você pode acessar um item individual do array pelo seu índice.
Um índice é como um endereço que identifica a posição do item no array.
O índice aparece diretamente após o nome do array, entre colchetes, assim:
```swift
arrayName[index]
```

Os índices de arrays começam com `0`, **não** `1`! Você acessa o primeiro item de um array assim: `arrayName[0]`.
O segundo item em um array está no índice 1: `arrayName[1]`.

---

Um índice de array se comporta como qualquer outro nome de variável.
Ele pode ser usado tanto para acessar quanto para atribuir valores.
Você viu como acessar um índice de array assim:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Imprime o valor "Jeremiah"
print(names[0])
```
É assim que uma atribuição funciona:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Atribui o novo valor "Jordan"
names[0] = "Jordan"
// Imprime o valor "Jordan"
print(names[0])
```

---

Assim como strings, arrays tem um **comprimento** `count`.
O comprimento de um array e o numero de itens que ele contem

---

Um array não precisa ter um tamanho fixo.
Você pode adicionar itens ao final de um array quando quiser!
Para adicionar um item a um array, usamos a função `append`:
```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// Imprime ["a", "b", "c"]
```

---

Às vezes, você só quer acessar uma parte de um array.
Considere o seguinte código:
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// imprime [2, 3]
```
Primeiro, criamos um array chamado `numbers`.
Depois, pegamos uma subseção do array e armazenamos no array slice.
Fazemos isso definindo os índices que queremos incluir após o nome do array: `numbers[1...2]`.
Em Swift, podemos incluir o último índice usando `...`, mas também podemos excluir o último índice usando `..<`

---

Em Swift, podemos fatiar um array como quisermos!
```swift
// Pega os dois primeiros itens
listName[..<2]
// Pega do quarto item até o último
listName[3...]
```
Se o seu fatiamento de array incluir o primeiro ou o último item de um array, o índice para esse item não precisa ser incluído

---

Os elementos de um array podem ser de qualquer tipo, se especificarmos o tipo `Any`:
```swift
var arrayName: [Any] = ["one", 2, true]
```
De fato, acima temos, em ordem, uma string, um inteiro e um booleano.
Mas também podemos ter arrays com arrays!

---

Às vezes você precisa procurar um item em um array.
Em Swift, podemos usar o método `firstIndex()`:
```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// imprime 1
```
O código acima imprime o primeiro índice que contém a string `"Zac"`, `1` neste caso.
Também podemos inserir itens em um array em um índice específico, usando o método `insert()`:
```swift
names.insert("Ali", at: 1)
// imprime ["Trevor", "Ali", "Zac", "Glenn"]
```
O código acima insere `"Ali"` no índice `1`, o que move tudo, após este índice, uma posição para baixo

---

Em Swift, podemos percorrer um array de forma muito simples usando as palavras-chave `for..in`:
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// imprime 1, 2, 3
```
Um nome de variável segue a palavra-chave `for`, ele receberá o valor de cada item do array por vez.

---

**Tuplas** são como arrays, mas você pode nomear os elementos e usar esses nomes para se referir a eles.
Para criar uma tupla, usamos os parênteses `()`
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
