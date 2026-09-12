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
print(r.area) // 12, no parentheses
```
Las propiedades calculadas no forman parte del inicializador miembro, ya que no hay nada que almacenar. Usa una cuando el valor se deriva de los otros, y un método cuando el trabajo necesita parámetros.
