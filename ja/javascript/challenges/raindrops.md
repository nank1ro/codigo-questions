---
language: javascript
exerciseType: 1
difficulty: 1
title: 雨粒
---

# --description--

あなたのタスクは、特定の潜在的な因数に対応する雨粒の音を含む文字列に数値を変換することです。
因数とは、別の数値を均等に割り切れる数で、余りがありません。
ある数が別の数の因数であるかどうかをテストする最も簡単な方法は、剰余演算を使用することです。
雨粒のルールは以下の通りです：

- 3を因数に持つ場合、結果に'Pling'を追加します。
- 5を因数に持つ場合、結果に'Plang'を追加します。
- 7を因数に持つ場合、結果に'Plong'を追加します。
- 3、5、7のいずれも因数に持たない場合、結果はその数字そのものになります。

# --instructions--

正しい文字列を返す関数を書いてください。例：

- 28は7を因数に持ちますが、3や5は持たないので、結果は`"Plong"`になります。
- 30は3と5の両方を因数に持ちますが、7は持たないので、結果は`"PlingPlang"`になります。
- 34は3、5、7のいずれの因数も持たないので、結果は`"34"`になります。

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

1の音は"1"

```javascript
tryCatch(convert(1) === "1");
```

3の音は"Pling"

```javascript
tryCatch(convert(3) === "Pling");
```

5の音は"Plang"

```javascript
tryCatch(convert(5) === "Plang");
```

7の音は"Plong"

```javascript
tryCatch(convert(7) === "Plong");
```

6の音は"Pling"

```javascript
tryCatch(convert(6) === "Pling");
```

8の音は"8"

```javascript
tryCatch(convert(8) === "8");
```

9の音は"Pling"

```javascript
tryCatch(convert(9) === "Pling");
```

10の音は"Plang"

```javascript
tryCatch(convert(10) === "Plang");
```

14の音は"Plong"

```javascript
tryCatch(convert(14) === "Plong");
```

15の音は"PlingPlang"

```javascript
tryCatch(convert(15) === "PlingPlang");
```

21の音は"PlingPlong"

```javascript
tryCatch(convert(21) === "PlingPlong");
```

25の音は"Plang"

```javascript
tryCatch(convert(25) === "Plang");
```

27の音は"Pling"

```javascript
tryCatch(convert(27) === "Pling");
```

35の音は"PlangPlong"

```javascript
tryCatch(convert(35) === "PlangPlong");
```

49の音は"Plong"

```javascript
tryCatch(convert(49) === "Plong");
```

52の音は"52"

```javascript
tryCatch(convert(52) === "52");
```

105の音は"PlingPlangPlong"

```javascript
tryCatch(convert(105) === "PlingPlangPlong");
```

3125の音は"Plang"

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
