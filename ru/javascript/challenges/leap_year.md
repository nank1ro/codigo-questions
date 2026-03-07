---
language: javascript
exerciseType: 1
difficulty: 3
title: Високосный год
---

# --description--

В календарном году ровно 365,25 дней. Но в конечном счёте это приведёт к путанице, поскольку люди обычно считают целыми числами, а не десятичными дробями. Поэтому, чтобы избежать этого, было решено суммировать все 0,25 дня каждые четыре года и давать этому году 366 дней (включая 29 февраля как дополнительный день), называя его __високосным годом__. Остальные три года четырёхлетнего цикла содержат только 365 дней и __не являются високосными__.

# --instructions--

В этом задании мы выходим на новый уровень: вам нужно определить, является ли год високосным, без использования класса `Date`, операторов `switch`, блоков __if__, блоков __if-else__ или __тернарного оператора__ (`x ? a : b`), а также логических операторов __И__ (`&&`) и __ИЛИ__ (`||`), за исключением оператора __НЕ__ (`!`).

Верните `true`, если год високосный, и `false` в противном случае.

Пример вызова функции:
```javascript
console.log(leapYear(2000));
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
function leapYear(year) {
  
}
```

# --asserts--

Использование `Date`, `switch`, `if`, `else`, `&&`, `||` или `?` не допускается.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Год `2016` является високосным.

```javascript
tryCatch(leapYear(2016) == true);
```

Год `1996` является високосным.

```javascript
tryCatch(leapYear(1996) == true);
```

Год `1600` является високосным.

```javascript
tryCatch(leapYear(1600) == true);
```

Год `2020` является високосным.

```javascript
tryCatch(leapYear(2020) == true);
```

Год `2000` является високосным.

```javascript
tryCatch(leapYear(2000) == true);
```

Год `2008` является високосным.

```javascript
tryCatch(leapYear(2008) == true);
```

Год `1521` не является високосным.

```javascript
tryCatch(leapYear(1521) == false);
```

Год `1800` не является високосным.

```javascript
tryCatch(leapYear(1800) == false);
```

Год `2007` не является високосным.

```javascript
tryCatch(leapYear(2007) == false);
```

Год `2002` не является високосным.

```javascript
tryCatch(leapYear(2002) == false);
```

Год `1979` не является високосным.

```javascript
tryCatch(leapYear(1979) == false);
```

Год `2006` не является високосным.

```javascript
tryCatch(leapYear(2006) == false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function leapYear(year) {
  return (year % 4 === 0) ^ ((year % 100 === 0) & (year % 400 !== 0));
}
```

```javascript
function leapYear(year){
   while(year % 100 === 0) {
     year = year / 100;
   }
  return year % 4 === 0; 
}
```
