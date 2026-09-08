Un `String` es una secuencia de caracteres escrita entre comillas dobles.
La propiedad `length` indica cuántos caracteres contiene una cadena, espacios incluidos:
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

Cada carácter de una cadena tiene un **índice**, empezando por `0` para el primero.
Lees un solo carácter con corchetes o con la función `get`, y el resultado es un `Char`:
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
El último carácter está en el índice `length - 1`. Las funciones `first()` y `last()` son atajos útiles:
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()` devuelve una copia de la cadena con todas las letras en mayúscula, `lowercase()` hace lo contrario.
La cadena original no se modifica:
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

Para comprobar si una cadena contiene un fragmento de texto usas `contains`, `startsWith` y `endsWith`. Todas devuelven un `Boolean`:
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
La comprobación distingue entre mayúsculas y minúsculas, a menos que pases `ignoreCase = true`:
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf` devuelve el índice donde un fragmento de texto aparece **por primera vez**, o `-1` si no aparece en absoluto.
`lastIndexOf` busca en cambio desde el final:
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring` extrae una parte de una cadena. Con dos argumentos toma los caracteres desde el índice inicial hasta el índice final, **sin incluirlo**.
Con un solo argumento toma todo desde ese índice hasta el final:
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
Combinar `indexOf` y `substring` te permite recortar una cadena alrededor de un marcador:
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split` divide una cadena en una `List` de fragmentos alrededor de un separador, mientras que `joinToString` hace lo contrario: une los elementos de una colección en una sola cadena con el separador que elijas:
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

Como `split` devuelve una `List`, puedes recorrer sus elementos como en cualquier otra lista:
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// prints a, then b
```

---

La entrada del usuario suele llevar espacios de más. `trim()` devuelve la cadena sin espacios al principio ni al final, `trimStart()` y `trimEnd()` los eliminan solo de un lado:
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()` es `true` para `""`, mientras que `isBlank()` también es `true` para cadenas formadas solo por espacios:
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)` devuelve una copia de la cadena en la que **todas** las apariciones de `old` se sustituyen por `new`:
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)` devuelve la cadena concatenada `n` veces:
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)` añade `char` al principio hasta que la cadena alcanza `width` caracteres; `padEnd` los añade al final.
Si la cadena ya es lo bastante larga, se devuelve sin cambios:
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
Los números no son cadenas: llama primero a `toString()`, como en `42.toString().padStart(4, '0')`.
