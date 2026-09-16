---
language: swift
exerciseType: 1
difficulty: 1
title: Расстояние Хэмминга
---

# --description--

ДНК записывается в виде цепочки нуклеотидов, каждый из которых обозначается одной буквой: `A`, `C`, `G` или `T`. Когда две цепочки одинаковой длины располагаются рядом друг с другом, в одних позициях стоит один и тот же нуклеотид, а в других — разные.

Количество позиций, в которых две цепочки различаются, называется расстоянием Хэмминга, и биологи используют его, чтобы измерить, насколько далеко две цепочки разошлись друг от друга. Если сопоставить `GAGCCTACTAACGGGAT` с `CATCGTAATGACGGCCT`, различающихся позиций окажется 7, поэтому их расстояние Хэмминга равно 7.

# --instructions--

Напишите функцию `hammingDistance`, которая принимает две цепочки ДНК одинаковой длины и возвращает количество позиций, в которых они различаются.

Примеры:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- У цепочек всегда одинаковая длина, поэтому обрабатывать цепочки разной длины не придётся.
- Две пустые цепочки не различаются нигде, поэтому их расстояние равно 0.

> ПОДСКАЗКА: опустите метки аргументов с помощью `_` (нижнее подчёркивание)

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
func hammingDistance(_ left: String, _ right: String) -> Int {
    
}
```

# --asserts--

Две пустые цепочки не различаются нигде

```swift
tryCatch(hammingDistance("", "") == 0)
```

Две одинаковые цепочки из одного нуклеотида не имеют различий

```swift
tryCatch(hammingDistance("A", "A") == 0)
```

Две разные цепочки из одного нуклеотида различаются в одной позиции

```swift
tryCatch(hammingDistance("A", "G") == 1)
```

Две короткие цепочки, различающиеся в каждой позиции

```swift
tryCatch(hammingDistance("AG", "CT") == 2)
```

Две короткие цепочки, различающиеся только в первой позиции

```swift
tryCatch(hammingDistance("AT", "CT") == 1)
```

Один различающийся нуклеотид в середине цепочек

```swift
tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

Одинаковые нуклеотиды в разных позициях всё равно считаются различиями

```swift
tryCatch(hammingDistance("TAG", "GAT") == 2)
```

Более длинная пара цепочек с четырьмя различиями

```swift
tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

Сдвиг цепочки на одну позицию делает почти каждую позицию различающейся

```swift
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

Две цепочки из описания имеют расстояние семь

```swift
tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func hammingDistance(_ left: String, _ right: String) -> Int {
    var distance = 0

    for (leftNucleotide, rightNucleotide) in zip(left, right) {
        if leftNucleotide != rightNucleotide {
            distance += 1
        }
    }

    return distance
}
```
