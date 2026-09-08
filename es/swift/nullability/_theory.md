A veces un valor simplemente falta: un usuario sin segundo nombre, una búsqueda que no encuentra nada, un texto que no se puede convertir en un número.
Swift representa un valor faltante con `nil`, pero una variable normal nunca puede contenerlo:
```swift
var age: Int = nil // error: 'nil' cannot initialize type 'Int'
```
Para permitir un valor faltante declaras un tipo **opcional** añadiendo un signo de interrogación `?` después del tipo.
Un `Int?` contiene un `Int` o `nil`:
```swift
var age: Int? = 30
age = nil // permitido
```
Una variable opcional declarada sin valor comienza como `nil`.

---

Puedes comparar un opcional con `nil` usando `==` y `!=`, y también puedes compararlo directamente con un valor simple del tipo envuelto:
```swift
var score: Int? = 10
print(score == nil) // false
print(score == 10)  // true
```
Recuerda que `Int?` e `Int` son dos tipos diferentes: un `Int?` puede estar vacío, un `Int` nunca lo está.

---

Un opcional es como una caja: antes de usar el valor de dentro tienes que abrirla, lo que Swift llama **desenvolver**.
La forma más rápida es el **desenvolvimiento forzado** con un signo de exclamación `!`:
```swift
let score: Int? = 10
print(score! + 5) // 15
```
El `!` le dice a Swift "estoy seguro de que aquí hay un valor". Si te equivocas y el opcional es `nil`, el programa se detiene inmediatamente con un fallo en tiempo de ejecución:
```swift
let missing: Int? = nil
print(missing! + 5) // Fatal error: Unexpectedly found nil
```
Por eso el desenvolvimiento forzado se considera peligroso: úsalo solo cuando estés seguro de que el valor existe.

---

El desenvolvimiento forzado solo es seguro cuando ya has comprobado que el opcional no es `nil`:
```swift
if score != nil {
    print(score! * 2)
}
```

---

Comprobar `nil` y luego desenvolver forzadamente es tedioso. Swift ofrece el **enlace opcional** con `if let`, que desenvuelve el opcional y guarda el valor en una nueva constante en un solo paso:
```swift
let score: Int? = 10
if let value = score {
    print("Score: \(value)") // value es un Int, no un Int?
} else {
    print("No score")
}
```
El cuerpo del `if` solo se ejecuta cuando el opcional contiene un valor; dentro de él `value` es un `Int` simple y no necesita `!`.

---

Cuando un valor faltante significa "detente aquí", `guard let` es más claro que `if let`.
Desenvuelve el opcional y, si eso falla, ejecuta el bloque `else`, que debe salir del ámbito actual (con `return`, `break`, `continue` o `throw`):
```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("Nobody here")
        return
    }
    print("Hello, \(name)!") // name es un String a partir de aquí
}
```
A diferencia de `if let`, la constante desenvuelta sigue disponible durante el resto de la función, así que el camino principal no queda anidado dentro de un `if`.

---

Un uso típico de `guard let` es validar la entrada de una función al principio y devolver un valor de respaldo cuando falta:
```swift
func length(of text: String?) -> Int {
    guard let text = text else { return 0 }
    return text.count
}
```

---

Muy a menudo lo único que quieres de un opcional es su valor o un valor predeterminado.
El **operador de fusión de nil** `??` hace exactamente eso: desenvuelve el opcional si tiene un valor, y en caso contrario devuelve el valor a su derecha:
```swift
let score: Int? = nil
let points = score ?? 0 // points es un Int igual a 0
```
El valor predeterminado debe tener el mismo tipo que el valor envuelto.
Puedes encadenar varios `??`: gana el primer valor que no sea `nil`.
```swift
let a: Int? = nil
let b: Int? = 7
print(a ?? b ?? 0) // 7
```

---

`??` es la forma más corta de convertir un opcional en un valor simple cuando existe un valor predeterminado razonable:
```swift
func volume(from setting: Int?) -> Int {
    return setting ?? 50
}
```

---

Al encadenar `??`, Swift evalúa de izquierda a derecha y se detiene en el primer valor que no sea `nil`; el último valor predeterminado se usa solo cuando todos los opcionales anteriores son `nil`.

---

Acceder a una propiedad o llamar a un método en un opcional requeriría desenvolverlo primero.
El **encadenamiento opcional** con `?.` lo hace por ti: si el opcional es `nil` toda la expresión se convierte en `nil`, en caso contrario el acceso continúa:
```swift
let name: String? = "swift"
let upper = name?.uppercased() // String? que contiene "SWIFT"
```
El resultado siempre es un opcional, incluso cuando la propiedad en sí no lo es.
Las cadenas pueden ser tan largas como necesites, y se combinan bien con `??`:
```swift
class User {
    var nickname: String? = "ace"
}
let user: User? = User()
print(user?.nickname?.count ?? 0) // 3
```

---

El encadenamiento opcional brilla cuando los datos pueden faltar en varios niveles: un objeto puede ser `nil`, y una de sus propiedades también puede serlo.
Una única cadena `?.` maneja ambos casos sin ningún `if`.

---

Un solo `if let` o `guard let` puede desenvolver varios opcionales a la vez: separa los enlaces con comas.
El cuerpo se ejecuta solo si todos los opcionales tienen un valor:
```swift
let first: String? = "Ada"
let last: String? = "Lovelace"
if let first = first, let last = last {
    print("\(first) \(last)")
}
```
También puedes añadir una condición booleana después de los enlaces, como `if let n = number, n > 0`.

---

Enlazar varios opcionales en un solo `if let` mantiene el código plano: una única rama `else` cubre cualquier valor faltante.

---

Muchas operaciones pueden fallar, y Swift informa del fallo devolviendo un opcional.
Convertir texto en un número es el ejemplo clásico: `Int("42")` devuelve un `Int?` que contiene `42`, mientras que `Int("abc")` devuelve `nil`.
`Int("3.5")` también es `nil`, porque el texto no es un número entero; usa `Double("3.5")` para decimales.
```swift
let typed = "42"
if let number = Int(typed) {
    print(number + 1) // 43
}
```
Otros ejemplos son `array.first` (`nil` para un array vacío) y `dictionary[key]` (`nil` cuando falta la clave).

---

Como una conversión puede fallar, su resultado siempre es un opcional y debe desenvolverse antes de usarlo, incluso cuando estés seguro de que el texto es un número válido.

---

Las conversiones que pueden fallar combinan de forma natural con `guard let`: convertir, salir si el resultado es `nil`, y luego trabajar con el valor simple.

---

A veces quieres transformar el valor dentro de un opcional y mantener el resultado opcional, sin desenvolver y volver a envolver a mano.
Los opcionales tienen un método `map`: aplica la clausura al valor si existe alguno, y devuelve `nil` en caso contrario.
```swift
let score: Int? = 10
let doubled = score.map { $0 * 2 } // Int? que contiene 20
let missing: Int? = nil
let stillMissing = missing.map { $0 * 2 } // nil
```
Combinado con una conversión que puede fallar, forma un pipeline compacto: `Int(text).map { $0 + 1 }`.
