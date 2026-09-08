Un **string** es un fragmento de texto. En Swift escribes un literal de string entre comillas dobles, y su tipo es `String`:
```swift
let greeting: String = "Hello"
var city = "Rome"
```
Como con cualquier otro valor, `let` crea una constante que no se puede cambiar y `var` crea una variable que sí puede cambiar.
Swift infiere el tipo `String` a partir del literal, así que la anotación de tipo es opcional.

---

La **interpolación de cadenas** inserta el valor de una expresión dentro de un literal de cadena. Envuelve la expresión en `\()`:
```swift
let name = "Ada"
let age = 36
print("\(name) is \(age) years old") // Ada is 36 years old
```
Se puede interpolar cualquier tipo: números, booleanos y otras cadenas se convierten automáticamente en texto.

---

Dos cadenas se pueden unir con el operador `+`, que produce una nueva cadena:
```swift
let full = "Hello" + " " + "world" // Hello world
```
Para añadir texto al final de una variable de cadena existente usa `+=`. La variable debe declararse con `var`, porque su valor cambia:
```swift
var log = "Start"
log += "..."
print(log) // Start...
```

---

La propiedad `count` devuelve el número de caracteres de una cadena, e `isEmpty` es `true` cuando la cadena no tiene ningún carácter:
```swift
print("Swift".count) // 5
print("".isEmpty)    // true
```
Se cuenta cada carácter, incluidos los espacios y la puntuación.

---

Un `String` es una colección de valores `Character`. Un `Character` es una sola letra, dígito, símbolo o espacio, y se escribe con las mismas comillas dobles que una cadena, por lo que necesitas una anotación de tipo para obtener uno:
```swift
let letter: Character = "a"
let text = "abc"
print(text.count) // 3
```
Comprobar `isEmpty` es preferible a comparar `count` con `0`: se lee mejor y no necesita contar cada carácter.

---

Un **literal de string multilínea** empieza y termina con tres comillas dobles `"""`, cada una en su propia línea. Cada línea entre ellas pasa a formar parte de la cadena, y los saltos de línea se conservan:
```swift
let poem = """
Roses are red
Violets are blue
"""
print(poem)
```
Esto imprime las dos líneas exactamente como se escribieron. Las comillas de cierre `"""` también determinan la sangría: cualquier espacio en blanco antes de ellas se elimina del inicio de cada línea.

---

Como una cadena es una colección de caracteres, puedes iterar sobre ella con un bucle `for`-`in`. Cada iteración te da un `Character`:
```swift
for letter in "hey" {
    print(letter)
}
// h
// e
// y
```
Un `Character` se puede comparar con `==` con un literal de carácter, así que contar cuántas veces aparece un carácter es solo un bucle con un contador.

---

A diferencia de los arrays, las cadenas no se pueden indexar con un entero como `text[2]`: algunos caracteres ocupan más memoria que otros, por lo que Swift usa un tipo dedicado `String.Index` para señalar una posición.
`startIndex` es la posición del primer carácter y `endIndex` es la posición *después* del último. Para moverte desde un índice usa `index(_:offsetBy:)`, y luego indexa la cadena con el resultado:
```swift
let word = "Swift"
let second = word.index(word.startIndex, offsetBy: 1)
print(word[second]) // w
```
Moverse más allá del final de la cadena provoca un fallo en tiempo de ejecución, así que el desplazamiento debe mantenerse dentro de `count`.

---

Trabajar con índices es tedioso, así que Swift ofrece atajos para los casos más comunes:
- `first` y `last` devuelven el primer y el último carácter como un `Character?` opcional (`nil` para una cadena vacía)
- `prefix(n)` devuelve los primeros `n` caracteres y `suffix(n)` los últimos `n`
```swift
let word = "Swift"
print(word.first!)     // S
print(word.prefix(2))  // Sw
print(word.suffix(3))  // ift
```
`prefix` y `suffix` devuelven una `Substring`, una vista sobre el texto original. Para guardarla como un `String` real, envuélvela en `String(...)`. Si `n` es mayor que `count`, simplemente obtienes la cadena completa.

---

Tres métodos responden a las preguntas más comunes sobre el contenido de una cadena, y cada uno devuelve un `Bool`:
- `contains(_:)` es `true` cuando la cadena incluye el texto dado (o carácter) en cualquier parte
- `hasPrefix(_:)` es `true` cuando la cadena empieza con el texto dado
- `hasSuffix(_:)` es `true` cuando la cadena termina con el texto dado
```swift
let email = "ada@example.com"
print(email.contains("@"))          // true
print(email.hasPrefix("ada"))       // true
print(email.hasSuffix(".org"))      // false
```
Los tres distinguen entre mayúsculas y minúsculas: `"Swift".hasPrefix("s")` es `false`.

---

Como `contains`, `hasPrefix` y `hasSuffix` devuelven booleanos, se combinan de forma natural con `||` y `&&` para construir comprobaciones más complejas.

---

`uppercased()` y `lowercased()` devuelven una **nueva** cadena con cada letra convertida a mayúscula o minúscula. La cadena original no se modifica:
```swift
let name = "Swift"
print(name.uppercased()) // SWIFT
print(name.lowercased()) // swift
print(name)              // Swift
```
Ambos son métodos, así que no olvides los paréntesis.

---

Convertir a minúsculas es la forma habitual de comparar texto ignorando mayúsculas y minúsculas: dos cadenas que solo difieren en las mayúsculas se vuelven iguales una vez que ambas se convierten a minúsculas.

---

`split(separator:)` divide una cadena en un array de fragmentos allí donde aparece el carácter separador. `joined(separator:)` hace lo contrario: une los elementos de un array en una sola cadena, colocando el separador entre ellos:
```swift
let parts = "a-b-c".split(separator: "-") // ["a", "b", "c"]
print(parts.count)                         // 3
print(parts.joined(separator: ", "))       // a, b, c
```
Al igual que `prefix`, `split` devuelve valores `Substring`; envuelve uno en `String(...)` si necesitas guardarlo como un `String`.

---

Dividir por espacios es la forma más simple de descomponer una frase en palabras, y unir es cómo reconstruyes texto a partir de un array.

---

El framework Foundation añade muchos métodos adicionales para cadenas. Uno de los más útiles es `replacingOccurrences(of:with:)`, que devuelve una nueva cadena en la que cada aparición del primer texto se reemplaza por el segundo:
```swift
import Foundation

let path = "a/b/c"
print(path.replacingOccurrences(of: "/", with: "-")) // a-b-c
```
Recuerda hacer `import Foundation` al principio del archivo, de lo contrario el método no está disponible. Las llamadas a métodos se pueden encadenar, así que `text.lowercased().replacingOccurrences(of: " ", with: "_")` es válido.

---

Las cadenas se pueden comparar con los mismos operadores que los números. `==` comprueba que dos cadenas tengan exactamente los mismos caracteres, mientras que `<` y `>` las comparan en orden alfabético, carácter por carácter:
```swift
print("apple" == "apple")  // true
print("apple" < "banana")  // true
print("car" < "cat")       // true
```
La comparación distingue entre mayúsculas y minúsculas, y cada letra mayúscula va **antes** que cada letra minúscula, así que `"B" < "a"` es `true`.

---

Un `Character` no es un `String`, así que no se puede unir directamente a una cadena con `+`. Conviértelo primero con `String(...)`:
```swift
let letter: Character = "a"
let text = String(letter) + "bc" // abc
```
Combinar esto con un bucle `for`-`in` te permite reconstruir una cadena carácter a carácter, por ejemplo colocando cada nuevo carácter delante de los ya recopilados.
