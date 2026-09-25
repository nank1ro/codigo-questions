---
language: javascript
exerciseType: 1
difficulty: 2
title: Кодирование длин серий
---

# --description--

Кодирование длин серий — один из старейших приёмов сжатия: вместо того чтобы писать один и тот же символ снова и снова, вы записываете, сколько раз он повторяется, а затем сам символ.

Факсимильный аппарат, сканирующий почти пустую страницу, встречает длинные участки одинаковых пикселей, поэтому ряд из двенадцати `W` передаётся по линии как гораздо более короткое `12W`. Когда символ встречается лишь однажды, считать его незачем, поэтому он копируется сам по себе.

# --instructions--

Напишите функцию `encodeRun`, которая принимает строку `text` и возвращает её закодированное представление.

Каждая серия одного и того же символа, повторённого два или более раз, превращается в длину серии, записанную в десятичном виде, за которой следует сам символ. Серия длины один копируется как одиночный символ, без числа перед ним.

Примеры:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Текст содержит только заглавные буквы от `A` до `Z` и пробелы.
- Серия длиннее девяти символов записывается своим полным десятичным количеством, поэтому двенадцать `W` превращаются в `12W`, но никогда в `9W3W`.
- Пробелы — обычные символы: они считаются и кодируются точно так же, как буквы.
- Пустая строка кодируется в пустую строку.

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
function encodeRun(text) {
  
}
```

# --asserts--

Пустая строка кодируется в пустую строку

```javascript
tryCatch(encodeRun("") === "");
```

Одиночный символ копируется без изменений

```javascript
tryCatch(encodeRun("A") === "A");
```

Строка без повторов проходит через кодирование без изменений

```javascript
tryCatch(encodeRun("ABCDE") === "ABCDE");
```

Серия из двух символов превращается в число, за которым следует символ

```javascript
tryCatch(encodeRun("AA") === "2A");
```

Смешанный пример "AABCCCDEEEE" превращается в "2AB3CD4E"

```javascript
tryCatch(encodeRun("AABCCCDEEEE") === "2AB3CD4E");
```

Серия из двенадцати записывается своим полным десятичным количеством, поэтому результат начинается с "12W"

```javascript
tryCatch(encodeRun("WWWWWWWWWWWWBWW") === "12WB2W");
```

Серии пробелов кодируются точно так же, как серии букв

```javascript
tryCatch(encodeRun("  HI  ") === "2 HI2 ");
```

Серия из десяти записывается как "10A", но никогда как две более короткие серии

```javascript
tryCatch(encodeRun("AAAAAAAAAA") === "10A");
```

Чередующиеся одиночные символы копируются без изменений

```javascript
tryCatch(encodeRun("ABABAB") === "ABABAB");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function encodeRun(text) {
  let result = "";
  let i = 0;

  while (i < text.length) {
    let run = 1;
    while (i + run < text.length && text[i + run] === text[i]) {
      run++;
    }
    if (run > 1) {
      result += run;
    }
    result += text[i];
    i += run;
  }

  return result;
}
```
