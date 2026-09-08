Um **array** armazena um número fixo de valores do mesmo tipo sob um único nome de variável.
Você cria um com `arrayOf`, lê um elemento com colchetes e um **índice** que começa em `0`, e obtém o número de elementos com `size`:
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
O último elemento está no índice `size - 1`.

---

`arrayOf(1, 2, 3)` cria um `Array<Int>` no qual cada elemento é um objeto encapsulado (boxed).
Para tipos primitivos, o Kotlin oferece tipos dedicados e mais eficientes, como `IntArray`, `DoubleArray` e `BooleanArray`:
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
Você também pode construir um array de um tamanho determinado com uma lambda de **inicialização** que recebe cada índice, ou um `IntArray` preenchido com zeros:
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

Todo array tem duas propriedades úteis para trabalhar com índices:
- `indices` é o intervalo de índices válidos, de `0` até o último
- `lastIndex` é o índice do último elemento, ou seja, `size - 1`
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

Mesmo quando um array é declarado com `val`, seus **elementos** podem ser substituídos atribuindo um valor a um índice:
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
Para visitar cada elemento você pode usar um loop `for` ou `forEach`:
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
Observe que `n` e `it` são cópias somente leitura dos valores e não podem ser reatribuídas, então para modificar elementos você precisa do índice deles.

---

Para verificar se um array contém um valor, use `in` ou `contains`, ambos retornam um `Boolean`.
`indexOf` retorna o índice da primeira ocorrência, ou `-1` quando o valor não está presente:
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

Imprimir um array diretamente não mostra seus elementos, imprime algo como `[Ljava.lang.String;@1b6d3586`.
Use `joinToString` para construir uma string legível, opcionalmente com um separador customizado (o padrão é `", "`), ou `contentToString` para obter os elementos entre colchetes:
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

Arrays podem ser ordenados **no local** (in place) ou copiados para uma nova coleção ordenada:
- `sort()` e `sortDescending()` reordenam o próprio array e não retornam nada
- `reverse()` inverte a ordem do próprio array
- `sorted()`, `sortedDescending()` e `reversed()` deixam o array intacto e retornam uma nova `List`
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

Arrays numéricos vêm com funções de agregação:
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()` e `min()` lançam uma exceção em um array vazio, use `maxOrNull()` e `minOrNull()` quando o array puder estar vazio.

---

A principal diferença entre um array e uma `MutableList` é que um array tem **tamanho fixo**: depois de criado você pode substituir seus elementos, mas nunca pode adicionar ou remover um, não existe função `add`.
Expressões como `nums + 4` não fazem `nums` crescer, elas constroem um array totalmente novo:
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
Prefira uma `MutableList` quando o número de elementos muda ao longo do tempo, e um array quando ele é conhecido de antemão ou quando você precisa de desempenho com tipos primitivos.

---

Arrays suportam as mesmas funções de transformação que as listas. `filter` mantém os elementos que atendem a uma condição e `map` transforma cada elemento.
Ambas retornam uma nova `List`, não um array:
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
Como o resultado é uma lista, imprimi-la diretamente mostra seus elementos.

---

Quando você precisa tanto do índice quanto do valor durante um loop, use `withIndex()` e desestruture cada par, ou `forEachIndexed`:
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

Arrays e listas se convertem facilmente uns nos outros:
- `toList()` e `toMutableList()` copiam um array para uma lista
- `toTypedArray()` copia uma lista para um `Array<T>`
- `toIntArray()` copia uma lista de `Int` para um `IntArray`
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
Cada conversão cria uma **cópia**, então alterar o resultado não afeta o original.

---

Diferente das listas, dois arrays com os mesmos elementos **não** são iguais com `==`: arrays são comparados por referência, então `==` é `true` apenas para o mesmíssimo objeto array.
Para comparar o conteúdo, use `contentEquals`:
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

Como arrays têm tamanho fixo, obter parte de um significa criar um novo array:
- `copyOf()` copia o array inteiro, `copyOf(n)` copia os primeiros `n` elementos
- `copyOfRange(from, to)` copia os elementos do índice `from` até `to` **excluído**
- `sliceArray(range)` copia os elementos nos índices do intervalo, com ambas as extremidades incluídas
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
