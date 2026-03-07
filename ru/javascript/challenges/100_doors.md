---
language: javascript
exerciseType: 1
difficulty: 1
title: 100 дверей
---

# --description--

В ряду расположены 100 дверей, все изначально закрыты.
Вы совершаете 100 проходов мимо дверей.
В первый раз вы посещаете каждую дверь и переключаете её (если дверь закрыта — открываете; если открыта — закрываете).
Во второй раз вы посещаете только каждую 2-ю дверь (т.е. дверь №2, №4, №6, ...) и переключаете её.
В третий раз вы посещаете каждую 3-ю дверь (т.е. дверь №3, №6, №9, ...) и так далее, пока не посетите только 100-ю дверь.

# --instructions--

Реализуйте функцию для определения состояния дверей после последнего прохода.
Верните конечный результат в виде массива, включая в массив только номер двери, если она открыта.
> Метод должен работать с переменным количеством дверей.

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
function getFinalOpenedDoors(numDoors) {
    
}
```

# --asserts--

Для 100 дверей вернуть правильный список открытых дверей

```javascript
const sol1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
tryCatch(arraysMatch(getFinalOpenedDoors(100), sol1));
```

Для 10 дверей вернуть правильный список открытых дверей

```javascript
const sol2 = [1, 4, 9];
tryCatch(arraysMatch(getFinalOpenedDoors(10), sol2));
```

Для 950 дверей вернуть правильный список открытых дверей

```javascript
const sol3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900];
tryCatch(arraysMatch(getFinalOpenedDoors(950), sol3));
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function getFinalOpenedDoors(numDoors) {
    const openDoors = [];
    var i = 1;
    while (Math.pow(i, 2) <= numDoors) {
        openDoors.push(Math.pow(i, 2));
        i++;
    }
    return openDoors;
}
```
