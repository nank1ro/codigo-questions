---
language: javascript
exerciseType: 1
difficulty: 1
title: 雨滴
---

# --description--

你的任务是将一个数字转换为包含与某些潜在因数对应的雨滴声的字符串。
因数是能够整除另一个数字且没有余数的数字。
测试一个数字是否是另一个数字的因数，最简单的方法是使用取模运算。
雨滴的规则如下：

- 如果3是因数，将 'Pling' 添加到结果中。
- 如果5是因数，将 'Plang' 添加到结果中。
- 如果7是因数，将 'Plong' 添加到结果中。
- 如果3、5或7都不是因数，结果应为该数字的数位。

# --instructions--

编写一个函数返回正确的字符串，示例：

- 28的因数有7，但没有3或5，所以结果是 `"Plong"`。
- 30的因数有3和5，但没有7，所以结果是 `"PlingPlang"`。
- 34不能被3、5或7整除，所以结果是 `"34"`。

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
function convert(number) {
  
}
```

# --asserts--

1的声音是 "1"

```javascript
tryCatch(convert(1) === "1");
```

3的声音是 "Pling"

```javascript
tryCatch(convert(3) === "Pling");
```

5的声音是 "Plang"

```javascript
tryCatch(convert(5) === "Plang");
```

7的声音是 "Plong"

```javascript
tryCatch(convert(7) === "Plong");
```

6的声音是 "Pling"

```javascript
tryCatch(convert(6) === "Pling");
```

8的声音是 "8"

```javascript
tryCatch(convert(8) === "8");
```

9的声音是 "Pling"

```javascript
tryCatch(convert(9) === "Pling");
```

10的声音是 "Plang"

```javascript
tryCatch(convert(10) === "Plang");
```

14的声音是 "Plong"

```javascript
tryCatch(convert(14) === "Plong");
```

15的声音是 "PlingPlang"

```javascript
tryCatch(convert(15) === "PlingPlang");
```

21的声音是 "PlingPlong"

```javascript
tryCatch(convert(21) === "PlingPlong");
```

25的声音是 "Plang"

```javascript
tryCatch(convert(25) === "Plang");
```

27的声音是 "Pling"

```javascript
tryCatch(convert(27) === "Pling");
```

35的声音是 "PlangPlong"

```javascript
tryCatch(convert(35) === "PlangPlong");
```

49的声音是 "Plong"

```javascript
tryCatch(convert(49) === "Plong");
```

52的声音是 "52"

```javascript
tryCatch(convert(52) === "52");
```

105的声音是 "PlingPlangPlong"

```javascript
tryCatch(convert(105) === "PlingPlangPlong");
```

3125的声音是 "Plang"

```javascript
tryCatch(convert(3125) === "Plang");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function convert(number) {
  var result = ""
  if (number % 3 == 0) {
    result += "Pling"
  }
  if (number % 5 == 0) {
    result += "Plang"
  }
  if (number % 7 == 0) {
    result += "Plong"
  }
  if (!result) {
    result = number.toString()
  }
  return result
}
```
