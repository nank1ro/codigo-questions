---
language: swift
exerciseType: 1
difficulty: 2
title: Szyfr Cezara
---

# --description--

Juliusz Cezar chronił swoje prywatne listy jedną z najstarszych sztuczek kryptografii: zastępował każdą literę wiadomości literą oddaloną o stałą liczbę pozycji w alfabecie. Przy przesunięciu o 3 `a` staje się `d`, `b` staje się `e`, a `c` staje się `f`.

Alfabet zachowuje się jak okrąg, więc litery z końca zawijają się z powrotem do początku: przy przesunięciu o 3 `x` staje się `a`, `y` staje się `b`, a `z` staje się `c`.

Wszystko, co nie jest literą, na przykład spacja, przecinek, wykrzyknik albo cyfra, przechodzi przez szyfr bez zmian.

# --instructions--

Napisz funkcję `caesarCipher`, która przyjmuje wiadomość `text` i liczbę całkowitą `shift`, i zwraca zaszyfrowaną wiadomość.

Przykłady:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Wiadomość zawsze składa się z małych liter, więc nie musisz przejmować się wielkimi literami.
- Znaki, które nie są literami, zachowują swoje miejsce i swoją wartość.
- Przesunięcie nigdy nie jest ujemne. Przesunięcie o `0` pozostawia wiadomość bez zmian, podobnie jak przesunięcie o `26`.

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
func caesarCipher(_ text: String, _ shift: Int) -> String {
    
}
```

# --asserts--

Przesunięcie o 3 zamienia "hello" w "khoor"

```swift
tryCatch(caesarCipher("hello", 3) == "khoor")
```

Koniec alfabetu zawija się do początku, więc "xyz" staje się "abc"

```swift
tryCatch(caesarCipher("xyz", 3) == "abc")
```

Przesunięcie o 0 pozostawia wiadomość bez zmian

```swift
tryCatch(caesarCipher("abc", 0) == "abc")
```

Przesunięcie o 26 to pełny obrót alfabetu, więc wiadomość pozostaje bez zmian

```swift
tryCatch(caesarCipher("abc", 26) == "abc")
```

Znaki interpunkcyjne i spacje przechodzą bez zmian

```swift
tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

Pusta wiadomość pozostaje pusta

```swift
tryCatch(caesarCipher("", 4) == "")
```

Spacje między pojedynczymi literami są zachowane

```swift
tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Cyfry nie są przesuwane, nawet przy przesunięciu o 25

```swift
tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

Przesunięcie o 13 szyfruje całe zdanie

```swift
tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func caesarCipher(_ text: String, _ shift: Int) -> String {
    let a = UInt8(ascii: "a")
    let z = UInt8(ascii: "z")
    let offset = UInt8(shift % 26)
    var bytes = Array(text.utf8)

    for i in 0..<bytes.count {
        let b = bytes[i]
        if b >= a && b <= z {
            bytes[i] = a + (b - a + offset) % 26
        }
    }

    return String(decoding: bytes, as: UTF8.self)
}
```
