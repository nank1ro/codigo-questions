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
func getFinalOpenedDoors(_ numDoors: Int) -> Array<Int> {
    
}
```

# --asserts--

Для 100 дверей вернуть правильный список открытых дверей

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    tryCatch(getFinalOpenedDoors(100) == solution)
}
```

Для 10 дверей вернуть правильный список открытых дверей

```swift
do {
    let solution = [1, 4, 9]
    tryCatch(getFinalOpenedDoors(10) == solution)
}
```

Для 950 дверей вернуть правильный список открытых дверей

```swift
do {
    let solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
    tryCatch(getFinalOpenedDoors(950) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
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
