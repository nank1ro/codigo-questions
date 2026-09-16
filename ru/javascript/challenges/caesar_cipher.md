---
language: javascript
exerciseType: 1
difficulty: 2
title: Шифр Цезаря
---

# --description--

Юлий Цезарь защищал свои личные письма одним из старейших приёмов криптографии: он заменял каждую букву сообщения буквой, отстоящей от исходной на фиксированное число позиций дальше по алфавиту. При сдвиге 3 `a` становится `d`, `b` становится `e`, а `c` становится `f`.

Алфавит замкнут в круг, поэтому буквы в его конце возвращаются к началу: при сдвиге 3 `x` становится `a`, `y` становится `b`, а `z` становится `c`.

Всё, что не является буквой — например, пробел, запятая, восклицательный знак или цифра, — проходит через шифр без изменений.

# --instructions--

Напишите функцию `caesarCipher`, которая принимает сообщение `text` и целое число `shift`, и возвращает закодированное сообщение.

Примеры:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Сообщение всегда записано строчными буквами, поэтому вам никогда не придётся иметь дело с заглавными буквами.
- Символы, не являющиеся буквами, сохраняют свою позицию и своё значение.
- Сдвиг никогда не бывает отрицательным. Сдвиг `0` оставляет сообщение без изменений, как и сдвиг `26`.

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
function caesarCipher(text, shift) {
  
}
```

# --asserts--

Сдвиг 3 превращает "hello" в "khoor"

```javascript
tryCatch(caesarCipher("hello", 3) === "khoor");
```

Конец алфавита замыкается по кругу, поэтому "xyz" становится "abc"

```javascript
tryCatch(caesarCipher("xyz", 3) === "abc");
```

Сдвиг 0 оставляет сообщение без изменений

```javascript
tryCatch(caesarCipher("abc", 0) === "abc");
```

Сдвиг 26 — это полный оборот алфавита, поэтому сообщение не меняется

```javascript
tryCatch(caesarCipher("abc", 26) === "abc");
```

Знаки препинания и пробелы проходят через шифр без изменений

```javascript
tryCatch(caesarCipher("codigo, rocks!", 5) === "htinlt, wthpx!");
```

Пустое сообщение остаётся пустым

```javascript
tryCatch(caesarCipher("", 4) === "");
```

Пробелы между отдельными буквами сохраняются

```javascript
tryCatch(caesarCipher("a b c", 1) === "b c d");
```

Цифры не сдвигаются, даже при сдвиге 25

```javascript
tryCatch(caesarCipher("abc 123!", 25) === "zab 123!");
```

Сдвиг 13 кодирует целое предложение

```javascript
tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) === "gur dhvpx oebja sbk whzcf bire gur ynml qbt");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function caesarCipher(text, shift) {
  const a = "a".charCodeAt(0);
  let result = "";

  for (const char of text) {
    const code = char.charCodeAt(0);
    if (char >= "a" && char <= "z") {
      result += String.fromCharCode(a + ((code - a + shift) % 26));
    } else {
      result += char;
    }
  }

  return result;
}
```
