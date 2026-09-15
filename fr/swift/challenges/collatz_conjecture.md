---
language: swift
exerciseType: 1
difficulty: 1
title: Conjecture de Collatz
---

# --description--

La conjecture de Collatz part de n'importe quel entier positif `n` et répète une règle simple : si `n` est pair, on le divise par deux ; si `n` est impair, on le remplace par `3n + 1`. Tôt ou tard, la séquence atteint 1.

Par exemple, en partant de 16, la séquence est `16 -> 8 -> 4 -> 2 -> 1`, donc il faut 4 étapes.

Personne n'a jamais prouvé que cela se produit toujours, mais c'est vrai pour tous les nombres testés jusqu'à présent.

# --instructions--

Écrivez une fonction `collatzSteps` qui prend un entier positif `n` et retourne le nombre d'étapes nécessaires pour atteindre 1.

`collatzSteps(1)` vaut 0, car 1 est déjà la fin de la séquence. `collatzSteps(12)` vaut 9, et `collatzSteps(27)` vaut 111.

Exemple d'appel de fonction :
```swift
print(collatzSteps(16))
// affiche 4
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
func collatzSteps(_ n: Int) -> Int {

}
```

# --asserts--

`collatzSteps(1)` doit retourner 0, car 1 est déjà la fin de la séquence.

```swift
tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` doit retourner 1.

```swift
tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` doit retourner 8.

```swift
tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` doit retourner 16.

```swift
tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` doit retourner 4.

```swift
tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` doit retourner 9.

```swift
tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` doit retourner 111.

```swift
tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` doit retourner 118.

```swift
tryCatch(collatzSteps(97) == 118)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func collatzSteps(_ n: Int) -> Int {
    var value = n
    var steps = 0
    while value != 1 {
        value = value % 2 == 0 ? value / 2 : 3 * value + 1
        steps += 1
    }
    return steps
}
```
