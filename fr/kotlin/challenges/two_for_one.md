---
language: kotlin
exerciseType: 1
difficulty: 1
title: Deux pour un
---

# --description--

Étant donné un nom, retournez une chaîne avec le message :
`Un pour X, un pour moi.`
Où `X` est le nom donné.
Cependant, si le nom est manquant, retournez la chaîne :
`Un pour vous, un pour moi.`

# --instructions--

Écrivez une fonction qui retourne la bonne chaîne, exemples :

**input**: `Walter`
**output**: `Un pour Walter, un pour moi.`

**input**: `James`
**output**: `Un pour James, un pour moi.`

**input**: `Martha`
**output**: `Un pour Martha, un pour moi.`

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

Aucun nom donné

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

Passez "James" en tant que nom

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

Passez "Martha" en tant que nom

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


