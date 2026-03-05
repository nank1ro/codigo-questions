---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100 portas
---

# --description--

Existem 100 portas em uma fileira que estão todas inicialmente fechadas.
Você faz 100 passagens pelas portas.
Na primeira vez, visite cada porta e 'alterne' a porta (se a porta estiver fechada, abra-a; se estiver aberta, feche-a).
Na segunda vez, visite apenas cada 2ª porta (ou seja, porta #2, #4, #6, ...) e alterne-a.
Na terceira vez, visite cada 3ª porta (ou seja, porta #3, #6, #9, ...), etc., até que você visite apenas a 100ª porta.

# --instructions--

Implemente uma função para determinar o estado das portas após a última passagem.
Retorne o resultado final em um array, com apenas o número da porta incluído no array se ela estiver aberta.
> O método deve ser capaz de funcionar com um número variável de portas.

# --seed--

```kotlin
fun getFinalOpenedDoors(numDoors: Int): ArrayList<Int> {
    
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

Dadas 100 portas, retorne a lista correta de portas abertas

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(getFinalOpenedDoors(100) == solution1)
```

Dadas 10 portas, retorne a lista correta de portas abertas

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(getFinalOpenedDoors(10) == solution2)
```

Dadas 950 portas, retorne a lista correta de portas abertas

```kotlin
    val solution3 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900)
    tryCatch(getFinalOpenedDoors(950) == solution3)
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
fun square(num: Int): Int {
    return Math.pow(num.toDouble(), 2.0).toInt()
}

fun getFinalOpenedDoors(numDoors: Int): ArrayList<Int> {
    val openDoors = ArrayList<Int>()
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.add(square(i))
        i += 1
    }
    return openDoors
}
```
