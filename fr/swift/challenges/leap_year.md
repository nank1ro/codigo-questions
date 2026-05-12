---
language: swift
exerciseType: 1
difficulty: 3
title: Année bissextile
---

# --description--

Il y a exactement 365,25 jours dans une année civile. Cependant, cela finira par créer de la confusion car les humains comptent normalement par divisibilité exacte de 1 et non par des points décimaux. Donc, pour éviter ce problème, on a décidé d'additionner tous les 0,25 jours tous les quatre ans et de donner à cette année 366 jours (y compris le 29 février en tant que jour intercalaire) et de l'appeler une **année bissextile**. Les trois autres années du cycle de quatre ans ne contiendraient que 365 jours et **ne seraient pas des années bissextiles**.

# --instructions--

Dans ce défi, nous allons le porter à un nouveau niveau, où vous devez déterminer si c'est une année bissextile ou non sans utiliser la classe `Date`, les instructions `switch`, les **blocs if**, les **blocs if-else** ou l'**opération ternaire** (`x ? a : b`) ni les opérateurs logiques **ET** (`&&`) et **OU** (`||`) à l'exception de l'opérateur **NON** (`!`).

Retournez `true` si c'est une année bissextile, `false` sinon.

Exemple d'appel de fonction :
```swift
print(leapYear(2000))
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
func leapYear(_ year: Int) -> Bool {
    
}
```

# --asserts--

L'utilisation de `Date`, `switch`, `if`, `else`, `&&`, `||` ou `?` n'est pas autorisée.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

L'année `2016` est une année bissextile.

```swift
tryCatch(leapYear(2016) == true)
```

L'année `1996` est une année bissextile.

```swift
tryCatch(leapYear(1996) == true)
```

L'année `1600` est une année bissextile.

```swift
tryCatch(leapYear(1600) == true)
```

L'année `2020` est une année bissextile.

```swift
tryCatch(leapYear(2020) == true)
```

L'année `2000` est une année bissextile.

```swift
tryCatch(leapYear(2000) == true)
```

L'année `2008` est une année bissextile.

```swift
tryCatch(leapYear(2008) == true)
```

L'année `1521` n'est pas une année bissextile.

```swift
tryCatch(leapYear(1521) == false)
```

L'année `1800` n'est pas une année bissextile.

```swift
tryCatch(leapYear(1800) == false)
```

L'année `2007` n'est pas une année bissextile.

```swift
tryCatch(leapYear(2007) == false)
```

L'année `2002` n'est pas une année bissextile.

```swift
tryCatch(leapYear(2002) == false)
```

L'année `1979` n'est pas une année bissextile.

```swift
tryCatch(leapYear(1979) == false)
```

L'année `2006` n'est pas une année bissextile.

```swift
tryCatch(leapYear(2006) == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func leapYear(_ year: Int) -> Bool {
    var yr = year
    while yr % 100 == 0 {
        yr = yr / 100
    }
    return yr % 4 == 0
}
```
