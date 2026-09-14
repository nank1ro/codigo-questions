---
language: swift
exerciseType: 1
difficulty: 1
title: Collatz-Vermutung
---

# --description--

Die Collatz-Vermutung startet von einer beliebigen positiven ganzen Zahl `n` und wiederholt eine einfache Regel: Ist `n` gerade, wird es halbiert; ist `n` ungerade, wird es durch `3n + 1` ersetzt. Früher oder später erreicht die Folge die 1.

Startet man zum Beispiel bei 16, lautet die Folge `16 -> 8 -> 4 -> 2 -> 1`, sie benötigt also 4 Schritte.

Niemand hat je bewiesen, dass das immer geschieht, aber es gilt für jede bisher getestete Zahl.

# --instructions--

Schreiben Sie eine Funktion `collatzSteps`, die eine positive ganze Zahl `n` nimmt und die Anzahl der Schritte zurückgibt, die benötigt werden, um 1 zu erreichen.

`collatzSteps(1)` ist 0, weil 1 bereits das Ende der Folge ist. `collatzSteps(12)` ist 9, und `collatzSteps(27)` ist 111.

Beispiel eines Funktionsaufrufs:
```swift
print(collatzSteps(16))
// prints 4
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

`collatzSteps(1)` sollte 0 zurückgeben, weil 1 bereits das Ende der Folge ist.

```swift
tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` sollte 1 zurückgeben.

```swift
tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` sollte 8 zurückgeben.

```swift
tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` sollte 16 zurückgeben.

```swift
tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` sollte 4 zurückgeben.

```swift
tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` sollte 9 zurückgeben.

```swift
tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` sollte 111 zurückgeben.

```swift
tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` sollte 118 zurückgeben.

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
