---
language: javascript
exerciseType: 1
difficulty: 2
title: Luhnチェックサム
---

# --description--

Luhnアルゴリズムは、クレジットカード番号などの識別番号を検証するために使われるシンプルなチェックサムです。

数をチェックする前に、文字列からすべてのスペースを取り除きます。残った部分が1文字より長く、元の文字列が数字とスペースのみを含んでいる場合にのみ、その文字列は有効です。

チェックを行うには、一番右の桁から始めて左へ進み、1つおきの桁を2倍していきます。2倍した結果が9より大きい数になった場合は、そこから9を引きます。次にすべての桁を合計します。その合計が10で割り切れる場合にのみ、数は有効です。

たとえば、`"059"`は`0`、次に`5`を2倍した`10`が`1`になり、そして`9`となります。合計は`10`で10で割り切れるので、この数は有効です。

# --instructions--

文字列を受け取り、数が有効な場合には`true`を、そうでない場合には`false`を返す関数`isValid`を書いてください。

- `"4539 3195 0343 6467"`はチェックサムを満たすため、結果は`true`です。
- `"8273 1232 7352 0569"`はチェックサムを満たさないため、結果は`false`です。
- `"0"`は長さが1文字しかないため、結果は`false`です。
- `"055-444-285"`には数字でもスペースでもない文字が含まれているため、結果は`false`です。

関数呼び出しの例：
```javascript
console.log(isValid("095 245 88"));
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
function isValid(value) {
  
}
```

# --asserts--

1桁の数字は有効ではありません。

```javascript
tryCatch(isValid("0") === false);
```

先頭にスペースが付いた1桁の数字は有効ではありません。

```javascript
tryCatch(isValid(" 0") === false);
```

数`"059"`は有効です。

```javascript
tryCatch(isValid("059") === true);
```

数`"59"`は有効です。

```javascript
tryCatch(isValid("59") === true);
```

数`"055 444 285"`は有効です。

```javascript
tryCatch(isValid("055 444 285") === true);
```

数`"055 444 286"`は有効ではありません。

```javascript
tryCatch(isValid("055 444 286") === false);
```

数`"8273 1232 7352 0569"`は有効ではありません。

```javascript
tryCatch(isValid("8273 1232 7352 0569") === false);
```

数`"4539 3195 0343 6467"`は有効です。

```javascript
tryCatch(isValid("4539 3195 0343 6467") === true);
```

数`"1 2345 6789 1234 5678 9012"`は有効ではありません。

```javascript
tryCatch(isValid("1 2345 6789 1234 5678 9012") === false);
```

数`"095 245 88"`は有効です。

```javascript
tryCatch(isValid("095 245 88") === true);
```

英字が1つあるだけで数は無効になります。

```javascript
tryCatch(isValid("055a 444 285") === false);
```

ダッシュがあると数は無効になります。

```javascript
tryCatch(isValid("055-444-285") === false);
```

句読点があると数は無効になります。

```javascript
tryCatch(isValid(":9") === false);
```

記号があると数は無効になります。

```javascript
tryCatch(isValid("055# 444$ 285") === false);
```

空の文字列は有効ではありません。

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
