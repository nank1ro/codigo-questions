Uma **enumeração** (ou *enum*) define um tipo comum para um grupo de valores relacionados, para que você possa trabalhar com esses valores de forma segura em relação ao tipo.
Em Kotlin você declara uma com as palavras-chave `enum class`, listando suas **entradas** separadas por vírgulas:
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
Por convenção, os nomes das entradas são escritos em maiúsculas. Cada entrada é um valor do tipo enum e é acessada através do nome da classe:
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
Classes enum devem ser declaradas no nível superior de um arquivo (ou dentro de outra classe), nunca dentro de uma função.

---

Toda entrada de enum tem duas propriedades embutidas:

- `name` é o nome da entrada como `String`
- `ordinal` é sua posição na declaração, começando em `0`

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

Entradas de enum são comparadas com `==`:
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

Uma expressão `when` é a forma natural de ramificar sobre um enum. Quando ela cobre **todas** as entradas, é *exaustiva* e não precisa de um ramo `else`:
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
Se você esquecer uma entrada, o compilador reporta um erro em vez de deixar o bug chegar em tempo de execução.

---

Uma classe enum pode ter um **construtor**, assim como uma classe comum. Cada entrada então passa seus próprios argumentos, e os valores são armazenados em propriedades:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
As propriedades do construtor geralmente são declaradas com `val`, já que os dados de uma entrada não devem mudar.

---

Classes enum também podem declarar **métodos**. A lista de entradas deve ser encerrada com um ponto e vírgula `;` antes de qualquer declaração de membro:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2);

    fun hasMoons(): Boolean {
        return moons > 0
    }
}
println(Planet.EARTH.hasMoons()) // true
```
Dentro de um método você pode acessar as propriedades da entrada, assim como `name` e `ordinal`.

---

Toda classe enum expõe uma propriedade `entries`: uma lista de todas as suas entradas na ordem de declaração. É útil para iterar:
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
Por ser uma lista, `entries` também suporta `size` e indexação, por exemplo `Direction.entries[0]` é `NORTH`.

Código mais antigo usa a função `values()` em vez disso, que retorna um array; `entries` é a escolha recomendada desde o Kotlin 1.9.

---

Para ir de uma `String` de volta a uma entrada, use a função `valueOf`. Ela procura a entrada cujo `name` corresponde exatamente:
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
A correspondência diferencia maiúsculas de minúsculas: `Direction.valueOf("east")` lança uma `IllegalArgumentException` porque nenhuma entrada tem esse nome.

---

Uma classe enum pode declarar um **método abstrato** e deixar que cada entrada forneça sua própria implementação em um corpo delimitado por chaves:
```kotlin
enum class Operation {
    ADD {
        override fun apply(a: Int, b: Int): Int = a + b
    },
    SUBTRACT {
        override fun apply(a: Int, b: Int): Int = a - b
    };

    abstract fun apply(a: Int, b: Int): Int
}
println(Operation.ADD.apply(2, 3)) // 5
```
Cada entrada se comporta de forma diferente, mas ainda compartilha o mesmo tipo e a mesma assinatura de método.

---

Uma **interface** declara métodos sem corpo; qualquer tipo que a implemente deve fornecê-los:
```kotlin
interface Greeter {
    fun greet(): String
}
```
Classes enum podem implementar interfaces. Você lista a interface depois de dois pontos e marca cada implementação com `override`. Dentro do corpo do enum, a entrada atual é `this` e outras entradas podem ser referenciadas sem o nome da classe:
```kotlin
enum class Language : Greeter {
    ENGLISH, ITALIAN;

    override fun greet(): String = when (this) {
        ENGLISH -> "Hello"
        ITALIAN -> "Ciao"
    }
}
println(Language.ITALIAN.greet()) // Ciao
```
