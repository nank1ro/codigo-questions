Una **función de orden superior** es una función que recibe otra función como argumento, devuelve una, o ambas cosas. Ya conoces `map`, `filter`, `reduce` y `sorted(by:)`: reciben un cierre y lo aplican a los elementos de una colección. Swift tiene muchas más, y conocerlas te permite reemplazar bucles largos con una única línea legible.
`compactMap` funciona como `map`, pero el cierre devuelve un opcional y los resultados `nil` se descartan:
```swift
let words = ["3", "seven", "12"]
let numbers = words.compactMap { Int($0) }
print(numbers) // [3, 12]
```
`Int("seven")` es `nil`, así que ese elemento desaparece y el resultado es un `[Int]`, no un `[Int?]`.

---

`flatMap` es para los cierres que devuelven un **array**: en lugar de construir un array de arrays, une todos los arrays devueltos en un único resultado plano:
```swift
let teams = [["Ann", "Bob"], ["Cid"]]
print(teams.map { $0 })     // [["Ann", "Bob"], ["Cid"]]
print(teams.flatMap { $0 }) // ["Ann", "Bob", "Cid"]
```
El cierre también puede transformar cada array interno antes de aplanarlo, por ejemplo `teams.flatMap { $0.reversed() }` da `["Bob", "Ann", "Cid"]`.

---

Las tres variantes de `map` solo se diferencian en lo que devuelve el cierre:
- `map`: cualquier valor, un resultado por elemento
- `compactMap`: un opcional, los resultados `nil` se descartan
- `flatMap`: un array, todos los resultados se unen en un solo array

El cierre que se pasa a `flatMap` puede a su vez llamar a `map` sobre el array interno, anidando una transformación dentro de la otra:
```swift
let matrix = [[1, 2], [3]]
print(matrix.flatMap { row in row.map { $0 + 1 } }) // [2, 3, 4]
```

---

`reduce` construye un nuevo valor acumulado en cada paso, lo cual es un desperdicio cuando el resultado es un array o un diccionario. `reduce(into:)` le entrega al cierre el acumulador como un parámetro `inout`, de modo que puede modificarse en el lugar sin `return`:
```swift
let words = ["a", "b", "a"]
let counts = words.reduce(into: [String: Int]()) { result, word in
    result[word, default: 0] += 1
}
print(counts["a"]!) // 2
```
`[String: Int]()` crea un diccionario vacío, y `result[word, default: 0]` lee el recuento actual o `0` cuando la clave no existe.

---

Algunas funciones de orden superior responden una pregunta sobre la colección en lugar de transformarla. Todas reciben un cierre que devuelve un `Bool`:
- `first(where:)` devuelve el primer elemento que satisface el cierre, o `nil` si no hay ninguno
- `contains(where:)` devuelve `true` si al menos un elemento lo satisface
- `allSatisfy` devuelve `true` si todos los elementos lo satisfacen

```swift
let nums = [4, 9, 16]
print(nums.first(where: { $0 > 5 }))  // Optional(9)
print(nums.contains(where: { $0 > 5 })) // true
print(nums.allSatisfy { $0 > 5 })       // false
```
A diferencia de `filter`, `first(where:)` se detiene en la primera coincidencia y no construye un nuevo array.

---

`contains(where:)` y `allSatisfy` reemplazan el patrón común de un bucle con una variable de bandera. Ambos se detienen en cuanto se conoce la respuesta: `contains(where:)` en la primera coincidencia, `allSatisfy` en el primer elemento que falla.
```swift
let ages = [15, 22, 40]
let anyMinor = ages.contains { $0 < 18 }  // true
let allAdults = ages.allSatisfy { $0 >= 18 } // false
```
`contains { ... }` es la forma de cierre final de `contains(where:)`, que no debe confundirse con `contains(_:)`, que busca un valor específico.

---

Las funciones de orden superior funcionan con cualquier array, incluidos los arrays de tus propios structs. Encadenar `filter` y luego `map` es la forma habitual de seleccionar algunos elementos y extraer un valor de cada uno:
```swift
struct Book {
    var title: String
    var pages: Int
}
let books = [Book(title: "Dune", pages: 412), Book(title: "Haiku", pages: 40)]
let long = books.filter { $0.pages > 100 }.map { $0.title }
print(long) // ["Dune"]
```
Hacerlo en el orden contrario, `map` y luego `filter`, perdería la propiedad `pages` antes de que la comprobación pudiera usarla.

---

Cuando un cierre solo lee una propiedad, puedes pasar en su lugar un **key path**: `\.name` significa "la propiedad `name` del elemento", y `map(\.name)` es lo mismo que `map { $0.name }`.
Ordenar por una propiedad usa el cierre habitual de dos argumentos, comparando esa propiedad en ambos elementos:
```swift
struct City {
    var name: String
    var population: Int
}
let cities = [City(name: "Oslo", population: 700), City(name: "Rome", population: 2800)]
let byPopulation = cities.sorted { $0.population > $1.population }
print(byPopulation.map(\.name)) // ["Rome", "Oslo"]
```

---

Para ordenar por **más de un criterio**, compara la primera propiedad y recurre a la segunda solo cuando los primeros valores sean iguales:
```swift
let sorted = people.sorted {
    if $0.age != $1.age {
        return $0.age < $1.age
    }
    return $0.name < $1.name
}
```
Aquí las personas se ordenan por edad, y las personas con la misma edad se ordenan por nombre. El cierre debe devolver `true` solo cuando el primer elemento deba ir antes que el segundo, así que el caso de igualdad pasa a la siguiente comparación.

---

`enumerated()` convierte un array en una secuencia de pares `(offset, element)`, de modo que un cierre puede usar la posición de cada elemento junto con su valor:
```swift
let steps = ["mix", "bake"]
let numbered = steps.enumerated().map { pair in
    "\(pair.offset + 1). \(pair.element)"
}
print(numbered) // ["1. mix", "2. bake"]
```
Como cada par es una tupla, el cierre también puede desestructurarlo: `.map { (i, step) in "\(i + 1). \(step)" }`.

---

`zip` empareja los elementos de dos secuencias posición por posición, produciendo una secuencia de tuplas. Se detiene al final de la más corta:
```swift
let names = ["Ann", "Bob"]
let ages = [31, 27, 99]
let pairs = zip(names, ages).map { "\($0) is \($1)" }
print(pairs) // ["Ann is 31", "Bob is 27"]
```
Dentro del cierre `$0` es el elemento de la primera secuencia y `$1` el de la segunda. `zip` es una función libre, no un método: escribes `zip(a, b)`, no `a.zip(b)`.

---

`forEach` es el gemelo de orden superior del bucle `for-in`: llama al cierre una vez por elemento, en orden. La diferencia está en cómo sales del bucle. En un `for-in` puedes hacer `break` o `continue`; dentro de un cierre de `forEach` no se permiten `break` ni `continue`, y `return` solo termina la **llamada actual** del cierre, luego el siguiente elemento se procesa como de costumbre:
```swift
[1, 2, 3].forEach { n in
    if n == 2 { return }
    print(n)
}
// prints 1 and 3
```
Usa `forEach` para un efecto secundario breve sobre cada elemento, y `for-in` cuando necesites detenerte antes.

---

`Dictionary(grouping:by:)` divide una colección en un diccionario de arrays. El cierre calcula la **clave** de cada elemento, y todos los elementos con la misma clave acaban en el mismo array:
```swift
let words = ["apple", "bee", "avocado"]
let byInitial = Dictionary(grouping: words, by: { $0.first! })
print(byInitial["a"]!) // ["apple", "avocado"]
```
`mapValues` transforma cada valor de un diccionario manteniendo las claves, así que es el siguiente paso natural después de agrupar:
```swift
let sizes = byInitial.mapValues { $0.count }
print(sizes["a"]!) // 2
```

---

`prefix(while:)` toma elementos desde el principio **mientras** el cierre devuelva `true`, y se detiene en el primer elemento que falla, incluso si los elementos posteriores volverían a pasar. `drop(while:)` es su complemento: se salta esa misma serie inicial y devuelve todo lo demás:
```swift
let temps = [12, 15, 21, 14]
print(temps.prefix { $0 < 20 }) // [12, 15]
print(temps.drop { $0 < 20 })   // [21, 14]
```
Ambos devuelven un `ArraySlice`, una vista sobre el array original que se imprime como un array y puede convertirse en uno con `Array(...)`.

---

Puedes escribir tus propias funciones de orden superior. Una función que recibe un cierre y **devuelve un nuevo cierre** construido a partir de él es un patrón común: el cierre devuelto captura el original, así que el parámetro debe ser `@escaping`.
Por ejemplo, `negate` convierte un predicado en su opuesto, listo para pasarse a `filter`:
```swift
func negate(_ predicate: @escaping (Int) -> Bool) -> (Int) -> Bool {
    return { !predicate($0) }
}
let isEven: (Int) -> Bool = { $0 % 2 == 0 }
print([1, 2, 3, 4].filter(negate(isEven))) // [1, 3]
```
Ten en cuenta que `filter(negate(isEven))` pasa el cierre como un argumento normal, sin la sintaxis de cierre final.

---

`map` y `filter` sobre un array son **ansiosos**: cada uno procesa todo el array y construye uno nuevo antes de que se ejecute el siguiente paso. En una colección grande, o cuando solo necesitas el primer resultado, eso es trabajo desperdiciado.
La propiedad `lazy` devuelve una vista cuyas operaciones se ejecutan solo cuando se solicita realmente un elemento, de uno en uno a través de toda la cadena:
```swift
let firstBig = (1...1000).lazy.map { $0 * $0 }.first { $0 > 50 }
print(firstBig!) // 64
```
Aquí solo `1, 2, ..., 8` se elevan al cuadrado: `first(where:)` pide elementos hasta que uno satisface la condición, y la cadena se detiene ahí. Sin `lazy`, `map` elevaría al cuadrado los 1000 números primero.
