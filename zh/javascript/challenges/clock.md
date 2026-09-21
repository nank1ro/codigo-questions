---
language: javascript
exerciseType: 1
difficulty: 2
title: 时钟
---

# --description--

24 小时制时钟以 `HH:MM` 的形式显示一天中的时间，从午夜刚过的 `00:00` 开始，到下一个午夜前一分钟的 `23:59` 结束。两部分始终写成两位数字，所以上午十一点零九分显示为 `11:09`。

一整天共有 1440 分钟。时钟一旦走过 `23:59` 就会回到 `00:00` 重新开始一天，而向后拨过 `00:00` 则会落在 `23:59`。

# --instructions--

编写一个函数 `clockTime`，它接收两个整数 `hours` 和 `minutes`，并返回 24 小时制时钟的读数，即字符串 `"HH:MM"`，两部分都补足成两位数字。

示例：
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- 两个数都可能是负数，也可能大于真实时钟所允许的范围。
- 先按 `hours * 60 + minutes` 算出总分钟数，再把这个总数折回 `0` 到 `1439` 的范围内，让时钟向两个方向都能回绕。
- `clockTime(24, 0)` 正好是一天，所以读数是 `"00:00"`。

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
function clockTime(hours, minutes) {
  
}
```

# --asserts--

早上八点显示为 `08:00`

```javascript
tryCatch(clockTime(8, 0) === "08:00");
```

个位数字会补足成两位，所以十一点零九分显示为 `11:09`

```javascript
tryCatch(clockTime(11, 9) === "11:09");
```

正好一整天的小时会回绕到 `00:00`

```javascript
tryCatch(clockTime(24, 0) === "00:00");
```

超过 60 的分钟数会进位到小时

```javascript
tryCatch(clockTime(25, 160) === "03:40");
```

负的小时数会把时钟向后拨过午夜

```javascript
tryCatch(clockTime(-1, 15) === "23:15");
```

负的分钟数同样会把时钟向后拨

```javascript
tryCatch(clockTime(0, -90) === "22:30");
```

向后超过一整天也会继续回绕

```javascript
tryCatch(clockTime(-25, 0) === "23:00");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function clockTime(hours, minutes) {
  // % 会保留左操作数的符号，所以先加上一整天再
  // 回绕一次，落回 0..1439。
  const total = (((hours * 60 + minutes) % 1440) + 1440) % 1440;

  const hh = String(Math.floor(total / 60)).padStart(2, "0");
  const mm = String(total % 60).padStart(2, "0");
  return `${hh}:${mm}`;
}
```
