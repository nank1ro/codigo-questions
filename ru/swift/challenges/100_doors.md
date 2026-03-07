---
language: swift
exerciseType: 1
difficulty: 1
title: 100 дверей
---

# --description--

В ряду находятся 100 дверей, все они изначально закрыты.
Вы совершаете 100 проходов мимо дверей.
В первый раз вы посещаете каждую дверь и «переключаете» её (если дверь закрыта — открываете; если открыта — закрываете).
Во второй раз вы посещаете только каждую 2-ю дверь (т.е. дверь №2, №4, №6, ...) и переключаете её.
В третий раз — каждую 3-ю дверь (т.е. дверь №3, №6, №9, ...) и так далее, пока не посетите только 100-ю дверь.

# --instructions--

Реализуйте функцию для определения состояния дверей после последнего прохода.
Верните результат в виде массива, содержащего только номера открытых дверей.
> Метод должен работать с переменным количеством дверей.

# --seed--

```swift
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --before-asserts--

```swift
import Foundation
import XCTest

class CodigoTests: XCTestCase {
```

# --asserts--

Для 100 дверей вернуть правильный список открытых дверей

```swift
    func test1() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        XCTAssertEqual(getFinalOpenedDoors(100), solution, "--err-t1--")
    }
```

Для 10 дверей вернуть правильный список открытых дверей

```swift
    func test2() {
        let solution = [1, 4, 9]
        XCTAssertEqual(getFinalOpenedDoors(16), solution, "--err-t2--")
    }
```

Для 950 дверей вернуть правильный список открытых дверей

```swift
    func test3() {
        let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        XCTAssertEqual(getFinalOpenedDoors(950), solution, "--err-t3--")
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
        ]
    }
}

XCTMain([testCase(CodigoTests.allTests)])
```

# --solutions--

```swift
func square(_ num: Int) -> Int {
    return Int(pow(Double(num), Double(2)))
}

func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    var openDoors: [Int] = []
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.append(square(i))
        i += 1
    }
    return openDoors
}
```
