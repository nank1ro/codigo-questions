---
language: swift
exerciseType: 1
difficulty: 2
title: Сортировка пузырьком
---

# --description--

Сортировка пузырьком — один из самых простых алгоритмов сортировки. Он проходит по списку и сравнивает каждую пару соседних элементов, меняя их местами всякий раз, когда они стоят в неправильном порядке. После каждого полного прохода наибольшее из оставшихся значений «всплывает» на своё окончательное место, а список считается отсортированным, как только проход завершается без единого обмена.

# --instructions--

Напишите функцию с именем `bubbleSort`, которая принимает массив целых чисел и возвращает **новый** массив с теми же значениями, отсортированными по возрастанию. Переданный массив изменять нельзя.

Вы должны сами реализовать алгоритм сортировки пузырьком, сравнивая и меняя местами соседние элементы. Не используйте функцию сортировки из стандартной библиотеки.

Ваша функция также должна работать с пустым массивом, массивом из одного элемента, уже отсортированным массивом, повторяющимися значениями и отрицательными числами.

Пример вызова функции:
```swift
print(bubbleSort([3, 1, 2]))
// выводит [1, 2, 3]
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
func bubbleSort(_ arr: [Int]) -> [Int] {
    
}
```

# --asserts--

Пустой массив должен вернуть пустой массив

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

Массив из одного элемента должен остаться прежним

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

Уже отсортированный массив должен сохранить тот же порядок

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

Массив, отсортированный в обратном порядке, должен быть упорядочен по возрастанию

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

Все повторяющиеся значения должны сохраниться

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

Отрицательные числа должны быть отсортированы перед положительными

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

Более длинный смешанный массив должен быть отсортирован по возрастанию

```swift
do {
    let solution: [Int] = [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]
    tryCatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func bubbleSort(_ arr: [Int]) -> [Int] {
    var result = arr
    var end = result.count
    var swapped = true
    while swapped && end > 1 {
        swapped = false
        for i in 1..<end {
            if result[i - 1] > result[i] {
                let temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end -= 1
    }
    return result
}
```
