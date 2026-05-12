---
language: swift
exerciseType: 1
difficulty: 3
title: Schaltjahr
---

# --description--

In einem Kalenderjahr gibt es genau 365,25 Tage. Dies führt jedoch schließlich zu Verwirrung, da Menschen normalerweise durch genaue Teilbarkeit durch 1 zählen und nicht mit Dezimalzahlen. Um das zu vermeiden, wurde beschlossen, alle 0,25 Tage in jedem Vier-Jahres-Zyklus zu addieren und diesem Jahr 366 Tage (einschließlich 29. Februar als Schalttag) zu geben und es ein __Schaltjahr__ zu nennen. Die anderen drei Jahre im Vier-Jahres-Zyklus würden nur 365 Tage haben und __wären keine Schaltjahre__.

# --instructions--

In dieser Herausforderung werden wir es auf ein neues Niveau heben, wo Sie bestimmen müssen, ob es ein Schaltjahr ist oder nicht, ohne die `Date`-Klasse, `switch`-Anweisungen, __if-Blöcke__, __if-else-Blöcke__ oder __ternäre Operatoren__ (`x ? a : b`) zu verwenden, noch die logischen Operatoren __AND__ (`&&`) und __OR__ (`||`), mit Ausnahme des __NOT__-Operators (`!`).

Geben Sie `true` zurück, wenn es ein Schaltjahr ist, `false` ansonsten.

Beispiel für einen Funktionsaufruf:
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

Die Verwendung von `Date`, `switch`, `if`, `else`, `&&`, `||` oder `?` ist nicht erlaubt.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Das Jahr `2016` ist ein Schaltjahr.

```swift
tryCatch(leapYear(2016) == true)
```

Das Jahr `1996` ist ein Schaltjahr.

```swift
tryCatch(leapYear(1996) == true)
```

Das Jahr `1600` ist ein Schaltjahr.

```swift
tryCatch(leapYear(1600) == true)
```

Das Jahr `2020` ist ein Schaltjahr.

```swift
tryCatch(leapYear(2020) == true)
```

Das Jahr `2000` ist ein Schaltjahr.

```swift
tryCatch(leapYear(2000) == true)
```

Das Jahr `2008` ist ein Schaltjahr.

```swift
tryCatch(leapYear(2008) == true)
```

Das Jahr `1521` ist kein Schaltjahr.

```swift
tryCatch(leapYear(1521) == false)
```

Das Jahr `1800` ist kein Schaltjahr.

```swift
tryCatch(leapYear(1800) == false)
```

Das Jahr `2007` ist kein Schaltjahr.

```swift
tryCatch(leapYear(2007) == false)
```

Das Jahr `2002` ist kein Schaltjahr.

```swift
tryCatch(leapYear(2002) == false)
```

Das Jahr `1979` ist kein Schaltjahr.

```swift
tryCatch(leapYear(1979) == false)
```

Das Jahr `2006` ist kein Schaltjahr.

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
