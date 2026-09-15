---
language: swift
exerciseType: 1
difficulty: 1
title: Hipoteza Collatza
---

# --description--

Hipoteza Collatza zaczyna się od dowolnej dodatniej liczby całkowitej `n` i powtarza jedną prostą regułę: jeśli `n` jest parzyste, dzielimy je na pół; jeśli `n` jest nieparzyste, zastępujemy je wartością `3n + 1`. Prędzej czy później ciąg osiąga 1.

Na przykład ciąg zaczynający się od 16 to `16 -> 8 -> 4 -> 2 -> 1`, więc zajmuje to 4 kroki.

Nikt nigdy nie udowodnił, że zawsze tak się dzieje, ale reguła ta obowiązuje dla każdej dotychczas przetestowanej liczby.

# --instructions--

Napisz funkcję `collatzSteps`, która przyjmuje dodatnią liczbę całkowitą `n` i zwraca liczbę kroków potrzebnych do osiągnięcia 1.

`collatzSteps(1)` to 0, ponieważ 1 to już koniec ciągu. `collatzSteps(12)` to 9, a `collatzSteps(27)` to 111.

Przykład wywołania funkcji:
```swift
print(collatzSteps(16))
// wypisuje 4
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

`collatzSteps(1)` powinno zwrócić 0, ponieważ 1 to już koniec ciągu.

```swift
tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` powinno zwrócić 1.

```swift
tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` powinno zwrócić 8.

```swift
tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` powinno zwrócić 16.

```swift
tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` powinno zwrócić 4.

```swift
tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` powinno zwrócić 9.

```swift
tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` powinno zwrócić 111.

```swift
tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` powinno zwrócić 118.

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
