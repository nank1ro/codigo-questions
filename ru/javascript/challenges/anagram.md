---
language: javascript
exerciseType: 1
difficulty: 2
title: Анаграмма
---

# --description--

Два слова являются анаграммами, когда одно из них является перестановкой другого: они используют ровно одни и те же буквы, и каждая буква встречается одно и то же число раз, просто в другом порядке. `listen` и `silent` — анаграммы, как и `stone` и `tones`.

Слово никогда не является анаграммой самого себя. Если два слова полностью совпадают, ничего не переставлялось, поэтому ответ — `false`. Оба слова заданы в нижнем регистре и содержат только буквы от `a` до `z`.

# --instructions--

Напишите функцию `isAnagram`, которая принимает два слова, `first` и `second`, и возвращает `true`, если они являются анаграммами друг друга, и `false` в противном случае.

Примеры:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Два одинаковых слова не являются анаграммами.
- Слова разной длины никогда не являются анаграммами.
- Каждая буква должна встречаться в обоих словах одинаковое число раз.

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
function isAnagram(first, second) {
  
}
```

# --asserts--

Слова "listen" и "silent" являются анаграммами

```javascript
tryCatch(isAnagram("listen", "silent") === true);
```

Слова "stone" и "tones" являются анаграммами

```javascript
tryCatch(isAnagram("stone", "tones") === true);
```

Слово не является анаграммой самого себя

```javascript
tryCatch(isAnagram("stone", "stone") === false);
```

Слова разной длины не являются анаграммами

```javascript
tryCatch(isAnagram("abc", "abcd") === false);
```

Одни и те же буквы в разном количестве не являются анаграммой

```javascript
tryCatch(isAnagram("aab", "abb") === false);
```

Слова "anagram" и "nagaram" являются анаграммами

```javascript
tryCatch(isAnagram("anagram", "nagaram") === true);
```

Два слова одинаковой длины с разными буквами не являются анаграммами

```javascript
tryCatch(isAnagram("rat", "car") === false);
```

Два пустых слова идентичны, поэтому они не являются анаграммами

```javascript
tryCatch(isAnagram("", "") === false);
```

Две разные одиночные буквы не являются анаграммами

```javascript
tryCatch(isAnagram("a", "b") === false);
```

Слова "evil" и "vile" являются анаграммами

```javascript
tryCatch(isAnagram("evil", "vile") === true);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isAnagram(first, second) {
  if (first === second) {
    return false;
  }

  const sortLetters = (word) => word.split("").sort().join("");

  return sortLetters(first) === sortLetters(second);
}
```
