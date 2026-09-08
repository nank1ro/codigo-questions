Um **Set** é uma coleção que armazena valores do mesmo tipo sem ordem definida e, o mais importante, **sem duplicatas**: cada valor aparece no máximo uma vez.
Sets são perfeitos quando você só se importa com *quais* valores estão presentes, não quantas vezes ou em qual posição.
Você declara um set com o tipo `Set<Element>` e um literal no estilo de array:
```swift
let numbers: Set<Int> = [1, 2, 3]
```
A anotação de tipo é obrigatória: sem ela o Swift criaria um array.
Se o literal contiver um valor mais de uma vez, o set mantém apenas uma cópia:
```swift
let rolls: Set<Int> = [6, 6, 6]
print(rolls.count) // 1
```
A propriedade `count` informa quantos valores distintos o set contém.

---

Assim como os arrays, os sets podem ser constantes (`let`) ou variáveis (`var`). Apenas um set `var` pode ser alterado depois de criado.
Para criar um set vazio você chama o inicializador do tipo, porque um literal vazio `[]` sozinho não diria ao Swift qual tipo de elemento usar:
```swift
var visited = Set<String>()
print(visited.isEmpty) // true
```
A propriedade `isEmpty` é `true` quando o set não tem elementos, exatamente como nos arrays.

---

Como um set nunca armazena o mesmo valor duas vezes, seu `count` é o número de valores *distintos*, não importa quantas vezes cada um foi escrito no literal.

---

Para verificar se um valor está em um set, use o método `contains(_:)`, que retorna um `Bool`:
```swift
let primes: Set<Int> = [2, 3, 5, 7]
print(primes.contains(5)) // true
print(primes.contains(6)) // false
```
Essa verificação é muito rápida em um set, mesmo com milhares de elementos, o que é uma das principais razões para preferir um set a um array em testes de pertencimento.

---

Um set `var` pode ser modificado com `insert(_:)` e `remove(_:)`:
```swift
var numbers: Set<Int> = [1, 2]
numbers.insert(3) // {1, 2, 3}
numbers.insert(2) // 2 is already there: nothing changes
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 is not there: nothing changes
```
Inserir um valor que já está presente não tem efeito, e remover um valor ausente não causa um erro.
`remove(_:)` retorna o valor removido como um opcional (`nil` quando nada foi removido), para que você possa verificar se a remoção realmente aconteceu.
Para esvaziar um set completamente, chame `removeAll()`.

---

Você pode percorrer um set com `for`-`in`, mas lembre-se de que um set **não tem ordem definida**: os elementos podem sair em qualquer ordem, e essa ordem pode mudar entre execuções.
Quando a ordem importa, chame `sorted()` primeiro: ele retorna um novo **array** com os elementos em ordem crescente, deixando o set intacto.
```swift
let numbers: Set<Int> = [3, 1, 2]
for number in numbers.sorted() {
    print(number) // 1, 2, 3 on separate lines
}
```
