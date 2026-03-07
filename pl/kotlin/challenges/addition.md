---
language: kotlin
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Dane są dwie liczby całkowite `num1` i `num2`. Napisz program, który doda te dwie liczby.

# --instructions--

Napisz funkcję, która zwraca sumę dwóch liczb.

Przykład wywołania funkcji:
```kotlin
println(addition(1, 2))
// prints 3
```

# --seed--

```kotlin
fun addition() {
    
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

Suma 1 i 3 musi wynosić 4

```kotlin
    tryCatch(addition(1, 3) == 4)
```

Suma 200 i 210 musi wynosić 410

```kotlin
    tryCatch(addition(200, 210) == 410)
```

Suma 15 i 35 musi wynosić 50

```kotlin
    tryCatch(addition(15, 35) == 50)
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
fun addition(num1: Int, num2: Int): Int {
    return num1 + num2
}
```
