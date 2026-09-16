---
language: javascript
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
function hammingDistance(left, right) {
  
}
```

# --asserts--

Две пустые цепочки не различаются нигде

```javascript
tryCatch(hammingDistance("", "") === 0);
```

Две одинаковые цепочки из одного нуклеотида не имеют различий

```javascript
tryCatch(hammingDistance("A", "A") === 0);
```

Две разные цепочки из одного нуклеотида различаются в одной позиции

```javascript
tryCatch(hammingDistance("A", "G") === 1);
```

Две короткие цепочки, различающиеся в каждой позиции

```javascript
tryCatch(hammingDistance("AG", "CT") === 2);
```

Две короткие цепочки, различающиеся только в первой позиции

```javascript
tryCatch(hammingDistance("AT", "CT") === 1);
```

Один различающийся нуклеотид в середине цепочек

```javascript
tryCatch(hammingDistance("GGACG", "GGTCG") === 1);
```

Одинаковые нуклеотиды в разных позициях всё равно считаются различиями

```javascript
tryCatch(hammingDistance("TAG", "GAT") === 2);
```

Более длинная пара цепочек с четырьмя различиями

```javascript
tryCatch(hammingDistance("GATACA", "GCATAA") === 4);
```

Сдвиг цепочки на одну позицию делает почти каждую позицию различающейся

```javascript
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") === 9);
```

Две цепочки из описания имеют расстояние семь

```javascript
tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") === 7);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function hammingDistance(left, right) {
  let distance = 0;

  for (let i = 0; i < left.length; i++) {
    if (left[i] !== right[i]) {
      distance++;
    }
  }

  return distance;
}
```
