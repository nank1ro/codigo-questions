---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100 Türen
---

# --description--

Es gibt 100 Türen in einer Reihe, die alle anfangs geschlossen sind.
Sie machen 100 Durchgänge an den Türen vorbei.
Beim ersten Durchgang besuchen Sie jede Tür und schalten sie um (wenn die Tür geschlossen ist, öffnen Sie sie; wenn sie offen ist, schließen Sie sie).
Beim zweiten Mal besuchen Sie nur jede 2. Tür (d.h. Tür #2, #4, #6, ...) und schalten sie um.
Beim dritten Mal besuchen Sie jede 3. Tür (d.h. Tür #3, #6, #9, ...), usw., bis Sie nur noch die 100. Tür besuchen.

# --instructions--

Implementieren Sie eine Funktion, um den Zustand der Türen nach dem letzten Durchgang zu bestimmen.
Geben Sie das Endergebnis in einem Array zurück, wobei nur die Türnummer im Array enthalten ist, wenn sie offen ist.
> Die Methode muss mit einer variablen Anzahl von Türen funktionieren.

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

Geben Sie bei 100 Türen die korrekte Liste der offenen Türen zurück.

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(getFinalOpenedDoors(100) == solution1)
```

Geben Sie bei 10 Türen die korrekte Liste der offenen Türen zurück.

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(getFinalOpenedDoors(10) == solution2)
```

Geben Sie bei 950 Türen die korrekte Liste der offenen Türen zurück.

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
