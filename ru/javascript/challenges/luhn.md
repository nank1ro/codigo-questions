---
language: javascript
exerciseType: 1
difficulty: 2
title: Контрольная сумма Луна
---

# --description--

Алгоритм Луна — это простая контрольная сумма, используемая для проверки идентификационных номеров, таких как номера кредитных карт.

Перед проверкой числа удалите из строки все пробелы. Строка является валидной, только если оставшееся длиннее одного символа, а исходная строка не содержит ничего, кроме цифр и пробелов.

Чтобы выполнить проверку, начните с крайней правой цифры и двигайтесь влево, удваивая каждую вторую цифру. Если удвоение даёт число больше 9, вычтите из него 9. Затем сложите все цифры: число является валидным, только если сумма делится на 10.

Например, `"059"` даёт `0`, затем `5` при удвоении превращается в `10`, которое становится `1`, затем `9`. Их сумма равна `10`, что делится на 10, поэтому число является валидным.

# --instructions--

Напишите функцию `isValid`, которая принимает строку и возвращает `true`, если число является валидным, и `false` в противном случае.

- `"4539 3195 0343 6467"` проходит контрольную сумму, поэтому результат — `true`.
- `"8273 1232 7352 0569"` не проходит контрольную сумму, поэтому результат — `false`.
- `"0"` имеет длину всего один символ, поэтому результат — `false`.
- `"055-444-285"` содержит символ, который не является цифрой или пробелом, поэтому результат — `false`.

Пример вызова функции:
```javascript
console.log(isValid("095 245 88"));
// prints true
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
function isValid(value) {
  
}
```

# --asserts--

Одиночная цифра не является валидной.

```javascript
tryCatch(isValid("0") === false);
```

Одиночная цифра с ведущим пробелом не является валидной.

```javascript
tryCatch(isValid(" 0") === false);
```

Число `"059"` является валидным.

```javascript
tryCatch(isValid("059") === true);
```

Число `"59"` является валидным.

```javascript
tryCatch(isValid("59") === true);
```

Число `"055 444 285"` является валидным.

```javascript
tryCatch(isValid("055 444 285") === true);
```

Число `"055 444 286"` не является валидным.

```javascript
tryCatch(isValid("055 444 286") === false);
```

Число `"8273 1232 7352 0569"` не является валидным.

```javascript
tryCatch(isValid("8273 1232 7352 0569") === false);
```

Число `"4539 3195 0343 6467"` является валидным.

```javascript
tryCatch(isValid("4539 3195 0343 6467") === true);
```

Число `"1 2345 6789 1234 5678 9012"` не является валидным.

```javascript
tryCatch(isValid("1 2345 6789 1234 5678 9012") === false);
```

Число `"095 245 88"` является валидным.

```javascript
tryCatch(isValid("095 245 88") === true);
```

Буква делает число невалидным.

```javascript
tryCatch(isValid("055a 444 285") === false);
```

Дефисы делают число невалидным.

```javascript
tryCatch(isValid("055-444-285") === false);
```

Знак препинания делает число невалидным.

```javascript
tryCatch(isValid(":9") === false);
```

Спецсимволы делают число невалидным.

```javascript
tryCatch(isValid("055# 444$ 285") === false);
```

Пустая строка не является валидной.

```javascript
tryCatch(isValid("") === false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isValid(value) {
  var sum = 0
  var count = 0
  for (var i = value.length - 1; i >= 0; i--) {
    var code = value.charCodeAt(i)
    if (code === 32) {
      continue
    }
    if (code < 48 || code > 57) {
      return false
    }
    var digit = code - 48
    if (count % 2 === 1) {
      digit *= 2
      if (digit > 9) {
        digit -= 9
      }
    }
    sum += digit
    count++
  }
  return count > 1 && sum % 10 === 0
}
```
