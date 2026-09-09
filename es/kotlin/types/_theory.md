Cada valor en Kotlin tiene un **tipo**, que le dice al compilador qué clase de dato es y qué puedes hacer con él.
Los tipos básicos son:
- `Int`: un número entero, como `42` o `-7`
- `Long`: un número entero que puede ser mucho mayor que un `Int`
- `Double`: un número con parte decimal, como `3.14`
- `Float`: un número decimal que usa la mitad de memoria que un `Double`, pero es menos preciso
- `Char`: un solo carácter entre comillas simples, como `'a'`
- `Boolean`: o bien `true` o bien `false`
- `String`: un texto entre comillas dobles, como `"Hello"`

Como viste en las lecciones de variables, puedes indicar el tipo explícitamente con dos puntos después del nombre:
```kotlin
val age: Int = 36
val name: String = "Ada"
```
Un valor de un tipo no puede almacenarse en una variable de otro tipo: `val age: Int = "36"` es un error de compilación.

---

La mayoría de las veces no escribes el tipo: Kotlin lo **infiere** a partir del valor que asignas, siguiendo unas reglas de literales:
- un número entero, como `42`, es un `Int`
- un número con punto decimal, como `3.14`, es un `Double`
- un texto entre comillas dobles es un `String`
- un carácter entre comillas simples es un `Char`
- `true` y `false` son `Boolean`
```kotlin
val count = 42     // Int
val price = 9.99   // Double
val name = "Ada"   // String
val grade = 'A'    // Char
val isOpen = true  // Boolean
```
Para comprobar qué infirió Kotlin puedes imprimir el nombre del tipo de cualquier valor con `::class.simpleName`:
```kotlin
println(count::class.simpleName) // Int
println(price::class.simpleName) // Double
```
Un literal decimal nunca se infiere como `Float`: `val ratio = 0.5` es un `Double`.

---

Un `Int` puede albergar números enteros hasta unos dos mil millones, más precisamente hasta `Int.MAX_VALUE`, que es `2147483647`.
Un literal de número entero demasiado grande para un `Int` se infiere automáticamente como `Long`, y puedes forzar un `Long` para cualquier literal con el sufijo `L`:
```kotlin
val big = 3000000000  // Long, too big for an Int
val small = 3L        // Long, thanks to the suffix
```
De la misma manera el sufijo `f` convierte un literal decimal en un `Float`: `val ratio = 0.5f`.
Los números largos son difíciles de leer, así que Kotlin te permite colocar guiones bajos `_` en cualquier lugar entre los dígitos; el compilador los ignora:
```kotlin
val population = 8_000_000_000L
val million = 1_000_000
println(million) // 1000000
```

---

Kotlin nunca convierte entre tipos numéricos por su cuenta cuando asignas un valor, ni siquiera de un tipo más pequeño a uno más grande: almacenar un `Int` en una variable `Long` o `Double` es un error de compilación.
```kotlin
val count = 3
val total: Long = count      // error: Int is not a Long
val price: Double = count    // error: Int is not a Double
```
Cada tipo numérico tiene **funciones de conversión** que construyen un nuevo valor del tipo que necesitas: `toInt()`, `toLong()`, `toDouble()`, `toFloat()` y, para obtener texto, `toString()`.
```kotlin
val total: Long = count.toLong()
val price: Double = count.toDouble() // 3.0
println(count.toString() + "!")      // 3!
```
Pasar de un decimal a un número entero **trunca**: `toInt()` simplemente descarta la parte decimal, así que `3.99.toInt()` es `3` y `(-3.99).toInt()` es `-3`.

---

Los tipos de los operandos deciden cómo funciona la división. Cuando ambos son `Int`, el operador `/` realiza una **división entera**: el resultado es un `Int` y el resto se descarta.
Cuando al menos un operando es un `Double`, `/` realiza una división en punto flotante y conserva la parte decimal:
```kotlin
println(7 / 2)              // 3
println(7.0 / 2)            // 3.5
val slices = 7
println(slices.toDouble() / 2) // 3.5
```
Así que para obtener un resultado decimal a partir de dos variables `Int` debes convertir al menos una de ellas **antes** de dividir: `(7 / 2).toDouble()` es `3.0`, porque la división entera ya ocurrió.

---

Cuando una función debe devolver un resultado decimal calculado a partir de números enteros, convierte los operandos a `Double` antes de dividir y declara el tipo de retorno como `Double`:
```kotlin
fun ratio(part: Int, total: Int): Double {
    return part.toDouble() / total
}
println(ratio(1, 4)) // 0.25
```
Recuerda que `sum()` y `size` de una `List<Int>` también son valores `Int`, así que necesitan la misma conversión.

---

Cada `Char` se almacena como un número, su **código**. La propiedad `code` da el `Int` que hay detrás de un carácter, y `toChar()` hace lo contrario, convirtiendo un `Int` en el `Char` con ese código:
```kotlin
println('A'.code)        // 65
println(66.toChar())     // B
println(('A'.code + 2).toChar()) // C
```
Las letras tienen códigos consecutivos, así que sumar al código avanza por el alfabeto.
Ten en cuenta que el código de `'7'` es `55`, no `7`: para leer el dígito que representa un `Char` usa `digitToInt()`, que devuelve `7`.

---

Dado que el código de un `Char` es un `Int`, puedes hacer aritmética con él y convertir el resultado de nuevo a un `Char`. Así es como avanzas por el alfabeto:
```kotlin
val next = ('a'.code + 1).toChar() // 'b'
```
Kotlin también te permite sumar un `Int` directamente a un `Char`: `'a' + 1` es `'b'`, y la diferencia entre dos caracteres `'d' - 'a'` es el `Int` `3`.

---

El texto escrito por un usuario siempre llega como un `String`, incluso cuando parece un número. Para hacer cálculos con él debes **analizarlo**: `toInt()` convierte `"42"` en el `Int` `42`, y `toDouble()` convierte `"3.5"` en el `Double` `3.5`.
```kotlin
val typed = "42"
println(typed.toInt() + 1) // 43
```
No todo texto es un número: `"4x2".toInt()` lanza una `NumberFormatException` y detiene el programa.
Las alternativas seguras `toIntOrNull()` y `toDoubleOrNull()` devuelven `null` en lugar de lanzar una excepción, así que, como aprendiste en las lecciones de nulabilidad, puedes proporcionar un valor por defecto con `?:`:
```kotlin
println("4x2".toIntOrNull())      // null
println("4x2".toIntOrNull() ?: 0) // 0
```

---

`toIntOrNull()` tiene éxito solo cuando todo el texto es un número entero válido, con un signo opcional:
```kotlin
println("42".toIntOrNull())   // 42
println("-7".toIntOrNull())   // -7
println("3.5".toIntOrNull())  // null, not a whole number
println(" 42".toIntOrNull())  // null, spaces are not allowed
println("abc".toIntOrNull())  // null
```
Para texto decimal usa `toDoubleOrNull()`, que acepta `"3.5"` y devuelve un `Double?` de la misma manera.

---

Un `Int` tiene un tamaño fijo, así que tiene un valor mínimo y uno máximo: `Int.MIN_VALUE` es `-2147483648` y `Int.MAX_VALUE` es `2147483647`.
Superar el límite **no** genera un error: el valor silenciosamente **da la vuelta** al otro extremo del rango, un comportamiento llamado desbordamiento.
```kotlin
println(Int.MAX_VALUE)     // 2147483647
println(Int.MAX_VALUE + 1) // -2147483648
```
Cuando un resultado puede superar los dos mil millones, usa un `Long`, cuyo límite `Long.MAX_VALUE` es unos nueve trillones. Recuerda convertir antes de la operación: `Int.MAX_VALUE.toLong() + 1` es `2147483648`.

---

Un `Double` almacena los decimales en binario, así que algunos valores no pueden representarse con exactitud y aparecen pequeños errores en los últimos dígitos:
```kotlin
println(0.1 + 0.2) // 0.30000000000000004
```
Para mostrar un número fijo de decimales, usa `String.format` con una cadena de formato: `"%.2f"` significa "un número decimal con 2 dígitos después del punto". El resultado es un `String`, redondeado a esa cantidad de dígitos:
```kotlin
println(String.format("%.2f", 0.1 + 0.2)) // 0.30
println(String.format("%.1f", 3.14159))   // 3.1
println(String.format("%.2f", 2.0))       // 2.00
```

---

`Any` es el tipo en la cima de la jerarquía: cada valor de Kotlin es un `Any`, así que una variable de tipo `Any` puede contener un `Int`, un `String`, un `Boolean`, o cualquier otra cosa.
Para averiguar qué contiene realmente usas el operador `is`, que devuelve `true` cuando el valor tiene ese tipo:
```kotlin
val value: Any = 42
println(value is Int)    // true
println(value is String) // false
```
Una vez que una comprobación ha pasado, el compilador hace un **smart cast** del valor: dentro del `if` (o de la rama del `when`) puedes usarlo como ese tipo, sin necesidad de conversión:
```kotlin
if (value is Int) println(value + 1) // 43, value is an Int here
when (value) {
    is String -> println(value.length)
    is Boolean -> println(!value)
}
```
