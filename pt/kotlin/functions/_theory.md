Uma função é um bloco de código que realiza uma tarefa específica e pode ser reutilizado ao longo do seu programa.
Em Kotlin, você define uma função usando a palavra-chave `fun`, seguida do nome da função e parênteses:
```kotlin
fun greet() {
    println("Hello!")
}
```
Para chamar (executar) uma função, use seu nome seguido de parênteses:
```kotlin
greet() // prints Hello!
```
Uma função que não retorna um valor retorna implicitamente `Unit`.

---

Funções podem retornar um valor. Você especifica o tipo de retorno após os parênteses usando dois pontos:
```kotlin
fun getNumber(): Int {
    return 42
}
```
A palavra-chave `return` envia um valor de volta ao chamador:
```kotlin
var result = getNumber()
println(result) // prints 42
```
O tipo de retorno deve corresponder ao tipo do valor que você retorna.

---

Funções podem aceitar parâmetros, que são entradas que você passa ao chamar a função.
Os parâmetros são declarados dentro dos parênteses com um nome e tipo:
```kotlin
fun greet(name: String) {
    println("Hello, $name!")
}
```
Você passa argumentos ao chamar a função:
```kotlin
greet("Alice") // prints Hello, Alice!
```
Os parâmetros permitem escrever código reutilizável que funciona com valores diferentes.

---

Kotlin suporta valores padrão de parâmetros. Se o chamador não fornecer um argumento, o valor padrão é usado:
```kotlin
fun greet(name: String = "World") {
    println("Hello, $name!")
}
greet()         // prints Hello, World!
greet("Alice")  // prints Hello, Alice!
```
Os valores padrão tornam os parâmetros opcionais, reduzindo a necessidade de funções sobrecarregadas.

---

Quando o corpo de uma função consiste em uma única expressão, você pode usar a sintaxe de expressão única com `=`:
```kotlin
fun square(n: Int): Int = n * n
```
Isso é mais conciso do que a forma de corpo em bloco. O Kotlin geralmente pode inferir o tipo de retorno, então você também pode escrever:
```kotlin
fun square(n: Int) = n * n
```
Funções de expressão única são um idioma Kotlin comum para computações simples.

---

Funções podem retornar valores `Boolean`, o que é útil para verificar condições:
```kotlin
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
println(isEven(4)) // prints true
println(isEven(7)) // prints false
```
Uma função `Boolean` retorna `true` ou `false`.

---

Funções podem ter múltiplos parâmetros de tipos diferentes:
```kotlin
fun introduce(name: String, age: Int): String {
    return "My name is $name and I am $age years old."
}
println(introduce("Bob", 30))
// prints My name is Bob and I am 30 years old.
```
Argumentos nomeados permitem passar valores em qualquer ordem usando o nome do parâmetro:
```kotlin
println(introduce(age = 30, name = "Bob"))
```

---

Uma função básica em Kotlin usa a palavra-chave `fun` seguida de um nome e parênteses:
```kotlin
fun sayBye() {
    println("Bye!")
}
```

---

Para declarar um tipo de retorno para uma função, adicione dois pontos e o tipo após os parênteses:
```kotlin
fun getName(): String {
    return "Alice"
}
```

---

Um parâmetro de função é declarado com um nome, dois pontos e um tipo:
```kotlin
fun greet(name: String) {
    println("Hi, $name!")
}
```

---

Uma função de expressão única usa `=` em vez de um corpo em bloco:
```kotlin
fun triple(n: Int) = n * 3
```
Esta é uma abreviação para:
```kotlin
fun triple(n: Int): Int {
    return n * 3
}
```
