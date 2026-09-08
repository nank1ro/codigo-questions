Una **extensión** añade funcionalidad nueva a un tipo existente: un tipo de la biblioteca estándar como `Int` o `String`, o un struct o una clase escritos por ti.
Escribes la palabra clave `extension` seguida del nombre del tipo, y pones los miembros nuevos entre llaves:
```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(4.squared()) // 16
```
Dentro de la extensión, `self` es el valor sobre el que se llama al método: en `4.squared()` es `4`. Una vez que la extensión existe, cada `Int` del programa tiene el método nuevo, exactamente como si hubiera formado parte de `Int` desde el principio.

---

Las extensiones funcionan con cualquier tipo, incluso con aquellos de los que no tienes el código fuente. `String` proviene de la biblioteca estándar, pero aun así puedes darle métodos nuevos:
```swift
extension String {
    func whisper() -> String {
        return self.lowercased() + "..."
    }
}
print("HELLO".whisper()) // hello...
```
Dentro de una extensión puedes omitir `self.` al llamar a otros miembros del tipo: `lowercased()` a secas significa `self.lowercased()`.

---

Una extensión no crea un tipo nuevo ni copia el antiguo: añade miembros al propio tipo, de modo que cada valor existente y futuro de ese tipo los obtiene.
Por eso las extensiones son tan útiles con tipos que no puedes editar, como los de la biblioteca estándar o los de un framework: no puedes abrir el archivo donde `Int` está definido, pero puedes extenderlo desde cualquier archivo de tu programa.
```swift
extension Int {
    func isDivisible(by other: Int) -> Bool {
        return self % other == 0
    }
}
let n = 12
print(n.isDivisible(by: 4)) // true
```

---

Además de métodos, una extensión puede añadir **propiedades calculadas**: propiedades que no almacenan un valor, sino que lo calculan cada vez que se leen.
Una propiedad calculada se declara con `var`, una anotación de tipo y un cuerpo entre llaves que devuelve el valor:
```swift
extension Int {
    var isNegative: Bool {
        return self < 0
    }
}
print((-3).isNegative) // true
print(7.isNegative)    // false
```
Se lee como cualquier propiedad, sin paréntesis: `7.isNegative`, no `7.isNegative()`.

---

Las propiedades calculadas también encajan de forma natural en las extensiones de `String`. El método `reversed()` devuelve los caracteres en orden inverso, y `String(...)` los convierte de nuevo en una cadena:
```swift
extension String {
    var backwards: String {
        return String(reversed())
    }
}
print("swift".backwards) // tfiws
```
Como con los métodos, `reversed()` dentro de la extensión significa `self.reversed()`.

---

Las extensiones pueden añadir propiedades calculadas pero **no propiedades almacenadas**: esto no compila:
```swift
extension Int {
    var label = "number" // error: extensions must not contain stored properties
}
```
Una propiedad almacenada necesita espacio dentro de cada instancia del tipo. Los valores `Int` ya existen por todo tu programa, e incluso en código compilado mucho antes de tu extensión, así que su disposición en memoria no puede cambiar. Una propiedad calculada no necesita espacio, porque es simplemente código que se ejecuta cuando se lee la propiedad.

---

`Int`, `String`, los arrays y los structs son **tipos de valor**: un método no puede cambiar el valor sobre el que se llama a menos que esté marcado como `mutating`. Las extensiones también pueden añadir métodos mutantes:
```swift
extension Int {
    mutating func increment() {
        self += 1
    }
}
var count = 1
count.increment()
print(count) // 2
```
Dentro de un método mutante puedes asignar a `self`. El valor debe estar almacenado en una variable `var`: llamar a `increment()` sobre una constante `let` es un error de compilación.

---

Un método mutante puede tomar parámetros como cualquier otro método, y puede reemplazar `self` por completo en lugar de actualizarlo in situ:
```swift
extension Int {
    mutating func reset(to value: Int) {
        self = value
    }
}
var score = 42
score.reset(to: 0)
print(score) // 0
```

---

Una extensión puede añadir **inicializadores** nuevos a un tipo. Para un struct este es el mejor lugar para ponerlos: un `init` escrito dentro del cuerpo del struct reemplaza el inicializador miembro a miembro automático, mientras que uno añadido en una extensión lo conserva.
El inicializador nuevo normalmente delega en uno existente con `self.init(...)`:
```swift
struct Size {
    var width: Double
    var height: Double
}
extension Size {
    init(square side: Double) {
        self.init(width: side, height: side)
    }
}
let a = Size(square: 3)          // from the extension
let b = Size(width: 2, height: 5) // memberwise, still available
```

---

Las extensiones no son solo para tipos ajenos. Una forma común de organizar tu propio código es mantener las propiedades almacenadas en el cuerpo del struct o de la clase, y añadir el comportamiento en una o más extensiones, cada una agrupando miembros relacionados:
```swift
struct Circle {
    var radius: Double
}
extension Circle {
    var diameter: Double {
        return radius * 2
    }
    func grown(by amount: Double) -> Circle {
        return Circle(radius: radius + amount)
    }
}
```
Los miembros añadidos en una extensión pueden usar las propiedades almacenadas directamente, exactamente como si estuvieran escritos dentro del tipo.

---

Una extensión también puede hacer que un tipo conforme un **protocolo**, una lista de requisitos que el tipo promete implementar. Escribe el nombre del protocolo después del nombre del tipo, separado por dos puntos, y añade los miembros requeridos en el cuerpo.
`CustomStringConvertible` es un protocolo estándar con un único requisito, una propiedad calculada `description` de tipo `String`, que `print` usa para mostrar el valor:
```swift
struct Dog {
    var name: String
}
extension Dog: CustomStringConvertible {
    var description: String {
        return "Dog named \(name)"
    }
}
print(Dog(name: "Rex")) // Dog named Rex
```
Mantener cada conformidad con un protocolo en su propia extensión es la forma habitual de organizar un tipo en Swift.

---

`Array` es un tipo genérico: `[Int]` y `[String]` son ambos arrays, con un tipo **`Element`** distinto. Una extensión de `Array` se aplica a todos ellos, lo cual es un problema cuando el miembro nuevo solo tiene sentido para algunos elementos: no puedes sumar números que son cadenas.
Una cláusula `where` restringe la extensión a los arrays cuyo `Element` es de un tipo dado:
```swift
extension Array where Element == Int {
    var largest: Int {
        var result = Int.min
        for number in self {
            if number > result {
                result = number
            }
        }
        return result
    }
}
print([3, 9, 2].largest) // 9
```
`[3, 9, 2].largest` funciona, mientras que `["a", "b"].largest` es un error de compilación: la propiedad no existe en `[String]`.

---

Las extensiones pueden añadir miembros **estáticos**: propiedades y métodos que pertenecen al propio tipo en lugar de a un solo valor, marcados con la palabra clave `static` y accesibles a través del nombre del tipo.
Un `static let` está permitido aunque almacene un valor, porque solo hay una copia para todo el tipo, no una por instancia:
```swift
extension Int {
    static let answer = 42
    static func zeroes(_ count: Int) -> [Int] {
        return Array(repeating: 0, count: count)
    }
}
print(Int.answer)     // 42
print(Int.zeroes(3))  // [0, 0, 0]
```
Un miembro estático no tiene ningún valor `self` sobre el que trabajar: `Int.answer` se lee en el tipo, no en un número.

---

Los métodos estáticos en las extensiones son un buen hogar para pequeñas funciones de fábrica que construyen un valor del tipo. `String(repeating:count:)` es el inicializador estándar que repite un fragmento de texto un número de veces:
```swift
extension String {
    static func dashes(_ count: Int) -> String {
        return String(repeating: "-", count: count)
    }
}
print(String.dashes(4)) // ----
```

---

Las extensiones solo pueden **añadir** miembros, nunca reemplazar o sobrescribir los existentes. `override` pertenece a las subclases, que son un tipo distinto de su clase padre; una extensión es el mismo tipo, así que declarar un método que ya existe es un error de redeclaración:
```swift
struct Dog {
    func speak() -> String {
        return "Woof"
    }
}
extension Dog {
    func speak() -> String { // error: invalid redeclaration of 'speak()'
        return "Bark"
    }
}
```
Si necesitas un comportamiento distinto, añade un método con un nombre nuevo, o escribe una subclase cuando el tipo sea una clase.
