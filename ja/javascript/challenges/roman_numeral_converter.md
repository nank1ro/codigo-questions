---
language: javascript
exerciseType: 1
difficulty: 3
title: ローマ数字変換器
---

# --description--

正の整数をパラメータとして受け取り、その整数のローマ数字表現を含む文字列を返す関数を作成してください。現代のローマ数字は、左端の桁から順に各桁を個別に表現し、値がゼロの桁はスキップして書きます。

# --instructions--

例：
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- すべてのローマ数字は大文字で返す必要があります。
- この表記法で表現できる最大の数は3,999です。

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

数値`2`は`II`でなければならない

```javascript
tryCatch(convertToRoman(2) === "II");
```

数値`12`は`XII`でなければならない

```javascript
tryCatch(convertToRoman(12) === "XII");
```

数値`16`は`XVI`でなければならない

```javascript
tryCatch(convertToRoman(16) === "XVI");
```

数値`44`は`XLIV`でなければならない

```javascript
tryCatch(convertToRoman(44) === "XLIV");
```

数値`68`は`LXVIII`でなければならない

```javascript
tryCatch(convertToRoman(68) === "LXVIII");
```

数値`400`は`CD`でなければならない

```javascript
tryCatch(convertToRoman(400) === "CD");
```

数値`798`は`DCCXCVIII`でなければならない

```javascript
tryCatch(convertToRoman(798) === "DCCXCVIII");
```

数値`1000`は`M`でなければならない

```javascript
tryCatch(convertToRoman(1000) === "M");
```

数値`3999`は`MMMCMXCIX`でなければならない

```javascript
tryCatch(convertToRoman(3999) === "MMMCMXCIX");
```

数値`649`は`DCXLIX`でなければならない

```javascript
tryCatch(convertToRoman(649) === "DCXLIX");
```

数値`1666`は`MDCLXVI`でなければならない

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
