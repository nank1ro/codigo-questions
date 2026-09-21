---
language: kotlin
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

# --seed--

```kotlin
fun isBalanced(text: String): Boolean {
    
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

Ein leerer String ist ausgeglichen

```kotlin
    tryCatch(isBalanced("") == true)
```

Ein einzelnes Paar runder Klammern ist ausgeglichen

```kotlin
    tryCatch(isBalanced("()") == true)
```

Die drei Arten von Paaren, ineinander verschachtelt, sind ausgeglichen

```kotlin
    tryCatch(isBalanced("{[()]}") == true)
```

Klammern, die mit anderem Text vermischt sind, sind weiterhin ausgeglichen

```kotlin
    tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Nebeneinander stehende Paare sind ausgeglichen

```kotlin
    tryCatch(isBalanced("()[]{}") == true)
```

Ein String ohne jegliche Klammern ist ausgeglichen

```kotlin
    tryCatch(isBalanced("no brackets in here at all") == true)
```

Ein überkreuztes Paar ist nicht ausgeglichen

```kotlin
    tryCatch(isBalanced("{[(])}") == false)
```

Eine öffnende Klammer, die nie geschlossen wird, ist nicht ausgeglichen

```kotlin
    tryCatch(isBalanced("(") == false)
```

Eine schließende Klammer vor jeder öffnenden ist nicht ausgeglichen

```kotlin
    tryCatch(isBalanced(")(") == false)
```

Überkreuzte Paare tiefer im String sind nicht ausgeglichen

```kotlin
    tryCatch(isBalanced("(([]{[}]))") == false)
```

Eine am Ende übrig gebliebene schließende Klammer ist nicht ausgeglichen

```kotlin
    tryCatch(isBalanced("())") == false)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun isBalanced(text: String): Boolean {
    val pairs = mapOf(')' to '(', ']' to '[', '}' to '{')
    val stack = ArrayDeque<Char>()

    for (char in text) {
        if (char == '(' || char == '[' || char == '{') {
            stack.addLast(char)
        } else if (pairs.containsKey(char)) {
            if (stack.isEmpty() || stack.removeLast() != pairs[char]) {
                return false
            }
        }
    }

    return stack.isEmpty()
}
```
