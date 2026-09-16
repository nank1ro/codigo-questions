---
language: swift
exerciseType: 1
difficulty: 2
title: Anagram
---

# --description--

Dwa słowa są anagramami, gdy jedno jest przestawieniem drugiego: używają dokładnie tych samych liter, a każda z nich występuje tę samą liczbę razy, tylko w innej kolejności. `listen` i `silent` są anagramami, podobnie jak `stone` i `tones`.

Słowo nigdy nie jest anagramem samego siebie. Jeśli oba słowa są dokładnie takie same, nic nie zostało przestawione, więc odpowiedź to `false`. Oba słowa są podane małymi literami i zawierają wyłącznie litery od `a` do `z`.

# --instructions--

Napisz funkcję `isAnagram`, która przyjmuje dwa słowa, `first` i `second`, i zwraca `true`, gdy jedno z nich jest anagramem drugiego, oraz `false` w przeciwnym razie.

Przykłady:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Dwa identyczne słowa nie są anagramami.
- Słowa o różnych długościach nigdy nie są anagramami.
- Każda litera musi występować tyle samo razy w obu słowach.

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
func isAnagram(_ first: String, _ second: String) -> Bool {
    
}
```

# --asserts--

Słowa "listen" i "silent" są anagramami

```swift
tryCatch(isAnagram("listen", "silent") == true)
```

Słowa "stone" i "tones" są anagramami

```swift
tryCatch(isAnagram("stone", "tones") == true)
```

Słowo nie jest anagramem samego siebie

```swift
tryCatch(isAnagram("stone", "stone") == false)
```

Słowa o różnych długościach nie są anagramami

```swift
tryCatch(isAnagram("abc", "abcd") == false)
```

Te same litery w różnych ilościach nie tworzą anagramu

```swift
tryCatch(isAnagram("aab", "abb") == false)
```

Słowa "anagram" i "nagaram" są anagramami

```swift
tryCatch(isAnagram("anagram", "nagaram") == true)
```

Dwa słowa tej samej długości z różnymi literami nie są anagramami

```swift
tryCatch(isAnagram("rat", "car") == false)
```

Dwa puste słowa są identyczne, więc nie są anagramami

```swift
tryCatch(isAnagram("", "") == false)
```

Dwie różne pojedyncze litery nie są anagramami

```swift
tryCatch(isAnagram("a", "b") == false)
```

Słowa "evil" i "vile" są anagramami

```swift
tryCatch(isAnagram("evil", "vile") == true)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isAnagram(_ first: String, _ second: String) -> Bool {
    if first == second {
        return false
    }

    return first.sorted() == second.sorted()
}
```
