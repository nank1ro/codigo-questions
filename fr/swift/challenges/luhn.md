---
language: swift
exerciseType: 1
difficulty: 2
title: Luhn checksum
---

# --description--

L'algorithme de Luhn est une somme de contrôle simple utilisée pour valider des numéros d'identification, tels que les numéros de carte bancaire.

Avant de vérifier un numéro, supprimez tous les espaces de la chaîne. La chaîne est valide uniquement si ce qui reste contient plus d'un caractère et si la chaîne d'origine ne contient rien d'autre que des chiffres et des espaces.

Pour effectuer la vérification, partez du chiffre le plus à droite et progressez vers la gauche en doublant un chiffre sur deux. Lorsque le doublement produit un nombre supérieur à 9, soustrayez-lui 9. Additionnez ensuite tous les chiffres : le numéro est valide uniquement si la somme est divisible par 10.

Par exemple, `"059"` donne `0`, puis `5` doublé donne `10`, qui devient `1`, puis `9`. Leur somme est `10`, qui est divisible par 10, donc le numéro est valide.

# --instructions--

Écrivez une fonction `isValid` qui prend une chaîne et retourne `true` lorsque le numéro est valide, `false` sinon.

- `"4539 3195 0343 6467"` passe la somme de contrôle, donc le résultat est `true`.
- `"8273 1232 7352 0569"` échoue à la somme de contrôle, donc le résultat est `false`.
- `"0"` ne contient qu'un seul caractère, donc le résultat est `false`.
- `"055-444-285"` contient un caractère qui n'est ni un chiffre ni un espace, donc le résultat est `false`.

> ASTUCE : omettez l'étiquette d'argument avec `_` (tiret bas)

Exemple d'appel de fonction :
```swift
print(isValid("095 245 88"))
// prints true
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
func isValid(_ value: String) -> Bool {
    
}
```

# --asserts--

Un chiffre seul n'est pas valide.

```swift
tryCatch(isValid("0") == false)
```

Un chiffre seul avec un espace au début n'est pas valide.

```swift
tryCatch(isValid(" 0") == false)
```

Le numéro `"059"` est valide.

```swift
tryCatch(isValid("059") == true)
```

Le numéro `"59"` est valide.

```swift
tryCatch(isValid("59") == true)
```

Le numéro `"055 444 285"` est valide.

```swift
tryCatch(isValid("055 444 285") == true)
```

Le numéro `"055 444 286"` n'est pas valide.

```swift
tryCatch(isValid("055 444 286") == false)
```

Le numéro `"8273 1232 7352 0569"` n'est pas valide.

```swift
tryCatch(isValid("8273 1232 7352 0569") == false)
```

Le numéro `"4539 3195 0343 6467"` est valide.

```swift
tryCatch(isValid("4539 3195 0343 6467") == true)
```

Le numéro `"1 2345 6789 1234 5678 9012"` n'est pas valide.

```swift
tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

Le numéro `"095 245 88"` est valide.

```swift
tryCatch(isValid("095 245 88") == true)
```

Une lettre rend le numéro invalide.

```swift
tryCatch(isValid("055a 444 285") == false)
```

Les tirets rendent le numéro invalide.

```swift
tryCatch(isValid("055-444-285") == false)
```

Un caractère de ponctuation rend le numéro invalide.

```swift
tryCatch(isValid(":9") == false)
```

Les symboles rendent le numéro invalide.

```swift
tryCatch(isValid("055# 444$ 285") == false)
```

Une chaîne vide n'est pas valide.

```swift
tryCatch(isValid("") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isValid(_ value: String) -> Bool {
    var sum = 0
    var count = 0
    for character in value.reversed() {
        if character == " " {
            continue
        }
        guard character.isASCII, character.isNumber,
              let number = character.wholeNumberValue else {
            return false
        }
        var digit = number
        if count % 2 == 1 {
            digit *= 2
            if digit > 9 {
                digit -= 9
            }
        }
        sum += digit
        count += 1
    }
    return count > 1 && sum % 10 == 0
}
```
