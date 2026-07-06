Uma **classe** é um modelo para criar objetos. Em Kotlin, você declara uma classe com a palavra-chave `class` seguida do nome da classe.

Uma classe pode conter **propriedades** (dados) e **métodos** (comportamento). Para declarar uma propriedade diretamente no construtor, use o prefixo `val` ou `var`:

```kotlin
class Dog(val name: String)
```

Isso cria uma classe `Dog` com uma propriedade `name`. Você cria uma instância chamando a classe como uma função:

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

Classes podem ter várias propriedades em seu **construtor primário**. Cada propriedade é declarada com `val` (somente leitura) ou `var` (mutável) diretamente na lista de parâmetros do construtor:

```kotlin
class Person(val name: String, var age: Int)
```

A palavra-chave `val` torna `name` somente leitura após a criação, enquanto `var` torna `age` mutável — você pode alterá-lo depois:

```kotlin
val p = Person("Alice", 30)
p.age = 31  // permitido porque age é var
```

---

O **bloco `init`** é executado imediatamente após o construtor primário. É usado para realizar validações ou lógica de configuração quando um objeto é criado:

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "O raio deve ser positivo" }
    }
}
```

Você também pode inicializar propriedades adicionais dentro do `init`:

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

Classes podem conter **métodos** — funções que pertencem à classe e operam sobre suas propriedades:

```kotlin
class Counter(var count: Int) {
    fun increment() {
        count++
    }
    fun value(): Int {
        return count
    }
}
```

Os métodos são chamados usando a notação de ponto em uma instância:

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

Uma **`data class`** é uma classe especial projetada para armazenar dados. O Kotlin gera automaticamente `equals()`, `hashCode()`, `toString()` e `copy()` para você:

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)           // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

A função `copy()` cria uma nova instância com algumas propriedades alteradas:

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
