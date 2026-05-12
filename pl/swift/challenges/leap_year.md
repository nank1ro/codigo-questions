---
language: swift
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

W roku kalendarzowym jest dokładnie 365,25 dnia. Jednak z czasem prowadzi to do zamieszania, ponieważ ludzie normalnie liczą przez dokładną podzielność przez 1, a nie z miejscami dziesiętnymi. Aby temu zapobiec, postanowiono sumować wszystkie 0,25 dnia w każdym cyklu czteroletnim i dawać temu rokowi 366 dni (włącznie z 29 lutego jako dniem przestępnym), nazywając go __rokiem przestępnym__. Pozostałe trzy lata w cyklu czteroletnim zawierają tylko 365 dni i __nie są latami przestępnymi__.

# --instructions--

W tym wyzwaniu podnosimy poprzeczkę — masz określić, czy dany rok jest rokiem przestępnym, bez użycia klasy `Date`, instrukcji `switch`, __bloków if__, __bloków if-else__ ani __operatora trójargumentowego__ (`x ? a : b`), ani operatorów logicznych __AND__ (`&&`) i __OR__ (`||`), z wyjątkiem operatora __NOT__ (`!`).

Zwróć `true` jeśli to rok przestępny, `false` w przeciwnym razie.

Przykład wywołania funkcji:
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

Użycie `Date`, `switch`, `if`, `else`, `&&`, `||` lub `?` jest niedozwolone.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Rok `2016` jest rokiem przestępnym.

```swift
tryCatch(leapYear(2016) == true)
```

Rok `1996` jest rokiem przestępnym.

```swift
tryCatch(leapYear(1996) == true)
```

Rok `1600` jest rokiem przestępnym.

```swift
tryCatch(leapYear(1600) == true)
```

Rok `2020` jest rokiem przestępnym.

```swift
tryCatch(leapYear(2020) == true)
```

Rok `2000` jest rokiem przestępnym.

```swift
tryCatch(leapYear(2000) == true)
```

Rok `2008` jest rokiem przestępnym.

```swift
tryCatch(leapYear(2008) == true)
```

Rok `1521` nie jest rokiem przestępnym.

```swift
tryCatch(leapYear(1521) == false)
```

Rok `1800` nie jest rokiem przestępnym.

```swift
tryCatch(leapYear(1800) == false)
```

Rok `2007` nie jest rokiem przestępnym.

```swift
tryCatch(leapYear(2007) == false)
```

Rok `2002` nie jest rokiem przestępnym.

```swift
tryCatch(leapYear(2002) == false)
```

Rok `1979` nie jest rokiem przestępnym.

```swift
tryCatch(leapYear(1979) == false)
```

Rok `2006` nie jest rokiem przestępnym.

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
