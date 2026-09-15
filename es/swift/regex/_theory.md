Una **expresión regular** (regex) es un patrón pequeño que describe una forma de texto: "una serie de dígitos", "una palabra seguida de un signo igual", "tres letras mayúsculas". En lugar de escribir bucles sobre caracteres, describes la forma una vez y dejas que Swift la encuentre.

Swift escribe una regex entre `#/` y `/#`:
```swift
let digits = #/\d+/#
```
Dentro del patrón, `\d` significa "cualquier dígito" y `+` significa "uno o más del elemento anterior", así que `\d+` significa "una serie de uno o más dígitos".

La pregunta más simple que puedes hacer es si un texto contiene una coincidencia. `contains(_:)` recibe una regex y devuelve un `Bool`:
```swift
print("order42".contains(#/\d+/#)) // true
print("order".contains(#/\d+/#))   // false
```
Usa siempre la forma `#/ ... /#` mostrada aquí: la escritura más corta `/ ... /` confunde al compilador cuando el patrón se escribe directamente dentro de una llamada a un método.

---

Unas pocas abreviaturas cubren la mayoría de los patrones. Cada una coincide exactamente con **un** carácter:
- `\d` es un dígito
- `\w` es una letra, un dígito o un guion bajo
- `\s` es un espacio, un tabulador o un salto de línea
- `.` es cualquier carácter suelto

Para coincidir con más de un carácter, añade un **cuantificador** justo después del patrón:
- `+` significa uno o más
- `*` significa cero o más
- `?` significa cero o uno

Así que `\w+` es una palabra, `\s*` es un espaciado opcional y `\d?` es un dígito opcional:
```swift
print("hello world".contains(#/\w+\s\w+/#)) // true
print("hello".contains(#/\w+\s\w+/#))       // false
```
Un carácter sin significado especial simplemente se representa a sí mismo, así que `#/cat/#` coincide con las tres letras `cat`.

---

Por defecto un patrón puede coincidir en cualquier lugar dentro del texto. Los **anclajes** lo atan a una posición en su lugar:
- `^` significa "el inicio del texto"
- `$` significa "el final del texto"

```swift
print("swift".contains(#/^sw/#))  // true, el texto empieza con sw
print("myswift".contains(#/^sw/#)) // false, sw no está al inicio
print("swift".contains(#/ft$/#))  // true, el texto termina con ft
```
Los anclajes coinciden con una posición, no con un carácter, así que no añaden nada a lo que contiene la coincidencia.

---

Cuando ninguna de las abreviaturas encaja, enumera entre corchetes los caracteres que aceptas. `[abc]` coincide con una `a`, una `b` o una `c`, y un guion escribe un rango:
```swift
print("f".contains(#/[a-f]/#))  // true
print("Z".contains(#/[A-Z]/#))  // true
print("5".contains(#/[0-9a-f]/#)) // true
```
Un número entre llaves dice exactamente cuántas veces se repite el patrón anterior: `{3}` significa tres veces, `{2,4}` significa entre dos y cuatro veces:
```swift
print("aaa".contains(#/^a{3}$/#))  // true
print("aa".contains(#/^a{3}$/#))   // false
```
Envolver un patrón en `^` y `$` con un recuento es la forma habitual de comprobar que un texto completo tiene una forma dada.

---

`contains(_:)` solo dice sí o no. Para obtener el texto coincidente, usa `firstMatch(of:)`. Devuelve una **coincidencia opcional**: `nil` cuando nada coincidió, así que se combina de forma natural con `if let`.

El texto coincidente se almacena en la propiedad `0` de la coincidencia, escrito `m.0`:
```swift
let text = "order 42 today"
if let m = text.firstMatch(of: #/\d+/#) {
    print(m.0) // 42
}
```
`firstMatch(of:)` se detiene en la primera coincidencia, incluso cuando el texto contiene más.

---

`m.0` no es un `String` sino un `Substring`: una vista del texto original, no una copia. Se imprime exactamente como una cadena, pero donde se requiere un `String` tienes que convertirlo:
```swift
let text = "order 42"
if let m = text.firstMatch(of: #/\d+/#) {
    let found: String = String(m.0)
    print(found) // 42
}
```
Los inicializadores de números aceptan un `Substring` directamente, así que `Int(m.0)` funciona sin el rodeo.

---

`matches(of:)` devuelve **todas** las coincidencias en lugar de la primera, como un array. El array nunca es `nil`: cuando nada coincide simplemente está vacío, así que se puede recorrer o transformar directamente:
```swift
let text = "a1 b22"
print(text.matches(of: #/\d+/#).count) // 2
```
Cada elemento es una coincidencia, así que `$0.0` dentro de un `map` es el texto coincidente:
```swift
let found = text.matches(of: #/\d+/#).map { String($0.0) }
print(found) // ["1", "22"]
```

---

Como `Int(_:)` acepta un `Substring`, convertir el texto encontrado en números es un solo paso. `compactMap` resulta útil aquí: descarta los valores que vuelven como `nil`:
```swift
let text = "a1 b22"
let numbers = text.matches(of: #/\d+/#).compactMap { Int($0.0) }
print(numbers) // [1, 22]
```
Usa `map` cuando todos los elementos se conviertan, `compactMap` cuando alguno pueda fallar.

---

Los paréntesis alrededor de una parte del patrón crean un **grupo de captura**: la coincidencia completa sigue siendo `m.0`, y la parte dentro de los paréntesis se convierte en `m.1`:
```swift
let text = "id-42"
if let m = text.firstMatch(of: #/id-(\d+)/#) {
    print(m.0) // id-42
    print(m.1) // 42
}
```
Así conservas la pieza interesante y descartas el texto de alrededor. Sin paréntesis no hay ningún `m.1` y el código no compila.

---

Un patrón puede contener varios grupos. Se numeran de izquierda a derecha por su paréntesis de apertura, así que el segundo es `m.2`, el tercero `m.3`, y así sucesivamente:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/([a-z]+)=(\d+)/#) {
    print(m.1, m.2) // size 10
}
```
`m.0` sigue siendo siempre la coincidencia completa, sea cual sea el número de grupos.

---

Contar paréntesis se vuelve frágil en cuanto un patrón crece. Dale al grupo un **nombre** en su lugar, escribiendo `?<nombre>` justo después de su paréntesis de apertura, y léelo como una propiedad de la coincidencia:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/(?<key>[a-z]+)=(?<value>\d+)/#) {
    print(m.key)   // size
    print(m.value) // 10
}
```
Los grupos con nombre siguen numerados, así que `m.1` sigue funcionando, pero `m.key` dice qué contiene y sobrevive a un cambio en el patrón.

---

`replacing(_:with:)` sustituye cada coincidencia por un texto fijo y devuelve un nuevo `String`, dejando el original intacto:
```swift
let text = "a1 b22"
print(text.replacing(#/\d+/#, with: "#")) // a# b#
print(text)                               // a1 b22
```
Observa que `\d+` sustituye una serie completa de dígitos por un solo `#`, mientras que `\d` sustituiría un dígito cada vez. El patrón decide cuánto desaparece.

---

`split(separator:)` también acepta una regex, lo que permite que una sola llamada gestione separadores que no siempre se escriben de la misma forma:
```swift
let line = "a, b;c"
let parts = line.split(separator: #/[,;]\s*/#)
print(parts.joined(separator: "|")) // a|b|c
```
El patrón `[,;]\s*` significa "una coma o un punto y coma, seguidos de cualquier cantidad de espaciado", así que cada separador se consume entero y no se produce ningún campo vacío. El resultado es un array de `Substring`.

---

Validar un texto completo con `^` y `$` funciona, pero `wholeMatch(of:)` lo dice directamente: devuelve una coincidencia solo cuando el patrón cubre el texto desde el primer carácter hasta el último, y `nil` en caso contrario:
```swift
print("1a2b".wholeMatch(of: #/[0-9a-f]+/#) != nil) // true
print("1z".wholeMatch(of: #/[0-9a-f]+/#) != nil)   // false
```
Usa `firstMatch(of:)` para encontrar algo dentro de un texto, y `wholeMatch(of:)` para comprobar que un texto tiene una forma exacta.

---

Un literal `#/ ... /#` es fijo al compilar. Cuando el patrón solo se conoce en tiempo de ejecución, por ejemplo porque lo escribió un usuario, constrúyelo con `Regex(_:)`:
```swift
let regex = try Regex("[0-9]+")
print("abc123".contains(regex)) // true
```
Este inicializador **lanza** errores: un patrón inválido como `"["` solo se descubre mientras el programa se ejecuta, así que la llamada necesita `try`, y el error debe manejarse con `do`/`catch` (o `try?`) o propagarse marcando la función que lo rodea como `throws`, como hace este ejercicio. Una regex construida así no tiene propiedades numeradas conocidas en tiempo de compilación, pero `contains`, `matches(of:)` y `replacing` funcionan exactamente igual que antes.
