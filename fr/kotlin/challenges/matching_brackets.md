---
language: kotlin
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

Une chaîne vide est équilibrée

```kotlin
    tryCatch(isBalanced("") == true)
```

Une seule paire de crochets ronds est équilibrée

```kotlin
    tryCatch(isBalanced("()") == true)
```

Les trois types de paires imbriquées l'une dans l'autre sont équilibrées

```kotlin
    tryCatch(isBalanced("{[()]}") == true)
```

Des crochets mélangés à d'autres textes restent équilibrés

```kotlin
    tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Des paires placées côte à côte sont équilibrées

```kotlin
    tryCatch(isBalanced("()[]{}") == true)
```

Une chaîne sans aucun crochet est équilibrée

```kotlin
    tryCatch(isBalanced("no brackets in here at all") == true)
```

Une paire croisée n'est pas équilibrée

```kotlin
    tryCatch(isBalanced("{[(])}") == false)
```

Un crochet ouvrant jamais fermé n'est pas équilibré

```kotlin
    tryCatch(isBalanced("(") == false)
```

Un crochet fermant avant tout crochet ouvrant n'est pas équilibré

```kotlin
    tryCatch(isBalanced(")(") == false)
```

Des paires croisées plus profondément dans la chaîne ne sont pas équilibrées

```kotlin
    tryCatch(isBalanced("(([]{[}]))") == false)
```

Un crochet fermant restant à la fin n'est pas équilibré

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
