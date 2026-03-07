---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100 doors
---

# --description--

W rzędzie stoi 100 drzwi, wszystkie początkowo zamknięte.
Wykonujesz 100 przejść obok drzwi.
Przy pierwszym przejściu odwiedzasz każde drzwi i je „przełączasz" (jeśli drzwi są zamknięte, otwierasz je; jeśli są otwarte, zamykasz).
Przy drugim przejściu odwiedzasz tylko co 2. drzwi (tj. drzwi nr 2, 4, 6, ...) i je przełączasz.
Przy trzecim przejściu odwiedzasz co 3. drzwi (tj. drzwi nr 3, 6, 9, ...) itd., aż do odwiedzenia tylko 100. drzwi.

# --instructions--

Zaimplementuj funkcję, która określa stan drzwi po ostatnim przejściu.
Zwróć końcowy wynik w tablicy, zawierającej tylko numery drzwi, które są otwarte.
> Metoda musi działać dla zmiennej liczby drzwi.

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

Dla 100 drzwi zwróć poprawną listę otwartych drzwi

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(getFinalOpenedDoors(100) == solution1)
```

Dla 10 drzwi zwróć poprawną listę otwartych drzwi

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(getFinalOpenedDoors(10) == solution2)
```

Dla 950 drzwi zwróć poprawną listę otwartych drzwi

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
