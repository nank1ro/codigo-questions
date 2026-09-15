---
language: kotlin
exerciseType: 1
difficulty: 2
title: Tri à bulles
---

# --description--

Le tri à bulles est l'un des algorithmes de tri les plus simples. Il parcourt une liste et compare chaque paire d'éléments adjacents, en les échangeant dès qu'ils sont dans le mauvais ordre. Après chaque passage complet, la plus grande valeur restante a « remonté » jusqu'à sa position finale, et la liste est triée dès qu'un passage se termine sans le moindre échange.

# --instructions--

Écrivez une fonction appelée `bubbleSort` qui prend une `List<Int>` et retourne une **nouvelle** liste avec les mêmes valeurs triées par ordre croissant. La liste passée en paramètre ne doit pas être modifiée.

Vous devez implémenter l'algorithme de tri à bulles vous-même, en comparant et en échangeant les éléments adjacents. N'utilisez pas de fonction de tri de la bibliothèque standard.

Votre fonction doit également fonctionner avec un tableau vide, un tableau d'un seul élément, un tableau déjà trié, des valeurs répétées et des nombres négatifs.

Exemple d'appel de fonction :
```kotlin
println(bubbleSort(listOf(3, 1, 2)))
// affiche [1, 2, 3]
```

# --seed--

```kotlin
fun bubbleSort(arr: List<Int>): List<Int> {
    
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

Un tableau vide doit retourner un tableau vide

```kotlin
    tryCatch(bubbleSort(listOf<Int>()) == listOf<Int>())
```

Un tableau d'un seul élément doit rester identique

```kotlin
    tryCatch(bubbleSort(listOf<Int>(42)) == listOf<Int>(42))
```

Un tableau déjà trié doit conserver le même ordre

```kotlin
    tryCatch(bubbleSort(listOf<Int>(1, 2, 3, 4, 5)) == listOf<Int>(1, 2, 3, 4, 5))
```

Un tableau trié à l'envers doit être mis en ordre croissant

```kotlin
    tryCatch(bubbleSort(listOf<Int>(5, 4, 3, 2, 1)) == listOf<Int>(1, 2, 3, 4, 5))
```

Toutes les valeurs répétées doivent être conservées

```kotlin
    tryCatch(bubbleSort(listOf<Int>(3, 1, 3, 2, 1)) == listOf<Int>(1, 1, 2, 3, 3))
```

Les nombres négatifs doivent être triés avant les positifs

```kotlin
    tryCatch(bubbleSort(listOf<Int>(-5, 3, -1, 0, -9)) == listOf<Int>(-9, -5, -1, 0, 3))
```

Un tableau mixte plus long doit être trié par ordre croissant

```kotlin
    tryCatch(bubbleSort(listOf<Int>(9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6)) == listOf<Int>(-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14))
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
fun bubbleSort(arr: List<Int>): List<Int> {
    val result = arr.toMutableList()
    var end = result.size
    var swapped = true
    while (swapped) {
        swapped = false
        for (i in 1 until end) {
            if (result[i - 1] > result[i]) {
                val temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end--
    }
    return result
}
```
