Arrays sao um tipo de dado que voce pode usar para armazenar uma colecao de diferentes informacoes como uma sequencia sob um unico nome de variavel.
Um array armazena multiplos valores de um ou varios tipos e usa **indices** para distinguir esses valores.
Voce pode atribuir itens a um array com uma expressao da forma:
```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType` representa o tipo dos itens dentro do array, por exemplo, pode ser `Int`, `String`, `Any`...

---

Voce pode acessar um item individual do array pelo seu indice.
Um indice e como um endereco que identifica a posicao do item no array.
O indice aparece diretamente apos o nome do array, entre colchetes, assim:
```swift
arrayName[index]
```

Os indices de arrays comecam com `0`, **nao** `1`! Voce acessa o primeiro item de um array assim: `arrayName[0]`.
O segundo item em um array esta no indice 1: `arrayName[1]`.

---

Um indice de array se comporta como qualquer outro nome de variavel.
Ele pode ser usado tanto para acessar quanto para atribuir valores.
Voce viu como acessar um indice de array assim:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
print(names[0])
```
E assim que uma atribuicao funciona:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
print(names[0])
```

---

Assim como strings, arrays tem um **comprimento** `count`.
O comprimento de um array e o numero de itens que ele contem

---

Um array nao precisa ter um tamanho fixo.
Voce pode adicionar itens ao final de um array quando quiser!
Para adicionar um item a um array, usamos a funcao `append`:
```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// Prints ["a", "b", "c"]
```

---

As vezes, voce so quer acessar uma parte de um array.
Considere o seguinte codigo:
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// prints [2, 3]
```
Primeiro, criamos um array chamado `numbers`.
Depois, pegamos uma subsecao do array e armazenamos no array slice.
Fazemos isso definindo os indices que queremos incluir apos o nome do array: `numbers[1...2]`.
Em Swift, podemos incluir o ultimo indice usando `...`, mas tambem podemos excluir o ultimo indice usando `..<`

---

Em Swift, podemos fatiar um array como quisermos!
```swift
// Grabs the first two items
listName[..<2]
// Grabs the fourth through last items
listName[3...]
```
Se o seu fatiamento de array incluir o primeiro ou o ultimo item de um array, o indice para esse item nao precisa ser incluido

---

Os elementos de um array podem ser de qualquer tipo, se especificarmos o tipo `Any`:
```swift
var arrayName: [Any] = ["one", 2, true]
```
De fato, acima temos, em ordem, uma string, um inteiro e um booleano.
Mas tambem podemos ter arrays com arrays!

---

As vezes voce precisa procurar um item em um array.
Em Swift, podemos usar o metodo `firstIndex()`:
```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// prints 1
```
O codigo acima imprime o primeiro indice que contem a string `"Zac"`, `1` neste caso.
Tambem podemos inserir itens em um array em um indice especifico, usando o metodo `insert()`:
```swift
names.insert("Ali", at: 1)
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
O codigo acima insere `"Ali"` no indice `1`, o que move tudo, apos este indice, uma posicao para baixo

---

Em Swift, podemos percorrer um array de forma muito simples usando as palavras-chave `for..in`:
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// prints 1, 2, 3
```
Um nome de variavel segue a palavra-chave `for`, ele recebera o valor de cada item do array por vez.

---

**Tuplas** sao como arrays, mas voce pode nomear os elementos e usar esses nomes para se referir a eles.
Para criar uma tupla, usamos os parenteses `()`
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
