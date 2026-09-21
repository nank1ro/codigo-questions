---
language: kotlin
exerciseType: 1
difficulty: 3
title: Parentesi bilanciate
---

# --description--

Il testo che contiene codice, formule matematiche o markup è pieno di parentesi, e ogni parentesi aperta ha bisogno di una chiusa dello stesso tipo. Una stringa è bilanciata quando le sue parentesi si accoppiano e si annidano come gli strati di una cipolla: `{[()]}` è bilanciata, mentre `{[(])}` non lo è, perché la coppia tonda viene chiusa prima della coppia quadrata al cui interno si trova.

Qui contano tre coppie: le tonde `()`, le quadre `[]` e le graffe `{}`. Ogni altro carattere della stringa viene ignorato. Una parentesi chiusa deve chiudere la parentesi aperta più di recente che risulta ancora aperta, e quando la stringa termina nessuna parentesi può rimanere aperta.

# --instructions--

Scrivi una funzione `isBalanced` che prende una stringa e restituisce `true` quando tutte le parentesi in essa contenute sono accoppiate e correttamente annidate, e `false` altrimenti.

Esempi:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Una stringa vuota è bilanciata.
- I caratteri che non sono parentesi vengono ignorati.
- Una parentesi chiusa deve corrispondere alla parentesi aperta più di recente che risulta ancora aperta.
- Nessuna parentesi può rimanere aperta quando la stringa termina.

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

Una stringa vuota è bilanciata

```kotlin
    tryCatch(isBalanced("") == true)
```

Una singola coppia di parentesi tonde è bilanciata

```kotlin
    tryCatch(isBalanced("()") == true)
```

I tre tipi di coppia annidati l'uno dentro l'altro sono bilanciati

```kotlin
    tryCatch(isBalanced("{[()]}") == true)
```

Parentesi mescolate ad altro testo restano comunque bilanciate

```kotlin
    tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Coppie poste una accanto all'altra sono bilanciate

```kotlin
    tryCatch(isBalanced("()[]{}") == true)
```

Una stringa senza alcuna parentesi è bilanciata

```kotlin
    tryCatch(isBalanced("no brackets in here at all") == true)
```

Una coppia incrociata non è bilanciata

```kotlin
    tryCatch(isBalanced("{[(])}") == false)
```

Una parentesi aperta che non viene mai chiusa non è bilanciata

```kotlin
    tryCatch(isBalanced("(") == false)
```

Una parentesi chiusa prima di qualsiasi parentesi aperta non è bilanciata

```kotlin
    tryCatch(isBalanced(")(") == false)
```

Coppie incrociate più in profondità nella stringa non sono bilanciate

```kotlin
    tryCatch(isBalanced("(([]{[}]))") == false)
```

Una parentesi chiusa lasciata alla fine non è bilanciata

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
