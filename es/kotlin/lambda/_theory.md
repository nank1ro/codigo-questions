Una **lambda** es una función pequeña sin nombre, escrita directamente como una expresión entre llaves.
Los parámetros van primero, después una flecha `->`, y después el cuerpo:
```kotlin
val add = { a: Int, b: Int -> a + b }
```
Una lambda es un valor como cualquier otro: puedes almacenarla en una variable y llamarla más tarde con paréntesis, exactamente como una función:
```kotlin
println(add(2, 3)) // 5
```
Una lambda sin parámetros no tiene flecha alguna: `val hello = { println("Hello!") }`.

---

Toda lambda tiene un **tipo de función**, escrito como los tipos de los parámetros entre paréntesis, una flecha y el tipo de retorno.
La lambda `{ a: Int, b: Int -> a + b }` tiene el tipo `(Int, Int) -> Int`: recibe dos valores `Int` y devuelve un `Int`.
Cuando declaras el tipo de función en la variable, los tipos de los parámetros dentro de la lambda se pueden omitir porque el compilador ya los conoce:
```kotlin
val add: (Int, Int) -> Int = { a, b -> a + b }
val greet: (String) -> Unit = { name -> println("Hi, $name") }
```
Una lambda que no devuelve nada tiene el tipo de retorno `Unit`.

---

El cuerpo de una lambda puede ocupar varias líneas. No hay palabra clave `return`: el valor de la **última expresión** es lo que la lambda devuelve.
```kotlin
val describe: (Int) -> String = { n ->
    val half = n / 2
    "half of $n is $half" // returned
}
println(describe(10)) // half of 10 is 5
```
Como `if` es una expresión en Kotlin, puede ser la última línea y decidir el resultado:
```kotlin
val parity: (Int) -> String = { n -> if (n % 2 == 0) "even" else "odd" }
```

---

Cuando una lambda tiene exactamente **un** parámetro puedes omitir declararlo: Kotlin lo llama `it` por ti.
```kotlin
// val double: (Int) -> Int = { n -> n * 2 }
val double: (Int) -> Int = { it * 2 } // same thing
```
`it` solo existe cuando el parámetro no se declara explícitamente, y solo para lambdas de un único parámetro.
Mantiene compactas las lambdas cortas, pero para cuerpos más largos un nombre real es más claro.

---

Las lambdas se usan sobre todo como argumentos de otras funciones. Las colecciones ofrecen muchas funciones que reciben una lambda:
- `forEach` ejecuta la lambda una vez por cada elemento
- `map` construye una lista nueva con el resultado de la lambda para cada elemento
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map({ it * 2 }) // [2, 4, 6]
```
Cuando la lambda es el **último** argumento, puedes moverla fuera de los paréntesis; cuando es el único argumento, los paréntesis se pueden omitir por completo. Esto se llama sintaxis de **trailing lambda** y es la forma habitual de escribirla:
```kotlin
val doubled = numbers.map { it * 2 }
doubled.forEach { println(it) }
```

---

Una lambda que devuelve un `Boolean` se llama **predicado**. Varias funciones de colecciones reciben una:
- `filter` conserva solo los elementos para los que el predicado es `true`
- `count` devuelve cuántos elementos lo satisfacen
- `any` y `all` dicen si algún elemento o todos los elementos lo satisfacen
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)
println(numbers.filter { it % 2 == 0 }) // [2, 4, 6]
println(numbers.count { it > 4 })        // 2
println(numbers.any { it > 5 })          // true
```
Las llamadas se pueden **encadenar**: cada función devuelve una lista nueva sobre la que trabaja la siguiente.
```kotlin
println(numbers.filter { it % 2 == 0 }.map { it * 10 }) // [20, 40, 60]
```

---

Las lambdas también impulsan la ordenación y la agregación:
- `sortedBy` devuelve una lista nueva ordenada por el valor que la lambda calcula para cada elemento; `sortedByDescending` hace lo contrario
- `reduce` combina todos los elementos en un único valor: la lambda recibe el resultado acumulado hasta el momento y el siguiente elemento
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })          // [fig, kiwi, banana]
println(words.sortedByDescending { it.length }) // [banana, kiwi, fig]

val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n })   // 10
```
`reduce` empieza con el primer elemento como `acc`, y después ejecuta la lambda para cada elemento restante.

---

Con `reduce` la forma del resultado la decide la lambda. Cualquier operación que combine dos valores sirve: una suma, un producto, quedarse con el mayor de los dos.
```kotlin
val numbers = listOf(3, 9, 4)
println(numbers.reduce { acc, n -> if (n > acc) n else acc }) // 9
```
Ten en cuenta que `reduce` lanza una excepción con una lista vacía, porque no hay un primer elemento desde el que empezar.

---

Una lambda puede usar las variables declaradas a su alrededor, incluso después de que el código circundante haya terminado. Esto se llama **closure**: la lambda *captura* las variables que necesita.
A diferencia de muchos otros lenguajes, Kotlin permite que una lambda **modifique** un `var` capturado:
```kotlin
var clicks = 0
val onClick = { clicks++ }
onClick()
onClick()
println(clicks) // 2
```
Cada llamada de `onClick` actualiza la misma variable `clicks` que ve el código exterior.

---

Como una lambda es un valor, una función puede **devolver** una. El tipo de retorno es un tipo de función:
```kotlin
fun multiplier(factor: Int): (Int) -> Int {
    return { it * factor }
}
val triple = multiplier(3)
println(triple(5)) // 15
```
La lambda devuelta captura `factor`, así que cada llamada de `multiplier` construye una función distinta.
Las funciones que reciben o devuelven otras funciones se llaman **funciones de orden superior**.

---

Una lambda devuelta puede capturar un `var` declarado dentro de la función. Esa variable sigue viva después de que la función haya retornado, y solo la lambda puede alcanzarla: es estado privado.
```kotlin
fun makeGreeter(): () -> String {
    var calls = 0
    return { calls++; "hello #$calls" }
}
val greeter = makeGreeter()
println(greeter()) // hello #1
println(greeter()) // hello #2
```
Cada llamada de `makeGreeter()` declara un `calls` nuevo, así que dos greeters cuentan de forma independiente.

---

Puedes escribir tus propias funciones de orden superior: un parámetro con un tipo de función acepta cualquier lambda de esa forma, y dentro de la función la llamas como una función normal.
```kotlin
fun repeatTwice(text: String, transform: (String) -> String): String {
    return transform(transform(text))
}
println(repeatTwice("a", { it + "!" })) // a!!
println(repeatTwice("a") { it + "!" })  // same, with a trailing lambda
```
Poner el parámetro de función el **último** es lo que hace disponible la sintaxis de trailing lambda para quienes llaman a la función.

---

Cuando la función que necesitas ya existe, no hace falta envolverla en una lambda: una **referencia a función** `::name` convierte una función con nombre en un valor con el tipo de función correspondiente.
```kotlin
fun isEven(n: Int) = n % 2 == 0
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { isEven(it) }) // [2, 4]
println(numbers.filter(::isEven))      // [2, 4], same thing
```
Las funciones miembro se referencian a través de su tipo, como `String::uppercase`:
```kotlin
println(listOf("a", "b").map(String::uppercase)) // [A, B]
```

---

Una **función anónima** es una función declarada con `fun` pero sin nombre. Es otra forma de crear un valor de función:
```kotlin
val square = fun(x: Int): Int {
    return x * x
}
println(square(4)) // 16
```
A diferencia de una lambda, puede declarar su tipo de retorno explícitamente y usa `return` para producir el valor.
Las funciones anónimas y las lambdas son intercambiables: ambas se pueden pasar a `map`, `filter` o cualquier función que reciba un tipo de función.

---

Las funciones de orden superior pueden tanto recibir como devolver funciones. Un ejemplo clásico es la **composición**: construir una función nueva que ejecuta una función y pasa su resultado a otra.
```kotlin
fun andThen(first: (Int) -> Int, second: (Int) -> Int): (Int) -> Int {
    return { n -> second(first(n)) }
}
val addOneThenDouble = andThen({ it + 1 }, { it * 2 })
println(addOneThenDouble(3)) // 8
```
La lambda devuelta captura tanto `first` como `second`, así que sigue funcionando mucho después de que `andThen` haya retornado.

---

Algunas funciones reciben una **lambda con receptor**: dentro de la lambda, `this` es un objeto concreto, así que puedes llamar a sus miembros directamente sin nombrarlo.
`buildString` es un ejemplo común: dentro de su lambda `this` es un `StringBuilder`, así que `append` se puede llamar como si fuera una función local:
```kotlin
val text = buildString {
    append("Hello")
    append(", ")
    append("world")
}
println(text) // Hello, world
```
`buildString` devuelve la cadena final. Es una alternativa cómoda a concatenar con `+` en un bucle.
