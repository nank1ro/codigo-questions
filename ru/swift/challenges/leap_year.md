---
language: swift
exerciseType: 1
difficulty: 3
title: Високосный год
---

# --description--

В календарном году ровно 365,25 дней. Но со временем это приводит к путанице, потому что люди обычно считают с точностью до целого числа, а не с десятичными дробями. Поэтому, чтобы избежать этого, было решено суммировать все 0,25 дня за каждый четырёхлетний цикл и дать этому году 366 дней (включая 29 февраля как дополнительный день) и назвать его __високосным годом__. Остальные три года в четырёхлетнем цикле содержат только 365 дней и __не являются високосными__.

# --instructions--

В этом задании мы поднимем планку: вам нужно определить, является ли год високосным, без использования класса `Date`, операторов `switch`, блоков __if__, блоков __if-else__ или __тернарного оператора__ (`x ? a : b`), а также логических операторов __И__ (`&&`) и __ИЛИ__ (`||`), за исключением оператора __НЕ__ (`!`).

Верните `true`, если год високосный, `false` в противном случае.

Пример вызова функции:
```swift
print(leapYear(2000))
// prints true
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func leapYear(_ year: Int) -> Bool {
    
}
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

```swift
tryCatch(leapYear(2016) == true)
```

Год `1996` является високосным.

```swift
tryCatch(leapYear(1996) == true)
```

Год `1600` является високосным.

```swift
tryCatch(leapYear(1600) == true)
```

Год `2020` является високосным.

```swift
tryCatch(leapYear(2020) == true)
```

Год `2000` является високосным.

```swift
tryCatch(leapYear(2000) == true)
```

Год `2008` является високосным.

```swift
tryCatch(leapYear(2008) == true)
```

Год `1521` не является високосным.

```swift
tryCatch(leapYear(1521) == false)
```

Год `1800` не является високосным.

```swift
tryCatch(leapYear(1800) == false)
```

Год `2007` не является високосным.

```swift
tryCatch(leapYear(2007) == false)
```

Год `2002` не является високосным.

```swift
tryCatch(leapYear(2002) == false)
```

Год `1979` не является високосным.

```swift
tryCatch(leapYear(1979) == false)
```

Год `2006` не является високосным.

```swift
tryCatch(leapYear(2006) == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func leapYear(_ year: Int) -> Bool {
    var yr = year
    while yr % 100 == 0 {
        yr = yr / 100
    }
    return yr % 4 == 0
}
```
