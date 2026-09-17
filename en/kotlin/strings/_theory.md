A `String` is a sequence of characters written between double quotes.
The `length` property tells how many characters a string contains, spaces included:
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

Each character of a string has an **index**, starting from `0` for the first one.
You read a single character with square brackets or the `get` function, and the result is a `Char`:
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
The last character is at index `length - 1`. The functions `first()` and `last()` are handy shortcuts:
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()` returns a copy of the string with every letter in upper case, `lowercase()` does the opposite.
The original string is not modified:
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

To check whether a string contains a piece of text you use `contains`, `startsWith` and `endsWith`. All of them return a `Boolean`:
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
The check is case sensitive, unless you pass `ignoreCase = true`:
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf` returns the index where a piece of text **first** appears, or `-1` if it does not appear at all.
`lastIndexOf` searches from the end instead:
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring` extracts a part of a string. With two arguments it takes the characters from the start index up to, but **not including**, the end index.
With one argument it takes everything from that index to the end:
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
Combining `indexOf` and `substring` lets you cut a string around a marker:
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split` breaks a string into a `List` of pieces around a separator, while `joinToString` does the opposite: it glues the elements of a collection into one string with the separator you choose:
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

Since `split` returns a `List`, you can loop over its elements like any other list:
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// prints a, then b
```

---

User input often carries extra spaces. `trim()` returns the string without spaces at the beginning and at the end, `trimStart()` and `trimEnd()` remove them on one side only:
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()` is `true` for `""`, while `isBlank()` is also `true` for strings made only of spaces:
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)` returns a copy of the string where **every** occurrence of `old` is replaced by `new`:
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)` returns the string concatenated `n` times:
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)` adds `char` at the beginning until the string reaches `width` characters; `padEnd` adds them at the end.
If the string is already long enough it is returned unchanged:
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
Numbers are not strings: call `toString()` first, as in `42.toString().padStart(4, '0')`.

---

Two strings are equal when they contain the same characters in the same order. In Kotlin `==` compares the **content** of the strings, so it is the normal way to compare them.
`equals` does the same, but it also accepts `ignoreCase = true` to ignore the difference between upper and lower case:
```kotlin
println("hello" == "hello")                          // true
println("Hello" == "hello")                          // false
println("Hello".equals("hello", ignoreCase = true))  // true
```
`===` checks whether two variables point to the very same object in memory, which is almost never what you want with strings.

---

`reversed()` returns the string with its characters in the opposite order:
```kotlin
println("stressed".reversed()) // desserts
```
A word that reads the same in both directions, like `"level"`, is called a **palindrome**.

---

Strings are **immutable**: once created they never change. Every function you have seen so far, like `uppercase()` or `replace()`, returns a **new** string and leaves the original untouched.
To keep the result you must store it, for example by reassigning a `var`:
```kotlin
var name = "kotlin"
name.uppercase()        // result is thrown away
println(name)           // kotlin
name = name.uppercase() // result is stored
println(name)           // KOTLIN
```

---

Building a long string piece by piece with `+` creates a new string at every step. A `StringBuilder` is a mutable text buffer made for this job: `append` adds text to the end (and returns the builder, so calls can be chained) and `toString()` gives the final `String`:
```kotlin
val sb = StringBuilder()
sb.append("Hello")
sb.append(", ").append("world")
println(sb.toString()) // Hello, world
```
`append` accepts strings, characters and numbers.
