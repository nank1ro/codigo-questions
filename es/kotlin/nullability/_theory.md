A veces un valor simplemente falta: un usuario sin segundo nombre, una búsqueda que no encuentra nada, un texto que no se puede convertir en un número.
Kotlin representa un valor faltante con `null`, pero una variable normal nunca puede contenerlo. Todos los tipos son **no nulos** por defecto:
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
Para permitir un valor faltante declaras un tipo **nullable** añadiendo un signo de interrogación `?` después del tipo.
Un `String?` contiene un `String` o `null`:
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String` y `String?` son dos tipos distintos: un `String` nunca falta, un `String?` puede faltar.

---

La diferencia entre `String` y `String?` la comprueba el **compilador**, no en tiempo de ejecución.
Asignar `null` a un tipo no nulo, o pasar un valor nullable donde se espera uno no nulo, es un error de compilación, así que el programa ni siquiera llega a arrancar:
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
Así es como Kotlin evita los fallos de "puntero nulo" comunes en otros lenguajes: un valor solo puede faltar donde lo hayas declarado explícitamente con `?`.

---

El `?` funciona en cualquier lugar donde se escribe un tipo: una función puede aceptar un parámetro nullable y devolver un valor nullable.
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
No puedes llamar a un método directamente sobre un valor nullable, porque podría ser `null`.
El operador de **llamada segura** `?.` llama al método solo cuando el valor no es `null`; en caso contrario toda la expresión es `null`:
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
El resultado de una llamada segura siempre es nullable: `word?.length` es un `Int?`, no un `Int`.

---

Muy a menudo todo lo que quieres de un valor nullable es el valor en sí o un valor predeterminado.
El **operador Elvis** `?:` hace exactamente eso: devuelve el lado izquierdo cuando no es `null`; en caso contrario, el valor de su derecha:
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
Como el lado derecho solo se usa cuando el izquierdo es `null`, el resultado es no nulo cuando el valor predeterminado lo es.
`?:` se combina muy bien con `?.` para convertir una llamada segura de nuevo en un valor simple:
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

Las llamadas seguras se pueden **encadenar**: en cuanto un eslabón es `null`, el resto de la cadena se omite y toda la expresión se convierte en `null`.
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
Una cadena que termina en `?:` te da un resultado no nulo en una sola línea:
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

Las cadenas de llamadas seguras brillan con objetos anidados, donde cualquier nivel puede faltar:
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
Cada `?.` protege el siguiente paso, y el `?:` final aporta el valor predeterminado.

---

El operador de **aserción de no nulo** `!!` convierte un valor nullable en uno no nulo, diciéndole al compilador "estoy seguro de que esto no es `null`":
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
Si te equivocas y el valor es `null`, el programa falla en tiempo de ejecución con un `NullPointerException`, justo el error que Kotlin fue diseñado para prevenir:
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
Usa `!!` solo cuando el valor realmente no pueda ser `null`; prefiere `?.`, `?:` y las comprobaciones de null en todos los demás casos.

---

Cuando compruebas si un valor es `null` con `if`, el compilador lo recuerda: dentro de la rama donde se sabe que el valor no es nulo, se aplica una **conversión inteligente** (*smart cast*) al tipo no nulo y puedes usarlo directamente, sin `?.` ni `!!`:
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
Lo mismo ocurre tras una salida anticipada:
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
Las conversiones inteligentes funcionan con variables `val` y parámetros de función, cuyo valor no puede cambiar entre la comprobación y el uso.

---

`let` ejecuta un bloque de código con el valor sobre el que se llama, disponible dentro del bloque como `it`.
Combinado con una llamada segura, `?.let` ejecuta el bloque **solo** cuando el valor no es `null`, y dentro del bloque `it` es no nulo:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
Es una alternativa compacta a `if (x != null) { ... }` cuando solo necesitas el valor dentro del bloque.

---

`let` también **devuelve** el valor de la última expresión de su bloque, así que `?.let` puede transformar un valor nullable y `?:` puede rellenar el valor predeterminado cuando es `null`:
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
Cuando `price` es `null`, el bloque `let` se omite, la expresión es `null` y el operador Elvis devuelve `"free"`.

---

Las colecciones también pueden contener elementos nullable: una `List<Int?>` puede contener entradas `null`, mientras que una `List<Int>` nunca las contiene.
`filterNotNull()` devuelve una nueva lista sin las entradas `null`, y su tipo de elemento pasa a ser no nulo, así que puedes usar los elementos libremente:
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

Muchas funciones estándar devuelven `null` en lugar de fallar. `toIntOrNull()` convierte una cadena en un `Int`, o devuelve `null` cuando el texto no es un número entero:
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull` transforma cada elemento como `map`, pero descarta los resultados que son `null`:
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

A veces una propiedad no puede recibir un valor cuando se crea el objeto, pero sabes que se asignará antes de usarse.
En lugar de hacerla nullable, márcala con `lateinit`: el tipo sigue siendo no nulo y no hace falta `?.` al leerla:
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
`lateinit` tiene algunas reglas: funciona solo en propiedades `var`, solo con tipos no nulos y no con tipos primitivos como `Int` o `Boolean`.
Leer una propiedad `lateinit` antes de asignarla lanza un `UninitializedPropertyAccessException`; puedes comprobarlo antes con `::player.isInitialized`.

---

Cuando un `null` significa que quien llamó cometió un error, falla cuanto antes con `requireNotNull`.
Devuelve el valor como no nulo cuando está presente, y lanza un `IllegalArgumentException` cuando es `null`, con un mensaje opcional:
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
Después de la llamada, el compilador también aplica una conversión inteligente (smart cast) al propio `name` como `String`, así que `name.length` está permitido a partir de esa línea.
A diferencia de `!!`, el fallo lleva un mensaje claro e indica que el *argumento* era incorrecto.

---

Una función de extensión puede declararse sobre un **receptor nullable**, así que se puede llamar incluso sobre un valor `null`. Dentro, `this` es nullable y debe comprobarse:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
Ten en cuenta que no hace falta `?.` en el punto de llamada: la propia función gestiona el caso `null`.
La biblioteca estándar usa este truco en `isNullOrEmpty()` y `orEmpty()`, que se pueden llamar con seguridad sobre cualquier `String?`.

---

El lado derecho de `?:` puede ser cualquier expresión, incluido `return`. Esto da una forma compacta de salir de una función en cuanto falta un valor:
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
Todas las herramientas que has visto se combinan bien: los parámetros nullable y los tipos de retorno describen *dónde* puede faltar un valor, y `?.`, `?:`, `let`, las conversiones inteligentes y `toIntOrNull` lo gestionan sin fallar jamás.
