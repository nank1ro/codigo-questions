---
language: kotlin
exerciseType: 1
difficulty: 3
title: Année bissextile
---

# --description--

Dans une année civile, il y a exactement 365,25 jours. Mais, finalement, cela causera de la confusion car les humains comptent normalement par divisibilité exacte par 1 et non par des décimales. Donc, pour éviter cela, il a été décidé d'ajouter tous les 0,25 jours tous les quatre ans et de donner à cette année 366 jours (y compris le 29 février comme jour intercalaire) et de l'appeler une __année bissextile__. Les trois autres années du cycle de quatre ans ne contiendraient que 365 jours et __ne seraient pas des années bissextiles__.

# --instructions--

Dans ce défi, nous allons le porter à un nouveau niveau, où vous devez déterminer si c'est une année bissextile ou non sans l'utilisation de la classe `Date`, des instructions `switch`, __des blocs if__, __des blocs if-else__ ou __de l'opération ternaire__ (`x ? a : b`) ni les opérateurs logiques __ET__ (`&&`) et __OU__ (`||`) à l'exception de l'opérateur __NON__ (`!`).

Retournez `true` si c'est une année bissextile, `false` sinon.

Exemple d'appel de fonction :
```kotlin
println(leapYear(2000))
// affiche true
```

# --seed--

```kotlin
fun leapYear(year: Int): Boolean {
    
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

L'utilisation de `Date`, `switch`, `if`, `else`, `&&`, `||` ou `?` n'est pas autorisée.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

L'année `2016` est une année bissextile.

```kotlin
    tryCatch(leapYear(2016) == true)
```

The year `1996` est une année bissextile.

```kotlin
    tryCatch(leapYear(1996) == true)
```

The year `1600` est une année bissextile.

```kotlin
    tryCatch(leapYear(1600) == true)
```

The year `2020` est une année bissextile.

```kotlin
    tryCatch(leapYear(2020) == true)
```

The year `2000` est une année bissextile.

```kotlin
    tryCatch(leapYear(2000) == true)
```

The year `2008` est une année bissextile.

```kotlin
    tryCatch(leapYear(2008) == true)
```

The year `1521` n'est pas une année bissextile.

```kotlin
    tryCatch(leapYear(1521) == false)
```

The year `1800` n'est pas une année bissextile.

```kotlin
    tryCatch(leapYear(1800) == false)
```

The year `2007` n'est pas une année bissextile.

```kotlin
    tryCatch(leapYear(2007) == false)
```

The year `2002` n'est pas une année bissextile.

```kotlin
    tryCatch(leapYear(2002) == false)
```

The year `1979` n'est pas une année bissextile.

```kotlin
    tryCatch(leapYear(1979) == false)
```

The year `2006` n'est pas une année bissextile.

```kotlin
    tryCatch(leapYear(2006) == false)
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
fun leapYear(year: Int): Boolean {
  var tempYear = year
  while (tempYear % 100 == 0) {
    tempYear = tempYear / 100
  }
  return tempYear % 4 == 0
}
```
