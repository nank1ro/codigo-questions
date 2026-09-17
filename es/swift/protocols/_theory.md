Un **protocolo** describe qué debe tener un tipo, sin decir cómo. Es una lista de requisitos — propiedades y métodos — que cualquier tipo que lo adopte promete proporcionar.

Lo declaras con la palabra clave `protocol`. Un requisito de propiedad se escribe con su tipo seguido de un bloque que indica cómo se puede acceder: `{ get }` significa que el tipo debe dejarte al menos leerla.
```swift
protocol Named {
    var name: String { get }
}
```
Un tipo **conforma** al protocolo escribiendo su nombre después de dos puntos y proporcionando todo lo que el protocolo pide:
```swift
struct Cat: Named {
    var name: String
}

let cat = Cat(name: "Luna")
print(cat.name) // Luna
```
Un protocolo no contiene datos propios: es un contrato. Todo tipo que lo satisfaga puede tratarse de la misma manera por el resto de tu código.

---

Un protocolo también puede requerir **métodos**. Escribes la firma —nombre, parámetros y tipo de retorno— y te detienes ahí, sin cuerpo:
```swift
protocol Greeter {
    func greet() -> String
}
```
Un tipo que conforma debe declarar un método con exactamente esa firma, y es él quien aporta el cuerpo:
```swift
struct Robot: Greeter {
    func greet() -> String {
        return "BEEP"
    }
}

print(Robot().greet()) // BEEP
```
Si algo difiere —el nombre, el tipo de un parámetro, el tipo de retorno—, el tipo no conforma, y el compilador te dice qué requisito falta.

---

Un requisito de propiedad siempre indica cómo se puede usar la propiedad. `{ get }` solo pide que el valor se pueda leer; `{ get set }` pide que se pueda leer **y** asignar:
```swift
protocol Account {
    var owner: String { get }
    var balance: Int { get set }
}
```
Un tipo que conforma siempre puede dar más de lo que pide el contrato: una propiedad almacenada `var` satisface `{ get }` perfectamente. Nunca puede dar menos —una constante `let`, o una propiedad computada de solo lectura, no puede satisfacer `{ get set }`.

---

Los protocolos no se limitan a los structs. Una **clase** conforma exactamente de la misma manera, poniendo el protocolo después de dos puntos:
```swift
protocol Openable {
    func open() -> String
}

class Door: Openable {
    func open() -> String {
        return "creak"
    }
}
```
Si la clase además hereda de otra clase, la superclase va primero en la lista y los protocolos la siguen. Un tipo puede adoptar varios protocolos a la vez, separados por comas.

---

Un **enum** también puede conformar. No tiene propiedades almacenadas, así que un requisito de propiedad normalmente se cumple con una propiedad computada que hace `switch` sobre los casos:
```swift
protocol Priced {
    var price: Int { get }
}

enum Ticket: Priced {
    case child, adult

    var price: Int {
        switch self {
        case .child: return 5
        case .adult: return 12
        }
    }
}

print(Ticket.adult.price) // 12
```
Structs, clases y enums: los tres adoptan protocolos de la misma manera, y el código escrito contra el protocolo funciona con todos ellos.

---

Un protocolo normalmente reúne más de un requisito, y un tipo que conforma debe satisfacerlos todos:
```swift
protocol Vehicle {
    var wheels: Int { get }
    func move() -> String
}

struct Bike: Vehicle {
    var wheels = 2

    func move() -> String {
        return "pedalling"
    }
}
```
El orden de los requisitos dentro de las llaves no importa, y tampoco importa el orden en que el tipo que conforma los proporciona: el compilador solo comprueba que no falte nada.

---

Un struct es un tipo de valor, así que un método que cambia una de sus propiedades almacenadas debe marcarse `mutating`. Cuando ese método es un requisito del protocolo, el protocolo también tiene que indicarlo:
```swift
protocol Togglable {
    mutating func toggle()
}

struct Light: Togglable {
    var isOn = false

    mutating func toggle() {
        isOn = !isOn
    }
}

var lamp = Light()
lamp.toggle()
print(lamp.isOn) // true
```
Sin `mutating` en el protocolo, un struct nunca podría satisfacer el requisito. Las clases son tipos de referencia y nunca necesitan la palabra clave: una clase cumple un requisito `mutating` con un método normal. Llamar a un método mutating necesita un `var` —sobre un `let` es un error de compilación.

---

La conformidad no tiene que declararse junto al tipo. Una **extensión** puede añadirla más tarde, lo que mantiene la propia declaración del tipo centrada en sus datos:
```swift
protocol Resettable {
    mutating func reset()
}

struct Timer {
    var seconds = 0
}

extension Timer: Resettable {
    mutating func reset() {
        seconds = 0
    }
}
```
Esto también funciona con tipos que no escribiste tú: puedes hacer que un tipo de la biblioteca estándar conforme a uno de tus protocolos sin tocar su código fuente.

---

Una extensión de un **protocolo** es una herramienta distinta: añade miembros a todo tipo que conforme, presente y futuro. Así es como le das a un requisito una **implementación por defecto**:
```swift
protocol Greeter {
    var name: String { get }
    func greet() -> String
}

extension Greeter {
    func greet() -> String {
        return "Hi, \(name)"
    }
}

struct Person: Greeter {
    var name: String
}

print(Person(name: "Ada").greet()) // Hi, Ada
```
`Person` nunca escribe `greet()` y aun así conforma. Dentro de la extensión del protocolo puedes usar cualquier requisito del protocolo —aquí `name`— porque cualquier tipo que conforme tiene garantizado tenerlo.

---

Una extensión de protocolo también puede añadir miembros que el protocolo nunca listó como requisitos. Son comodidades extra, disponibles en todo tipo que conforme:
```swift
protocol Sized {
    var count: Int { get }
}

extension Sized {
    var isEmpty: Bool {
        return count == 0
    }
}
```
`isEmpty` no es un requisito, así que un tipo que conforma no tiene que proporcionarlo —simplemente lo obtiene.

---

Un protocolo puede construirse sobre otro. Escribir el nombre de un protocolo después de los dos puntos hace que el nuevo protocolo **herede** todos los requisitos del anterior:
```swift
protocol Named {
    var name: String { get }
}

protocol Aged: Named {
    var age: Int { get }
}
```
Un tipo que conforma a `Aged` debe proporcionar `age` *y* `name`, y cuenta como un tipo `Named` en todas partes. Un protocolo puede heredar de varios protocolos a la vez, separados por comas.

---

Una implementación por defecto es un respaldo, no una regla. Si un tipo que conforma proporciona su propia versión de un requisito, es esa versión la que se ejecuta:
```swift
protocol Priced {
    var price: Int { get }
}

extension Priced {
    var price: Int { return 0 }
}

struct Ticket: Priced {
    var price = 12
}

print(Ticket().price) // 12, no 0
```
El valor por defecto solo rellena los huecos que el tipo deja abiertos.

---

La biblioteca estándar está construida a partir de protocolos, y tus propios tipos pueden adoptarlos.

`Equatable` le da a un tipo el operador `==`. Para un struct cuyas propiedades almacenadas son todas `Equatable`, basta con declarar la conformidad —Swift escribe `==` por ti:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

print(Point(x: 1, y: 2) == Point(x: 1, y: 2)) // true
```
`Comparable` hereda de `Equatable` y añade ordenación. Implementas un único operador, `<`, escrito como una `static func` que toma los dos valores, y obtienes `>`, `<=`, `>=`, además de `sorted()`, `min()` y `max()` sobre colecciones gratis:
```swift
struct Version: Comparable {
    var number: Int

    static func < (lhs: Version, rhs: Version) -> Bool {
        return lhs.number < rhs.number
    }
}
```

---

`CustomStringConvertible` decide qué muestra `print` para tu tipo. Su único requisito es una propiedad `description`:
```swift
struct Coin: CustomStringConvertible {
    var value: Int

    var description: String {
        return "\(value)c"
    }
}

print(Coin(value: 25)) // 25c
```
Sin la conformidad, imprimir un struct recurre por defecto a un volcado como `Coin(value: 25)`, y una propiedad `description` por sí sola no cambia nada —`print` busca el protocolo. La interpolación de cadenas también usa `description`.

---

El nombre de un protocolo por sí solo no es un tipo, es una restricción, así que Swift te pide que digas cuál de dos cosas quieres decir.

`some Shape` significa *un tipo concreto que conforma*, fijado en tiempo de compilación. Quien llama nunca sabe cuál es, pero siempre es el mismo:
```swift
func unitSquare() -> some Shape {
    return Square(side: 1)
}
```
`any Shape` significa *una caja que puede contener cualquier tipo que conforme*, y dos valores de ese tipo pueden contener tipos diferentes. Lo necesitas siempre que el tipo concreto pueda variar, como dentro de un array mixto:
```swift
let shapes: [any Shape] = [Square(side: 2), Rect(width: 2, height: 3)]
```
Ambos te dejan llamar a los requisitos del protocolo. Prefiere `some` cuando un único tipo es suficiente, porque no cuesta nada en tiempo de ejecución; recurre a `any` cuando realmente necesites mezclar tipos.
