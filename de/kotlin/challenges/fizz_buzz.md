---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

Erstellen Sie eine Funktion, die eine Zahl als Argument nimmt und `"Fizz"`, `"Buzz"` oder `"FizzBuzz"` zurückgibt.

# --instructions--

- Wenn die Zahl ein Vielfaches von `3` ist, sollte die Ausgabe `"Fizz"` sein.
- Wenn die angegebene Zahl ein Vielfaches von `5` ist, sollte die Ausgabe `"Buzz"` sein.
- Wenn die angegebene Zahl ein Vielfaches von `3` und `5` ist, sollte die Ausgabe `"FizzBuzz"` sein.
- Wenn die Zahl kein Vielfaches von `3` oder `5` ist, sollte die Zahl selbst ausgegeben werden, wie in den Beispielen unten gezeigt.
- Die Ausgabe sollte immer eine Zeichenkette sein, auch wenn sie kein Vielfaches von `3` oder `5` ist.

Beispiele:
```kotlin
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
```

# --seed--

```kotlin
fun fizzBuzz() {
    
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

Die Zahl `3` muss gleich `"Fizz"` sein.

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

Die Zahl `5` muss gleich `"Buzz"` sein.

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

Die Zahl `15` muss gleich `"FizzBuzz"` sein.

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

Die Zahl `10` muss gleich `"Buzz"` sein.

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

Die Zahl `98` muss gleich `"98"` sein.

```kotlin
    tryCatch(fizzBuzz(98) == "98");
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
fun fizzBuzz(number: Int): String {
    if (number % 3 == 0 && number % 5 == 0) {
        return "FizzBuzz"
    }
    if (number % 3 == 0) {
        return "Fizz"
    }
    if (number % 5 == 0) {
        return "Buzz"
    }
    return number.toString()
}
```
