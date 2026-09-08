Ein `String` ist eine Folge von Zeichen, die zwischen doppelten Anführungszeichen steht.
Die Eigenschaft `length` gibt an, wie viele Zeichen eine Zeichenkette enthält, Leerzeichen eingeschlossen:
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

Jedes Zeichen einer Zeichenkette hat einen **Index**, beginnend bei `0` für das erste Zeichen.
Du liest ein einzelnes Zeichen mit eckigen Klammern oder der Funktion `get`, und das Ergebnis ist ein `Char`:
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
Das letzte Zeichen befindet sich am Index `length - 1`. Die Funktionen `first()` und `last()` sind praktische Abkürzungen:
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()` gibt eine Kopie der Zeichenkette zurück, bei der jeder Buchstabe groß geschrieben ist, `lowercase()` macht das Gegenteil.
Die ursprüngliche Zeichenkette wird nicht verändert:
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

Um zu prüfen, ob eine Zeichenkette einen bestimmten Text enthält, verwendest du `contains`, `startsWith` und `endsWith`. Alle geben einen `Boolean` zurück:
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
Die Prüfung unterscheidet zwischen Groß- und Kleinschreibung, es sei denn, du übergibst `ignoreCase = true`:
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf` gibt den Index zurück, an dem ein Text **zuerst** vorkommt, oder `-1`, wenn er gar nicht vorkommt.
`lastIndexOf` sucht stattdessen vom Ende aus:
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring` extrahiert einen Teil einer Zeichenkette. Mit zwei Argumenten nimmt es die Zeichen vom Start-Index bis zum End-Index, aber **ohne diesen einzuschließen**.
Mit einem Argument nimmt es alles von diesem Index bis zum Ende:
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
Die Kombination von `indexOf` und `substring` ermöglicht es dir, eine Zeichenkette an einer Markierung zu zerschneiden:
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split` zerlegt eine Zeichenkette anhand eines Trennzeichens in eine `List` von Teilen, während `joinToString` das Gegenteil macht: Es fügt die Elemente einer Collection mit dem gewählten Trennzeichen zu einer einzigen Zeichenkette zusammen:
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

Da `split` eine `List` zurückgibt, kannst du wie bei jeder anderen Liste über ihre Elemente iterieren:
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// prints a, then b
```

---

Benutzereingaben enthalten oft zusätzliche Leerzeichen. `trim()` gibt die Zeichenkette ohne Leerzeichen am Anfang und am Ende zurück, `trimStart()` und `trimEnd()` entfernen sie nur auf einer Seite:
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()` ist `true` für `""`, während `isBlank()` auch für Zeichenketten `true` ist, die nur aus Leerzeichen bestehen:
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)` gibt eine Kopie der Zeichenkette zurück, in der **jedes** Vorkommen von `old` durch `new` ersetzt wird:
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)` gibt die Zeichenkette `n`-mal aneinandergereiht zurück:
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)` fügt am Anfang so oft `char` hinzu, bis die Zeichenkette `width` Zeichen lang ist; `padEnd` fügt sie am Ende hinzu.
Ist die Zeichenkette bereits lang genug, wird sie unverändert zurückgegeben:
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
Zahlen sind keine Zeichenketten: Rufe zuerst `toString()` auf, wie in `42.toString().padStart(4, '0')`.
