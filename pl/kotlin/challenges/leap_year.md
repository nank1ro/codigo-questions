---
language: kotlin
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

W roku kalendarzowym jest dokładnie 365,25 dnia. Jednak z czasem prowadziłoby to do zamieszania, ponieważ ludzie liczą zazwyczaj przez dokładną podzielność przez 1, a nie z ułamkami dziesiętnymi. Aby tego uniknąć, postanowiono zbierać wszystkie 0,25 dnia w każdym cyklu czteroletnim i dawać danemu rokowi 366 dni (w tym 29 lutego jako dzień przestępny), nazywając go __rokiem przestępnym__. Pozostałe trzy lata w cyklu czteroletnim mają tylko 365 dni i __nie są latami przestępnymi__.

# --instructions--

W tym wyzwaniu wchodzimy na wyższy poziom — masz określić, czy dany rok jest rokiem przestępnym, bez używania klasy `Date`, instrukcji `switch`, __bloków if__, __bloków if-else__, __operacji trójargumentowej__ (`x ? a : b`) ani operatorów logicznych __AND__ (`&&`) i __OR__ (`||`), z wyjątkiem operatora __NOT__ (`!`).

Zwróć `true`, jeśli jest to rok przestępny, w przeciwnym razie `false`.

Przykład wywołania funkcji:
```kotlin
println(leapYear(2000))
// prints true
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

Używanie `Date`, `switch`, `if`, `else`, `&&`, `||` lub `?` jest niedozwolone.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Rok `2016` jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(2016) == true)
```

Rok `1996` jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(1996) == true)
```

Rok `1600` jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(1600) == true)
```

Rok `2020` jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(2020) == true)
```

Rok `2000` jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(2000) == true)
```

Rok `2008` jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(2008) == true)
```

Rok `1521` nie jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(1521) == false)
```

Rok `1800` nie jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(1800) == false)
```

Rok `2007` nie jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(2007) == false)
```

Rok `2002` nie jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(2002) == false)
```

Rok `1979` nie jest rokiem przestępnym.

```kotlin
    tryCatch(leapYear(1979) == false)
```

Rok `2006` nie jest rokiem przestępnym.

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
