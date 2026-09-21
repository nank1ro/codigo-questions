---
language: swift
exerciseType: 1
difficulty: 3
title: 괄호 짝 맞추기
---

# --description--

코드, 수식 또는 마크업을 담는 텍스트에는 괄호가 가득하며, 모든 여는 괄호에는 같은 종류의 닫는 괄호가 필요합니다. 문자열의 괄호들이 양파의 겹처럼 쌍을 이루고 중첩될 때 그 문자열은 균형이 잡혀 있다고 합니다: `{[()]}`는 균형이 잡혀 있지만, `{[(])}`는 그렇지 않습니다. 이는 그 안에 있는 둥근 괄호 쌍이 자신을 감싸고 있는 대괄호 쌍보다 먼저 닫히기 때문입니다.

여기서는 세 쌍이 대상입니다: 둥근 괄호 `()`, 대괄호 `[]`, 그리고 중괄호 `{}`입니다. 문자열에 있는 다른 모든 문자는 무시합니다. 닫는 괄호는 아직 열려 있는 괄호 중 가장 최근에 열린 괄호를 닫아야 하며, 문자열이 끝날 때 열려 있는 괄호가 남아 있어서는 안 됩니다.

# --instructions--

문자열을 받아 그 안의 모든 괄호가 서로 맞고 올바르게 중첩되어 있으면 `true`를, 그렇지 않으면 `false`를 반환하는 함수 `isBalanced`를 작성하세요.

예시:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- 빈 문자열은 균형이 잡혀 있습니다.
- 괄호가 아닌 문자는 무시합니다.
- 닫는 괄호는 아직 열려 있는 괄호 중 가장 최근에 열린 괄호와 맞아야 합니다.
- 문자열이 끝날 때 열려 있는 괄호가 남아 있으면 안 됩니다.

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

빈 문자열은 균형이 잡혀 있습니다

```swift
tryCatch(isBalanced("") == true)
```

둥근 괄호 한 쌍은 균형이 잡혀 있습니다

```swift
tryCatch(isBalanced("()") == true)
```

세 종류의 쌍이 서로 중첩되어 있으면 균형이 잡혀 있습니다

```swift
tryCatch(isBalanced("{[()]}") == true)
```

다른 텍스트와 섞인 괄호도 여전히 균형이 잡혀 있습니다

```swift
tryCatch(isBalanced("{what is (42)}[?]") == true)
```

나란히 놓인 쌍들은 균형이 잡혀 있습니다

```swift
tryCatch(isBalanced("()[]{}") == true)
```

괄호가 전혀 없는 문자열은 균형이 잡혀 있습니다

```swift
tryCatch(isBalanced("no brackets in here at all") == true)
```

교차된 쌍은 균형이 잡혀 있지 않습니다

```swift
tryCatch(isBalanced("{[(])}") == false)
```

끝까지 닫히지 않는 여는 괄호는 균형이 잡혀 있지 않습니다

```swift
tryCatch(isBalanced("(") == false)
```

여는 괄호보다 먼저 나오는 닫는 괄호는 균형이 잡혀 있지 않습니다

```swift
tryCatch(isBalanced(")(") == false)
```

문자열 깊은 곳에서 교차된 쌍들은 균형이 잡혀 있지 않습니다

```swift
tryCatch(isBalanced("(([]{[}]))") == false)
```

끝에 남는 닫는 괄호는 균형이 잡혀 있지 않습니다

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
