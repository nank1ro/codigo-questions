Una función es un bloque de código que realiza una tarea específica y puede reutilizarse en todo el programa.
En Kotlin, se define una función usando la palabra clave `fun`, seguida del nombre de la función y paréntesis:
```kotlin
fun greet() {
    println("Hello!")
}
```
Para llamar (ejecutar) una función, usa su nombre seguido de paréntesis:
```kotlin
greet() // prints Hello!
```
Una función que no devuelve un valor devuelve implícitamente `Unit`.

---

Las funciones pueden devolver un valor. Se especifica el tipo de retorno después de los paréntesis usando dos puntos:
```kotlin
fun getNumber(): Int {
    return 42
}
```
La palabra clave `return` envía un valor de vuelta al llamador:
```kotlin
var result = getNumber()
println(result) // prints 42
```
El tipo de retorno debe coincidir con el tipo del valor que devuelves.

---

Las funciones pueden aceptar parámetros, que son entradas que se pasan al llamar a la función.
Los parámetros se declaran dentro de los paréntesis con un nombre y un tipo:
```kotlin
fun greet(name: String) {
    println("Hello, $name!")
}
```
Se pasan argumentos al llamar a la función:
```kotlin
greet("Alice") // prints Hello, Alice!
```
Los parámetros permiten escribir código reutilizable que trabaja con diferentes valores.

---

Kotlin admite valores de parámetros predeterminados. Si un llamador no proporciona un argumento, se usa el valor predeterminado:
```kotlin
fun greet(name: String = "World") {
    println("Hello, $name!")
}
greet()         // prints Hello, World!
greet("Alice")  // prints Hello, Alice!
```
Los valores predeterminados hacen que los parámetros sean opcionales, reduciendo la necesidad de funciones sobrecargadas.

---

Cuando el cuerpo de una función consiste en una sola expresión, puedes usar la sintaxis de expresión única con `=`:
```kotlin
fun square(n: Int): Int = n * n
```
Esto es más conciso que la forma de cuerpo de bloque. Kotlin a menudo puede inferir el tipo de retorno, por lo que también puedes escribir:
```kotlin
fun square(n: Int) = n * n
```
Las funciones de expresión única son un modismo común de Kotlin para cálculos simples.

---

Las funciones pueden devolver valores `Boolean`, lo cual es útil para verificar condiciones:
```kotlin
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
println(isEven(4)) // prints true
println(isEven(7)) // prints false
```
Una función `Boolean` devuelve `true` o `false`.

---

Las funciones pueden tener múltiples parámetros de diferentes tipos:
```kotlin
fun introduce(name: String, age: Int): String {
    return "My name is $name and I am $age years old."
}
println(introduce("Bob", 30))
// prints My name is Bob and I am 30 years old.
```
Los argumentos con nombre permiten pasar valores en cualquier orden usando el nombre del parámetro:
```kotlin
println(introduce(age = 30, name = "Bob"))
```

---

Una función básica en Kotlin usa la palabra clave `fun` seguida de un nombre y paréntesis:
```kotlin
fun sayBye() {
    println("Bye!")
}
```

---

Para declarar un tipo de retorno para una función, agrega dos puntos y el tipo después de los paréntesis:
```kotlin
fun getName(): String {
    return "Alice"
}
```

---

Un parámetro de función se declara con un nombre, dos puntos y un tipo:
```kotlin
fun greet(name: String) {
    println("Hi, $name!")
}
```

---

Una función de expresión única usa `=` en lugar de un cuerpo de bloque:
```kotlin
fun triple(n: Int) = n * 3
```
Esto es una forma abreviada de:
```kotlin
fun triple(n: Int): Int {
    return n * 3
}
```
