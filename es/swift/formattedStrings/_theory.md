Una **cadena formateada** es un fragmento de texto en el que algunas partes se rellenan con valores en tiempo de ejecución: un precio, un nombre, una puntuación. Swift te da dos herramientas para esto.

La primera es la **interpolación de cadenas**, que ya conoces: todo lo que se escribe dentro de `\( )` se evalúa y se inserta en el texto. No tiene que ser una variable, puede ser cualquier expresión:
```swift
let price = 4
print("Total: \(price * 3)") // Total: 12
print("Name: \("ada".uppercased())") // Name: ADA
```
La interpolación es la forma más rápida de construir una cadena, pero imprime los números exactamente como Swift los almacena: `3.5` se queda en `3.5`, nunca `3.50`. Para tener control total sobre dígitos, ancho y relleno usaremos `String(format:)`, que se introduce en el siguiente ejercicio.

---

La segunda herramienta es `String(format:)`, que proviene del framework **Foundation**, así que el archivo debe empezar con `import Foundation`.

Recibe una **cadena de formato** seguida de los valores a insertar. Dentro de la cadena de formato, un **especificador** que empieza con `%` marca dónde va cada valor y cómo se escribe. El especificador para un entero es `%d`:
```swift
import Foundation

let count = 7
let text = String(format: "Item %d", count)
print(text) // Item 7
```
`String(format:)` devuelve un `String` normal, así que puedes imprimirlo, almacenarlo o devolverlo desde una función.

---

Para los números decimales (`Double`) el especificador es `%f`. Por sí solo siempre imprime seis dígitos después del punto:
```swift
print(String(format: "%f", 3.5)) // 3.500000
```
Para elegir cuántos decimales quieres, escribe un punto y un número entre `%` y `f`. Esto es la **precisión**, y el valor se redondea para ajustarse:
```swift
print(String(format: "%.2f", 3.5))     // 3.50
print(String(format: "%.1f", 3.14159)) // 3.1
print(String(format: "%.0f", 2.71))    // 3
```
`%.2f` es la elección habitual para los precios, porque siempre muestra exactamente dos decimales.

---

Un número entre `%` y la letra establece el **ancho mínimo** del campo. Si el valor es más corto, se añaden espacios a la izquierda para que quede **alineado a la derecha**; si es más largo, no se corta nada:
```swift
print(String(format: "%5d|", 42))    //    42|
print(String(format: "%5d|", 12345)) // 12345|
```
Ancho y precisión se combinan: `%8.2f` significa "al menos 8 caracteres de ancho, con 2 decimales":
```swift
print(String(format: "%8.2f|", 3.14159)) //     3.14|
```
Los anchos fijos son lo que alinea las columnas de una tabla.

---

Por defecto el relleno va a la izquierda. Un signo menos justo después de `%` pone el relleno a la derecha, de modo que el valor queda **alineado a la izquierda**:
```swift
print(String(format: "%-5d|", 42)) // 42   |
print(String(format: "%5d|", 42))  //    42|
```
El signo menos es una **bandera**: cambia cómo se rellena el campo sin cambiar el ancho.

---

Otra bandera es `0`: en lugar de espacios, el campo se rellena con ceros a la izquierda. Así obtienes números como `007` o `00042`:
```swift
print(String(format: "%05d", 42))  // 00042
print(String(format: "%03d", 7))   // 007
print(String(format: "%03d", 1234)) // 1234
```
Como con los espacios, un valor más largo que el ancho nunca se corta.

---

Una cadena de formato puede contener tantos especificadores como quieras. Los valores siguen en el mismo orden, separados por comas, y cada uno debe coincidir con el tipo de su especificador: `%d` para un `Int`, `%f` para un `Double`:
```swift
let count = 3
let weight = 4.5
print(String(format: "%d items, %.1f kg", count, weight)) // 3 items, 4.5 kg
```
Pasar un `Double` a `%d` (o un `Int` a `%f`) compila, pero imprime un número sin sentido, así que comprueba siempre que los especificadores y los valores coincidan.

---

Los enteros también se pueden escribir en otras bases. `%x` imprime el valor en **hexadecimal** con letras minúsculas, `%X` con letras mayúsculas, y `%o` en octal:
```swift
print(String(format: "%x", 255)) // ff
print(String(format: "%X", 255)) // FF
print(String(format: "%o", 8))   // 10
```
El ancho y la bandera `0` también funcionan aquí: `%02x` es la forma clásica de escribir un byte de un color, como en `#ff8000`.

---

Para insertar un `String` en una cadena de formato, usa el especificador `%@`:
```swift
let name = "Ada"
let age = 36
print(String(format: "%@ is %d years old", name, age)) // Ada is 36 years old
```
`%@` acepta un `String` de Swift directamente. No uses `%s` con una cadena de Swift: ese especificador espera una cadena de C e imprime basura o se bloquea.
