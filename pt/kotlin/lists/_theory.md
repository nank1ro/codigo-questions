Listas são um tipo de dado que você pode usar para armazenar uma coleção de diferentes informações como uma sequência sob um único nome de variável.
Uma lista armazena múltiplos valores de um ou mais tipos e usa **índices** para distinguir esses valores.
Você pode atribuir itens a uma lista com uma expressão da forma:
```kotlin
val listName = listOf<itemsType>(item1, item2)
```
`itemsType` representa o tipo dos itens dentro da lista, por exemplo, pode ser `Int`, `String`, `Any`...

---

Uma lista é uma coleção de itens com uma ordem específica. Existem dois tipos de listas em Kotlin:

- `List` não pode ser modificada após sua criação.
- `MutableList` pode ser modificada após sua criação, o que significa que você pode adicionar, remover ou atualizar seus elementos.

```kotlin
val numbers = listOf(1, 3, 5)
numbers.add(7) // [1]
```
__[1]__ lança um erro porque `List`s são _somente leitura_.

Para criar uma lista modificável, use a palavra-chave `mutableListOf`
```kotlin
val numbers = mutableListOf(1, 3, 5)
numbers.add(7)
println(numbers)
// prints [1, 3, 5, 7]
```

---

Você pode acessar um item individual da lista pelo seu índice.
Um índice é como um endereço que identifica a posição do item na lista.
O índice aparece diretamente após o nome da lista, entre colchetes, assim:
```kotlin
listName[index]
```

Os índices das listas começam em `0`, **não** em `1`! Você acessa o primeiro item de uma lista assim: `listName[0]` ou `listName.get(0)` ou até `listName.first()`.
O segundo item em uma lista está no índice __1__: `listName[1]`.

---

O índice é na verdade um deslocamento a partir do primeiro elemento. Por exemplo, quando você diz `list[2]` você não está pedindo o segundo elemento da lista, mas sim o elemento que está 2 posições deslocado do primeiro elemento. Portanto, `list[0]` é o primeiro elemento (deslocamento zero), `list[1]` é o segundo elemento (deslocamento de 1), `list[2]` é o terceiro elemento (deslocamento de 2), e assim por diante.

Um índice de lista pode ser usado tanto para acessar quanto para atribuir valores.
Você viu como acessar um índice de lista assim:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
println(names[0])
```
É assim que uma atribuição funciona:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel")
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
println(names[0])
```

---

Assim como strings, listas têm um **comprimento** obtido com o getter `size`.
O comprimento de uma lista é o número de itens que ela contém

---

Outra operação útil de listas é o método `contains` para descobrir se um determinado elemento está na lista.
Por exemplo, se você tem uma lista de nomes, pode usar o método `contains` para descobrir se um determinado nome está presente na lista.
```kotlin
val names = listOf("Thomas", "Donald", "Scarlett")
println(names.contains("Scarlett"))
// prints true
```

---

Uma lista mutável não precisa ter um tamanho fixo.
Você pode adicionar itens ao final de uma lista quando quiser!
Para adicionar um item a uma lista mutável, usamos a função `add` ou o atalho `+=`:
```kotlin
val letters = mutableListOf("a", "b")
letters.add("c")
println(letters)
// prints [a, b, c]
```

---

Como vimos no exemplo anterior, podemos adicionar itens um por um usando a função `add`.
Mas se precisamos adicionar todos os elementos de outra lista de uma vez, podemos simplesmente usar a função `addAll`, ou o atalho `+=`:
```kotlin
val letters = mutableListOf("a", "b")
val newLetters = listOf("c", "d", "e")
letters.addAll(newLetters)
println(letters)
// prints [a, b, c, d, e]
```

---

Às vezes, você só quer acessar uma parte de uma lista.
Considere o seguinte código:
```kotlin
val numbers = listOf(1, 2, 3, 4) // [1]
val slice = numbers.slice(1..2) // [2]
println(slice)
// prints [2, 3]
```
__[1]__: primeiro, criamos uma lista _somente leitura_ chamada `numbers`.
__[2]__: depois, pegamos uma subseção da lista usando a função `slice` e armazenamos na lista slice.
Fazemos isso definindo os índices que queremos incluir dentro da função `slice`.

Em Kotlin, podemos incluir o último índice usando `..`, mas também podemos excluir o último índice usando `until`

---

Os elementos de listas podem ser de qualquer tipo, se especificarmos o tipo `Any`:
```kotlin
var listName: List<Any> = listOf("one", 2, true)
```
De fato, acima temos, em ordem, um `String`, um `Integer` e um `Boolean`.
Mas também podemos ter listas dentro de listas!

---

Às vezes você precisa procurar um item em uma lista.
Em Kotlin, podemos usar o método `indexOfFirst`:
```kotlin
val names = mutableListOf("Trevor", "Zac", "Glenn")
println(names.indexOfFirst { it == "Zac"})
// prints 1
```

O método `indexOfFirst` recebe uma função __predicado__ que será avaliada para cada item da lista até ser verdadeira, retornando o _índice_ do elemento.
O código acima imprime o primeiro índice que contém a string `"Zac"`, `1` neste caso.

Também podemos inserir itens em uma lista modificável em um índice específico, usando o método `add(index, element)`:
```kotlin
names.add(1, "Ali")
// prints [Trevor, Ali, Zac, Glenn]
```
O código acima insere `"Ali"` no índice `1`, o que desloca tudo após esse índice em 1 posição

---

Em Kotlin, podemos percorrer uma lista de forma muito simples usando as palavras-chave `for..in`:
```kotlin
val numbers = listOf(1, 2, 3)
for (num in numbers) {
    println(num)
}
// prints 1, 2, 3
```
Um nome de variável segue a palavra-chave `for`, e receberá o valor de cada item da lista por vez.
