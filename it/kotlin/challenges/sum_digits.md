---
language: kotlin
exerciseType: 1
difficulty: 1
title: Somma cifre
---

# --description--

Ti viene dato un numero intero `num`.
Scrivi un programma per calcolare la somma di tutte le cifre di `num`

# --instructions--

Restituisci la somma delle cifre di `num`

Esempio di chiamata:
```kotlin
println(sommaCifre(28))
// stampa 10
```

# --seed--

```kotlin
fun sommaCifre() {

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

La somma delle cifre di 12345 è 15

```kotlin
    tryCatch(sommaCifre(12345) == 15)
```

La somma delle cifre di 57253 è 22

```kotlin
    tryCatch(sommaCifre(57253) == 22)
```

La somma delle cifre di 122 è 5

```kotlin
    tryCatch(sommaCifre(122) == 5)
```

La somma delle cifre di 91979997 è 60

```kotlin
    tryCatch(sommaCifre(91979997) == 60)
```

La somma delle cifre di 2147483647 è 46

```kotlin
    tryCatch(sommaCifre(2147483647) == 46)
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
fun sommaCifre(num: Int): Int {
    var n = num
    var result = 0
    while (n > 0) {
        result += n % 10
        n = (n / 10).toInt()
    }
    return result
}
```

