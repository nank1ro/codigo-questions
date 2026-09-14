---
language: kotlin
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

Pangram to zdanie, w którym każda litera angielskiego alfabetu występuje co najmniej raz. Najbardziej znanym przykładem jest "the quick brown fox jumps over the lazy dog", które mieści wszystkie 26 liter w dziewięciu krótkich słowach.

Sprawdzenie nie rozróżnia wielkości liter, więc `A` i `a` liczą się jako ta sama litera. Cyfry, znaki interpunkcyjne i spacje są ignorowane: nie są literami, ale nie są też powodem do odrzucenia zdania.

# --instructions--

Napisz funkcję `isPangram`, która przyjmuje zdanie i zwraca `true`, jeśli zdanie jest pangramem, a `false` w przeciwnym razie.

Przykłady:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Puste zdanie nie jest pangramem.
- Liczy się tylko 26 liter od `a` do `z`.

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

Puste zdanie nie jest pangramem

```kotlin
    tryCatch(isPangram("") == false)
```

Klasyczne zdanie "the quick brown fox jumps over the lazy dog" jest pangramem

```kotlin
    tryCatch(isPangram("the quick brown fox jumps over the lazy dog") == true)
```

Zdanie, w którym brakuje litery `x`, nie jest pangramem

```kotlin
    tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false)
```

Zdanie "the five boxing wizards jump quickly" jest pangramem

```kotlin
    tryCatch(isPangram("the five boxing wizards jump quickly") == true)
```

Podkreślenia są ignorowane, więc zdanie nadal jest pangramem

```kotlin
    tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true)
```

Cyfry są ignorowane, więc zdanie nadal jest pangramem

```kotlin
    tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true)
```

Cyfry nie zastępują liter `e`, `i` oraz `t`

```kotlin
    tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false)
```

Zdanie zapisane wielkimi literami też jest pangramem

```kotlin
    tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true)
```

Mieszanie wielkości liter w tej samej połowie alfabetu nie wystarczy

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
