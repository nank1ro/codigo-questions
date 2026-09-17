En Swift un error es un **valor**, no un fallo. Cualquier tipo puede actuar como tal adoptando el protocolo `Error`, y un enum es la opción habitual porque sus casos nombran exactamente lo que puede salir mal:
```swift
enum LoginError: Error {
    case wrongPassword
}
```
Una función que puede fallar se marca con `throws`, e informa del fallo con `throw`:
```swift
func login(_ password: String) throws {
    if password != "swift" {
        throw LoginError.wrongPassword
    }
    print("welcome")
}
```
Llamar a semejante función necesita `try`, y la llamada debe vivir dentro de un bloque `do` seguido de un bloque `catch` que diga qué hacer cuando falla:
```swift
do {
    try login("hunter2")
} catch {
    print("login failed")
}
// login failed
```
Cuando se ejecuta `throw`, el resto del bloque `do` se omite y `catch` toma el control. Nada se interrumpe: el programa continúa después del `catch`.

---

Una función que lanza errores puede seguir devolviendo un valor. La palabra clave `throws` va entre la lista de parámetros y la flecha de retorno:
```swift
func square(_ n: Int) throws -> Int {
    if n < 0 {
        throw SquareError.negative
    }
    return n * n
}
```
Leyéndolo en voz alta: *square recibe un `Int`, puede lanzar errores y devuelve un `Int`*.

En el punto de llamada el valor solo existe cuando no se lanzó nada, así que la asignación vive dentro del bloque `do`:
```swift
do {
    let result = try square(4)
    print(result) // 16
} catch {
    print("failed")
}
```
El `try` no es un adorno opcional: el compilador rechaza la llamada sin él, así que quien lee siempre ve qué líneas pueden fallar.

---

Un `catch` sin patrón maneja todos los errores de la misma manera. La mayoría de las veces quieres reaccionar a un fallo concreto, así que un `catch` puede llevar un **patrón**: el caso que está dispuesto a manejar.
```swift
do {
    try check("")
} catch ValidationError.empty {
    print("the text is empty")
} catch {
    print("something else")
}
```
Swift prueba las cláusulas `catch` de arriba a abajo y ejecuta la primera cuyo patrón coincida.

El último `catch` no tiene patrón a propósito. Un `catch` con patrón solo cubre el caso que nombra, y Swift insiste en que cada error se maneje en algún sitio, así que un bloque `do` que enumera patrones necesita un `catch` final sin patrón que recoja el resto.

---

El orden importa. Swift compara el valor lanzado con cada patrón de `catch` en el orden en que están escritos y se detiene en la primera coincidencia, así que un `catch` sin patrón colocado primero se tragará todo lo que haya debajo. Mantén los casos específicos arriba y el `catch` general abajo.

Un error que no coincide con ninguno de los patrones no se ignora: cae en el `catch` final sin patrón.

---

Un caso de error puede llevar datos. Dale al caso **valores asociados** y el `throw` los rellena, así quien captura el error aprende no solo *qué* falló sino *cuánto*:
```swift
enum ValidationError: Error {
    case tooShort(minimum: Int)
}

throw ValidationError.tooShort(minimum: 8)
```
El `catch` correspondiente enlaza esos valores con `let`:
```swift
} catch ValidationError.tooShort(let minimum) {
    print("needs at least \(minimum) characters")
}
```
El nombre después de `let` lo eliges tú; es una nueva constante disponible solo dentro de ese bloque `catch`. Así un error lleva un mensaje útil sin que tengas que pegar números en cadenas en el punto donde ocurre el fallo.

---

Un enum suele contener todas las maneras en que un mismo trabajo puede fallar, un caso por motivo:
```swift
enum FormError: Error {
    case empty
    case tooLong
}
```
Escribir un `catch` por cada caso se vuelve repetitivo. En su lugar, captura el tipo entero de una vez y usa `switch` sobre el valor:
```swift
} catch let error as FormError {
    switch error {
    case .empty: print("empty")
    case .tooLong: print("too long")
    }
} catch {
    print("unknown")
}
```
`catch let error as FormError` significa *captura cualquier cosa que sea un `FormError` y llámala `error`*. Dentro del bloque `error` tiene el tipo del enum, así que `switch` ve los casos y comprueba que los cubriste todos. El `catch` final sin patrón sigue siendo obligatorio, porque algún otro tipo de error podría llegar a este bloque `do`.

---

Un validador se lee mejor cuando los rechazos van primero y el trabajo real queda sin indentar abajo. `guard` está hecho para eso: enuncia la condición que debe cumplirse, y su bloque `else` se ejecuta cuando no se cumple.
```swift
func priceFor(_ quantity: Int) throws -> Int {
    guard quantity > 0 else {
        throw OrderError.notPositive
    }
    return quantity * 3
}
```
El bloque `else` de un `guard` tiene que abandonar el ámbito actual, y `throw` es una de las formas de hacerlo, junto con `return`, `break` y `continue`. Varios `guard` apilados al principio de una función se leen como la lista de reglas que la entrada debe satisfacer.

---

A veces no te importa *por qué* falló algo, solo que fallara. `try?` convierte una llamada que lanza errores en un **opcional**: el valor si tiene éxito, `nil` si lanza un error.
```swift
enum ParseError: Error {
    case notANumber
}

func toInt(_ text: String) throws -> Int {
    guard let value = Int(text) else {
        throw ParseError.notANumber
    }
    return value
}

if let number = try? toInt("42") {
    print(number) // 42
}
```
No hay `do` ni `catch`: el fallo queda plegado en el opcional que ya sabes desenvolver. El precio es que el valor del error se descarta, así que recurre a `try?` solo cuando de verdad no haya nada que informar.

---

Como `try?` produce un opcional, el operador nil-coalescing `??` termina el trabajo aportando un respaldo:
```swift
let port = (try? readPort(text)) ?? 8080
```
Los paréntesis importan. De otro modo `try?` intentaría cubrir toda la expresión, incluido el `??`, y el compilador te pide ser explícito acerca de dónde termina la llamada que puede fallar.

Lee la línea como una sola frase: *usa el puerto que logramos leer, si no 8080*. Dos líneas de `do`/`catch` se colapsan en una cuando la recuperación de verdad es solo un valor por defecto.

---

Hay una tercera forma: `try!`. Le dice al compilador *esta llamada no puede fallar*, así que no hay `do`, ni `catch`, ni opcional. Si de todas formas falla, el programa se detiene inmediatamente.
```swift
let pattern = try! Regex("[0-9]+")
```
Esa es la situación donde `try!` es defendible: el argumento es un literal escrito por ti, en tu propio código fuente, y si está mal el programa está roto y debería detenerse en tu primera ejecución de pruebas.

Cualquier cosa que llegue en tiempo de ejecución — una línea escrita por un usuario, un archivo, una respuesta de red — puede estar mal de maneras que no puedes ver mientras escribes el código, y `try!` sobre ella convierte un fallo recuperable en un cierre inesperado delante del usuario. Usa `do`/`catch` o `try?` ahí.

---

Cuando una función lanza un error, todo lo que va después del `throw` se omite — incluida la línea que se suponía que cerraba el archivo o liberaba el bloqueo. `defer` lo resuelve: registra un bloque ahora y lo ejecuta cuando termina el ámbito actual, ocurra como ocurra.
```swift
func load() throws {
    print("open")
    defer { print("close") }
    throw FileError.missing
}
```
La llamada imprime `open`, luego `close`, y solo entonces el error viaja hacia quien llamó. Si la función hubiera devuelto con normalidad, `close` igual se habría impreso — de eso se trata. Pon la limpieza justo al lado de la preparación y deja de preocuparte por qué salida toma el código.

---

Un ámbito puede registrar más de un `defer`. Se ejecutan en orden **inverso**: el último registrado es el primero en ejecutarse.

Esa no es una regla arbitraria. Las limpiezas suelen deshacer una preparación que ocurrió en orden — abrir el archivo, luego bloquearlo — y deshacer tiene que ir al revés: desbloquear, luego cerrar. El orden inverso hace de cada `defer` la imagen especular de la línea que tiene encima.

---

Una función que recibe un cierre tiene un problema: no puede saber si el cierre que le entregan lanzará un error. Marcar la función como `throws` obligaría a quien la llama a escribir `try`, incluso a quien pasa un cierre inofensivo. `rethrows` dice *yo lanzo solo si el cierre que me diste lanza*:
```swift
func applyTwice(_ value: Int, _ transform: (Int) throws -> Int) rethrows -> Int {
    return try transform(transform(value))
}
```
Dentro del cuerpo igual escribes `try`, porque la llamada de verdad podría fallar. En el punto de llamada el compilador mira el cierre que pasaste:
```swift
let doubled = applyTwice(3, { (n: Int) -> Int in n * 2 }) // no se necesita try
```
La biblioteca estándar usa esto por todas partes — `map`, `filter` y `sorted(by:)` son todas `rethrows` — razón por la que nunca escribes `try` delante de un `map` ordinario.

---

Un bloque `do` no está limitado a un solo tipo de error. Cada paso puede fallar a su manera, y cada fallo tiene su propio `catch`:
```swift
do {
    let text = try load(false)
    let value = try parse(text)
    print(value)
} catch NetworkError.offline {
    print("offline")
} catch ParseError.badFormat {
    print("bad format")
} catch {
    print("unknown")
}
```
El primer `try` que lanza un error termina el bloque, así que los pasos posteriores nunca se ejecutan — el valor sencillamente nunca existió. Eso es lo que hace legible esta forma: el camino feliz queda en una sola línea recta arriba, y todas las maneras en que puede salir mal quedan listadas debajo.

---

Dónde se sitúa el bloque `do` decide cuánto cuesta un solo fallo. Ponlo **dentro** del bucle y cada elemento obtiene su propio intento, así un valor malo se omite y el resto sigue ejecutándose:
```swift
for age in [4, -1, 7] {
    do {
        print(try label(age))
    } catch {
        print("skipped")
    }
}
```
Envolver todo el bucle en un solo `do` en cambio se detendría en el primer error y nunca llegaría a `7`. Ninguna opción está mal — es la diferencia entre *un elemento malo* y *rendirse*.

---

Todo en este capítulo responde a una pregunta: ¿quién se encarga del fallo?

Una función que lanza errores se niega a responderla. Nombra lo que salió mal — un caso de un enum `Error`, que lleva lo que el gestor vaya a necesitar — y pasa la decisión hacia arriba. Quien llama entonces elige una herramienta: `do`/`catch` para reaccionar caso por caso, `try?` y `??` para recurrir a un valor por defecto, `defer` para limpiar al salir, pase lo que pase.

Esa separación es todo el punto. La función que detecta el problema rara vez sabe qué debería pasar después, y el código que lo sabe rara vez quiere repetir la comprobación.
