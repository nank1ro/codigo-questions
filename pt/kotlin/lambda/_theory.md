Uma **lambda** é uma pequena função sem nome, escrita diretamente como uma expressão entre chaves.
Os parâmetros vêm primeiro, depois uma seta `->`, depois o corpo:
```kotlin
val add = { a: Int, b: Int -> a + b }
```
Uma lambda é um valor como qualquer outro: você pode armazená-la em uma variável e chamá-la depois com parênteses, exatamente como uma função:
```kotlin
println(add(2, 3)) // 5
```
Uma lambda sem parâmetros não tem seta alguma: `val hello = { println("Hello!") }`.

---

Toda lambda tem um **tipo função**, escrito como os tipos dos parâmetros entre parênteses, uma seta e o tipo de retorno.
A lambda `{ a: Int, b: Int -> a + b }` tem o tipo `(Int, Int) -> Int`: ela recebe dois valores `Int` e retorna um `Int`.
Quando você declara o tipo função na variável, os tipos dos parâmetros dentro da lambda podem ser omitidos, porque o compilador já os conhece:
```kotlin
val add: (Int, Int) -> Int = { a, b -> a + b }
val greet: (String) -> Unit = { name -> println("Hi, $name") }
```
Uma lambda que não retorna nada tem o tipo de retorno `Unit`.

---

O corpo de uma lambda pode ocupar várias linhas. Não há palavra-chave `return`: o valor da **última expressão** é o que a lambda retorna.
```kotlin
val describe: (Int) -> String = { n ->
    val half = n / 2
    "half of $n is $half" // returned
}
println(describe(10)) // half of 10 is 5
```
Como `if` é uma expressão no Kotlin, ele pode ser a última linha e decidir o resultado:
```kotlin
val parity: (Int) -> String = { n -> if (n % 2 == 0) "even" else "odd" }
```

---

Quando uma lambda tem exatamente **um** parâmetro, você pode omitir a declaração dele: o Kotlin o nomeia como `it` para você.
```kotlin
// val double: (Int) -> Int = { n -> n * 2 }
val double: (Int) -> Int = { it * 2 } // same thing
```
O `it` só existe quando o parâmetro não é declarado explicitamente, e apenas para lambdas de um único parâmetro.
Ele mantém lambdas curtas compactas, mas para corpos mais longos um nome real é mais claro.

---

Lambdas são usadas principalmente como argumentos de outras funções. As coleções oferecem muitas funções que recebem uma lambda:
- `forEach` executa a lambda uma vez para cada elemento
- `map` constrói uma nova lista com o resultado da lambda para cada elemento
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map({ it * 2 }) // [2, 4, 6]
```
Quando a lambda é o **último** argumento, você pode movê-la para fora dos parênteses; quando ela é o único argumento, os parênteses podem ser omitidos completamente. Isso é chamado de sintaxe **trailing lambda** e é a forma usual de escrevê-la:
```kotlin
val doubled = numbers.map { it * 2 }
doubled.forEach { println(it) }
```

---

Uma lambda que retorna um `Boolean` é chamada de **predicado**. Várias funções de coleção recebem um:
- `filter` mantém apenas os elementos para os quais o predicado é `true`
- `count` retorna quantos elementos o satisfazem
- `any` e `all` dizem se alguns ou todos os elementos o satisfazem
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)
println(numbers.filter { it % 2 == 0 }) // [2, 4, 6]
println(numbers.count { it > 4 })        // 2
println(numbers.any { it > 5 })          // true
```
As chamadas podem ser **encadeadas**: cada função retorna uma nova lista sobre a qual a próxima trabalha.
```kotlin
println(numbers.filter { it % 2 == 0 }.map { it * 10 }) // [20, 40, 60]
```

---

Lambdas também comandam a ordenação e a agregação:
- `sortedBy` retorna uma nova lista ordenada pelo valor que a lambda calcula para cada elemento; `sortedByDescending` faz o oposto
- `reduce` combina todos os elementos em um único valor: a lambda recebe o resultado acumulado até agora e o próximo elemento
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })          // [fig, kiwi, banana]
println(words.sortedByDescending { it.length }) // [banana, kiwi, fig]

val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n })   // 10
```
O `reduce` começa com o primeiro elemento como `acc` e depois executa a lambda para cada elemento restante.

---

Com o `reduce` a forma do resultado fica a cargo da lambda. Qualquer operação que combine dois valores funciona: uma soma, um produto, manter o maior dos dois.
```kotlin
val numbers = listOf(3, 9, 4)
println(numbers.reduce { acc, n -> if (n > acc) n else acc }) // 9
```
Note que o `reduce` lança uma exceção em uma lista vazia, porque não há um primeiro elemento de onde partir.

---

Uma lambda pode usar as variáveis declaradas ao redor dela, mesmo depois que o código ao redor já seguiu adiante. Isso é chamado de **closure**: a lambda *captura* as variáveis de que precisa.
Diferente de muitas outras linguagens, o Kotlin permite que uma lambda **modifique** um `var` capturado:
```kotlin
var clicks = 0
val onClick = { clicks++ }
onClick()
onClick()
println(clicks) // 2
```
Cada chamada de `onClick` atualiza a mesma variável `clicks` que o código externo vê.

---

Como uma lambda é um valor, uma função pode **retornar** uma. O tipo de retorno é um tipo função:
```kotlin
fun multiplier(factor: Int): (Int) -> Int {
    return { it * factor }
}
val triple = multiplier(3)
println(triple(5)) // 15
```
A lambda retornada captura `factor`, então cada chamada de `multiplier` constrói uma função diferente.
Funções que recebem ou retornam outras funções são chamadas de **funções de ordem superior**.

---

Uma lambda retornada pode capturar um `var` declarado dentro da função. Essa variável continua viva depois que a função retornou, e apenas a lambda pode alcançá-la: é um estado privado.
```kotlin
fun makeGreeter(): () -> String {
    var calls = 0
    return { calls++; "hello #$calls" }
}
val greeter = makeGreeter()
println(greeter()) // hello #1
println(greeter()) // hello #2
```
Cada chamada de `makeGreeter()` declara um novo `calls`, então dois greeters contam de forma independente.

---

Você pode escrever suas próprias funções de ordem superior: um parâmetro com um tipo função aceita qualquer lambda dessa forma, e dentro da função você a chama como uma função comum.
```kotlin
fun repeatTwice(text: String, transform: (String) -> String): String {
    return transform(transform(text))
}
println(repeatTwice("a", { it + "!" })) // a!!
println(repeatTwice("a") { it + "!" })  // same, with a trailing lambda
```
Colocar o parâmetro função por **último** é o que torna a sintaxe trailing lambda disponível para quem chama.

---

Quando a função de que você já precisa existe, não é necessário envolvê-la em uma lambda: uma **referência de função** `::name` transforma uma função nomeada em um valor com o tipo função correspondente.
```kotlin
fun isEven(n: Int) = n % 2 == 0
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { isEven(it) }) // [2, 4]
println(numbers.filter(::isEven))      // [2, 4], same thing
```
Funções membro são referenciadas por meio do seu tipo, como `String::uppercase`:
```kotlin
println(listOf("a", "b").map(String::uppercase)) // [A, B]
```

---

Uma **função anônima** é uma função declarada com `fun`, mas sem nome. É outra maneira de criar um valor função:
```kotlin
val square = fun(x: Int): Int {
    return x * x
}
println(square(4)) // 16
```
Diferentemente de uma lambda, ela pode declarar seu tipo de retorno explicitamente e usa `return` para produzir o valor.
Funções anônimas e lambdas são intercambiáveis: ambas podem ser passadas para `map`, `filter` ou qualquer função que receba um tipo função.

---

Funções de ordem superior podem tanto receber quanto retornar funções. Um exemplo clássico é a **composição**: construir uma nova função que executa uma função e alimenta seu resultado em outra.
```kotlin
fun andThen(first: (Int) -> Int, second: (Int) -> Int): (Int) -> Int {
    return { n -> second(first(n)) }
}
val addOneThenDouble = andThen({ it + 1 }, { it * 2 })
println(addOneThenDouble(3)) // 8
```
A lambda retornada captura tanto `first` quanto `second`, então ela continua funcionando muito depois de `andThen` ter retornado.

---

Algumas funções recebem uma **lambda com receptor**: dentro da lambda, `this` é um objeto específico, então você pode chamar seus membros diretamente sem nomeá-lo.
`buildString` é um exemplo comum: dentro de sua lambda `this` é um `StringBuilder`, então `append` pode ser chamado como se fosse uma função local:
```kotlin
val text = buildString {
    append("Hello")
    append(", ")
    append("world")
}
println(text) // Hello, world
```
O `buildString` retorna a string final. É uma alternativa conveniente a concatenar com `+` em um loop.
