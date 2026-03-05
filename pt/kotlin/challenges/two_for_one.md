---
language: kotlin
exerciseType: 1
difficulty: 1
title: "Dois por um"
---

# --description--

Dado um nome, retorne uma string com a mensagem:
`One for X, one for me.`
Onde `X` é o nome fornecido.
No entanto, se o nome estiver ausente, retorne a string:
`One for you, one for me.`

# --instructions--

Escreva uma função que retorne a string correta, exemplos:

**entrada**: `Walter`
**saída**: `One for Walter, one for me.`

**entrada**: `James`
**saída**: `One for James, one for me.`

**entrada**: `Martha`
**saída**: `One for Martha, one for me.`

# --seed--

```kotlin
fun twoForOne(): String {
    
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

Nenhum nome fornecido

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

Passar "James" como nome

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

Passar "Martha" como nome

```kotlin
    tryCatch(twoForOne(name = "Martha") == "One for Martha, one for me.")
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
fun twoForOne(name: String? = null): String {
    name?.let {
        return "One for $it, one for me."
    }
    return "One for you, one for me."
}
```


