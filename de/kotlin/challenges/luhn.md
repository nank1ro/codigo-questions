---
language: kotlin
exerciseType: 1
difficulty: 2
title: Luhn-Prüfsumme
---

# --description--

Der Luhn-Algorithmus ist eine einfache Prüfsumme, die zur Überprüfung von Identifikationsnummern wie Kreditkartennummern verwendet wird.

Bevor Sie eine Zahl überprüfen, entfernen Sie alle Leerzeichen aus dem String. Der String ist nur gültig, wenn der übrig gebliebene Teil länger als ein Zeichen ist und der ursprüngliche String nichts außer Ziffern und Leerzeichen enthält.

Um die Überprüfung durchzuführen, beginnen Sie bei der äußersten rechten Ziffer und bewegen Sie sich nach links, wobei Sie jede zweite Ziffer verdoppeln. Wenn das Verdoppeln eine Zahl größer als 9 ergibt, subtrahieren Sie 9 davon. Addieren Sie dann alle Ziffern: Die Zahl ist nur gültig, wenn die Summe durch 10 teilbar ist.

Zum Beispiel ergibt `"059"` `0`, dann ergibt `5` verdoppelt `10`, was zu `1` wird, dann `9`. Ihre Summe ist `10`, was durch 10 teilbar ist, also ist die Zahl gültig.

# --instructions--

Schreiben Sie eine Funktion `isValid`, die einen String entgegennimmt und `true` zurückgibt, wenn die Zahl gültig ist, andernfalls `false`.

- `"4539 3195 0343 6467"` besteht die Prüfsumme, also ist das Ergebnis `true`.
- `"8273 1232 7352 0569"` besteht die Prüfsumme nicht, also ist das Ergebnis `false`.
- `"0"` ist nur ein Zeichen lang, also ist das Ergebnis `false`.
- `"055-444-285"` enthält ein Zeichen, das weder eine Ziffer noch ein Leerzeichen ist, also ist das Ergebnis `false`.

Beispiel eines Funktionsaufrufs:
```kotlin
println(isValid("095 245 88"))
// prints true
```

# --seed--

```kotlin
fun isValid(value: String): Boolean {
    
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

Eine einzelne Ziffer ist nicht gültig.

```kotlin
    tryCatch(isValid("0") == false)
```

Eine einzelne Ziffer mit einem führenden Leerzeichen ist nicht gültig.

```kotlin
    tryCatch(isValid(" 0") == false)
```

Die Zahl `"059"` ist gültig.

```kotlin
    tryCatch(isValid("059") == true)
```

Die Zahl `"59"` ist gültig.

```kotlin
    tryCatch(isValid("59") == true)
```

Die Zahl `"055 444 285"` ist gültig.

```kotlin
    tryCatch(isValid("055 444 285") == true)
```

Die Zahl `"055 444 286"` ist not gültig.

```kotlin
    tryCatch(isValid("055 444 286") == false)
```

Die Zahl `"8273 1232 7352 0569"` ist not gültig.

```kotlin
    tryCatch(isValid("8273 1232 7352 0569") == false)
```

Die Zahl `"4539 3195 0343 6467"` ist gültig.

```kotlin
    tryCatch(isValid("4539 3195 0343 6467") == true)
```

Die Zahl `"1 2345 6789 1234 5678 9012"` ist not gültig.

```kotlin
    tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

Die Zahl `"095 245 88"` ist gültig.

```kotlin
    tryCatch(isValid("095 245 88") == true)
```

Ein Buchstabe macht die Zahl ungültig.

```kotlin
    tryCatch(isValid("055a 444 285") == false)
```

Bindestriche machen die Zahl ungültig.

```kotlin
    tryCatch(isValid("055-444-285") == false)
```

Ein Satzeichen macht die Zahl ungültig.

```kotlin
    tryCatch(isValid(":9") == false)
```

Symbole machen die Zahl ungültig.

```kotlin
    tryCatch(isValid("055# 444\$ 285") == false)
```

Ein leerer String ist nicht gültig.

```kotlin
    tryCatch(isValid("") == false)
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
fun isValid(value: String): Boolean {
    var sum = 0
    var count = 0
    for (i in value.length - 1 downTo 0) {
        val character = value[i]
        if (character == ' ') {
            continue
        }
        if (character < '0' || character > '9') {
            return false
        }
        var digit = character - '0'
        if (count % 2 == 1) {
            digit *= 2
            if (digit > 9) {
                digit -= 9
            }
        }
        sum += digit
        count++
    }
    return count > 1 && sum % 10 == 0
}
```
