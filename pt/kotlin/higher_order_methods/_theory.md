Um **método de ordem superior** é um método que recebe uma função como argumento. As coleções do Kotlin oferecem muitos deles, e a função que você passa geralmente é uma **lambda**: uma pequena função anônima escrita entre chaves.
`map` é o mais comum: chama a lambda em cada elemento e retorna uma **nova lista** com os resultados, deixando a original intacta:
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6]
println(numbers) // [1, 2, 3]
```
Quando a lambda tem um único parâmetro você não precisa declará-lo: o Kotlin o chama de `it`. A lambda é escrita depois do nome do método, fora dos parênteses, que podem ser omitidos quando a lambda é o único argumento. Essa é a sintaxe de **trailing lambda** e ela é usada em todos os exercícios deste tópico.

---

`filter` recebe uma lambda que retorna um `Boolean`, chamada de **predicado**, e retorna uma nova lista apenas com os elementos para os quais o predicado é `true`:
```kotlin
val numbers = listOf(4, -2, 7, 0)
println(numbers.filter { it > 0 }) // [4, 7]
```
Em vez de `it` você pode dar um nome ao parâmetro, seguido de uma seta `->`. Um parâmetro nomeado torna lambdas longas mais legíveis, e é obrigatório quando uma lambda está aninhada dentro de outra, porque o `it` interno esconde o elemento externo:
```kotlin
val minLength = 4
val words = listOf("fig", "banana", "kiwi")
println(words.filter { word -> word.length >= minLength }) // [banana, kiwi]
```

---

`forEach` executa a lambda uma vez para cada elemento e não retorna nada. É a alternativa de ordem superior ao laço `for`, e é usado para efeitos colaterais como imprimir:
```kotlin
listOf("a", "b").forEach { println(it) }
```
`forEachIndexed` também dá a posição de cada elemento. Sua lambda tem **dois** parâmetros, então eles precisam ser nomeados: `it` só existe para lambdas com exatamente um parâmetro.
```kotlin
listOf("a", "b").forEachIndexed { index, letter ->
    println("$index: $letter") // 0: a, depois 1: b
}
```

---

`reduce` combina todos os elementos em um único valor. Sua lambda recebe dois parâmetros: o **acumulador** (o resultado até aquele ponto) e o próximo elemento. Ele começa com o primeiro elemento como acumulador e executa a lambda para cada elemento restante:
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n }) // 10
```
`reduce` lança uma exceção em uma lista vazia, porque não há um primeiro elemento do qual partir. `fold` resolve isso: você passa o **valor inicial** do acumulador como argumento, e a lambda é executada para cada elemento, incluindo o primeiro:
```kotlin
println(numbers.fold(0) { acc, n -> acc + n })   // 10
println(listOf<Int>().fold(0) { acc, n -> acc + n }) // 0
```
Com `fold` o acumulador pode até ter um tipo diferente dos elementos, como construir uma `String` a partir de uma lista de números.

---

Alguns métodos de ordem superior respondem a uma pergunta sobre a coleção em vez de construir uma nova. Todos eles recebem um predicado:
- `any` retorna `true` se **pelo menos um** elemento o satisfaz
- `all` retorna `true` se **todos** os elementos o satisfazem
- `none` retorna `true` se **nenhum** elemento o satisfaz
- `count` retorna **quantos** elementos o satisfazem
```kotlin
val numbers = listOf(1, 2, 3)
println(numbers.any { it > 2 })   // true
println(numbers.all { it > 2 })   // false
println(numbers.none { it > 2 })  // false
println(numbers.count { it > 1 }) // 2
```
Em uma lista vazia `any` retorna `false`, enquanto `all` e `none` retornam `true`: não há nenhum elemento que quebre a regra.

---

Os métodos de agregação transformam uma coleção inteira em um único valor:
- `sum()` soma uma lista de números, enquanto `sumOf` soma o valor que a lambda calcula para cada elemento
- `maxByOrNull` e `minByOrNull` retornam o **elemento** para o qual a lambda dá o maior ou o menor valor, ou `null` em uma lista vazia
```kotlin
val words = listOf("fig", "banana", "kiwi")
println(words.sumOf { it.length })      // 13
println(words.minByOrNull { it.length }) // fig
println(listOf(1, 2, 3).sum())           // 6
```
Observe a diferença em relação a `maxOf { it.length }`, que retorna o maior **valor** (`6`) em vez do elemento que o produziu.

---

`sortedBy` retorna uma nova lista ordenada pelo valor que a lambda calcula para cada elemento, do menor para o maior. `sortedByDescending` ordena do maior para o menor. Quando são os próprios elementos que você quer comparar, `sorted()` e `sortedDescending()` não precisam de lambda:
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })            // [fig, kiwi, banana]
println(words.sortedByDescending { it.length })  // [banana, kiwi, fig]
println(words.sorted())                          // [banana, fig, kiwi]
```
A ordenação é **estável**: elementos com a mesma chave mantêm sua ordem relativa original. A lista original nunca é modificada.

---

`take(n)` retorna uma nova lista com os primeiros `n` elementos, e `drop(n)` retorna uma nova lista **sem** os primeiros `n` elementos. Nenhum dos dois recebe uma lambda, mas eles costumam ser encadeados depois de um método que recebe:
```kotlin
val numbers = listOf(5, 3, 8, 1)
println(numbers.take(2))                    // [5, 3]
println(numbers.drop(2))                    // [8, 1]
println(numbers.sortedDescending().take(2)) // [8, 5]
```
`takeWhile` e `dropWhile` são as versões com um predicado: pegam ou descartam elementos a partir do início **enquanto** o predicado for `true`, e param no primeiro elemento que não o satisfaz:
```kotlin
println(numbers.takeWhile { it > 2 }) // [5, 3, 8]
```

---

`groupBy` divide uma coleção em um `Map`: a lambda calcula a **chave** de cada elemento, e cada chave é associada à lista dos elementos que a produziram, na ordem original:
```kotlin
val words = listOf("fig", "kiwi", "pear")
val byLength = words.groupBy { it.length }
println(byLength)    // {3=[fig], 4=[kiwi, pear]}
println(byLength[4]) // [kiwi, pear]
```
O resultado tem o tipo `Map<K, List<T>>`, onde `K` é o tipo retornado pela lambda e `T` é o tipo dos elementos. As chaves aparecem na ordem em que são encontradas pela primeira vez.

---

Quando a lambda retorna uma **lista** para cada elemento, `map` produz uma lista de listas. `flatMap` faz o mesmo, mas depois junta todas essas listas em uma única lista plana:
```kotlin
val numbers = listOf(1, 2)
println(numbers.map { listOf(it, -it) })     // [[1, -1], [2, -2]]
println(numbers.flatMap { listOf(it, -it) }) // [1, -1, 2, -2]
```
A ordem é preservada: primeiro vêm todos os valores produzidos pelo primeiro elemento, depois os do segundo, e assim por diante. Se você já tem uma lista de listas, `flatten()` as junta sem uma lambda.

---

`zip` emparelha os elementos de duas listas posição por posição. Sem uma lambda ele retorna uma lista de valores `Pair`, cujas metades são lidas com `.first` e `.second`; com uma lambda, os dois elementos de cada posição são passados para ela e os resultados são reunidos em uma lista:
```kotlin
val names = listOf("Ann", "Bob")
val ages = listOf(31, 25)
println(names.zip(ages))                            // [(Ann, 31), (Bob, 25)]
println(names.zip(ages) { name, age -> "$name:$age" }) // [Ann:31, Bob:25]
```
O resultado tem o tamanho da **menor** das duas listas: os elementos extras da mais longa são ignorados.

---

A forma da lambda deve corresponder ao que o método espera:
- os métodos que trabalham com um elemento por vez (`map`, `filter`, `sortedBy`, `groupBy`...) recebem uma lambda de **um parâmetro**, onde `it` está disponível
- `reduce`, `fold`, `forEachIndexed` e `zip` com uma lambda passam **dois** valores, então os parâmetros precisam ser nomeados explicitamente com `a, b ->`
```kotlin
val numbers = listOf(1, 2, 3)
numbers.map { it * 2 }                  // ok: um parâmetro, it está disponível
numbers.reduce { acc, n -> acc + n }    // ok: dois parâmetros, nomeados
numbers.reduce { it + 1 }               // erro: it não existe com dois parâmetros
```
Nomear os parâmetros é sempre permitido, mesmo com um só: `numbers.map { n -> n * 2 }`.

---

Os métodos de ordem superior podem ser **encadeados**: cada um retorna uma nova coleção sobre a qual o próximo trabalha, então um cálculo inteiro se lê como um pipeline da esquerda para a direita:
```kotlin
val words = listOf("kiwi", "fig", "banana", "date")
println(words.filter { it.length == 4 }.map { it.uppercase() }.sorted()) // [DATE, KIWI]
```
Os mapas também têm métodos de ordem superior. `mapValues` mantém as chaves e substitui cada valor pelo resultado da lambda, que recebe a **entrada** com `.key` e `.value`:
```kotlin
val byLength = words.groupBy { it.length }      // {4=[kiwi, date], 3=[fig], 6=[banana]}
println(byLength.mapValues { it.value.size })   // {4=2, 3=1, 6=1}
```

---

Em uma cadeia, o tipo de `it` muda a cada passo: depois de `filter` em uma `List<String>` você ainda tem strings, mas depois de `map { it.length }` você tem uma `List<Int>`, então a próxima lambda vê números.
```kotlin
val words = listOf("kiwi", "fig")
println(words.map { it.length }.filter { it > 3 }) // [4]
```
Cada passo retorna uma lista **nova** e nunca toca na anterior, então uma cadeia pode ser dividida em valores intermediários nomeados sem mudar o resultado.

---

Uma lambda pode conter outra chamada de ordem superior. Dentro da lambda interna, `it` se refere ao elemento **interno** e esconde o externo, então dê um nome explícito ao parâmetro externo para manter os dois acessíveis:
```kotlin
val sales = listOf("north" to 120, "south" to 80, "north" to 30)
val byRegion = sales.groupBy { it.first }
val totals = byRegion.mapValues { entry -> entry.value.sumOf { it.second } }
println(totals) // {north=150, south=80}
```
`"north" to 120` cria um `Pair`. Aqui a lambda externa trabalha sobre uma entrada do mapa, enquanto a interna trabalha sobre os pares da lista dessa entrada.

---

Um `Map` pode ser processado como uma lista de entradas: `filter` e `map` funcionam diretamente no mapa e recebem cada entrada com `.key` e `.value`. `filter` em um mapa retorna um mapa, enquanto `map` retorna uma lista. Métodos de ordenação como `sortedBy` não são definidos em um mapa: passe primeiro por `scores.entries`, que é uma coleção das entradas:
```kotlin
val scores = mapOf("Ann" to 90, "Bob" to 72)
println(scores.filter { it.value > 80 })              // {Ann=90}
println(scores.entries.sortedBy { it.value }.map { it.key }) // [Bob, Ann]
```
`scores.entries` é o conjunto de todas as entradas; `scores.keys` e `scores.values` dão apenas um dos lados.
