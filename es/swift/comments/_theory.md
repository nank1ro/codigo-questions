Un **comentario** es una nota escrita dentro del código fuente para las personas que lo leen. El compilador ignora los comentarios por completo, así que nunca cambian lo que hace el programa.

El comentario más simple es el **comentario de una línea**: empieza con `//` y se extiende hasta el final de la línea.
```swift
// Greets the user
print("Hello")
```
Usa los comentarios para explicar para qué sirve un fragmento de código, o por qué se escribió de esa manera.

---

Un comentario no necesita su propia línea: puede ir después del código en la misma línea. Esto es un **comentario al final de la línea**, y es un buen lugar para una nota breve sobre esa instrucción concreta:
```swift
let retries = 3 // give up after three attempts
```
Todo lo que va desde `//` hasta el final de la línea se ignora, mientras que el código anterior se ejecuta como de costumbre.

---

Como el compilador elimina los comentarios por completo, añadir o borrar un comentario nunca cambia lo que hace un programa. Solo se ejecuta el código que **no** está comentado.

Esto hace de `//` una forma rápida de desactivar una línea de código sin borrarla. Esto se llama **comentar código**:
```swift
var total = 10
// total = total + 5
print(total) // prints 10
```
La segunda línea ahora es un comentario, así que `total` se queda en `10`. Quitar el `//` devuelve la línea a la vida.

Comentar código es útil mientras experimentas, pero recuerda limpiar después: el código que permanece comentado durante mucho tiempo solo confunde a quien lo lea a continuación.

---

Cuando un comentario necesita más de una línea, Swift ofrece el **comentario multilínea** (también llamado comentario de bloque): empieza con `/*` y termina con `*/`, y todo lo que hay en medio se ignora, incluidos los saltos de línea.
```swift
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
print("Welcome!")
```
Un comentario de bloque también puede ser corto y quedarse en una sola línea: `/* like this */`.

---

A diferencia de `//`, que se detiene al final de la línea, un comentario `/*` solo se detiene en el `*/`. Si olvidas cerrarlo, el compilador trata todo el código siguiente como parte del comentario y reporta un error:
```swift
let width = 10 /* in centimetres
print(width) // still inside the comment: error, the comment is never closed
```
Tanto `//` como `/* */` funcionan como comentarios al final de la línea, pero con `/*` asegúrate siempre de que el `*/` está presente.

---

En muchos lenguajes los comentarios de bloque no pueden contener otros comentarios de bloque, pero en Swift **se pueden anidar**: cada `/*` debe estar emparejado con su propio `*/`, y el comentario termina solo cuando se cierra el más externo.
```swift
/* outer /* inner */ still a comment */
print("done")
```
Aquí `still a comment */` es parte del comentario externo, así que solo se imprime `done`. Esto es lo que te permite comentar un bloque entero de código aunque ese bloque ya contenga un comentario `/* */`.

---

Para comentar varias líneas a la vez, envuélvelas en un único comentario de bloque en lugar de añadir `//` a cada línea:
```swift
var total = 100
/*
total = total - 30
total = total - 20
*/
print(total) // prints 100
```
Gracias al anidamiento, esto funciona incluso cuando una de esas líneas ya contiene un comentario `/* */`.

---

Un uso común de los comentarios de bloque es el **comentario de cabecera**: un bloque breve colocado justo encima de una función que dice qué hace y qué significan sus parámetros.
```swift
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
Quien llame a `toSeconds` puede leer la cabecera en lugar del cuerpo. Mantén la cabecera junto a la función para que se actualicen juntas.

---

Swift tiene un tercer tipo de comentario, el **comentario de documentación**: un comentario de una sola línea que empieza con `///` (tres barras) y se coloca justo encima de una función, un tipo o una propiedad.
```swift
/// Returns the greeting for `name`.
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
Para el compilador es solo un comentario, pero herramientas como Xcode lo leen y lo muestran como texto de ayuda de `greet`. Los comentarios de documentación admiten **Markdown**, así que puedes usar acentos graves para el código, `**negrita**` y listas.

---

La primera línea de un comentario de documentación es el **resumen**: una frase corta que dice qué hace la función. Escríbela en tercera persona, como si describieras a la función: "Devuelve...", "Suma...", "Comprueba...".
```swift
/// Returns `true` when `n` is divisible by two.
func isEven(_ n: Int) -> Bool {
    return n % 2 == 0
}
```
El comentario debe estar justo encima de la declaración, sin ninguna línea en blanco en medio; de lo contrario, Xcode no lo asocia a la función.

---

Los comentarios de documentación también existen en forma de bloque: `/**` lo abre y `*/` lo cierra, exactamente como un comentario multilínea pero con un segundo asterisco al principio.
```swift
/**
 Returns the greeting for `name`.

 The result always ends with an exclamation mark.
 */
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
`/// text` y `/** text */` significan lo mismo para las herramientas; `///` es la opción más común en el código Swift, mientras que `/** */` resulta útil para descripciones largas. Un comentario normal `/* */` o `//` **no** es documentación, ni siquiera cuando se coloca encima de una función.

---

Después del resumen, un comentario de documentación puede describir los parámetros y el valor de retorno con elementos de lista especiales de Markdown que Xcode reconoce:
```swift
/// Returns the number of seconds in the given minutes.
/// - Parameter minutes: a whole number of minutes, never negative
/// - Returns: `minutes` multiplied by sixty
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
El orden es siempre el mismo: primero el resumen, después `- Parameter nombre:` para cada parámetro y por último `- Returns:`.

---

Algunos comentarios siguen una convención que los editores entienden. En Swift los **marcadores** más comunes son:
- `// MARK: - Title` etiqueta una sección del archivo, de modo que aparece en el menú de navegación de Xcode
- `// TODO: ...` señala algo que aún falta por escribir
- `// FIXME: ...` señala código que se sabe que está mal y debe corregirse

```swift
// MARK: - Setup
let limit = 10
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Para el compilador son comentarios ordinarios; Xcode los lista para que el trabajo pendiente sea fácil de encontrar. Cuando el trabajo esté hecho, borra el marcador: un `TODO` obsoleto induce a error.

---

Un `TODO` suele ir junto a un marcador de posición que mantiene el código compilando hasta que se escribe la implementación real. Cuando completes el trabajo, reemplaza el marcador de posición y elimina el marcador en el mismo cambio, para que el comentario nunca mienta sobre el estado del código.

---

Un `FIXME` es diferente de un `TODO`: el código ya existe, pero se sabe que está mal. Un buen `FIXME` dice cuál es el error y, cuando es posible, da un ejemplo que lo muestra, para que la siguiente persona pueda corregirlo rápidamente. Igual que con `TODO`, borra el marcador una vez corregido el error, pero conserva el comentario de documentación, que sigue siendo cierto.

---

Un buen comentario explica **por qué** el código hace algo, no **qué** hace. El código ya muestra qué ocurre; repetirlo con palabras solo añade ruido y queda obsoleto en cuanto cambia el código:
```swift
// set timeout to 30
let timeout = 30
```
La razón que hay detrás del número es lo que el lector no puede adivinar:
```swift
// the server drops idle connections after 35 seconds, so stop earlier
let timeout = 30
```
Si un comentario solo repite la línea que tiene debajo, bórralo o reemplázalo por la razón.
