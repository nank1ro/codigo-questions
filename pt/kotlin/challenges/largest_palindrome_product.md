---
language: kotlin
exerciseType: 1
difficulty: 2
title: Maior produto palíndromo
---

# --description--

Um número palíndromo se lê da mesma forma nos dois sentidos. O maior palíndromo formado pelo produto de dois números de 2 dígitos é 9009 = 91 × 99.

# --instructions--

Escreva uma função que encontre o maior palíndromo formado pelo produto de dois números de n dígitos.

Exemplo de chamada da função:
```kotlin
println(largestPalindromeProduct(2))
// imprime 9009
```

# --seed--

```kotlin
fun largestPalindromeProduct(n: Int): Int {

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

O maior produto palíndromo de dois números de 2 dígitos deve ser 9009

```kotlin
    tryCatch(largestPalindromeProduct(2) == 9009)
```

O maior produto palíndromo de dois números de 3 dígitos deve ser 906609

```kotlin
    tryCatch(largestPalindromeProduct(3) == 906609)
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
fun largestPalindromeProduct(n: Int): Int {
    val max = Math.pow(10.0, n.toDouble()).toInt() - 1
    val min = Math.pow(10.0, (n - 1).toDouble()).toInt()
    var largest = 0
    for (i in max downTo min) {
        for (j in i downTo min) {
            val product = i * j
            if (product <= largest) break
            if (isPalindrome(product)) {
                largest = product
            }
        }
    }
    return largest
}

fun isPalindrome(n: Int): Boolean {
    val s = n.toString()
    return s == s.reversed()
}
```
