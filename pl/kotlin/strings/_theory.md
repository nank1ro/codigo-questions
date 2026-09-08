`String` to sekwencja znaków zapisana w cudzysłowach.
Właściwość `length` mówi, ile znaków zawiera ciąg znaków, łącznie ze spacjami:
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

Każdy znak ciągu znaków ma **indeks**, zaczynając od `0` dla pierwszego.
Pojedynczy znak odczytujesz za pomocą nawiasów kwadratowych lub funkcji `get`, a wynikiem jest `Char`:
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
Ostatni znak znajduje się pod indeksem `length - 1`. Funkcje `first()` i `last()` to wygodne skróty:
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()` zwraca kopię ciągu znaków ze wszystkimi literami zapisanymi wielkimi literami, `lowercase()` robi coś przeciwnego.
Oryginalny ciąg znaków nie zostaje zmodyfikowany:
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

Aby sprawdzić, czy ciąg znaków zawiera fragment tekstu, używasz `contains`, `startsWith` i `endsWith`. Wszystkie zwracają `Boolean`:
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
Sprawdzenie rozróżnia wielkość liter, chyba że przekażesz `ignoreCase = true`:
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf` zwraca indeks, pod którym fragment tekstu pojawia się **pierwszy raz**, lub `-1`, jeśli w ogóle się nie pojawia.
`lastIndexOf` przeszukuje od końca:
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring` wyodrębnia część ciągu znaków. Z dwoma argumentami pobiera znaki od indeksu początkowego aż do, ale **bez uwzględnienia**, indeksu końcowego.
Z jednym argumentem pobiera wszystko od tego indeksu do końca:
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
Łącząc `indexOf` i `substring`, możesz wyciąć fragment ciągu znaków wokół znacznika:
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split` dzieli ciąg znaków na `List` fragmentów wokół separatora, natomiast `joinToString` robi coś przeciwnego: łączy elementy kolekcji w jeden ciąg znaków z wybranym przez ciebie separatorem:
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

Ponieważ `split` zwraca `List`, możesz przechodzić po jej elementach jak po każdej innej liście:
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// prints a, then b
```

---

Dane wprowadzane przez użytkownika często zawierają dodatkowe spacje. `trim()` zwraca ciąg znaków bez spacji na początku i na końcu, `trimStart()` i `trimEnd()` usuwają je tylko po jednej stronie:
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()` ma wartość `true` dla `""`, natomiast `isBlank()` ma wartość `true` również dla ciągów znaków złożonych wyłącznie ze spacji:
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)` zwraca kopię ciągu znaków, w której **każde** wystąpienie `old` jest zastąpione przez `new`:
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)` zwraca ciąg znaków powtórzony `n` razy:
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)` dodaje `char` na początku, aż ciąg znaków osiągnie `width` znaków; `padEnd` dodaje je na końcu.
Jeśli ciąg znaków jest już wystarczająco długi, zostaje zwrócony bez zmian:
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
Liczby nie są ciągami znaków: najpierw wywołaj `toString()`, jak w `42.toString().padStart(4, '0')`.
