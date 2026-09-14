---
language: kotlin
exerciseType: 1
difficulty: 1
title: Hipoteza Collatza
---

# --description--

Hipoteza Collatza zaczyna się od dowolnej dodatniej liczby całkowitej `n` i powtarza jedną prostą regułę: jeśli `n` jest parzyste, dzielimy je na pół; jeśli `n` jest nieparzyste, zastępujemy je wartością `3n + 1`. Prędzej czy później ciąg osiąga 1.

Na przykład ciąg zaczynający się od 16 to `16 -> 8 -> 4 -> 2 -> 1`, więc zajmuje to 4 kroki.

Nikt nigdy nie udowodnił, że zawsze tak się dzieje, ale reguła ta obowiązuje dla każdej dotychczas przetestowanej liczby.

# --instructions--

Napisz funkcję `collatzSteps`, która przyjmuje dodatnią liczbę całkowitą `n` i zwraca liczbę kroków potrzebnych do osiągnięcia 1.

`collatzSteps(1)` to 0, ponieważ 1 to już koniec ciągu. `collatzSteps(12)` to 9, a `collatzSteps(27)` to 111.

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
```

# --seed--

```kotlin
fun collatzSteps(n: Int): Int {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`collatzSteps(1)` powinno zwrócić 0, ponieważ 1 to już koniec ciągu.

```kotlin
    tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` powinno zwrócić 1.

```kotlin
    tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` powinno zwrócić 8.

```kotlin
    tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` powinno zwrócić 16.

```kotlin
    tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` powinno zwrócić 4.

```kotlin
    tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` powinno zwrócić 9.

```kotlin
    tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` powinno zwrócić 111.

```kotlin
    tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` powinno zwrócić 118.

```kotlin
    tryCatch(collatzSteps(97) == 118)
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
fun collatzSteps(n: Int): Int {
    var value = n
    var steps = 0
    while (value != 1) {
        value = if (value % 2 == 0) value / 2 else 3 * value + 1
        steps++
    }
    return steps
}
```
