Uma **exceção** é a maneira do Kotlin de relatar que uma instrução não pode ser realizada. Converter `"abc"` em um número, dividir um inteiro por zero ou ler além do fim de uma lista todas lançam uma.

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
Este programa imprime `before` e depois para. `toInt()` não consegue ler `"abc"`, então ele **lança** uma `NumberFormatException`; nada no programa trata isso, então o Kotlin encerra o programa com um relatório de erro e `after` nunca é impresso.

Você também pode lançar uma exceção você mesmo com a palavra-chave `throw`:
```kotlin
throw Exception("something went wrong")
```

Uma exceção que ninguém trata não é um aviso: é o fim da execução.

---

Para manter o programa vivo, coloque a instrução arriscada dentro de um bloco `try` e descreva a recuperação em um bloco `catch`:
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
O Kotlin executa o bloco `try`; assim que uma instrução dentro dele lança, o restante do bloco é ignorado e o controle salta para o bloco `catch`. O nome entre parênteses — `e` aqui — é o objeto da exceção, e `Exception` é o tipo que está sendo capturado.

Depois que o bloco `catch` termina, o programa continua normalmente com a linha depois de todo o `try`/`catch`.

---

Capturar `Exception` captura tudo, o que raramente é o que você quer: um erro de digitação em outro lugar do bloco também seria engolido. Em vez disso, nomeie o **tipo exato** do qual você sabe se recuperar.

Cada falha tem seu próprio tipo. `"abc".toInt()` lança uma `NumberFormatException`, então esse é o tipo a ser capturado:
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
Se um tipo diferente de exceção for lançado dentro do bloco, este `catch` não corresponde e a exceção continua viajando para fora da função.

---

Um `try` pode ser seguido por vários blocos `catch`, cada um tratando um tipo diferente:
```kotlin
val letters = listOf("a", "b")
val index = 5
val text = "abc"
try {
    println(letters[index] + text.toInt())
} catch (e: NumberFormatException) {
    println("not a number")
} catch (e: IndexOutOfBoundsException) {
    println("no such letter")
} catch (e: Exception) {
    println("something else went wrong")
}
```
O Kotlin testa os blocos **de cima para baixo** e executa o primeiro cujo tipo corresponde. Apenas um bloco é executado.

A ordem, portanto, importa. `NumberFormatException` e `IndexOutOfBoundsException` são ambos tipos de `Exception`, então um `catch (e: Exception)` escrito primeiro corresponderia a todas as falhas e os blocos abaixo dele nunca seriam executados. Escreva o tipo mais específico primeiro e o mais geral por último.

---

Um bloco `finally` pode ser adicionado no final. Ele executa **independente do que aconteça**: depois de um `try` bem-sucedido, depois de um `catch` ter recuperado, e até mesmo quando a exceção não é capturada de forma alguma.

```kotlin
try {
    println("reading")
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("bad number")
} finally {
    println("closing")
}
```
```
reading
bad number
closing
```
Isso faz dele o lugar para limpeza que não deve ser ignorada, como fechar um arquivo. Um `try` precisa de pelo menos um `catch` ou um `finally`, mas pode ter ambos.

---

No Kotlin, `try` não é apenas uma instrução: é uma **expressão** que produz um valor. O valor é a última expressão do bloco que executou — o bloco `try` quando nada falhou, o bloco `catch` quando falhou.

```kotlin
val n = try { "abc".toInt() } catch (e: NumberFormatException) { 0 }
println(n) // 0
```
Esta é a forma idiomática no Kotlin. Em vez de declarar uma `var`, atribuí-la em dois lugares e torcer para que todos os caminhos a definam, você obtém um único `val` que sempre contém um valor utilizável.

Note que um bloco `finally` nunca muda o valor: ele executa apenas pelos seus efeitos colaterais.

---

Como `try` é uma expressão, ele pode ser usado em qualquer lugar onde um valor é esperado — inclusive como o corpo inteiro de uma função escrita com `=`:
```kotlin
fun length(text: String): Int = try {
    text.toInt()
} catch (e: NumberFormatException) {
    -1
}
```
Ambos os blocos devem produzir um valor do mesmo tipo, aqui `Int`. Escreva o valor alternativo como a última expressão do bloco `catch`; não há `return` dentro de nenhum dos blocos.

---

Lançar e capturar não é gratuito, e para as conversões comuns o Kotlin oferece uma variante mais barata que simplesmente retorna `null` em vez de lançar: `toIntOrNull()`, `toDoubleOrNull()`, `toLongOrNull()`.

```kotlin
println("42".toIntOrNull())  // 42
println("abc".toIntOrNull()) // null
```
Combinado com o operador elvis `?:`, que fornece um substituto quando o valor à sua esquerda é `null`, todo o `try`/`catch` colapsa em uma linha:
```kotlin
val n = "abc".toIntOrNull() ?: 0
println(n) // 0
```
Use `try`/`catch` quando a falha for genuinamente excepcional; use `toIntOrNull()` quando uma entrada inválida é esperada.

---

Suas próprias funções podem recusar entradas inválidas da mesma maneira que a biblioteca padrão faz, com `throw`. A biblioteca já fornece um tipo para o caso mais comum: `IllegalArgumentException` significa "o valor que você me passou não é aceitável".

```kotlin
fun half(n: Int): Int {
    if (n < 0) throw IllegalArgumentException("n must not be negative")
    return n / 2
}
```
`throw` encerra a função imediatamente — o `return` abaixo dele nunca é alcançado. Quem chama decide o que fazer com isso:
```kotlin
try { println(half(-4)) }
catch (e: IllegalArgumentException) { println("rejected") }
```
Lançar é melhor do que retornar discretamente um valor inventado: uma resposta errada viaja longe, uma exceção para no primeiro chamador que está pronto para tratá-la.

---

Toda exceção carrega o texto com o qual foi criada. Dentro de um bloco `catch` você a lê por meio da propriedade `message` do objeto da exceção:
```kotlin
try {
    throw IllegalArgumentException("price must be positive")
} catch (e: IllegalArgumentException) {
    println(e.message) // price must be positive
}
```
`message` é nullable, porque uma exceção pode ser construída sem nenhum texto; `e.message ?: "unknown"` fornece um substituto seguro quando você precisa de um `String` simples.

Prefira imprimir `e.message` a imprimir o objeto da exceção em si: o texto do próprio objeto também inclui o nome da classe, o que é ruído para quem lê a saída.

---

Escrever `if (...) throw IllegalArgumentException(...)` em cada argumento fica barulhento, então o Kotlin fornece duas abreviações que se leem como frases simples:

```kotlin
require(n >= 0) { "n must not be negative" }   // lança IllegalArgumentException
check(started) { "not started" }               // lança IllegalStateException
```
Ambas recebem uma condição e um bloco que produz a mensagem, e ambas lançam **quando a condição é falsa**. A única diferença é o tipo da exceção, e essa diferença é uma mensagem para o leitor:

* `require` protege os **argumentos** que quem chamou passou, e falha com `IllegalArgumentException`.
* `check` protege o **estado** do objeto ou programa, e falha com `IllegalStateException`.

O bloco só é avaliado quando a verificação falha, então construir a mensagem não custa nada no caminho feliz.

---

Quando nenhum dos tipos embutidos descreve bem a sua falha, declare a sua própria. Uma exceção é uma classe comum que estende `Exception` e entrega seu texto ao pai:

```kotlin
class InsufficientFundsException(message: String) : Exception(message)
```
Essa única linha é um tipo de exceção completo. Ela é lançada e capturada como qualquer outra, e `e.message` retorna o texto com o qual foi construída:
```kotlin
try {
    throw InsufficientFundsException("balance too low")
} catch (e: InsufficientFundsException) {
    println(e.message) // balance too low
}
```
O ganho é a precisão: quem chama pode capturar apenas `InsufficientFundsException` e deixar toda outra falha seguir em frente.

---

`runCatching` executa um bloco e nunca deixa uma exceção escapar. Em vez disso, ele devolve um `Result`, um objeto que contém **ou** o valor que o bloco produziu **ou** a exceção que ele lançou:

```kotlin
val ok = runCatching { "42".toInt() }
val bad = runCatching { "abc".toInt() }

println(ok.isSuccess)   // true
println(bad.isFailure)  // true
```
O valor é lido depois, e você escolhe o que uma falha deve se tornar:
```kotlin
println(ok.getOrNull())      // 42
println(bad.getOrNull())     // null
println(bad.getOrElse { 0 }) // 0
```
`getOrNull()` transforma uma falha em `null`, enquanto `getOrElse { ... }` executa o bloco para construir um substituto. Nada é lançado no ponto da chamada, então a falha pode ser carregada e tratada mais tarde.

---

Como um `Result` é um valor comum, ele pode ser armazenado em um `val` e consultado quantas vezes você quiser:

```kotlin
val result = runCatching { "abc".toInt() }

println(result.getOrElse { 0 })  // 0
println(result.getOrNull())      // null
println(result.isSuccess)        // false
```
Um `try`/`catch` não consegue fazer isso. Ali o resultado é tratado uma única vez, no momento da falha, e depois desaparece. Um `Result` mantém a falha guardada, então o código que reage a ela não precisa estar onde ela aconteceu.

---

Um `Result` também pode ser inspecionado sem ser desembrulhado. `onFailure` executa seu bloco apenas quando o resultado contém uma exceção, `onSuccess` apenas quando contém um valor, e **ambos devolvem o mesmo `Result`** para que as chamadas possam ser encadeadas:

```kotlin
runCatching { "abc".toInt() }
    .onFailure { println("could not read it") }
    .onSuccess { println("read $it") }
```
Dentro do bloco a exceção (ou o valor) está disponível como `it`, então `it.message` é o texto da falha.

Esta é a forma de "registrar e continuar": relate o problema onde ele aconteceu, depois siga em frente, sem um `return` antecipado e sem uma `var` definida a partir de dois lugares.

---

Onde o `try` está posicionado decide quanto trabalho um único valor inválido destrói. Envolva o **loop inteiro** e a primeira falha abandona o restante do lote; envolva o **corpo** e apenas aquele elemento é perdido:

```kotlin
var total = 0
for (value in listOf("3", "x", "5")) {
    try {
        total += value.toInt()
    } catch (e: NumberFormatException) {
        // pula este
    }
}
println(total) // 8
```
Isso combina naturalmente com uma função de validação que lança: a função declara uma regra e recusa qualquer coisa que a viole, e o loop decide que uma recusa custa apenas um elemento.
