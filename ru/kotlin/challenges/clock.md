---
language: kotlin
exerciseType: 1
difficulty: 2
title: Часы
---

# --description--

24-часовые часы показывают время суток в формате `HH:MM`: отсчёт начинается с `00:00` сразу после полуночи и заканчивается `23:59` — за минуту до следующей полуночи. Обе части всегда записываются двумя цифрами, поэтому девять минут двенадцатого утра выглядят как `11:09`.

Целые сутки длятся 1440 минут. Как только часы проходят `23:59`, они переключаются на `00:00` и день начинается заново, а при переводе назад мимо `00:00` получается `23:59`.

# --instructions--

Напишите функцию `clockTime`, которая принимает два целых числа, `hours` и `minutes`, и возвращает показания 24-часовых часов в виде строки `"HH:MM"`, причём обе части дополнены до двух цифр.

Примеры:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Каждое из чисел может быть отрицательным или больше, чем допускают настоящие часы.
- Вычислите общее количество минут как `hours * 60 + minutes`, а затем заверните полученную сумму в диапазон от `0` до `1439`, чтобы часы переключались в обоих направлениях.
- `clockTime(24, 0)` — это ровно один день, поэтому получится `"00:00"`.

# --seed--

```kotlin
fun clockTime(hours: Int, minutes: Int): String {
    
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

Восемь часов утра — это `08:00`

```kotlin
    tryCatch(clockTime(8, 0) == "08:00")
```

Одиночные цифры дополняются до двух, поэтому девять минут двенадцатого — это `11:09`

```kotlin
    tryCatch(clockTime(11, 9) == "11:09")
```

Ровно одни полные сутки переключаются на `00:00`

```kotlin
    tryCatch(clockTime(24, 0) == "00:00")
```

Минуты сверх 60 переходят в часы

```kotlin
    tryCatch(clockTime(25, 160) == "03:40")
```

Отрицательный час переводит часы назад мимо полуночи

```kotlin
    tryCatch(clockTime(-1, 15) == "23:15")
```

Отрицательное количество минут тоже переводит часы назад

```kotlin
    tryCatch(clockTime(0, -90) == "22:30")
```

Больше целых суток назад — часы продолжают переключаться

```kotlin
    tryCatch(clockTime(-25, 0) == "23:00")
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
fun clockTime(hours: Int, minutes: Int): String {
    // % сохраняет знак левого операнда, но mod() всегда заворачивает вперёд
    // в диапазон 0..1439.
    val total = (hours * 60 + minutes).mod(1440)

    return "%02d:%02d".format(total / 60, total % 60)
}
```
