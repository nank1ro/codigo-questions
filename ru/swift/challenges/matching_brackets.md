---
language: swift
exerciseType: 1
difficulty: 3
title: Сбалансированные скобки
---

# --description--

Текст, в котором есть код, математика или разметка, полон скобок, и каждой открывающей скобке нужна закрывающая того же вида. Строка сбалансирована, когда её скобки образуют пары и вкладываются друг в друга, как слои луковицы: `{[()]}` сбалансирована, а `{[(])}` — нет, ведь круглая пара закрывается раньше квадратной пары, внутри которой она находится.

Здесь учитываются три пары: круглые `()`, квадратные `[]` и фигурные `{}`. Все остальные символы строки игнорируются. Закрывающая скобка должна закрывать последнюю из ещё открытых скобок, а к концу строки не должно остаться ни одной незакрытой скобки.

# --instructions--

Напишите функцию `isBalanced`, которая принимает строку и возвращает `true`, если все скобки в ней образуют пары и правильно вложены, и `false` в противном случае.

Примеры:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Пустая строка сбалансирована.
- Символы, не являющиеся скобками, игнорируются.
- Закрывающая скобка должна соответствовать последней из ещё открытых скобок.
- К концу строки не должно оставаться ни одной открытой скобки.

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

Пустая строка сбалансирована

```swift
tryCatch(isBalanced("") == true)
```

Одна пара круглых скобок сбалансирована

```swift
tryCatch(isBalanced("()") == true)
```

Три вида пар, вложенные друг в друга, сбалансированы

```swift
tryCatch(isBalanced("{[()]}") == true)
```

Скобки вперемешку с другим текстом остаются сбалансированными

```swift
tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Пары, стоящие друг за другом, сбалансированы

```swift
tryCatch(isBalanced("()[]{}") == true)
```

Строка вовсе без скобок сбалансирована

```swift
tryCatch(isBalanced("no brackets in here at all") == true)
```

Перекрёстная пара не сбалансирована

```swift
tryCatch(isBalanced("{[(])}") == false)
```

Открывающая скобка, которая никогда не закрывается, не сбалансирована

```swift
tryCatch(isBalanced("(") == false)
```

Закрывающая скобка раньше любой открывающей не сбалансирована

```swift
tryCatch(isBalanced(")(") == false)
```

Перекрёстные пары в глубине строки не сбалансированы

```swift
tryCatch(isBalanced("(([]{[}]))") == false)
```

Лишняя закрывающая скобка в конце строки не сбалансирована

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
