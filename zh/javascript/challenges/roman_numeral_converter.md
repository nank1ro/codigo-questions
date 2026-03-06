---
language: javascript
exerciseType: 1
difficulty: 3
title: 罗马数字转换器
---

# --description--

创建一个函数，接受一个正整数作为参数，返回该整数的罗马数字表示的字符串。现代罗马数字通过分别表示每个数位来书写，从最左边的数位开始，跳过值为零的数位。

# --instructions--

示例：
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- 所有罗马数字应以大写形式返回。
- 此表示法可以表示的最大数字是3,999。

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
function convertToRoman(n) {
  
}
```

# --asserts--

数字 `2` 必须等于 `II`

```javascript
tryCatch(convertToRoman(2) === "II");
```

数字 `12` 必须等于 `XII`

```javascript
tryCatch(convertToRoman(12) === "XII");
```

数字 `16` 必须等于 `XVI`

```javascript
tryCatch(convertToRoman(16) === "XVI");
```

数字 `44` 必须等于 `XLIV`

```javascript
tryCatch(convertToRoman(44) === "XLIV");
```

数字 `68` 必须等于 `LXVIII`

```javascript
tryCatch(convertToRoman(68) === "LXVIII");
```

数字 `400` 必须等于 `CD`

```javascript
tryCatch(convertToRoman(400) === "CD");
```

数字 `798` 必须等于 `DCCXCVIII`

```javascript
tryCatch(convertToRoman(798) === "DCCXCVIII");
```

数字 `1000` 必须等于 `M`

```javascript
tryCatch(convertToRoman(1000) === "M");
```

数字 `3999` 必须等于 `MMMCMXCIX`

```javascript
tryCatch(convertToRoman(3999) === "MMMCMXCIX");
```

数字 `649` 必须等于 `DCXLIX`

```javascript
tryCatch(convertToRoman(649) === "DCXLIX");
```

数字 `1666` 必须等于 `MDCLXVI`

```javascript
tryCatch(convertToRoman(1666) === "MDCLXVI");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function convertToRoman(n) {
  var result = "";

  const values = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"]
  ];

  for (var i = 0; i < values.length; i++) {
    var value = values[i][0];
    var letter = values[i][1];

    while (n >= value) {
      result += letter;
      n -= value;
    }
  }

  return result;
}
```
