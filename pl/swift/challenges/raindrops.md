---
language: swift
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Twoim zadaniem jest zamiana liczby na ciąg znaków zawierający dźwięki kropli deszczu odpowiadające określonym potencjalnym dzielnikOm.
Dzielnik to liczba, która dzieli inną liczbę bez reszty.
Najprostszym sposobem sprawdzenia, czy liczba jest dzielnikiem innej, jest użycie operacji modulo.
Zasady Raindrops są następujące — jeśli dana liczba:

- ma 3 jako dzielnik, dodaj 'Pling' do wyniku.
- ma 5 jako dzielnik, dodaj 'Plang' do wyniku.
- ma 7 jako dzielnik, dodaj 'Plong' do wyniku.
- nie ma żadnego z 3, 5 ani 7 jako dzielnika, wynikiem powinny być cyfry tej liczby.

# --instructions--

Napisz funkcję, która zwraca poprawny ciąg znaków, przykłady:

- 28 ma 7 jako dzielnik, ale nie 3 ani 5, więc wynik to `"Plong"`.
- 30 ma zarówno 3, jak i 5 jako dzielniki, ale nie 7, więc wynik to `"PlingPlang"`.
- 34 nie jest podzielne przez 3, 5 ani 7, więc wynik to `"34"`.

> WSKAZÓWKA: pomiń etykietę argumentu używając `_` (podkreślnika)

Przykład wywołania funkcji:
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

Dźwięk dla 1 to "1"

```swift
tryCatch("1" == raindrops(1))
```

Dźwięk dla 3 to "Pling"

```swift
tryCatch("Pling" == raindrops(3))
```

Dźwięk dla 5 to "Plang"

```swift
tryCatch("Plang" == raindrops(5))
```

Dźwięk dla 7 to "Plong"

```swift
tryCatch("Plong" == raindrops(7))
```

Dźwięk dla 6 to "Pling"

```swift
tryCatch("Pling" == raindrops(6))
```

Dźwięk dla 8 to "8"

```swift
tryCatch("8" == raindrops(8))
```

Dźwięk dla 9 to "Pling"

```swift
tryCatch("Pling" == raindrops(9))
```

Dźwięk dla 10 to "Plang"

```swift
tryCatch("Plang" == raindrops(10))
```

Dźwięk dla 14 to "Plong"

```swift
tryCatch("Plong" == raindrops(14))
```

Dźwięk dla 15 to "PlingPlang"

```swift
tryCatch("PlingPlang" == raindrops(15))
```

Dźwięk dla 21 to "PlingPlong"

```swift
tryCatch("PlingPlong" == raindrops(21))
```

Dźwięk dla 25 to "Plang"

```swift
tryCatch("Plang" == raindrops(25))
```

Dźwięk dla 27 to "Pling"

```swift
tryCatch("Pling" == raindrops(27))
```

Dźwięk dla 35 to "PlangPlong"

```swift
tryCatch("PlangPlong" == raindrops(35))
```

Dźwięk dla 49 to "Plong"

```swift
tryCatch("Plong" == raindrops(49))
```

Dźwięk dla 52 to "52"

```swift
tryCatch("52" == raindrops(52))
```

Dźwięk dla 105 to "PlingPlangPlong"

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

Dźwięk dla 3125 to "Plang"

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


