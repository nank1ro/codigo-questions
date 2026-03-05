---
language: javascript
exerciseType: 1
difficulty: 1
title: 2対1
---

# --description--

名前が与えられた場合、次のメッセージを含む文字列を返します：
`One for X, one for me.`
ここで`X`は与えられた名前です。
ただし、名前が指定されていない場合は、次の文字列を返します：
`One for you, one for me.`

# --instructions--

正しい文字列を返す関数を書いてください。例：

**入力**: `Walter`
**出力**: `One for Walter, one for me.`

**入力**:
**出力**: `One for you, one for me.`

**入力**: `David`
**出力**: `One for David, one for me.`

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
function twoForOne() {
  
}
```

# --asserts--

名前が指定されていない場合

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

名前として"James"を渡す

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

名前として"Martha"を渡す

```javascript
tryCatch(twoForOne("Martha") === "One for Martha, one for me.");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function twoForOne(name) {
  if (!name) return "One for you, one for me."
  return `One for ${name}, one for me.`
}
```
