Uma `String` é uma sequência de caracteres escrita entre aspas duplas.
A propriedade `length` informa quantos caracteres uma string contém, incluindo espaços:
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

Cada caractere de uma string tem um **índice**, começando em `0` para o primeiro.
Você lê um único caractere com colchetes ou com a função `get`, e o resultado é um `Char`:
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
O último caractere está no índice `length - 1`. As funções `first()` e `last()` são atalhos úteis:
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()` retorna uma cópia da string com todas as letras em maiúsculas, `lowercase()` faz o oposto.
A string original não é modificada:
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

Para verificar se uma string contém um trecho de texto você usa `contains`, `startsWith` e `endsWith`. Todas elas retornam um `Boolean`:
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
A verificação diferencia maiúsculas de minúsculas, a menos que você passe `ignoreCase = true`:
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf` retorna o índice onde um trecho de texto aparece **pela primeira vez**, ou `-1` se ele não aparecer de forma alguma.
`lastIndexOf` procura a partir do final:
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring` extrai uma parte de uma string. Com dois argumentos, ela pega os caracteres do índice inicial até, mas **sem incluir**, o índice final.
Com um argumento, ela pega tudo daquele índice até o final:
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
Combinar `indexOf` e `substring` permite recortar uma string em torno de um marcador:
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split` divide uma string em uma `List` de pedaços em torno de um separador, enquanto `joinToString` faz o oposto: ela une os elementos de uma coleção em uma única string com o separador que você escolher:
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

Como `split` retorna uma `List`, você pode percorrer seus elementos como qualquer outra lista:
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// imprime a, depois b
```

---

A entrada do usuário costuma trazer espaços extras. `trim()` retorna a string sem espaços no início e no final, `trimStart()` e `trimEnd()` os removem apenas de um lado:
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()` é `true` para `""`, enquanto `isBlank()` também é `true` para strings formadas apenas por espaços:
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)` retorna uma cópia da string em que **toda** ocorrência de `old` é substituída por `new`:
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)` retorna a string concatenada `n` vezes:
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)` adiciona `char` no início até que a string atinja `width` caracteres; `padEnd` os adiciona no final.
Se a string já for longa o suficiente, ela é retornada sem alterações:
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
Números não são strings: chame `toString()` primeiro, como em `42.toString().padStart(4, '0')`.

---

Duas strings são iguais quando contêm os mesmos caracteres na mesma ordem. Em Kotlin, `==` compara o **conteúdo** das strings, então essa é a forma normal de compará-las.
`equals` faz o mesmo, mas também aceita `ignoreCase = true` para ignorar a diferença entre maiúsculas e minúsculas:
```kotlin
println("hello" == "hello")                          // true
println("Hello" == "hello")                          // false
println("Hello".equals("hello", ignoreCase = true))  // true
```
`===` verifica se duas variáveis apontam para o exato mesmo objeto na memória, o que quase nunca é o que você quer com strings.

---

`reversed()` retorna a string com seus caracteres na ordem oposta:
```kotlin
println("stressed".reversed()) // desserts
```
Uma palavra que se lê da mesma forma nas duas direções, como `"level"`, é chamada de **palíndromo**.

---

Strings são **imutáveis**: uma vez criadas, elas nunca mudam. Toda função que você viu até agora, como `uppercase()` ou `replace()`, retorna uma **nova** string e deixa a original intacta.
Para manter o resultado você precisa armazená-lo, por exemplo reatribuindo uma `var`:
```kotlin
var name = "kotlin"
name.uppercase()        // o resultado é descartado
println(name)           // kotlin
name = name.uppercase() // o resultado é guardado
println(name)           // KOTLIN
```

---

Construir uma string longa pedaço por pedaço com `+` cria uma nova string a cada etapa. Um `StringBuilder` é um buffer de texto mutável feito para esse trabalho: `append` adiciona texto ao final (e retorna o builder, para que as chamadas possam ser encadeadas) e `toString()` fornece a `String` final:
```kotlin
val sb = StringBuilder()
sb.append("Hello")
sb.append(", ").append("world")
println(sb.toString()) // Hello, world
```
`append` aceita strings, caracteres e números.
