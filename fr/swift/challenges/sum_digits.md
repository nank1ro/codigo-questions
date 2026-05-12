---
language: swift
exerciseType: 1
difficulty: 1
title: Somme des chiffres
---

# --description--

On vous donne un entier `N`.
Écrivez un programme pour calculer la somme de tous les chiffres de N

# --instructions--

Retournez la somme des chiffres de `N`.
> ASTUCE : omettez l'étiquette d'argument avec le `_` (trait de soulignement)

Exemple d'appel de fonction :
```swift
print(sumDigits(28))
// prints 10
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
func sumDigits() {

}
```

# --asserts--

La somme des chiffres de 12345 est 15

```swift
tryCatch(sumDigits(12345) == 15)
```

La somme des chiffres de 57253 est 22

```swift
tryCatch(sumDigits(57253) == 22)
```

La somme des chiffres de 122 est 5

```swift
tryCatch(sumDigits(122) == 5)
```

La somme des chiffres de 91979997 est 60

```swift
tryCatch(sumDigits(91979997) == 60)
```

La somme des chiffres de 2147483647 est 46

```swift
tryCatch(sumDigits(2147483647) == 46)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func sumDigits(_ num: Int) -> Int {
    var n = num
    var result = 0
    while n > 0 {
        result += n % 10
        n = Int(n / 10)
    }
    return result
}
```

