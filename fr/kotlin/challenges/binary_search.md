---
language: kotlin
exerciseType: 1
difficulty: 2
title: Recherche binaire
---

# --description--

La recherche binaire trouve une valeur dans une collection **triée** en divisant à plusieurs reprises la plage de recherche par deux : regarde l'élément du milieu et, si ce n'est pas celui que tu cherches, continue dans la moitié gauche lorsque la valeur cherchée est plus petite ou dans la moitié droite lorsqu'elle est plus grande.

Comme chaque étape écarte la moitié des éléments restants, la recherche binaire atteint la réponse en quelques comparaisons même sur de très grandes collections, alors que vérifier les éléments un par un coûterait autant d'étapes qu'il y a d'éléments.

# --instructions--

Écris une fonction `binarySearch` qui prend un tableau d'entiers trié par ordre croissant et un entier cherché, et renvoie l'index de la valeur cherchée dans le tableau, ou `-1` lorsque la valeur n'est pas présente.

Le tableau ne contient jamais de doublons, l'index est donc toujours unique. Le tableau peut aussi être vide. Ta fonction doit utiliser la recherche binaire, en divisant la plage de recherche par deux à chaque étape, et non un parcours linéaire.

Exemple d'appel de fonction :
```kotlin
println(binarySearch(intArrayOf(1, 3, 5, 7), 5))
// affiche 2
```

# --seed--

```kotlin
fun binarySearch() {

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

Rechercher dans un tableau vide doit renvoyer -1

```kotlin
    tryCatch(binarySearch(intArrayOf(), 7) == -1)
```

Rechercher 5 dans `[5]` doit renvoyer 0

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 5) == 0)
```

Rechercher 9 dans `[5]` doit renvoyer -1

```kotlin
    tryCatch(binarySearch(intArrayOf(5), 9) == -1)
```

Le premier élément -9 du tableau de 12 éléments doit être trouvé à l'index 0

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -9) == 0)
```

Le dernier élément 78 du tableau de 12 éléments doit être trouvé à l'index 11

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 78) == 11)
```

L'élément 15 doit être trouvé à l'index 6

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 15) == 6)
```

L'élément 22 doit être trouvé à l'index 7

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 22) == 7)
```

La valeur 12, qui se situe entre 11 et 15, doit renvoyer -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 12) == -1)
```

Une valeur cherchée plus petite que tous les éléments doit renvoyer -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), -100) == -1)
```

Une valeur cherchée plus grande que tous les éléments doit renvoyer -1

```kotlin
    tryCatch(binarySearch(intArrayOf(-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78), 100) == -1)
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
fun binarySearch(arr: IntArray, target: Int): Int {
    var low = 0
    var high = arr.size - 1
    while (low <= high) {
        val mid = low + (high - low) / 2
        if (arr[mid] == target) {
            return mid
        }
        if (arr[mid] < target) {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return -1
}
```
