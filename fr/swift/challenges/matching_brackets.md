---
language: swift
exerciseType: 1
difficulty: 3
title: Crochets correspondants
---

# --description--

Le texte qui contient du code, des maths ou du balisage regorge de crochets, et chaque crochet ouvrant a besoin d'un crochet fermant de même type. Une chaîne est équilibrée lorsque ses crochets s'apparient et s'imbriquent comme les couches d'un oignon : `{[()]}` est équilibrée, alors que `{[(])}` ne l'est pas, car la paire ronde est fermée avant la paire carrée dans laquelle elle se trouve.

Trois paires comptent ici : les rondes `()`, les carrées `[]` et les accolades `{}`. Tous les autres caractères de la chaîne sont ignorés. Un crochet fermant doit fermer le crochet le plus récemment ouvert encore ouvert, et lorsque la chaîne se termine, aucun crochet ne doit rester ouvert.

# --instructions--

Écrivez une fonction `isBalanced` qui prend une chaîne et retourne `true` lorsque tous les crochets qu'elle contient sont appariés et correctement imbriqués, et `false` sinon.

Exemples :
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Une chaîne vide est équilibrée.
- Les caractères qui ne sont pas des crochets sont ignorés.
- Un crochet fermant doit correspondre au crochet le plus récemment ouvert encore ouvert.
- Aucun crochet ne doit rester ouvert lorsque la chaîne se termine.

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

Une chaîne vide est équilibrée

```swift
tryCatch(isBalanced("") == true)
```

Une seule paire de crochets ronds est équilibrée

```swift
tryCatch(isBalanced("()") == true)
```

Les trois types de paires imbriquées l'une dans l'autre sont équilibrées

```swift
tryCatch(isBalanced("{[()]}") == true)
```

Des crochets mélangés à d'autres textes restent équilibrés

```swift
tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Des paires placées côte à côte sont équilibrées

```swift
tryCatch(isBalanced("()[]{}") == true)
```

Une chaîne sans aucun crochet est équilibrée

```swift
tryCatch(isBalanced("no brackets in here at all") == true)
```

Une paire croisée n'est pas équilibrée

```swift
tryCatch(isBalanced("{[(])}") == false)
```

Un crochet ouvrant jamais fermé n'est pas équilibré

```swift
tryCatch(isBalanced("(") == false)
```

Un crochet fermant avant tout crochet ouvrant n'est pas équilibré

```swift
tryCatch(isBalanced(")(") == false)
```

Des paires croisées plus profondément dans la chaîne ne sont pas équilibrées

```swift
tryCatch(isBalanced("(([]{[}]))") == false)
```

Un crochet fermant restant à la fin n'est pas équilibré

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
