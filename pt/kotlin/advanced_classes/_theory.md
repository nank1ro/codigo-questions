Uma `data class` é uma classe cujo trabalho é **armazenar dados**. A partir das propriedades que você declara no construtor primário, o compilador gera quatro membros para você:

- `toString()`, um texto legível no formato `ClassName(prop=value, ...)`
- `equals()` e `hashCode()`, para que duas instâncias com os mesmos dados sejam consideradas iguais
- `copy()`, que cria uma nova instância reutilizando os valores atuais

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

O `copy()` realmente brilha com **argumentos nomeados**: você nomeia apenas as propriedades que deseja alterar, e todos os outros valores são mantidos.

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

O original nunca é modificado: `copy()` retorna um objeto completamente novo.

---

Para cada propriedade no construtor primário, uma data class também gera uma função `componentN()`: `component1()` para a primeira propriedade, `component2()` para a segunda, e assim por diante.

Essas funções possibilitam as **declarações de desestruturação**, em que você desempacota um objeto em várias variáveis em uma única linha:

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

A ordem das variáveis segue a ordem das propriedades, não os seus nomes. Use `_` para pular uma que você não precisa:

```kotlin
val (_, onlyY) = point
```

---

O `equals()` gerado torna o `==` uma comparação **estrutural**: duas instâncias são iguais quando toda propriedade do construtor primário é igual. O operador `===` é diferente, ele pergunta se ambos os nomes apontam para o **mesmo objeto** na memória.

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true, mesmos dados
println(a === b) // false, dois objetos diferentes
println(a === a) // true
```

Como o `hashCode()` é gerado junto com o `equals()`, as instâncias de data class também se comportam corretamente dentro de um `Set` ou como chaves de `Map`: duplicatas colapsam.

```kotlin
println(setOf(a, b).size) // 1
```

Uma classe comum não gera nada disso, então, para ela, o `==` volta a ser a identidade.

---

Os membros gerados olham apenas para as propriedades declaradas no **construtor primário**. Uma propriedade declarada no **corpo** da classe é uma propriedade normal: ela não faz parte de `toString()`, `equals()`, `hashCode()` ou `copy()`.

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

Isso é fácil de esquecer, então coloque no construtor primário tudo o que identifica o objeto, e mantenha no corpo o estado derivado ou temporário.

---

Uma classe `sealed` descreve um conjunto **fechado** de alternativas: apenas as subclasses escritas no mesmo pacote e módulo são permitidas, então o compilador conhece todas elas.

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

A vantagem é o **`when` exaustivo**: quando você faz um branch sobre um tipo sealed e cobre todas as subclasses, pode omitir o branch `else`. Adicione uma nova subclasse mais tarde e o compilador relatará todo `when` que você esqueceu de atualizar, em vez de seguir silenciosamente o `else`.

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

Depois de `is Circle`, o valor sofre smart cast, então `shape.radius` está disponível dentro desse branch sem nenhum cast manual.

---

Às vezes você precisa de exatamente **uma** instância de algo: um logger, um registro, uma configuração de aplicação. Substituir `class` por `object` declara esse singleton para você:

```kotlin
object Registry {
    var size = 0
    fun add() {
        size++
    }
}

Registry.add()
println(Registry.size) // 1
```

A instância é criada na primeira vez que você a usa, e você usa o próprio nome, não há chamada `Registry()` nem construtor. Um `object` pode conter propriedades, métodos, blocos `init`, e pode implementar interfaces ou estender uma classe.

---

Um `companion object` é o singleton que pertence a uma classe. Além de constantes, o seu trabalho natural é armazenar **funções de fábrica**: funções que verificam ou transformam a entrada antes de construir uma instância, e que podem retornar `null` quando a entrada não faz sentido.

Marcar o construtor como `private` obriga todo chamador a passar pela fábrica:

```kotlin
class Age private constructor(val years: Int) {
    companion object {
        fun of(years: Int): Age? = if (years >= 0) Age(years) else null
    }
}

println(Age.of(30)?.years) // 30
println(Age.of(-1))        // null
```

O companion é chamado no nome da classe, `Age.of(...)`, e ele pode acessar o construtor privado porque vive dentro da classe.

---

Uma `interface` lista o que um tipo pode fazer. Os seus membros são abstratos por padrão, mas uma interface também pode fornecer uma **implementação padrão**, um corpo que toda classe implementadora herda de graça e pode sobrescrever:

```kotlin
interface Greeter {
    val name: String              // abstrata, a classe deve fornecê-la
    fun greet(): String = "Hi, $name"  // implementação padrão
}

class Person(override val name: String) : Greeter

class Robot(override val name: String) : Greeter {
    override fun greet(): String = "BEEP $name"
}

println(Person("Ann").greet()) // Hi, Ann
println(Robot("R2").greet())   // BEEP R2
```

Uma interface não pode armazenar estado (ela não tem backing fields), então uma propriedade abstrata precisa ser implementada pela classe, geralmente com `override val` no construtor. Ao contrário de uma classe, um tipo pode implementar quantas interfaces quiser.

---

Uma classe `abstract` fica entre uma interface e uma classe normal: ela não pode ser instanciada, e mistura membros **abstratos**, que não têm corpo e devem ser sobrescritos, com membros concretos que as subclasses herdam como estão.

```kotlin
abstract class Vehicle(val name: String) {
    abstract fun wheels(): Int
    fun describe(): String = "$name has ${wheels()} wheels"
}

class Bike(name: String) : Vehicle(name) {
    override fun wheels(): Int = 2
}

println(Bike("BMX").describe()) // BMX has 2 wheels
```

Ao contrário de uma interface, uma classe abstrata tem um construtor e pode armazenar estado em propriedades, e é por isso que a subclasse passa `name` para cima com `: Vehicle(name)`. Uma classe pode estender apenas uma classe, então use uma classe abstrata quando as subclasses compartilham dados, e uma interface quando elas compartilham apenas comportamento. Membros abstratos podem ser sobrescritos sem adicionar `open`.

---

Uma classe declarada dentro de outra classe é **aninhada** por padrão. Ela não sabe nada sobre a instância externa e você a constrói a partir do nome da classe externa:

```kotlin
class Outer {
    class Nested {
        fun hello() = "hi"
    }
}

println(Outer.Nested().hello()) // hi
```

Adicione a palavra-chave `inner` e a situação muda: uma classe `inner` carrega uma referência à instância externa, então ela pode ler as propriedades externas, e você a constrói **a partir de uma instância**:

```kotlin
class Counter(val step: Int) {
    inner class Doubler {
        fun value() = step * 2
    }
}

println(Counter(5).Doubler().value()) // 10
```

Dentro de uma classe `inner`, `this` é o objeto interno; use `this@Counter` quando precisar do externo explicitamente.

---

As peças deste tópico geralmente são combinadas: uma `enum class` cujas entradas carregam as suas próprias propriedades modela um conjunto fixo de etiquetas, enquanto uma `data class` carrega o payload que as acompanha.

```kotlin
enum class Speed(val surcharge: Int) {
    STANDARD(0),
    EXPRESS(15)
}

data class Order(val total: Int, val speed: Speed)

val order = Order(100, Speed.EXPRESS)
println(order.total + order.speed.surcharge) // 115
```
