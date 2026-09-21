---
language: swift
exerciseType: 1
difficulty: 3
title: 括弧の対応
---

# --description--

コードや数式、マークアップを含むテキストには括弧が数多く登場し、開き括弧にはどれも同じ種類の閉じ括弧が必要です。括弧が対をなして玉ねぎの層のように入れ子になっていくとき、その文字列はバランスが取れています。`{[()]}` はバランスが取れていますが、`{[(])}` はバランスが取れていません。丸括弧の組が、その丸括弧が内側に収まっている角括弧の組よりも先に閉じられているからです。

ここで数えるのは、丸括弧 `()`、角括弧 `[]`、波括弧 `{}` の3組です。文字列内のそれ以外の文字はすべて無視されます。閉じ括弧は、まだ開いている括弧の中で最も新しく開かれた括弧を閉じなければならず、文字列が終わるときに開いたままの括弧が残っていてはいけません。

# --instructions--

文字列を受け取り、その中のすべての括弧が対応して正しく入れ子になっていれば `true` を、そうでなければ `false` を返す関数 `isBalanced` を書いてください。

例:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- 空の文字列はバランスが取れています。
- 括弧以外の文字は無視されます。
- 閉じ括弧は、まだ開いている括弧の中で最も新しく開かれた括弧と対応しなければなりません。
- 文字列が終わるとき、開いたままの括弧が残っていてはいけません。

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
func isBalanced(_ text: String) -> Bool {
    
}
```

# --asserts--

空の文字列はバランスが取れている

```swift
tryCatch(isBalanced("") == true)
```

丸括弧1組だけの文字列はバランスが取れている

```swift
tryCatch(isBalanced("()") == true)
```

3種類の組が互いに入れ子になった文字列はバランスが取れている

```swift
tryCatch(isBalanced("{[()]}") == true)
```

括弧が他のテキストと混ざっていてもバランスが取れている

```swift
tryCatch(isBalanced("{what is (42)}[?]") == true)
```

組が横に並んでいてもバランスが取れている

```swift
tryCatch(isBalanced("()[]{}") == true)
```

括弧をまったく含まない文字列はバランスが取れている

```swift
tryCatch(isBalanced("no brackets in here at all") == true)
```

交差した組はバランスが取れていない

```swift
tryCatch(isBalanced("{[(])}") == false)
```

閉じられないままの開き括弧はバランスが取れていない

```swift
tryCatch(isBalanced("(") == false)
```

開き括弧より先に来る閉じ括弧はバランスが取れていない

```swift
tryCatch(isBalanced(")(") == false)
```

文字列の奥で交差した組はバランスが取れていない

```swift
tryCatch(isBalanced("(([]{[}]))") == false)
```

最後に余った閉じ括弧はバランスが取れていない

```swift
tryCatch(isBalanced("())") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isBalanced(_ text: String) -> Bool {
    let pairs: [Character: Character] = [")": "(", "]": "[", "}": "{"]
    var stack: [Character] = []

    for char in text {
        if char == "(" || char == "[" || char == "{" {
            stack.append(char)
        } else if let opening = pairs[char] {
            if stack.popLast() != opening {
                return false
            }
        }
    }

    return stack.isEmpty
}
```
