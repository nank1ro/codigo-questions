---
language: kotlin
exerciseType: 1
difficulty: 1
title: Due per uno
---

# --description--

Dato un nome, restituire una stringa con il messaggio:
`Uno per X, uno per me.`
Dove `X` e' il nome dato.
Tuttavia, se il nome manca, restituire la stringa:
`Uno per te, uno per me.`

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

**input**: `Walter`
**output**: `Uno per Walter, uno per me.`

**input**:
**output**: `Uno per te, uno per me.`

**input**: `Davide`
**output**: `Uno per Davide, uno per me.`

# --seed--

```kotlin
fun duePerUno(): String {
    
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

Dividi con qualcuno

```kotlin
    tryCatch(duePerUno() == "Uno per te, uno per me.")
```

Dividi con "Daniele"

```kotlin
    tryCatch(duePerUno(nome = "Daniele") == "Uno per Daniele, uno per me.")
```

Dividi con "Marta"

```kotlin
    tryCatch(duePerUno(nome = "Marta") == "Uno per Marta, uno per me.")
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
fun duePerUno(nome: String? = null): String {
    nome?.let {
    	return "Uno per $it, uno per me."
	}
    return "Uno per te, uno per me."
}
```


