Uma **função de extensão** adiciona uma nova função a um tipo existente sem tocar no seu código-fonte.
Você escreve `fun`, depois o tipo que quer estender (o **tipo receptor**), um ponto e o nome da função:
```kotlin
fun Int.squared(): Int {
    return this * this
}
println(4.squared()) // 16
```
Dentro da função, `this` é o valor sobre o qual a função é chamada, chamado de **receptor**: em `4.squared()` ele é `4`.
Uma vez que a extensão existe, você a chama com o ponto exatamente como uma função que fizesse parte de `Int` desde o início.

---

Extensões funcionam em qualquer tipo, mesmo naqueles cujo código-fonte você não tem. `String` vem da biblioteca padrão, mas você ainda pode dar novas funções a ela:
```kotlin
fun String.whisper(): String {
    return this.lowercase() + "..."
}
println("HELLO".whisper()) // hello...
```
Dentro de uma extensão você pode omitir `this.` ao usar outros membros do receptor: `lowercase()` sozinho significa `this.lowercase()`, e `length` sozinho significa `this.length`.

---

Uma função de extensão pode receber parâmetros como qualquer outra função. O receptor fica à esquerda do ponto e os parâmetros vão entre os parênteses:
```kotlin
fun Int.isDivisibleBy(other: Int): Boolean {
    return this % other == 0
}
println(12.isDivisibleBy(4)) // true
println(12.isDivisibleBy(5)) // false
```
O tipo antes do ponto é um tipo normal, então você pode estender `List<Int>`, `Double` ou uma classe que você mesmo escreveu da mesma forma.

---

Uma extensão **não** modifica a classe que estende e não insere um novo membro nela. O compilador simplesmente reescreve a chamada: `"kotlin".first3()` vira uma chamada à função com `"kotlin"` passado como `this`.
```kotlin
fun String.first3(): String = take(3)
val word = "kotlin"
println(word.first3()) // kot
```
É por isso que você pode estender classes finais como `String` e `Int`: nada dentro delas muda, a extensão vive apenas no seu código.

---

Além de funções, você pode adicionar uma **propriedade de extensão**. Ela é declarada com `val`, o tipo receptor, um ponto e o nome, seguidos de um `get()` que calcula o valor toda vez que a propriedade é lida:
```kotlin
val String.wordCount: Int
    get() = split(" ").size

println("Kotlin is fun".wordCount) // 3
```
Uma propriedade de extensão não pode armazenar nada: ela não tem campo de apoio, então um inicializador como `val String.label = "text"` é um erro de compilação. Ela só pode calcular seu valor a partir do receptor.
Propriedades de extensão não podem ser declaradas dentro de uma função (propriedades de extensão locais não são permitidas), ao contrário das funções de extensão.

---

Propriedades de extensão são lidas sem parênteses, exatamente como o `length` nativo de uma `String`. Elas são a escolha natural quando o valor descreve o receptor em vez de fazer algo com ele:
```kotlin
val Int.isNegative: Boolean
    get() = this < 0

println((-3).isNegative) // true
println(7.isNegative)    // false
```
Repare nos parênteses ao redor de `-3`: sem eles, `-3.isNegative` leria primeiro a propriedade de `3` e depois tentaria negar um `Boolean`, o que não compila.

---

O tipo receptor pode ser **nullable**. Uma extensão em `String?` pode ser chamada sobre uma variável que talvez contenha `null`, e dentro da função `this` é uma `String?`, então você mesmo trata o caso `null`, geralmente com o operador Elvis `?:` que você viu nas lições sobre nulidade:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val name: String? = null
println(name.orDash())  // -
println("Ada".orDash()) // Ada
```
Chamar `name.orDash()` sobre um valor `null` é seguro: nenhum `?.` é necessário, porque a própria função aceita um receptor `null`.

---

Dentro de uma extensão com receptor nullable você também pode usar a chamada segura `this?.` para alcançar os membros do valor apenas quando ele não for `null`. A biblioteca padrão usa a mesma ideia para funções como `isNullOrEmpty()`:
```kotlin
fun String?.firstOrQuestion(): Char {
    return this?.firstOrNull() ?: '?'
}
val text: String? = null
println(text.firstOrQuestion())    // ?
println("Kotlin".firstOrQuestion()) // K
```

---

Quando uma classe já tem um membro com o mesmo nome e os mesmos parâmetros de uma extensão, **o membro sempre vence**: a extensão nunca é chamada, e o compilador avisa que ela está sombreada.
```kotlin
class Box {
    fun describe(): String = "member"
}
fun Box.describe(): String = "extension"

println(Box().describe()) // member
```
Uma extensão não pode sobrescrever nem substituir um comportamento existente; ela só pode adicionar novas funções e propriedades. Para ser escolhida, uma extensão precisa de um nome ou de uma lista de parâmetros que a classe ainda não tenha.

---

Uma extensão pode trabalhar sobre uma família de tipos de uma vez graças a um **parâmetro de tipo**: um espaço reservado para um tipo, declarado entre colchetes angulares logo depois de `fun`, que o Kotlin preenche a cada chamada. Isso torna a extensão **genérica**:
```kotlin
fun <T> List<T>.second(): T {
    return this[1]
}
println(listOf(1, 2, 3).second())      // 2
println(listOf("a", "b").second())     // b
```
Com `listOf(1, 2, 3)` o espaço reservado `T` é `Int`, com `listOf("a", "b")` ele é `String`, então a mesma função retorna o tipo certo todas as vezes.

---

O parâmetro de tipo pode ser usado em qualquer lugar da assinatura: como tipo de retorno, como `T?` nullable, ou dentro de outro tipo. Uma extensão genérica que pode não encontrar nada retorna `T?`, como o `firstOrNull()` nativo:
```kotlin
fun <T> List<T>.lastOrDefault(default: T): T {
    return if (isEmpty()) default else this[size - 1]
}
println(listOf(1, 2).lastOrDefault(0))          // 2
println(emptyList<String>().lastOrDefault("-")) // -
```
Dentro da função você pode usar `size`, `isEmpty()` e a indexação exatamente como em qualquer lista, porque o receptor é uma `List<T>`.

---

Você também pode estender o **companion object** de uma classe, desde que a classe declare um, mesmo vazio. O tipo receptor é escrito `ClassName.Companion`, e a extensão é então chamada no nome da classe, como uma função fábrica:
```kotlin
class Temperature(val degrees: Int) {
    companion object
}
fun Temperature.Companion.freezing(): Temperature = Temperature(0)

println(Temperature.freezing().degrees) // 0
```
A classe e a extensão são ambas declarações de nível superior, então precisam ser escritas fora de `main`.

---

Uma extensão de companion pode receber parâmetros, o que a torna um lugar prático para construtores alternativos que convertem de outra unidade ou formato:
```kotlin
class Distance(val meters: Int) {
    companion object
}
fun Distance.Companion.fromKilometers(km: Int): Distance = Distance(km * 1000)

println(Distance.fromKilometers(3).meters) // 3000
```

---

Onde você declara uma extensão decide onde ela pode ser usada, o seu **escopo**:
- no nível superior de um arquivo, ela fica disponível no arquivo inteiro e no resto do pacote
- dentro de uma função, é uma extensão local, utilizável apenas naquela função
- dentro de uma classe, é uma **extensão membro**, utilizável apenas dentro daquela classe

Uma extensão membro pode ler as propriedades da classe em que vive, então ela combina dois receptores: a instância da classe e o valor sobre o qual é chamada:
```kotlin
class Greeter(val greeting: String) {
    fun String.greet(): String = "$greeting, $this!"
    fun welcome(name: String): String = name.greet()
}
println(Greeter("Hello").welcome("Ada")) // Hello, Ada!
```
Dentro de `greet`, `greeting` vem do `Greeter` e `this` é a `String` sobre a qual a função é chamada. Fora da classe, `"Ada".greet()` é um erro de compilação.

---

Uma função de extensão com exatamente **um** parâmetro pode ser marcada como `infix`. Uma função infix pode ser chamada sem o ponto e sem os parênteses, com o receptor à esquerda e o argumento à direita, o que se lê quase como uma frase:
```kotlin
infix fun Int.percentOf(total: Int): Int = total * this / 100

println(20 percentOf 50)   // 10
println(20.percentOf(50))  // 10, the normal call still works
```
O Kotlin usa isso também em algumas funções nativas: `1 to "one"` constrói um `Pair`, e `1 until 5` constrói um intervalo.

---

Para ser marcada como `infix`, uma função precisa ser um membro ou uma extensão, precisa receber exatamente um parâmetro, e esse parâmetro não pode ter valor padrão. Qualquer outra coisa é um erro de compilação:
```kotlin
infix fun Int.add(other: Int): Int = this + other          // ok
infix fun add(a: Int, b: Int): Int = a + b                 // error: not a member or extension
infix fun Int.add(a: Int, b: Int): Int = this + a + b      // error: two parameters
```
Chamadas infix ficam, em precedência, entre a aritmética e a comparação: `1 add 2 * 3` é `1 add 6`, enquanto `1 add 2 == 3` compara o resultado com `3`.
