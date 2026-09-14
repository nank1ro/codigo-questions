**Funções de escopo** executam um bloco de código *dentro do contexto de um objeto*. Elas não adicionam recursos novos à linguagem: apenas tornam o código que trabalha sobre um objeto mais curto e mais fácil de ler. O Kotlin tem cinco delas: `let`, `run`, `with`, `apply` e `also`.

Elas diferem em apenas **dois** pontos: como o objeto é referenciado dentro do bloco e o que a chamada devolve. Começamos com `let`: dentro do seu bloco o objeto é chamado de `it`, e a chamada retorna o **resultado da última expressão** do bloco.
```kotlin
val word = "kotlin"
val letters = word.let { it.length } // 6
println(letters)
```
Sem `let` você precisaria de uma variável temporária; com ele o objeto fica disponível sob o nome curto `it` enquanto o bloco durar.

---

Como `let` retorna o valor da sua última expressão, é uma forma prática de **transformar um valor em outra coisa** sem nomear uma variável intermediária:
```kotlin
val price = 12
val label = price.let { "$it EUR" }
println(label) // 12 EUR
```
Dentro do bloco você pode usar `it` quantas vezes precisar:
```kotlin
println("kiwi".let { "${it.uppercase()} has ${it.length} letters" })
// KIWI has 4 letters
```

---

`let` se torna realmente útil depois de uma chamada segura. `?.let { ... }` executa o bloco **apenas** quando o valor não é `null`, e dentro do bloco `it` é um valor não nulo, então nenhuma verificação extra é necessária:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to ${it.uppercase()}") }
```
Quando o valor é `null`, a expressão inteira é `null` e o bloco nunca executa, então o operador Elvis `?:` é o parceiro natural para fornecer um fallback:
```kotlin
fun label(city: String?): String {
    return city?.let { "City: $it" } ?: "No city"
}
```

---

Dentro de um bloco `let` você não é obrigado a chamar o objeto de `it`: você pode dar um nome ao parâmetro da lambda, o que mantém o código legível quando há blocos aninhados ou quando `it` não diria nada de útil.
```kotlin
val price: Int? = 12
println(price?.let { amount -> "$amount EUR" }) // 12 EUR
```
A mesma nomeação funciona para todas as funções de escopo que usam `it`, ou seja, para `let` e `also`.

---

`apply` avança nos dois eixos ao mesmo tempo: dentro do seu bloco o objeto é o receptor `this` (então seus membros podem ser usados **sem nenhum prefixo**), e a chamada retorna **o próprio objeto**, não o resultado do bloco.

Essa combinação faz de `apply` a ferramenta para **configurar** um objeto bem no momento em que você o cria:
```kotlin
class Server {
    var host = "localhost"
    var port = 80
}

val server = Server().apply {
    host = "example.com"
    port = 8080
}
println("${server.host}:${server.port}") // example.com:8080
```
`host` e `port` dentro do bloco são `this.host` e `this.port`; como `apply` devolve o `Server` configurado, ele pode ser atribuído imediatamente.

---

`apply` não se limita a objetos que você acabou de criar: funciona sobre qualquer objeto, e como devolve o próprio objeto você pode usar a expressão inteira onde quer que o objeto seja esperado.
```kotlin
val box = Box()
box.apply { label = "tools" }        // changes box and returns it
println(listOf(Box().apply { label = "nails" }).size) // 1
```
O bloco é um bloco de código normal, então pode conter quantas instruções você precisar.

---

`also` é a imagem espelhada de `apply`: o objeto é referenciado como `it`, e a chamada retorna **o próprio objeto**. Como o resultado do bloco é descartado, `also` serve para **efeitos colaterais**, como registrar logs ou fazer verificações, e pode ser inserido no meio de uma cadeia sem mudar o que ela produz:
```kotlin
val total = listOf(1, 2, 3)
    .also { println("size: ${it.size}") } // size: 3
    .sum()
println(total) // 6
```
Leia-o como *"e também faça isto com ele"*: o valor continua fluindo para o próximo passo intacto.

---

Quando o bloco precisa do objeto como **argumento** de outra coisa, `also` fica mais legível que `apply`: `it` pode ser entregue diretamente, enquanto `this` teria de ser escrito por extenso.
```kotlin
val names = mutableListOf<String>()
val user = "ada".also { names.add(it) }
println(user)  // ada
println(names) // [ada]
```
O valor da expressão continua sendo `"ada"`: `also` apenas o observa passar.

---

`run` é o `let` com a outra forma de nomear o objeto: dentro do bloco o objeto é `this`, então os seus membros não precisam de prefixo, e a chamada retorna o **resultado da última expressão**.

Ele se encaixa quando você lê vários membros do mesmo objeto para calcular um valor:
```kotlin
class Rect(val w: Int, val h: Int)

val area = Rect(3, 4).run { w * h }
println(area) // 12
```
Compare-o com `apply`, que usa `this` exatamente da mesma forma, mas devolve o objeto em vez do resultado do bloco.

---

`with` faz o mesmo trabalho que `run`, mas **não** é uma extensão: o objeto é passado como o primeiro argumento em vez de ser o receptor de uma chamada com ponto.
```kotlin
val text = with(StringBuilder()) {
    append("Hello")
    append(", world")
    toString()
}
println(text) // Hello, world
```
Dentro do bloco o objeto é `this` e a chamada retorna a última expressão, exatamente como `run`. Prefira `with` quando você já tem um objeto não nulo e quer agrupar várias chamadas sobre ele; prefira `run` quando o objeto sai de uma cadeia ou pode precisar de uma chamada segura (`obj?.run { ... }`).

---

Todas as cinco funções de escopo estão agora sobre a mesa, e cada uma é apenas um ponto nos dois eixos:
- `let` - o objeto é `it`, retorna o resultado do bloco
- `run` - o objeto é `this`, retorna o resultado do bloco
- `with` - o objeto é `this` (passado como argumento), retorna o resultado do bloco
- `apply` - o objeto é `this`, retorna o objeto
- `also` - o objeto é `it`, retorna o objeto

Escolha a linha de que precisa: `it` fica mais legível quando você passa o objeto adiante para outra coisa, `this` fica mais legível quando você acessa muitos dos seus membros; retorne o resultado do bloco quando quiser um novo valor, retorne o objeto quando quiser continuar trabalhando com ele.
