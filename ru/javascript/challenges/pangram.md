---
language: javascript
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

Панграмма — это предложение, в котором каждая буква английского алфавита используется хотя бы один раз. Самый известный пример — "the quick brown fox jumps over the lazy dog", в котором все 26 букв умещаются в девять коротких слов.

Проверка не учитывает регистр, поэтому `A` и `a` считаются одной и той же буквой. Цифры, знаки препинания и пробелы игнорируются: они не являются буквами, но и не являются причиной отклонить предложение.

# --instructions--

Напишите функцию `isPangram`, которая принимает предложение и возвращает `true`, если предложение является панграммой, и `false` в противном случае.

Примеры:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- Пустое предложение не является панграммой.
- Считаются только 26 букв от `a` до `z`.

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
function isPangram(sentence) {
  
}
```

# --asserts--

Пустое предложение не является панграммой

```javascript
tryCatch(isPangram("") === false);
```

Классическое предложение "the quick brown fox jumps over the lazy dog" является панграммой

```javascript
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") === true);
```

Предложение, в котором отсутствует буква `x`, не является панграммой

```javascript
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") === false);
```

Предложение "the five boxing wizards jump quickly" является панграммой

```javascript
tryCatch(isPangram("the five boxing wizards jump quickly") === true);
```

Подчёркивания игнорируются, поэтому предложение остаётся панграммой

```javascript
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") === true);
```

Цифры игнорируются, поэтому предложение остаётся панграммой

```javascript
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") === true);
```

Цифры не заменяют буквы `e`, `i` и `t`

```javascript
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") === false);
```

Предложение в верхнем регистре тоже является панграммой

```javascript
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") === true);
```

Смешения регистров одной и той же половины алфавита недостаточно

```javascript
tryCatch(isPangram("abcdefghijklm ABCDEFGHIJKLM") === false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isPangram(sentence) {
  const letters = new Set();

  for (const char of sentence.toLowerCase()) {
    if (char >= "a" && char <= "z") {
      letters.add(char);
    }
  }

  return letters.size === 26;
}
```
