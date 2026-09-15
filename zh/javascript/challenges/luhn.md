---
language: javascript
exerciseType: 1
difficulty: 2
title: Luhn 校验和
---

# --description--

Luhn 算法是一种简单的校验和，用于验证身份识别号码，例如信用卡号。

在检查一个号码之前，先去掉字符串中的所有空格。只有当剩下的部分长度超过一个字符，并且原始字符串只包含数字和空格时，该字符串才是有效的。

执行检查时，从最右边的数字开始向左移动，将每隔一位的数字加倍。当加倍后得到大于 9 的数时，将其减去 9。然后把所有数字相加：只有当总和能被 10 整除时，该号码才有效。

例如，`"059"` 得到 `0`，然后 `5` 加倍为 `10`，它变成 `1`，再是 `9`。它们的和是 `10`，能被 10 整除，所以这个号码是有效的。

# --instructions--

编写一个函数 `isValid`，它接收一个字符串，当号码有效时返回 `true`，否则返回 `false`。

- `"4539 3195 0343 6467"` 通过校验和，所以结果是 `true`。
- `"8273 1232 7352 0569"` 未通过校验和，所以结果是 `false`。
- `"0"` 只有一个字符长，所以结果是 `false`。
- `"055-444-285"` 包含既不是数字也不是空格的字符，所以结果是 `false`。

函数调用示例：
```javascript
console.log(isValid("095 245 88"));
// 打印 true
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

单个数字是无效的。

```javascript
tryCatch(isValid("0") === false);
```

前面带一个空格的单个数字是无效的。

```javascript
tryCatch(isValid(" 0") === false);
```

号码 `"059"` 是有效的。

```javascript
tryCatch(isValid("059") === true);
```

号码 `"59"` 是有效的。

```javascript
tryCatch(isValid("59") === true);
```

号码 `"055 444 285"` 是有效的。

```javascript
tryCatch(isValid("055 444 285") === true);
```

号码 `"055 444 286"` 是无效的。

```javascript
tryCatch(isValid("055 444 286") === false);
```

号码 `"8273 1232 7352 0569"` 是无效的。

```javascript
tryCatch(isValid("8273 1232 7352 0569") === false);
```

号码 `"4539 3195 0343 6467"` 是有效的。

```javascript
tryCatch(isValid("4539 3195 0343 6467") === true);
```

号码 `"1 2345 6789 1234 5678 9012"` 是无效的。

```javascript
tryCatch(isValid("1 2345 6789 1234 5678 9012") === false);
```

号码 `"095 245 88"` 是有效的。

```javascript
tryCatch(isValid("095 245 88") === true);
```

字母会使号码无效。

```javascript
tryCatch(isValid("055a 444 285") === false);
```

短横线会使号码无效。

```javascript
tryCatch(isValid("055-444-285") === false);
```

标点符号字符会使号码无效。

```javascript
tryCatch(isValid(":9") === false);
```

符号会使号码无效。

```javascript
tryCatch(isValid("055# 444$ 285") === false);
```

空字符串是无效的。

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
