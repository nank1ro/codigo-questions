---
language: swift
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

Панграмма — это предложение, в котором каждая буква английского алфавита используется хотя бы один раз. Самый известный пример — "the quick brown fox jumps over the lazy dog", в котором все 26 букв умещаются в девять коротких слов.

Проверка не учитывает регистр, поэтому `A` и `a` считаются одной и той же буквой. Цифры, знаки препинания и пробелы игнорируются: они не являются буквами, но и не являются причиной отклонить предложение.

# --instructions--

Напишите функцию `isPangram`, которая принимает предложение и возвращает `true`, если предложение является панграммой, и `false` в противном случае.

Примеры:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Пустое предложение не является панграммой.
- Считаются только 26 букв от `a` до `z`.

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
func isPangram(_ sentence: String) -> Bool {
    
}
```

# --asserts--

Пустое предложение не является панграммой

```swift
tryCatch(isPangram("") == false)
```

Классическое предложение "the quick brown fox jumps over the lazy dog" является панграммой

```swift
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") == true)
```

Предложение, в котором отсутствует буква `x`, не является панграммой

```swift
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false)
```

Предложение "the five boxing wizards jump quickly" является панграммой

```swift
tryCatch(isPangram("the five boxing wizards jump quickly") == true)
```

Подчёркивания игнорируются, поэтому предложение остаётся панграммой

```swift
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true)
```

Цифры игнорируются, поэтому предложение остаётся панграммой

```swift
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true)
```

Цифры не заменяют буквы `e`, `i` и `t`

```swift
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false)
```

Предложение в верхнем регистре тоже является панграммой

```swift
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true)
```

Смешения регистров одной и той же половины алфавита недостаточно

```swift
tryCatch(isPangram("abcdefghijklm ABCDEFGHIJKLM") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isPangram(_ sentence: String) -> Bool {
    var letters = Set<Character>()

    for char in sentence.lowercased() {
        if char.isASCII && char.isLetter {
            letters.insert(char)
        }
    }

    return letters.count == 26
}
```
