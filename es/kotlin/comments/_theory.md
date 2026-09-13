Un **comentario** es una nota escrita dentro del código fuente para las personas que lo leen. El compilador ignora los comentarios por completo, así que nunca cambian lo que hace el programa.

El comentario más simple es el **comentario de una línea**: empieza con `//` y se extiende hasta el final de la línea.
```kotlin
// Greets the user
println("Hello")
```
Usa los comentarios para explicar para qué sirve un fragmento de código, o por qué se escribió de esa manera.

---

Un comentario no necesita su propia línea: puede seguir al código en la misma línea. Esto es un **comentario al final de línea**, y es un buen lugar para una nota breve sobre esa sentencia concreta:
```kotlin
val retries = 3 // give up after three attempts
```
Todo lo que va desde `//` hasta el final de la línea se ignora, mientras que el código anterior se ejecuta como de costumbre.

---

Como el compilador elimina los comentarios por completo, añadir o borrar un comentario nunca cambia lo que hace un programa. Solo se ejecuta el código que **no** está comentado.

Esto convierte a `//` en una forma rápida de desactivar una línea de código sin borrarla. Esto se llama **comentar**:
```kotlin
var total = 10
// total = total + 5
println(total) // prints 10
```
La segunda línea ahora es un comentario, así que `total` se queda en `10`. Quitar el `//` devuelve la línea a la vida.

Comentar es útil mientras experimentas, pero recuerda limpiar después: el código que permanece comentado durante mucho tiempo solo confunde a quien lo lea después.

---

Cuando un comentario necesita más de una línea, Kotlin ofrece el **comentario multilínea** (también llamado comentario de bloque): empieza con `/*` y termina con `*/`, y todo lo que hay en medio se ignora, incluidos los saltos de línea.
```kotlin
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
println("Welcome!")
```
Un comentario de bloque también puede ser corto y quedarse en una línea: `/* like this */`.

---

A diferencia de `//`, que se detiene al final de la línea, un comentario `/*` solo se detiene en el `*/`. Si olvidas cerrarlo, el compilador trata todo el código siguiente como parte del comentario y reporta un error:
```kotlin
val width = 10 /* in centimetres
println(width) // still inside the comment: error, the comment is never closed
```
Tanto `//` como `/* */` funcionan como comentarios al final de línea, pero con `/*` asegúrate siempre de que el `*/` está presente.

---

En Java un comentario de bloque no puede contener otro comentario de bloque, pero en Kotlin **pueden anidarse**: cada `/*` debe emparejarse con su propio `*/`, y el comentario termina solo cuando se cierra el más externo.
```kotlin
/* outer /* inner */ still a comment */
println("done")
```
Aquí `still a comment */` forma parte del comentario externo, así que solo se imprime `done`. Esto es lo que te permite comentar un bloque entero de código aunque ese bloque ya contenga un comentario `/* */`.

---

Para comentar varias líneas a la vez, envuélvelas en un único comentario de bloque en lugar de añadir `//` a cada línea:
```kotlin
var total = 100
/*
total = total - 30
total = total - 20
*/
println(total) // prints 100
```
Gracias al anidamiento, esto funciona incluso cuando una de esas líneas ya contiene un comentario `/* */`.

---

Un uso común de los comentarios de bloque es el **comentario de cabecera**: un bloque corto colocado justo encima de una función que dice qué hace y qué significan sus parámetros.
```kotlin
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
Quien llame a `toSeconds` puede leer la cabecera en lugar del cuerpo. Mantén la cabecera junto a la función para que se actualicen juntas.

---

Kotlin tiene un tercer tipo de comentario, el **comentario de documentación**, escrito en un formato llamado **KDoc**: empieza con `/**` (una barra y dos asteriscos) y termina con `*/`, y se coloca justo encima de una función, una clase o una propiedad.
```kotlin
/**
 * Returns the greeting for [name].
 */
fun greet(name: String): String {
    return "Hi, $name!"
}
```
Para el compilador es solo un comentario, pero herramientas como IntelliJ IDEA lo leen y lo muestran como texto de ayuda de `greet`. El `*` al principio de las líneas interiores es solo una convención que mantiene el bloque alineado. Dentro de KDoc puedes usar Markdown, y los corchetes como `[name]` se convierten en enlaces a ese parámetro.

---

La primera línea de un comentario de documentación es el **resumen**: una frase corta que dice qué hace la función. Escríbela en tercera persona, como si describieras la función: "Devuelve...", "Suma...", "Comprueba...".
```kotlin
/**
 * Returns `true` when [n] is divisible by two.
 */
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
```
El comentario debe quedar justo encima de la declaración, sin ninguna otra sentencia en medio, de lo contrario las herramientas no lo asocian a la función.

---

Después del resumen, un comentario de documentación puede describir los parámetros y el valor devuelto con **etiquetas KDoc**, que siempre empiezan con `@`:
```kotlin
/**
 * Returns the number of seconds in the given minutes.
 * @param minutes a whole number of minutes, never negative
 * @return [minutes] multiplied by sixty
 */
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
`@param` va seguido del nombre del parámetro y después de su descripción; hay un `@param` por parámetro. `@return` describe el valor que la función devuelve. El orden es siempre el mismo: primero el resumen, luego las etiquetas `@param` y después `@return`.

---

Una función con más de un parámetro recibe una etiqueta `@param` por cada uno de ellos, escritas en el mismo orden que los parámetros:
```kotlin
/**
 * Returns the area of a rectangle.
 * @param width the horizontal side, in centimetres
 * @param height the vertical side, in centimetres
 * @return the product of [width] and [height]
 */
fun area(width: Int, height: Int): Int {
    return width * height
}
```
Una etiqueta sigue siendo solo un comentario: si renombras un parámetro y olvidas la etiqueta, no se rompe nada, pero la documentación empieza a mentir. Actualiza el KDoc junto con la firma.

---

El compilador busca comentarios solo en el código, nunca dentro de una **cadena literal**. Entre comillas dobles, `//` y `/* */` son caracteres ordinarios:
```kotlin
println("50 // 2") // prints 50 // 2
```
El primer `//` forma parte del texto, el segundo empieza un comentario de verdad. Esto sorprende a la gente sobre todo con direcciones web, que contienen `//` justo después del protocolo.

---

Algunos comentarios siguen una convención que los editores entienden. Los **marcadores** más comunes son:
- `// TODO: ...` señala algo que todavía queda por escribir
- `// FIXME: ...` señala código que se sabe que está mal y debe corregirse

```kotlin
val limit = 10
// TODO: read the limit from the settings
```
Para el compilador son comentarios ordinarios; IntelliJ IDEA los recopila en una ventana de herramientas dedicada para que el trabajo pendiente sea fácil de encontrar. Un `TODO` suele ir junto a un marcador de posición que mantiene el código compilando hasta que se escribe la implementación real. Cuando completes el trabajo, sustituye el marcador de posición y elimina el marcador en el mismo cambio, para que el comentario nunca mienta sobre el estado del código.

---

Un `FIXME` es diferente de un `TODO`: el código ya existe, pero se sabe que está mal. Un buen `FIXME` dice cuál es el error y, cuando es posible, da un ejemplo que lo muestra, para que la siguiente persona pueda arreglarlo rápidamente. Igual que con `TODO`, borra el marcador una vez corregido el error, pero conserva el comentario de documentación, que sigue siendo válido.

---

Un buen comentario explica **por qué** el código hace algo, no **qué** hace. El código ya muestra qué ocurre; repetirlo con palabras añade ruido y queda obsoleto en cuanto cambia el código:
```kotlin
// set timeout to 30
val timeout = 30
```
La razón que hay detrás del número es lo que un lector no puede adivinar:
```kotlin
// the server drops idle connections after 35 seconds, so stop earlier
val timeout = 30
```
Si un comentario solo repite la línea de abajo, bórralo o sustitúyelo por la razón. Los mejores comentarios son los que dicen algo que el código no puede.
