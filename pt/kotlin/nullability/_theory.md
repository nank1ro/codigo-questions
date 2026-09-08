Às vezes um valor está simplesmente ausente: um usuário sem nome do meio, uma busca que não encontra nada, um texto que não pode ser convertido em número.
O Kotlin representa um valor ausente com `null`, mas uma variável comum nunca pode contê-lo. Todos os tipos são **não nulos** por padrão:
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
Para permitir um valor ausente, você declara um tipo **nullable** adicionando um ponto de interrogação `?` depois do tipo.
Um `String?` contém um `String` ou `null`:
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String` e `String?` são dois tipos diferentes: um `String` nunca está ausente, um `String?` pode estar.

---

A diferença entre `String` e `String?` é verificada pelo **compilador**, não em tempo de execução.
Atribuir `null` a um tipo não nulo, ou passar um valor nullable onde um não nulo é esperado, é um erro de compilação, então o programa nem chega a iniciar:
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
É assim que o Kotlin evita as falhas de "null pointer" comuns em outras linguagens: um valor só pode estar ausente onde você o declarou explicitamente com `?`.

---

O `?` funciona em qualquer lugar onde um tipo é escrito: uma função pode aceitar um parâmetro nullable e pode retornar um valor nullable.
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
Você não pode chamar um método diretamente em um valor nullable, porque ele pode ser `null`.
O operador de **chamada segura** `?.` chama o método apenas quando o valor não é `null`; caso contrário, a expressão inteira é `null`:
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
O resultado de uma chamada segura é sempre nullable: `word?.length` é um `Int?`, não um `Int`.

---

Muitas vezes, tudo o que você quer de um valor nullable é o próprio valor ou um padrão.
O **operador Elvis** `?:` faz exatamente isso: ele retorna o lado esquerdo quando não é `null`, caso contrário o valor à sua direita:
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
Como o lado direito é usado apenas quando o lado esquerdo é `null`, o resultado é não nulo quando o padrão o é.
O `?:` combina bem com o `?.` para transformar uma chamada segura de volta em um valor simples:
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

Chamadas seguras podem ser **encadeadas**: assim que um elo é `null`, o restante da cadeia é pulado e a expressão inteira se torna `null`.
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
Uma cadeia que termina com `?:` lhe dá um resultado não nulo em uma linha:
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

Cadeias de chamadas seguras brilham com objetos aninhados, onde qualquer nível pode estar ausente:
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
Cada `?.` protege o passo seguinte, e o `?:` final fornece o padrão.

---

O operador de **asserção não nula** `!!` converte um valor nullable em um não nulo, dizendo ao compilador "tenho certeza de que isto não é `null`":
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
Se você estiver errado e o valor for `null`, o programa falha em tempo de execução com um `NullPointerException`, exatamente o erro que o Kotlin foi projetado para evitar:
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
Use `!!` apenas quando o valor realmente não puder ser `null`; prefira `?.`, `?:` e verificações de nulo em todos os outros lugares.

---

Quando você verifica um valor quanto a `null` com `if`, o compilador lembra disso: dentro do ramo onde o valor é sabidamente não nulo, ele sofre um **smart cast** para o tipo não nulo e você pode usá-lo diretamente, sem `?.` ou `!!`:
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
O mesmo acontece depois de uma saída antecipada:
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
Smart casts funcionam em variáveis `val` e parâmetros de função, cujo valor não pode mudar entre a verificação e o uso.

---

O `let` executa um bloco de código com o valor sobre o qual é chamado, disponível dentro do bloco como `it`.
Combinado com uma chamada segura, o `?.let` executa o bloco **apenas** quando o valor não é `null`, e dentro do bloco `it` é não nulo:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
É uma alternativa compacta a `if (x != null) { ... }` quando você só precisa do valor dentro do bloco.

---

O `let` também **retorna** o valor da última expressão em seu bloco, então o `?.let` pode transformar um valor nullable e o `?:` pode preencher o padrão quando ele é `null`:
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
Quando `price` é `null`, o bloco `let` é pulado, a expressão é `null` e o operador Elvis retorna `"free"`.

---

Coleções também podem conter elementos nullable: uma `List<Int?>` pode conter entradas `null`, enquanto uma `List<Int>` nunca contém.
O `filterNotNull()` retorna uma nova lista com as entradas `null` removidas, e o tipo de seus elementos se torna não nulo, então você pode usar os elementos livremente:
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

Muitas funções padrão retornam `null` em vez de falhar. A `toIntOrNull()` converte uma string em um `Int`, ou retorna `null` quando o texto não é um número inteiro:
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
O `mapNotNull` transforma cada elemento como o `map`, mas descarta os resultados que são `null`:
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

Às vezes, uma propriedade não pode receber um valor quando o objeto é criado, mas você sabe que ela será definida antes de ser usada.
Em vez de torná-la nullable, marque-a com `lateinit`: o tipo permanece não nulo e nenhum `?.` é necessário ao lê-la:
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
O `lateinit` tem algumas regras: funciona apenas em propriedades `var`, apenas com tipos não nulos, e não com tipos primitivos como `Int` ou `Boolean`.
Ler uma propriedade `lateinit` antes de atribuí-la lança uma `UninitializedPropertyAccessException`; você pode verificá-la antes com `::player.isInitialized`.

---

Quando um `null` significa que quem chamou cometeu um erro, falhe cedo com `requireNotNull`.
Ele retorna o valor como não nulo quando ele está presente, e lança uma `IllegalArgumentException` quando ele é `null`, com uma mensagem opcional:
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
Depois da chamada, o compilador também faz um smart cast do próprio `name` para `String`, então `name.length` é permitido a partir dessa linha.
Diferente do `!!`, a falha carrega uma mensagem clara e indica que o *argumento* estava errado.

---

Uma função de extensão pode ser declarada com um **receptor nullable**, então ela pode ser chamada mesmo em um valor `null`. Dentro dela, `this` é nullable e deve ser verificado:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
Note que nenhum `?.` é necessário no ponto de chamada: a própria função trata o caso `null`.
A biblioteca padrão usa esse truque em `isNullOrEmpty()` e `orEmpty()`, que podem ser chamadas com segurança em qualquer `String?`.

---

O lado direito de `?:` pode ser qualquer expressão, incluindo `return`. Isso oferece uma forma compacta de abandonar uma função assim que um valor está ausente:
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
Todas as ferramentas que você viu combinam bem: parâmetros nullable e tipos de retorno descrevem *onde* um valor pode estar ausente, e `?.`, `?:`, `let`, smart casts e `toIntOrNull` o tratam sem nunca falhar.
