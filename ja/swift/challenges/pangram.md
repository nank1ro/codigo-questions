---
language: swift
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

パングラムとは、英語のアルファベットのすべての文字を少なくとも1回使う文のことです。最もよく知られている例は "the quick brown fox jumps over the lazy dog" で、26文字すべてを9つの短い単語に収めています。

この判定は大文字と小文字を区別しないため、`A` と `a` は同じ文字として数えます。数字、句読点、スペースは無視されます。これらは文字ではありませんが、文を却下する理由にもなりません。

# --instructions--

文を受け取り、その文がパングラムなら `true` を、そうでなければ `false` を返す関数 `isPangram` を書いてください。

例:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- 空の文はパングラムではありません。
- `a` から `z` までの26文字だけが数えられます。

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

空の文はパングラムではない

```swift
tryCatch(isPangram("") == false)
```

古典的な文 "the quick brown fox jumps over the lazy dog" はパングラムである

```swift
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") == true)
```

文字 `x` が欠けている文はパングラムではない

```swift
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false)
```

文 "the five boxing wizards jump quickly" はパングラムである

```swift
tryCatch(isPangram("the five boxing wizards jump quickly") == true)
```

アンダースコアは無視されるので、その文は依然としてパングラムである

```swift
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true)
```

数字は無視されるので、その文は依然としてパングラムである

```swift
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true)
```

数字は文字 `e`、`i`、`t` の代わりにはならない

```swift
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false)
```

大文字の文もパングラムである

```swift
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true)
```

アルファベットの同じ半分の大文字と小文字を混ぜるだけでは足りない

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
