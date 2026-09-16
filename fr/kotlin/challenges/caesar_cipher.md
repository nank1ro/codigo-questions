---
language: kotlin
exerciseType: 1
difficulty: 2
title: Chiffre de César
---

# --description--

Jules César protégeait ses lettres privées avec l'une des plus anciennes astuces de la cryptographie : il remplaçait chaque lettre d'un message par la lettre située un nombre fixe de positions plus loin dans l'alphabet. Avec un décalage de 3, `a` devient `d`, `b` devient `e` et `c` devient `f`.

L'alphabet se comporte comme un cercle, ainsi les lettres de la fin reviennent au début : avec un décalage de 3, `x` devient `a`, `y` devient `b` et `z` devient `c`.

Tout ce qui n'est pas une lettre, comme un espace, une virgule, un point d'exclamation ou un chiffre, traverse le chiffrement sans être modifié.

# --instructions--

Écrivez une fonction `caesarCipher` qui prend un message `text` et un nombre entier `shift`, et retourne le message encodé.

Exemples :
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Le message est toujours en minuscules, vous n'avez donc jamais à gérer de lettres majuscules.
- Les caractères qui ne sont pas des lettres conservent leur place et leur valeur.
- Le décalage n'est jamais négatif. Un décalage de `0` laisse le message inchangé, et il en va de même pour un décalage de `26`.

# --seed--

```kotlin
fun caesarCipher(text: String, shift: Int): String {
    
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

Un décalage de 3 transforme "hello" en "khoor"

```kotlin
    tryCatch(caesarCipher("hello", 3) == "khoor")
```

La fin de l'alphabet revient au début, ainsi "xyz" devient "abc"

```kotlin
    tryCatch(caesarCipher("xyz", 3) == "abc")
```

Un décalage de 0 laisse le message inchangé

```kotlin
    tryCatch(caesarCipher("abc", 0) == "abc")
```

Un décalage de 26 correspond à un tour complet de l'alphabet, le message est donc inchangé

```kotlin
    tryCatch(caesarCipher("abc", 26) == "abc")
```

La ponctuation et les espaces passent sans être modifiés

```kotlin
    tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

Un message vide reste vide

```kotlin
    tryCatch(caesarCipher("", 4) == "")
```

Les espaces entre les lettres isolées sont conservés

```kotlin
    tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Les chiffres ne sont pas décalés, même avec un décalage de 25

```kotlin
    tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

Un décalage de 13 encode une phrase entière

```kotlin
    tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt")
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
fun caesarCipher(text: String, shift: Int): String {
    val result = StringBuilder()

    for (char in text) {
        if (char in 'a'..'z') {
            result.append('a' + (char - 'a' + shift) % 26)
        } else {
            result.append(char)
        }
    }

    return result.toString()
}
```
