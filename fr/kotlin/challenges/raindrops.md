---
language: kotlin
exerciseType: 1
difficulty: 1
title: Gouttes de pluie
---

# --description--

Votre tâche est de convertir un nombre en une chaîne qui contient des sons de gouttes de pluie correspondant à certains facteurs potentiels.
Un facteur est un nombre qui se divise uniformément dans un autre nombre, sans reste.
La façon la plus simple de tester si un nombre est un facteur d'un autre est d'utiliser l'opération modulo.
Les règles des gouttes de pluie sont que si un nombre donné :

- a 3 comme facteur, ajoutez 'Pling' au résultat.
- a 5 comme facteur, ajoutez 'Plang' au résultat.
- a 7 comme facteur, ajoutez 'Plong' au résultat.
- n'a aucun de 3, 5 ou 7 comme facteur, le résultat doit être les chiffres du nombre.

# --instructions--

Écrivez une fonction qui retourne la bonne chaîne, exemples :

- 28 a 7 comme facteur, mais pas 3 ou 5, donc le résultat serait `"Plong"`.
- 30 a à la fois 3 et 5 comme facteurs, mais pas 7, donc le résultat serait `"PlingPlang"`.
- 34 n'est pas divisible par 3, 5 ou 7, donc le résultat serait `"34"`.

Exemple d'appel de fonction :
```kotlin
println(raindrops(28))
// affiche "Plong"
```

# --seed--

```kotlin
fun raindrops(): String {
    
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

Le son pour 1 est "1"

```kotlin
    tryCatch(raindrops(1) == "1")
```

Le son pour 3 est "Pling"

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

Le son pour 5 est "Plang"

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

Le son pour 7 est "Plong"

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

Le son pour 6 est "Pling"

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

Le son pour 8 est "8"

```kotlin
    tryCatch(raindrops(8) == "8")
```

Le son pour 9 est "Pling"

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

Le son pour 10 est "Plang"

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

Le son pour 14 est "Plong"

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

Le son pour 15 est "PlingPlang"

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

Le son pour 21 est "PlingPlong"

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

Le son pour 25 est "Plang"

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

Le son pour 27 est "Pling"

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

Le son pour 35 est "PlangPlong"

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

Le son pour 49 est "Plong"

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

Le son pour 52 est "52"

```kotlin
    tryCatch(raindrops(52) == "52")
```

Le son pour 105 est "PlingPlangPlong"

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

Le son pour 3125 est "Plang"

```kotlin
    tryCatch(raindrops(3125) == "Plang")
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
fun raindrops(num: Int): String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty()) {
        result = num.toString()     
    }
    return result
}
```
