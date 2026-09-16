---
language: kotlin
exerciseType: 1
difficulty: 2
title: Anagrama
---

# --description--

Duas palavras são anagramas quando uma é um rearranjo da outra: elas usam exatamente as mesmas letras, cada letra o mesmo número de vezes, apenas em uma ordem diferente. `listen` e `silent` são anagramas, assim como `stone` e `tones`.

Uma palavra nunca é um anagrama de si mesma. Se as duas palavras forem exatamente iguais, nada foi rearranjado, então a resposta é `false`. Ambas as palavras são dadas em minúsculas e contêm apenas as letras de `a` a `z`.

# --instructions--

Escreva uma função `isAnagram` que recebe duas palavras, `first` e `second`, e retorna `true` quando elas são anagramas uma da outra e `false` caso contrário.

Exemplos:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Duas palavras idênticas não são anagramas.
- Palavras de tamanhos diferentes nunca são anagramas.
- Cada letra deve aparecer o mesmo número de vezes nas duas palavras.

# --seed--

```kotlin
fun isAnagram(first: String, second: String): Boolean {
    
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

As palavras "listen" e "silent" são anagramas

```kotlin
    tryCatch(isAnagram("listen", "silent") == true)
```

As palavras "stone" e "tones" são anagramas

```kotlin
    tryCatch(isAnagram("stone", "tones") == true)
```

Uma palavra não é um anagrama de si mesma

```kotlin
    tryCatch(isAnagram("stone", "stone") == false)
```

Palavras de tamanhos diferentes não são anagramas

```kotlin
    tryCatch(isAnagram("abc", "abcd") == false)
```

As mesmas letras em quantidades diferentes não formam um anagrama

```kotlin
    tryCatch(isAnagram("aab", "abb") == false)
```

As palavras "anagram" e "nagaram" são anagramas

```kotlin
    tryCatch(isAnagram("anagram", "nagaram") == true)
```

Duas palavras do mesmo tamanho com letras diferentes não são anagramas

```kotlin
    tryCatch(isAnagram("rat", "car") == false)
```

Duas palavras vazias são idênticas, então não são anagramas

```kotlin
    tryCatch(isAnagram("", "") == false)
```

Duas letras únicas diferentes não são anagramas

```kotlin
    tryCatch(isAnagram("a", "b") == false)
```

As palavras "evil" e "vile" são anagramas

```kotlin
    tryCatch(isAnagram("evil", "vile") == true)
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
fun isAnagram(first: String, second: String): Boolean {
    if (first == second) {
        return false
    }

    return first.toList().sorted() == second.toList().sorted()
}
```
