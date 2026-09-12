Una **expresión regular** (o **regex**) es un patrón pequeño que describe una forma de texto: "cuatro dígitos", "una palabra seguida de `@`", "cualquier cosa entre comillas". En Kotlin un patrón es un objeto `Regex`, que se construye de dos maneras equivalentes:
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
La mayoría de los caracteres de un patrón se representan a sí mismos, pero unos pocos son **abreviaturas**:
- `\d` es cualquier dígito, escrito `"\\d"` en una cadena de Kotlin porque `\` debe escaparse
- `[a-z]` es cualquier letra minúscula, y `[abc]` es cualquiera de `a`, `b` o `c`
- `+` después de un elemento significa "uno o más de él", así que `\d+` es una serie de dígitos

La pregunta más simple que puedes hacer es `matches`, que es `true` solo cuando el patrón describe **toda** la cadena:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, the letter is not a digit
```

---

`matches` suele ser demasiado estricto: normalmente solo quieres saber si el patrón aparece en **algún lugar** del texto. Eso es `containsMatchIn`:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, the whole string is not digits
println(digits.containsMatchIn("order 42"))  // true, "42" is in there
```
Junto a `\d` hay dos abreviaturas más que usarás constantemente: `\w` es un carácter de palabra (letra, dígito o `_`) y `\s` es un carácter de espacio en blanco. Cada una de ellas se puede repetir con un **cuantificador**:
- `+` uno o más
- `*` cero o más
- `?` cero o uno
- `{3}` exactamente tres, `{2,4}` de dos a cuatro

Duplicar cada barra invertida resulta molesto, así que los patrones se suelen escribir como **cadenas crudas** con comillas triples, donde `\` es solo un carácter:
```kotlin
val digits = Regex("""\d+""") // same as Regex("\\d+")
```

---

`containsMatchIn` solo dice *si* el patrón está ahí. `find` también dice **qué** y **dónde**: devuelve la primera coincidencia como un `MatchResult`, o `null` cuando no hay nada que encontrar.
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value` es el texto coincidente y `range` son los índices que cubre en la cadena original. Como el resultado es nullable, accedes a él con la llamada segura `?.`, que da `null` en lugar de fallar cuando no se encontró ninguna coincidencia:
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

Los paréntesis en un patrón crean un **grupo de captura**: una parte de la coincidencia que quieres leer por separado. `MatchResult.groupValues` los contiene, con el índice `0` para la coincidencia completa y `1`, `2`, ... para los grupos, de izquierda a derecha:
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
Cuando no hay ninguna coincidencia, `find` devuelve `null` y no hay nada que leer, así que una función que extrae un grupo normalmente decide qué devolver en ese caso:
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

Contar paréntesis para descubrir que el host es el grupo `2` se vuelve frágil en cuanto el patrón crece. Un grupo puede recibir un **nombre** con `(?<name>...)` y leerse de `groups` por ese nombre:
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups` devuelve el grupo como un `MatchGroup?`, así que aún tienes que pedir su `.value`. Un grupo con nombre también se numera como de costumbre, así que `groupValues[1]` sigue funcionando junto a él.

---

`find` se detiene en la primera coincidencia. `findAll` devuelve **todas** las coincidencias, como un `Sequence<MatchResult>`: una cadena perezosa que puedes tratar como una lista con `map`, `filter`, `count` y `toList`.
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
Cuando nada coincide, `findAll` devuelve una secuencia vacía en lugar de `null`, así que no hay ninguna llamada segura que escribir. Imprimir la secuencia en sí no es útil, muestra el objeto, no las coincidencias: conviértela primero en una lista.

---

`replace` reescribe el texto: devuelve una cadena **nueva** donde cada coincidencia se sustituye por el reemplazo, dejando el original intacto.
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
En la cadena de reemplazo, `$1`, `$2`, ... representan los grupos capturados de esa coincidencia, así que puedes reordenar o reutilizar las piezas que coincidieron:
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0` es la coincidencia completa. Si necesitas un `$` literal en el reemplazo, escápalo como `\$`.
`replace` reescribe **todas** las coincidencias, así que cuando solo se debe reescribir una cadena completa, fija el patrón con las **anclas** `^` (inicio del texto) y `$` (fin del texto):
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, nothing is replaced
```

---

Una cadena de reemplazo solo puede reorganizar las piezas que se le dieron. Cuando el nuevo texto tiene que **calcularse**, pásale a `replace` una lambda en su lugar: recibe el `MatchResult` y devuelve la cadena que ocupa su lugar.
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
Dentro de la lambda tienes el `MatchResult` completo, así que `m.value`, `m.range` y `m.groupValues` están todos disponibles. Ten en cuenta que `$1` no tiene ningún significado aquí: es un carácter ordinario en la cadena que devuelvas.

---

`split` corta una cadena dondequiera que el patrón coincida y devuelve las piezas como un `List<String>`. A diferencia de dividir por una cadena delimitadora fija, un separador regex puede describir toda una familia de separadores:
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
Los separadores coincidentes no forman parte del resultado. Si el texto empieza o termina con un separador, la pieza de al lado está vacía:
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split` acepta un `limit` como segundo argumento para detenerse tras un número dado de piezas, dejando el resto intacto en la última.

---

Los patrones distinguen mayúsculas de minúsculas: `Regex("kotlin")` no coincide con `"Kotlin"`. En lugar de escribir `[kK][oO]...`, pásale una opción como segundo argumento:
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
La opción pertenece al `Regex`, así que todos los métodos de ese objeto la obedecen: `matches`, `find`, `findAll`, `replace` y `split` por igual. Otras opciones útiles son `RegexOption.MULTILINE`, que hace que `^` y `$` coincidan en cada línea, y `RegexOption.DOT_MATCHES_ALL`. Para combinarlas, pásale un conjunto: `Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`.

---

`Regex("cat")` también coincide con el `cat` dentro de `catalog`. Para exigir una palabra completa, usa el **límite de palabra** `\b`: coincide con la posición vacía entre un carácter de palabra y cualquier otra cosa, incluidos el inicio y el fin del texto.
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
Un patrón es una cadena ordinaria, así que puede construirse a partir de partes en tiempo de ejecución:
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

Los caracteres `. * + ? ( ) [ ] { } | ^ $ \` tienen un significado especial dentro de un patrón. El más traicionero es `.`, que coincide con **cualquier** carácter, no con un punto. Para referirse al carácter en sí, escápalo con una barra invertida:
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, the dot matches the x
println(Regex("""3\.14""").matches("3x14")) // false
```
Cuando el texto a buscar viene de una variable y debe tomarse literalmente, deja que la biblioteca haga el escapado con `Regex.escape`:
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll` y los grupos juntos convierten una línea de texto en datos estructurados. Cada `MatchResult` de la secuencia lleva su propio `groupValues`, así que una sola cadena puede construir una lista, un mapa o un total:
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate` construye un mapa a partir de los pares `key to value` que devuelve la lambda. Cuando un patrón tiene un número fijo de grupos, `destructured` te permite desempaquetarlos en variables con nombre en lugar de leerlos por índice:
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

Los corchetes definen una **clase de caracteres**: un carácter del conjunto listado. Dentro de ellos puedes usar rangos, y un `^` inicial niega toda la clase:
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, no digit allowed
```
Una clase solo elige entre caracteres individuales. Para elegir entre alternativas completas, usa `|`, normalmente envuelto en un grupo para que no se trague el resto del patrón:
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

Como `findAll` da una secuencia, los métodos de agregación que ya conoces funcionan también sobre las coincidencias: `sumOf`, `maxOfOrNull`, `filter`, `sortedBy`. Extraer números de texto libre es un trabajo de dos pasos: encontrarlos y luego convertir el texto en un número.
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

Un patrón realista suele mezclar todo a la vez: grupos para conservar las partes que necesitas, un `\.` escapado para los puntos literales y un reemplazo con lambda para reconstruir el texto alrededor de ellos.
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
Mantén los patrones tan simples como el trabajo permita: un patrón que intenta describir toda dirección de correo válida resulta ilegible, mientras que `\w+@\w+\.\w+` es suficiente para encontrar las direcciones en una frase.
