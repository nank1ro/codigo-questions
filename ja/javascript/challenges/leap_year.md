---
language: javascript
exerciseType: 1
difficulty: 3
title: うるう年
---

# --description--

暦年にはちょうど365.25日あります。しかし、最終的には人間は通常1の正確な割り切りで数え、小数点では数えないため、混乱を招きます。そこで、後者を避けるため、4年周期ごとに0.25日をすべて足し合わせ、その年を366日（閏日として2月29日を含む）とし、__うるう年__と呼ぶことにしました。4年周期の他の3年は365日のみで、__うるう年ではありません__。

# --instructions--

このチャレンジでは、`Date`クラス、`switch`文、__ifブロック__、__if-elseブロック__、__三項演算子__（`x ? a : b`）、論理演算子__AND__（`&&`）および__OR__（`||`）を使用せずに、うるう年かどうかを判定する必要があります。ただし、__NOT__（`!`）演算子は使用できます。

うるう年の場合は`true`を、そうでない場合は`false`を返してください。

関数呼び出しの例：
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

`Date`、`switch`、`if`、`else`、`&&`、`||`、`?`の使用は許可されていません。

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

`2016`年はうるう年です。

```javascript
tryCatch(leapYear(2016) == true);
```

`1996`年はうるう年です。

```javascript
tryCatch(leapYear(1996) == true);
```

`1600`年はうるう年です。

```javascript
tryCatch(leapYear(1600) == true);
```

`2020`年はうるう年です。

```javascript
tryCatch(leapYear(2020) == true);
```

`2000`年はうるう年です。

```javascript
tryCatch(leapYear(2000) == true);
```

`2008`年はうるう年です。

```javascript
tryCatch(leapYear(2008) == true);
```

`1521`年はうるう年ではありません。

```javascript
tryCatch(leapYear(1521) == false);
```

`1800`年はうるう年ではありません。

```javascript
tryCatch(leapYear(1800) == false);
```

`2007`年はうるう年ではありません。

```javascript
tryCatch(leapYear(2007) == false);
```

`2002`年はうるう年ではありません。

```javascript
tryCatch(leapYear(2002) == false);
```

`1979`年はうるう年ではありません。

```javascript
tryCatch(leapYear(1979) == false);
```

`2006`年はうるう年ではありません。

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
