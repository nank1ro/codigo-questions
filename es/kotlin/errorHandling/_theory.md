Una **excepción** es la forma en que Kotlin informa de que una sentencia no puede llevarse a cabo. Convertir `"abc"` en un número, dividir un entero entre cero o leer más allá del final de una lista lanzan todas una.

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
Este programa imprime `before` y después se detiene. `toInt()` no puede leer `"abc"`, así que **lanza** una `NumberFormatException`; nada en el programa se ocupa de ella, así que Kotlin termina el programa con un informe de error y `after` nunca se imprime.

También puedes lanzar una excepción tú mismo con la palabra clave `throw`:
```kotlin
throw Exception("something went wrong")
```

Una excepción que nadie maneja no es una advertencia: es el final de la ejecución.

---

Para mantener vivo el programa, coloca la sentencia arriesgada dentro de un bloque `try` y describe la recuperación en un bloque `catch`:
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
Kotlin ejecuta el bloque `try`; en cuanto una sentencia dentro de él lanza, el resto del bloque se omite y el control salta al bloque `catch`. El nombre entre paréntesis — `e` aquí — es el objeto de la excepción, y `Exception` es el tipo que se captura.

Una vez que el bloque `catch` ha terminado, el programa continúa normalmente con la línea posterior al `try`/`catch` completo.

---

Capturar `Exception` lo captura todo, lo que rara vez es lo que quieres: un error de escritura en otra parte del bloque también quedaría engullido. En su lugar, indica el **tipo exacto** del que sabes cómo recuperarte.

Cada fallo tiene su propio tipo. `"abc".toInt()` lanza una `NumberFormatException`, así que ese es el tipo a capturar:
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
Si se lanza un tipo de excepción diferente dentro del bloque, este `catch` no coincide y la excepción sigue saliendo de la función.

---

Un `try` puede ir seguido de varios bloques `catch`, cada uno manejando un tipo diferente:
```kotlin
val letters = listOf("a", "b")
val index = 5
val text = "abc"
try {
    println(letters[index] + text.toInt())
} catch (e: NumberFormatException) {
    println("not a number")
} catch (e: IndexOutOfBoundsException) {
    println("no such letter")
} catch (e: Exception) {
    println("something else went wrong")
}
```
Kotlin prueba los bloques **de arriba a abajo** y ejecuta el primero cuyo tipo coincide. Solo se ejecuta un bloque.

Por tanto, el orden importa. `NumberFormatException` e `IndexOutOfBoundsException` son ambos tipos de `Exception`, así que un `catch (e: Exception)` escrito primero coincidiría con cada fallo y los bloques debajo de él nunca se ejecutarían. Escribe el tipo más específico primero y el más general al final.

---

Un bloque `finally` puede añadirse al final. Se ejecuta **pase lo que pase**: después de un `try` exitoso, después de que un `catch` se haya recuperado, e incluso cuando la excepción no se captura en absoluto.

```kotlin
try {
    println("reading")
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("bad number")
} finally {
    println("closing")
}
```
```
reading
bad number
closing
```
Eso lo convierte en el lugar para la limpieza que no debe omitirse, como cerrar un archivo. Un `try` necesita al menos un `catch` o un `finally`, pero puede tener ambos.

---

En Kotlin `try` no es solo una sentencia: es una **expresión** que produce un valor. El valor es la última expresión del bloque que se ejecutó — el bloque `try` cuando nada falló, el bloque `catch` cuando algo falló.

```kotlin
val n = try { "abc".toInt() } catch (e: NumberFormatException) { 0 }
println(n) // 0
```
Esta es la forma idiomática en Kotlin. En lugar de declarar un `var`, asignarlo en dos lugares y esperar que cada camino lo asigne, obtienes un único `val` que siempre contiene un valor utilizable.

Ten en cuenta que un bloque `finally` nunca cambia el valor: se ejecuta solo por sus efectos secundarios.

---

Como `try` es una expresión, puede usarse en cualquier lugar donde se espera un valor — incluido como cuerpo completo de una función escrita con `=`:
```kotlin
fun length(text: String): Int = try {
    text.toInt()
} catch (e: NumberFormatException) {
    -1
}
```
Ambos bloques deben producir un valor del mismo tipo, aquí `Int`. Escribe el valor de reserva como la última expresión del bloque `catch`; no hay ningún `return` dentro de ninguno de los bloques.

---

Lanzar y capturar no es gratis, y para las conversiones comunes Kotlin ofrece una variante más barata que simplemente devuelve `null` en lugar de lanzar: `toIntOrNull()`, `toDoubleOrNull()`, `toLongOrNull()`.

```kotlin
println("42".toIntOrNull())  // 42
println("abc".toIntOrNull()) // null
```
Combinado con el operador elvis `?:`, que suministra un reemplazo cuando el valor a su izquierda es `null`, todo el `try`/`catch` se colapsa en una línea:
```kotlin
val n = "abc".toIntOrNull() ?: 0
println(n) // 0
```
Acude a `try`/`catch` cuando el fallo es genuinamente excepcional; acude a `toIntOrNull()` cuando se espera una entrada errónea.

---

Tus propias funciones pueden rechazar una entrada errónea de la misma manera que lo hace la biblioteca estándar, con `throw`. La biblioteca ya proporciona un tipo para el caso más común: `IllegalArgumentException` significa "el valor que me pasaste no es aceptable".

```kotlin
fun half(n: Int): Int {
    if (n < 0) throw IllegalArgumentException("n must not be negative")
    return n / 2
}
```
`throw` termina la función inmediatamente — el `return` debajo de él nunca se alcanza. Quien llama decide qué hacer al respecto:
```kotlin
try { println(half(-4)) }
catch (e: IllegalArgumentException) { println("rejected") }
```
Lanzar es mejor que devolver silenciosamente un valor inventado: una respuesta errónea viaja lejos, una excepción se detiene en el primer llamador que está listo para manejarla.

---

Cada excepción lleva el texto con el que fue creada. Dentro de un bloque `catch` la lees a través de la propiedad `message` del objeto de la excepción:
```kotlin
try {
    throw IllegalArgumentException("price must be positive")
} catch (e: IllegalArgumentException) {
    println(e.message) // price must be positive
}
```
`message` es nullable, porque una excepción puede construirse sin ningún texto; `e.message ?: "unknown"` da un reemplazo seguro cuando necesitas un `String` plano.

Es mejor imprimir `e.message` que imprimir el objeto de la excepción en sí: el texto del propio objeto también incluye el nombre de la clase, lo cual es ruido para quien lee la salida.

---

Escribir `if (...) throw IllegalArgumentException(...)` en cada argumento se vuelve ruidoso, así que Kotlin proporciona dos atajos que se leen como frases sencillas:

```kotlin
require(n >= 0) { "n must not be negative" }   // lanza IllegalArgumentException
check(started) { "not started" }               // lanza IllegalStateException
```
Ambos toman una condición y un bloque que produce el mensaje, y ambos lanzan **cuando la condición es falsa**. La única diferencia es el tipo de la excepción, y esa diferencia es un mensaje para el lector:

* `require` vigila los **argumentos** que pasó quien llama, y falla con `IllegalArgumentException`.
* `check` vigila el **estado** del objeto o del programa, y falla con `IllegalStateException`.

El bloque solo se evalúa cuando la comprobación falla, así que construir el mensaje no cuesta nada cuando todo va bien.

---

Cuando ninguno de los tipos incorporados describe bien tu fallo, declara el tuyo propio. Una excepción es una clase ordinaria que extiende `Exception` y le entrega su texto al padre:

```kotlin
class InsufficientFundsException(message: String) : Exception(message)
```
Esa única línea es un tipo de excepción completo. Se lanza y se captura como cualquier otra, y `e.message` devuelve el texto con el que se construyó:
```kotlin
try {
    throw InsufficientFundsException("balance too low")
} catch (e: InsufficientFundsException) {
    println(e.message) // balance too low
}
```
La ganancia es precisión: quien llama puede capturar solo `InsufficientFundsException` y dejar que cualquier otro fallo siga su camino.

---

`runCatching` ejecuta un bloque y nunca deja que una excepción escape. En su lugar devuelve un `Result`, un objeto que contiene **ya sea** el valor que el bloque produjo **o** la excepción que lanzó:

```kotlin
val ok = runCatching { "42".toInt() }
val bad = runCatching { "abc".toInt() }

println(ok.isSuccess)   // true
println(bad.isFailure)  // true
```
El valor se lee después, y tú eliges en qué debe convertirse un fallo:
```kotlin
println(ok.getOrNull())      // 42
println(bad.getOrNull())     // null
println(bad.getOrElse { 0 }) // 0
```
`getOrNull()` convierte un fallo en `null`, mientras que `getOrElse { ... }` ejecuta el bloque para construir un reemplazo. Nada se lanza en el lugar de la llamada, así que el fallo puede llevarse de un lado a otro y tratarse más tarde.

---

Un `Result` también puede inspeccionarse sin desenvolverlo. `onFailure` ejecuta su bloque solo cuando el resultado contiene una excepción, `onSuccess` solo cuando contiene un valor, y **ambos devuelven el mismo `Result`** así que las llamadas pueden encadenarse:

```kotlin
runCatching { "abc".toInt() }
    .onFailure { println("could not read it") }
    .onSuccess { println("read $it") }
```
Dentro del bloque la excepción (o el valor) está disponible como `it`, así que `it.message` es el texto del fallo.

Esta es la forma de "registrar y continuar": informa del problema donde ocurrió, luego continúa, sin un `return` anticipado y sin un `var` asignado desde dos lugares.

---

Dónde se coloca el `try` decide cuánto trabajo destruye un único valor erróneo. Envuelve **todo el bucle** y el primer fallo abandona el resto del lote; envuelve el **cuerpo** y solo se pierde ese elemento:

```kotlin
var total = 0
for (value in listOf("3", "x", "5")) {
    try {
        total += value.toInt()
    } catch (e: NumberFormatException) {
        // ignora este valor
    }
}
println(total) // 8
```
Esto se combina naturalmente con una función de validación que lanza: la función enuncia una regla y rechaza todo lo que la incumpla, y el bucle decide que un rechazo solo cuesta un elemento.
