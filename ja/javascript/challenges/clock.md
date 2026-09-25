---
language: javascript
exerciseType: 1
difficulty: 2
title: 時計
---

# --description--

24時間時計は、時刻を `HH:MM` の形で表します。真夜中の直後の `00:00` に始まり、次の真夜中の1分前の `23:59` で終わります。どちらの部分も常に2桁で書かれるため、午前11時9分は `11:09` と表示されます。

1日はちょうど1440分です。時計が `23:59` を過ぎると `00:00` に折り返して1日がまた始まり、逆に `00:00` より前へ巻き戻すと `23:59` に到達します。

# --instructions--

2つの整数 `hours` と `minutes` を受け取り、24時間時計の時刻を、両方の部分が2桁になるようゼロ埋めした文字列 `"HH:MM"` として返す関数 `clockTime` を書いてください。

例:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- どちらの数も、負の値や実際の時計が取りうる範囲を超える大きな値になることがあります。
- 合計分数を `hours * 60 + minutes` として求め、その合計を `0` から `1439` の範囲に折り返して、時計がどちらの方向にも巡るようにします。
- `clockTime(24, 0)` はちょうど1日なので、`"00:00"` と表示されます。

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

午前8時は `08:00` と表示される

```javascript
tryCatch(clockTime(8, 0) === "08:00");
```

1桁の数字は2桁になるようゼロ埋めされるため、午前11時9分は `11:09` と表示される

```javascript
tryCatch(clockTime(11, 9) === "11:09");
```

ちょうど1日分の時間は `00:00` に折り返される

```javascript
tryCatch(clockTime(24, 0) === "00:00");
```

60を超える分は時間の方へ繰り越される

```javascript
tryCatch(clockTime(25, 160) === "03:40");
```

負の時間は時計を真夜中より前へ巻き戻す

```javascript
tryCatch(clockTime(-1, 15) === "23:15");
```

負の分数も時計を巻き戻す

```javascript
tryCatch(clockTime(0, -90) === "22:30");
```

1日より多く巻き戻しても折り返しが続く

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
  // % keeps the sign of the left operand, so add a whole day before wrapping
  // again to land in 0..1439.
  const total = (((hours * 60 + minutes) % 1440) + 1440) % 1440;

  const hh = String(Math.floor(total / 60)).padStart(2, "0");
  const mm = String(total % 60).padStart(2, "0");
  return `${hh}:${mm}`;
}
```
