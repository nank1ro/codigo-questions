---
language: swift
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Étant donné deux entiers `num1` et `num2`, écrivez un programme pour additionner ces deux nombres

# --instructions--

Écrivez une fonction qui retourne la somme de deux nombres.
> ASTUCE : omettez les étiquettes d'argument avec le `_` (trait de soulignement)

Exemple d'appel de fonction :
```swift
print(addition(1, 2))
// prints 3
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
func addition() {
    
}
```

# --asserts--

La somme de 1 et 3 doit être égale à 4

```swift
tryCatch(addition(1, 3) == 4)
```

La somme de 200 et 210 doit être égale à 410

```swift
tryCatch(addition(200, 210) == 410)
```

La somme de 15 et 35 doit être égale à 50

```swift
tryCatch(addition(15, 35) == 50)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func addition(_ num1: Int, _ num2: Int) -> Int {
    return num1 + num2
}
```
