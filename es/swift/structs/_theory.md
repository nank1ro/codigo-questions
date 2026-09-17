Una **estructura** (*struct*) es un tipo que diseñas tú mismo para mantener juntos valores relacionados. En lugar de manejar un `title` separado y un `pages` separado, describes un `Book` una vez y lo usas en todas partes.

Lo declaras con la palabra clave `struct`, y las variables escritas dentro de él son sus **propiedades almacenadas**:
```swift
struct Book {
    var title: String
    var pages: Int
}
```
`Book` ahora es un tipo, exactamente como `Int` o `String`. Accedes a una propiedad de una instancia con un punto:
```swift
let book = Book(title: "Swift", pages: 120)
print(book.title) // Swift
```

---

Nunca escribiste el código que construye un `Book`, y sin embargo `Book(title: "Swift", pages: 120)` funcionó. Swift lo escribe por ti: toda estructura recibe gratis un **inicializador miembro**, un inicializador cuyos parámetros son sus propiedades almacenadas, en el orden en que se declaran, y cada uno usa el nombre de la propiedad como etiqueta de argumento:
```swift
struct Point {
    var x: Int
    var y: Int
}

let p = Point(x: 3, y: 4)
print(p.x) // 3
```
Las clases no reciben esto gratis, que es una de las razones por las que las estructuras son la forma más rápida de modelar un valor.

---

A una propiedad almacenada se le puede dar un **valor por defecto** justo donde se declara. Swift infiere su tipo a partir de ese valor, así que puedes omitir la anotación de tipo:
```swift
struct Counter {
    var label: String
    var value = 0
}
```
El inicializador miembro convierte cada propiedad con valor por defecto en un argumento opcional: pásalo para sobrescribir el valor por defecto, omítelo para conservarlo.
```swift
let a = Counter(label: "clicks")
print(a.value) // 0

let b = Counter(label: "clicks", value: 7)
print(b.value) // 7
```

---

Una estructura también puede contener **métodos**: funciones escritas dentro de las llaves que trabajan sobre la instancia en la que se llaman. Dentro de un método usas los nombres de las propiedades directamente, sin ningún prefijo:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    func area() -> Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area()) // 12
```
Si un parámetro del método oculta el nombre de una propiedad, escribe `self.width` para referirte a la propiedad de la instancia.

---

Una **propiedad calculada** parece una propiedad pero se comporta como un método: no almacena nada, calcula su valor cada vez que la lees. Escribes el tipo y luego un bloque de código que devuelve el valor:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    var area: Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area) // 12, sin paréntesis
```
Las propiedades calculadas no forman parte del inicializador miembro, ya que no hay nada que almacenar. Usa una cuando el valor se deriva de los otros, y un método cuando el trabajo necesita parámetros.

---

Una estructura es un **tipo de valor**: asignarla a otra variable, o pasarla a una función, entrega una *copia*. Cambiar la copia deja el original intacto.
```swift
struct Point {
    var x: Int
}

var a = Point(x: 1)
var b = a
b.x = 99
print(a.x) // 1
```
Una clase es un **tipo de referencia**: `b = a` haría que ambos nombres apuntaran a la misma instancia, así que `b.x = 99` también cambiaría `a.x` a `99`.

Esa es la diferencia real entre ambos, y la razón por la que Swift modela la mayoría de los datos como estructuras: un valor que tienes no puede ser modificado a tus espaldas por el código que lo recibió.

---

Como una estructura es un valor, a un método no se le permite cambiar sus propiedades a menos que lo indiques con la palabra clave `mutating`:
```swift
struct Counter {
    var value = 0

    mutating func increase(by amount: Int) {
        value += amount
    }
}

var c = Counter()
c.increase(by: 5)
print(c.value) // 5
```
Un método mutante solo puede llamarse sobre una instancia almacenada en una `var`. Sobre una instancia `let` el valor está congelado, así que `c.increase(by: 5)` no compilaría.

---

Cuando el inicializador miembro no es la forma en que quieres que se construya tu tipo, escribe tu propio **inicializador**. Se declara con `init`, toma los parámetros que elijas y debe dar un valor a cada propiedad almacenada antes de terminar. Dentro de él, `self` es la instancia que se está creando:
```swift
struct Square {
    var side: Int

    init(_ side: Int) {
        self.side = side
    }
}

let s = Square(5)
print(s.side) // 5
```
Escribir un `init` dentro de las llaves de la estructura reemplaza al inicializador miembro, así que a partir de ahora `Square(side: 5)` ya no existe.

---

Algunos valores pertenecen al tipo mismo en lugar de a una instancia concreta: un código de moneda, un valor por defecto compartido, una fábrica que construye un caso común. Márcalos `static` y léelos a través del nombre del tipo:
```swift
struct Money {
    static let currency = "EUR"
    var amount: Int

    static func zero() -> Money {
        return Money(amount: 0)
    }
}

print(Money.currency)     // EUR
print(Money.zero().amount) // 0
```
Aquí `currency` se declara con `let` porque nunca cambia, así que es una constante compartida por todo el programa. `Money.currency` funciona sin crear ni un solo `Money`, mientras que `amount` necesita una instancia.

---

Dos estructuras no pueden compararse con `==` hasta que el tipo declara que lo soporta. Lo haces haciendo que conforme el **protocolo** `Equatable`, escrito después de dos puntos en la declaración:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

let a = Point(x: 1, y: 2)
let b = Point(x: 1, y: 2)
print(a == b) // true
```
No tienes que escribir `==` tú mismo: cuando cada propiedad almacenada ya es `Equatable`, Swift lo sintetiza por ti, comparando las propiedades una por una. Dos instancias son iguales cuando todas sus propiedades son iguales, que es exactamente lo que esperas de un valor.

---

Una estructura es un tipo como cualquier otro, así que puede almacenarse en un array, un diccionario o un conjunto, y cada herramienta que ya conoces sigue funcionando con ella:
```swift
struct Item {
    var name: String
    var price: Int
}

let items = [Item(name: "Tea", price: 3), Item(name: "Cake", price: 7)]

for item in items {
    print(item.name)
}

let names = items.map { $0.name }
let total = items.reduce(0) { $0 + $1.price }
print(total) // 10
```
Recuerda que el array contiene *copias*: leer `items[0]` en una variable y cambiarla no toca el array.
