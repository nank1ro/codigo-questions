---
language: javascript
exerciseType: 1
difficulty: 3
title: 로마 숫자 변환기
---

# --description--

양의 정수를 매개변수로 받아 해당 정수의 로마 숫자 표현을 포함하는 문자열을 반환하는 함수를 만드세요. 현대 로마 숫자는 가장 왼쪽 자릿수부터 시작하여 각 자릿수를 별도로 표현하며, 값이 0인 자릿수는 건너뜁니다.

# --instructions--

예시:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- 모든 로마 숫자는 대문자로 반환되어야 합니다.
- 이 표기법으로 표현할 수 있는 가장 큰 숫자는 3,999입니다.

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

숫자 `2`는 `II`여야 합니다

```javascript
tryCatch(convertToRoman(2) === "II");
```

숫자 `12`는 `XII`여야 합니다

```javascript
tryCatch(convertToRoman(12) === "XII");
```

숫자 `16`은 `XVI`여야 합니다

```javascript
tryCatch(convertToRoman(16) === "XVI");
```

숫자 `44`는 `XLIV`여야 합니다

```javascript
tryCatch(convertToRoman(44) === "XLIV");
```

숫자 `68`은 `LXVIII`이어야 합니다

```javascript
tryCatch(convertToRoman(68) === "LXVIII");
```

숫자 `400`은 `CD`여야 합니다

```javascript
tryCatch(convertToRoman(400) === "CD");
```

숫자 `798`은 `DCCXCVIII`이어야 합니다

```javascript
tryCatch(convertToRoman(798) === "DCCXCVIII");
```

숫자 `1000`은 `M`이어야 합니다

```javascript
tryCatch(convertToRoman(1000) === "M");
```

숫자 `3999`는 `MMMCMXCIX`여야 합니다

```javascript
tryCatch(convertToRoman(3999) === "MMMCMXCIX");
```

숫자 `649`는 `DCXLIX`여야 합니다

```javascript
tryCatch(convertToRoman(649) === "DCXLIX");
```

숫자 `1666`은 `MDCLXVI`여야 합니다

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
