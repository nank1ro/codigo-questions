---
language: javascript
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
```javascript
console.log(bubbleSort([3, 1, 2]));
// prints [ 1, 2, 3 ]
```

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};

// Returns true if two arrays are equal and in the same order
var arraysMatch = function (arr1, arr2) {
    // Check if the arrays are the same length
    if (arr1.length !== arr2.length) return false;

    // Check if all items exist and are in the same order
    for (var i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }

    // Otherwise, return true
    return true;
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function bubbleSort(arr) {
  
}
```

# --asserts--

Пустой массив должен вернуть пустой массив

```javascript
tryCatch(arraysMatch(bubbleSort([]), []));
```

Массив из одного элемента должен остаться прежним

```javascript
tryCatch(arraysMatch(bubbleSort([42]), [42]));
```

Уже отсортированный массив должен сохранить тот же порядок

```javascript
tryCatch(arraysMatch(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]));
```

Массив, отсортированный в обратном порядке, должен быть упорядочен по возрастанию

```javascript
tryCatch(arraysMatch(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]));
```

Все повторяющиеся значения должны сохраниться

```javascript
tryCatch(arraysMatch(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3]));
```

Отрицательные числа должны быть отсортированы перед положительными

```javascript
tryCatch(arraysMatch(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3]));
```

Более длинный смешанный массив должен быть отсортирован по возрастанию

```javascript
tryCatch(arraysMatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]));
```

Переданный массив изменять нельзя

```javascript
const original = [3, 1, 2];
bubbleSort(original);
tryCatch(arraysMatch(original, [3, 1, 2]));
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function bubbleSort(arr) {
  const result = [...arr];
  let end = result.length;
  let swapped = true;
  while (swapped) {
    swapped = false;
    for (let i = 1; i < end; i++) {
      if (result[i - 1] > result[i]) {
        const temp = result[i - 1];
        result[i - 1] = result[i];
        result[i] = temp;
        swapped = true;
      }
    }
    end--;
  }
  return result;
}
```
