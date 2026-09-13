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
println(a == b)  // true, same data
println(a === b) // false, two different objects
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
