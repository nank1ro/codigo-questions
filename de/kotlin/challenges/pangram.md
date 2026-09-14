---
language: kotlin
exerciseType: 1
difficulty: 1
title: Pangramm
---

# --description--

Ein Pangramm ist ein Satz, der jeden Buchstaben des englischen Alphabets mindestens einmal verwendet. Das bekannteste Beispiel ist "the quick brown fox jumps over the lazy dog", das alle 26 Buchstaben in neun kurze Wörter unterbringt.

Die Prüfung unterscheidet nicht zwischen Groß- und Kleinschreibung, daher zählen `A` und `a` als derselbe Buchstabe. Ziffern, Satzzeichen und Leerzeichen werden ignoriert: Sie sind keine Buchstaben, aber sie sind auch kein Grund, einen Satz abzulehnen.

# --instructions--

Schreiben Sie eine Funktion `isPangram`, die einen Satz entgegennimmt und `true` zurückgibt, wenn der Satz ein Pangramm ist, und andernfalls `false`.

Beispiele:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Ein leerer Satz ist kein Pangramm.
- Nur die 26 Buchstaben von `a` bis `z` zählen.

# --seed--

```kotlin
fun isPangram(sentence: String): Boolean {
    
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

Ein leerer Satz ist kein Pangramm

```kotlin
    tryCatch(isPangram("") == false)
```

Der klassische Satz "the quick brown fox jumps over the lazy dog" ist ein Pangramm

```kotlin
    tryCatch(isPangram("the quick brown fox jumps over the lazy dog") == true)
```

Ein Satz, dem der Buchstabe `x` fehlt, ist kein Pangramm

```kotlin
    tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false)
```

Der Satz "the five boxing wizards jump quickly" ist ein Pangramm

```kotlin
    tryCatch(isPangram("the five boxing wizards jump quickly") == true)
```

Unterstriche werden ignoriert, daher ist der Satz weiterhin ein Pangramm

```kotlin
    tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true)
```

Ziffern werden ignoriert, daher ist der Satz weiterhin ein Pangramm

```kotlin
    tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true)
```

Ziffern ersetzen nicht die Buchstaben `e`, `i` und `t`

```kotlin
    tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false)
```

Ein Satz in Großbuchstaben ist ebenfalls ein Pangramm

```kotlin
    tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true)
```

Das Mischen der Groß- und Kleinschreibung derselben Hälfte des Alphabets reicht nicht aus

```kotlin
    tryCatch(isPangram("abcdefghijklm ABCDEFGHIJKLM") == false)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun isPangram(sentence: String): Boolean {
    val letters = mutableSetOf<Char>()

    for (char in sentence.lowercase()) {
        if (char in 'a'..'z') {
            letters.add(char)
        }
    }

    return letters.size == 26
}
```
