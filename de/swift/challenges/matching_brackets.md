---
language: swift
exerciseType: 1
difficulty: 3
title: Passende Klammern
---

# --description--

Text, der Code, Formeln oder Markup enthält, ist voller Klammern, und jede öffnende Klammer braucht eine schließende derselben Art. Ein String ist ausgeglichen, wenn sich seine Klammern paarweise entsprechen und wie die Schichten einer Zwiebel verschachteln: `{[()]}` ist ausgeglichen, `{[(])}` dagegen nicht, weil das runde Paar vor dem eckigen Paar geschlossen wird, in dem es liegt.

Hier zählen drei Paare: runde `()`, eckige `[]` und geschweifte `{}`. Jedes andere Zeichen im String wird ignoriert. Eine schließende Klammer muss die zuletzt geöffnete Klammer schließen, die noch offen ist, und wenn der String endet, darf keine Klammer offen geblieben sein.

# --instructions--

Schreiben Sie eine Funktion `isBalanced`, die einen String entgegennimmt und `true` zurückgibt, wenn alle darin enthaltenen Klammern übereinstimmen und korrekt verschachtelt sind, und andernfalls `false`.

Beispiele:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Ein leerer String ist ausgeglichen.
- Zeichen, die keine Klammern sind, werden ignoriert.
- Eine schließende Klammer muss zu der zuletzt geöffneten Klammer passen, die noch offen ist.
- Wenn der String endet, darf keine Klammer offen geblieben sein.

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

Ein leerer String ist ausgeglichen

```swift
tryCatch(isBalanced("") == true)
```

Ein einzelnes Paar runder Klammern ist ausgeglichen

```swift
tryCatch(isBalanced("()") == true)
```

Die drei Arten von Paaren, ineinander verschachtelt, sind ausgeglichen

```swift
tryCatch(isBalanced("{[()]}") == true)
```

Klammern, die mit anderem Text vermischt sind, sind weiterhin ausgeglichen

```swift
tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Nebeneinander stehende Paare sind ausgeglichen

```swift
tryCatch(isBalanced("()[]{}") == true)
```

Ein String ohne jegliche Klammern ist ausgeglichen

```swift
tryCatch(isBalanced("no brackets in here at all") == true)
```

Ein überkreuztes Paar ist nicht ausgeglichen

```swift
tryCatch(isBalanced("{[(])}") == false)
```

Eine öffnende Klammer, die nie geschlossen wird, ist nicht ausgeglichen

```swift
tryCatch(isBalanced("(") == false)
```

Eine schließende Klammer vor jeder öffnenden ist nicht ausgeglichen

```swift
tryCatch(isBalanced(")(") == false)
```

Überkreuzte Paare tiefer im String sind nicht ausgeglichen

```swift
tryCatch(isBalanced("(([]{[}]))") == false)
```

Eine am Ende übrig gebliebene schließende Klammer ist nicht ausgeglichen

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
