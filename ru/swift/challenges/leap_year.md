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

# --seed--

```swift
func leapYear(_ year: Int) -> Bool {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
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
    func test1() {
        XCTAssertEqual(leapYear(2016), true, "--err-t1--")
    }
```

Год `1996` является високосным.

```swift
    func test2() {
        XCTAssertEqual(leapYear(1996), true, "--err-t2--")
    }
```

Год `1600` является високосным.

```swift
    func test3() {
        XCTAssertEqual(leapYear(1600), true, "--err-t3--")
    }
```

Год `2020` является високосным.

```swift
    func test4() {
        XCTAssertEqual(leapYear(2020), true, "--err-t4--")
    }
```

Год `2000` является високосным.

```swift
    func test5() {
        XCTAssertEqual(leapYear(2000), true, "--err-t5--")
    }
```

Год `2008` является високосным.

```swift
    func test6() {
        XCTAssertEqual(leapYear(2008), true, "--err-t6--")
    }
```

Год `1521` не является високосным.

```swift
    func test7() {
        XCTAssertEqual(leapYear(1521), false, "--err-t7--")
    }
```

Год `1800` не является високосным.

```swift
    func test8() {
        XCTAssertEqual(leapYear(1800), false, "--err-t8--")
    }
```

Год `2007` не является високосным.

```swift
    func test9() {
        XCTAssertEqual(leapYear(2007), false, "--err-t9--")
    }
```

Год `2002` не является високосным.

```swift
    func test10() {
        XCTAssertEqual(leapYear(2002), false, "--err-t10--")
    }
```

Год `1979` не является високосным.

```swift
    func test11() {
        XCTAssertEqual(leapYear(1979), false, "--err-t11--")
    }
```

Год `2006` не является високосным.

```swift
    func test12() {
        XCTAssertEqual(leapYear(2006), false, "--err-t12--")
    }
```

# --after-asserts--

```swift
}

extension CodigoTests {
    static var allTests : [(String, (CodigoTests) -> () throws -> Void)] {
        return [
            ("test1", test1),
            ("test2", test2),
            ("test3", test3),
            ("test4", test4),
            ("test5", test5),
            ("test6", test6),
            ("test7", test7),
            ("test8", test8),
            ("test9", test9),
            ("test10", test10),
            ("test11", test11),
            ("test12", test12), 
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
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
