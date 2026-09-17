Un **cierre** es un bloque de código que puedes pasar y llamar más tarde, como una función sin nombre.
La sintaxis completa de una expresión de cierre coloca los parámetros y el tipo de retorno dentro de llaves, seguidos de la palabra clave `in` y el cuerpo:
```swift
{ (parameters) -> ReturnType in
    body
}
```
Como cualquier otro valor, un cierre se puede almacenar en una constante y luego llamarse usando el nombre de la constante:
```swift
let greet = { (name: String) -> String in
    return "Hello, \(name)!"
}
print(greet("Ada")) // Hello, Ada!
```

---

Escribir cada tipo dentro del cierre suele ser innecesario. Cuando la constante tiene un **tipo de función** explícito, Swift infiere los tipos de los parámetros y del retorno, así que solo hace falta indicar los nombres de los parámetros antes de `in`:
```swift
let triple: (Int) -> Int = { n in
    return n * 3
}
```
El tipo `(Int) -> Int` se lee como "una función que recibe un `Int` y devuelve un `Int`".
Cuando el cuerpo es una única expresión, la palabra clave `return` también se puede omitir, esto se llama **retorno implícito**:
```swift
let triple: (Int) -> Int = { n in n * 3 }
print(triple(4)) // 12
```

---

Swift va un paso más allá: dentro de un cierre puedes referirte a los argumentos con los **nombres de argumento abreviados** `$0`, `$1`, `$2`, etc., sin declarar ningún parámetro ni la palabra clave `in`.
`$0` es el primer argumento, `$1` el segundo:
```swift
let add: (Int, Int) -> Int = { $0 + $1 }
print(add(2, 3)) // 5
```
Los tipos siguen viniendo de la anotación `(Int, Int) -> Int`.

---

Como los cierres son valores, una función puede aceptar uno como parámetro. El tipo del parámetro es simplemente el tipo de función:
```swift
func apply(_ n: Int, _ operation: (Int) -> Int) -> Int {
    return operation(n)
}
print(apply(5, { $0 + 1 })) // 6
```
La función `apply` no sabe qué hace `operation`, solo sabe que recibe un `Int` y devuelve un `Int`, y la llama como a cualquier otra función.

---

Cuando un cierre es el **último** argumento de una función, puedes escribirlo después del paréntesis de cierre de la llamada. Esta es la sintaxis de **cierre final**:
```swift
print(apply(5) { $0 + 1 }) // 6
```
Si el cierre es el único argumento, los paréntesis se pueden omitir por completo:
```swift
func run(_ task: () -> Int) -> Int {
    return task()
}
print(run { 42 }) // 42
```
Ambas formas llaman exactamente a la misma función, la sintaxis final solo es más fácil de leer cuando el cierre es largo.

---

Los cierres brillan con los métodos de array que reciben uno como argumento. `map` llama al cierre en cada elemento y devuelve un nuevo array con los resultados:
```swift
let nums = [1, 2, 3]
let doubled = nums.map { $0 * 2 }
print(doubled) // [2, 4, 6]
```
El array original no cambia. Como `map` recibe un único cierre como argumento, la sintaxis de cierre final es la forma habitual de llamarlo.

---

`filter` conserva solo los elementos para los que el cierre devuelve `true`. El cierre recibe un elemento y debe devolver un `Bool`:
```swift
let nums = [5, 12, 8, 20]
let big = nums.filter { $0 > 10 }
print(big) // [12, 20]
```
Los elementos conservan su orden original, y el resultado es un nuevo array del mismo tipo de elemento.

---

`reduce` combina todos los elementos en un único valor. Recibe un valor inicial y un cierre con dos argumentos: el valor acumulado hasta el momento y el elemento actual. El cierre devuelve el nuevo valor acumulado:
```swift
let nums = [1, 2, 3, 4]
let product = nums.reduce(1) { $0 * $1 }
print(product) // 24
```
Aquí `$0` empieza siendo `1`, luego pasa a ser `1 * 1`, `1 * 2`, `2 * 3` y finalmente `6 * 4`.
Como `map`, `filter` y `reduce` devuelven valores, se pueden encadenar: `nums.filter { $0 > 1 }.map { $0 * 10 }`.

---

`sorted(by:)` devuelve un nuevo array ordenado. El cierre recibe dos elementos y devuelve `true` cuando el primero debe ir **antes** que el segundo:
```swift
let nums = [3, 1, 2]
print(nums.sorted { $0 < $1 }) // [1, 2, 3]
print(nums.sorted { $0 > $1 }) // [3, 2, 1]
```
El cierre puede comparar cualquier cosa, por ejemplo `words.sorted { $0.count < $1.count }` ordena las cadenas de la más corta a la más larga.

---

Un cierre puede usar variables declaradas fuera de su cuerpo. Las **captura**: la variable sigue existiendo mientras el cierre exista, incluso después de que la función que la declaró haya retornado.
Esto permite que una función construya un cierre con su propio estado privado:
```swift
func makeCounter() -> () -> Int {
    var count = 0
    return {
        count += 1
        return count
    }
}
```
`() -> Int` es el tipo de un cierre sin parámetros que devuelve un `Int`. Cada llamada al cierre devuelto incrementa el mismo `count` capturado:
```swift
let counter = makeCounter()
print(counter()) // 1
print(counter()) // 2
```

---

Devolver un cierre es una forma práctica de construir funciones personalizadas. Los parámetros de la función externa son capturados por el cierre que devuelve:
```swift
func makeAdder(_ amount: Int) -> (Int) -> Int {
    return { $0 + amount }
}
let addFive = makeAdder(5)
print(addFive(10)) // 15
```
El tipo de retorno `(Int) -> Int` describe el cierre, y la forma abreviada `$0` se refiere al argumento de ese cierre, no al de `makeAdder`.

---

Un cierre almacenado en una constante se puede pasar donde se espere un argumento de tipo cierre, usando la etiqueta del argumento del parámetro:
```swift
let ascending = { (a: Int, b: Int) -> Bool in a < b }
print([3, 1, 2].sorted(by: ascending)) // [1, 2, 3]
```

---

Cada llamada a una función que devuelve un cierre crea una **nueva** variable capturada. Dos cierres construidos por llamadas separadas no comparten su estado:
```swift
let first = makeCounter()
let second = makeCounter()
print(first())  // 1
print(first())  // 2
print(second()) // 1
```
El estado se comparte solo entre llamadas del mismo cierre.

---

Por defecto, un cierre pasado a una función solo debe usarse mientras esa función se ejecuta. Si la función almacena el cierre o devuelve otro cierre que lo usa, el cierre **escapa** de la función, y su parámetro debe marcarse con `@escaping`:
```swift
func twice(_ task: @escaping () -> Int) -> () -> Int {
    return { task() * 2 }
}
let answer = twice { 21 }
print(answer()) // 42
```
Sin `@escaping` el compilador informa un error, porque el cierre devuelto usaría `task` después de que `twice` haya terminado.

---

Los cierres se pueden almacenar en arrays como cualquier otro valor. El tipo del elemento es el tipo de función:
```swift
let steps: [(Int) -> Int] = [{ $0 + 1 }, { $0 * 10 }]
print(steps[1](3)) // 30
```
Recorrer un array así y llamar a cada cierre en orden construye un pequeño **pipeline** de transformaciones.
