---
language: kotlin
exerciseType: 1
difficulty: 2
title: Caesar-Verschlüsselung
---

# --description--

Julius Caesar schützte seine privaten Briefe mit einem der ältesten Tricks der Kryptografie: Er ersetzte jeden Buchstaben einer Nachricht durch den Buchstaben, der eine feste Anzahl von Stellen weiter hinten im Alphabet steht. Bei einer Verschiebung von 3 wird `a` zu `d`, `b` zu `e` und `c` zu `f`.

Das Alphabet verhält sich wie ein Kreis, daher laufen die Buchstaben am Ende wieder zum Anfang zurück: Bei einer Verschiebung von 3 wird `x` zu `a`, `y` zu `b` und `z` zu `c`.

Alles, was kein Buchstabe ist, etwa ein Leerzeichen, ein Komma, ein Ausrufezeichen oder eine Ziffer, durchläuft die Verschlüsselung unverändert.

# --instructions--

Schreiben Sie eine Funktion `caesarCipher`, die eine Nachricht `text` und eine ganze Zahl `shift` entgegennimmt und die verschlüsselte Nachricht zurückgibt.

Beispiele:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Die Nachricht besteht immer aus Kleinbuchstaben, Sie müssen sich also nie um Großbuchstaben kümmern.
- Zeichen, die keine Buchstaben sind, behalten ihren Platz und ihren Wert.
- Die Verschiebung ist nie negativ. Eine Verschiebung von `0` lässt die Nachricht unverändert, und eine Verschiebung von `26` ebenfalls.

# --seed--

```kotlin
fun caesarCipher(text: String, shift: Int): String {
    
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

Eine Verschiebung von 3 macht aus "hello" "khoor"

```kotlin
    tryCatch(caesarCipher("hello", 3) == "khoor")
```

Die Buchstaben am Ende des Alphabets laufen zum Anfang zurück, daher wird "xyz" zu "abc"

```kotlin
    tryCatch(caesarCipher("xyz", 3) == "abc")
```

Eine Verschiebung von 0 lässt die Nachricht unverändert

```kotlin
    tryCatch(caesarCipher("abc", 0) == "abc")
```

Eine Verschiebung von 26 ist eine volle Runde durch das Alphabet, daher bleibt die Nachricht unverändert

```kotlin
    tryCatch(caesarCipher("abc", 26) == "abc")
```

Satzzeichen und Leerzeichen werden unverändert durchgereicht

```kotlin
    tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

Eine leere Nachricht bleibt leer

```kotlin
    tryCatch(caesarCipher("", 4) == "")
```

Leerzeichen zwischen einzelnen Buchstaben bleiben erhalten

```kotlin
    tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Ziffern werden nicht verschoben, auch nicht bei einer Verschiebung von 25

```kotlin
    tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

Eine Verschiebung von 13 verschlüsselt einen ganzen Satz

```kotlin
    tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt")
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
fun caesarCipher(text: String, shift: Int): String {
    val result = StringBuilder()

    for (char in text) {
        if (char in 'a'..'z') {
            result.append('a' + (char - 'a' + shift) % 26)
        } else {
            result.append(char)
        }
    }

    return result.toString()
}
```
