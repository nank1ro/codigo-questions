---
language: kotlin
exerciseType: 1
difficulty: 3
title: Високосный год
---

# --description--

В календарном году ровно 365,25 дней. Но со временем это приведёт к путанице, потому что люди обычно считают с точностью до 1, а не с десятичными знаками. Поэтому, чтобы избежать этого, было решено складывать все 0,25 дня каждые четыре года и давать этому году 366 дней (включая 29 февраля как дополнительный день) и называть его __високосным годом__. Остальные три года в четырёхлетнем цикле содержат только 365 дней и __не являются високосными__.

# --instructions--

В этом задании мы перейдём на новый уровень, где вам нужно определить, является ли год високосным или нет, без использования класса `Date`, операторов `switch`, блоков __if__, блоков __if-else__ или __тернарного оператора__ (`x ? a : b`), а также логических операторов __И__ (`&&`) и __ИЛИ__ (`||`), за исключением оператора __НЕ__ (`!`).

Верните `true`, если год високосный, `false` в противном случае.

Пример вызова функции:
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

Использование `Date`, `switch`, `if`, `else`, `&&`, `||` или `?` не допускается.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Год `2016` является високосным.

```kotlin
    tryCatch(leapYear(2016) == true)
```

Год `1996` является високосным.

```kotlin
    tryCatch(leapYear(1996) == true)
```

Год `1600` является високосным.

```kotlin
    tryCatch(leapYear(1600) == true)
```

Год `2020` является високосным.

```kotlin
    tryCatch(leapYear(2020) == true)
```

Год `2000` является високосным.

```kotlin
    tryCatch(leapYear(2000) == true)
```

Год `2008` является високосным.

```kotlin
    tryCatch(leapYear(2008) == true)
```

Год `1521` не является високосным.

```kotlin
    tryCatch(leapYear(1521) == false)
```

Год `1800` не является високосным.

```kotlin
    tryCatch(leapYear(1800) == false)
```

Год `2007` не является високосным.

```kotlin
    tryCatch(leapYear(2007) == false)
```

Год `2002` не является високосным.

```kotlin
    tryCatch(leapYear(2002) == false)
```

Год `1979` не является високосным.

```kotlin
    tryCatch(leapYear(1979) == false)
```

Год `2006` не является високосным.

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
