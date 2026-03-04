---
language: kotlin
exerciseType: 1
difficulty: 1
title: Dos por uno
---

# --description--

Dado un nombre, devuelve una cadena con el mensaje:
`One for X, one for me.`
Donde `X` es el nombre dado.
Sin embargo, si el nombre falta, devuelve la cadena:
`One for you, one for me.`

# --instructions--

Escribe una función que devuelva la cadena correcta, ejemplos:

**entrada**: `Walter`
**salida**: `One for Walter, one for me.`

**entrada**: `James`
**salida**: `One for James, one for me.`

**entrada**: `Martha`
**salida**: `One for Martha, one for me.`

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

Sin nombre dado

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

Pasar "James" como nombre

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

Pasar "Martha" como nombre

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


