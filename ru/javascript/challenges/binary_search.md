---
language: javascript
exerciseType: 1
difficulty: 2
title: Двоичный поиск
---

# --description--

Двоичный поиск находит значение внутри **отсортированной** коллекции, многократно деля диапазон поиска пополам: посмотрите на элемент в середине, и если это не тот, который вам нужен, продолжайте в левой половине, когда искомое значение меньше, или в правой половине, когда оно больше.

Поскольку каждый шаг отбрасывает половину оставшихся элементов, двоичный поиск приходит к ответу за считанные сравнения даже на очень больших коллекциях, тогда как проверка элементов по одному стоила бы столько шагов, сколько есть элементов.

# --instructions--

Напишите функцию `binarySearch`, которая принимает массив целых чисел, отсортированный по возрастанию, и искомое целое число, и возвращает индекс искомого числа в массиве или `-1`, если числа в массиве нет.

Массив никогда не содержит дубликатов, поэтому индекс всегда уникален. Массив также может быть пустым. Ваша функция должна использовать двоичный поиск, деля диапазон поиска пополам на каждом шаге, а не линейный перебор.

Пример вызова функции:
```javascript
console.log(binarySearch([1, 3, 5, 7], 5));
// выводит 2
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
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function binarySearch(arr, target) {
  
}
```

# --asserts--

Поиск в пустом массиве должен вернуть -1

```javascript
tryCatch(binarySearch([], 7) === -1);
```

Поиск 5 в `[5]` должен вернуть 0

```javascript
tryCatch(binarySearch([5], 5) === 0);
```

Поиск 9 в `[5]` должен вернуть -1

```javascript
tryCatch(binarySearch([5], 9) === -1);
```

Первый элемент -9 массива из 12 элементов должен быть найден по индексу 0

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9) === 0);
```

Последний элемент 78 массива из 12 элементов должен быть найден по индексу 11

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78) === 11);
```

Элемент 15 должен быть найден по индексу 6

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15) === 6);
```

Элемент 22 должен быть найден по индексу 7

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22) === 7);
```

Значение 12, которое находится между 11 и 15, должно вернуть -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12) === -1);
```

Искомое значение меньше всех элементов должно вернуть -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100) === -1);
```

Искомое значение больше всех элементов должно вернуть -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100) === -1);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] === target) {
      return mid;
    }
    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return -1;
}
```
