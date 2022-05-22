---
language: kotlin
exerciseType: 1
difficulty: 1
title: Addizione
---

# --description--

Dati due numeri interi `num1` e `num2`, scrivi un programma per sommare questi due numeri

# --instructions--

Scrivi una funzione che restituisca la somma tra i due numeri

Esempio di chiamata:
```kotlin
println(somma(1, 2))
// stampa 3
```

# --seed--

```kotlin
fun somma() {
    
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

La somma di 1 e 3 deve essere uguale a 4

```kotlin
    tryCatch(somma(1, 3) == 4)
```

La somma di 200 e 210 deve essere uguale a 410

```kotlin
    tryCatch(somma(200, 210) == 410)
```

La somma di 15 e 35 deve essere uguale a 50

```kotlin
    tryCatch(somma(15, 35) == 50)
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
fun somma(num1: Int, num2: Int): Int {
    return num1 + num2
}
```
