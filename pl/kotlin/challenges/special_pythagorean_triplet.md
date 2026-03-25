---
language: kotlin
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

Trójka pitagorejska to zbiór trzech liczb naturalnych, a < b < c, dla których a² + b² = c². Istnieje dokładnie jedna trójka pitagorejska, dla której a + b + c = 1000. Znajdź iloczyn a × b × c.

# --instructions--

Napisz funkcję, która znajduje iloczyn trójki pitagorejskiej, gdzie a + b + c = n.

Przykład wywołania funkcji:
```kotlin
println(specialPythagoreanTriplet(12))
// prints 60
```

# --seed--

```kotlin
fun specialPythagoreanTriplet(n: Int): Int {

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

Iloczyn trójki pitagorejskiej, gdzie a + b + c = 12, musi wynosić 60

```kotlin
    tryCatch(specialPythagoreanTriplet(12) == 60)
```

Iloczyn trójki pitagorejskiej, gdzie a + b + c = 1000, musi wynosić 31875000

```kotlin
    tryCatch(specialPythagoreanTriplet(1000) == 31875000)
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
fun specialPythagoreanTriplet(n: Int): Int {
    for (a in 1 until n) {
        for (b in a + 1 until n) {
            val c = n - a - b
            if (c > b && a * a + b * b == c * c) {
                return a * b * c
            }
        }
    }
    return -1
}
```
