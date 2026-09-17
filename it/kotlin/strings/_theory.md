Una `String` è una sequenza di caratteri scritta tra virgolette doppie.
La proprietà `length` indica quanti caratteri contiene una stringa, spazi inclusi:
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

Ogni carattere di una stringa ha un **indice**, a partire da `0` per il primo.
Leggi un singolo carattere con le parentesi quadre o con la funzione `get`, e il risultato è un `Char`:
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
L'ultimo carattere si trova all'indice `length - 1`. Le funzioni `first()` e `last()` sono comode scorciatoie:
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()` restituisce una copia della stringa con ogni lettera in maiuscolo, `lowercase()` fa il contrario.
La stringa originale non viene modificata:
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

Per verificare se una stringa contiene un pezzo di testo usi `contains`, `startsWith` e `endsWith`. Tutte restituiscono un `Boolean`:
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
Il controllo distingue tra maiuscole e minuscole, a meno che tu non passi `ignoreCase = true`:
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf` restituisce l'indice in cui un pezzo di testo compare **per la prima volta**, oppure `-1` se non compare affatto.
`lastIndexOf` cerca invece a partire dalla fine:
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring` estrae una parte di una stringa. Con due argomenti prende i caratteri dall'indice iniziale fino all'indice finale, **escluso**.
Con un solo argomento prende tutto da quell'indice fino alla fine:
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
Combinare `indexOf` e `substring` ti permette di tagliare una stringa attorno a un marcatore:
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split` divide una stringa in una `List` di pezzi attorno a un separatore, mentre `joinToString` fa il contrario: unisce gli elementi di una collezione in un'unica stringa con il separatore che scegli:
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

Dato che `split` restituisce una `List`, puoi scorrere i suoi elementi come qualsiasi altra lista:
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// stampa a, poi b
```

---

L'input dell'utente spesso contiene spazi in più. `trim()` restituisce la stringa senza spazi all'inizio e alla fine, `trimStart()` e `trimEnd()` li rimuovono solo da un lato:
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()` è `true` per `""`, mentre `isBlank()` è `true` anche per le stringhe composte solo da spazi:
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)` restituisce una copia della stringa in cui **ogni** occorrenza di `old` viene sostituita da `new`:
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)` restituisce la stringa concatenata `n` volte:
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)` aggiunge `char` all'inizio finché la stringa non raggiunge `width` caratteri; `padEnd` li aggiunge alla fine.
Se la stringa è già abbastanza lunga, viene restituita invariata:
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
I numeri non sono stringhe: chiama prima `toString()`, come in `42.toString().padStart(4, '0')`.

---

Due stringhe sono uguali quando contengono gli stessi caratteri nello stesso ordine. In Kotlin `==` confronta il **contenuto** delle stringhe, quindi è il modo normale per confrontarle.
`equals` fa lo stesso, ma accetta anche `ignoreCase = true` per ignorare la differenza tra maiuscole e minuscole:
```kotlin
println("hello" == "hello")                          // true
println("Hello" == "hello")                          // false
println("Hello".equals("hello", ignoreCase = true))  // true
```
`===` verifica se due variabili puntano esattamente allo stesso oggetto in memoria, cosa che quasi mai è ciò che vuoi con le stringhe.

---

`reversed()` restituisce la stringa con i caratteri in ordine inverso:
```kotlin
println("stressed".reversed()) // desserts
```
Una parola che si legge allo stesso modo in entrambe le direzioni, come `"level"`, si chiama **palindromo**.

---

Le stringhe sono **immutabili**: una volta create, non cambiano mai. Ogni funzione vista finora, come `uppercase()` o `replace()`, restituisce una **nuova** stringa e lascia intatta quella originale.
Per conservare il risultato devi memorizzarlo, ad esempio riassegnando una `var`:
```kotlin
var name = "kotlin"
name.uppercase()        // il risultato viene scartato
println(name)           // kotlin
name = name.uppercase() // il risultato viene memorizzato
println(name)           // KOTLIN
```

---

Costruire una stringa lunga pezzo per pezzo con `+` crea una nuova stringa a ogni passaggio. Uno `StringBuilder` è un buffer di testo mutabile pensato proprio per questo compito: `append` aggiunge testo alla fine (e restituisce il builder, così le chiamate possono essere concatenate) e `toString()` restituisce la `String` finale:
```kotlin
val sb = StringBuilder()
sb.append("Hello")
sb.append(", ").append("world")
println(sb.toString()) // Hello, world
```
`append` accetta stringhe, caratteri e numeri.
