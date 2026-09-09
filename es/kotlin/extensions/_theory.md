Una **función de extensión** añade una nueva función a un tipo existente sin tocar su código fuente.
Escribes `fun`, luego el tipo que quieres extender (el **tipo receptor**), un punto y el nombre de la función:
```kotlin
fun Int.squared(): Int {
    return this * this
}
println(4.squared()) // 16
```
Dentro de la función, `this` es el valor sobre el que se llama a la función, llamado **receptor**: en `4.squared()` es `4`.
Una vez que la extensión existe, la llamas con el punto exactamente igual que una función que hubiera formado parte de `Int` desde el principio.

---

Las extensiones funcionan sobre cualquier tipo, incluso sobre aquellos de los que no tienes el código fuente. `String` viene de la biblioteca estándar, pero aun así puedes darle nuevas funciones:
```kotlin
fun String.whisper(): String {
    return this.lowercase() + "..."
}
println("HELLO".whisper()) // hello...
```
Dentro de una extensión puedes omitir `this.` al usar otros miembros del receptor: `lowercase()` por sí solo significa `this.lowercase()`, y `length` por sí solo significa `this.length`.

---

Una función de extensión puede recibir parámetros como cualquier otra función. El receptor se queda a la izquierda del punto y los parámetros van entre los paréntesis:
```kotlin
fun Int.isDivisibleBy(other: Int): Boolean {
    return this % other == 0
}
println(12.isDivisibleBy(4)) // true
println(12.isDivisibleBy(5)) // false
```
El tipo delante del punto es un tipo normal, así que puedes extender `List<Int>`, `Double` o una clase que hayas escrito tú de la misma manera.

---

Una extensión **no** modifica la clase que extiende ni le inserta un nuevo miembro. El compilador simplemente reescribe la llamada: `"kotlin".first3()` se convierte en una llamada a la función con `"kotlin"` pasado como `this`.
```kotlin
fun String.first3(): String = take(3)
val word = "kotlin"
println(word.first3()) // kot
```
Por eso puedes extender clases finales como `String` e `Int`: dentro de ellas no cambia nada, la extensión solo vive en tu código.

---

Además de funciones, puedes añadir una **propiedad de extensión**. Se declara con `val`, el tipo receptor, un punto y el nombre, seguidos de un `get()` que calcula el valor cada vez que se lee la propiedad:
```kotlin
val String.wordCount: Int
    get() = split(" ").size

println("Kotlin is fun".wordCount) // 3
```
Una propiedad de extensión no puede almacenar nada: no tiene campo de respaldo, así que un inicializador como `val String.label = "text"` es un error de compilación. Solo puede calcular su valor a partir del receptor.
Las propiedades de extensión no se pueden declarar dentro de una función (las propiedades de extensión locales no están permitidas), a diferencia de las funciones de extensión.

---

Las propiedades de extensión se leen sin paréntesis, exactamente igual que el `length` integrado de un `String`. Son la elección natural cuando el valor describe al receptor en lugar de hacer algo con él:
```kotlin
val Int.isNegative: Boolean
    get() = this < 0

println((-3).isNegative) // true
println(7.isNegative)    // false
```
Fíjate en los paréntesis alrededor de `-3`: sin ellos, `-3.isNegative` leería primero la propiedad de `3` y luego intentaría negar un `Boolean`, lo que no compila.

---

El tipo receptor puede ser **nullable**. Una extensión sobre `String?` se puede llamar sobre una variable que quizá contenga `null`, y dentro de la función `this` es un `String?`, así que el caso `null` lo manejas tú, normalmente con el operador Elvis `?:` que viste en las lecciones de nulabilidad:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val name: String? = null
println(name.orDash())  // -
println("Ada".orDash()) // Ada
```
Llamar a `name.orDash()` sobre un valor `null` es seguro: no hace falta `?.`, porque la propia función acepta un receptor `null`.

---

Dentro de una extensión con receptor nullable también puedes usar la llamada segura `this?.` para acceder a los miembros del valor solo cuando no es `null`. La biblioteca estándar usa la misma idea para funciones como `isNullOrEmpty()`:
```kotlin
fun String?.firstOrQuestion(): Char {
    return this?.firstOrNull() ?: '?'
}
val text: String? = null
println(text.firstOrQuestion())    // ?
println("Kotlin".firstOrQuestion()) // K
```

---

Cuando una clase ya tiene un miembro con el mismo nombre y los mismos parámetros que una extensión, **el miembro siempre gana**: la extensión nunca se llama, y el compilador te avisa de que está ensombrecida.
```kotlin
class Box {
    fun describe(): String = "member"
}
fun Box.describe(): String = "extension"

println(Box().describe()) // member
```
Una extensión no puede sobrescribir ni reemplazar un comportamiento existente; solo puede añadir nuevas funciones y propiedades. Para que se elija, una extensión necesita un nombre o una lista de parámetros que la clase no tenga ya.

---

Una extensión puede trabajar sobre toda una familia de tipos a la vez gracias a un **parámetro de tipo**: un marcador de posición para un tipo, declarado entre corchetes angulares justo después de `fun`, que Kotlin rellena en cada llamada. Esto hace que la extensión sea **genérica**:
```kotlin
fun <T> List<T>.second(): T {
    return this[1]
}
println(listOf(1, 2, 3).second())      // 2
println(listOf("a", "b").second())     // b
```
Con `listOf(1, 2, 3)` el marcador `T` es `Int`, con `listOf("a", "b")` es `String`, así que la misma función devuelve el tipo correcto cada vez.

---

El parámetro de tipo se puede usar en cualquier parte de la firma: como tipo de retorno, como `T?` nullable, o dentro de otro tipo. Una extensión genérica que puede no encontrar nada devuelve `T?`, como el `firstOrNull()` integrado:
```kotlin
fun <T> List<T>.lastOrDefault(default: T): T {
    return if (isEmpty()) default else this[size - 1]
}
println(listOf(1, 2).lastOrDefault(0))          // 2
println(emptyList<String>().lastOrDefault("-")) // -
```
Dentro de la función puedes usar `size`, `isEmpty()` y la indexación exactamente igual que en cualquier lista, porque el receptor es una `List<T>`.

---

También puedes extender el **companion object** de una clase, siempre que la clase declare uno, aunque esté vacío. El tipo receptor se escribe `ClassName.Companion`, y la extensión se llama entonces sobre el nombre de la clase, como una función factoría:
```kotlin
class Temperature(val degrees: Int) {
    companion object
}
fun Temperature.Companion.freezing(): Temperature = Temperature(0)

println(Temperature.freezing().degrees) // 0
```
La clase y la extensión son ambas declaraciones de nivel superior, así que deben escribirse fuera de `main`.

---

Una extensión sobre el companion puede recibir parámetros, lo que la convierte en un lugar cómodo para constructores alternativos que convierten desde otra unidad o formato:
```kotlin
class Distance(val meters: Int) {
    companion object
}
fun Distance.Companion.fromKilometers(km: Int): Distance = Distance(km * 1000)

println(Distance.fromKilometers(3).meters) // 3000
```

---

Dónde declaras una extensión decide dónde se puede usar, su **ámbito**:
- en el nivel superior de un archivo, está disponible en todo el archivo y en el resto del paquete
- dentro de una función, es una extensión local, utilizable solo en esa función
- dentro de una clase, es una **extensión miembro**, utilizable solo dentro de esa clase

Una extensión miembro puede leer las propiedades de la clase en la que vive, así que combina dos receptores: la instancia de la clase y el valor sobre el que se llama:
```kotlin
class Greeter(val greeting: String) {
    fun String.greet(): String = "$greeting, $this!"
    fun welcome(name: String): String = name.greet()
}
println(Greeter("Hello").welcome("Ada")) // Hello, Ada!
```
Dentro de `greet`, `greeting` viene del `Greeter` y `this` es el `String` sobre el que se llama a la función. Fuera de la clase, `"Ada".greet()` es un error de compilación.

---

Una función de extensión con exactamente **un** parámetro se puede marcar como `infix`. Una función infix se puede llamar sin el punto ni los paréntesis, con el receptor a la izquierda y el argumento a la derecha, lo que se lee casi como una frase:
```kotlin
infix fun Int.percentOf(total: Int): Int = total * this / 100

println(20 percentOf 50)   // 10
println(20.percentOf(50))  // 10, the normal call still works
```
Kotlin también usa esto para algunas funciones integradas: `1 to "one"` construye un `Pair`, y `1 until 5` construye un rango.

---

Para poder marcarse como `infix`, una función debe ser un miembro o una extensión, debe recibir exactamente un parámetro, y ese parámetro no puede tener un valor por defecto. Cualquier otra cosa es un error de compilación:
```kotlin
infix fun Int.add(other: Int): Int = this + other          // ok
infix fun add(a: Int, b: Int): Int = a + b                 // error: not a member or extension
infix fun Int.add(a: Int, b: Int): Int = this + a + b      // error: two parameters
```
Las llamadas infix tienen una precedencia entre la aritmética y la comparación: `1 add 2 * 3` es `1 add 6`, mientras que `1 add 2 == 3` compara el resultado con `3`.
