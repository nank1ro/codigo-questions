Cada valor en Swift tiene un **tipo**, que le dice al compilador qué clase de dato es y qué puedes hacer con él.
Los tipos básicos son:
- `Int`: un número entero, como `42` o `-7`
- `Double`: un número con parte decimal, como `3.14`
- `String`: un fragmento de texto, como `"Hello"`
- `Character`: un solo carácter, como `"a"`
- `Bool`: o bien `true` o bien `false`

Puedes indicar el tipo de una constante o variable con una **anotación de tipo**: dos puntos y el nombre del tipo después del nombre:
```swift
let age: Int = 36
let name: String = "Ada"
```
Un valor de un tipo no se puede almacenar en una constante de otro tipo: `let age: Int = "36"` es un error de compilación.

---

La mayoría de las veces no escribes la anotación de tipo: Swift **infiere** el tipo a partir del valor que asignas, siguiendo unas pocas reglas de literales:
- un número sin punto decimal, como `42`, es un `Int`
- un número con punto decimal, como `3.14`, es un `Double`
- el texto entre comillas dobles es un `String`
- `true` y `false` son `Bool`
```swift
let count = 42     // Int
let price = 9.99   // Double
let name = "Ada"   // String
let isOpen = true  // Bool
```
Swift también tiene `Float`, un número decimal que usa la mitad de memoria que un `Double` pero es menos preciso, así que un literal decimal nunca se infiere como `Float`: debes pedirlo con una anotación.
De la misma manera, `"a"` se infiere como `String`, así que un `Character` siempre necesita una anotación.

---

La función `type(of:)` devuelve el tipo de un valor, lo que resulta útil para comprobar qué infirió Swift:
```swift
print(type(of: 42))    // Int
print(type(of: 2.5))   // Double
print(type(of: "hi"))  // String
```
Cuando quieres un tipo distinto del inferido, añade una anotación. Un literal de número entero se puede almacenar en una constante `Double` o `Float`, y un literal de un carácter en una constante `Character`:
```swift
let ratio: Double = 3       // 3.0, not an Int
let half: Float = 0.5
let initial: Character = "S"
print(type(of: ratio))      // Double
```

---

Swift nunca convierte entre tipos numéricos por sí solo: sumar un `Int` a un `Double` es un error de compilación, aunque ambos sean números.
```swift
let apples = 3
let price = 1.5
let total = apples * price // error: Int and Double can't be mixed
```
Para combinarlos creas un nuevo valor del tipo que necesitas, pasando el valor al inicializador del tipo:
```swift
let total = Double(apples) * price // 4.5
```
Funciona igual a la inversa: `Int(4.5)` produce un `Int`, conservando solo la parte entera del número.

---

`Int(x)` no redondea: **trunca**, simplemente descartando la parte decimal, así que `Int(3.99)` es `3` e `Int(-3.99)` es `-3`.
Para redondear al número entero más cercano, llama primero a `rounded()` sobre el `Double` y luego convierte:
```swift
let x = 3.99
print(Int(x))            // 3
print(Int(x.rounded()))  // 4
```
Los valores intermedios como `2.5` se redondean lejos del cero: `2.5` se convierte en `3.0` y `-2.5` en `-3.0`.

---

El tipo de los operandos decide cómo funciona la división. Cuando ambos son `Int`, el operador `/` realiza una **división entera**: el resultado es un `Int` y el resto se descarta.
Cuando al menos un operando es un `Double`, `/` realiza una división en coma flotante y conserva la parte decimal:
```swift
print(7 / 2)              // 3
print(7.0 / 2)            // 3.5
let slices = 7
print(Double(slices) / 2) // 3.5
```
Así que para obtener un resultado decimal a partir de dos valores `Int` debes convertir al menos uno de ellos a `Double` **antes** de dividir: `Double(7 / 2)` es `3.0`, porque la división entera ya ha ocurrido.

---

Cuando una función debe devolver un resultado decimal calculado a partir de números enteros, convierte los operandos a `Double` antes de dividir y declara el tipo de retorno como `Double`:
```swift
func ratio(_ part: Int, _ total: Int) -> Double {
    return Double(part) / Double(total)
}
print(ratio(1, 4)) // 0.25
```
Recuerda que el `count` de un array también es un `Int`, así que necesita la misma conversión.

---

Los números y las cadenas se convierten con la misma sintaxis de inicializador. `String(42)` convierte un número en el texto `"42"`, exactamente igual que al interpolarlo con `"\(42)"`.
La dirección opuesta puede fallar, porque no todo texto es un número, así que `Int("42")` devuelve un `Int?` **opcional**: aquí contiene `42`, pero `Int("hello")` es `nil`.
Como aprendiste en las lecciones de nulabilidad, puedes proporcionar un valor de respaldo con `??` o desenvolverlo con `if let`:
```swift
let typed = "42"
let number = Int(typed) ?? 0
print(number + 1) // 43
```

---

`Int(text)` tiene éxito solo cuando todo el texto es un número entero válido, con un signo opcional:
```swift
print(Int("42"))   // Optional(42)
print(Int("-7"))   // Optional(-7)
print(Int("3.5"))  // nil, not a whole number
print(Int(" 42"))  // nil, spaces are not allowed
print(Int("abc"))  // nil
```
Para texto decimal usa `Double(text)`, que devuelve un `Double?` de la misma manera: `Double("3.5")` es `Optional(3.5)`.

---

Un **alias de tipo** le da un nuevo nombre a un tipo existente, con la palabra clave `typealias`:
```swift
typealias Score = Int
let best: Score = 100
print(best + 1) // 101
```
`Score` e `Int` son el mismo tipo, así que se mezclan libremente. Un alias no añade ninguna seguridad: solo hace que el código se lea mejor cuando un tipo sencillo tiene un significado específico en tu programa.

---

Un `Int` usa 64 bits, así que solo puede representar números en un rango fijo. Los valores mayor y menor están disponibles como `Int.max` e `Int.min`:
```swift
print(Int.max) // 9223372036854775807
print(Int.min) // -9223372036854775808
```
Superar esos límites se llama **overflow**. A diferencia de muchos otros lenguajes, Swift no da la vuelta silenciosamente al otro extremo del rango: una operación que desborda es un **error en tiempo de ejecución** que detiene el programa.

---

`Int.max` e `Int.min` son útiles como valores iniciales cuando buscas un extremo: cualquier número real es menor que `Int.max`, así que es un valor inicial seguro para "el menor visto hasta ahora":
```swift
var smallest = Int.max
for number in [8, 3, 5] {
    if number < smallest {
        smallest = number
    }
}
print(smallest) // 3
```

---

Como viste en las lecciones de cadenas, iterar sobre una `String` te da un `Character` a la vez. Un `Character` no es una `String`, así que para usarlo como texto lo conviertes con `String(c)`.
Cuando el carácter es un dígito, la propiedad `wholeNumberValue` te da su valor numérico como un `Int?`: es `nil` para los caracteres que no son dígitos.
```swift
for c in "a1" {
    print(c.wholeNumberValue)
}
// nil
// Optional(1)
```

---

Como `Int(text)` y `Double(text)` devuelven `nil` en caso de fallo, comparar el resultado con `nil` te dice si un texto es un número de ese tipo:
```swift
print(Int("42") != nil)     // true
print(Double("4.2") != nil) // true
print(Double("42") != nil)  // true, a whole number is also a valid Double
```
Fíjate en la última línea: todo texto aceptado por `Int` también es aceptado por `Double`, así que comprueba primero `Int` cuando quieras distinguirlos.

---

A veces necesitas almacenar juntos valores de diferentes tipos. El tipo especial `Any` puede contener un valor de **cualquier** tipo, así que un array declarado como `[Any]` puede mezclar números, cadenas y booleanos:
```swift
let items: [Any] = [1, "two", true]
```
Cada elemento aún recuerda su tipo real, que `type(of:)` revela. Para trabajar con el valor como su tipo real usas un **cast condicional** con `as?`, que devuelve un opcional: contiene el valor cuando el tipo coincide y `nil` en caso contrario:
```swift
for item in items {
    if let number = item as? Int {
        print(number + 1) // runs only for 1
    }
}
```
`Any` es un último recurso: un array de un único tipo concreto es más seguro y más fácil de usar, así que prefierelo siempre que puedas.

---

Los casts condicionales se encadenan naturalmente con `else if` para manejar varios tipos posibles, convirtiendo cada uno al tipo que necesitas para el resultado:
```swift
let item: Any = 2.5
if let number = item as? Int {
    print(Double(number))
} else if let number = item as? Double {
    print(number)
}
```
Un `Int` almacenado en `Any` sigue siendo un `Int`: `as? Double` sobre él devuelve `nil`, porque `as?` comprueba el tipo, no convierte números.
