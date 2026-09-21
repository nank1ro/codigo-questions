---
language: swift
exerciseType: 1
difficulty: 2
title: Horloge
---

# --description--

Une horloge 24 heures affiche l'heure de la journée sous la forme `HH:MM`, commençant à `00:00` juste après minuit et se terminant à `23:59` une minute avant le minuit suivant. Les deux parties sont toujours écrites avec deux chiffres, ainsi neuf minutes après onze heures du matin se lit `11:09`.

Une journée entière dure 1440 minutes. Lorsque l'horloge dépasse `23:59`, elle repasse à `00:00` et recommence la journée, et la remonter en arrière avant `00:00` la fait atterrir sur `23:59`.

# --instructions--

Écrivez une fonction `clockTime` qui prend deux nombres entiers, `hours` et `minutes`, et retourne l'affichage d'une horloge 24 heures sous la forme de la chaîne `"HH:MM"`, les deux parties étant complétées sur deux chiffres.

Exemples :
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Chacun des deux nombres peut être négatif ou plus grand que ce qu'une véritable horloge permet.
- Calculez le nombre total de minutes avec `hours * 60 + minutes`, puis ramenez ce total dans la plage de `0` à `1439` afin que l'horloge boucle dans les deux sens.
- `clockTime(24, 0)` correspond exactement à une journée, donc l'affichage est `"00:00"`.

> ASTUCE : omettez les étiquettes d'arguments avec le `_` (trait de soulignement)

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
func clockTime(_ hours: Int, _ minutes: Int) -> String {
    
}
```

# --asserts--

Huit heures du matin se lit `08:00`

```swift
tryCatch(clockTime(8, 0) == "08:00")
```

Les chiffres uniques sont complétés sur deux chiffres, ainsi neuf minutes après onze heures se lit `11:09`

```swift
tryCatch(clockTime(11, 9) == "11:09")
```

Exactement une journée entière d'heures repasse à `00:00`

```swift
tryCatch(clockTime(24, 0) == "00:00")
```

Les minutes au-delà de 60 se reportent sur les heures

```swift
tryCatch(clockTime(25, 160) == "03:40")
```

Une heure négative remonte l'horloge en arrière au-delà de minuit

```swift
tryCatch(clockTime(-1, 15) == "23:15")
```

Un nombre de minutes négatif remonte également l'horloge en arrière

```swift
tryCatch(clockTime(0, -90) == "22:30")
```

Plus d'une journée entière en arrière continue de boucler

```swift
tryCatch(clockTime(-25, 0) == "23:00")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func clockTime(_ hours: Int, _ minutes: Int) -> String {
    // Le % conserve le signe de l'opérande de gauche, donc ajoutez une journée
    // entière avant de ramener à nouveau pour atterrir dans 0..1439.
    let total = (((hours * 60 + minutes) % 1440) + 1440) % 1440

    return String(format: "%02d:%02d", total / 60, total % 60)
}
```
