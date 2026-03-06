---
language: javascript
exerciseType: 1
difficulty: 3
title: 闰年
---

# --description--

一个日历年恰好有365.25天。但最终，这会导致混乱，因为人类通常按整数计数而不是用小数点。因此，为了避免这种情况，决定将每四年周期中的所有0.25天累加起来，使该年有366天（包括2月29日作为闰日），称之为__闰年__。四年周期中的其他三年只有365天，__不是闰年__。

# --instructions--

在这个挑战中，我们将提高难度，你需要在不使用 `Date` 类、`switch` 语句、__if代码块__、__if-else代码块__或__三元运算符__（`x ? a : b`）以及逻辑运算符 __AND__（`&&`）和 __OR__（`||`）的情况下判断是否为闰年，但可以使用 __NOT__（`!`）运算符。

如果是闰年返回 `true`，否则返回 `false`。

函数调用示例：
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

不允许使用 `Date`、`switch`、`if`、`else`、`&&`、`||` 或 `?`。

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

年份 `2016` 是闰年。

```javascript
tryCatch(leapYear(2016) == true);
```

年份 `1996` 是闰年。

```javascript
tryCatch(leapYear(1996) == true);
```

年份 `1600` 是闰年。

```javascript
tryCatch(leapYear(1600) == true);
```

年份 `2020` 是闰年。

```javascript
tryCatch(leapYear(2020) == true);
```

年份 `2000` 是闰年。

```javascript
tryCatch(leapYear(2000) == true);
```

年份 `2008` 是闰年。

```javascript
tryCatch(leapYear(2008) == true);
```

年份 `1521` 不是闰年。

```javascript
tryCatch(leapYear(1521) == false);
```

年份 `1800` 不是闰年。

```javascript
tryCatch(leapYear(1800) == false);
```

年份 `2007` 不是闰年。

```javascript
tryCatch(leapYear(2007) == false);
```

年份 `2002` 不是闰年。

```javascript
tryCatch(leapYear(2002) == false);
```

年份 `1979` 不是闰年。

```javascript
tryCatch(leapYear(1979) == false);
```

年份 `2006` 不是闰年。

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
