---
language: swift
exerciseType: 1
difficulty: 1
title: Gouttes de pluie
---

# --description--

Votre tâche est de convertir un nombre en une chaîne contenant des sons de gouttes de pluie correspondant à certains facteurs potentiels.
Un facteur est un nombre qui divise exactement un autre nombre, sans reste.
Le moyen le plus simple de tester si un nombre est un facteur d'un autre est d'utiliser l'opération modulo.
Les règles des gouttes de pluie sont que si un nombre donné :

- a 3 comme facteur, ajoutez 'Pling' au résultat.
- a 5 comme facteur, ajoutez 'Plang' au résultat.
- a 7 comme facteur, ajoutez 'Plong' au résultat.
- n'a pas 3, 5 ou 7 comme facteur, le résultat doit être les chiffres du nombre.

# --instructions--

Écrivez une fonction qui retourne la chaîne correcte, exemples :

- 28 a 7 comme facteur, mais pas 3 ou 5, donc le résultat serait `"Plong"`.
- 30 a à la fois 3 et 5 comme facteurs, mais pas 7, donc le résultat serait `"PlingPlang"`.
- 34 n'est pas factorisé par 3, 5 ou 7, donc le résultat serait `"34"`.

> ASTUCE : omettez l'étiquette d'argument avec le `_` (trait de soulignement)

Exemple d'appel de fonction :
```swift
print(raindrops(28))
// prints "Plong"
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
func raindrops() {
    
}
```

# --asserts--

Le son pour 1 est "1"

```swift
tryCatch("1" == raindrops(1))
```

Le son pour 3 est "Pling"

```swift
tryCatch("Pling" == raindrops(3))
```

Le son pour 5 est "Plang"

```swift
tryCatch("Plang" == raindrops(5))
```

Le son pour 7 est "Plong"

```swift
tryCatch("Plong" == raindrops(7))
```

Le son pour 6 est "Pling"

```swift
tryCatch("Pling" == raindrops(6))
```

Le son pour 8 est "8"

```swift
tryCatch("8" == raindrops(8))
```

Le son pour 9 est "Pling"

```swift
tryCatch("Pling" == raindrops(9))
```

Le son pour 10 est "Plang"

```swift
tryCatch("Plang" == raindrops(10))
```

Le son pour 14 est "Plong"

```swift
tryCatch("Plong" == raindrops(14))
```

Le son pour 15 est "PlingPlang"

```swift
tryCatch("PlingPlang" == raindrops(15))
```

Le son pour 21 est "PlingPlong"

```swift
tryCatch("PlingPlong" == raindrops(21))
```

Le son pour 25 est "Plang"

```swift
tryCatch("Plang" == raindrops(25))
```

Le son pour 27 est "Pling"

```swift
tryCatch("Pling" == raindrops(27))
```

Le son pour 35 est "PlangPlong"

```swift
tryCatch("PlangPlong" == raindrops(35))
```

Le son pour 49 est "Plong"

```swift
tryCatch("Plong" == raindrops(49))
```

Le son pour 52 est "52"

```swift
tryCatch("52" == raindrops(52))
```

Le son pour 105 est "PlingPlangPlong"

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

Le son pour 3125 est "Plang"

```swift
tryCatch("Plang" == raindrops(3125))
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func raindrops(_ num: Int) -> String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


