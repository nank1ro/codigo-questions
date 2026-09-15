---
language: swift
exerciseType: 1
difficulty: 2
title: Tri à bulles
---

# --description--

Le tri à bulles est l'un des algorithmes de tri les plus simples. Il parcourt une liste et compare chaque paire d'éléments adjacents, en les échangeant dès qu'ils sont dans le mauvais ordre. Après chaque passage complet, la plus grande valeur restante a « remonté » jusqu'à sa position finale, et la liste est triée dès qu'un passage se termine sans le moindre échange.

# --instructions--

Écrivez une fonction appelée `bubbleSort` qui prend un tableau d'entiers et retourne un **nouveau** tableau avec les mêmes valeurs triées par ordre croissant. Le tableau passé en paramètre ne doit pas être modifié.

Vous devez implémenter l'algorithme de tri à bulles vous-même, en comparant et en échangeant les éléments adjacents. N'utilisez pas de fonction de tri de la bibliothèque standard.

Votre fonction doit également fonctionner avec un tableau vide, un tableau d'un seul élément, un tableau déjà trié, des valeurs répétées et des nombres négatifs.

Exemple d'appel de fonction :
```swift
print(bubbleSort([3, 1, 2]))
// affiche [1, 2, 3]
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func bubbleSort(_ arr: [Int]) -> [Int] {
    
}
```

# --asserts--

Un tableau vide doit retourner un tableau vide

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

Un tableau d'un seul élément doit rester identique

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

Un tableau déjà trié doit conserver le même ordre

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

Un tableau trié à l'envers doit être mis en ordre croissant

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

Toutes les valeurs répétées doivent être conservées

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

Les nombres négatifs doivent être triés avant les positifs

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

Un tableau mixte plus long doit être trié par ordre croissant

```swift
do {
    let solution: [Int] = [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]
    tryCatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func bubbleSort(_ arr: [Int]) -> [Int] {
    var result = arr
    var end = result.count
    var swapped = true
    while swapped && end > 1 {
        swapped = false
        for i in 1..<end {
            if result[i - 1] > result[i] {
                let temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end -= 1
    }
    return result
}
```
