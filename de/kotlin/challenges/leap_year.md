---
language: kotlin
exerciseType: 1
difficulty: 3
title: Schaltjahr
---

# --description--

In einem Kalenderjahr gibt es genau 365,25 Tage. Aber schließlich wird dies zu Verwirrung führen, da Menschen normalerweise in ganzen Einheiten zählen und nicht mit Dezimalstellen. Um dies zu vermeiden, wurde beschlossen, alle 0,25 Tage alle vier Jahre aufzuaddieren und diesem Jahr 366 Tage zu geben (einschließlich dem 29. Februar als Schalttag) und es ein __Schaltjahr__ zu nennen. Die anderen drei Jahre des vierjährigen Zyklus würden nur 365 Tage haben und __wären keine Schaltjahre__.

# --instructions--

In dieser Herausforderung werden wir es auf eine neue Stufe bringen, in der Sie bestimmen müssen, ob es ein Schaltjahr ist oder nicht, ohne die `Date`-Klasse, `switch`-Anweisungen, __if-Blöcke__, __if-else-Blöcke__ oder __ternäre Operation__ (`x ? a : b`) oder die logischen Operatoren __AND__ (`&&`) und __OR__ (`||`) zu verwenden, mit Ausnahme des __NOT__-Operators (`!`).

Geben Sie `true` zurück, wenn es ein Schaltjahr ist, `false` andernfalls.

Beispiel für einen Funktionsaufruf:
```kotlin
println(leapYear(2000))
// gibt true aus
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

Die Verwendung von `Date`, `switch`, `if`, `else`, `&&`, `||` oder `?` ist nicht zulässig.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Das Jahr `2016` ist ein Schaltjahr.

```kotlin
    tryCatch(leapYear(2016) == true)
```

Das Jahr `1996` ist ein Schaltjahr.

```kotlin
    tryCatch(leapYear(1996) == true)
```

Das Jahr `1600` ist ein Schaltjahr.

```kotlin
    tryCatch(leapYear(1600) == true)
```

Das Jahr `2020` ist ein Schaltjahr.

```kotlin
    tryCatch(leapYear(2020) == true)
```

Das Jahr `2000` ist ein Schaltjahr.

```kotlin
    tryCatch(leapYear(2000) == true)
```

Das Jahr `2008` ist ein Schaltjahr.

```kotlin
    tryCatch(leapYear(2008) == true)
```

Das Jahr `1521` ist kein Schaltjahr.

```kotlin
    tryCatch(leapYear(1521) == false)
```

Das Jahr `1800` ist kein Schaltjahr.

```kotlin
    tryCatch(leapYear(1800) == false)
```

Das Jahr `2007` ist kein Schaltjahr.

```kotlin
    tryCatch(leapYear(2007) == false)
```

Das Jahr `2002` ist kein Schaltjahr.

```kotlin
    tryCatch(leapYear(2002) == false)
```

Das Jahr `1979` ist kein Schaltjahr.

```kotlin
    tryCatch(leapYear(1979) == false)
```

Das Jahr `2006` ist kein Schaltjahr.

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
