`Set`s são um tipo de dado que você pode usar para armazenar uma coleção de diferentes informações como uma sequência sob um único nome de variável.
A principal diferença com `List`s é que um `Set` permite apenas um elemento de cada valor.

Assim como `List`s, um `Set` armazena múltiplos valores de um ou mais tipos e usa **índices** para distinguir esses valores.
Você pode atribuir itens a um set com uma expressão da forma:
```kotlin
val setName = setOf<itemsType>(item1, item2)
```
`itemsType` representa o tipo dos itens dentro do set, por exemplo, pode ser `Int`, `String`, `Any`...

---

Um `Set` é uma coleção de itens __únicos__ sem uma ordem específica.

```kotlin
val numbers = setOf(1, 1, 2) // [1]
println(numbers)
// prints [1, 2]
```

Em __[1]__ estamos tentando criar um set com o número __1__ presente duas vezes, mas como você pode ver, cada elemento deve ser único e o segundo __1__ é automaticamente descartado.

---

Existem dois tipos de `Set`s em Kotlin:

- `Set` não pode ser modificado após a criação.
- `MutableSet` pode ser modificado após a criação, o que significa que você pode adicionar, remover ou atualizar seus elementos.

```kotlin
val numbers = setOf(1, 2, 3)
numbers.add(4) // [1]
```
__[1]__ lança um erro porque `Set`s são _somente leitura_.

Para criar um set modificável, use a palavra-chave `mutableSetOf`
```kotlin
val numbers = mutableSetOf(1, 2, 3)
numbers.add(4)
println(numbers)
// prints [1, 2, 3, 4]
```

---

A atividade mais comum com `Set` é testar a pertinência usando `in` ou `contains()`

```kotlin
val numbers = setOf(1, 2, 3)
println(2 in numbers) // prints true
println(numbers.contains(5)) // prints false
```

Como você pode ver acima, `in` e `contains` retornam um `Bool` indicando se o elemento passado está presente no set

---

A ordem dos elementos em um `Set` não é importante.
Na verdade, se você tentar comparar dois `Set`s com os mesmos elementos mas em ordem diferente, verá que eles são iguais.

---

Em `Set`s você pode realizar diversas operações como verificar união, interseção, diferença e subconjunto.

```kotlin
val firstNumbers = setOf(1, 2, 3)
val lastNumbers = setOf(3, 4, 5)
val union = firstNumbers.union(lastNumbers) // [1, 2, 3, 4, 5]
val intersection = firstNumbers intersect lastNumbers // [3]
val difference = firstNumbers subtract lastNumbers // [1, 2]
val subset = firstNumbers.containsAll(lastNumbers) // false
```

---

Para converter um `Set` em uma `List` podemos usar a função `toList()`
