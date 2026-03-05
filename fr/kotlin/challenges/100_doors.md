---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100 portes
---

# --description--

Il y a 100 portes à la suite qui sont toutes initialement fermées.
Vous faites 100 passages devant les portes.
La première fois, visitez chaque porte et 'basculez' la porte (si la porte est fermée, ouvrez-la ; si elle est ouverte, fermez-la).
La deuxième fois, visitez seulement chaque 2ème porte (c'est-à-dire la porte #2, #4, #6, ...) et basculez-la.
La troisième fois, visitez chaque 3ème porte (c'est-à-dire la porte #3, #6, #9, ...), etc., jusqu'à ce que vous ne visitiez que la 100ème porte.

# --instructions--

Implémentez une fonction pour déterminer l'état des portes après le dernier passage.
Retournez le résultat final dans un tableau, avec seulement le numéro de la porte inclus dans le tableau s'il est ouvert.
> La méthode doit pouvoir fonctionner avec un nombre variable de portes.

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

Donné 100 doors, retournez la liste correcte des portes ouvertes

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(getFinalOpenedDoors(100) == solution1)
```

Donné 10 doors, retournez la liste correcte des portes ouvertes

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(getFinalOpenedDoors(10) == solution2)
```

Donné 950 doors, retournez la liste correcte des portes ouvertes

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
